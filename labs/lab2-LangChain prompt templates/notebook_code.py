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