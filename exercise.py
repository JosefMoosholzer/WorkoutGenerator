from typing import Callable
from muscle_area import MuscleArea

class Exercise():
    def __init__(self, name: str, sets: int, muscle_area: MuscleArea) -> None:
        self.name = name
        self.sets = sets
        self.muscle_area = muscle_area

    def to_str(self, factor: int) -> str:
        pass
    

class WeightedExercise(Exercise):
    def __init__(self, name: str, sets: int, muscle_area: MuscleArea, reps_range: Callable[[int], str], weights: Callable[[int], float]) -> None:
        super().__init__(name, sets, muscle_area)
        self.reps_range = reps_range
        self.weights = weights

    def to_str(self, factor: int) -> str:
        return self.name + ":\n\t" + str(self.sets) + "sets of " + self.reps_range(factor) + " w/ " + str(self.weights(factor)) + "kg"

    
class BodyExercise(Exercise):
    def __init__(self, name: str, sets: int, muscle_area: MuscleArea, reps: Callable[[int], str], extra_weights: Callable[[int], float]) -> None:
        super().__init__(name, sets, muscle_area)
        self.reps = reps
        self.extra_weights = extra_weights

    def calculate_extra_weight(self, factor: int) -> str:
        extra_weight = self.extra_weights(factor)
        if extra_weight:
            return " w/ " + str(extra_weight) + " kg added."
        else:
            return "."

    def to_str(self, factor: float) -> str:
        return self.name + ":\n\t" + str(self.sets) + "sets of " + self.reps(factor) + self.calculate_extra_weight(factor)

body_exercise = BodyExercise("Push Ups", 3, MuscleArea("Upper Push"), lambda x: f"{15 + 2*x}", lambda x: (x-5)*2 if x > 5 else 0)
print(body_exercise.to_str(2))