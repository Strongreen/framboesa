# 🍓 Framboesa
**Interface gráfica (GUI) para o FFUF**

O **Framboesa** é uma interface gráfica (GUI) desenvolvida para facilitar o uso do FFUF (Fuzz Faster U Fool), uma ferramenta poderosa usada por pentesters, hackers éticos e especialistas forenses para descobrir diretórios, hosts virtuais e realizar fuzzing de parâmetros. 🎯

O objetivo deste projeto é tornar o FFUF mais acessível, permitindo que usuários configurem e executem a ferramenta sem a necessidade de utilizar a linha de comando, ideal para quem não está familiarizado com terminais. 🚀

## 📥 Pré-requisitos Windows

Para usar o Framboesa no Windows, você precisará instalar o FFUF e configurar o Go:

1. **Instale o Go:** [Download Go](https://golang.org/dl/)
   ```bash
   go version
   go install github.com/ffuf/ffuf/v2@latest
   ```

2. **Adicione o Go ao PATH (opcional):**
   Para garantir que você possa executar o FFUF de qualquer lugar no Prompt de Comando:

   - Vá até `Configurações do Sistema` > `Sistema` > `Configurações Avançadas do Sistema` > `Variáveis de Ambiente`.
   - Na seção `Variáveis de sistema`, encontre a variável `Path`, selecione-a e clique em `Editar`.
   - Adicione o caminho `C:\Users\<SeuUsuário>\go\bin` ao final da lista (substitua `<SeuUsuário>` pelo seu nome de usuário do Windows).
   - Clique em `OK` para salvar as alterações.

3. **Via terminal (PowerShell):**

   - Defina a variável GOPATH:
     ```powershell
     [System.Environment]::SetEnvironmentVariable('GOPATH', [System.IO.Path]::Combine($env:USERPROFILE, 'go'), [System.EnvironmentVariableTarget]::User)
     ```

   - Adicione GOPATH\bin ao PATH:
     ```powershell
     $env:Path += ";$env:GOPATH\bin"
     ```

   - Atualize a variável PATH permanentemente:
     ```powershell
     [System.Environment]::SetEnvironmentVariable('Path', $env:Path, [System.EnvironmentVariableTarget]::User)
     ```

4. **Verifique a instalação:**
   ```bash
   ffuf -h
   ```
## 📥 Pré-requisitos Linux

Para usar o Framboesa no Linux, você precisará instalar o FFUF e configurar o ambiente de desenvolvimento:

1. **Instale o Go e o FFUF:**

   Dependendo da sua distribuição Linux, você pode usar os seguintes comandos:

   - **Debian/Ubuntu:**
     ```bash
     sudo apt update
     sudo apt install golang-go
     go install github.com/ffuf/ffuf/v2@latest
     ```

   - **Fedora:**
     ```bash
     sudo dnf install golang
     go install github.com/ffuf/ffuf/v2@latest
     ```

   - **Arch Linux:**
     ```bash
     sudo pacman -S go
     go install github.com/ffuf/ffuf/v2@latest
     ```

2. **Configure o Go e adicione ao PATH:**

   Para garantir que você possa executar o FFUF de qualquer lugar no terminal, adicione o diretório `$GOPATH/bin` ao seu `PATH`.

   - Defina a variável GOPATH:
     ```bash
     echo 'export GOPATH=$HOME/go' >> ~/.bashrc
     source ~/.bashrc
     ```

   - Adicione `$GOPATH/bin` ao PATH:
     ```bash
     echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
     source ~/.bashrc
     ```

3. **Verifique a instalação:**

   Confirme que o FFUF foi instalado corretamente executando:

   ```bash
   ffuf -h
   ```

## ▶️ Execução

Após configurar tudo, você pode executar o Framboesa ( versão completa ) com:

```bash
python -m framboesa.main
```
Após configurar tudo, você pode executar o Framboesa ( versão simplificada ) com:

```bash
python simple/__init__.py
```
## 📝 Contribuições Futuras

- **Versão beta:** Trabalhando para criar uma versão que não exija a instalação de FFUF separada ou dependências adicionais 💡

## 🎨 Melhorias no projeto

Este foi criado e está aberto para a comunidade. Se você tiver sugestões de melhorias ou encontrar algum erro, sinta-se à vontade para contribuir! 🙌

---
