"""
Z-Score:
Definition:
Z-score tells us how many standard deviations a data point is away from the mean.

Formula:
z = (x - μ) / σ

Where:
x = data value
μ = mean
σ = standard deviation

Outlier Rule:
|Z| > 3 → Outlier

Advantages:
- Works well for normally distributed data.
- Shows exactly how far a value is from the mean.
- Useful for comparing values from different datasets.

Disadvantages:
- Sensitive to extreme values.
- Mean and standard deviation can be distorted by outliers.

--------------------------------------------------

IQR (Interquartile Range):
Definition:
IQR measures the spread of the middle 50% of the data.

Formula:
IQR = Q3 - Q1

Where:
Q1 = 25th percentile
Q3 = 75th percentile

Outlier Rule:
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR

Any value outside these bounds is considered an outlier.

Advantages:
- Robust to extreme values.
- Works well for skewed data.
- Reliable for outlier detection.

Disadvantages:
- Does not tell how many standard deviations a value is from the center.
- Less useful when data is perfectly normal and standard deviation is important.

--------------------------------------------------

Which One Should You Use?

Use Z-Score:
- When data is approximately normally distributed.
- When mean and standard deviation are meaningful.
- When you want to measure distance from the mean in standard deviations.

Use IQR:
- When data is skewed.
- When the dataset contains extreme values.
- When the goal is reliable outlier detection.

Interview Summary:
Z-score measures how many standard deviations a value is from the mean, 
while IQR detects outliers using quartiles and the middle 50% of the data.
For normally distributed data, Z-score is preferred. 
For skewed data and robust outlier detection, IQR is usually the better choice."""