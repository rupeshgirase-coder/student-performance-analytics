# Student Performance Analytics System

## 1. Project Overview
The Student Performance Analytics System is a Python-based data analysis project that analyzes student marks and attendance. It calculates student performance metrics and generates meaningful class-level insights.

## 2. Objectives
- Calculate total and average marks for each student.
- Assign grades based on average marks.
- Identify pass and fail students.
- Analyze subject-wise performance.
- Find the highest and lowest performers.
- Identify the top five students.
- Export analyzed results to a CSV file.

## 3. Technologies Used
- Python
- Pandas
- NumPy
- CSV

## 4. Dataset Description
The dataset contains 20 student records with the following fields:
- Student ID
- Name
- Department
- Python marks
- AI marks
- Mathematics marks
- Attendance percentage

## 5. Project Files
- `main.py` — Main program and performance analysis.
- `functions.py` — Reusable calculation functions.
- `students.csv` — Original student dataset.
- `student_results.csv` — Generated analysis results.

## 6. Key Features
- Data loading using Pandas.
- Data validation for marks and attendance.
- Total and average calculations using NumPy.
- Grade assignment and pass/fail classification.
- Subject-wise average analysis.
- Class performance statistics.
- Top-five student ranking.
- Export of results to CSV.

## 7. Grading Rules
Grades are assigned according to the student's average marks:
- A+: 90 and above
- A: 80 to below 90
- B: 70 to below 80
- C: 60 to below 70
- D: 40 to below 60
- F: Below 40

A student passes only if every subject mark is at least 35.

## 8. How to Run
1. Install Python.
2. Install the required libraries:
   `python -m pip install pandas numpy`
3. Keep `main.py`, `functions.py`, and `students.csv` in the same folder.
4. Run:
   `python main.py`

## 9. Expected Outcome
The program displays individual student results, class performance statistics, subject-wise averages, and the top five students. It also saves the analyzed dataset to `student_results.csv`.

## 10. Future Enhancements
- Create charts for subject-wise performance.
- Add a graphical user interface.
- Analyze attendance and its relationship with marks.
