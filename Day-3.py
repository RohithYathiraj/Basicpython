n=[1,2,3,4,5,6,7,8,9]
print("Original list:",n)
n.insert(9,10)
print("List after inserting 10 at the end:",n)
n.pop(0)
print("List after removing 3:",n)
n.append(10)
print("List after appending 10:",n)

for num in n:
 print(num)