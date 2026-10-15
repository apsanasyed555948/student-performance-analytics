"""
Student Performance Analytics System
Sample educational project using Python, NumPy, and Pandas.
Replace the sample data in students.csv with your own permitted dataset.
"""

import numpy as np
import pandas as pd

DATA_FILE = "students.csv"
SUBJECTS = ["Python_Marks", "AI_Marks", "Data_Analysis_Marks"]
PASS_MARK = 40  # A student must score at least 40 in every subject to pass.


def assign_grade(average):
    """Return a letter grade based on the student's average mark."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def load_data(filename):
    """Load the CSV dataset and validate its required columns."""
    data = pd.read_csv(filename)
    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance_Percent"]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    if data.empty:
        raise ValueError("The dataset has no student records.")
    return data


def process_students(data):
    """Calculate total, average, grade, and pass/fail status for each student."""
    result = data.copy()
    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = np.round(result[SUBJECTS].mean(axis=1), 2)
    result["Grade"] = result["Average_Marks"].apply(assign_grade)

    # Loop demonstrates iteration and checks every subject for each student.
    pass_status = []
    for _, student in result.iterrows():
        passed = True
        for subject in SUBJECTS:
            if student[subject] < PASS_MARK:
                passed = False
                break
        pass_status.append("Pass" if passed else "Fail")

    result["Result"] = pass_status
    return result


def show_analysis(result):
    """Print student-level results and class/subject summaries."""
    print("\n" + "=" * 72)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 72)
    print("\nSTUDENT RESULTS")
    display_columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance_Percent"
    ]
    print(result[display_columns].to_string(index=False))

    print("\nCLASS SUMMARY")
    print(f"Number of students: {len(result)}")
    print(f"Class average (all subject marks): {result[SUBJECTS].to_numpy().mean():.2f}")
    print(f"Highest student average: {result['Average_Marks'].max():.2f}")
    print(f"Lowest student average: {result['Average_Marks'].min():.2f}")
    print(f"Students passed: {(result['Result'] == 'Pass').sum()}")
    print(f"Students failed: {(result['Result'] == 'Fail').sum()}")
    print(f"Average attendance: {result['Attendance_Percent'].mean():.2f}%")

    top_student = result.loc[result["Average_Marks"].idxmax()]
    low_student = result.loc[result["Average_Marks"].idxmin()]
    print(f"Top performer: {top_student['Name']} ({top_student['Average_Marks']:.2f})")
    print(f"Lowest performer: {low_student['Name']} ({low_student['Average_Marks']:.2f})")

    print("\nSUBJECT-WISE AVERAGES")
    subject_averages = result[SUBJECTS].mean().sort_values(ascending=False)
    for subject, average in subject_averages.items():
        print(f"{subject.replace('_Marks', '')}: {average:.2f}")

    print("\nDEPARTMENT-WISE AVERAGE MARKS")
    print(result.groupby("Department")[SUBJECTS].mean().mean(axis=1).round(2).to_string())

    print("\nTOP 5 STUDENTS")
    top_five = result.nlargest(5, "Average_Marks")
    print(top_five[["Name", "Department", "Average_Marks", "Grade"]].to_string(index=False))

    result.to_csv("student_results.csv", index=False)
    print("\nDetailed results saved to student_results.csv")


def main():
    try:
        data = load_data(DATA_FILE)
        result = process_students(data)
        show_analysis(result)
    except FileNotFoundError:
        print(f"Error: Could not find {DATA_FILE}. Keep it in the same folder as main.py.")
    except (ValueError, KeyError) as error:
        print(f"Data error: {error}")


if __name__ == "__main__":
    main()
