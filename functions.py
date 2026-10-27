import numpy as np


def calculate_total(marks):
    return np.sum(marks)


def calculate_average(marks):
    return np.mean(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def check_pass_fail(marks):
    for mark in marks:
        if mark < 35:
            return "Fail"
    return "Pass"