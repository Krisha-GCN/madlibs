import random
# from english_words import get_english_words_set
import sys

def print_colored(text, color, end='\n'):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m'}
    reset = '\x1b[0m'
    return colors.get(color, '') + text + reset + end


adj1 = input("Enter an adjective: ")
food = input("Enter a food: ")
body_part = input("Enter a body part: ")
spice = input("Enter a seasoning/spice: ")
adj2 = input("Enter an adjective: ")
adj3 = input("Enter another adjective: ")
adverb = input("Enter an adverb: ")
person = input("Enter a person: ")
emotion = input("Enter an emotion: ")


print("I love making food because it allows me to get creative in the" + print_colored(adj1, color="blue") + "kitchen. One of my favorite recipes to cook is" + print_colored(food, color="blue") + "which always makes my" + print_colored(body_part, color="blue") + "water. I like to add a pinch of" + print_colored(spice, color="blue") + "for some extra", print_colored(adj2, color="blue") + "flavor. Cooking is a", print_colored(adj3, color="blue"), "activity that relaxes me and brings me joy. The best part is enjoying the delicious meal", print_colored(adverb, color="blue"), "with", print_colored(person, color="blue"), "and seeing their", print_colored(emotion, color="blue") + "on their face when they take the first bite.")