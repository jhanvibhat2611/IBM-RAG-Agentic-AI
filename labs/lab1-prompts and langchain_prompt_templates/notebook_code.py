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

# 1. One-shot prompt for formal email writing
formal_email_prompt = """
Here is an example of a formal email requesting information:

Subject: Inquiry Regarding Product Specifications for Model XYZ-100

Dear Customer Support Team,

I hope this email finds you well. I am writing to request detailed specifications for your product Model XYZ-100. Specifically, I am interested in learning about its dimensions, power requirements, and compatibility with third-party accessories.

Could you please provide this information at your earliest convenience? Additionally, I would appreciate any available documentation or user manuals that you could share.

Thank you for your assistance in this matter.

Sincerely,
John Smith

---

Now, please write a formal email to a university admissions office requesting information about their application deadline and required documents for the Master's program in Computer Science:

"""

# 2. One-shot prompt for simplifying technical concepts
technical_concept_prompt = """
Here is an example of explaining a technical concept in simple terms:

Technical Concept: Blockchain
Simple Explanation: A blockchain is like a digital notebook that many people have copies of. When someone writes a new entry in this notebook, everyone's copy gets updated. Once something is written, it can't be erased or changed, and everyone can see who wrote what. This makes it useful for recording important information that needs to be secure and trusted by everyone.

---

Now, please explain the following technical concept in simple terms:

Technical Concept: Machine Learning
Simple Explanation:
"""

# 3. One-shot prompt for keyword extraction
keyword_extraction_prompt = """
Here is an example of extracting keywords from a sentence:

Sentence: "Cloud computing offers businesses flexibility, scalability, and cost-efficiency for their IT infrastructure needs."
Keywords: cloud computing, flexibility, scalability, cost-efficiency, IT infrastructure

---

Now, please extract the main keywords from the following sentence:

Sentence: "Sustainable agriculture practices focus on biodiversity, soil health, water conservation, and reducing chemical inputs."
Keywords:
"""

responses = {}
responses["formal_email"] = llm_model(formal_email_prompt)
responses["technical_concept"] = llm_model(technical_concept_prompt)
responses["keyword_extraction"] = llm_model(keyword_extraction_prompt)

for prompt_type, response in responses.items():
    print(f"=== {prompt_type.upper()} RESPONSE ===")
    print(response)
    print()

# Output
# === FORMAL_EMAIL RESPONSE ===
# Subject: Inquiry Regarding Application Deadline and Required Documents for Master's Program in Computer Science
#
# Dear Admissions Office,
#
# I hope this email finds you well. I am writing to request information about the application deadline and required documents for the Master's program in Computer Science at your esteemed institution.
#
# Could you please provide details regarding the application deadline for the upcoming academic year? Additionally, I would appreciate it if you could share a list of required documents, such as transcripts, letters of recommendation, and a statement of purpose.
#
# Thank you for your assistance in this matter. I look forward to your prompt response.
#
# Sincerely,
# [Your Name]
#
# === TECHNICAL_CONCEPT RESPONSE ===
# Machine learning is like teaching a computer to learn from experience, similar to how humans learn. Instead of being explicitly programmed to perform a task, the computer is given a lot of data and learns to recognize patterns and make decisions based on that data. For example, if you show a computer many pictures of cats and dogs, it can learn to identify new pictures as either a cat or a dog without being specifically told the rules for distinguishing them. This is useful for tasks like recognizing speech, recommending products, or detecting fraud, where the patterns might be too complex for humans to easily program.
#
# === KEYWORD_EXTRACTION RESPONSE ===
# 1. sustainable agriculture
# 2. biodiversity
# 3. soil health
# 4. water conservation
# 5. reducing chemical inputs

# parameters: Set `max_new_tokens` to 10, which constrains the model to generate brief responses

params = {
    "max_new_tokens": 10,
}

prompt = """Here are few examples of classifying emotions in statements:

            Statement: 'I just won my first marathon!'
            Emotion: Joy

            Statement: 'I can't believe I lost my keys again.'
            Emotion: Frustration

            Statement: 'My best friend is moving to another country.'
            Emotion: Sadness

            Now, classify the emotion in the following statement:
            Statement: 'That movie was so scary I had to cover my eyes.’


"""
response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")

# Output
# prompt: Here
# are
# few
# examples
# of
# classifying
# emotions in statements:
#
# Statement: 'I just won my first marathon!'
# Emotion: Joy
#
# Statement: 'I can'
# t
# believe
# I
# lost
# my
# keys
# again.
# '
# Emotion: Frustration
#
# Statement: 'My best friend is moving to another country.'
# Emotion: Sadness
#
# Now, classify
# the
# emotion in the
# following
# statement:
# Statement: 'That movie was so scary I had to cover my eyes.’
#
# response: Emotion: Fear

