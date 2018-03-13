import random 
import sys
import os

#dicts are like maps, but you cannot join two dicts together like you can do with 
#lists with a + sign

sup = {'Fiddler':'Isaac Bowin',
	    'Captain Cold':'Leonard Snart',
	    'tobedel':'hahdoesntmatter'
		}

print(sup['Captain Cold'])
print(sup['tobedel'])
del sup['tobedel']
#print(sup['tobedel'])#will give error now
print(sup) #item deleted!
sup['Fiddler'] = "Isaaac Bowin" #easily change entries !
print(sup)
print(len(sup)) #currently 2 pairs (key value)

sup['yakut'] = 'healthy bacteria' # Easily extensible, unlike lists where we are bound to use append
print(sup)
print(len(sup)) #currently 3 pairs (key value)


print(sup.get('yakut'))
print(sup['yakut'])
#the above 2 statements are almost the same

print(sup.keys()) #output is in form of a list
print(sup.values()) #again, list 


