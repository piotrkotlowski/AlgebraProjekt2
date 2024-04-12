import copy
import random
random.seed(13)

def main():
    #ZAD 6
    vector1 = [1, 0, 0, 2, 4]
    vector2 = [0, 1, 0, 1, 0]
    vector3 = [0, 0, 1, 5, 6]
    listofvector = [vector1, vector2, vector3]
    linearcombinations= linear(listofvector,7)
    #ToPrint(linearcombinations)
    linearcombinations_with_cords=linearwithcords(listofvector,7)


    #ZAD 7.
    #Losowo wybrany wektor
    vector = [1, 2, 3, 4, 5]
    #Wyświetlenia wyniku
    #print(MinimizeHammingDistance(linearcombinations,vector,linearcombinations_with_cords))


    #ZAD 8
    #Generowanie macierzy
    #a)
    a=generateMatrix()
    #b)
    aDivided = divideMatrix(a)
    #Ekstraktowanie wektorów z wygenrowanej macierzy
    #d)
    extreactedVecot=extractingVectors(a)
    #Macierzy przykształcona w celu zrobienia Image

    #Macierz G z polecenia
    Gmatrix=[[1, 0 ,0 ,0 ,0, 4, 4, 2, 0, 1, 1],[0, 1, 0 ,0, 0, 3 ,0, 2, 2,1 ,0],[0, 0, 1, 0 ,0, 2 ,0, 1, 1, 1, 1],[0, 0, 0, 1 ,1, 0 ,0, 0, 4, 3, 0]]

    #Wymnożenie wyekstraktowanych wektorów z macierzą G
    b=MatrixMulti(Gmatrix,extreactedVecot)
    #ToPrintVectors(b)
    #Symulacja wysyłania do kolegi zakodowanych wektorów
    #e)
    b_sendedtoFRiend=SendingToFriend(b)
    #ToPrintVectors(b_sendedtoFRiend)
    #Genrowanie przestrzeni
    linearcombinationsEight=linear(Gmatrix,5)
    linearcombinationsEight_with_cords=linearwithcords(Gmatrix,5)
    #f)
    #Wykonanie algorytmu MinimizeHammingDiscatence
    sendedtofriendanduncoded=MinimizeHammingDistancevectors(linearcombinationsEight,b_sendedtoFRiend,linearcombinationsEight_with_cords)
    #g)
    result=Transpose(sendedtofriendanduncoded)
    #Wyświetlanie wyniku
    #h)
    #print(divideMatrix(Transpose(sendedtofriendanduncoded)))

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
def MinimizeHammingDistancevectors(C,v,listofvectors_with_cords):
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
def MinimizeHammingDistance(C,v,listofvectors_with_cords):
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
    return matrix
def divideMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j]=matrix[i][j]/4
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
def ToPrint(matrix):
    for i in range(len(matrix)):
        if i%8==0 and i!=0:
            print(matrix[i],end="\n")
        else:
            print(matrix[i],end=" ")
def ToPrintVectors(matrix):
    for i in range(len(matrix)):
        if i%3==0:
            print(matrix[i],end="\n")
        else:
            print(matrix[i],end=" ")
if __name__ == '__main__':
    main()