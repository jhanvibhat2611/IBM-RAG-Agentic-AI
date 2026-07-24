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

## Starter code: provide your solutions in the TODO parts

# 1. Prompt for decision-making process
decision_making_prompt = """Consider this dilemma: A student has a test due in 2 days, should the student study 
tonight or go to a movie with friends.
                            Think through this dilemma step-by-step, considering the pros and cons of each option, 
                            and what factors might be most important in making this choice."""

# 2. Prompt for explaining a process
sandwich_making_prompt = """Explain how to make a peanut butter and jelly sandwich.

Break down each step of the process in detail, from gathering ingredients to finishing the sandwich.
"""

responses = {}
responses["decision_making"] = llm_model(decision_making_prompt)
responses["sandwich_making"] = llm_model(sandwich_making_prompt)

for prompt_type, response in responses.items():
    print(f"=== {prompt_type.upper()} RESPONSE ===")
    print(response)
    print()

# Output
# === DECISION_MAKING RESPONSE ===
#
# To think through this dilemma step-by-step, let's consider the pros and cons of each option and the factors that might be most important in making this choice.
#
# ### Option 1: Study tonight
#
# **Pros:**
# 1. The student will be better prepared for the test, increasing the likelihood of a good grade.
# 2. Studying tonight allows the student to relax and enjoy the movie with friends without worrying about the test.
# 3. The student will have more time to study or relax in the following days, reducing stress levels.
#
# **Cons:**
# 1. The student will miss out on spending time with friends tonight, which could be a valuable social experience.
# 2. Studying tonight might lead to fatigue, affecting the student's performance at the movie or the following day's activities.
#
# ### Option 2: Go to the movie with friends tonight
#
# **Pros:**
# 1. The student will have a fun and enjoyable evening with friends, creating positive memories and strengthening social bonds.
# 2. Taking a break from studying might help the student relax and recharge, potentially improving their focus and performance on the test.
# 3. The student will have more time to study in the following days, allowing for a more relaxed schedule.

# === SANDWICH_MAKING RESPONSE ===
#
# To make a peanut butter and jelly sandwich, follow these steps:
#
# 1. Gather the ingredients.
#    - Two slices of bread
#    - Peanut butter
#    - Jelly or jam
#    - A butter knife or spreader
#    - A plate
#
# 2. Prepare the bread.
#    - Place the two slices of bread on the plate.
#
# 3. Spread the peanut butter.
#    - Scoop a generous amount of peanut butter using the knife.
#    - Spread it evenly over one slice of bread.
#    - Cover the entire surface, spreading close to the edges without going over them.
#
# 4. Spread the jelly or jam.
#    - Clean the knife or use a different one.
#    - Scoop a generous amount of jelly or jam.
#    - Spread it evenly over the second slice of bread.
#    - Again, spread close to the edges without going over them.
#
# 5. Combine the slices.
#    - Place the peanut butter slice on top of the jelly slice.
#    - Make sure the spread sides face each other.
#    - Press down gently so the sandwich stays together.
#
# 6. Cut the sandwich (optional).
#    - Cut it diagonally or horizontally, depending on your preference.
#    - Serve and enjoy.
