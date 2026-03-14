palavras = ("Cachorro","Girafa","Macaco","Rinoceronte","Bode","Cabra","Jacare","Onça")
for palavra in range (0, len(palavras)):
    print(f"\nAs VOGAIS da palavra {palavras[palavra]} são:", end =' ')
    for letra in palavras[palavra]:
        if letra.lower() in 'aeiou':
            print(f"{letra}", end =',')

