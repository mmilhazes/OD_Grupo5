import random
import csv

# n=5

# mat =[[0 for i in range(n)] for j in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i!=j:
#             x = int(input(f'Enter distance between location {i} and location {j} : '))
#             mat[i][j] = x

# print('Distances Matrix is :')
# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mat]))

# These are the necessary variables.
# values = []
# n_nos = []
# matrix = []

# # This opens the input file as a csv.
# input_file = open('./Traveling_Salesman_Problem_main/input7.txt', 'r')
# reader = csv.reader(input_file)

# # This reads in the values.
# for row in reader:
#     values.append(row)

# # This retrieves the number of nodes.
# n_nos = values[0]
# n_nos = list(map(int, n_nos))
# n_nos = int(n_nos.pop(0))
# values.pop(0) # Discard the top value.
# print(n_nos)
# # This retrieves the matrix values.
# mat = [[int(int(j)) for j in i] for i in values]

file = open('./NN/kro124p.atsp', 'r') # Open txt file. To change the file just change "ft53.atsp" to "kro124p.atsp"
read_file = file.read() # Read the txt file
split_file = read_file.split('\n') # Splits the file in lines
dimension_line = split_file[3]
n = dimension_line.split(' ')
n_nos = int(n[1]) # Give us the number of nodes (n) of the matrix. Dimension of the matrix is nxn
space = ''
for line in split_file[7:-2]:
    space = space + line
lista_num = [int(s) for s in space.split(' ') if s != '']

mat=[lista_num[i:i + n_nos] for i in range(0, len(lista_num), n_nos)]

#start= random.randint(0,n_nos-1)
distance_for_every_run = []
for s in range(n_nos-1):
    start = int(s)
    tour=[start]
    total_distance=0

    for i in range(n_nos-1):

        m=next(x for x in list(range(0,n_nos)) if x not in tour)
        
        for j in range(n_nos):
            if j not in tour:
                if mat[start][j] < mat[start][m]:
                    m=j
        
        total_distance+=mat[start][m]
        tour.append(m)
        start = m


    tour.append(tour[0])
    total_distance+=mat[start][tour[0]]
    distance_for_every_run.append(total_distance)

    print(f"\nStart location : {tour[0]}")
    print("Tour :",tour)
    print(f"Total distance is : {total_distance}")

    max_distance = max(distance_for_every_run)
    min_distance = min(distance_for_every_run)
    avg_distance = average(distance_for_every_run)
    starting_point_max = distance_for_every_run.index(max_distance)
    starting_point_min = distance_for_every_run.index(min_distance)
    print(min_distance, starting_point_min)
    print(max_distance, starting_point_max)
    print(avg_distance)
    
# Calculate Standart deviation
average = sum(distance_for_every_run)/len(distance_for_every_run)
print('\n This is average')
print(average)
variation1= [ (x-average)**2 for x in distance_for_every_run ]
variation = (sum(variation1)/len(variation1))**(1/2)
print('\n The Standart deviation is')
print(variation)
