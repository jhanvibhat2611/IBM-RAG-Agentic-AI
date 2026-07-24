params = {
    "max_new_tokens": 128,
    "min_new_tokens": 10,
    "temperature": 0.5,
    "top_p": 0.2,
    "top_k": 1
}

prompt = "The benefits of sustainable energy include "

# Getting a reponse from the model with the provided prompt and new parameters
response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")

# Output
# prompt: The benefits of sustainable energy include
# #
# # response : 1) reduced greenhouse gas emissions, 2) improved air quality,
# 3) increased energy security, 4) job creation, and 5) cost savings.
# By transitioning to sustainable energy sources, we can mitigate the impacts of climate change,
# reduce our dependence on fossil fuels, and create a more resilient and sustainable energy system for the future.