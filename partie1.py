if __name__ == '__main__':
    fichier = open('input1', 'r')
    content = fichier.read()

    montableau = [int(i) for i in content.split('\n')]
    for i in montableau:
        for j in montableau:
            for h in montableau:
                x = i + j + h
                if x == 2020 :
                    print (i, '+',j, '+',h ,'=', 2020)
                    print(i*j*h)