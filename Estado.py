import matplotlib.pyplot as plt

class Estado:
    def __init__(self, nome, valor_faturamento):
        self.nome = nome
        self.valor_faturamento = valor_faturamento

    def calcular_percentual(self, total_faturamento):
        return self.valor_faturamento / total_faturamento * 100



sp = Estado("SP", 67836.43)
rj = Estado("RJ", 36678.66)
mg = Estado("MG", 29229.88)
es = Estado("ES", 27165.48)
outros = Estado("Outros", 19849.53)

calc_faturamento_total = sum([estado.valor_faturamento for estado in [sp, rj, mg, es, outros]])

calc_percentuais = [estado.calcular_percentual(calc_faturamento_total) for estado in [sp, rj, mg, es, outros]]

# grafico pizza
labels = [estado.nome for estado in [sp, rj, mg, es, outros]]
plt.pie(calc_percentuais, labels=labels, autopct='%1.1f%%')
plt.title("Percentual do faturamento mensal de cada estado")
plt.show()
