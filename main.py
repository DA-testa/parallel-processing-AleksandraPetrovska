# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    connection = [(i, 0) for i in range(n)]

    for i in range(m):
        t = data[i]
        j, start = min(connection, key = lambda x : x[1])

        output. append((j, start))
        connection[j] = (j, start + t) 

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    input_ = input()
    n, m = [int(x) for x in input_.split()]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for connection1, start in result:
        print(connection1, start)

if __name__ == "__main__":
    main()
