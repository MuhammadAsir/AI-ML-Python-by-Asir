import numpy as np


study=np.array([2, 3, 4, 5, 6])
score=np.array([70, 60, 90, 55, 20])
correlation=np.corrcoef(study, score)
print(correlation)
