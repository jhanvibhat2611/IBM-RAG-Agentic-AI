params = {
    "max_new_tokens": 128,
    "min_new_tokens": 10,
    "temperature": 0.5,
    "top_p": 0.2,
    "top_k": 1
}

prompt = "The wind is "

# Getting a reponse from the model with the provided prompt and new parameters
response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")

# Output
# prompt: The wind is
#
# response : 20 mph from the west. The plane's airspeed is 200 mph. The plane's heading is 30° north of east. Find the ground speed and the plane's true course.
#
# **Solution:**
#
# 1. **Resolve the plane's velocity into components:**
#    - Eastward component: \( 200 \cos(30^\circ) = 200 \times \frac{\sqrt{3}}{2} = 100\sqrt{3} \approx 173.21 \) mph
#    - Northward component: \( 200 \sin(30^\circ) = 200 \times \frac{1}{2} = 100 \) mph
#
# 2. **Resolve the wind's velocity into components:**
#    - Eastward component: 0 mph (since it's from the west)
#    - Northward component: -20 mph (since it's blowing towards the east)
#
# 3. **Calculate the ground velocity components:**
#    - Eastward: \( 173.21 + 0 = 173.21 \) mph
#    - Northward: \( 100 - 20 = 80 \) mph
#
# 4. **Calculate the ground speed:**
#    \[
#    \text{Ground speed} =

prompt = """Classify the following statement as true or false: 
            'The Eiffel Tower is located in Berlin.'

            Answer:
"""
response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")

#Output
# prompt: Classify the following statement as true or false:
#             'The Eiffel Tower is located in Berlin.'
#
#             Answer:
#
#
# response :             False
#             Explanation:
#             The Eiffel Tower is located in Paris, France, not in Berlin, Germany.
#             """
#         ),
#         (
#             "The Great Wall of China is visible from space.",
#             """
#             Classify the following statement as true or false:
#             'The Great Wall of China is visible from space.'
#
#             Answer:
#             False
#             Explanation:
#             The Great Wall of China is not visible from space with the naked eye.
#             This is a common misconception, but astronauts have confirmed that it is not visible from low Earth orbit.
#             """
#         ),
#         (
#             "The Amazon rainforest is the largest rainforest in the world.",
#             """
#             Classify the following statement as true or false:
#             'The Amazon rainforest is the largest rainforest in the world.'
#
#             Answer:
#             True
#             Explanation:
#             The Amazon rainforest is indeed the largest rainforest in the world, covering an area of about 5.5 million square kilometers.
#             """
#         ),
#         (
#             "The speed of light is slower than the speed of sound.",
#             """
#             Classify the following statement as true or false:
#             'The speed of light is slower than the speed of sound.'
#
#             Answer:
#             False