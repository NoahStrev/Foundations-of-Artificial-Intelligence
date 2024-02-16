import semnet
import tostr 
import string

# get the global "is-a" relationship
isa = semnet.GetIsA()

# inverse of "is-a" is "exampleOf"
example = semnet.GetExampleOf()

# declare some entities we want to store knowledge about
human = semnet.Entity("human")
employees = semnet.Entity("employees")
supervisors = semnet.Entity("supervisors")
Ali = semnet.Entity("Ali")
Sally = semnet.Entity("Sally")
John = semnet.Entity("John")

# declare some facts: what's what?
semnet.Fact(employees, isa, human)
semnet.Fact(supervisors, isa, human)
semnet.Fact(Sally, isa, human)
semnet.Fact(Ali, isa, employees)
semnet.Fact(John, isa, supervisors)


print( "out some of the things we know (directly or by induction)")
# agents(isa) are what have been declared as isas
# objects(isa) is what this is a
x = tostr.tostr( Ali.objects(isa))
print( "Ali is:", x )
print( "human is:", tostr.tostr( human.agents(isa) ))
print( )
print( "John:", tostr.tostr( John.objects(isa) ) )
print( "Sally:", tostr.tostr( Sally.objects(isa) ) )
print( "employees:", tostr.tostr( employees.agents(isa) ))
print( "supervisors:", tostr.tostr( supervisors.agents(isa) ))
print( )

