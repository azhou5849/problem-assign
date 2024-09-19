# Imports and helpers
from sys import exit
from random import shuffle

def proceed():
    c = input("Do you wish to proceed? (Y/N) ")
    if c == 'N' or c == 'n':
        exit(1)



"""
Step 1: Get input data. There are n students and n problems, and each student will be assigned m problems so that every problem is assigned to m students.
"""
print("-" * 80)
print("STEP 1: INPUT DATA")
print("-" * 80)

problems_string = input("Enter a comma-separated list of the problems that will be assigned: ")
problems = [int(p) for p in problems_string.split(',')]
n = len(problems)
print(f"You have provided a list of {n} problems:", problems)
proceed()

print("-" * 80)

students = []
for i in range(n):   
    name = input(f"Enter the name of student {i}: ")
    students.append(name)
shuffle(students)
print(f"There are {n} students in the class, named:")
for i in range(n):
    print(f"{i:>2}. {students[i]}")
proceed()

print("-" * 80)

m = int(input("How many problems should each student get? "))
print(f"Each student should receive {m} problems.")
proceed()



"""
Step 2: Do the assignments. This is done with the networkx bipartite configuration model, restarting from scratch whenever we assign a problem to a student multiple times.
"""
print("-" * 80)
print("STEP 2: ASSIGNING PROBLEMS TO SOLVE")
print("-" * 80)

done = False
while not done:
    problems_per_student = {s: [] for s in students}
    students_per_problem = {p: [] for p in problems}
    done = True  # set to False when a duplicate assignment occurs

    problem_copies = problems * m
    shuffle(problem_copies)
    for s in students:
        provisional_list = []
        for _ in range(m):
            p = problem_copies.pop()
            provisional_list.append(p)
            students_per_problem[p].append(s)
        print(f"Problems for {s}: ", provisional_list)
        if len(provisional_list) != len(set(provisional_list)):
            print("Duplicate detected! Restarting...\n")
            done = False
            break
        else:
            problems_per_student[s] = sorted(provisional_list)


# Display problem assignments
print("-" * 80)
print("Students assigned to each problem:")
for p in problems:
    print(f"{p:>2}: {students_per_problem[p]}")
print("Problems assigned to each student:")
for s in students:
    print(f"{s:<15} {problems_per_student[s]}")
proceed()



"""
Step 3: Pick one problem from each student to grade, so that every problem is graded exactly once. This is done with 
"""
print("-" * 80)
print("STEP 3: PICKING PROBLEMS TO GRADE")
print("-" * 80)

# Initialise
unpaired_students = list(range(n))
selections = {problem: None for problem in range(n)}

# Iterate the offer-and-accept process
rounds = {student: 0 for student in range(n)}
while len(unpaired_students) > 0:
    print(unpaired_students)
    claimed_students = []
    for student in unpaired_students:
        problem = problems_per_student[student][rounds[student]]
        rounds[student] += 1
        if selections[problem] is None:
            selections[problem] = student
        else:
            old_student = selections[problem]
            if student < old_student:
                selections[problem] = student
    print(selections)
    unpaired_students = [i for i in range(n) if i not in selections.values()]

# Display final selection
print(selections)