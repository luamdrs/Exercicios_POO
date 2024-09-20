class VerificadorIdade:
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    

print(VerificadorIdade.maior_idade(16))
print(VerificadorIdade.maior_idade(18))