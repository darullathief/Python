
#Membuat papan/board
def printBoard():
    print('-------------')
    print('| '+board[1]+' | '+board[2]+' | '+board[3]+ ' |')
    print('-------------')
    print('| '+board[4]+' | '+board[5]+' | '+board[6]+ ' |')
    print('-------------')
    print('| '+board[7]+' | '+board[8]+' | '+board[9]+ ' |')
    print('-------------')

#Mengecek board yang masih kosong
def freeSpace(pos):
    return board[pos]==' '

#Giliran Player 1
def player1Move():
    print('Giliran Player 1')
    run = True
    while run:
        if boardFull(board): #cek board sudah penuh
            break
        move = int(input('Masukan pilihan untuk menempatkan \'X\' (1-9): '))
        if move > 0 and move < 10:
            if freeSpace(move): #Cek board kosong atau terisi
                run = False
                insertLetter('X', move)
            else:
                print('Maaf, Tempat telah terisi')
                continue
        else:
            print('Silahkan pilih no. 1-9')
            continue

#Giliran Player 2
def player2Move():
    print('Giliran Player 2')
    run = True
    while run:
        if boardFull(board): #Cek board sudah penuh
            break

        move = int(input('Masukan pilihan untuk menempatkan \'O\' (1-9): '))
        if move > 0 and move < 10:
            if freeSpace(move): #Cek board kosong atau terisi
                run = False
                insertLetter('O', move)
            else:
                print('Maaf, Tempat telah terisi')
                continue
        else:
            print('Silahkan pilih no. 1-9')
            continue

#Menambah simbol ke dalam indeks board
def insertLetter(letter, pos):
    board[pos] = letter

#Mengecek pemenang
def winner(bo, le):
    #Kondisi yang meyatakan menang
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)


#Cek board apakah sudah penuh   
def boardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def main():
    print('Selamat Datang di Tic Tac Toe!')
    printBoard()

    while not(boardFull(board)): #cek board tidak penuh
        if not(winner(board, 'O')): #cek kondisi menang dari Player 2
            player1Move()
            printBoard()
        else:
            print('Player 2 Menang !')
            break

        if not(winner(board, 'X')): #cek kondisi menang dari Player 2
            player2Move()
            printBoard()
        else:
            print('Player 1 Menang !')
            break

        if boardFull(board):
            print('Game Seri !')
            break


while True:
    board = []  #Mendefinisikan indeks untuk pengisian simbol X atau O
    for i in range (10):
        board.append(' ')

    answer = input('Apakah ingin memulai permainan? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes': #answer.lower = mengubah string kelowcase
        main()
    else:
        break
