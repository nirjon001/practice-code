
def calculate_average_grade(grades):
    if not grades:
        return 0.0
    
    total = sum(grades)
    average_grade = total/len(grades)
    return average_grade



students_grades = [3.5,3.9 ,4.0,3.35,3.9]

average_grade = calculate_average_grade(students_grades)
print(f"Average grade :{average_grade:.2f}")

