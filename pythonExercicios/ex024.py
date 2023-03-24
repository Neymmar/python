'''
só irá considerar como true a cidade q começar com santo
'''
cid = str(input('Qual cidade você mora: ')).strip()
print(cid[:5].lower() == 'santo')
