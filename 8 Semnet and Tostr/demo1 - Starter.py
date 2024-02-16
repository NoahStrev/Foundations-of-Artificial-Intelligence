import semnet
import tostr 
import string

# get the global "is-a" relationship
isa = semnet.GetIsA()

# inverse of "is-a" is "exampleOf"
example = semnet.GetExampleOf()

# declare some entities we want to store knowledge about
thing = semnet.Entity("thing")
animal = semnet.Entity("animal")
bird = semnet.Entity("bird")
fish = semnet.Entity("fish")
minnow = semnet.Entity("minnow")
trout = semnet.Entity("trout")
ape = semnet.Entity("ape")

# declare some facts: what's what?
semnet.Fact(animal, isa, thing)
semnet.Fact(ape, isa, animal)
semnet.Fact(bird, isa, animal)
semnet.Fact(fish, isa, animal)


print( "out some of the things we know (directly or by induction)")
x = tostr.tostr( trout.objects(isa))
print( "trout is:", x )
print( "animal is:", tostr.tostr( animal.objects(isa) ))
print( )
print( "fish:", tostr.tostr( fish.objects(example) ) )
print( "fish:", tostr.tostr( fish.agents(isa) ) )
print( "animals:", tostr.tostr( animal.agents(isa) ))
print( )

# declare size relationships
biggerThan = semnet.Relation("bigger than", 1)



# look at all the things we know now!
print( "ape is a fish?", isa(ape,fish))
print( "minnow is a fish?", isa(minnow,fish))
print( "minnow is an animal?", isa(minnow,animal))
print()
print( "ape bigger than minnow?", biggerThan(ape,minnow))
print( "minnow bigger than trout?", biggerThan(minnow,trout))

print( "ape is bigger than:", tostr.tostr( ape.objects(biggerThan) ))

# declare entities for actions (these are nouns too, you know)
act = semnet.Entity("act")
swim = semnet.Entity("swim")
walk = semnet.Entity("walk")
semnet.Fact( swim, isa, act )
semnet.Fact( walk, isa, act )

# declare an "ableTo" relation, so we can say who can do what
ableTo = semnet.Relation("ableTo", 0)
whatCan = semnet.Relation("whatCan", 0, ableTo)

# note that fish can swim and apes can walk
semnet.Fact( fish, ableTo, swim )


# see what we can say about swimming ability
print()
print( "fish can swim?", ableTo( fish, swim ) )
print( "minnow can swim?", ableTo( minnow, swim ) )
print( "bird can swim?", ableTo( bird, swim ) )
print( "what can swim?", tostr.tostr( swim.getObjects(whatCan) ) )
print( "what can walk?", tostr.tostr( walk.getObjects(whatCan) ) )

# declare a "has" relationship (and its inverse)
has = semnet.Relation("has", 0)
whatHas = semnet.Relation("whatHas", 0, has)

scales = semnet.Entity("scales")
hair = semnet.Entity("hair")
semnet.Fact( fish, has, scales )

print( )
print( "minnow has hair?", has( minnow, hair ) )
print( "minnow has scales?", has( minnow, scales ) )
print( "ape has hair?", has( ape, hair ) )
print( "ape has scales?", has( ape, scales ) )
print( "what has scales?", tostr.tostr( scales.getAgents(has) ) )
print( "what has hair?", tostr.tostr( hair.getAgents(has) ) )
