# 🍓 Framboesa
**Interface gráfica (GUI) para o FFUF**

O **Framboesa** é uma interface gráfica (GUI) desenvolvida para facilitar o uso do FFUF (Fuzz Faster U Fool), uma ferramenta poderosa usada por pentesters, hackers éticos e especialistas forenses para descobrir diretórios, hosts virtuais e realizar fuzzing de parâmetros. 🎯

O objetivo deste projeto é tornar o FFUF mais acessível, permitindo que usuários configurem e executem a ferramenta sem a necessidade de utilizar a linha de comando, ideal para quem não está familiarizado com terminais. 🚀

## 📥 Pré-requisitos

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

## 🛠️ Construção do Executável

Para transformar o Framboesa em um executável `.exe`:

```bash
pyinstaller --onefile --windowed --name Framboesa --distpath=. --icon=icon/framboesa.ico framboesa/main.py
```
*(Observação: Tem um erro de módulo, como `ModuleNotFoundError: No module named 'src'` que precisa ser resolvidos.)*

## ▶️ Execução

Após configurar tudo, você pode executar o Framboesa com:

```bash
python -m framboesa.main
```

## 📝 Contribuições Futuras

- **Versão beta:** Trabalhando para criar uma versão que não exija a instalação de FFUF separada ou dependências adicionais 💡

## 🎨 Melhorias no projeto

Este foi criado e está aberto para a comunidade. Se você tiver sugestões de melhorias ou encontrar algum erro, sinta-se à vontade para contribuir! 🙌

---
