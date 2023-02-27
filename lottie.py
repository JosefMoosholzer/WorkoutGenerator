from streamlit_lottie import st_lottie
import json

def load_lottie(muscle_area: str):
    if "upper" in muscle_area.lower():
        with open("lotties/bicep_curl.json", 'r') as f:
            st_lottie(json.load(f), height=300, key="coding")
    elif "core" in muscle_area.lower():
        with open("lotties/crunches.json", 'r') as f:
            st_lottie(json.load(f), height=300, key="coding")
    else:
        with open("lotties/low_squat.json", 'r') as f:
            st_lottie(json.load(f), height=300, key="coding")