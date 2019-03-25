# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

newLst = [random.randint(-10,10) for _ in range (10)]
print (newLst)
newList=[]
i = 0
for i in newLst: 
   if (newLst[i]%3 == 0 or newLst[i]>0 or newLst[i]%4 != 0):
       newList = newLst[i]
   i += 1 
print (newList) 

 
#i = for int(newLst(i)) in newLst: print(f'{i}. {i:>8}') 
#i += 1 

 
 