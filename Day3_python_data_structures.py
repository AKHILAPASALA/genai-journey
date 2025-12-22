#This python source code is an example for list creation and list operations
print("Enter the list1 elements:",end=" ")
l1=list(map(int, input().split(" ")))
print("The given l1 list elements are: ",l1)

a=int(input("Eneter the element which you want to append for the l1 list: "))
l1.append(a) #apending an element to the list
print("The updated list1 elements after appending {} is {}".format(a,l1))

e,p=list(map(int,input("Eneter the element and position where you want to insert in l1 list: ").split(" ")))
l1.insert(p,e) #insert operation
print("The updated list1 elements after inserting {} at {} index is {}".format(e,p,l1))

print("Enter the list2 elements:",end=" ")
l2=list(map(int, input().split(" ")))
print("The given l1 list elements are: ",l2)

l1.extend(l2) #etend operation
print("The updated l1 elements after etending l1 with l1 list: ",l1)

r=input("Enter which element you want to remove from l1 list: ")
l1.remove(r) #removing an element from list sometimes it will throws an error the element which you want to remove is 
print("l1 after removing {} is {}".format(r,l1))

r1=input("Enter which element you want to remove from l1 list: ")
l1.discard(r1) #removing an element from list sometimes it will throws an error the element which you want to remove is 
print("l1 after removing {} is {}".format(r1,l1))

#tuple oerations
t=(12,3)
del t

#set operations
s={3,6,30,6}
s.add(8)
s2={5,6,3}
s.update(s2)
s.union(s2)
s.intersection(s2)
print(s)

#dictinary creation and basic operations

d={"akhila":1, "charu":2}
print(d)
d.update({"akash":9,"lucky":3})
print(d)
d["ravi"]=8
print(d)
k=d.pop("ravi")
print(d)
print(k)
v=d.popitem()
print(d)
print(v)
del d["charu"]
print(d)
g=d.get("akash")
print(g)
print(d.keys())
print(d.values())
print(d.items())


