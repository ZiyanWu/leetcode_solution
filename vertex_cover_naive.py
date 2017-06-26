from itertools import *

def validity_check(cover, graph):
    # Your code should go here.
    n=len(graph)
    for row in range(n):
        for col in range(n):
            if graph[row][col]==1:
                if(cover[row]!=1 and cover[col]!=1):
                    return False
    return True

def vertex_cover_naive(input_graph):
    n = len(input_graph)
    minimum_vertex_cover = n
    # loops through all strings of 0s and 1s of length n
    for assignment in product([0,1], repeat=n):
        # Your code should go here.
        # Based on the assignment (a list of 0s and 1s)
        # - Check the assignment is valid
        # - Calculate the size of assignment
        # - Update the minimum_vertex_cover variable if appropriate
        if(validity_check(list(assignment),input_graph)==True):
            vertex_cover=list(assignment).count(1)
            if(vertex_cover<minimum_vertex_cover):
                minimum_vertex_cover=vertex_cover

    # End of your code
    return minimum_vertex_cover

def test():
    graph = [[0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0]]
    print(vertex_cover_naive(graph))
    #assert vertex_cover_naive(graph)==3 

# If you've not seen testing like this before, all you need to do is
# to call test(). If the tests pass, you'll get no output. If they don't
# you'll get an assertion error. Don't forget to remove the call to the
# test before submitting your code.

test()