


def calculate_cgpa(data):

    total = 0
    total_c= 0

    for course_info in data:
        credits = course_info["credits"]
        cgpa = course_info["cgpa"]

        total = total + (credits*cgpa)
        total_c = total_c + credits 

    average = total / total_c
    return average



data = [
    {"course":"math","credits":3.0,"cgpa":3.3},
    {"course": "Programming", "credits": 4.0, "cgpa": 4.0},
    {"course": "Statistics", "credits": 3.0, "cgpa": 3.7},
    {"course": "AI", "credits": 3.0,"cgpa": 3.0},
    {"course": "Databases", "credits": 4.0, "cgpa": 4.0}
]

result = calculate_cgpa(data)
print(f"Average:{result:2f}")