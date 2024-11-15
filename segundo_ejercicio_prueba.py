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
            if step == 1:
                print(f'Se rompió en el piso {intervalo['start']}')
                return intervalo['start']
            else:
                print(f'Se verificará intervalo {intervalo['start']} al {intervalo['stop']}, con intervalo {step//10}')
                return verificar(intervalo['start'], intervalo['stop'], step // 10)
        else:
            print(f'No se rompio')

verificar(1, 1000, 100)