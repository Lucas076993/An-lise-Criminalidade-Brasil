import pandas as pd
from printar_dados import printar_dados

data = pd.read_excel("data/bruto/indicadoressegurancapublicauf.xlsx")
crimes_disponiveis = data["Tipo Crime"].unique()
ufs_disponiveis = data["UF"].unique()
print("\nBEM VINDO AO PAINEL CLI DOS DADOS DO CRIME")
while(True):
    print("\nOpções:\n 1- Printar Crime\n 2- Mostrar tipos de crime disponíveis\n 3- Mostrar UF's disponíveis\n 4- Sair")
    
    try:
        menu = int(input("$: "))
        
        if not menu  in [1, 2, 3, 4] :
            raise Exception("Opção Inválida!!!!")
        
        if menu == 1:
            tipo = input("Tipo de Crime: ")
            if not tipo in crimes_disponiveis:
                raise Exception("Tipo de Crime Inválido!!!!")
                
            
            uf = input("UF: ")
            if not uf in ufs_disponiveis:
                raise("Unidade Federativa Inválida!!!!")

            printar_dados(data, uf, tipo)
            print("Gráfico Gerado!!!!")

        if menu == 2:
            print("Tipos de crimes disponíveis para análise:\n - ")
            print(*crimes_disponiveis, sep="\n - ")

        if menu == 3:
            print("Unidades Federativas disponíveis para análise:")
            print(*ufs_disponiveis, sep="\n - ")

        if menu == 4:
            print("Encerrando...")
            break
    except Exception as erro:
        print(erro)
