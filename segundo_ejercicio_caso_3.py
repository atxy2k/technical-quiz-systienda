# Ahora solo tiene 2 platos. ¿Cuál es el número mínimo de lanzamientos para encontrar el suelo
import random

pisos = 1000

def tirar(disparos: list, platos: list) -> bool:
    disparos.append(1)
    response = random.choice([True, False])
    if response:
        platos.append(1)
    return response

def verificar(start: int, stop: int, step: int, disparos: list, platos: list):
    print(f'================ VERIFICANDO DEL {start} AL {stop} / {step} ================')
    intervalos = []
    for n in [*range(start, stop, step)]:
        intervalos.append({
            "start": n,
            "stop": (n+step)-1
        })
    for intervalo in intervalos:
        print(f'Verificando pisos del {intervalo['start']} al {intervalo['stop']} / {step}')
        if tirar(disparos, platos):
            print(f'Se rompio / step {step}')
            if step == 1:
                print(f'Se rompió en el piso {intervalo['start']}')
                return disparos
            else:
                if len(platos) == 2:
                    print(f'Se rompió entre el piso {intervalo['start']} y el piso {intervalo['stop']}')
                    break
                else:
                    print(f'Se verificará intervalo {intervalo['start']} al {intervalo['stop']}, con intervalo {step//10}')
                    return verificar(intervalo['start'], intervalo['stop'], step // 10, disparos, platos)
        else:
            print(f'No se rompio')
    return disparos
platos = []
disparos = []
disparos = verificar(1, 1000, 100, disparos, platos)
print(f'Número de disparos mínimos: {len(disparos)}')