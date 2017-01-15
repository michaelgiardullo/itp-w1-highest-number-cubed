"""This is the entry point of the program."""

def highest_number_cubed(num):
    x=0
    found = False
    while found == False:
        if x*x*x > num:
            return x-1
            found = True
        x=x+1
