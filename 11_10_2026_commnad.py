# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:00:20 2026

@author: Saikumar.Gudavadla
"""

#command processing

def calculate():
    try:
        a = float(input("Hey digger 1st nummer?: "))
        b = float(input("Hey digger 2st nummer?: "))
        answer = a+b
        return f"The answer is  {answer:g}"
    except ValueError:
        return " Please enter valid number."



def get_time_info():
    return " I can tell the time soon!"

def tell_joke():
    return "why do programmers love python? It has great snakes!"

def process_command(command):
    command = command.lower()
    
    if command == "hello":
         return "hey  Digger"
     
    elif command == "joke":
            return tell_joke()
        
    elif command == "time":
            return get_time_info()
        
    elif command == "calc":
            return calculate()
        
    else:
            return " sorry , I dont know that command yet"
        
print("Liam Jarvis:online!")

while True:
    command = input("You: ")
    if command.lower() == "exit":
        print("Jarvis:Goodbye")
        break

    response =process_command(command)
    print("Jarvis:", response)            
