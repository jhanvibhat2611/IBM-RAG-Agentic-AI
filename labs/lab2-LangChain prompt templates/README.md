# PromptTemplate in LangChain

## Objective

Understand how LangChain's `PromptTemplate` helps create dynamic and reusable prompts by replacing variables with actual values at runtime.

Instead of writing a new prompt every time, we define a template once and fill in the required values whenever needed.

---

# Why do we need PromptTemplate?

Suppose we want to ask the LLM:

```
Tell me a funny joke about chickens.
```

Later we want:

```
Tell me a scary joke about ghosts.
```

Then:

```
Tell me a short joke about programmers.
```

Without PromptTemplate, we would have to rewrite the entire prompt every time.

Instead, we create a template with placeholders, and LangChain automatically replaces those placeholders with the values we provide.

This makes prompts reusable, cleaner, and much easier to maintain.

---

# Overall Workflow

Template with Variables
        │
        ▼
Create PromptTemplate
        │
        ▼
Provide Input Values
        │
        ▼
Replace Variables
        │
        ▼
Final Prompt
        │
        ▼
Send to LLM

---

# Code Walkthrough

## 1. Define the Template

```python
template = """
Tell me a {adjective} joke about {content}.
"""
```

### What does this do?

This creates a prompt template.

The words inside curly braces are **placeholders (variables)**.

Here we have:

- `{adjective}`
- `{content}`

These values are not fixed yet. They will be supplied later.

---

## 2. Create the PromptTemplate

```python
prompt = PromptTemplate.from_template(template)
```

### What does this do?

LangChain converts the string into a `PromptTemplate` object.

It automatically detects the variables inside the template.

If you print it,

```python
print(prompt)
```

you'll get something like

```python
PromptTemplate(
    input_variables=['adjective', 'content'],
    template='Tell me a {adjective} joke about {content}.'
)
```

This tells us:

- the template being used
- which variables need values before the prompt can be sent to the LLM

---

## 3. Format the Prompt

```python
prompt.format(
    adjective="funny",
    content="chickens"
)
```

### What does this do?

LangChain replaces the placeholders with the provided values.

---

# Output

```
Tell me a funny joke about chickens.
```

This final prompt is now ready to be sent to the language model.

---

# What is happening internally?

Before formatting

```
Tell me a {adjective} joke about {content}.
```

↓

After formatting

```
Tell me a funny joke about chickens.
```

The placeholders are replaced with actual values while the rest of the prompt remains unchanged.

---

# Why is PromptTemplate useful?

- Avoids rewriting similar prompts.
- Makes prompts reusable.
- Makes code cleaner and easier to maintain.
- Reduces typing errors.
- Makes it easy to generate many prompts using the same structure.
- Very useful when building larger LangChain applications.

---

# Key Takeaways

- `PromptTemplate` creates reusable prompts.
- Variables are written inside `{}`.
- `PromptTemplate.from_template()` converts a string into a PromptTemplate object.
- `.format()` replaces the variables with actual values.
- The formatted prompt is then sent to the LLM.

# Building a PromptTemplate Chain with LCEL

## Objective

Understand how LangChain combines PromptTemplate, RunnableLambda, an LLM, and an Output Parser into a reusable pipeline using LCEL (LangChain Expression Language).

Instead of manually formatting the prompt and calling the LLM every time, we create a chain that performs the entire workflow automatically.

---

# Overall Workflow

Input Variables (Dictionary)
        │
        ▼
RunnableLambda
(format_prompt)
        │
        ▼
PromptTemplate
(Fill placeholders)
        │
        ▼
Formatted Prompt
        │
        ▼
LLM
(Generate response)
        │
        ▼
StrOutputParser
(Convert output to string)
        │
        ▼
Final Response

---

# Code Walkthrough

## 1. Creating a Helper Function

```python
def format_prompt(variables):
    return prompt.format(**variables)
```

### What does this do?

This helper function formats the prompt by replacing all placeholders with the values provided in a dictionary.

Instead of writing:

```python
prompt.format(
    adjective="funny",
    content="chickens"
)
```

we simply pass

```python
{
    "adjective":"funny",
    "content":"chickens"
}
```

The `**` operator unpacks the dictionary into keyword arguments before calling `prompt.format()`.

---

## 2. RunnableLambda

```python
RunnableLambda(format_prompt)
```

### What does this do?

`RunnableLambda` converts a normal Python function into a Runnable object.

Since LCEL chains work with Runnable components, wrapping the function allows it to become part of the processing pipeline.

---

## 3. Building the Chain

```python
joke_chain = (

    RunnableLambda(format_prompt)

    |

    llm

    |

    StrOutputParser()

)
```

### What does this do?

The pipe operator (`|`) connects components together.

The output of one component automatically becomes the input of the next component.

Pipeline:

```
Input Dictionary

↓

Prompt Formatting

↓

LLM

↓

Output Parser

↓

Final Response
```

---

## 4. StrOutputParser

```python
StrOutputParser()
```

### What does this do?

The LLM may return a structured response object.

`StrOutputParser()` extracts only the generated text and converts it into a normal Python string.

---

## 5. Running the Chain

```python
response = joke_chain.invoke({

    "adjective":"funny",

    "content":"chickens"

})
```

### What does this do?

The input variables are passed to the chain.

The chain automatically:

- formats the prompt,
- sends it to the LLM,
- parses the response,
- returns the final output.

No manual formatting or LLM call is required.

---

## Reusing the Same Chain

```python
response = joke_chain.invoke({

    "adjective":"sad",

    "content":"fish"

})
```

Only the input variables change.

The PromptTemplate, pipeline, and LLM remain exactly the same.

This makes the chain highly reusable.

---

# Why use LCEL?

Without LCEL:

```
Create Prompt

↓

Format Prompt

↓

Call LLM

↓

Extract Response
```

Every step must be written manually.

With LCEL:

```
Input Variables

↓

invoke()

↓

Everything happens automatically
```

The chain manages the complete workflow.

---

# Key Takeaways

- `RunnableLambda` converts a Python function into a Runnable component.
- `format_prompt()` formats the PromptTemplate using a dictionary of variables.
- The pipe operator (`|`) connects multiple components into a single workflow.
- `StrOutputParser()` converts the LLM output into a plain string.
- `invoke()` executes the entire chain from start to finish using only the input variables.

---

# Example: Text Summarization using PromptTemplate + LCEL

## Objective

Use the same PromptTemplate and LCEL pipeline to summarize a long paragraph into a single sentence.

Instead of changing the chain itself, only the prompt template and input data are changed.

---

## Code Walkthrough

### 1. Store the Input Text

```python
content = """
Long paragraph...
"""
```

### What does this do?

The paragraph that needs to be summarized is stored in a variable.

Keeping the text inside a variable makes it reusable. Instead of rewriting the prompt every time, we can simply replace the value of `content`.

---

### 2. Create the Prompt Template

```python
template = """
Summarize the {content} in one sentence.
"""
```

### What does this do?

The prompt tells the LLM what task it needs to perform.

`{content}` is a placeholder that will later be replaced with the actual paragraph.

---

### 3. Convert it into a PromptTemplate

```python
prompt = PromptTemplate.from_template(template)
```

### What does this do?

This converts the normal string into a reusable PromptTemplate.

Instead of hardcoding the paragraph, the template accepts different input values whenever it is used.

---

### 4. Build the LCEL Chain

```python
summarize_chain = (

    RunnableLambda(format_prompt)

    |

    llm

    |

    StrOutputParser()

)
```

### What does this do?

The chain connects three components:

- `RunnableLambda` formats the prompt.
- `llm` generates the summary.
- `StrOutputParser()` converts the LLM response into a plain string.

The pipe operator (`|`) automatically passes the output of one component as the input of the next.

---

### 5. Execute the Chain

```python
summary = summarize_chain.invoke({
    "content": content
})
```

### What does this do?

The dictionary provides the value for the `{content}` placeholder.

The chain then automatically:

- formats the prompt,
- sends it to the LLM,
- generates the summary,
- returns the final output.

---

## Overall Workflow

```
Long Paragraph

↓

PromptTemplate

↓

Formatted Prompt

↓

LLM

↓

Generated Summary

↓

Output Parser

↓

Final One-Sentence Summary
```

---

## Key Takeaways

- PromptTemplates are reusable for different NLP tasks.
- Only the input data changes; the LCEL pipeline remains the same.
- Long text is stored separately from the prompt, making the code cleaner.
- The same LangChain workflow can be used for summarization, translation, classification, question answering, and many other tasks simply by changing the prompt template.

---

# Example: Question Answering using PromptTemplate + LCEL

## Objective

Build a simple Question Answering (QA) pipeline where the LLM answers a question **only using the provided context**.

Unlike a normal prompt where the model can answer from its general knowledge, this prompt explicitly instructs the model to use the given content. If the answer cannot be found in the content, the model should respond with **"Unsure about answer"**.

---

## Code Walkthrough

### 1. Store the Context

```python
content = """
The solar system consists of...
"""
```

### What does this do?

The information that the LLM should use is stored inside the `content` variable.

Instead of embedding the paragraph directly inside the prompt, it is stored separately so that different documents can be passed later without changing the prompt itself.

---

### 2. Store the Question

```python
question = "Which planets in the solar system are rocky and solid?"
```

### What does this do?

The user's question is stored separately.

Keeping the question as a variable allows the same prompt template to answer different questions by simply changing the value of `question`.

---

### 3. Create the Prompt Template

```python
template = """
Answer the {question} based on the {content}.

Respond "Unsure about answer" if not sure about the answer.

Answer:
"""
```

### What does this do?

This template defines the instructions that the LLM should follow.

It contains two placeholders:

- `{question}` → the user's question.
- `{content}` → the context the model should use.

The prompt also tells the LLM **not to guess**. If the answer is not present in the provided context, it should return **"Unsure about answer"** instead of making up information.

This is a simple way to reduce hallucinations.

---

### 4. Convert to a PromptTemplate

```python
prompt = PromptTemplate.from_template(template)
```

### What does this do?

This converts the normal string into a reusable PromptTemplate.

Whenever new values for `question` and `content` are provided, LangChain automatically replaces the placeholders.

---

### 5. Create the LCEL Chain

```python
qa_chain = (

    RunnableLambda(format_prompt)

    |

    llm

    |

    StrOutputParser()

)
```

### What does this do?

The chain has three stages:

- **RunnableLambda(format_prompt)** → replaces the placeholders with actual values.
- **llm** → sends the completed prompt to the language model.
- **StrOutputParser()** → converts the model output into a plain Python string.

The pipe operator (`|`) automatically passes the output from one component to the next.

---

### 6. Run the Chain

```python
answer = qa_chain.invoke({
    "question": question,
    "content": content
})
```

### What does this do?

The dictionary provides values for both placeholders.

The pipeline then:

- formats the prompt,
- inserts the question and context,
- sends the prompt to the LLM,
- generates an answer,
- returns the final response.

---

## Overall Workflow

```

Context

+

Question

↓

PromptTemplate

↓

Formatted Prompt

↓

LLM

↓

Answer

↓

Output Parser

↓

Final Response

```

---

## Why is this important?

This is one of the simplest forms of **context-aware question answering**.

Instead of answering from everything the model knows, we first provide the information that the model is allowed to use.

Although this example uses a small paragraph, the same workflow is later used in **Retrieval-Augmented Generation (RAG)**, where the `content` is retrieved from documents or a vector database before being passed to the LLM.

---

## Key Takeaways

- Store the context separately from the prompt.
- Store the question separately so the same template can answer multiple questions.
- PromptTemplate automatically fills the placeholders.
- LCEL connects formatting, the LLM, and output parsing into one pipeline.
- Asking the model to respond with **"Unsure about answer"** helps reduce hallucinations by preventing unsupported answers.

---

# Example: Text Classification using PromptTemplate + LCEL

## Objective

Build a text classification pipeline that classifies a piece of text into one of the given categories.

The same PromptTemplate + LCEL workflow is reused. Only the prompt and the input variables are different.

---

## Code Walkthrough

### 1. Store the Text

```python
text = """
The concert last night was an exhilarating experience with outstanding performances by all artists.
"""
```

### What does this do?

This variable stores the text that needs to be classified.

Instead of embedding the sentence directly into the prompt, it is stored separately so different inputs can be classified without modifying the template.

---

### 2. Store the Categories

```python
categories = "Entertainment, Food and Dining, Technology, Literature, Music."
```

### What does this do?

This variable contains all the possible categories that the model can choose from.

Providing the categories guides the LLM and limits the possible outputs.

---

### 3. Create the Prompt Template

```python
template = """
Classify the {text} into one of the {categories}.

Category:
"""
```

### What does this do?

The PromptTemplate defines the task for the LLM.

It contains two placeholders:

- `{text}` → the sentence to classify.
- `{categories}` → the list of possible categories.

When the chain runs, LangChain automatically replaces these placeholders with the provided values.

---

### 4. Convert to a PromptTemplate

```python
prompt = PromptTemplate.from_template(template)
```

### What does this do?

This converts the normal string into a reusable PromptTemplate.

The same template can now classify any text by simply changing the values of `text` or `categories`.

---

### 5. Create the LCEL Chain

```python
classification_chain = (

    RunnableLambda(format_prompt)

    |

    llm

    |

    StrOutputParser()

)
```

### What does this do?

The LCEL chain consists of three components:

- **RunnableLambda(format_prompt)** → fills the placeholders in the prompt.
- **llm** → processes the formatted prompt and predicts the category.
- **StrOutputParser()** → converts the model output into a plain string.

The pipe operator (`|`) automatically passes the output of one component to the next.

---

### 6. Execute the Chain

```python
category = classification_chain.invoke({
    "text": text,
    "categories": categories
})
```

### What does this do?

The input values are passed as a dictionary.

LangChain automatically:

- replaces the placeholders,
- sends the completed prompt to the LLM,
- generates the predicted category,
- returns the final output.

---

## Overall Workflow

```

Input Text

+

Possible Categories

↓

PromptTemplate

↓

Formatted Prompt

↓

LLM

↓

Predicted Category

↓

Output Parser

↓

Final Response

```

---

## Why is this useful?

Classification is one of the most common NLP tasks.

Instead of writing separate code for every classification problem, the same PromptTemplate and LCEL pipeline can be reused simply by changing:

- the input text,
- the available categories,
- or the prompt instructions.

The pipeline remains exactly the same.

---

## Key Takeaways

- Store the input text separately from the prompt.
- Store the possible categories separately so they can be changed easily.
- PromptTemplate automatically inserts the variables into the prompt.
- LCEL connects prompt formatting, the LLM, and output parsing into a single workflow.
- The same pipeline can classify different types of text by changing only the inputs, making the code reusable and modular.

---

# Example: SQL Query Generation using PromptTemplate + LCEL

## Objective

Generate an SQL query from a natural language description.

Instead of manually writing SQL, we describe what we want in plain English, and the LLM converts it into the corresponding SQL query.

---

## Code Walkthrough

### 1. Store the Query Description

```python
description = """
Retrieve the names and email addresses of all customers from the 'customers' table who have made a purchase.
The table 'purchases' contains a column 'purchase_date'.
"""
```

### What does this do?

The task is described in natural language.

Instead of writing SQL ourselves, we explain what data we want to retrieve.

This description becomes the input for the LLM.

---

### 2. Create the Prompt Template

```python
template = """
Generate an SQL query based on the {description}

SQL Query:
"""
```

### What does this do?

The PromptTemplate tells the LLM exactly what task it should perform.

It contains one placeholder:

- `{description}` → the natural language description of the required SQL query.

Whenever a different description is provided, LangChain automatically inserts it into the prompt.

---

### 3. Convert to a PromptTemplate

```python
prompt = PromptTemplate.from_template(template)
```

### What does this do?

This converts the template string into a reusable PromptTemplate.

The same template can generate SQL for many different database queries by simply changing the value of `description`.

---

### 4. Create the LCEL Chain

```python
sql_generation_chain = (

    RunnableLambda(format_prompt)

    |

    llm

    |

    StrOutputParser()

)
```

### What does this do?

The LCEL chain connects three components:

- **RunnableLambda(format_prompt)** → fills the `{description}` placeholder.
- **llm** → generates the SQL query.
- **StrOutputParser()** → converts the model output into a plain string.

Each component passes its output to the next using the pipe operator (`|`).

---

### 5. Execute the Chain

```python
sql_query = sql_generation_chain.invoke({
    "description": description
})
```

### What does this do?

The description is passed to the PromptTemplate.

The pipeline then:

- formats the prompt,
- sends it to the LLM,
- generates an SQL query,
- returns the final SQL statement.

---

## Overall Workflow

```
Natural Language Description

↓

PromptTemplate

↓

Formatted Prompt

↓

LLM

↓

Generated SQL Query

↓

Output Parser

↓

Final SQL Statement
```

---

## Why is this useful?

Many users know **what information they need** but don't know SQL syntax.

Instead of writing SQL manually, they can simply describe the required data in plain English.

The LLM then converts the natural language request into an SQL query, making database interaction much easier.

This is commonly used in AI-powered database assistants and analytics tools.

---

## Key Takeaways

- Natural language is used instead of manually writing SQL.
- PromptTemplate makes the solution reusable for different database queries.
- LCEL handles prompt formatting, LLM execution, and output parsing in one pipeline.
- The same workflow can generate different SQL queries simply by changing the description.

---

# Example: Role-Based Chatbot using PromptTemplate + LCEL

## Objective

Build an interactive chatbot where the LLM behaves as a specific role or persona.

Instead of only asking a question, we also specify:

- **who the LLM should act as**
- **how it should respond**

This allows us to reuse the same chatbot for different applications simply by changing the role or tone.

---

## Code Walkthrough

### 1. Define the Role

```python
role = """
Dungeon & Dragons game master
"""
```

### What does this do?

This variable defines the **persona** the LLM should adopt.

Instead of answering as a generic AI assistant, the model will answer as a Dungeon & Dragons game master.

Changing this variable changes the chatbot's behavior without changing the rest of the code.

Examples:

- Python Tutor
- Career Advisor
- Doctor
- Interviewer
- Travel Guide

---

### 2. Define the Tone

```python
tone = "engaging and immersive"
```

### What does this do?

The tone specifies **how** the model should communicate.

It doesn't change the knowledge of the model—it changes the style of the response.

Examples:

- Professional
- Friendly
- Formal
- Humorous
- Motivational

---

### 3. Create the Prompt Template

```python
template = """
You are an expert {role}.

I have this question {question}.

I would like our conversation to be {tone}.

Answer:
"""
```

### What does this do?

This PromptTemplate combines three pieces of information:

- `{role}` → Who the LLM should act as.
- `{question}` → The user's input.
- `{tone}` → The communication style.

Every time the chatbot is used, these placeholders are automatically replaced with the provided values.

---

### 4. Convert to a PromptTemplate

```python
prompt = PromptTemplate.from_template(template)
```

### What does this do?

This converts the template into a reusable PromptTemplate.

Now the chatbot can easily switch roles or tones without rewriting the prompt.

---

### 5. Create the LCEL Chain

```python
roleplay_chain = (

    RunnableLambda(format_prompt)

    |

    llm

    |

    StrOutputParser()

)
```

### What does this do?

The chain connects three components:

- **RunnableLambda(format_prompt)** → fills the placeholders.
- **llm** → generates the response.
- **StrOutputParser()** → converts the output into a plain string.

The pipe operator (`|`) automatically passes the output of one component to the next.

---

### 6. Create an Interactive Chat Loop

```python
while True:
```

### What does this do?

The chatbot keeps running continuously.

Instead of asking only one question, it allows the user to keep chatting until they decide to exit.

---

### 7. Read User Input

```python
query = input("Question: ")
```

### What does this do?

This waits for the user to type a question.

The question is stored in the `query` variable and will replace the `{question}` placeholder in the PromptTemplate.

---

### 8. Exit the Chat

```python
if query.lower() in ["quit", "exit", "bye"]:
    print("Answer: Goodbye!")
    break
```

### What does this do?

Checks whether the user wants to end the conversation.

If the input is:

- quit
- exit
- bye

the loop stops and the chatbot exits gracefully.

---

### 9. Invoke the Chain

```python
response = roleplay_chain.invoke({
    "role": role,
    "question": query,
    "tone": tone
})
```

### What does this do?

The values are passed as a dictionary.

LangChain automatically:

- replaces the placeholders,
- creates the final prompt,
- sends it to the LLM,
- generates the response,
- returns the final answer.

---

### 10. Print the Response

```python
print("Answer:", response)
```

### What does this do?

Displays the chatbot's generated response to the user.

The loop then starts again, allowing another question to be asked.

---

## Overall Workflow

```
Role

+

Tone

+

User Question

↓

PromptTemplate

↓

Formatted Prompt

↓

LLM

↓

Generated Response

↓

Output Parser

↓

Displayed to User

↓

Wait for Next Question
```

---

## Why is this useful?

This is one of the simplest ways to build a conversational AI assistant.

Instead of hardcoding different chatbots, we simply change:

- the role,
- the tone,
- or the prompt,

while keeping the same LCEL pipeline.

This makes the chatbot flexible and reusable for many different applications.

---

## Key Takeaways

- PromptTemplates can define the LLM's role or persona.
- Tone controls the style of the response without changing the model itself.
- LCEL connects prompt formatting, the LLM, and output parsing into a reusable pipeline.
- The chatbot runs continuously using a `while` loop until the user exits.
- The same chatbot can become a tutor, interviewer, travel guide, coding assistant, or customer support agent simply by changing the role and tone.

