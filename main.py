student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#  Don't change the code above 

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.
def student_grading():
    for key, val in student_scores.items():
        if int(val) >= 91 and int(val) <= 100:
            student_grades[key] = "Outstanding"
        elif int(val) >= 81 and int(val) <= 90:
            student_grades[key] = "Exceeds Expectations"
        elif int(val) >= 71 and int(val) <= 80:
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"
    
student_grading()
# Don't change the code below 
print(student_grades)