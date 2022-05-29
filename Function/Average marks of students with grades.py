def avg_marks(marks):
    total_subjects=len(marks)
    sum_of_marks=sum(marks)
    average=sum_of_marks/total_subjects
    return average

def compute_grade(average_grade):
  
    if average_grade >=90:
        grade='A'
    elif average_grade >=80:
        grade='B'
    elif average_grade >=70:
        grade='C'
    return grade

marks=[90,75,84,90]
average=avg_marks(marks)
print('your average marks is ',average)

grade=compute_grade(average)
print('Your grade is ',grade)
