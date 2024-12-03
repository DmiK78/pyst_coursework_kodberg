import random
import emoji

def rps_game():
    rsp_list = ['Rock', 'Scissors', 'Paper']
    user_input = input('Rock, Scissors, Paper?: ')
    user_correct = user_input.capitalize()
    comp_input = random.choice(rsp_list)
    print(f'You: {user_correct}')
    print(f'Comp: {comp_input}')
    if user_correct == comp_input:
        print('Draw game! No winner.')
    elif user_correct == 'Rock' and comp_input == 'Scissors':
        print('You are winner!')
    elif user_correct == 'Rock' and comp_input == 'Paper':
        print('You are loser.')
    elif user_correct == 'Scissors' and comp_input == 'Rock':
        print('You are loser.')
    elif user_correct == 'Scissors' and comp_input == 'Paper':
        print('You are winner!')
    elif user_correct == 'Paper' and comp_input == 'Rock':
        print('You are winner!')
    elif user_correct == 'Paper' and comp_input == 'Scissors':
        print('You are loser.')

def bot_menu():
    menu_data = {
        'Films': {
            'film1': '"Terminator 2: Judgment Day"',
            'film2': '"The Wolf of Wall Street"',
            'film3': '"Groundhog Day"'
        },
        'Music': {
            'music1': 'Deep Purple, "Smoke On The Water"',
            'music2': 'Eisbrecher, "Zwischen Uns"',
            'music3': 'Fabri Fibra, "Mal Di Stomaco"'    
        },
        'Games': {
            'game1': 'Shooter: "Project I.G.I."',
            'game2': 'Adventure: "L.A. Noire"',
            'game3': 'Strategy: "Diplomacy"' 
        },
        'Jokes': {
            'joke1': 'In court:\n- I hope you know what awaits you for giving false words?\n- Yes, they promised BMW',
            'joke2': 'On interview:\n- What are your strengths?\n- Insistence.\n- Thank you. We will contact you.\n- I will wait here',
            'joke3': '\n- Just imagine how happy they will be if we do not come.\n- Yes, we have to go'
        },
        'Play now': 'RPS'
    }
    
    print()
    for idx, key in enumerate(menu_data):
        print(f'{idx + 1}. {key}')

    return menu_data

def tell_jokes(jokes):
    for joke in jokes.values():
        print(joke)
        user_in_jokes = input(f'Press "Enter" to read the next joke or type "0" to exit to main menu: \n')
        if user_in_jokes == '0':
            break

bot_face = emoji.emojize(':alien:')

print()
print(f'{bot_face} Hello! I am a bot.')
guest_name = input('   What is your name? - ')
print()
print(f'{bot_face} Hello, {guest_name}!')
print('   I would like you to have fun. Here is a menu:')
menu = bot_menu()

while True:
    print()
    print(f'{bot_face} What is your choice, {guest_name}?')
    user_choice = input('   Enter the number you have chosen: ')
    print()

    if user_choice == '1':
        print(f'{bot_face} I can recommend you the films:\n')
        films = menu['Films']
        for idx, value in enumerate(films.values()):
            print(f'{idx + 1}. {value}')
    elif user_choice == '2':
        print(f'{bot_face} Okay, let us listen to some music!\n')
        music = menu['Music']
        for idx, value in enumerate(music.values()):
            print(f'{idx + 1}. {value}')
    elif user_choice == '3':
        print(f'{bot_face} Please find my suggestion for PC games below:\n')
        games = menu['Games']
        for idx, value in enumerate(games.values()):
            print(f'{idx + 1}. {value}')
    elif user_choice == '4':
        print(f'{bot_face} Well, jokes! Have fun reading)\n')
        jokes = menu['Jokes']
        tell_jokes(jokes)
    elif user_choice == '5':
        print(f'{bot_face} I knew you would have chosen the game\n')
        rps_game()
    else:
        print(f'{bot_face} There is no such menu number. Please try again.')
    print()
