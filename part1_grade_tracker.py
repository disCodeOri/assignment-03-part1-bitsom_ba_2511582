# Part 1: Student Grade Tracker
# This script processes raw student data, analyzes marks, generates a report, and performs basic string operations.

# Raw input data that needs cleaning
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

print("--- Processing Students ---")
for student in raw_students:
    # Standardizing names and converting numeric strings to integers
    name = student["name"].strip().title()
    roll = int(student["roll"])
    marks = [int(m) for m in student["marks_str"].split(", ")]
    
    # Validating that names only contain letters
    is_valid = all(word.isalpha() for word in name.split())
    status = "✓ Valid name" if is_valid else "✗ Invalid name"
    print(f"{name: <15} | {status}")
    
    # Printing the profile card format
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")
    
    cleaned_students.append({"name": name, "roll": roll, "marks": marks})

# Showing specific data for roll number 103 as instructed in the assignment
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nStudent 103 Name: {s['name'].upper()} / {s['name'].lower()}")

# Task 2: Marks Analysis
print("\n--- Task 2: Marks Analysis ---")
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# Numerical scores to letter grades mapper
def get_grade(mark):
    if mark >= 90: return "A+"
    if mark >= 80: return "A"
    if mark >= 70: return "B"
    if mark >= 60: return "C"
    return "F"

for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks[i]} | Grade: {get_grade(marks[i])}")

# Calculating totals and averages
total_marks = sum(marks)
avg_marks = round(total_marks / len(marks), 2)
max_idx = marks.index(max(marks))
min_idx = marks.index(min(marks))

print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {avg_marks}")
print(f"Highest scoring subject: {subjects[max_idx]} ({marks[max_idx]})")
print(f"Lowest scoring subject: {subjects[min_idx]} ({marks[min_idx]})")

# Loop for users to continuously input new subjects until "done" is inputted
print("\n--- New Subject Entry System ---")
new_subjects = 0
while True:
    sub = input("Enter subject name (or 'done' to stop): ").strip()
    if sub.lower() == 'done':
        break
    
    val = input(f"Enter marks for {sub} (0-100): ")
    
    # Non-numeric inputs handler
    try:
        val = float(val)
        if 0 <= val <= 100:
            subjects.append(sub)
            marks.append(val)
            new_subjects += 1
        else:
            print("Warning: Marks must be between 0 and 100.")
    except ValueError:
        print("Warning: Invalid input. Please enter a numeric value.")

updated_avg = round(sum(marks) / len(marks), 2)
print(f"\nAdded {new_subjects} subjects.")
print(f"Updated average: {updated_avg}")

# Task 3: Class Performance Summary
print("\n--- Task 3: Class Performance Summary ---")
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print(f"{'Name': <18} | {'Average': <7} | {'Status'}")
print("-" * 40)

pass_count = 0
fail_count = 0
student_averages = []

# Calculating status for each student in the class list
for name, marks_list in class_data:
    avg = sum(marks_list) / len(marks_list)
    status = "Pass" if avg >= 60 else "Fail"
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1
    student_averages.append({"name": name, "avg": avg})
    print(f"{name: <18} | {avg: >7.2f} | {status}")

# Calculating final class stats
topper = max(student_averages, key=lambda x: x["avg"])
class_avg = sum(s["avg"] for s in student_averages) / len(student_averages)

print("\nSummary:")
print(f"Passed: {pass_count}, Failed: {fail_count}")
print(f"Class Topper: {topper['name']} ({topper['avg']:.2f})")
print(f"Class Average: {class_avg:.2f}")

# Task 4: String Manipulation Utility
print("\n--- Task 4: String Manipulation Utility ---")
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip()
print(f"1. Stripped: {clean_essay}")
print(f"2. Title Case: {clean_essay.title()}")

# Calculating occurrences regardless of casing
count = clean_essay.lower().count("python")
print(f"3. Count of 'python': {count}")

replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"4. Replaced: {replaced_essay}")

# Splitting sentences by period and space
sentences = clean_essay.split(". ")
print(f"5. Sentences list: {sentences}")

print("6. Numbered Sentences:")
for i, sentence in enumerate(sentences, 1):
    # Adding a period if it happens to be missing
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")
