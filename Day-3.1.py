n=[8,9,3,1,2,0,5,0]

numbers=[]
zero=[]

for num in n:
   if num  == 0:
      zero.append(num)      
   else :
      numbers.append(num)

print(zero)
print(numbers)

for item in n:
   n.append(item)
   print(item)




