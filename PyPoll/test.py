# t = [1, 3, 6]
# v = [t[i+1]-t[i] for i in range(len(t)-1)]
# print(v)

from collections import Counter
import operator
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print("z =", z)
print("len(z):", len(z))

mydict = (Counter(z))
mydict_items = mydict.items()
print('items =', mydict_items)
print("mydict['blue'] =", mydict['blue'])
blue = mydict["blue"]
quotient = (mydict['blue'])/(len(z))
print("(mydict['blue'])/(len(z)) =", quotient)
percent = quotient*100
print(percent, '%', sep='')

red = mydict['red']
yellow = mydict['yellow']
#print('red =', red)
#print('yellow =', yellow)

for key,item in mydict_items:
    print(key,str(item) + " " + str(round((item/len(z)*100),2) ) + "%")

winner = max(mydict, key=mydict.get) #WorkS!!!
#winner = max(mydict.iteritems(), key=operator.itemgetter(1))[0]
#winner = max([red, yellow, blue])
print("winner =", winner) #Why is winner 1??


#print('Blue:', mydict['blue'])
#mydict[blue]
