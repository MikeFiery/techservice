class Cliente:

    def __init__(self, nome, email, telefone="", id_cliente=None, status=1):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.status = status

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_telefone(self):
        return self.telefone

    def get_id_cliente(self):
        return self.id_cliente

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def set_nome(self, nome):
        self.nome = nome    

    def set_email(self, email):
        self.email = email

    def set_telefone(self, telefone):
        self.telefone = telefone
    