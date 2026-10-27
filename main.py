import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    calculate_grade,
    check_pass_fail
)

# Load the student dataset
df = pd.read_csv("students.csv")

# Validate student data
subjects = ["Python", "AI", "Mathematics"]

if df[subjects].isnull().any().any():
    raise ValueError("Student marks contain missing values.")

if not df[subjects].apply(
    lambda column: column.between(0, 100).all()
).all():
    raise ValueError("Marks must be between 0 and 100.")

if not df["Attendance"].between(0, 100).all():
    raise ValueError("Attendance must be between 0 and 100.")

print("Data validation successful.")

print("\n===== STUDENT PERFORMANCE ANALYTICS SYSTEM =====")
print("\nStudent Dataset:")
print(df.to_string(index=False))

print("\nTotal number of students:", len(df))

# Calculate student performance
subjects = ["Python", "AI", "Mathematics"]

df["Total"] = 0
df["Average"] = 0.0
df["Grade"] = ""
df["Result"] = ""

for index, student in df.iterrows():
    marks = student[subjects].to_numpy(dtype=float)

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    result = check_pass_fail(marks)

    df.at[index, "Total"] = total
    df.at[index, "Average"] = round(average, 2)
    df.at[index, "Grade"] = grade
    df.at[index, "Result"] = result

print("\n===== STUDENT RESULTS =====")
print(
    df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]]
    .to_string(index=False)
)


# Class Performance Analysis
print("\n===== CLASS PERFORMANCE ANALYSIS =====")

print("Overall Class Average:", round(df["Average"].mean(), 2))

highest_student = df.loc[df["Average"].idxmax()]
lowest_student = df.loc[df["Average"].idxmin()]

print(
    "Top Performer:",
    highest_student["Name"],
    "-",
    highest_student["Average"]
)

print(
    "Lowest Performer:",
    lowest_student["Name"],
    "-",
    lowest_student["Average"]
)

# Pass and Fail Statistics
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("Students Passed:", pass_count)
print("Students Failed:", fail_count)

# Subject-wise Average
print("\n===== SUBJECT-WISE AVERAGES =====")

for subject in subjects:
    average = np.mean(df[subject].to_numpy())
    print(subject, "Average:", round(average, 2))

# Top 5 Students
print("\n===== TOP 5 STUDENTS =====")

top_students = df.nlargest(5, "Average")

print(
    top_students[["Name", "Average", "Grade"]]
    .to_string(index=False)
)


# Save the analyzed results
df.to_csv("student_results.csv", index=False)
print("\nAnalysis results saved to student_results.csv")