
new_some_list = [[99,23,80,0,94,58,119,15,35,75,15,47],
                 [16,23,4,4,55,89,144,10,34,18,23,65],
                 [43,23,75,0,94,58,119,15,35,75,15,47],
                 [76,23,6,4,55,89,144,10,34,18,23,65],
                 [86,23,65,0,94,58,119,15,35,75,15,47],
                 [12,23,9,4,55,89,144,10,34,18,23,65]]

for i in new_some_list:
    print('1 :', i)

new_some_list.sort(key=lambda i: i[0])
for i in new_some_list:
    print('2 :', i)

new_some_list[4].sort()
for i in new_some_list:
    print('3 :', i)
#for i in new_some_list:
   # print(i)
#def sort_col(i):
    #return i[n]

#a.sort(key=sort_col)
#practice_list.sort(key=lambda i: i[1])
"""
d1 = dict(short='dict', long='dictionary')
d2 = {'dictyyy': 1, 'dictionary': 2, 'phonenumber': +17344356466,
      'dict': 3, 'Adress': ['Korolska str 34','Highroad 23',3,4,5], 'phonenumber': +17344356466}
print(d2['dictionary'])
print(d2)
d2.pop('dictionary')
print('POP "dictionary"',d2)
item = d2.popitem()   #возвращает удаленный объект
print(d2)
print(d2.setdefault('clock'))
print(d2)
print(d2.setdefault('phonenumber'))
print(d2)
d2.update({'postcard': '56067'})
print(d2)
bg = {'Name' : {'Name': 'Julia'}, 'Secondname' : 'Washington'}
print(bg)
d2.update(bg)
"""