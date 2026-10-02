class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self._salario = salario
    def __str__(self):
        return f"Nome Funcionário: {self.nome}\n|Cargo: {self.cargo}\n|Salario: {self.cambio_salario}"
    @property
    def cambio_salario(self):
        return f"R${round(self._salario,2)}"
    def aumentar_salario(self, percentual):
        calculo_percentual = percentual / 100
        aumento = self._salario * calculo_percentual
        self._salario = self._salario + aumento

paulo = Funcionario("Paulo", "Repositor", 2500)
Funcionario.aumentar_salario(paulo, 15)
print(paulo)