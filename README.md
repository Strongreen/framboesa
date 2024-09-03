# Carinhosamente apelidado de Framboesa
Interface grafica (GUI) para o FFUF


O intuito desse projeto é desenvolver uma interface gráfica (GUI) para o FFUF (Fuzz Faster U Fool), uma ferramenta popularmente conhecida, escrito em Go e que permite a descoberta de diretórios, descoberta de hosts virtuais (sem registros DNS) e fuzzing de parâmetros.

Este programa é útil para pentesters, hackers éticos e especialistas forenses. Também pode ser usado para testes de segurança.

O objetivo seria criar uma interface que permita aos usuários configurar e executar o FFUF sem precisar usar a linha de comando, tornando a ferramenta mais acessível, especialmente para quem não é tão familiar com terminal.


Ainda estou melhorando ele, pra não precisar instalar nada, mas de momento precisa ter o fuff instalado na maquina e algumas bibliotecas que o pyhton usa.


para usar o FFUF no windows:

primeiro instale o Go: https://golang.org/dl/

go version
go install github.com/ffuf/ffuf/v2@latest


Adicione o binário do Go ao PATH ( opicional )
Para garantir que você possa executar o FFUF de qualquer lugar no Prompt de Comando, adicione o diretório $GOPATH/bin ao seu PATH do sistema.

Vá até Configurações do Sistema > Sistema > Configurações Avançadas do Sistema > Variáveis de Ambiente.
Na seção Variáveis de sistema, encontre a variável Path, selecione-a e clique em Editar.
Adicione o caminho C:\Users\<SeuUsuário>\go\bin ao final da lista. (Substitua <SeuUsuário> pelo seu nome de usuário do Windows.)
Clique em OK para salvar as alterações.

Se tudo der certo: 

ffuf -h
