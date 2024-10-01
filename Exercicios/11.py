class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    @classmethod
    def de_string(cls, data_str):
        dia, mes, ano = map(int, data_str.split('/'))
        return cls(dia, mes, ano)
    
    
    def mostrar_data(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    

data1 = Data.de_string('18/09/2024')
print(data1.mostrar_data())