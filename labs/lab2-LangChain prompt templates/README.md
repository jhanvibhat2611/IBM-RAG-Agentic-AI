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