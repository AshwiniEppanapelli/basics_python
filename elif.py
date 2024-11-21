name=input()
marks=int(input())
if(marks>=90):
    print(name,"secure A grade")
elif(80<=marks<=89):
    print(name,"secured B grade")
elif(70<=marks<=79):
    print(name,"secured C grade")
elif(60<=marks<=69):
    print(name,"secured D grade")
else:
    print(name,"is Fail")                