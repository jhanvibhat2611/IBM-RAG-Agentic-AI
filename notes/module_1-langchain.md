# Module 1 - LangChain

# What is LangChain?

LangChain is basically a Python framework that helps streamline the development of LLM-powered applications.

It makes it easier to integrate Large Language Models (LLMs) into AI applications without having to build everything from scratch.

One of its biggest strengths is that it can work with large amounts of data and generate concise, contextually relevant responses.

LangChain mainly helps with four things:

- Retrieval
- Extraction
- Processing
- Generation

---

# Why do developers like LangChain?

Some of the major benefits of LangChain are:

- Modularity
- Extensibility
- Decomposition capabilities
- Easy integration with vector databases

---

# 1. Modularity

LangChain follows a modular design.

Because of this, developers can build AI applications like building blocks, adding one component at a time instead of creating one huge application all at once.

This makes development much more organized and flexible.

---

# 2. Extensibility

Extensibility means it is easy to add new features or components to an existing LangChain application.

You don't have to rewrite a lot of code every time you want to add something new.

It also integrates well with external tools, APIs, and other systems.

---

# 3. Decomposition

One thing I found interesting is that LangChain kind of mimics how humans solve problems.

Instead of solving one huge complex problem at once, it breaks it down into smaller sub-problems.

Each smaller problem is solved separately, and then the results are combined.

Because of this, it is able to generate more accurate and contextually appropriate responses.

---

# 4. Vector Database Compatibility

LangChain works really well with vector databases.

Vector databases are mainly used for **semantic search**, where the search is based on meaning instead of exact keyword matching.

Since LLM applications often deal with huge amounts of data, LangChain and vector databases are commonly used together in AI applications.

---

# LangChain Expression Language (LCEL)

## What is LCEL?

LCEL stands for **LangChain Expression Language**.

It is basically a way of connecting different LangChain components using the **pipe (`|`) operator**.

Because of this, the flow of data becomes much cleaner and more readable.

---

## Basic Workflow

The basic workflow while using LCEL is:

1. Define a prompt template with variables inside curly braces `{}`.
2. Create a PromptTemplate instance.
3. Build a chain by connecting different components using the **pipe (`|`) operator**.
4. Invoke the chain by passing values for the variables in the prompt template.

---

# Runnables

In LangChain, **Runnables** are basically the building blocks used to create AI pipelines.

They provide a common interface for connecting different components such as:

- LLMs
- Retrievers
- Prompt Templates
- Output Parsers
- Other tools

Since every component follows the same interface, they can easily be connected together.

---

# Runnable Composition

There are two main ways of composing runnables.

## 1. RunnableSequence

As the name suggests, it connects components **sequentially**.

The output of one component becomes the input of the next component.

Example:

```
Prompt → LLM → Output Parser
```

---

## 2. RunnableParallel

Again, as the name suggests, multiple components run **in parallel**.

All of them receive the **same input** and execute simultaneously.

This is useful when we want multiple independent outputs from the same input.

---

# How LCEL helps

Normally, we would explicitly create a `RunnableSequence`.

With LCEL, we don't have to do that.

Instead, we simply connect components using the **pipe (`|`) operator**.

Example (conceptually):

```
Prompt | LLM | Output Parser
```

This is much cleaner and easier to read.

---

Another useful thing is that LCEL automatically converts compatible objects into Runnable components whenever possible.

Because of this, we usually don't have to manually convert everything ourselves.
