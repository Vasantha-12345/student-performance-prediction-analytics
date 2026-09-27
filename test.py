
import pandas as pd

data = pd.read_csv("students.csv")

print(data)
print("Average Final Marks:", data["Final_Marks"].mean())
print("Highest Final Marks:", data["Final_Marks"].max())
print("Lowest Final Marks:", data["Final_Marks"].min())
print("\nStudent Performance:")

for index, row in data.iterrows():
    if row["Final_Marks"] >= 80:
        print(row["Student_ID"], "- Good Performance")
    else:
        print(row["Student_ID"], "- Needs Improvement")
        print("\nAttendance Analysis:")

average_attendance = data["Attendance"].mean()

print("Average Attendance:", average_attendance)

for index, row in data.iterrows():
    if row["Attendance"] >= average_attendance:
        print(row["Student_ID"], "- Attendance is Good")
    else:
        print(row["Student_ID"], "- Attendance is Low")
        import matplotlib.pyplot as plt

plt.scatter(data["Attendance"], data["Final_Marks"])

plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")

plt.show()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = data[["Attendance", "Study_Hours", "Assignment_Score", "Internal_Marks"]]
y = data["Final_Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("\nMachine Learning Model trained successfully!")
new_student = pd.DataFrame({
    "Attendance": [85],
    "Study_Hours": [5],
    "Assignment_Score": [82],
    "Internal_Marks": [84]
})

predicted_marks = model.predict(new_student)

print("\nPredicted Final Marks:", round(predicted_marks[0], 2))
from sklearn.metrics import mean_absolute_error, r2_score

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation")
print("MAE:", round(mae, 2))
print("R2 Score:", round(r2, 2))

import sqlite3

# Create database
conn = sqlite3.connect("students.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    Student_ID TEXT,
    Attendance REAL,
    Study_Hours REAL,
    Assignment_Score REAL,
    Internal_Marks REAL,
    Final_Marks REAL
)
""")

# Insert CSV data into database
data.to_sql("students", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("\nSQL Database created successfully!")
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

print("\nStudents with Final Marks above 80:")

cursor.execute("""
SELECT Student_ID, Final_Marks
FROM students
WHERE Final_Marks > 80
""")

for row in cursor.fetchall():
    print(row)

conn.close()

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# 1. Average Final Marks
cursor.execute("SELECT AVG(Final_Marks) FROM students")
print("\nAverage Final Marks:", round(cursor.fetchone()[0], 2))

# 2. Highest Final Marks
cursor.execute("SELECT MAX(Final_Marks) FROM students")
print("Highest Final Marks:", cursor.fetchone()[0])

# 3. Students with low attendance
cursor.execute("""
SELECT Student_ID, Attendance
FROM students
WHERE Attendance < 75
""")

print("\nStudents with Low Attendance:")
for row in cursor.fetchall():
    print(row)

conn.close()