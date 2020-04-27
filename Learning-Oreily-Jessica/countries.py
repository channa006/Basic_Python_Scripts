f=open("countries.txt", "r")
countries=[]
for i in f:
    i=i.strip()
    countries.append(i)
f.close()

print(countries)

for i in countries:
    if i[3]=="N":
        print(i)
        
