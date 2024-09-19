# Imports and helpers
import networkx as nx



"""
Step 1: Get input data.
"""
print("-" * 80)
print("STEP 1: INPUT DATA")
print("-" * 80)

problems_string = input("Enter a comma-separated list of the problems that will be assigned: ")
problems = [int(p) for p in problems_string.split(',')]
n = len(problems)

students = []
for i in range(n):   
    name = input(f"Enter the name of student {i}: ")
    students.append(name)

m = int(input("How many problems should each student get? "))



"""
Step 2: Do the assignments. This is done with the networkx bipartite configuration model, restarting from scratch whenever we assign a problem to a student multiple times.
"""
print("-" * 80)
print("STEP 2: ASSIGNING PROBLEMS TO SOLVE")
print("-" * 80)

done = False
while not done:
    assignment_graph = nx.bipartite.configuration_model([m] * n, [m] * n, create_using = nx.Graph())
    if assignment_graph.number_of_edges() == m * n:
        done = True

nx.relabel_nodes(assignment_graph, {i: students[i] for i in range(n)}, copy = False)
nx.relabel_nodes(assignment_graph, {j+n: problems[j] for j in range(n)}, copy = False)

assignments = {s: sorted([p for p in assignment_graph.adj[s].keys()]) for s in students}
max_name_length = max([len(s) for s in students])
for student, problem_list in assignments.items():
    print(f"{student:<{max_name_length}} {problem_list}")



"""
Step 3: Pick problems to grade. This is done with the networkx matching function for bipartite graphs.
"""
print("-" * 80)
print("STEP 3: PICKING PROBLEMS TO GRADE")
print("-" * 80)

grading = {s: nx.bipartite.maximum_matching(assignment_graph)[s] for s in students}

for student, problem in grading.items():
    print(f"{student:<{max_name_length}} {problem}")