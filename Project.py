
"""
Create a program that will take two inputs from the user. It will take one word first
then take the second word. Once it has both words the program will determine if the two
words are anagrams or not. To avoid input errors the program will also any punctions or
spaces to be able to return a yes or no answer.
"""


"""
def main
    string1 = input from user
    string2 = input from user
    if string1 and string2 are anagrams
        print yes
    else
        print no

def anagrams
    string1 = make lowercase
    string2 = make lowercase
    gather letters1 from string1
    gather letters2 from string2
    sort letters1
    sort letters2
    return letters1 == letters2
"""

def main():
    string1 = input("Please enter your first word: ")
    string2 = input("Please enter your second word: ")
    if areAnagrams(string1, string2):
        print("These words are anagrams.")
    else:
        print("These words are not anagrams.")

def areAnagrams(string1, string2):
    firstString = string1.lower()
    secondString = string2.lower()
    letters1 = [ch for ch in firstString if 'a' <= ch <= 'z']
    letters2 = [ch for ch in secondString if 'a' <= ch <= 'z']
    letters1.sort()
    letters2.sort()
    return (letters1 == letters2)
main()