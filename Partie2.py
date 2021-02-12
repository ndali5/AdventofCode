if __name__ == '__main__':
    fichier = open('input2', 'r')
    content = fichier.read()

    montableau = [x for x in content.split('\n')]

    for x in montableau:
        s = x.split(' ')
        min = s[0].split('-')[0]
        max = s[0].split('-')[1]
        mdp = s[2]
        lettre = s[1].split(":")[0]
        print(min,'-',max,'-',mdp, ' l:',lettre)
        