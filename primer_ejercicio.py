#1. Dada una cadena de expresión exp, escriba un programa para examinar si los pares y los órdenes de "{", "}", "(", ")", "[", "]" son correctos en exp.
# Ejemplo:
#  
# correcto (({{[]}}))
#  
# incorrecto ([({))}

class Item:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.opposite = None
        if self.symbol == '(':
            self.opposite = ')'
        elif self.symbol == '{':
            self.opposite = '}'
        else:
            self.opposite = ']'


def remove_elements(expression: str, symbol: str) -> str:
    item = Item(symbol)
    if expression[0] == item.symbol:
        expression = expression[1:]
    else:
        raise Exception('Invalid expression')
    if expression[-1] == item.opposite:
        expression = expression[:-1]
    else:
        raise Exception('Invalid expression')
    return expression

def check(expression: str) -> bool:
    valid = False
    try:
        if len(expression) > 0:
            if len(expression) % 2 == 0:
                n = len(expression) // 2
                for i in range(n + 1):
                    remove_elements(expression, expression[0])
                valid = True
    except Exception as e:
        print(str(e))
    return valid

print(check('(({{[]}}))'))
print(check('([({))}'))



