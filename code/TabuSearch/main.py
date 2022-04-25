from solution import Solution
import matplotlib.pyplot as plt
import sys
import numpy as np

def tabu_search(max_iter, tabu_tenure, neighbor_size=1000, init='No'):

    tabu = dict()
    sol = Solution()
    if init == 'NN':
        sol.nearest_neighborhood_initialization() 
    for i in range(sol.number_of_nodes):
        for j in range(sol.number_of_nodes):
            tabu[(i,  j)] = 0

    obj = []
    my_list = []
    average_list = []
    count = 0

    best_obj = sys.float_info.max
    while count <= max_iter:

        pair = sol.best_neighbor_w_tabu_aspiration(neighbor_size, tabu, best_obj)
        tabu[pair] += tabu_tenure
        for i in range(sol.number_of_nodes):
            for j in range(sol.number_of_nodes):
                if tabu[(i, j)] > 0:
                    tabu[(i, j)] -= 1
        sol.swap_operation(pair[0], pair[1])
        obj.append(sol.get_obj_func_value())
        count += 1

        average_cost = sum(obj)/len(obj)
        average_list.append(average_cost)

        if sol.get_obj_func_value() < best_obj:
            best_obj = sol.get_obj_func_value()
            my_list.append(best_obj)
        else:
            my_list.append(best_obj)

    print('Best Cost: ', str(best_obj))

    plt.plot(list(range(len(my_list))), my_list)
    plt.plot(list(range(len(average_list))), average_list)
    plt.xlabel('Iteration No')
    plt.ylabel('Cost')
    plt.title('Tabu Search')
    plt.legend(['Evaluation of the Optimal Cost', 'Average Cost'])
    plt.show()

    return sol



if __name__ == '__main__':

    import time
    s = time.time()
    sol = tabu_search(200, 10, init='NN')
    print(sol.get_route())
    e = time.time()
    print('cpu time: ', str(e-s))