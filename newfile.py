square_list = []

for element in range(1,21):
    square_list.append(element * element)

print(f'\nList of squares{square_list}')

square_list.clear()

print(f'\nEmpty List {square_list}')

square_list = [element * element for element in range(1,21)]

print(f'\nList of squares{square_list}')
      

matirx_list = []
for i in range(1,4):
    row_list = []
    for row in range(1,4):
        row_list.append(row * i)

    print(f'\n Row {i} : {row_list}')
    matirx_list.append(row_list)

print(f'\n Matrix List {matirx_list}')

matirx_list = [ [row * i for row in range(1,4)] for i in range(1,4)]
print(f'\n Matrix List {matirx_list}')

my_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(f'\n Tuple {my_tuple}')

my_tuple1 = tuple(element * element for element in range(1,11))
print(f'\n Tuple {my_tuple1}')


from math import pi

print(pi)
circle_area_set = set()
range_from = 1
range_to = 8 
for r in range(range_from,range_to):
    circle_area_set.add((r ** 2) * pi)

print(f'\n Area of cirlcle {circle_area_set}')

circle_area_set = {(r ** 2) * pi for r in range(range_from,range_to) }
print(f'\n Area of cirlcle {circle_area_set}')

circle_area_set = set((r ** 2) * pi for r in range(range_from,range_to))
print(f'\n Area of cirlcle {circle_area_set}')


petrol_price = 103.44
range_from = 1
range_to = 31

amount_tobe_paid = {}
for litre in range(range_from, range_to):
    amount_tobe_paid[litre] = petrol_price * litre

print(f'\n Amount to be paid : {amount_tobe_paid}')

amount_tobe_paid = {litre : petrol_price * litre for litre in range(range_from, range_to ) }
print(f'\n Amount to be paid : {amount_tobe_paid}')


list_of_sets = [{1,2,3}, {2,1,8,4,6,7,0,3,9}, {"Amit", "Koshti"}, {'A', 'B', 'C'}]
print(f'\n List of sets : {list_of_sets}')

set1 = list_of_sets[2]
print(f'\n List of set1 : {set1}')

for element in list_of_sets[3]:
    print(f'\n Element of 4th set : {element}')

set2 = list_of_sets[1]
print(f'\n Set2 before pop: {set2}')
print(f'\npopped item : {set2.pop()}')
print(f'\n Set2 after pop : {set2}')

list_of_tuple = [(1,2,3), (1,4,6),(1,8,18)]
print(f'\n List of tuples : {list_of_tuple}')

