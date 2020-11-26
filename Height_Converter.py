##########                                                Start of Code                                           ##########

"""
This program aims at converting a known user height  
from feet to metres.

Developed by Bright U.O
"""
# Measure to break loop when user is done
end = False
# Provide this knowledge to the user
print("Press the number '0' to exit when done")
# Loop the process of converting given height to metres 
while end == False:
    height = eval(input("Please input height in feet: "))
    # For handling invalid inputs by the user
    if height < 0:
        new_height = eval(input("The height you entered is invalid. Please try again: "))
        metres = new_height * 0.305
        print("You are {} metres tall.".format(metres))
    elif height == 0:
        end = True
    else:
        metres = height * 0.305
        print("You are {} metres tall.".format(metres))

##########                                                End of Code                                           ##########