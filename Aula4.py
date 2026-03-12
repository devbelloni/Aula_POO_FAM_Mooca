class Teste1:
    def __init__(self, teste):
        self.teste = teste
        print(f"Executando init para o objeto no endereço: {hex(id(self))}")

    def demonstra(self):
        print(f"""
            Executando demonstração para o objeto no endereço: {hex(id(self))}
            valor {self.teste}
        """)

a = Teste1(2)
b = Teste1(3)

print(f"Endereço A: {hex(id(a))}")
print(f"Endereço B: {hex(id(b))}")
print(f"São o mesmo objeto? {a is b}")

print("-" * 30)
a.demonstra()
b.demonstra()

# ---------------------------------------------------------------------
# Singleton é uma técnica que permite sobrescrever a classe anterior.
# Há uma alocação fixa de memória
# ---------------------------------------------------------------------

class Teste2:
    _instance = None  # Variável de classe para armazenar a instância única

    def __new__(cls, *args, **kwargs):
        # O __new__ recebe a classe (cls) e não a instância (self)
        if cls._instance is None:
            print("[__new__]: Alocando nova memória...")
            # Chamamos o método da superclasse (object) para alocar os bytes
            cls._instance = super().__new__(cls)
        else:
            print("""
            [__new__]: Objeto já existe. Reciclando endereço de memória...
            """)

        return cls._instance

    def __init__(self, teste):
        print(f"[__init__]: Inicializando objeto no endereço: {hex(id(self))}")

        self.teste = teste
        print(f"Executando init para o objeto no endereço: {hex(id(self))}")

    def demonstra(self):
      print(f"""
      Executando demonstração para o objeto no endereço: {hex(id(self))}
      valor {self.teste}
            """)

print("Tentativa 1: Criando objeto 'a'")
a = Teste2(2)

print("\nTentativa 2: Criando objeto 'b'")
b = Teste2(3)

print("\n" + "="*40)
print(f"Endereço A: {hex(id(a))}")
print(f"Endereço B: {hex(id(b))}")
print(f"São o mesmo objeto na memória? {a is b}")

print("-" * 30)
a.demonstra()
b.demonstra()