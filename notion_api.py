from typing import List, Dict, Callable
import requests
import re as regex
from random import sample
import streamlit as st

from exercise import *
from muscle_area import MuscleArea


def str_to_exercise(prompt: str) -> Exercise:
    """ Creates an (Weighted)Exercise object out of the give string prompt. """
    inputs = prompt.split(",")
    if len(inputs) == 2:
        return str_to_body_exercise(inputs)
    elif len(inputs) == 4:
        return str_to_weighted_exercise(inputs)
    else:
        raise ValueError(f"Workout {inputs[0]} does not give either 2 or 4 inputs. Check Notion!")


def str_to_body_exercise(inputs: List[str]) -> BodyExercise:
    """ Creates an Exercise object from a list of two strings.\n
    The second element will be converted into a function that provides a dynamic number of reps for a given 'factor'. """

    return Exercise(
            inputs[0],
            extract_reps_function(inputs[1]))


def str_to_weighted_exercise(inputs: List[str]) -> WeightedExercise:
    """ Creates an Exercise object from a list of four strings.\n
    The second element will be converted into a function that provides a dynamic number of reps for a given 'factor'.\n
    The third elements will be converted into a function that provides a dynamic amount of weight for a given 'factor' """

    return WeightedExercise(
            inputs[0],
            extract_reps_function(inputs[1]),
            extract_weight_function(inputs[1], inputs[2]),
            inputs[3])


def extract_reps_function(rep_prompt: str) -> Callable[[int], str]:
    """ Extracts the amount of reps from the prompt.\n
    Either being an alternation of reps in steps of two between two numbers or an infinite increment in reps or seconds."""
    measure = "seconds" if "sec" in rep_prompt else "reps"
    if "to" in rep_prompt:
        return reps_from_to(*rep_prompt.split("to"))
    elif len(rep_prompt.split("+")) > 1:
        base = int(regex.sub("[^0-9.]", "", rep_prompt.split("+")[0]))
        increment = int(regex.sub("[^0-9.]", "", rep_prompt.split("+")[1]))
        return lambda x: f'{base + x * increment} {measure}'
    else:
        return lambda x: f'{int(regex.sub("[^0-9.]", "", rep_prompt))} {measure}'


def reps_from_to(num_from: int, num_to: int) -> Callable[[int], str]:
    num_from, num_to = int(num_from), int(num_to)
    steps: int = int((num_to - num_from)/2)
    return lambda x: f"{num_from + (x % steps) * 2} reps"


def extract_weight_function(rep_prompt: str, weight_prompt: str) -> Callable[[int], float]:
    base: float = float(regex.sub("[^0-9.]", "", weight_prompt.split("+")[0]))
    increment: float = float(regex.sub("[^0-9.]", "", weight_prompt.split("+")[1]))
    if "to" in rep_prompt:
        steps: int = (int(rep_prompt.split("to")[1]) - int(rep_prompt.split("to")[0]))/2
        return lambda x: base + increment * (x // steps)
    elif "over" in weight_prompt:
        return lambda x: max([0, x-base]) * increment
    else:
        return lambda x: base + increment * x


def create_header():
    api_key: st.secrets["NOTION_API_KEY"]

    return {'Authorization': f"Bearer {api_key}", 
            'Content-Type': 'application/json', 
            'Notion-Version': '2022-06-28'}


def api_get(id) -> dict:
    return requests.get(f"https://api.notion.com/v1/blocks/{id}/children", headers=create_header()).json()["results"]


def get_exercises() -> List[Exercise]:
    page_id: str = "e46955bc-195a-4840-87a9-c3e7e9f57418"
    bullets = [(result["bulleted_list_item"]["rich_text"][0]["plain_text"].lower(), result["id"]) for result in api_get(page_id)]
    
    return [str_to_exercise(exercise["bulleted_list_item"]["rich_text"][0]["plain_text"]) for bullet in bullets for exercise in api_get(bullet[1])]


def sample_exercises(exercises: List[Exercise], muscle_area: MuscleArea, exercise_type, amount: int):
    sub_pop = [exercise for exercise in exercises if (exercise.muscle_area == muscle_area and type(exercise) == exercise_type)]
    try: # in case the sub-population is too small
        return sample(sub_pop, amount)
    except ValueError:
        return sample_exercises(exercises, muscle_area, exercise_type, amount - 1)