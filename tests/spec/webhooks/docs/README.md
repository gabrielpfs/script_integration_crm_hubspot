# Integração HubSpot com Python - HubSpot Webhooks API Test

## Descrição

Este projeto foi criado para integrar o HubSpot usando scripts Python. O objetivo principal é trazer informações da visão de contatos e coletar todas as informações de todos os contatos. Isso permite uma visão mais clara e detalhada dos contatos, facilitando a gestão e a tomada de decisões.

Esse `test_webhooks` foi construido para testar como funcionaria utilizando conhecimento de de APIs de configurações e assinaturas webhook com importação de configurações do proprio HubSpot `from HubSpot import HubSpot`.

Este projeto fornece um exemplo de como verificar se as APIs de configurações e assinaturas do módulo de webhooks da biblioteca HubSpot estão corretamente instanciadas.

## O que o Script esta fazendo?

O código Python está fazendo o seguinte:

1. Importa a classe `HubSpot` do módulo `hubspot`.
2. Importa as classes `SubscriptionsApi` e `SettingsApi` do módulo `hubspot.webhooks`.
3. Define uma função de teste chamada `test_is_discoverable()`.
4. Dentro dessa função, ele cria uma instância da classe `HubSpot` e acessa a propriedade `webhooks`.
5. Em seguida, verifica se `apis.settings_api` é uma instância de `SettingsApi` e se `apis.subscriptions_api` é uma instância de `SubscriptionsApi`.

Essencialmente, este é um teste para verificar se as APIs de configurações e assinaturas do webhook estão corretamente configuradas e são acessíveis através da instância da classe `HubSpot`.

## Webhooks

Um webhook é uma função de retorno de chamada baseada em HTTP que viabiliza a comunicação lightweight e orientada por eventos entre duas APIs (Interfaces de Progracao de Aplicacoes). Os webhooks são usados por várias apps (aplicacoes) web para receber pequenos volumes de dados de outras apps (aplicacoes).

### Webhooks HubSpot

A API de Webhooks permite assinar eventos que acontecem em uma conta da HubSpot com sua integração instalada. Em vez de fazer uma chamada de API quando um evento acontece em uma conta conectada, o HubSpot pode enviar uma solicitação HTTP para um endpoint que você configurar.

O uso da API dos Webhooks requer o seguinte:

1. Configurar um aplicativo da HubSpot para usar webhooks, inscrevendo-se nos eventos sobre os quais deseja ser notificado e especificando um URL para envio dessas notificações.
2. Implantar um endpoint seguro (HTTPS) e disponível publicamente para esse URL que seja capaz de lidar com as cargas do webhook.

Os webhooks estão configurados para um [aplicativo da HubSpot](https://developers.hubspot.com/docs/faq/how-do-i-create-an-app-in-hubspot?_ga=2.238823232.190745408.1718018636-1581166926.1715862096&_gl=1*1uxslcr*_gcl_au*ODY3OTkzMjk0LjE3MTU4NjIwOTU.*_ga*MTU4MTE2NjkyNi4xNzE1ODYyMDk2*_ga_LXTM6CQ0XK*MTcxODAyMjM3My4xNS4xLjE3MTgwMjI2MTcuMTQuMC4w).

Para mais informações em relação aos Webhooks API para conexão com o CRM HubSpot, segue o link da documentação: [HubSpot API Docs | Webhooks](https://developers.hubspot.com/docs/api/webhooks)

## Instalação

Para instalar e executar este projeto, siga as etapas abaixo:

1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/hubspot-webhooks-api-test.git
    cd hubspot-webhooks-api-test
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

Para usar este projeto, execute o script principal teste `test_webhooks.py`. Isso iniciará o processo de coleta de informações de contato do HubSpot.

```bash
python test_webhooks.py
```

O script `test_webhooks.py` contém um teste simples para verificar se as APIs de configurações e assinaturas do módulo de webhooks estão acessíveis.

## Execução do Script

Para realizar a execução do Script deve-se, com o projeto aberto no VsCode abra o terminal e rode o comando:

```bash
python test_webhooks.py
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

Lembre-se de que este é apenas um exemplo e você pode precisar ajustá-lo de acordo com as necessidades específicas do seu projeto.