"""
Encoding is the process of converting data from one form to another. 
In the context of machine learning and data processing, 
encoding is often used to convert categorical data into a numerical format 
that can be easily processed by algorithms.

Ordinal encoding is a type of encoding that assigns a unique integer 
to each category in a categorical variable.It follows orders the categories 
based on their natural order or hierarchy.
For example, if we have a categorical variable "Color" with three categories:
- Red
- Green
- Blue
We can assign the following integer values:
- Red: 0
- Green: 1
- Blue: 2


Nominal encoding, on the other hand, does not assign any order or hierarchy to the categories.
For the same "Color" variable, we can use one-hot encoding to represent 
the categories as binary vectors:
- Red: [1, 0, 0]
- Green: [0, 1, 0]
- Blue: [0, 0, 1]

Ordinal encoding is suitable when there is a natural order or hierarchy among the categories,
while nominal encoding is appropriate when there is no natural order or hierarchy.

"""


