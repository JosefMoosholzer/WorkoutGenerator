from typing import List
from exercise import *

class Workout():
    def __init__(self, exercises: List[Exercise], intensity: int, muscle_areas: MuscleArea) -> None:
        self.exercises = exercises
        self.intensity = intensity
        self.muscle_areas = muscle_areas
    
    def list_exercises(self) -> List[str]:
        return [exercise.to_str(self.intensity) for exercise in self.exercises]

    def ma_str(self) -> str:
        return self.muscle_areas

    def to_str(self) -> str:
        return "\n" + "\n".join(self.list_exercises())

    def incr_intensity(self) -> str:
        self.intensity += 1
        return self.to_str()

    def decr_intensity(self) -> str:
        self.intensity -= 1
        return self.to_str()

def str_to_exercise_types(string: str) -> List[Exercise]:
    if string == "Bodyweight":
        return [BodyExercise]
    elif string == "Weighted Exercises":
        return [WeightedExercise]
    elif string == "Both":
        return [BodyExercise, WeightedExercise]
    else: return []