import numpy as np

Stud_marks = np.array( [
    
 [80, 70, 90],
 [60, 65, 75],
 [65, 55, 95],
 [90, 55, 85],
 [70, 85, 65]

])

print("Dataset:\n", Stud_marks)

total_marks = np.sum(Stud_marks, axis=1)
print("\nTotal marks per student:", total_marks)

total_avg = np.average(Stud_marks, axis=1)
print("\nTotal avg marks per student:", total_avg)

max_marks = np.max(Stud_marks, axis=0)
print("\nMax marks per student:", max_marks)

min_marks = np.min(Stud_marks, axis=0)
print("Lowest marks in each subject:", min_marks)

top_student_index = np.argmax(total_avg)
print("\nTop student index:", top_student_index)

# Step 7: Normalize data (0–1 scale)
normalized = Stud_marks / 100
print("\nNormalized Data:\n", normalized)

# Step 8: Students scoring >80 in ALL subjects
condition = np.all(Stud_marks > 80, axis=1)
high_scorers = Stud_marks[condition]

print("\nStudents scoring >80 in all subjects:\n", high_scorers)