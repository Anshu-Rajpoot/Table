a= int(input("Enter the number to see table of: ")) #take input for the table of number a
i=0
x=(int(input("Enter the number till where you want your table to run: "))) #take another input for range of table
for i in range(1,x+1): #use loop
    x=i*a #create formula
    print(a,"*",i,"=",x) #print result

