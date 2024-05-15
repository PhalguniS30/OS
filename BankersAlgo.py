if __name__ == "__main__":
  
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resources: "))
    
    # Allocation Matrix
    print("Enter the Allocation Matrix:")
    alloc = []
    for i in range(n):
        alloc.append(list(map(int, input().split())))
    
    # Max Matrix
    max = [[7, 5, 3 ],[3, 2, 2 ],
		   [7, 0, 2 ],[2, 2, 2]]
    
    # Available Resources
    print("Enter the Available Resources:")
    avail = list(map(int, input().split()))
    
    # Initialization
    f = [0] * n
    ans = [0] * n
    ind = 0
    for k in range(n):
        f[k] = 0
        
    need = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]
    
    # Banker's Algorithm
    for k in range(n):
        for i in range(n):
            if f[i] == 0:
                flag = 0
                for j in range(m):
                    if need[i][j] > avail[j]:
                        flag = 1
                        break
                if flag == 0:
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1
                    
    # Print the SAFE Sequence
    print("Following is the SAFE Sequence")
    for i in range(n - 1):
        print(" P", ans[i], " ->", sep="", end="")
    print(" P", ans[n - 1], sep="")
