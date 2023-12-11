# Projeto de Classificação de Risco

Este projeto implementa um sistema de classificação de risco de crédito usando aprendizado de máquina. Ele consiste em um modelo de aprendizado de máquina localizado na pasta `ml`, um aplicativo cliente e um servidor que fornece um serviço de análise de crédito.

## Estrutura do Projeto

```
|-- ml
| |-- ... # Arquivos do Modelo de Aprendizado de Máquina
|-- client
| |-- ... # Arquivos do Aplicativo Cliente
|-- server 
| |-- ... # Arquivos do Aplicativo Servidor
| |-- Makefile
| |-- docs/open_api/swagger.yaml
|-- README.md

```

## Modelo de Aprendizado de Máquina (ml)

A pasta `ml` contém os arquivos relacionados ao modelo de aprendizado de máquina usado para classificação de risco de crédito.

## Cliente (cliente)

A pasta `cliente` contém o aplicativo cliente que interage com o serviço de análise de crédito.

## Servidor (servidor)

A pasta `servidor` contém o aplicativo servidor que fornece o serviço de análise de crédito.

### Como Executar o Servidor

Para executar o servidor, navegue até a pasta `servidor` e use o Makefile fornecido:

```bash
cd server 
pip install -r requirements.txt
make run
```

## Documentação da API (Swagger)
A documentação da API está disponível no arquivo swagger.yaml. Ele fornece detalhes sobre os endpoints, parâmetros de solicitação e respostas.

## Analisar Crédito (/v1/analyze_credit)
O endpoint /v1/analyze_credit é usado para análise de risco de crédito. Ele aceita dados JSON representando os atributos para avaliação de crédito e retorna os resultados da análise.

Solicitação:
Método: POST
Caminho: /v1/analyze_credit
Tipo de Conteúdo: application/json

Exemplo de Solicitação

```
{
  "Attribute1": "A11",
  "Attribute2": 12,
  "Attribute3": "A30",
  ...
}
```

Resposta
Exemplo de Resposta:

```
{
  "prediction": 1,
  "class": "Bom",
  "mapped_response": {
    "Attribute1": "A11",
    "Attribute2": 12,
    "Attribute3": "A30",
    ...
  }
}
```

