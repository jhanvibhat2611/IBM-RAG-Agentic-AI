# Module 1 - Natural Language Processing (NLP)

## What is NLP?

NLP (Natural Language Processing) is basically the process of moving between **unstructured data** and **structured data**.

### Unstructured Data

Unstructured data is the natural language that we use every day. Humans understand it naturally, but computers do not.

### Structured Data

Structured data is data that is organized in a format that computers can easily understand and process.

---

## NLU (Natural Language Understanding)

Natural Language Understanding (NLU) converts **unstructured data → structured data**.

For example:

Input:

> Add eggs and milk to my shopping list.

Structured output could look something like:

Shopping List

- Eggs
- Milk

---

## NLG (Natural Language Generation)

Natural Language Generation (NLG) converts **structured data → natural language**.

It takes structured information and generates human-readable text.

---

# Why do we need NLP?

One of the biggest reasons is **context**.

For example, if a sentence is translated from English to another language and then translated back to English, the meaning can change.

NLP tries to preserve the intended meaning by understanding context instead of just translating words literally.

---

# Applications of NLP

NLP is used in:

- Machine Translation
- Virtual Assistants
- Chatbots
- Sentiment Analysis
- Many other language-based AI applications

NLP is not a single algorithm.

It is more like a collection (or bag) of different tools and techniques that work together to solve language-related problems.

---

# NLP Pipeline

## Step 1 - Tokenization

Tokenization means breaking a sentence or string into multiple smaller pieces called **tokens**.

After tokenization, we can process each token individually.

---

## Step 2 - Stemming

Stemming is used to normalize words by removing prefixes or suffixes and reducing them to a base form.

However, it is not always reliable because it simply cuts words without understanding their meaning.

For example, words like **university** and **universe** are different words even though they look similar.

---

## Step 3 - Lemmatization

Lemmatization is a better approach.

Instead of simply cutting the word, it looks up the word in a dictionary and finds its correct root word based on its meaning.

Because of this, it is generally more accurate than stemming.

---

## Step 4 - Part of Speech (POS) Tagging

Part of Speech Tagging identifies the role of each word in a sentence.

For example, it determines whether a word is:

- Noun
- Verb
- Adjective
- Adverb
- etc.

This information helps the model understand the sentence more accurately.

---

## Step 5 - Named Entity Recognition (NER)

Named Entity Recognition identifies important entities in a sentence.

For example, it can recognize:

- Person
- Organization
- Location
- Date
- Money
- and other important entities.

---

After the text has been converted into structured data using all these NLP techniques, it becomes much easier for AI models and applications to process and use it.