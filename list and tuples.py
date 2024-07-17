friends = ["apple", "orange", "5", "34.7", False, "Anuj", "Swarup"]

print(friends[2])

friends[0] = "Ms dhoni"   #unlike strings lists are mutable

print(friends[0])

# new concept of list 

friends.append("cricket")  #append means insertion at the  end of the list

print(friends)   

friends.reverse()
print(friends)

l1 = [1,34,62,2,6,11]
l1.sort()
print(l1)

l2 = [12,69,34,349]
l2.insert(3 , 143)
print(l2)

print(l2.pop(2))  #l2.pop(2) this is the main method
print(l2)

l3 = [23,45,90,56,45]
l3.remove(23)
print(l3)