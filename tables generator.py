print("***********Multiplication table*************")
while True:
    n=int(input("Enter a Number: "))
    if(n==0):
        print("Thank You !!!")
        break
    else:
        for i in range(0,11):
            print(n,"*",i,"=",n*i)
            i+=1
