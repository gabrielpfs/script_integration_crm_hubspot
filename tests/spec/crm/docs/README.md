# Projeto de Exportação de Contatos do HubSpot

Este projeto é um script Python simples que usa a API do HubSpot para exportar contatos e negocios para um arquivo JSON.

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `requests`: Usada para fazer requisições HTTP para a API do HubSpot.
- `json`: Usada para manipular dados no formato JSON.

## How to use

Primeiro, substitua `'YOUR_LIST_ID'` pelo ID da lista que você deseja acessar no arquivo principal do script.

Em seguida, execute o script Python. Ele fará requisições à API do HubSpot para obter todos os contatos da lista especificada e os salvará em um arquivo JSON chamado `deals_app.json`, `contacts_app.json` e  `contacts_especific_list_app.json`.

```python
python main.py
```

## Script Result

Após a execução do script, você verá uma mensagem informando quantos contatos foram exportados para o arquivo `JSON`.

## Contribuindo

Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar uma solicitação pull.
