# Lab 01 - Master Prompt Engineering and LangChain PromptTemplates

## Objective

Understand how an LLM generates text and how generation parameters influence the model's output.

---

# Overall Flow

User Prompt
        │
        ▼
Generation Parameters
        │
        ▼
IBM Granite LLM
        │
        ▼
Token Generation
        │
        ▼
Generated Response

The prompt tells the model **what** to generate, while the generation parameters control **how** it generates the response.

---

# Code Walkthrough

## 1. Generation Parameters

```python
params = {
    "max_new_tokens": 128,
    "min_new_tokens": 10,
    "temperature": 0.5,
    "top_p": 0.2,
    "top_k": 1
}
```

### What does this do?

This dictionary controls the behaviour of the LLM **during text generation**.

The model itself is already trained.

These parameters **do not change the model**. They only control how the model selects the next token while generating the response.

Think of it as changing the model's "generation strategy" rather than its knowledge.

---

### max_new_tokens

Limits the maximum number of tokens the model is allowed to generate.

Without this limit, the model could continue generating unnecessarily long responses.

Role in the pipeline:

LLM
↓
Predict next token
↓
Repeat until
- stop token
OR
- 128 tokens generated

---

### min_new_tokens

Forces the model to generate at least a minimum number of tokens.

This prevents responses from ending too early.

---

### temperature

Temperature controls **how confident the model should be when choosing the next token**.

At every step, the LLM predicts probabilities for thousands of possible next words.

Example:

```
beautiful → 70%
strong → 20%
cold → 8%
banana → 2%
```

Low temperature makes the model strongly prefer the highest probability words.

High temperature flattens these probabilities, making less likely words more likely to be selected.

It changes **creativity**, not intelligence.

---

### top_p

The model first sorts all possible next tokens by probability.

Instead of looking at every token, it keeps only the smallest set whose cumulative probability reaches `p`.

For `top_p = 0.2`, the model only samples from the most probable 20% of the probability distribution.

This removes unlikely words before sampling.

---

### top_k

After ranking all possible next tokens, the model only keeps the **top K tokens**.

With

```python
top_k = 1
```

the model always chooses from only the single most probable token.

This makes the output highly deterministic.

---

## 2. Prompt

```python
prompt = "The wind is"
```

The prompt provides the starting context.

The LLM now predicts the next token based on everything it learned during training.

It repeats this prediction one token at a time until a stopping condition is reached.

---

## 3. Model Invocation

```python
response = llm_model(prompt, params)
```

This sends

- the prompt
- generation parameters

to the IBM Granite model.

Pipeline:

Prompt
+
Generation Parameters
↓

Granite LLM

↓

Predict next token

↓

Append token

↓

Predict next token again

↓

Continue until stopping condition

↓

Return complete response

---

## 4. Displaying the Output

```python
print(prompt)
print(response)
```

Simply prints the original prompt and the generated response.

No new computation happens here.

---

# Key Takeaways

- The prompt provides context.
- The LLM generates one token at a time.
- Generation parameters control **how tokens are selected**, not what the model knows.
- The model's weights never change during inference.

# Zero-Shot Prompting

## Objective

Understand how an LLM performs a task without being given any examples.

The goal of this experiment is to test whether the model can use the knowledge it learned during pre-training to correctly answer a factual question.

---

# Overall Pipeline

User Prompt
        │
        ▼
LLM reads the instruction
        │
        ▼
LLM understands the task
(True/False Classification)
        │
        ▼
LLM retrieves knowledge from its parameters
        │
        ▼
LLM generates the answer

Unlike few-shot prompting, **no examples are provided** inside the prompt.

---

# Code Walkthrough

## Prompt

```python
prompt = """
Classify the following statement as true or false:
'The Eiffel Tower is located in Berlin.'

Answer:
"""
```

### What does this do?

The prompt tells the LLM:

1. What task to perform.
2. What information to evaluate.
3. Where to generate the answer.

Notice that **no examples** are provided.

The model has to infer how to solve the task entirely from the instruction.

---

## Why does the model still know the answer?

The model has already been pre-trained on a massive amount of text.

During inference, it does **not search Google** or train itself again.

Instead, it uses the knowledge stored inside its learned parameters (weights).

When it reads

> "The Eiffel Tower is located in Berlin."

it recognizes:

- Eiffel Tower
- Berlin

and recalls from its learned knowledge that

> Eiffel Tower → Paris

Therefore it predicts:

```
False
```

---

## Model Invocation

```python
response = llm_model(prompt, params)
```

The prompt is passed to the language model.

The generation parameters determine **how** the response is generated, while the prompt determines **what** the model is trying to accomplish.

---

## Output

```python
print(response)
```

Displays the model's generated answer.

---

# How this fits into the bigger picture

Zero-shot prompting is usually the first technique we try.

It works well when:

- the task is simple
- the model already has enough knowledge
- no demonstrations are required

If the model struggles, we can move to:

Zero-shot

↓

One-shot

↓

Few-shot

↓

Fine-tuning (if necessary)

---

# Key Takeaways

- No examples are given to the model.
- The model relies entirely on knowledge learned during pre-training.
- The prompt only describes the task.
- The model's parameters are **not updated** during inference.