
print("welcome to treasure game!")


while True:
    answer = input('play? (y/n): ')
    if answer in ('y', 'n'):
        break

if answer == 'n':
    print('Goodbye')
    quit  # FIX THIS HOW DO I QUIT IT

else:
    pass

board = []
length = int(input("enter length: "))  # I HAVE 2 MAKE SURE IT QUITS IF NOT INT
width = int(input("enter width: "))

for i in range(0, length):
    line_board = []
    line_board.append(["0"]*width)

for i in range(0, length):
    board.append(line_board)

print(board) # HAVE TO MAKE IT PRETTY IN ROWS AND SHIT
