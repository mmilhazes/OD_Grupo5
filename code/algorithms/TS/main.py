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
        print ("n ite", count, end = " ")

        if sol.get_obj_func_value() < best_obj:
            best_obj = sol.get_obj_func_value()
            my_list.append(best_obj)
        else:
            my_list.append(best_obj)

    # Print the results
    print('incumbent value: ', str(best_obj))
    plt.plot(list(range(len(obj))), obj)
    plt.xlabel('Iteration No')
    plt.ylabel('Objective Function Value for every iteration')
    plt.title('Tabu Search')
    plt.show()

    plt.plot(list(range(len(my_list))), my_list)
    plt.xlabel('Iteration No')
    plt.ylabel('Current Optimal Objective Function Value')
    plt.title('Tabu Search')
    plt.show()

    # dt = [('len', float)]
    # A = sol.distance_matrix/100
    # A = A.view(dt)
    # print('aaaaaaaaaaaa')
    # G = nx.from_numpy_matrix(A)
    # G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    
    # print('bbbbbbbbbb')
    # G = nx.drawing.nx_agraph.to_agraph(G)
    # print('cccccccccc')
    # # G.node_attr.update(color="red", style="filled")
    # # G.edge_attr.update(color="blue", width="2.0")

    # plt.draw('/tmp/out.png', format='png', prog='neato')

    return sol



if __name__ == '__main__':

    import time
    s = time.time()
    # Choose the parameters
    sol = tabu_search(500, 100, init='NN')
    print(sol.get_route())
    e = time.time()
    print('cpu time: ', str(e-s))
