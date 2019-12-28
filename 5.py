def createMatrix(ordo):
    A = []
    an = 1
    diagonalA = 0
    diagonalB = 0
    for i in range(ordo):       
        a = [] 
        for o in range(ordo):
            a.append(an)
            an+=1
        A.append(a)
  
    for a in range(ordo):
        diagonalA += A[a][a]
    
    dim = (ordo-1)
    for p in range(ordo):
        diagonalB += A[p][dim]
        dim-=1

    for u in A:
        print(u)

    total = diagonalA * diagonalB
    print("Total = {}".format(total))

createMatrix(3)
