with open ("Быцань А.И._УБ-23_vvod.txt","r") as file:
    line=file.readlines()
    a=[element.replace("\n"," ").split()for element in line]
    n=len(a)
    m=len(a[0])
    A=a
for i in range(n):
    for j in range(m):
        print(A[i][j],end=' ')
    print()                       # вариант 2 задание 1