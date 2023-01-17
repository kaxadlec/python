days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days,fruits,drinks,desserts):
print(day,":drink", drink,"-eat",fruit,"-enjoy",dessert)
print(list(zip(fruits,drinks)))

number_list = []
for number in range(1,6):
    number_list.append(number)
print(number_list)

number_list = list(range(1,6))
print(number_list)

number_list = [number for number in range(1,6)]
print(number_list)

number_list = [number-1 for number in range(1,6)]
print(number_list)

a_list = [number for number in range(1,6) if number % 3 ==1]
print(a_list)

a_list = []
for number in range(1,6):
    if number % 3 == 1:
        a_list.append(number)
print(a_list)

rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row,col)

rows=range(1,4)
cols=range(1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

number_thing = (number for number in range(1,6))
print(type(number_thing))

# list comprehension

#옛날방법
odd_lists = []
for i in range(1,11):
    if i % 2 == 1:
        odd_lists.append(i)
print(odd_lists)

odd_lists = [i for i in range(1,11) if i % 2 == 1]
print(odd_lists,type(odd_lists))
#tuple
odd_tuples= (i for i in range(1,11) if i % 2 ==1)
print(odd_tuples,type(odd_tuples))

print(range(1,101))
print(type(range(1,101)))