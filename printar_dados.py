import pandas as pd
from converte_mes import converte_mes as cm
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def printar_dados(data, uf, tipo):
    # reta da regressão linear
    def reta(x, a, b):
        return a * x + b 

    # limpeza de dados
    data = data[data["UF"] == uf]
    data = data[data["Tipo Crime"] == tipo]


    # convertendo meses pra int
    data["Mês"] = data["Mês"].apply(lambda x: cm(x))

    # ordenando os valores e ajustando o index
    data = data.sort_values(by=["Ano", "Mês"], ascending=True)
    data = data.reset_index()


    # calcula médias móveis com janela de 3 dias
    media_movel = data["Ocorrências"].rolling(3, min_periods=1).mean()

    # ajuste da reta
    parametros = curve_fit(reta, data.index, media_movel)[0]
    ajuste = reta(data.index, parametros[0], parametros[1])


    # plottando dados
    plt.scatter(data.index, data["Ocorrências"], s=1, label="Dados")
    plt.plot(data.index, media_movel, label="Média Móvel", color="g")
    plt.plot(data.index, ajuste, label="Regressão Linear", color="r")

    plt.title("Casos de {} em {}".format(tipo, uf))
    plt.legend()

    plt.xlabel("Mês")
    plt.ylabel(tipo)

    plt.savefig("data/graficos/dados.png")

if __name__ == "__main__":
    uf = "Rio de Janeiro"
    tipo = "Homicídio doloso"
    data = pd.read_excel("data/bruto/indicadoressegurancapublicauf.xlsx")

    printar_dados(data, uf, tipo)