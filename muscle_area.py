from enum import Enum
from typing import List

class MuscleArea(Enum):
    PUSH = "Upper Push"
    PULL = "Upper Pull"
    ABS = "Core Abs"
    BACK = "Core Back"
    LEGS = "Legs"

def str_to_muscle_areas(area: str) -> List[MuscleArea]:
    if area == "Full Upper Body":
        return [MuscleArea("Upper Push"), MuscleArea("Upper Pull")]
    elif area == "Upper Body - Push":
        return [MuscleArea("Upper Push")]
    elif area == "Upper Body - Pull":
        return [MuscleArea("Upper Pull")]
    elif area == "Full Core":
        return [MuscleArea("Core Abs"), MuscleArea("Core Back")]
    elif area == "Core - Abs":
        return [MuscleArea("Core Abs")]
    elif area == "Core - Lower Back":
        return [MuscleArea("Core Back")]
    elif area == "Legs":
        return [MuscleArea("Legs")]
    else: return []