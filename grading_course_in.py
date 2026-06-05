
def calculate_grade(courses):

    total = 0
    count = 0

    for course, grade in courses.items(): 

        total = total + grade
        count = count + 1
    
    average = total / count
    return average
        


courses = {
    "Structure_programing": 3.3,
    "Object Oriented Programing" : 4.0,
    "Data Structure" : 4.0,
    "Algorithm" : 3.3,
    "AI": 3.0,
    "Operating System" : 4.0

}

result = calculate_grade(courses)
print(f"The average CG is :{result:.2f}")
