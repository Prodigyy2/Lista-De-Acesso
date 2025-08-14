# **🚪 Sistema de Controle de Acesso por Idade**  

![Python](https://img.shields.io/badge/Python-3.x-%233776AB?logo=python&logoColor=white)  
![VS Code](https://img.shields.io/badge/Desenvolvido%20no-VS%20Code-%23007ACC?logo=visual-studio-code)  
![Terminal](https://img.shields.io/badge/Interface-Terminal-%234EAA25?logo=gnu-bash)  

Um programa Python simples para verificação de idade, desenvolvido como parte dos estudos em **Análise e Desenvolvimento de Sistemas na UNICSUL**.  

---

## **📋 Funcionalidades**  

✔ **Validação de idade** (acesso permitido apenas para maiores de 19 anos)  
✔ **Armazenamento em lista** (registro dos dados dos usuários autorizados)  
✔ **Relatório final** (lista de pessoas autorizadas e contagem total)  
✔ **Loop interativo** (permite cadastrar vários usuários até digitar -'sair'-)  

---

## **⚙️ Tecnologias Utilizadas**  

- **Python 3.x** (Linguagem principal)  
- **Terminal/Console** (Interface atual de execução)  
- **VS Code** (Ambiente de desenvolvimento)  
- **Estruturas de dados** (Listas e dicionários para armazenamento)  

---

## **▶️ Como Executar**  

1. **Certifique-se de ter Python instalado**  
   ```sh
   python --version
   ```
2. **Clone o repositório ou copie o código**  
3. **Execute no terminal:**  
   ```sh
   python controle_acesso.py
   ```
4. **Siga as instruções:**  
   - Digite o **nome** do usuário  
   - Digite a **idade**  
   - Para encerrar, digite **"sair"**  

---

## **📝 Exemplo de Uso**  

```plaintext
Digite seu nome! (ou "sair" para encerrar): João
Digite sua idade: 20
Pode entrar!

Digite seu nome! (ou "sair" para encerrar): Maria
Digite sua idade: 18
Entrada não autorizada!

Digite seu nome! (ou "sair" para encerrar): sair

--- Pessoas autorizadas (maiores de 19 anos) ---
Nome: João, Idade: 20 anos

Total de pessoas autorizadas: 1
```

---

## **🔧 Melhorias Futuras**  

✅ **Interface gráfica** (Tkinter, PySimpleGUI)  
✅ **Persistência de dados** (Salvar em JSON ou SQLite)  
✅ **Tratamento de erros** (Evitar crash se idade não for número)  
✅ **Versão web** (Flask, Django)  
✅ **Sistema de login** (Senha para acesso administrativo)  

---

## **🤝 Como Contribuir**  

🔹 **Reportar bugs** (Issues)  
🔹 **Sugerir melhorias** (Pull Requests)  
🔹 **Compartilhar ideias** (Discussions)  
