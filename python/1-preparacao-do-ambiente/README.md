# Instalação do Python no Windows

Este guia irá ajudá-lo a instalar o Python no sistema operacional Windows e verificar se o ambiente está configurado corretamente.

## 1. Baixar o Instalador do Python
1. Acesse o site oficial do Python: [https://www.python.org/](https://www.python.org/).

2. Na barra de navegação, clique em **"Downloads"**.

3. Clique no botão **"Download Python 3.X.X"**, onde "3.X.X" é a versão mais recente do Python que será baixada, pois o site detecta automaticamente o sistema operacional que está sendo utilizado e sugere o download da versão atualizada. 

## 2. Executar o Instalador
1. Após o download, abra o instalador. Certifique-se de marcar a opção **"Add Python to PATH"** para que o Python seja adicionado automaticamente ao PATH do sistema, isso irá facilitar o acesso utilizando linhas de comando.

2. Clique em **"Install Now"** para iniciar a instalação padrão. Caso queira personalizar a instalação, clique em "Customize Installation" e selecione as opções desejadas.

3. Aguarde enquanto o instalador baixa todos os arquivos e executa todas as configurações necessárias. Após a conclusão, clique em **"Close"** para fechar o instalador.

## 3. Verificar a Instalação
1. Abra o terminal (Command Prompt). Você pode fazer isso pressionando `Win + R`, digitando `cmd` e pressionando `Enter`.

2. No terminal, digite os comandos a seguir para verificar se a instalação do Python e do pip (gerenciador de pacotes do Python) foram concluídas com sucesso:

```sh
python --version
pip --version
```

1. Você deverá ver a versão do Python e do pip que foram instalados no sistema, por exemplo:

```sh
Python 3.10.4
pip 21.1.1
```