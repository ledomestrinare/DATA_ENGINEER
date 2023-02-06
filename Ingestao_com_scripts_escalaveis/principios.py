import datetime
import math
from typing import List

# class Pessoa:
#     def __init__(
#         self,
#         nome: str,
#         sobrenome: str,
#         data_nascimento: datetime.date) -> None:
        
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.data_nascimento = data_nascimento
    
#     @property
#     def idade(self) -> int:
#         return math.floor((datetime.date.today() - self.data_nascimento).days / 365.24) 
    
#     def __str__(self) -> str:
#         return f"{self.nome} {self.sobrenome} tem {self.idade} anos"
    

# class Curriculo:
#     def __init__(self, pessoa: Pessoa, experiencias: List[str]) -> None:
#         self.pessoa = pessoa
#         self.experiencias = experiencias
        
#     @property
#     def quantidade_experiencias(self) -> int:
#         return len(self.experiencias)

#     @property
#     def empresa_atual(self) -> str:
#         return self.experiencias[-1]
    
#     def adiciona_experiencia(self, experiencia: str) -> None:
#         self.experiencias.append(experiencia)
        
        
#     def __str__(self) -> str:
#         return f"{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.idade} anos e já " \
#             f"trabalhou com {self.quantidade_experiencias} experiência(s) e "\
#             f"atualmente trabalha na empresa {self.empresa_atual}"

# andre = Pessoa(nome='André', sobrenome='Silva', data_nascimento=datetime.date(1991,1,9))

# curriculo_andre = Curriculo(
#     pessoa=andre, 
#     experiencias=['HSBC', 'Polytech', 'Grupo Boticário', 'Olist', 'EmCasa', 'Gousto']
#     )

# curriculo_andre.adiciona_experiencia('How Education')

class Vivente:
    def __init__(self, nome: str, data_nascimento: datetime.date) -> None:
        self.nome = nome
        self.data_nascimento = data_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_nascimento).days / 365.24) 
    
    def emite_ruido(self, ruido: str):
        print(f"{self.nome} fez ruido: {ruido}")


class PessoaHeranca(Vivente):
    def __str__(self) -> str:
        return f"{self.nome} tem {self.idade} anos"
    
    def fala(self, frase):
        return self.emite_ruido(frase)
        

class Cachorro(Vivente):
    def __init__(self, nome: str, data_nascimento: datetime.date, raca: str) -> None:
        super().__init__(nome=nome, data_nascimento=data_nascimento)
        self.raca = raca
    
    def __str__(self) -> str:
        return f"{self.nome} é da raça {self.raca} e tem {self.idade} anos"
    
    def late(self):
        return self.emite_ruido('Au! Au!')

andre2 = PessoaHeranca(nome='André', data_nascimento=datetime.date(1991,1,9))
print(andre2)

belisco = Cachorro(nome='Belisco', data_nascimento=datetime.date(2019,4,15), raca='Lhasa Apso')

print(belisco)
belisco.late()
belisco.late()
belisco.late()
belisco.late()
belisco.late()
belisco.late()
andre2.fala('Cala a boca Belisco')
belisco.late()


