import streamlit as st
import oai
from notion_api import get_exercises
from workout import Workout

em_dash = "—"
notion_exercises = ""
oai_exercises = ""

# Define the options for each user input
muscle_areas = ["Full Upper Body", "Upper Body - Push", "Upper Body - Pull", "Full Core", "Core - Abs", "Core - Lower Back", "Legs"]
#intensity_levels = list(range(1, 11))

# Set up the Streamlit app
st.set_page_config(layout="wide", page_title="Exercise Generator")
st.title("Exercise Generator :man-lifting-weights:")
st.markdown("### Select the muscle area, exercise type, and intensity level below, then click  Submit button to generate a list of exercises.")

col1, col2 = st.columns([2,3])

# Add inputs to the left column
with col1:
    muscle_area = st.selectbox("Muscle area", muscle_areas)
    exercise_type = st.selectbox("Exercise type", ["Bodyweight", "Weighted Exercises"])
    intensity = st.slider("Intensity level", 1, 10, 2)
    num_exercises = st.slider("Number of exercises", 4, 8, 6)
    _, subcol1, _, subcol2, _= st.columns(5)
    with subcol1:
        oai_button = st.button("OpenAI", key="oai_button")
    with subcol2:
        notion_button = st.button("Notion", key="notion_button")

# Add the generated output to the right column
with col2:
    if oai_button:
        oai_exercises = oai.generate_exercises(muscle_area, exercise_type, intensity, num_exercises)
        if oai_exercises:
            st.write(f"Here are some {exercise_type} exercises targeting the {muscle_area} area at an intensity level of {intensity}:")
            for exercise in oai_exercises[1:]:
                st.write(f"- {exercise}")
        else:
            st.write("OpenAI seems to be too busy, try the other option! :smile:")
    if notion_button:
        if not notion_exercises:
            notion_exercises = get_exercises()
        

