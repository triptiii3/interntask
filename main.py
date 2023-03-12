from helper import sort;
NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
        value = int(input("Please enter the Value of %d Element : " %i))
        NumList.append(value)
sort(NumList,Number);
print("Element After Sorting List in Ascending Order is : ", NumList)
