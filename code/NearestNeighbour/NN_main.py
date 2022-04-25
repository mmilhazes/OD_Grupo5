file = open('kro124p.atsp','r') # Open txt file. To change the file just change "ft53.atsp" to "kro124p.atsp"
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

    min_distance = min(distance_for_every_run)
    starting_point = distance_for_every_run.index(min_distance)
    print(min_distance, starting_point)

# Calculate Standart deviation
average = sum(distance_for_every_run)/len(distance_for_every_run)
print('This is average')
print(average)
variation1= [ (x-average)**2 for x in distance_for_every_run ]
variation = (sum(variation1)/len(variation1))**(1/2)
print('The Standart deviation is')
print(variation)
