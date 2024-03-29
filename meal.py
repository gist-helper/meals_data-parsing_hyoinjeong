class Meal:
    title: str
    meal_date: str
    kind_of_meal: str
    menu: str


class MealWrapper:
    meal: Meal

    def __init__(self) -> None:
        self.meal = Meal()


kind_of_meals = [["조식", "중식", "석식"], ["Breakfast", "Lunch", "Dinner"]]

kind_of_restaurants = [
    ["제1학생회관1층", "제1학생회관2층", "제2학생회관1층"],
    [
        "Student Union Bldg.1 1st floor",
        "Student Union Bldg.1 2nd floor",
        "Student Union Bldg.2 1st floor",
    ],
]

slot_endpoints = [(3, 13), (13, 23), (23, 30)]
slot_filenames_postfix = [
    ["_b_kor.json", "_l_kor.json", "_d_kor.json"],
    ["_b_eng.json", "_l_eng.json", "_d_eng.json"],
]
