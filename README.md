# 📄🚀 DocuMaster PDF Extractor

O **DocuMaster PDF Extractor** é uma solução robusta em Python desenvolvida para converter documentos PDF em arquivos de texto (`.txt`) de forma inteligente.

Diferente de extratores simples, esta ferramenta utiliza **Expressões Regulares (Regex)** para tratar quebras de linha indevidas, garantindo que o texto final seja fluido e altamente legível.

---

## 🌟 Diferenciais da Versão v1.1.0

- 🧠 **Processamento Inteligente:**  
  Algoritmo que identifica o fim real de parágrafos, evitando frases "picotadas" comuns na extração de PDFs.

- ⚙️ **Automação de Saída:**  
  Criação automática de um arquivo de texto formatado com o sufixo `_extraido.txt`.

- 💻 **Interface CLI Interativa:**  
  Menu dinâmico que permite ao usuário filtrar páginas ou processar o documento completo.

---

## 🛠️ Funcionalidades

- 📄 **Extração Inteligente:**  
  Uso de Regex para manter a fluidez dos parágrafos e remover espaços indesejados.

- 🎯 **Modo Seletivo:**  
  Opção de extrair o arquivo completo ou apenas páginas específicas (ex: 1, 3, 5).

- ⚠️ **Tratamento de Erros:**  
  Validação para:
  - Arquivos protegidos por senha  
  - Arquivos não encontrados  
  - Entradas de página inválidas  

- 💾 **Exportação Automática:**  
  Salvamento em `.txt` com codificação UTF-8.

---

## 🔧 Tecnologias Utilizadas

- 🐍 Python 3.10+
- 📚 `pypdf` — Manipulação e leitura de PDFs
- 🔍 `re (Regex)` — Processamento e limpeza de texto

---

## 📁 Estrutura do Projeto

```text
PDF_EXTRACTOR/
├── docs/               # Documentação e evidências
├── src/
│   └── extractor.py    # Código principal
├── requirements.txt    # Dependências do projeto
├── README.md           # Guia do projeto
└── arquivo.pdf         # PDF de entrada

```

## 🚀 Como Usar

### Preparação
Coloque o arquivo PDF que deseja converter na raiz do projeto (mesma pasta do `README.md`).

### Instalação das Dependências

```bash
pip install -r requirements.txt

```
### Execução

```bash
python src/extractor.py

```
### Resultado

O arquivo extraído será gerado automaticamente com o nome:

```text
nome_do_arquivo_extraido.txt
