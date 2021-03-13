#!/usr/bin/env python3.6

def closures_greeter(prefix):
    othername = "chandrakala"
    def clousers_greet(name):
        print(f"{prefix} {name} and {othername}")
    return(clousers_greet)

# closures basically hold up the return for litter longer. In normal functions once it return 
# it won't hold it 

hello = closures_greeter("Hello,")
goodBye= closures_greeter("GoodBye,")

hello("Nandisha")
goodBye("Nandhu")

