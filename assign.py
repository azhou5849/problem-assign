# Imports
from random import shuffle


"""
Stage 1: With n students and n problems, assign m problems to each student so that each problem is assigned to m students. This is essentially done with the configuration model, restarting from scratch whenever we select a problem to a student multiple times.
"""
# Get input data
n = int(input("How many students are there? (There will be the same number of problems.) "))
m = int(input("How many problems should each student get? "))

# Main loop
while True:
    success = True
    student_edges = {i: [] for i in range(n)}
    problem_edges = {j: [] for j in range(n)}
    problem_stubs = list(range(n)) * m
    shuffle(problem_stubs)
    for i in range(n):
        for _ in range(m):
            j = problem_stubs.pop()
            if j in student_edges[i]:
                success = False
                break
            else:
                student_edges[i].append(j)
                problem_edges[j].append(i)
        if len(student_edges[i]) < m:
            break
    if success:
        break

# Display problem assignments
print(student_edges)
print(problem_edges)


"""
Stage 2: Pick 1 problem from each student to grade, so that every problem is graded exactly once. We can essentially apply Gale-Shapley for this.
"""
# Initialise
unpaired_students = list(range(n))
unpaired_problems = list(range(n))
selection = []

# Iterate the offer-and-accept process
round = 0
while len(unpaired_students) > 0:
    claimed_students = []
    for i in unpaired_students:
        j = student_edges[i][round]
        if student_edges[i][round] in unpaired_problems:
            selection.append((i,j))
            claimed_students.append(i)
            unpaired_problems.pop(unpaired_problems.index(j))
    for i in claimed_students:
        unpaired_students.pop(unpaired_students.index(i))
    round += 1

# Display final selection
print(selection)