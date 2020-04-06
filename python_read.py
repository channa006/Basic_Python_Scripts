f=open("score.txt","r")

participants= {}

for i in f:
    entry=i.strip().split(",")
    participant=entry[0]
    score=entry[1]
    participants[participant] = score
        
f.close()

print(participants)

    
    
    