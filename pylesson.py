v=[i*i*i for i in range(1,11)]

favorite_languages={'jen':'python',
                    'sarah': 'c',
                    'edward': 'ruby',
                    'phil': 'python'}

for language in set(favorite_languages.values()):
    print(language.title())


promt='\nTell me something, and I will repeat it back to you:'
promt+="\nEnter 'quit' to end the program."
message=''
while message !='quit':
    message=input(promt)
    print(message)


def make_pizza(*toppings):
    print(toppings)

