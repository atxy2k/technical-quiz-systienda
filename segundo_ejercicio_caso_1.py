# Caso 1: Solo tiene un plancha y tiros ilimitados. ¿qué harías?
import random

pisos = 1000

def tirar() -> bool:
    return random.choice([True, False])

def verificar(start: int, stop: int, step: int):
    print(f'================ VERIFICANDO DEL {start} AL {stop} / {step} ================')
    intervalos = []
    for n in [*range(start, stop, step)]:
        intervalos.append({
            "start": n,
            "stop": (n+step)-1
        })
    for intervalo in intervalos:
        print(f'Verificando pisos del {intervalo['start']} al {intervalo['stop']} / {step}')
        if tirar():
            print(f'Se rompio / step {step}')
            print(f'Se rompió entre el piso {intervalo['start']} y el piso {intervalo['stop']}')
            break
        else:
            print(f'No se rompio')

verificar(1, 1000, 100)