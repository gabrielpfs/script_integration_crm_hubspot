# Integração HubSpot com Python - HubSpot Contacts Exporter

Este projeto é um script Python para exportar todos os contatos de sua conta do HubSpot e salvá-los em um arquivo `JSON`.

# Overview

Este script usa a API do HubSpot para buscar todos os contatos de uma conta e os salva em um arquivo `JSON` chamado `contacts_application.json`. Ele lida com a paginação automaticamente para garantir que todos os contatos sejam recuperados.

## O que o Script esta fazendo?

O código Python está fazendo o seguinte:

1. Importa os módulos `requests` e `json`.
2. Define a chave de acesso (`access token`) e a `URL` da API do HubSpot para contatos.
3. Define os cabeçalhos da requisição `HTTP`, que incluem a chave de acesso e o tipo de conteúdo.
4. Define uma função `get_all_contacts` que:
    1. Inicializa uma lista vazia de contatos e algumas variáveis de controle para a paginação.
    2. Entra em um loop que continua enquanto houver mais páginas de contatos para buscar.
    3. Dentro do loop, faz uma requisição `GET` para a `URL` da API, passando os cabeçalhos e os parâmetros da requisição.
    4. Processa a resposta da API, adicionando os contatos retornados à lista de contatos e atualizando as variáveis de controle para a paginação.
5. Chama a função `get_all_contacts` para obter todos os contatos e armazena o resultado na variável `contacts`.
6. Exporta os contatos para um arquivo `JSON` chamado `contacts_application.json`.
7. Imprime a quantidade de contatos exportados.

Obs.: 

## Instalação

Para instalar e executar este projeto, siga as etapas abaixo:

1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/hubspot-contacts-exporter.git
cd hubspot-contacts-exporter
    ```
2. Navegue até a pasta do projeto:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```
3. Instale as dependências necessárias com o comando:
    ```bash
        pip install requests
    ```
4. Substitua `YOUR_ACCESS_TOKEN` no script `contacts_app.py` pelo seu token de acesso privado do HubSpot:
    ```bash
    python contacts_app.py
    ```
O script exportará todos os contatos para um arquivo chamado `contacts_app.json` no diretório atual e imprimirá o número total de contatos exportados.

## Requirements

Para garantir que o projeto funcione corretamente, precisamos listar as dependências no arquivo requirements.txt.

Caso queira clonar o repositório e quiser instalar as dependências, podera usar o seguinte comando:

1. Clone o repositório para sua máquina local.
2. Navegue até a pasta do projeto.
3. Instale as dependências necessárias com o comando:

```bash
pip install -r requirements.txt
```

## Uso

Para usar este projeto, você precisa substituir `YOUR_HUBSPOT_API_KEY` pela sua chave de API do HubSpot no script. Em seguida, você pode executar o script para obter uma página de negócios do HubSpot.

```bash
python contacts_app.py
python contacts_specific_list_app_.py
```

O script `contacts_app.py` e `contacts_specific_list_app.py` contém um teste simples para verificar uma página de negócios do HubSpot

## Execução do Script

Para realizar a execução dos Scripts deve-se, com o projeto aberto no VsCode abra o terminal e rode o comando:

```bash
python contacts_app.py
python contacts_specific_list_app_.py
```

Passo a passo para realizar esse processo, siga as etapas abaixo:

1. No topo do VsCode vai encontrar a barra de comando com as denominacoes File, Edit, Selection, View, Go, Run e ...:
    ```bash
    ![Tutorial](http://url/to/comand_bar.png)
    ```
2. Apos isso, va em Terminal:
    ```bash
    ![Tutorial](http://url/to/terminal.png)
    ```
3. E, por fim, clicar em New Terminal:
    ```bash
        ![Tutorial](http://url/to/new_terminal.png)
    ```
4. De outra maneira podemos, simplesmente, realizar o atalho Ctrl+Shift+`.

## Result

O script irá imprimir a resposta da API, que inclui uma lista de contatos em `contacts_app.py` e `contacts_specific_list_app_.py` com um tratamento para puxar a lista de informacoes de um contato. Aqui está um exemplo de como pode ser a saída:

```bash
{'results': [...], 'paging': {'next': {'after': '...' }}}
```

## Configuracao

Substitua `YOUR_HUBSPOT_API_KEY` no código pelo seu API Key do HubSpot.

```bash
access_token = 'YOUR_ACCESS_TOKEN'
```

## Contribuição

Contribuições para este projeto são bem-vindas. Se você encontrar um bug ou acha que algo pode ser melhorado, sinta-se à vontade para abrir uma issue ou um pull request.

Caso deseja contribuir com seus conhecimentos para o Projeto, siga os seguintes passos:

1. Faça um fork do projeto.
2. Crie um branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -m 'Adiciona nova feature').
4. Push para o branch (git push origin feature/nova-feature).
5. Abra um Pull Request.
