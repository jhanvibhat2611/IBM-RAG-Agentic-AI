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

# One-Shot Prompting

## Objective

Understand how providing **one example** helps an LLM learn the expected output format and apply the same pattern to a new input.

Unlike zero-shot prompting, the model is given **one demonstration** before solving the actual task.

---

# Overall Pipeline

User Prompt
        │
        ▼
One Example (Demonstration)
        │
        ▼
LLM learns the expected pattern
        │
        ▼
New Input
        │
        ▼
LLM applies the same pattern
        │
        ▼
Generated Response

The example acts as a guide for the model. The model does not retrain itself—it simply infers the pattern from the example provided in the prompt.

---

# Code Walkthrough

## 1. Generation Parameters

```python
params = {
    "max_new_tokens": 20,
    "temperature": 0.1,
}
```

### What does this do?

These parameters control **how the response is generated**.

- `max_new_tokens = 20`
  - Limits the response length.
  - Since translation responses are short, a small limit is sufficient.

- `temperature = 0.1`
  - Makes the model highly deterministic.
  - Translation has one primary goal—accuracy—so we don't want creative or random outputs.

---

## 2. Prompt

```python
prompt = """
Here is an example of translating a sentence from English to French:

English: "How is the weather today?"
French: "Comment est le temps aujourd'hui?"

Now, translate the following sentence from English to French:

English: "Where is the nearest supermarket?"
"""
```

### What does this do?

This prompt contains **one complete example** of the task.

The example teaches the LLM:

- the input language (English),
- the output language (French),
- the formatting style to follow.

The model then applies the same pattern to the new sentence.

This is why it is called **One-Shot Prompting**.

---

## 3. Model Invocation

```python
response = llm_model(prompt, params)
```

The prompt and generation parameters are sent to the LLM.

The model first understands the example, then applies the same translation pattern to the new sentence.

---

## Why does one example help?

LLMs are very good at recognizing patterns.

Instead of explicitly programming translation rules, we simply **show one example**, and the model infers the format and expected behaviour.

It is essentially saying:

```
Input A → Output A

Now...

Input B → ?
```

The model predicts Output B by following the demonstrated pattern.

---

# One-Shot vs Zero-Shot

### Zero-Shot

```
Translate:

"Where is the nearest supermarket?"
```

The model receives only an instruction.

---

### One-Shot

```
English → French
Hello → Bonjour

Now...

English → French
Where is the nearest supermarket?
```

The model first observes one example and then applies the same pattern.

---

# Key Takeaways

- One-shot prompting provides exactly one example.
- The example helps the model understand the expected format.
- No model parameters are updated.
- The model performs **in-context learning** by recognizing the pattern inside the prompt.

# Few-Shot Prompting

## Objective

Understand how providing **multiple examples** helps the LLM identify a pattern and generalize it to new inputs.

Unlike one-shot prompting, where only one example is given, few-shot prompting provides several demonstrations before asking the model to solve a new task.

---

# Overall Pipeline

User Prompt
        │
        ▼
Multiple Examples (Demonstrations)
        │
        ▼
LLM identifies the common pattern
        │
        ▼
New Input
        │
        ▼
LLM applies the learned pattern
        │
        ▼
Generated Response

The model is not trained again. It simply uses the examples present in the prompt as context to infer the expected behaviour.

---

# Code Walkthrough

## 1. Generation Parameters

```python
params = {
    "max_new_tokens": 10
}
```

### What does this do?

This controls the maximum length of the generated response.

Since the task is emotion classification, the expected output is only a single emotion such as **Joy**, **Fear**, or **Sadness**. Therefore, only a small number of tokens are required.

---

## 2. Prompt

```python
prompt = """
Here are few examples of classifying emotions...

Statement: "I just won my first marathon!"
Emotion: Joy

Statement: "I can't believe I lost my keys again."
Emotion: Frustration

Statement: "My best friend is moving to another country."
Emotion: Sadness

Now classify:

Statement: "That movie was so scary I had to cover my eyes."
"""
```

### What does this do?

The prompt first provides **three labelled examples**.

From these examples, the LLM learns:

- the expected input format,
- the expected output format,
- the relationship between a statement and its corresponding emotion.

After understanding the pattern, it predicts the emotion for the new statement.

This is called **Few-Shot Prompting** because multiple examples are used to guide the model.

---

## 3. Model Invocation

```python
response = llm_model(prompt, params)
```

The prompt is sent to the LLM.

Instead of relying only on its pre-trained knowledge, the model first studies the examples inside the prompt and then follows the same pattern for the new input.

---

# Why do multiple examples help?

Every example gives the model additional context.

With more demonstrations, the LLM has a better understanding of:

- the task,
- the expected format,
- the type of reasoning required.

As a result, the response is usually more reliable than zero-shot prompting, especially for tasks that could be interpreted in multiple ways.

---

# Zero-Shot vs One-Shot vs Few-Shot

### Zero-Shot

```
Classify the emotion:

"I just won my first marathon."
```

Only an instruction is provided.

---

### One-Shot

```
I lost my wallet.
Emotion: Sadness

Now classify:

I won my first marathon.
```

One example is provided.

---

### Few-Shot

```
Example 1
Input → Output

Example 2
Input → Output

Example 3
Input → Output

Now solve:

New Input
```

Multiple examples are provided before the actual task.

---

# Key Takeaways

- Few-shot prompting provides multiple demonstrations.
- The model identifies patterns from all the examples.
- No additional training or fine-tuning takes place.
- More examples generally improve consistency and accuracy for difficult tasks.


# Chain-of-Thought Prompting

## Objective

Understand how asking the LLM to reason step-by-step improves its performance on problems that require logical thinking or multiple calculations.

Instead of asking only for the final answer, we explicitly tell the model to explain its reasoning process.

---

# Overall Pipeline

Problem
      │
      ▼
Prompt asks for step-by-step reasoning
      │
      ▼
LLM breaks the problem into smaller logical steps
      │
      ▼
Intermediate reasoning
      │
      ▼
Final Answer

Unlike Zero-Shot or Few-Shot prompting, the focus here is **not on giving examples**. Instead, we guide *how* the model should think.

---

# Code Walkthrough

## 1. Generation Parameters

```python
params = {
    "max_new_tokens": 512,
    "temperature": 0.5
}
```

### What does this do?

### `max_new_tokens = 512`

Allows the model to generate a much longer response.

Since the model now has to explain every reasoning step before reaching the answer, it needs many more tokens than a simple classification task.

### `temperature = 0.5`

Keeps the output balanced.

The model can still explain naturally, but it stays reasonably consistent and doesn't become overly random.

---

## 2. Prompt

```python
prompt = """
Consider the problem:

A store had 22 apples.
They sold 15 apples today and got a new delivery...

Break down each step of your calculation.
"""
```

### What does this do?

Instead of asking:

> "How many apples are there?"

we ask

> "Break down each step of your calculation."

This changes **how the LLM generates its response**.

Rather than jumping directly to the answer, it first performs intermediate reasoning and then arrives at the final answer.

---

## 3. Model Invocation

```python
response = llm_model(prompt, params)
```

The complete prompt is sent to the LLM.

Because the prompt explicitly requests step-by-step reasoning, the model generates its reasoning first and then produces the final answer.

---

# Why does Chain-of-Thought work?

Complex problems usually involve multiple logical steps.

If the model is forced to think through every step, it is less likely to skip important information or make calculation mistakes.

Breaking a large problem into smaller reasoning steps often leads to more accurate answers.

---

# When should it be used?

Chain-of-Thought prompting is useful for tasks involving:

- Mathematical calculations
- Logical reasoning
- Multi-step decision making
- Complex problem solving
- Situations where understanding the reasoning is important

It is generally unnecessary for simple tasks like translation or sentiment classification.

---

# Key Takeaways

- Chain-of-Thought prompting tells the LLM to reason step by step.
- The model generates intermediate reasoning before producing the final answer.
- It improves accuracy on complex reasoning tasks.
- Longer reasoning requires a larger `max_new_tokens` value.

# Self-Consistency Prompting

## Objective

Understand how asking the LLM to solve the same problem multiple times using different reasoning paths helps improve the reliability and accuracy of the final answer.

Instead of generating a single response, the model generates multiple independent reasoning paths and then selects the answer that appears most consistent across them.

---

# Overall Pipeline

Problem
      │
      ▼
Prompt requests multiple independent solutions
      │
      ▼
LLM generates several reasoning paths
      │
      ├──► Reasoning Path 1
      ├──► Reasoning Path 2
      └──► Reasoning Path 3
      │
      ▼
Compare the different results
      │
      ▼
Select the most consistent answer
      │
      ▼
Final Response

Unlike Chain-of-Thought, which produces one reasoning process, Self-Consistency generates multiple reasoning paths before deciding on the final answer.

---

# Code Walkthrough

## 1. Generation Parameters

```python
params = {
    "max_new_tokens": 512
}
```

### What does this do?

`max_new_tokens = 512` allows the model to generate long responses.

Since the model now needs to produce multiple complete reasoning paths instead of just one answer, it requires a much larger token limit.

---

## 2. Prompt

```python
prompt = """
When I was 6, my sister was half of my age.
Now I am 70, what age is my sister?

Provide three independent calculations and explanations, then determine the most consistent result.
"""
```

### What does this do?

The prompt does not simply ask for the answer.

Instead, it instructs the model to:

- solve the problem multiple times,
- use different reasoning approaches,
- compare the different solutions,
- and finally choose the answer that appears most consistent.

This encourages the model to verify its own reasoning before giving the final response.

---

## 3. Model Invocation

```python
response = llm_model(prompt, params)
```

The prompt is sent to the LLM.

Instead of generating one answer immediately, the model creates multiple independent reasoning paths, compares them internally, and then returns the most reliable answer.

---

# Why does Self-Consistency work?

LLMs can sometimes arrive at different answers depending on the reasoning path they follow.

By generating several independent solutions and selecting the answer that appears most consistently, the chances of choosing the correct answer increase.

This makes the output more reliable, especially for complex reasoning tasks.

---

# Chain-of-Thought vs Self-Consistency

### Chain-of-Thought

Problem
↓
One reasoning path
↓
Final answer

The model explains its reasoning once.

---

### Self-Consistency

Problem
↓
Reasoning Path 1

Reasoning Path 2

Reasoning Path 3
↓
Compare all reasoning paths
↓
Most consistent answer

The model verifies its own reasoning before giving the final answer.

---

# Key Takeaways

- Self-Consistency generates multiple independent reasoning paths.
- The model compares these reasoning paths before selecting the final answer.
- It improves the reliability and accuracy of responses.
- It is especially useful for logical reasoning, mathematics, and complex decision-making tasks.