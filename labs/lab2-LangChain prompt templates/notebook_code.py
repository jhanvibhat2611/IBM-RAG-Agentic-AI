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