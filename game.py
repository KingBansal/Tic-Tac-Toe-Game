
import random 

board = '''
                  |       |        
              1   |   2   |   3      
           _______|_______|_______
                  |       |       
              4   |   5   |   6    
           _______|_______|_______
                  |       |       
              7   |   8   |   9    
                  |       |        '''

start = False
player = ''
comp = ""
choices = ['1','2','3','4','5','6','7','8','9']


while True:
    if start == False :
        choice = input('what do you want to choose: X or O (type x and o resp)')
        choice = choice.lower()
        if choice == 'x':
            start = True
            player = 'X'
            comp = 'O'
        elif choice == "o":
            start = True
            player = "O"
            comp = "X"
        elif choice == "quit":
            break
        else:
            print('Please choose a valid option, type x or o for X or O respectively')
    elif start == True:
        print(board)
        choice = input('type the seriel no. of box >')
        if choice in choices:
            choices.remove(choice)
            board = board.replace(choice, player)
            print(type(choice))
            print(choices)
            comp_choice = random.choice(choices)
            choices.remove(comp_choice)
            board = board.replace(comp_choice, comp)
        else:
            choice = input(f'please type a valid option from {choices}')