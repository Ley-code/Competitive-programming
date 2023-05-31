def roundgrades(grades):
    new_grades = []
    for grade in grades:
       if grade < 37:
           new_grades.append(grade)
       else:
           if grade % 5 == 0 or grade % 5 <=2:
               new_grades.append(grade)
           else:
               new_grades.append(grade-grade%5+5)
    return new_grades
