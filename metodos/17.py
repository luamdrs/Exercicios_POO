class UtilidadesNumericas:
    @staticmethod
    def eh_par(numero):
        return numero % 2 == 0
    

print(UtilidadesNumericas.eh_par(5))
print(UtilidadesNumericas.eh_par(4))