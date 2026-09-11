import numpy as np

a=np.array([[1, 2, 3],
            [5, 6, 7]
            ])

b=np.array([[9, 10],
            [13, 14],
            [17, 18]
            ])

#Matrix Multiplication
dot_product=np.dot(a,b)
print(dot_product)

#Matric Trace
trace=np.trace(a)
print(trace)


x=np.array([[4,2],[3,6]])
#Matrix Determinant
det_of_x=np.linalg.det(x)
print(det_of_x)

"""Rank is a number of linearly independent rows or columns in a matrix,
suppose we have a matrix with 3 rows and 4 columns
 but only 2 rows are linearly independent then the rank of the matrix is 2"""

rank=np.linalg.matrix_rank(a)
print(rank)

#Correlation Coefficient
study=np.array([2, 3, 4, 5, 6])
score=np.array([70, 75, 80, 85, 90])
correlation=np.corrcoef(study, score)
print(correlation)