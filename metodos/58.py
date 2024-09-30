# __del__(self) -> É o método destrutor, chamado quando o 
# objeto é destruído ou coletado pelo garbage collector.

class Material:

    def __del__(self):
        print('O objeto do Material foi destruído.')


material = Material()
del material