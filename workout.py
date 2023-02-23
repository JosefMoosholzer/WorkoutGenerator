from typing import List
from exercise import *

class Workout():
    def __init__(self, exercises: List[Exercise], intensity: int, muscle_area: MuscleArea) -> None:
        self.exercises = exercises
        self.intensity = intensity
        self.muscle_area = muscle_area
    
    def ma_str(self) -> str:
        return self.muscle_area.value

    def to_str(self) -> str:
        return "\n" + "\n".join([exercise.to_str(self.intensity) for exercise in self.exercises])

    def incr_intensity(self) -> str:
        self.intensity += 1
        return self.to_str()

    def decr_intensity(self) -> str:
        self.intensity -= 1
        return self.to_str()
    