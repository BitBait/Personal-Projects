import time
from PIL import Image
print("Welcome to the world little buddy, this is you")
x = input( "Whats your name in this new exiting world? ")
#Welcome, this is my first real project, its coded really badly, I know. The commented out code is just for fun. Enjoy :)

#if x == "Charlie":
    #print("Senpai notice me")
#else:
    #print("Welcome", x, "i'll be your guide for today")

print("Welcome to the universe", x)
time.sleep(5)
print("This is what you look like")
img = Image.open("Star.png")
img.show()
time.sleep(5)
#This section here prints out an ascii image of a star from the Star.txt file (Currently only works on this directory, want to make it
#so it works on any machiene, so put it in th elocal directory?)


print("You're crashing through the atmosphere quick do something")
img = Image.open("Star.gif")
img.show()
time.sleep(5)
#Atmosphere sequence starts here, gif inserted here, hopefully with a good image viewer a gif should appear

print("Do something")
z = 0
#Defining z as a dummy varaible for counting

y1 = input("")
if y1 == "Shine":
    print("Wow, that's")
    z = z + 1
    time.sleep(1)
    print("that's, incredible")
else:
    print("...")

#First Crash Sequence

if z == 0:
    print("Quick, HURRY")
else:
    print("Keep going")


y2 = input("")
if y2 == "Shine":
    print("So...")
    z = z + 1
    time.sleep(1)
    print("so pretty")
else:
    print("...")

#Second Crash Sequence

if z == 0:
    print("This, this is important, you have to be yourself")
    if z == 1:
        print("You're doing well, keep it up")

else:
    print("You, you're great, keep going")

#If sequence, part of gameplay? Encouragement? idk this is just an experiment

y3 = input("")
if y3 == "Shine":
    print("You streak across the sky, it's beautiful, it's amazing, it's")
    time.sleep(1)
    print("it's")
    time.sleep(1)
    print("indescribable")
    z = z + 1
else:
    print("...")

#Last Crash sequence

time.sleep(2)
print("Well")

if z == 0:
    print("Tonight wasn't your night, you'll be better one day, sometime soon in the future you'll have another chance")
elif z == 1:
    print("You put on a good show, you burned brightly")
elif z == 2:
    print("Wow, that was spectacular the shear bursts of energy light up the night sky")
elif z == 3:
    print("The air is cold and sharp below, people look up into the night sky, they see a "
          "brilliant burst of white streak up the night sky, you have touched more people "
           "than you will ever know")
    img = Image.open("The night sky.gif")
    img.show()
    time.sleep(7)
    print("You are amazing, you are youself, the earth is not a "
          "cold dead place, because you exist, because you exist")
    time.sleep(5)

else:
    print("E R R O R")


#ADD LIST, add more options + a if len(y(n)) = 0 then print (please try), also add quit