lisa = {
    "name": "Lisa",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
cathy = {
    "name": "Cathy",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
lynn = {
    "name": "Lynn",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
tony = {
    "name": "Tony",
    "homework": [0.0, 80.0, 72.0, 25.0],
    "quizzes": [0.0, 80.0, 75.0],
    "tests": [95.0, 100.0]
}

# function to define average of a list
def average(numbers):
    total = sum(numbers)
    total = float(total)
    result = total / len(numbers)
    return result

#function to calculate student grade
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    #calculating grade when each category is weighted
    return .1 * homework + .3 * quizzes + .6 * tests
