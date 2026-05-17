import numpy as np

# Rows = students (10 students)
# Columns = subjects (English, Math, Science)

marks = np.array([
    [75, 80, 78],
    [88, 92, 85],
    [60, 70, 65],
    [90, 95, 93],
    [55, 60, 58],
    [72, 68, 70],
    [85, 87, 90],
    [78, 75, 80],
    [66, 72, 68],
    [91, 89, 94]
])

print("Marks of 10 students (English, Math, Science):")
print(marks)

# Example operations
print("\nAverage marks of each subject:")
print(np.mean(marks, axis=0))  # column-wise average

#Mark of each student
math_marks=marks[:,1]
print("\nMarks of each student in Math:",math_marks)
math_avg=np.mean(math_marks)
print("\nAverage marks in Math:",math_avg)

max_math_marks=np.max(math_marks)
print("\nMaximum marks in Math:",max_math_marks)

#Median

median_math_marks=np.median(math_marks)
print("\nMedian marks in Math:",median_math_marks)

#Standard deviation

std_math_marks=np.std(math_marks)
print("\nStandard deviation of marks in Math:",std_math_marks)

