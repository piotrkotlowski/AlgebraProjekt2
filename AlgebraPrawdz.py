import copy
import random
random.seed(13)

def main():
    #ZAD 7
    vector1 = [1, 0, 0, 2, 4]
    vector2 = [0, 1, 0, 1, 0]
    vector3 = [0, 0, 1, 5, 6]
    listofvector = [vector1, vector2, vector3]
    wyn = linear(listofvector,7)
    wyn_with_cords=linearwithcords(listofvector,7)
    #print(len(wyn))
    #printowanie(wyn_with_cords)
    vector=[1,2,3,4,5]
    #print(MinimizeHammingDistance(wyn,1,vector,wyn_with_cords))


    #ZAD 8
    a=generateMatrix()
    #print(a)
    extreactedVecot=extractingVectors(a)
    #print(divideMatrix(a))
    Gmatrix=[[1, 0 ,0 ,0 ,0, 4, 4, 2, 0, 1, 1],[0, 1, 0 ,0, 0, 3 ,0, 2, 2,1 ,0],[0, 0, 1, 0 ,0, 2 ,0, 1, 1, 1, 1],[0, 0, 0, 1 ,1, 0 ,0, 0, 4, 3, 0]]
    b=MatrixMulti(Gmatrix,extreactedVecot)
    #print(b)
    b_sendedtoFRiend=SendingToFriend(b)
    wyn8=linear(Gmatrix,5)
    wyn8_with_cords=linearwithcords(Gmatrix,5)
    #print(b_sendedtoFRiend)
    sendedtofriendanduncoded=MinimizeHammingDistancevectors(wyn8,1,b_sendedtoFRiend,wyn8_with_cords)
    #print(sendedtofriendanduncoded)
    print(divideMatrix(Transpose(sendedtofriendanduncoded)))



def linear(listofvectors,Z):
    scalar=[0]*len(listofvectors)
    result=[]
    counter=0
    while True:
        counter += 1
        DoNotAdd=False
        newvecetor=[0]*len(listofvectors[0])
        for j in range(len(listofvectors[0])):
            Sum=0
            for i in range(len(scalar)):
                Sum+=(scalar[i]*listofvectors[i][j] )
            newvecetor[j]=Sum%7
        for m in range(len(result)):
            if result[m]==newvecetor:
                DoNotAdd=True
        if DoNotAdd==False:
            result.append(newvecetor)
        scalar[len(scalar)-1]+=1
        for i in range(len(scalar)-2,-1,-1):
            if scalar[i+1]==Z:
                scalar[i+1]=0
                scalar[i]+=1
        if counter==Z**len(listofvectors):
            break
    return result
def linearwithcords(listofvectors,Z):
    scalar=[0]*len(listofvectors)
    result=[]
    counter=0
    while True:
        counter += 1
        DoNotAdd=False
        newvecetor=[0]*len(listofvectors[0])
        for j in range(len(listofvectors[0])):
            Sum=0
            for i in range(len(scalar)):
                Sum+=(scalar[i]*listofvectors[i][j] )
            newvecetor[j]=Sum%7
        for m in range(len(result)):
            if result[m]==newvecetor:
                DoNotAdd=True
        if DoNotAdd==False:
            result.append(newvecetor)
            scalartoget=copy.deepcopy(scalar)
            result.append(["WSPOŁRZEDNE:",scalartoget])

        scalar[len(scalar)-1]+=1
        for i in range(len(scalar)-2,-1,-1):
            if scalar[i+1]==Z:
                scalar[i+1]=0
                scalar[i]+=1
        if counter==Z**len(listofvectors):
            break
    return result
def checkcords(vector,listofvectors):
    for i in range(len(listofvectors)):
        if listofvectors[i]==vector:
            return listofvectors[i+1]
def Hammingdistance(vector1,vector2):
    counter=0
    for i in range(len(vector1)):
        if vector1[i]!=vector2[i]:
            counter+=1
    return counter
def MinimizeHammingDistancevectors(C,B,v,listofvectors_with_cords):
    result=[]
    for k in range(len(v)):
        min = float("+inf")
        listofmin = []
        for i in range(len(C)):
            if Hammingdistance(C[i], v[k]) < min:
                min = Hammingdistance(C[i], v[k])
        for s in range(len(C)):
            if Hammingdistance(C[s], v[k]) == min:
                listofmin.append(C[s])
        randomvariable = random.randint(0, len(listofmin) - 1)
        vectoroutput = listofmin[randomvariable]
        #print(vectoroutput)
        result.append(checkcords(vectoroutput, listofvectors_with_cords)[1])
    return result
def MinimizeHammingDistance(C,B,v,listofvectors_with_cords):
    min=float("+inf")
    listofmin=[]
    for i in range(len(C)):
        if Hammingdistance(C[i],v)<min:
            min=Hammingdistance(C[i],v)
    for k in range(len(C)):
        if Hammingdistance(C[k],v)==min:
                listofmin.append(C[k])
    randomvariable=random.randint(0,len(listofmin)-1)
    vectoroutput=listofmin[randomvariable]
    #print(vectoroutput)
    return checkcords(vectoroutput,listofvectors_with_cords)
def Transpose(matrix):
    result=[]
    for k in range(len(matrix[0])):
        subrow=[]
        for i in range(len(matrix)):
            subrow.append(matrix[i][k])
        result.append(subrow)

    return result




def generateMatrix():
    matrix=[[random.randint(0,4) for i in range(10)] for k in range(4)]
    #print(matrix)
    return matrix
def divideMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j]=matrix[i][j]/4
    #print(matrix)
    return matrix
def MatrixMulti(matrix,v):
    result=[]
    for i in range(len(v)):
        codedvector=[0] *len(matrix[0])
        for k in range(len(matrix[0])):
            Sum = 0
            for s in range(len(v[i])):
                Sum+=v[i][s]*matrix[s][k]
            codedvector[k]=Sum%5
        result.append(codedvector)
    return result
def extractingVectors(matrix):
    result=[]
    for i in range(len(matrix[0])):
        result.append([matrix[0][i],matrix[1][i],matrix[2][i],matrix[3][i]])
    return result
def SendingToFriend(listoofcodedvectors):
    codedvectors=copy.deepcopy(listoofcodedvectors)
    for k in range(len(codedvectors)):
        for i in range(len(codedvectors[k])):
            randomvariable=random.randint(0,99)
            if randomvariable<=4:
                randomvariable=3
            else:
                randomvariable=0
            codedvectors[k][i]= (codedvectors[k][i]+randomvariable) % 5
    return codedvectors


if __name__ == '__main__':
    main()