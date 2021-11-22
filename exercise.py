import functools

def get_year(data):
    ano = str(data)
    ano = ano.split('/')
    return int(ano[2])

file = './base.csv'

# Abre o arquivo colocando linha por linha na memória
lines = (line for line in open(file))

# Separa cada vírgula como uma coluna
list_line = (s.rstrip().split(',') for s in lines)
cols = next(list_line)

# Converte cada linha para um dicionário com as chaves 'cols'
dicionario = (dict(zip(cols, data)) for data in list_line)

# Filtra as datas maiores ou iguais a 2012
dicionario = filter(lambda d: get_year(d['12 months ending']) > 2012, dicionario)
# map(int,(dicionario['Rolling year total number of offences'] for dicionario in dicionario))

# Reduce
total_crimes = functools.reduce(lambda soma, d: soma + int(d['Rolling year total number of offences']), dicionario, 0)

print(f'O número total de crimes à partir de 2012, foi de: {total_crimes}')