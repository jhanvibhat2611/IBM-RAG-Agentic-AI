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

description = """
    Retrieve the names and email addresses of all customers from the 'customers' table who have made a purchase in the last 30 days. 
    The table 'purchases' contains a column 'purchase_date'
"""

template = """
    Generate an SQL query based on the {description}

    SQL Query:

"""
prompt = PromptTemplate.from_template(template)

# Create the LCEL chain
sql_generation_chain = (
        RunnableLambda(format_prompt)
        | llm
        | StrOutputParser()
)

# Run the chain
sql_query = sql_generation_chain.invoke({"description": description})
print(sql_query)

# Output
# SELECT c.name, c.email
#     FROM customers c
#     JOIN purchases p ON c.customer_id = p.customer_id
#     WHERE p.purchase_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
#     """
#
#     # Execute the SQL query
#     cursor.execute(query)
#
#     # Fetch all the results
#     results = cursor.fetchall()
#
#     # Close the cursor and connection
#     cursor.close()
#     connection.close()
#
#     return results
#
# # Example usage
# # Assuming 'your_database_name' is the name of your database
# customers_with_recent_purchases = get_customers_with_recent_purchases('your_database_name')
# for customer in customers_with_recent_purchases:
#     print(customer)
# ```

role = """
    Dungeon & Dragons game master
"""

tone = "engaging and immersive"

template = """
    You are an expert {role}. I have this question {question}. I would like our conversation to be {tone}.

    Answer:

"""
prompt = PromptTemplate.from_template(template)

# Create the LCEL chain
roleplay_chain = (
        RunnableLambda(format_prompt)
        | llm
        | StrOutputParser()
)

# Create an interactive chat loop
while True:
    query = input("Question: ")

    if query.lower() in ["quit", "exit", "bye"]:
        print("Answer: Goodbye!")
        break

    response = roleplay_chain.invoke({"role": role, "question": query, "tone": tone})
    print("Answer: ", response)
# Output
# Question:  Where are you from
# Answer:      I hail from the mystical realm of Eldoria, a land of magic and wonder, where dragons soar through the skies and ancient forests whisper secrets of long-forgotten lore. My journey has taken me across countless realms, from the bustling streets of Waterdeep to the treacherous depths of the Underdark. I have faced formidable foes and forged unbreakable alliances, all in the name of adventure and the pursuit of knowledge. Now, I find myself in your world, ready to share my tales and guide you through the trials and triumphs that await in the realm of Dungeons & Dragons. So, my friend, what brings you to this crossroads of fate?
# Question:  woah I would like to know about my ancestor, the great queen of perdoria
# Answer:      *clears throat and speaks in a dramatic, mythical tone* Greetings, adventurer! You have come seeking knowledge about the legendary Queen of Perdoria, a tale as old as the realm itself. Very well, let us embark on this journey together and uncover the secrets of your esteemed ancestor. But first, tell me, what is your name, brave soul? For in the grand tapestry of Perdoria, every hero's name is woven with care.
# Question:  katherine