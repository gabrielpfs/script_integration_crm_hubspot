# Integração HubSpot com Python - HubSpot Deals API Client

Este repositório contém um exemplo de como acessar negócios (deals) usando a API do HubSpot com o pacote `hubspot-api-client` em Python.

# Overview

O script conecta-se à API do HubSpot e recupera uma página de negócios (deals). Ele usa o cliente hubspot-api-client para realizar chamadas à API. Este exemplo demonstra como configurar o cliente, realizar uma solicitação para obter negócios e lidar com exceções.

## O que o Script esta fazendo?

O código Python está fazendo o seguinte:

1. Importa a biblioteca `hubspot`, a função `pprint` do módulo `pprint` e a classe `ApiException` do módulo `hubspot.crm.deals`.
2. Cria um cliente do HubSpot usando uma chave de API.
3. Tenta obter uma página de negócios (deals) do HubSpot com um limite de 10 e sem incluir negócios arquivados.
4. Imprime a resposta da API.
5. Se ocorrer uma `ApiException` durante a chamada da API, imprime a exceção.

## Instalação

Para instalar e executar este projeto, siga as etapas abaixo:

1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/hubspot-deals-api.git
    cd hubspot-deals-api
    ```
2. Navegue até a pasta do projeto:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```
3. Instale as dependências necessárias com o comando:
    ```bash
        pip install -r requirements.txt
    ```
    ```bash
    pip install hubspot-api-client
    ```
4. Atualize o pacote hubspot-api-client se necessário:
    ```bash
    pip install --upgrade hubspot-api-client
    ```

## Requirements

Para garantir que o projeto funcione corretamente, precisamos listar as dependências no arquivo requirements.txt. Com base no código, a dependência principal é a biblioteca `hubspot-api-client`.

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
python deals_hubspot_app_v2.py
python deals_hubspot_app_.py
python view_app.py
```

O script `python deals_hubspot_app_v2.py`, `python deals_hubspot_app_.py` e `python view_app.py.py` contém um teste simples para verificar uma página de negócios do HubSpot

## Execução do Script

Para realizar a execução dos Scripts deve-se, com o projeto aberto no VsCode abra o terminal e rode o comando:

```bash
python deals_hubspot_app_v2.py
python deals_hubspot_app_.py
python view_app.py
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

O script irá imprimir a resposta da API, que inclui uma lista de negócios. Aqui está um exemplo de como pode ser a saída:

```bash
{'results': [...], 'paging': {'next': {'after': '...' }}}
```

## Errors

O script inclui um bloco `try-except` para capturar exceções ao chamar a API. Se ocorrer um erro, uma mensagem será impressa:

```bash
except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)
```

## Configuracao

Substitua `YOUR_HUBSPOT_API_KEY` no código pelo seu API Key do HubSpot.

```bash
client = hubspot.Client.create(api_key="YOUR_HUBSPOT_API_KEY")
```

## Contribuição

Contribuições para este projeto são bem-vindas. Se você encontrar um bug ou acha que algo pode ser melhorado, sinta-se à vontade para abrir uma issue ou um pull request.

Caso deseja contribuir com seus conhecimentos para o Projeto, siga os seguintes passos:

1. Faça um fork do projeto.
2. Crie um branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -m 'Adiciona nova feature').
4. Push para o branch (git push origin feature/nova-feature).
5. Abra um Pull Request.

Lembre-se de que este é apenas um exemplo e você pode precisar ajustá-lo de acordo com as necessidades específicas do seu projeto.

## Accessando Views na visao de Negocios do Hubspot

### How to access Views via API?

I have created Views in Contacts, but I do not see a way to create/access Views with the HubSpot API.

### Is this possible?

We don’t have an API for getting views, so you’ll only be able to see that in the UI.

If you have the marketing tools, contact lists can work with most of the criteria that views use, and we do have a Contact Lists API.