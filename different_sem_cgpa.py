



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



sem1 = [
    {"course":"math","credits":3.0,"cgpa":3.3},
    {"course": "Programming", "credits": 4.0, "cgpa": 4.0},
    {"course": "Statistics", "credits": 3.0, "cgpa": 3.7},
    {"course": "AI", "credits": 3.0,"cgpa": 3.0},
    {"course": "Databases", "credits": 4.0, "cgpa": 4.0}
]

sem2 = [
    {"course": "Compiler Design", "credits": 3.0, "cgpa": 3.4},
    {"course": "Graph Theory", "credits": 3.0, "cgpa": 3.1},
    {"course": "Embedded Systems", "credits": 4.0, "cgpa": 2.8},
    {"course": "Human Computer Interaction", "credits": 2.0, "cgpa": 3.7},
    {"course": "Cloud Computing", "credits": 3.0, "cgpa": 3.9},
    {"course": "Mobile App Development", "credits": 3.0, "cgpa": 3.5}
]

result1 = calculate_cgpa(sem1)
print(f"first semester CGPA:{result1:.2f}")

result2 = calculate_cgpa(sem2)
print(f"Second semseter CGPA:{result2:.2f}")


avg_cgpa = (result1 + result2)/2
print(f"CGPA:{avg_cgpa:.2f}")