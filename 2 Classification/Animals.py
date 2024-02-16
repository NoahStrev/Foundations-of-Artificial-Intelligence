name = input("What is the name of your animal?:")

birth = input("Does the animal give birth? (y/n):")
flight = input("Does the animal fly? (y/n):")
water = input("Does the animal live in water? (y/n/s):")
blood = input("What is the animal's blood type? (warm/cold):")

classification = ""

if birth == "n" and flight == "y":
    classification = "Birds"
elif birth == "n" and water == "y":
    classification = "Fishes"
elif birth == "y" and blood == "warm":
    classification = "Mammals"
elif birth == "n" and flight == "n":
    classification = "Reptiles"
elif water == "s":
    classification = "Amphibians"
else:
    classification = "Unknown"

print("The " + name + " would be classified as a " + classification)
