print ("Задание 1")
numbers = [1+2+3+4+5]
print(numbers)

print("Задание 2")
numbers = [1,8,32,7,2,9]
max = max(numbers)
print(max)


print("Задание 3")
numbers = [5,5,5,1,2,3,4,5,7,7,8,8,8,10]
print(set(numbers))


print("Задание 4 ")
numbers = [1,2,3,4,5]
numbers = [7,7,8,8,8,9,9,9,10]
result = numbers + numbers
print(result)

print ("Задание 5")
t = (5,6,7,8,9)
index = t.index(5)
index = int (input()) 
print(index)
if index <= 4:
  print("Такой элемент есть")
else:
 print("Элемент не найден")



print("Задание 6")
x = (2,5)
y = (10,15,100)
print(x+y)


print("Задание 7")
point = (3,5,6,7,8)
point = list(point)
index = point.index(7)
point.remove(7)
back_to_tuple = tuple(point)
print(point)


print("Задание 8")
l = [1,5,5,5,5,5,5,5]
count = l.count(5)
print(count)
