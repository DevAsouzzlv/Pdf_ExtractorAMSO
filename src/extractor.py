from pypdf import PdfReader
import re
import os
import platform
import sys

def limpar_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def exibir_banner():
    limpar_terminal()
    print("=" * 50)
    print("       DOCUMASTER PDF EXTRACTOR v1.1.0 📄🚀")
    print("=" * 50)
    print()

def extrair_texto_pdf(caminho_pdf, lista_paginas=None):
    try:
        if not os.path.exists(caminho_pdf):
            return f"❌ Erro: O arquivo '{caminho_pdf}' não foi encontrado na pasta."

        leitor = PdfReader(caminho_pdf)
        
        if leitor.is_encrypted:
            return "❌ Erro: O arquivo PDF está protegido por senha."

        texto_completo = ""
        paginas_para_ler = range(len(leitor.pages)) if lista_paginas is None else [p - 1 for p in lista_paginas]

        for indice in paginas_para_ler:
            if 0 <= indice < len(leitor.pages):
                texto_extraido = leitor.pages[indice].extract_text()
                if texto_extraido:
                    texto_limpo = re.sub(r'(?<![.!?:●])\n', ' ', texto_extraido)
                    texto_limpo = re.sub(r' +', ' ', texto_limpo)
                    texto_completo += f"--- Página {indice + 1} ---\n{texto_limpo.strip()}\n\n"
            else:
                print(f"⚠️ Aviso: A página {indice + 1} não existe.")

        nome_txt = caminho_pdf.replace(".pdf", "_extraido.txt")
        with open(nome_txt, "w", encoding="utf-8") as f:
            f.write(texto_completo)
        
        return texto_completo

    except Exception as e:
        return f"❌ Erro na extração: {e}"

if __name__ == "__main__":
    try:
        exibir_banner()
        arquivo_usuario = input("📂 Digite o nome do arquivo PDF (ex: teste.pdf): ").strip()
        
        if not arquivo_usuario:
            print("Você não digitou o nome do arquivo!")
            sys.exit()

        print("\nEscolha uma opção:")
        print("(1) Extrair Tudo")
        print("(2) Páginas específicas")
        opcao = input("\n👉 Opção: ")

        if opcao == "2":
            entrada = input("\n🔢 Digite as páginas (ex: 1,3): ")
            lista = [int(p.strip()) for p in entrada.split(",")]
            resultado = extrair_texto_pdf(arquivo_usuario, lista)
        else:
            resultado = extrair_texto_pdf(arquivo_usuario)

        # Só limpa para mostrar o resultado se não for erro
        if "Erro" not in resultado:
            input("\n✅ Processo concluído! Pressione Enter para ver o texto...")
            exibir_banner()
            print(resultado)
        else:
            print("\n" + resultado)
            
        input("\n🏁 Fim do programa. Pressione Enter para fechar...")

    except KeyboardInterrupt:
        print("\n\nPrograma encerrado pelo usuário.")
    except Exception as e:
        print(f"\nERRO CRÍTICO NO SISTEMA: {e}")
        input("\nPressione Enter para sair...")