# Análise de Criminalidade do Brasil

Olá! Este projeto visa criar uma ferramenta que forneça gráficos com tendências sobre o número de ocorrências de determinados crimes no Brasil.

## Um pouco sobre

A ferramenta consiste em uma aplicação em terminal, que com alguns comandos básicos, descritos em um menu, gera gráficos de ocorrências. Os gráficos contem análises de tendências simples, como uma regressão linear e a média móvel de ocorrências, mas muito explicativas sobre o conjunto de dados. A janela utilizada para média móvel é de 3 meses.

## Sobre os dados

Os dados utilizados estão disponíveis no Portal de Dados Abertos no site do governo federal (https://dados.gov.br/dados/conjuntos-dados/sistema-nacional-de-estatisticas-de-seguranca-publica). A granularidade temporal dos dados utilizados é mensal, enquanto a granularidade espacial é a nível de unidades federativas. Não foram encontrados no portal dados recentes de todas as unidades federativas, apenas de alguns poucos estados. Por conta disso, as análises vão de janeiro de 2015 à novembro de 2022.

## Como usar

Basta executar o arquivo main.py utilizando o interpretador Python. Será gerado um menu no próprio terminal com instruções sobre como utilizar a ferramenta.

## Trabalhos futuros

Encontrar e adicionar a análise dados mais recentes. Adicionar mais funcionalidades a ferramente, como outros tipos de regressão e análise preditiva.

## Dicas e sugestões

Caso queira dar qualquer dica, sugestão ou crítica construtiva, o email para contato é: lucaspaiva280@gmail.com

### Patch notes

- 1.0.0: Ferramenta lançada.
