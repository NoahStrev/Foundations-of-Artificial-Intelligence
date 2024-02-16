
from kanren import *

father = Relation()
mother = Relation()

def get_maternal_parent(x,y) : 
    return lall(mother(x,y))

def get_paternal_parent(x,y) :
     return lall(father(x,y))

def parent(x,y) :
     return lany(get_maternal_parent(x,y), get_paternal_parent(x,y))

def grandparent(x, z):
    y = var()
    return lall(parent(x, y), parent(y, z))

def great_grandparent(x, y) :
    g = var()
    return lall(grandparent(x, g), parent(g, y))

def isparent(x,y):
     h = run(0,x,parent(x,y))
     if len(h) == 0:
          return 'No'
     else:
          return 'Yes'


def xs_ancestors(y) :
    x = var()
    h = run(0,x,parent(x,y))
    if len(h) == 0:
        return 
    else :
        for i in h :
            ancestors.append(i)
            xs_ancestors(i)
            
ancestors = []
def ancestor (x) :
    ancestors = []
    xs_ancestors(x)


# ###############    DEFINE THE FAMILY    ###############################


facts(father,("tony","abe"))
facts(father, ('tony', 'sarah'))
facts(father, ('abe', 'john'))
facts(father, ('bill', 'susan'))
facts(mother, ('susan', 'phil'))
facts(father, ('rob', 'phil'))
facts(mother, ('lisa', 'abe'))
facts(mother, ('lisa', 'sarah'))
facts(mother, ('nancy', 'john'))
facts(mother, ('sarah', 'susan'))
facts(mother, ('mary', 'jill'))
facts(father, ('john', 'jill'))


# ####################   ASK ABOUT THE FAMILY  ###########################

x = var()
g = var()
print('*********************************************************')                
print("Tony's children:")
tonyskids = run(0,x,parent("tony",x))                
for k in tonyskids :
     print(k)

print()
print('*********************************************************')                
print()
print("tony's grandchildren:")
tonys_grandkids = run(0, g, grandparent('tony',g))
for k in tonys_grandkids:
    print(k)

print()
print('*********************************************************')                
print()
print("lisa's great-grandchildren:")
gg = var()
lisas_greatgrandkids = run(0, gg, great_grandparent('lisa',gg))
for g in lisas_greatgrandkids :
    print(g)

print()
print('*********************************************************')                
print()
print('Is tony a parent of kate? ',isparent('tony','kate'))
print('Is lisa a parent of abe? ',isparent('lisa','abe'))


print()
print('*********************************************************')        
print()
print("Who are susan's parents?")
susansparents =  run(0,x,parent(x,'susan'))
for p in susansparents :
    print(p)



print()
print("Who are john's parents?")
johnsparents =  run(0,x,parent(x,'john'))
for p in johnsparents :
    print(p)

print()
print('*********************************************************')        
print()
ancestors = []
ancestor('john')       
print("john's ancestors: ", ancestors)



