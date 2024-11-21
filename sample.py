name = input()
age = int(input())
if(age>=18):
    print(f"{name} is eligible to vote")
else:
    c=18-age
    print(f"{name} is {c} years less to vote,come after {c} years")    