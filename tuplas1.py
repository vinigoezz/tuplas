from time import sleep
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético - MG', 'Botafogo', 'Athletico -PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'Ec vitoria', 'Coritiba', 'Avaí', 'Ponte preta', 'Atlético-GO')
print(f'Lista de times do brasileirão:{times}')
sleep(0.5)
print(f'Os 5 primeiros são: {times[0:5]}')
sleep(0.5)
print(f'Os 4 últimos são: {times[-4:]}')
sleep(0.5)
print(f'Times em ordem alfabética: {sorted(times)}')
sleep(0.9)
print(f'A Chapecoense está na {times.index("Chapecoense")}° posição')