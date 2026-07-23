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