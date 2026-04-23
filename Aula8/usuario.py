class Usuario:
    def __init__(self, nome, email):
        self._nome = nome  # O '_' indica que o atributo é privado
        self._email = email

    @property # Este é o Getter
    def nome(self):
        return self._nome

    @nome.setter # Este é o Setter
    def nome(self, valor):
        self._nome = valor