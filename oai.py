import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Define a function that generates a list of exercises based on user inputs
def generate_exercises(muscle_area, exercise_type, intensity, amount):
    # Define the prompt to be fed to the OpenAI API, with benchmarks for the intensity levels
    benchmarks = {"Upper Body - Push": ("15 push ups", "50 push ups"),
                "Upper Body - Pull": ("6 pull ups", "20 pull ups"),
                "Full Upper Body": ("15 push ups", "50 push ups"),
                "Core - Abs": ("30 crunches", "80 crunches"),
                "Core - Lower Back": ("10 back extensions", "20 back extensions with 20kg extra weight"),
                "Full Core": ("30 crunches", "80 crunches"),
                "Legs": ("15 squats", "50 squats")}
    
    prompt = f"Generate a list of {amount} {exercise_type} exercises for an '{muscle_area}' workout, with an intensity level of {intensity}." + \
                f"A level of intensity of 0 shall be equivalent to {benchmarks[muscle_area][0]} and an intensity level of 10 equivalent to {benchmarks[muscle_area][1]}" + \
                "Provide the exercises in a bullet list in the following format: Name of exercise, sets, repetitions" + \
                (" and weights in kg." if "Weighted" in exercise_type else ".") + \
                "Do not provide a prompt before and after the bullet list."

    # Use the OpenAI API to generate the list of exercises
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=120,
        n=1,
        stop=None,
        timeout=10,
    )
    
    # Extract the generated text from the API response
    return response.choices[0].text.strip().split("•")




