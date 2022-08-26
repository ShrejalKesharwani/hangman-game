import pyfiglet
def logo():
    result=pyfiglet.figlet_format("hangman")
    print(result)

    #return result

logo()
stages = ['''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
-----------
''', '''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
-----------
''', '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
-----------
''', '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
-----------
''', '''
    +---+
    |   |
    0   |
    |   |
        |
        |
-----------
''', '''
    +---+
    |   |
    0   |
        |
        |
        |
-----------
''', '''
    +---+
    |   |
        |
        |
        |
        |
-----------
''']