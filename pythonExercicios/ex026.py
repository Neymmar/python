frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra (a) aparece ', frase.count('a'), 'na frase.')
print('A letra (a) aparece pela primeira vez na posição:', frase.find('a')+1)
print('A letra (a) aparece pela ultima vez na posição:', frase.rfind('a')+1)