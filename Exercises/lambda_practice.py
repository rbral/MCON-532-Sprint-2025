# 1. Use lambda with dictionary comprehension to map names to name lengths
names = ['david', 'lila', 'miriam', 'chana']
name_lengths = {
    # TODO: Use lambda to compute length
    name: (lambda x: len(x))(name) for name in names
}
print("Name lengths:", name_lengths)

# 2. Filter a list to keep only numbers divisible by 3
numbers = list(range(1, 20))
divisible_by_3 = list(
    # TODO: Use filter with lambda
    filter(lambda x: x % 3 == 0, numbers)
)
print("Divisible by 3:", divisible_by_3)

# 3. Filter a dictionary to keep only values > 75
scores = {'Eli': 88, 'Sara': 74, 'Mo': 91, 'Rachel': 68}
high_scores = {
    # TODO: Use dictionary comprehension and lambda
    k: v for k, v in scores.items() if (lambda score: score > 75)(v)
}
print("High scores:", high_scores)

# 4. Sort a list of (name, age) tuples by age
people = [('Eli', 28), ('Sara', 21), ('Mo', 35), ('Rachel', 25)]
sorted_people = sorted(
    # TODO: Use lambda to sort by age
    people, key=lambda x: x[1]
)
print("Sorted people by age:", sorted_people)

# 5. Sort dictionary entries by value (descending)
grades = {'Eli': 88, 'Sara': 74, 'Mo': 91, 'Rachel': 68}
sorted_grades = dict(
    # TODO: Use sorted with lambda
    sorted(grades.items(), key=lambda x: x[1])
)
print("Grades sorted:", sorted_grades)