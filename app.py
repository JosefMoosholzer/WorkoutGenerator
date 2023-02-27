import streamlit as st
import oai
import re as regex
from notion_api import get_exercises, sample_exercises
from workout import Workout, str_to_exercise_types
from muscle_area import MuscleArea, str_to_muscle_areas
from email_notifier import send_message_to
from lottie import load_lottie

# Global variables
NOTION_URL = "https://dapper-lobe-3ac.notion.site/Workouts-e46955bc195a484087a9c3e7e9f57418"
MUSCLE_AREAS = ["Full Upper Body", "Upper Body - Push", "Upper Body - Pull", "Full Core", "Core - Abs", "Core - Lower Back", "Legs"]


# Set up the Streamlit app
st.set_page_config(page_title="Exercise Generator", page_icon=":muscle:", layout="wide")
with st.container():
    st.header("Hi, my name is Josef! :wave:")
    st.title("Exercise Generator :man-lifting-weights:")
    st.markdown("### Select the muscle area, exercise type, intensity level and number of exercises below, then choose an option to generate a fitting workout.")
    st.write("---")

left_col, right_col = st.columns([2,3])

# Left column
with left_col:
    # Define the options for each user input
    muscle_area = st.selectbox("Muscle area", MUSCLE_AREAS)
    exercise_type = st.selectbox("Exercise type", ["Bodyweight", "Weighted Exercises", "Both"])
    intensity = st.slider("Intensity level", 0, 10, 2)
    num_exercises = st.slider("Number of exercises", 1, 6, 4)
    email = st.text_input("(Optional) Enter your email address - to retrieve your workout later!")

    _, subcol1, _, subcol2, _= st.columns(5)
    with subcol1:
        oai_button = st.button("OpenAI", key="oai_button")
    with subcol2:
        notion_button = st.button("Notion", key="notion_button")

# Add the generated output to the right column
with right_col:
    if oai_button:
        oai_exercises = oai.generate_exercises(muscle_area, exercise_type, intensity, num_exercises)
        if oai_exercises:
            st.markdown(f"Here are some {exercise_type.lower()} exercises provided by **OpenAI** targeting the {regex.sub('-', '/', muscle_area).lower()} with an intensity level of {intensity}:")
            for exercise in oai_exercises[1:]:
                st.write(f"- {exercise}")
            if email:
                send_message_to("\n".join(oai_exercises), email)
                st.write("You should have received an E-Mail with the subject 'Your generated workout'!")
        else:
            st.write("OpenAI seems to be too busy, try the other option! :smile:")
    if notion_button:
        notion_exercises = get_exercises()
        if notion_exercises:
            sampled_exercises = sample_exercises(notion_exercises, str_to_muscle_areas(muscle_area), str_to_exercise_types(exercise_type), num_exercises)
            workout = Workout(sampled_exercises, intensity, str_to_muscle_areas(muscle_area))
            st.markdown(f"Here are some {exercise_type.lower()} exercises taken from my **Notion-notebook** ([see here]({NOTION_URL})) targeting the {regex.sub('-', '/', muscle_area).lower()} with an intensity level of {intensity}:")
            for exercise in workout.list_exercises():
                st.write(f"- {exercise}")
            if email:
                send_message_to(workout.to_str(), email)
                st.write("You should have received an E-Mail with the subject 'Your generated workout'!")
        else:
            st.write("The Notion-API does not to seem work :disappointed:")

    if oai_button or notion_button:
        load_lottie(muscle_area)
