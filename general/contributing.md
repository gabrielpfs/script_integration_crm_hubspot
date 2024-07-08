# Contributing on Github Projects

# Passos para Clonar um Repositório do GitHub

## Instale o Git (se ainda não o tiver instalado):

- Para Windows: Baixe e instale o Git a partir do site oficial do Git.
- Para Mac: Use o Homebrew (brew install git) ou baixe o instalador do site oficial do Git.
- Para Linux: Use o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu, execute:

```
sudo apt-get install git
```

## Abra o Terminal:

- No Windows, você pode usar o Git Bash (instalado junto com o Git) ou o Prompt de Comando.
- No Mac ou Linux, abra o Terminal.

## Navegue até o Diretório de Destino:

Vá para o diretório onde você deseja clonar o repositório. Use o comando cd para mudar de diretório. Por exemplo:

```
cd /path/to/your/directory
```

## Clonar o Repositório:

Use o comando git clone seguido pelo URL do repositório. Por exemplo, para clonar um repositório chamado integration-crm-hubspot-contacts do GitHub, use:

```
git clone https://github.com/Vinteum-Software/integration-crm-hubspot-contacts.git
```

## Verifique se o Repositório foi Clonado:

Depois que o clone estiver completo, você verá uma nova pasta com o nome do repositório no diretório de destino. Navegue até essa pasta para começar a trabalhar com o projeto:

```
cd integration-crm-hubspot-contacts
```

# Passos para Mudar a Visibilidade de um Repositório no GitHub

## Acesse o GitHub:

- Faça login na sua conta GitHub no site do GitHub.

## Navegue até o Repositório:

- Vá até a página do repositório que você deseja tornar público.

## Acesse as Configurações do Repositório:

- Na página do repositório, clique na aba Settings, que está no menu superior à direita.

## Alterar a Visibilidade:

- Role a página de configurações para baixo até encontrar a seção Danger Zone.
- Na seção Danger Zone, você verá a opção Change repository visibility.
- Clique no botão Change visibility.

## Confirme a Alteração:

- Uma janela pop-up aparecerá solicitando que você confirme a alteração de visibilidade.
- Selecione a opção Make public e, em seguida, clique no botão I understand, make this repository public.

## Confirme com sua Senha:

- Você pode ser solicitado a inserir sua senha do GitHub para confirmar a alteração.


## Clone o Repositório Existente:

Primeiro, clone o repositório existente da primeira conta do GitHub para o seu computador local usando o comando:

```
git clone <url_do_repositório>
```

## Ajuste o Remote do Git:

Navegue para o diretório do seu projeto clonado e ajuste o URL do remote para apontar para a nova conta do GitHub usando o comando:

```
git remote set-url origin <novo_url_do_repositório>
```

Substitua <novo_url_do_repositório> pelo URL do novo repositório que você criou na outra conta do GitHub.

## Push para o Novo Repositório:

Por fim, faça o push das suas alterações para o novo repositório usando o comando:

```
git push -u origin master
```

Isso vai enviar todos os commits e arquivos do seu repositório local para o novo repositório na outra conta do GitHub.

## Verifique o Diretório Git:

Certifique-se de estar no diretório correto do projeto que foi clonado do GitHub. Você precisa estar dentro do diretório que contém o subdiretório .git. Normalmente, ao clonar um repositório, o Git cria um diretório oculto .git dentro do diretório clonado.

Você pode verificar se está no diretório certo usando o comando:

```
ls -a
```

Isso mostrará todos os arquivos e diretórios, incluindo os ocultos, como .git.

## Inicialize o Repositório Git:

Se o diretório atual não for um repositório Git, você precisará inicializá-lo como tal. Se estiver no diretório correto que contém o código do projeto, mas não há um repositório Git ainda, você pode inicializá-lo com o comando:

```
git init
```

Isso criará um novo repositório Git local no diretório atual.

## Reverifique o Comando:

Após verificar que está no diretório certo e que é um repositório Git válido, tente novamente configurar o remote com o comando:

```
git remote set-url origin <novo_url_do_repositório>
```

Certifique-se de substituir <novo_url_do_repositório> pelo URL correto do novo repositório que você deseja usar.

## Push para o Novo Repositório:

Você precisa fazer o push dos seus commits locais para o novo repositório remoto na outra conta do GitHub. Para fazer isso, use o comando:

```
git push -u origin main
```

O -u configura o upstream para a branch main, o que significa que nas próximas vezes que você fizer git push, não precisará especificar o branch e apenas git push será suficiente.

origin é o nome do remote que você configurou anteriormente para apontar para o novo repositório na sua outra conta do GitHub.

main é o nome da branch local que você está empurrando para o repositório remoto. Se sua branch principal for diferente (por exemplo, master), substitua main pelo nome correto.

# Removing a Repository

Para remover um repositório Git remoto (como origin neste caso), você pode usar o comando git remote remove seguido pelo nome do remote que você deseja remover. Aqui está como fazer:

```
git remote remove origin
```

Isso remove o remote chamado origin do seu repositório Git local. Depois de executar este comando, o Git não terá mais o remote origin configurado para este repositório.

Lembre-se de que isso apenas remove a referência ao remote do seu repositório local. O repositório remoto no GitHub ou em qualquer outro servidor Git não será afetado por esta ação.

Se você já possui um repositório local com histórico de commits e deseja publicá-lo em um novo repositório no GitHub, siga estes passos para adicionar o novo repositório remoto e fazer o push dos seus arquivos:

## Adicionar o Novo Remote:

Primeiro, adicione o novo remote chamado origin apontando para o URL do novo repositório no GitHub usando o comando:

```
git remote add origin https://github.com/Vinteum-Software/integration-crm-hubspot-contacts.git
```

Substitua https://github.com/Vinteum-Software/integration-crm-hubspot-contacts.git pelo URL correto do seu novo repositório.


## Fazer o Push dos Arquivos:

Depois de adicionar o remote, você pode fazer o push dos seus arquivos e commits locais para o novo repositório usando o comando:


```
git push -u origin main
```

- -u configura o upstream para a branch main, o que significa que nas próximas vezes que você fizer git push, não precisará especificar o branch e apenas git push será suficiente.
- origin é o nome do remote que você acabou de adicionar.
- main é o nome da branch local que você está empurrando para o repositório remoto. Substitua main pelo nome correto da sua branch principal, se for diferente.

Se você deseja usar um novo repositório no GitHub e origin já está configurado para outro URL, você tem algumas opções:

## Opção 1: Renomear o Remote Existente

Se você deseja mudar o remote atual origin para apontar para um novo URL, você pode usar o comando git remote set-url:

```
git remote set-url origin https://github.com/Vinteum-Software/integration-crm-hubspot-contacts.git
```

Isso atualiza o URL do remote origin para apontar para o novo repositório no GitHub.

## Opção 2: Remover o Remote Existente e Adicionar Novamente

Se você deseja remover o remote origin existente e adicionar um novo, você pode fazer da seguinte maneira:

- Remova o remote origin atual:

```
git remote remove origin
```

- Em seguida, adicione o novo remote com o mesmo comando que você tentou originalmente:

```
git remote add origin https://github.com/Vinteum-Software/integration-crm-hubspot-contacts.git
```

- Agora você pode fazer o push dos seus arquivos para o novo repositório:

```
git push -u origin main
```

Certifique-se de ajustar main para o nome correto da sua branch principal se ela for diferente.

## Opção 3: Configurar um Novo Remote com Outro Nome

Se preferir manter o remote origin existente e configurar um novo remote com outro nome (por exemplo, new-origin), você pode fazer assim:

- Adicione um novo remote com um nome diferente (por exemplo, new-origin):

```
git remote add new-origin https://github.com/Vinteum-Software/integration-crm-hubspot-contacts.git
```

- Faça o push dos seus arquivos para o novo remote new-origin:

```
git push -u new-origin main
```

Escolha a opção que melhor se adequa ao que você precisa fazer com seu repositório Git local e ao novo repositório no GitHub.