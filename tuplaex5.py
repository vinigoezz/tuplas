#VOGAIS
letra = str(input('Digite uma letra: ')).upper().strip()[0]
vogal = ('A', 'E', 'I', 'O', 'U')
if letra in vogal:
    print(f'A letra {letra} é uma vogal.')
else:
    print(f'A letra {letra} é uma consoante')