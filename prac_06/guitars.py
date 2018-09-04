"""
CP1404/CP5632 Practical - Suggested Solution
Guitar program.
"""


def main():
    
    name = input("Enter Name: ")
    #Always Error Check
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print("My guitar: {}, first made in {1} costed {2}".format(name, year, cost))

main()