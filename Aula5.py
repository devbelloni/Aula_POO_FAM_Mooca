# Sem encapsulamento

# class Conta:
#     def __init__(self):
#         self.saldo = 1000

#     def saldo(self):
#       return self.saldo          # permite VER o saldo

# conta = Conta()

# print(conta.saldo)

# conta.saldo = 2000

# print(conta.saldo)

#-------------------------------------------------------------------

# # Por convenção [_nome]

# class Conta:
#     def __init__(self):
#         self._saldo = 1000

#     def saldo(self):
#       return self._saldo          

# conta = Conta()

# print(conta._saldo)

# conta._saldo = 2000 # isso é proibido por convenção

# print(conta._saldo)

# ------------------------------------------------------------------------------

# mangling [__nome]
# mostrando que é proteção mecânica

# class Conta:
#     def __init__(self):
#         self.__saldo = 42

# t = Conta()

# print(t._Conta__saldo)    # → 42     (funciona)
# t._Conta__saldo = 100     # muda mesmo!
# print(t._Conta__saldo)    # → 100

# Isso dá erro (correto!):
# print(t.__saldo)       # AttributeError: 'Test' object has no attribute '__saldo'

# ------------------------------------------------------------------------------

# [__nome + @property]
# class Conta:
#     def __init__(self):
#         self.__saldo = 1000

#     @property
#     def saldo(self):
#       return self.__saldo

# conta = Conta()

# print(conta.saldo)

# conta.__saldo = 2000

# print(conta.saldo)

# ------------------------------------------------------------------------------------
# [@dataclass(frozen=True)]
from dataclasses import dataclass

@dataclass(frozen=True)     # frozen = "congelado"
class Conta:
    saldo: float = 1000
    nome: str = "Maria"

conta = Conta()

print(conta.saldo)         # 1000

# Isso dá erro:
conta.saldo = 5000       # FrozenInstanceError!
