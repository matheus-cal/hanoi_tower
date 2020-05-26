def game(n, frm, aux, to):
    if n > 0:
        game(n-1, frm, to, aux)

        if frm[0]:
            disk = frm[0].pop()
            print ("Movendo disco " + str(disk) + " da torre " + frm[1] + " para torre " + to[1])
            to[0].append(disk)
            moves.append(disk)
            
        game(n-1, aux, frm, to)

def sanity_check():
    n = 2 ** len(to[0]) - 1
    
    if n == len(moves):
        print('A quantidade ideal de movimentos foi realizada - ' + str(n))

if __name__ == '__main__':        
    frm = ([1, 2, 3, 4, 5], "A")
    to = ([], "C")
    aux = ([], "B")
    moves = []
    game(len(frm[0]), frm, aux, to)
    sanity_check()
