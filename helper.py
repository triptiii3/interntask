def sort(NumList,Number):
    temporary=0

    for i in range (Number):
        for j in range(i + 1, Number):
            if(NumList[i] > NumList[j]):
               temporary = NumList[i]
               NumList[i] = NumList[j]
               NumList[j] = temporary



