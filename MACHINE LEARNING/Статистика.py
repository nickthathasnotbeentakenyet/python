import numpy as np

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]

print("mean:", np.mean(data))
print("median:", np.median(data))
print("50th percentile (median):", np.percentile(data, 50))
print("25th percentile:", np.percentile(data, 25))
print("75th percentile:", np.percentile(data, 75))
print("standard deviation:", np.std(data))
print("variance:", np.var(data))

# ----------------------------------------------
data = [15, 16, 18, 19, 22, 24, 29, 30, 34]

# MEAN is 23
# 15 is 8 away from the mean (since 23-15=8)

distances = [8, 7, 5, 4, 1, 1, 6, 7, 11]

# если сложить квадраты значений разброса , поделить на количество значений, то получим variance (отклонение)
# 362 / 9 = 40.22

# чтобы получить std deviation (стандартный разброс), надо получить корень из отклонения: = 6.34
# среднее 23 - 6.34 и 23 + 6.34: 
# 16.66 (нижняя граница) и 29.34 (верхняя граница)
