import numpy as np
import pandas as pd

while True:
    student_data = {}
    num_students = int(input("Enter number of students: "))

    for _ in range(num_students):
        name = input("\nEnter student name: ")
        math = float(input(f"Enter {name}'s Math marks: "))
        science = float(input(f"Enter {name}'s Science marks: "))
        english = float(input(f"Enter {name}'s English marks: "))
        student_data[name] = {'Math': math, 'Science': science, 'English': english}

    print("\n📚 Student Data Dictionary:")
    for student, marks in student_data.items():
        print(f"{student}: {marks}")

    confirm = input("\nIs the entered data correct? (Y/N): ").strip().lower()
    if confirm == 'y':
        break
    else:
        print("\n🔄 Let's re-enter the data...\n")

df = pd.DataFrame(student_data).T

print("\n📋 Full Marksheet:")
print(df)

marks_array = df.to_numpy()
average_scores = np.mean(marks_array, axis=1)
max_scores = np.max(marks_array, axis=1)
min_scores = np.min(marks_array, axis=1)

df['Average'] = average_scores
df['Max'] = max_scores
df['Min'] = min_scores

print("\n📊 Marksheet with Stats:")
print(df)

print("\n📈 Subject-wise Averages:")
print(df[['Math', 'Science', 'English']].mean())

print("\n🔥 Topper:")
topper = df['Average'].idxmax()
print(f"{topper} with an average of {df['Average'].max():.2f}")
print("\n📉 Lowest Scorer:")
lowest_scorer = df['Average'].idxmin()
print(f"{lowest_scorer} with an average of {df['Average'].min():.2f}")
print("\n📊 Subject-wise Highest and Lowest Scores:")
print(df[['Math', 'Science', 'English']].agg(['max', 'min']))
print("\n📊 Overall Highest and Lowest Scores:")
print(f"Highest: {df['Max'].max()} in {df['Max'].idxmax()}")
print(f"Lowest: {df['Min'].min()} in {df['Min'].idxmin()}")
print("\n📊 Overall Average Score:")
print(f"{df['Average'].mean():.2f}")