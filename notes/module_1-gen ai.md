# Module 1 - Generative AI

## Discriminative AI vs Generative AI

### Discriminative AI

- Discriminative AI is mostly used for classification.
- It basically distinguishes between different classes of data.
- It is more focused on analytical and predictive tasks.

### Limitations of Discriminative AI

- It is not context-aware.
- It cannot generate new data.
- It can only classify or predict based on the data it has.

---

### Generative AI

- Generative AI is capable of generating new data.
- It generates data based on the input provided by the user.
- The input is given in the form of a **prompt**.

A prompt can be:
- Text
- Image
- Audio
- Or other forms of input.

One interesting thing is that the output does not necessarily have to be in the same format as the input.

For example:
- Input → Text prompt
- Output → Image

or vice versa.

Generative AI is mainly focused on creativity and content generation.

---

## Difference Between Discriminative AI and Generative AI

Discriminative AI focuses on analytical and predictive tasks.

Generative AI focuses on creative tasks by generating completely new content.

### Example

Suppose we have an image.

Using **Discriminative AI**, we can classify whether the image contains a nest or an egg.

Using **Generative AI**, we can give a prompt like:

> "Generate an image of a bird's nest with eggs."

and it can create a completely new image.

---

## Neural Networks

Generative AI is mainly built using neural networks.

We already know that neural networks are inspired by the human brain.

A **neuron** is the basic unit of a neural network and is modeled after the way neurons work in the human brain.

When many artificial neural networks are trained on massive amounts of data, it is called **Deep Learning**.

---

## Technologies Used in Generative AI

Generative AI develops creativity using:

- Generative Adversarial Networks (GANs)
- Variational Autoencoders (VAEs)
- Transformers
- Diffusion Models

---

## Foundation Models

Foundation models are AI models with broad capabilities.

They are trained on huge amounts of data and can later be adapted for specific tasks or applications.

One example of a foundation model is an **LLM (Large Language Model)**.

---

# Foundation Models

Foundation models came into the picture when researchers noticed a new paradigm.

They saw that one single model was able to perform multiple different tasks, not just the task it was originally intended for.

This was possible because these models were trained on massive amounts of **unlabeled (unsupervised)** data.

---

## Tuning (Fine-Tuning)

One cool thing about foundation models is that even though they are mainly built for generative purposes, if they are given a small amount of labeled data, they can be tuned to perform normal NLP tasks as well.

For example:

- Text classification
- Sentiment analysis
- Other NLP tasks that are not usually associated with generation.

This process is known as **fine-tuning**.

---

## Prompting

Another cool thing is that foundation models work really well even when you have only a small amount of data.

For example, suppose I give the model a sentence and ask it whether the sentiment is **positive** or **negative**.

Instead of having a separate classification model, the foundation model predicts the next words in the sequence, and based on the generated continuation and context, it is able to determine the sentiment.

So, prompting also becomes a very effective way of solving tasks without training a completely new model.

---

# Advantages of Foundation Models

## 1. Performance

Because they are trained on huge amounts of data, they perform really well even on tasks where only a small amount of task-specific data is available.

This is usually much better than training a completely separate model from scratch using limited data.

---

## 2. Productivity

Since the model has already learned from massive amounts of unlabeled data, it can perform tasks like prompting and fine-tuning very efficiently.

This saves a lot of time and effort compared to building and training separate models for every task.

---

# Disadvantages of Foundation Models

## 1. Cost

Training foundation models is extremely expensive.

Many small-scale companies cannot afford to train their own foundation models because they require huge computational resources and large numbers of GPUs for both training and deployment.

---

## 2. Trust

Since these models are trained on enormous amounts of internet data, it is difficult to verify whether all of that information is trustworthy.

Also, it is practically impossible to inspect billions of data points that the model has been trained on, so issues like misinformation and bias can exist.