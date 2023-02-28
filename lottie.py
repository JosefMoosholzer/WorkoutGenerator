from streamlit_lottie import st_lottie
import json

def load_lottie(muscle_area: str, bullet_points):
    if "upper" in muscle_area.lower():
        with open("lotties/bicep_curl.json", 'r') as f:
            st_lottie(json.load(f), height=bullet_points*50, key="coding")
    elif "core" in muscle_area.lower():
        with open("lotties/crunches.json", 'r') as f:
            st_lottie(json.load(f), height=bullet_points*50, key="coding")
    else:
        with open("lotties/high_squat.json", 'r') as f:
            st_lottie(json.load(f), height=bullet_points*50, key="coding")
