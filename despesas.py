import matplotlib.pyplot as plt
import csv

class ControleDeGastosAI:
    def __init__(self):
        self.despesas = {}
        self.limites = {}

    def adicionar_despesa(self, categoria, valor):
        if categoria in self.despesas:
            self.despesas[categoria] += valor
        else:
            self.despesas[categoria] = valor

        if categoria in self.limites and self.despesas[categoria] > self.limites[categoria]:
            print(f"Atenção! Você ultrapassou o limite para {categoria}.")

        print(f'Adicionado {valor:.2f} à {categoria}')

    def remover_despesa(self, categoria, valor):
        if categoria in self.despesas:
            self.despesas[categoria] -= valor
            if self.despesas[categoria] <= 0:
                del self.despesas[categoria]
            print(f'Removido {valor:.2f} de {categoria}')
        else:
            print(f'Nenhuma despesa encontrada em {categoria}.')

    def definir_limite(self, categoria, limite):
        self.limites[categoria] = limite
        print(f'Limite de {limite:.2f} definido para {categoria}')

    def ver_total_despesas(self):
        total = sum(self.despesas.values())
        print(f'Total de despesas: {total:.2f}')
        return total

    def ver_despesas_por_categoria(self):
        print("Despesas por categoria:")
        for categoria, valor in self.despesas.items():
            print(f'{categoria}: {valor:.2f}')

    def sugerir_dicas_economicas(self):
        total = self.ver_total_despesas()
        if total > 1000:
            print("Suas despesas estão altas! Considere reduzir categorias não essenciais.")
        elif total > 500:
            print("Você está gastando moderadamente. Tente economizar onde puder.")
        else:
            print("Seus gastos estão sob controle. Continue assim!")

    def exportar_para_csv(self, nome_arquivo="despesas.csv"):
        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Categoria", "Valor", "Limite"])
            for categoria, valor in self.despesas.items():
                limite = self.limites.get(categoria, "Sem limite")
                writer.writerow([categoria, valor, limite])
        print(f"Despesas exportadas para {nome_arquivo}")

    def plotar_despesas(self):
        categorias = list(self.despesas.keys())
        valores = list(self.despesas.values())

        plt.figure(figsize=(8, 6))
        plt.bar(categorias, valores, color='blue')
        plt.xlabel('Categorias')
        plt.ylabel('Valor Gasto')
        plt.title('Despesas por Categoria')
        plt.show()

def main():
    ai = ControleDeGastosAI()

    while True:
        print("\n1. Adicionar despesa")
        print("2. Remover despesa")
        print("3. Definir limite de categoria")
        print("4. Ver total de despesas")
        print("5. Ver despesas por categoria")
        print("6. Obter dicas de economia")
        print("7. Exportar despesas para CSV")
        print("8. Mostrar gráfico de despesas")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            categoria = input("Informe a categoria (ex: Alimentação, Transporte, Entretenimento): ")
            valor = float(input("Informe o valor: "))
            ai.adicionar_despesa(categoria, valor)
        elif escolha == '2':
            categoria = input("Informe a categoria para remover: ")
            valor = float(input("Informe o valor a ser removido: "))
            ai.remover_despesa(categoria, valor)
        elif escolha == '3':
            categoria = input("Informe a categoria para definir o limite: ")
            limite = float(input("Informe o limite: "))
            ai.definir_limite(categoria, limite)
        elif escolha == '4':
            ai.ver_total_despesas()
        elif escolha == '5':
            ai.ver_despesas_por_categoria()
        elif escolha == '6':
            ai.sugerir_dicas_economicas()
        elif escolha == '7':
            nome_arquivo = input("Informe o nome do arquivo para exportar (padrão: despesas.csv): ")
            if nome_arquivo.strip() == "":
                nome_arquivo = "despesas.csv"
            ai.exportar_para_csv(nome_arquivo)
        elif escolha == '8':
            ai.plotar_despesas()
        elif escolha == '9':
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
