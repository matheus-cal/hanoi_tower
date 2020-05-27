import sys
    
def game(n, frm, aux, to):
    if n > 0:
        game(n-1, frm, to, aux)

        if frm[0]:
            disk = frm[0].pop()
            print ('{0}>{1}>{2};'.format(disk, frm[1], to[1]))
            to[0].append(disk)
            moves.append(disk)
            
        game(n-1, aux, frm, to)

def sanity_check():
    n = 2 ** len(to[0]) - 1
    
    if n == len(moves):
        print('{}'.format(str(n)))

if __name__ == '__main__': 
    
    try:
        n = int(sys.argv[1])
    except IndexError:
        n = 1

    frm = ([], "A")
    for i in reversed(range(n)):
        frm[0].append(i+1)
    to = ([], "C")
    aux = ([], "B")
    moves = []
    game(len(frm[0]), frm, aux, to)
    sanity_check()
