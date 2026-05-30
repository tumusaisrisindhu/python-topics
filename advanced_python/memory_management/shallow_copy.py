import copy

data = [[1, 2], [3, 4]]

new_data = copy.copy(data)

new_data[0].append(100)

print(data)
print(new_data)