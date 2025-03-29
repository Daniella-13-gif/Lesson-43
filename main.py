list = ['Apple', 'Orange', 'Pawpaw', 'Banana', 'Mango']

print("length of list:", len(list))
print("first element:", list[0])
print("last element:", list[-1])

list.append('Grape')
print("Updated List:", list)

list.remove('Orange')
print("Updated List:", list)

list.sort()
print("Sorted List:", list)

list.pop(2)
print("Updated List:", list)

list.reverse()
print("Reversed list:", list)
 
print("Multiplication on List:", list*4)

list = list[:6]
print("Sliced List:", list)

list.clear()
print("Updated List:", list)