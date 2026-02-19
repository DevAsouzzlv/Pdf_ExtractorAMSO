from pypdf import PdfReader
import re
import os
import platform

def limpar_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def exibir_banner():
    limpar_terminal()
    print("=" * 50)
    print("       DOCUMASTER PDF EXTRACTOR v1.2.0 📄🚀")
    print("=" * 50)
    print()

def extrair_texto_pdf(caminho_pdf, lista_paginas=None):
    try:
        leitor = PdfReader(caminho_pdf)
        total_paginas = len(leitor.pages)
        
        texto_completo = ""
        
        # Define quais páginas serão lidas
        if lista_paginas is None:
            paginas_para_ler = range(total_paginas)
        else:
            # Filtra apenas páginas que existem para evitar erro de índice
            paginas_para_ler = [p - 1 for p in lista_paginas if 0 < p <= total_paginas]

        for indice in paginas_para_ler:
            texto_extraido = leitor.pages[indice].extract_text()
            if texto_extraido:
                # Limpeza Regex
                texto_limpo = re.sub(r'(?<![.!?:●])\n', ' ', texto_extraido)
                texto_limpo = re.sub(r' +', ' ', texto_limpo)
                texto_completo += f"--- Página {indice + 1} ---\n{texto_limpo.strip()}\n\n"
        
        return texto_completo, total_paginas

    except Exception as e:
        return f"❌ Erro: {e}", 0

if __name__ == "__main__":
    exibir_banner()
    arquivo_usuario = input("📂 Digite o nome do arquivo PDF: ").strip()
    
    if not os.path.exists(arquivo_usuario):
        print(f"❌ Erro: O arquivo '{arquivo_usuario}' não foi encontrado.")
    else:
        # Primeiro, pegamos o total de páginas para informar o usuário
        leitor_temp = PdfReader(arquivo_usuario)
        total_de_paginas = len(leitor_temp.pages)
        
        exibir_banner()
        print(f"📄 Arquivo: {arquivo_usuario}")
        print(f"📊 Total de páginas: {total_de_paginas}")
        print("-" * 30)
        print("Escolha uma opção:")
        print("(1) Extrair Tudo")
        print("(2) Escolher páginas específicas")
        opcao = input("\n👉 Opção: ")

        resultado = ""
        if opcao == "2":
            entrada = input(f"🔢 Digite as páginas entre 1 e {total_de_paginas} (ex: 1,3): ")
            lista = [int(p.strip()) for p in entrada.split(",")]
            resultado, _ = extrair_texto_pdf(arquivo_usuario, lista)
        else:
            resultado, _ = extrair_texto_pdf(arquivo_usuario)

        # Exibe o resultado no terminal
        exibir_banner()
        print("--- 📝 CONTEÚDO EXTRAÍDO ---")
        print(resultado)
        print("-" * 50)

        # Pergunta se deseja salvar o .txt
        decisao = input("\n💾 Deseja salvar este conteúdo em um arquivo .txt? (s/n): ").lower()

        if decisao == 's':
            nome_txt = arquivo_usuario.replace(".pdf", "_extraido.txt")
            with open(nome_txt, "w", encoding="utf-8") as f:
                f.write(resultado)
            print(f"✨ Sucesso! Arquivo '{nome_txt}' gerado.")
        else:
            print("🚫 O arquivo .txt não foi criado.")

    input("\n🏁 Pressione Enter para fechar...")