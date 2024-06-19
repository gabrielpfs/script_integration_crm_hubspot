# Integração HubSpot com Python - HubSpot Authurl and Signature Tests

## Descrição test_signature

Este projeto é uma biblioteca Python para a integração com a API do HubSpot. Ele fornece uma série de testes para a classe `Signature` do módulo `hubspot.utils.signature`. Esses testes verificam a correta geração e validação de assinaturas para diferentes versões e cenários.

Os testes cobrem as seguintes áreas:

- Geração de assinaturas para diferentes versões (`v1`, `v2`, `v3`)
- Validação das assinaturas para garantir sua autenticidade
- Tratamento de erros para versões de assinaturas inválidas
- Validação de assinaturas com timestamps ausentes ou expirados

## Descrição test_signature

Este repositório contém testes para a geração de URLs de autenticação OAuth utilizando a biblioteca `hubspot`.

O código neste repositório verifica a funcionalidade de geração de URLs de autenticação OAuth da HubSpot. Especificamente, ele testa a função `get_auth_url` para assegurar que os parâmetros corretos são incluídos nas URLs geradas.

## What is pytest and how it could help us?

The `pytest` framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

`pytest` requires: Python 3.8+ or PyPy3.

## Getting Start with pytest

1. Run the following command in your command line:

```
pip install -U pytest
```

2. Check that you installed the correct version:

```
$ pytest --version
pytest 8.2.2
```

## Instalação

Caso queira clonar o repositório e quiser instalar as dependências, podera usar o seguinte comando:

1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/hubspot-signature-tests.git
    cd hubspot-signature-tests
    ```
2. Navegue até a pasta do projeto ou crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
3. Instale as dependências necessárias com o comando:
    ```bash
    pip install -r requirements.txt
    ```
4. Rodando os Testes:
    ```bash
    pytest
    ```

## Estrutura do Projeto e Testes

### Geração de Assinaturas

`test_get_signature__v1`: Testa a geração de uma assinatura versão v1.
`test_get_signature__v2`: Testa a geração de uma assinatura versão v2 incluindo a URL.
`test_get_signature__v3`: Testa a geração de uma assinatura versão v3 incluindo a URL, método HTTP e timestamp.
`test_get_signature__wrong_version`: Garante que uma exceção `InvalidSignatureVersionError` seja lançada para uma versão de assinatura inválida.

### Geração de Assinaturas

`test_is_valid__v1`: Valida a assinatura versão `v1`.
`test_is_valid__v2`: Valida a assinatura versão `v2` incluindo a `URL`.
`test_is_valid__v2_get_method`: Valida a assinatura versão `v2` com o método HTTP `GET`.
`test_is_valid__v3`: Valida a assinatura versão `v3` com `timestamp` atual.
`test_is_valid__none_timestamp`: Garante que uma exceção `InvalidSignatureTimestampError` seja lançada se o `timestamp` estiver ausente para a versão `v3`.
`test_is_valid__expired_timestamp`: Garante que uma exceção `InvalidSignatureTimestampError` seja lançada se o `timestamp` estiver expirado para a versão `v3`.

### Configuracao de Autenticacao

`DATA`: Um dicionário contendo informações de configuração para a autenticação OAuth.

`test_get_auth_url__empty_scope`: Verifica se a URL é gerada corretamente quando nenhum escopo é especificado.
`test_get_auth_url__scope`: Verifica se a URL é gerada corretamente quando escopos específicos são fornecidos.
`test_get_auth_url__optional_scope`: Verifica se a URL é gerada corretamente quando escopos opcionais são fornecidos.
`test_get_auth_url__state`: Verifica se a URL é gerada corretamente quando o parâmetro `state` é fornecido.

### Configuracao de Dependencias

`urllib`: Biblioteca padrão do Python para manipulação de URLs.
`hubspot`: Biblioteca para integração com a API da HubSpot.
`hubspot.utils.oauth`: Contém as funções `get_auth_url` e a constante `AUTHORIZE_URL`.

## What is urllib

`urllib` is a package that collects several modules for working with URLs:

[urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) for opening and reading URLs

[urllib.error](https://docs.python.org/3/library/urllib.error.html#module-urllib.error) containing the exceptions raised by urllib.request

[urllib.parse](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse) for parsing URLs

[urllib.robotparser](https://docs.python.org/3/library/urllib.robotparser.html#module-urllib.robotparser) for parsing robots.txt files

## Uso

Para usar este projeto, execute o script principal teste `test_get_auth_url.py` e `test_signature.py`. Isso iniciará o processo de testes que verificam a correta geração e validação de assinaturas para diferentes versões e cenários.

```bash
python test_get_auth_url.py
python test_signature.py
```

O script `test_get_auth_url.py` e `test_signature.py` contém um teste simples para verificar a geração e validação de assinaturas.


## Contribuição

Contribuições para este projeto são bem-vindas. Se você encontrar um bug ou acha que algo pode ser melhorado, sinta-se à vontade para abrir uma issue ou um pull request.

Caso deseja contribuir com seus conhecimentos para o Projeto, siga os seguintes passos:

1. Faça um fork do projeto.
2. Crie um branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -m 'Adiciona nova feature').
4. Push para o branch (git push origin feature/nova-feature).
5. Abra um Pull Request.

Lembre-se de que este é apenas um exemplo e você pode precisar ajustá-lo de acordo com as necessidades específicas do seu projeto.