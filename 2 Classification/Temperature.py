#Very simple example of a Simple Reflex Agent
#Dressing a robot for the outdoors

#Is there any precipitation
precipitation = input("What is the precipitation? (Possible answers, raining, snowing, none):")

#Get the temperature
temperature = float(input("What is the temperature in degrees?:"))

if temperature <= 32:
    print("put on a winter coat")
elif temperature < 55:
    print("put on a jacket")
elif temperature < 72:
    print("put on a windbreaker")

if precipitation == "raining":
    print("take an umbrella")
if precipitation == "snowing":
    print("put on boots")
