# In-Context Learning

In-context learning is basically a method of prompt engineering that does **not require any additional training or fine-tuning**.

Instead of training the model again, we simply **show it a few examples inside the prompt itself**.

So basically, the prompt not only contains the instruction but also demonstrates how the task should be done.

The model learns the new task from these examples during **inference time**, meaning while it is generating the response.

---

## Advantages

- Does not require fine-tuning.
- Saves time and computational resources.
- Usually improves performance because the model understands the pattern from the examples.

---

## Limitations

- It is limited by the context window. If too many examples are given, they won't fit into the prompt.
- It is not suitable for very complex tasks where the model actually needs to learn something new.

Some tasks require **gradient updates**, which means the model's internal parameters need to change. In-context learning cannot do that because it never changes the model itself.

---

# What are Prompts?

A prompt is simply the input that we give to an LLM.

It usually contains **instructions** and **context** so that the LLM can generate the desired output.

---

## Instructions

Instructions tell the LLM exactly what we want it to do.

The more specific the instructions are, the better the output is likely to be.

---

## Context

Context provides background information.

It helps the LLM understand the situation and generate a more relevant response instead of guessing.

---

# Prompt Engineering

Prompt engineering is basically the process of refining prompts so that they are more clear, concise, and specific.

The goal is to communicate with the LLM in the best possible way so that it gives accurate and contextually appropriate responses.

---

# Why do we need Prompt Engineering?

Prompt engineering is important because the quality of the prompt directly affects the quality of the response.

A well-written prompt can:

- Improve accuracy.
- Produce more contextually appropriate responses.
- Better satisfy the user's needs.
- Reduce the need for continual fine-tuning.

---

# Elements of a Prompt

## 1. Instructions

Tell the LLM exactly what task needs to be performed.

---

## 2. Context

Provides the background or scenario related to the task.

---

## 3. Input Data

The actual data that the LLM needs to process.

---

## 4. Output Indicator

Specifies where or in what format the response should be generated.

---

## Example

### Instruction

Classify the following customer review as **Positive**, **Negative**, or **Neutral**.

### Context

This review is part of the feedback collected for a recently launched product.

### Input Data

"The product arrived late, but the quality exceeded my expectations."

### Output Indicator

Sentiment:

---

# Advanced Prompt Engineering Techniques

## 1. Zero-Shot Prompting

Zero-shot prompting is when we ask an LLM to perform a task **without giving it any examples** related to that task.

The model relies only on the knowledge it has already learned during training.

### Example

Instruction:

> Classify the following statement as True or False.

Statement:

> India Gate is located in Bihar.

The LLM is expected to answer correctly without being shown any similar examples beforehand.

---

## 2. One-Shot Prompting

As the name suggests, one-shot prompting provides **one example** before asking the actual question.

The example helps the LLM understand the pattern that it needs to follow.

### Example

English: Good morning.

French: Bonjour.

Now translate:

English: Thank you.

The LLM uses the single example to understand what it is expected to do.

---

## 3. Few-Shot Prompting

Few-shot prompting is similar to one-shot prompting, except that we provide **multiple examples** instead of just one.

The LLM learns the pattern from these examples and then applies the same pattern to the new input.

Generally, few-shot prompting performs better than one-shot prompting because the model has more examples to learn from.

---

## 4. Chain of Thought (CoT) Prompting

Chain of Thought prompting guides the LLM to solve a problem **step by step**, similar to how a human would think through a complex problem.

Instead of directly asking for the final answer, we encourage the model to explain its reasoning before reaching the conclusion.

This technique is especially useful for complex reasoning tasks and multi-step problems.

---

## 5. Self-Consistency

Self-consistency is used to improve the **accuracy and reliability** of the final answer.

Instead of generating only one solution, we ask the LLM to generate **multiple independent reasoning paths** for the same question.

The final answer is then selected based on the most consistent result among those different reasoning paths.

This increases confidence that the answer is correct.

---

# Prompt Templates (LangChain)

LangChain provides **Prompt Templates**, which are basically predefined templates for generating effective prompts.

Instead of writing the entire prompt every time, we create a template with placeholders that can be replaced later.

This helps us generate multiple prompts while keeping the overall structure the same.

Prompt templates can include:

- Instructions
- Context
- Few-shot examples
- Variables (placeholders)

### Example

Template:

```
Tell me a {adjective} joke about {topic}.
```

Here,

- `{adjective}` is a variable.
- `{topic}` is another variable.

When formatting the prompt, we can replace these placeholders with different values.

Example:

```
Tell me a funny joke about programming.

Tell me a dark joke about football.

Tell me a sarcastic joke about AI.
```

The structure of the prompt remains the same, while the variables change depending on the situation.