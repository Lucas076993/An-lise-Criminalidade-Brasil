def converte_mes(x:str):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    try:
        return meses.index(x)
    except:
        return 99999