fruits=["apple","banana","chickoo","kiwi","guava"]
print("mango" in fruits)
print("apple" in fruits)
#repeatition
print(fruits*10)
print(len(fruits))
print(fruits[3])
print(fruits[1:3])
print(fruits[-1:-3])

matrix = [1,0,1, 0, 1, 0, 0 , 0,1, 1,1, 1,0, 1,1,0, 1,1,0, 1,1]
print(matrix*1000000)

# Extend
list1 = [1,2,3,4]
list1.extend([5,6])
print(list1)
print(" ")

# Append
list2 = [3,77,87,88]
list2.append(4)
print(list2)
print(" ")

# Insert
list3 = [9,98,67,54]
list3.insert(2,5)
print(list3)
print(" ")

# Remove
list4 = [5,6,2,12,34]
list4.remove(2)
print(list4)

# Pop
list5 = [6,56,6,7,867]
popped = list5.pop()
print(popped)

# Del
list6 = [4,14614,4614,13,4312,89]
del list6[0]
print(list6)
print(max(list6))
print(min(list6))

# Sum
total = sum(list6)
print(total)
total2 = sum(list6,50)
print(total2)
# Reverse
list6.reverse()
print(list6)

# Index
print(list6.index(13))

# Count
list7 = [13,4,14614,4614,13,4312,89]
a = list6.count(13)
print(a)

# Slice
L1 = [1, 2, 3, 4, 5, 6]

print (L1[-4:-1])
print (L1[-1:-4])
print (L1[1:-4])
print (L1[1:-5])
print (L1[1:-6])
print (L1[1:-5])
print (L1[-2:5])
print (L1[-1:4])
