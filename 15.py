times = ('FLAMENGO','PALMEIRAS','SÃO PAULO','CORINTHIANS', 'FLUMINENSE', 'GRÊMIO', 'FORTALEZA', 'BOTAFOGO')

user = str(input("Qual time ? ")).strip().upper()
if user in times:
    posicao = times.index(user)
    print("Esse time está na Tupla !")
    print(f"Este é o {posicao+1}° time da sua tupla que se encontra na POSIÇÃO {posicao}")
else:
    print("Não temos esse time na Tupla !")
