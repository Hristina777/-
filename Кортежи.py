# кортежи

list_10 = 'c', 'd', 'e'
tuple_1 = (1, 2, 3, True, 'text')
not_tuple = [1, 2, 3, True, 'text']
print (type (tuple_1))  #1
print (type(not_tuple)) #2

tuple_2 = ()
print (type (tuple_2))  #3 кортеж весит меньше, чем список, т.к неизменяем

# copy, count, index, len

tuple_3 = tuple_1[1:4]
print (type (tuple_3))  #4

tuple_4 = (1, 2, 3, [3, 4, 5], 'text')
print (tuple_4 [3])

tuple_4 = (1, 2, 3, [3, 4, 5], 'text')
print (tuple_4 [3][0]) #обратились к элементу под индексом 0 в списке

tuple_4 = (1, 2, 3, [3, 4, 5], 'text')
tuple_4 [3][2] = 'text'
print (tuple_4)

tuple_4 [3][2] = [3, 2, True, 'text']
print (tuple_4)
print (tuple_4 [3][2][2])

tuple_5 = ('element',) # если кортеж из одного элемента, то "," обязательна, иначе воспринимает как строку

tuple_6 = tuple('Hello')
print (tuple_6)

tuple_7 = tuple(list_10)
print (tuple_7)

symbol = tuple_7 [1]
print (type(symbol)) # тоже самое что и список, но не изменяемый. Если хотим изменить нужно создавать новый кортеж














