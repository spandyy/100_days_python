student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#so here we accessed the keys and value of the dictionary 
#
student_grades = {}


for i in student_scores:
    score=student_scores[i]
    if score > 90:
      student_scores[i] = "Outstanding"
    elif score > 80:
      student_scores[i] = "Exceeds Expectations"
    elif score > 70:
      student_scores[i] = "Acceptable"
    else:
      student_scores[i] = "Fail"

    
print(student_scores)

for i in student_scores:
    print(f"{i} : {student_scores[i]}")