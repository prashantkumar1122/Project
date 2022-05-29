def avg_marks(marks):
    total_subjects=len(marks)
    sum_of_marks=sum(marks)
    average=sum_of_marks/total_subjects
    return average

marks=[90,75,84,90]
average=avg_marks(marks)

print('your average marks is ',average)
