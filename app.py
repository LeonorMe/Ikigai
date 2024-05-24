from ikigai import Ikigai

#Initialization
"""
slove  = ["default"]
sgood  = ["default"]
sneeds = ["default"]
spaid = ["default"]
my_ikigai = Ikigai(slove, sgood, sneeds, spaid)
"""
my_ikigai = Ikigai()

# Dialog
print("Whats your name?")
name = input()
print("Hi " + name + ". Welcome to the journy of discovering your Ikigai!")
print("The more you write the better, try to repeat words and write them in the same way (exemple same capitalization a != A). Everything is valid, write it all.")

print("What do you absolutly love to do? Genuinely enjoying the process. (Press x to exit)")
love = input()
while love != "x":
    my_ikigai.love.append(love) 
    love = input()
    
print("What do you do better than average? Genuinely enjoying the processWhat are your talents. (Press x to exit)")
good = input()
while good != "x":
    my_ikigai.good.append(good) 
    good = input()

print("What do you think the world needs? And what can you do for it. (Press x to exit)")
need = input()
while need != "x":
    my_ikigai.need.append(need)
    need = input()

print("What can you be paid for? What services can you provide. (Press x to exit)")
paid = input()
while paid != "x":
    my_ikigai.paid.append(paid) 
    paid = input()

# Generate 
my_ikigai.generate()

my_ikigai.save("Ikigai_Results_" + name + ".txt")

my_ikigai.show_message()
