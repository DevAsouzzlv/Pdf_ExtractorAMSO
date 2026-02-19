# DocuMaster PDF Extractor 📄🚀

O **DocuMaster PDF Extractor** é uma ferramenta inteligente desenvolvida em Python para transformar arquivos PDF em texto puro (`.txt`). Ele utiliza processamento de texto avançado para garantir que o conteúdo seja extraído de forma organizada, eliminando quebras de linha desnecessárias.

## 🛠️ Funcionalidades
- **Extração Inteligente:** Uso de Regex para limpar o texto e manter a fluidez dos parágrafos.
- **Leitura Flexível:** Opção de extrair o arquivo completo ou apenas páginas específicas.
- **Exportação Automática:** Gera um arquivo `.txt` formatado na raiz do projeto.
- **Tratamento de Erros:** Identifica arquivos protegidos, inexistentes ou erros de digitação.

## 🔧 Tecnologias Utilizadas
- **Python 3**
- **pypdf** (Biblioteca para manipulação de PDFs)
- **Regex** (Para limpeza e formatação do texto)

## 📁 Estrutura do Projeto
- `src/extractor.py`: Código principal.
- `docs/`: Pasta para documentação e prints de evidência.
- `requirements.txt`: Lista de bibliotecas necessárias.
- `README.md`: Este manual de instruções.

## 🚀 Como Usar

1. **Prepare o arquivo:** Coloque o seu arquivo PDF na **raiz da pasta do projeto** (ao lado deste README).
   
2. **Execute o programa:**
   No terminal do VS Code, digite:
   ```powershell
   py src/extractor.py