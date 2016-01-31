list1 = [2, 5, 8]
list2 = [1, 3, 4]
result = []
print zip(list1, list2)
for a, b in zip(list1, list2):
	result.append(a + b)

print result