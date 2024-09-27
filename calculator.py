# user inputs notes

labprogrammingproblems = int(input("Enter the number of labs completed: "))
quizzes = int(input("Enter the number of quizzes completed: "))
assignment1 = int(input("Enter grade for Assignment 1: "))
assignment2 = int(input("Enter grade for Assignment 2: "))
assignment3 = int(input("Enter grade for Assignment 3: "))
assignment4 = int(input("Enter grade for Assignment 4: "))
midterm1 = int(input("Enter grade for Midterm 1: "))
midterm2 = int(input("Enter grade for Midterm 2: "))
final = int(input("Enter grade for Final Exam: "))
midterms = int(input("Enter grade for Midterms and Final Preparation: "))

# weights

weight1 = 20
weight2 = 15
weight3 = 16
weight4 = 25
weight5 = 18
weight6 = 6

# calculator1 for labs and quizzes (the ones out of /6)

def calculator1(grade: int, weight: int):
    return grade/6 * weight

# calculator2 for 4 assignments (the ones out of /100)

def calculator2(grade1: int, grade2: int, grade3: int, grade4: int, weight: int):
    return (grade1 + grade2 + grade3 + grade4)/400 * weight

# calculator3 for 2 midterms (the ones out of /100)

def calculator3(grade1: int, grade2: int, weight: int):
    return (grade1 + grade2)/200 * weight

# calculator4 for final, midterm and final preparation (the ones out of /100)

def calculator4(grade: int, weight: int):
    return grade/100 * weight

result1 = calculator1(labprogrammingproblems, weight1)
result2 = calculator1(quizzes, weight2)
result3 = calculator2(assignment1, assignment2, assignment3, assignment4, weight3)
result4 = calculator3(midterm1, midterm2, weight4)
result5 = calculator4(final, weight5)
result6 = calculator4(midterms, weight6)

# prints the final grade

print(int(result1 + result2 + result3 + result4 + result5 + result6))
