# Table of a number

#take input for the table of number a
a= int(input("enter the number to see table of: ")) 
i=0
#take another input for range of table
x=(int(input("enter the number till where you want your table to run: ")))
#use loop
for i in range(1,x+1):
   #create formula
    x=i*a
    #print result
    print(a,"*",i,"=",x) 
