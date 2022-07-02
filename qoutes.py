import random

def Qoutes():
    listText = ["Don’t let my motorcycle ride interfere with the safety of your phone call.",
                    "It’s your road others can ride it with you but no one can ride it for you.", 
                    "A bad day on a mountain bike always beats a good day in the office.", 
                    "Biker heaven, Free road, Full tank, Full throttle.", 
                    "I don’t need therapy, I just need to ride my fat bike.",
                    "We need to go on an adventure road trip.",
                    "Everything looks better from the inside of a motorcycle helmet",
                    "No matter how bad your day is your bike will always make you feel better.",
                    "Some call it an adventure, We call it life.",
                    "You don’t stop when you get old, You get old when you stop riding.",
                    "Every day is a good day for a ride.",
                    "The brave don’t live forever the cautious don’t live forever.",
                    "A traveller should be happy, not perfect."
                    ]
    
    text = random.choice(listText)
    return text