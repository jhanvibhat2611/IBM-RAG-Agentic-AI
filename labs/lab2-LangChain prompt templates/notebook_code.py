from idlelib.outwin import OutputWindow

template = """Tell me a {adjective} joke about {content}.
"""
prompt = PromptTemplate.from_template(template)
prompt

# Output
# PromptTemplate(input_variables=['adjective', 'content'], template='Tell me a {adjective} joke about {content}.\n')

prompt.format(adjective="funny", content="chickens")

# Output
# 'Tell me a funny joke about chickens.\n'

from langchain_core.runnables import RunnableLambda

# Define a function to ensure proper formatting
def format_prompt(variables):
    return prompt.format(**variables)

# Create the chain with explicit formatting
joke_chain = (
    RunnableLambda(format_prompt)
    | llm
    | StrOutputParser()
)

# Run the chain
response = joke_chain.invoke({"adjective": "funny", "content": "chickens"})
print(response)

# Output
# Why did the chicken cross the road? To prove to the possum that it could be done!

content = """
    The rapid advancement of technology in the 21st century has transformed various industries, including healthcare, education, and transportation. 
    Innovations such as artificial intelligence, machine learning, and the Internet of Things have revolutionized how we approach everyday tasks and complex problems. 
    For instance, AI-powered diagnostic tools are improving the accuracy and speed of medical diagnoses, while smart transportation systems are making cities more efficient and reducing traffic congestion. 
    Moreover, online learning platforms are making education more accessible to people around the world, breaking down geographical and financial barriers. 
    These technological developments are not only enhancing productivity but also contributing to a more interconnected and informed society.
"""

template = """Summarize the {content} in one sentence.
"""
prompt = PromptTemplate.from_template(template)

# Create the LCEL chain
summarize_chain = (
    RunnableLambda(format_prompt)
    | llm
    | StrOutputParser()
)

# Run the chain
summary = summarize_chain.invoke({"content": content})
print(summary)

# Output
# The rapid advancement of technology, including AI, machine learning, and IoT, has transformed healthcare, education,
# and transportation, enhancing productivity and fostering a more interconnected society.

content = """
    The solar system consists of the Sun, eight planets, their moons, dwarf planets, and smaller objects like asteroids and comets. 
    The inner planets—Mercury, Venus, Earth, and Mars—are rocky and solid. 
    The outer planets—Jupiter, Saturn, Uranus, and Neptune—are much larger and gaseous.
"""

question = "Which planets in the solar system are rocky and solid?"

template = """
    Answer the {question} based on the {content}.
    Respond "Unsure about answer" if not sure about the answer.

    Answer:

"""
prompt = PromptTemplate.from_template(template)

# Create the LCEL chain
qa_chain = (
        RunnableLambda(format_prompt)
        | llm
        | StrOutputParser()
)

# Run the chain
answer = qa_chain.invoke({"question": question, "content": content})
print(answer)

# Output
# The rocky, solid planets in our solar system are Mercury, Venus, Earth, and Mars.

text = """
    The concert last night was an exhilarating experience with outstanding performances by all artists.
"""

categories = "Entertainment, Food and Dining, Technology, Literature, Music."

template = """
    Classify the {text} into one of the {categories}.

    Category:

"""
prompt = PromptTemplate.from_template(template)

# Create the LCEL chain
classification_chain = (
        RunnableLambda(format_prompt)
        | llm
        | StrOutputParser()
)

# Run the chain
category = classification_chain.invoke({"text": text, "categories": categories})
print(category)

# Output
# Music