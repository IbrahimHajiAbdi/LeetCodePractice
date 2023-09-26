def spiralMatrix(matrix):
        res = []
        x, y = 0, 0
        replicaMatrix = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))]
        def checkPosEmpty(y, x):
            if replicaMatrix[y][x] == 0:
                replicaMatrix[y][x] = 1
                return True
            else: 
                return False
        def checkIfComplete():
            unprocessedCoords = []
            for y in range(len(replicaMatrix)):
                for x in range(len(replicaMatrix[y])):
                    if replicaMatrix[y][x] == 0:
                        unprocessedCoords.append([y, x])
            if len(unprocessedCoords) == 1:
                return unprocessedCoords[0]
            else: 
                return None
        i = 0
        while True:
            if i == 12: break
            i += 1
            while x < len(matrix[0]) - 1:
                if checkPosEmpty(y, x):
                    res.append(matrix[y][x])
                    x += 1
                else:
                    break    
            while y < len(matrix) - 1:
                if checkPosEmpty(y, x):
                    res.append(matrix[y][x])
                    y += 1  
                else:
                    break      
            while x > 0:
                if checkPosEmpty(y, x):
                    res.append(matrix[y][x])
                    x -= 1
                else:
                    break 
            while y > 0:
                if checkPosEmpty(y, x):
                    res.append(matrix[y][x])
                    y -= 1  
                else:
                    break  
            print(replicaMatrix, y, x)
            if checkIfComplete() != None:
                y, x = checkIfComplete()
                res.append(matrix[y][x])
            if len(res) == len(matrix[0]) * len(matrix):
                return res
            # else: print(res)
            
print(spiralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))