# Student Performance Analytics System

A beginner-friendly Python data-analysis project using Python, NumPy, and Pandas.

## Features
- Reads student records from `students.csv` using Pandas.
- Calculates total and average marks.
- Assigns grades using a clear grading rule.
- Marks a student as Pass only if they score at least 40 in every subject.
- Reports class statistics, attendance, subject-wise averages, department averages, and the top five students.
- Saves processed results to `student_results.csv`.

## Files
- `main.py` - main program
- `students.csv` - sample dataset with 20 student records
- `Project_Documentation.docx` - documentation template
- `requirements.txt` - required libraries

## Requirements
Python 3.9 or newer is recommended.

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

## Run the project
Place `main.py` and `students.csv` in the same folder, then run:
```bash
python main.py
```

## Grading rule
- A+: 90 and above
- A: 80–89.99
- B: 70–79.99
- C: 60–69.99
- D: 50–59.99
- F: below 50

Pass/fail rule: a student passes only when each subject mark is at least 40. Update these rules if your trainer specified different criteria.

## Important
The included records are sample data for demonstrating the program. Review the code, run it yourself, and adapt the project to your own work and your trainer's requirements before submission.
