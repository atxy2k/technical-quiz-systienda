# Hay platos ilimitados. ¿Cuál es el número mínimo de disparos para encontrar el suelo?
import random

pisos = 1000

def tirar(disparos: list) -> bool:
    disparos.append(1)
    return random.choice([True, False])

def verificar(start: int, stop: int, step: int, disparos: list):
    print(f'================ VERIFICANDO DEL {start} AL {stop} / {step} ================')
    intervalos = []
    for n in [*range(start, stop, step)]:
        intervalos.append({
            "start": n,
            "stop": (n+step)-1
        })
    for intervalo in intervalos:
        print(f'Verificando pisos del {intervalo['start']} al {intervalo['stop']} / {step}')
        if tirar(disparos):
            print(f'Se rompio / step {step}')
            if step == 1:
                print(f'Se rompió en el piso {intervalo['start']}')
                return disparos
            else:
                print(f'Se verificará intervalo {intervalo['start']} al {intervalo['stop']}, con intervalo {step//10}')
                return verificar(intervalo['start'], intervalo['stop'], step // 10, disparos)
        else:
            print(f'No se rompio')
    return disparos
disparos = []
disparos = verificar(1, 1000, 100, disparos)
print(f'Número de disparos mínimos: {len(disparos)}')