print("*"*20,"ATM MACHINE","*"*20)
amount=int(input("Enter the amount:"))
l=[500,200,100,50,20,10,5,2,1]
c=0
singlenotes=0
for i in l:
    notes=amount//i
    c=c+notes
    print(f"{i} notes --> {notes}")
    amount=amount-i*notes
    if(notes==1):
        singlenotes+=1
print("singlenotes are:",singlenotes)        
print("Maximum number of notes:",c)    