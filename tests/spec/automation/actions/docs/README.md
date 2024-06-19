# Integração HubSpot com Python - HubSpot Automation Actions Test

O código é um teste que verifica se as APIs de automação do HubSpot são descobertas corretamente através da biblioteca Python da HubSpot.

O código usa a biblioteca HubSpot para Python e verifica se as APIs de automação (CallbacksApi, DefinitionsApi, FunctionsApi, RevisionsApi) são acessíveis através do objeto HubSpot().automation.actions. Aqui está o que cada parte do código faz:

```bash
from hubspot import HubSpot
from hubspot.automation.actions import (
    CallbacksApi,
    DefinitionsApi,
    FunctionsApi,
    RevisionsApi,
)
```
1. Importa a classe `HubSpot` da biblioteca `hubspot`.
2. Importa as APIs de automação específicas: `CallbacksApi`, `DefinitionsApi`, `FunctionsApi`, `RevisionsApi`.

# Overview

O código realiza testes de unidade para garantir que as APIs de automação (`CallbacksApi`, `DefinitionsApi`, `FunctionsApi`, `RevisionsApi`) sejam acessíveis através do objeto `HubSpot().automation.actions`.

## Instalação

Para instalar e executar este projeto, siga as etapas abaixo:

1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/hubspot-automation-automations-other-actions.git
    cd hubspot-automation-automations-other-actions
    ```
2. Navegue até a pasta do projeto:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```
3. Instale as dependências necessárias com o comando:
    ```bash
        pip install hubspot-api-client
    ```

## Requirements

Para garantir que o projeto funcione corretamente, precisamos listar as dependências no arquivo requirements.txt.

Caso queira clonar o repositório e quiser instalar as dependências, podera usar o seguinte comando:

1. Clone o repositório para sua máquina local.
2. Navegue até a pasta do projeto.
3. Instale as dependências necessárias com o comando:

```bash
pip install -r requirements.txt
```


## Execução do Script

Para executar o teste, podemos utilizar o `pytest`:

1. Instale o `pytest` se ainda não tiver instalado:
    ```bash
    pip install pytest
    ```
2. Execute o teste:
    ```bash
    pytest test_actions.py
    ```

Para realizar a execução dos Scripts deve-se, com o projeto aberto no VsCode abra o terminal e rode o comando:

```bash
python test_actions.py
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

## Contribuição

Contribuições para este projeto são bem-vindas. Se você encontrar um bug ou acha que algo pode ser melhorado, sinta-se à vontade para abrir uma issue ou um pull request.

Caso deseja contribuir com seus conhecimentos para o Projeto, siga os seguintes passos:

1. Faça um fork do projeto.
2. Crie um branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -m 'Adiciona nova feature').
4. Push para o branch (git push origin feature/nova-feature).
5. Abra um Pull Request.
