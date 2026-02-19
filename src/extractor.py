from pypdf import PdfReader
import re

def extrair_texto_pdf(caminho_pdf, lista_paginas=None):
    try:
        leitor = PdfReader(caminho_pdf)
        
        if leitor.is_encrypted:
            return "Erro: O arquivo PDF está protegido por senha."

        texto_completo = ""
        
        # Lógica de seleção de páginas restaurada
        if lista_paginas is None:
            paginas_para_ler = range(len(leitor.pages))
        else:
            # Converte para índice zero (página 1 vira 0)
            paginas_para_ler = [p - 1 for p in lista_paginas]

        for indice in paginas_para_ler:
            if 0 <= indice < len(leitor.pages):
                texto_completo += f"--- Página {indice + 1} ---\n"
                texto_extraido = leitor.pages[indice].extract_text()
                
                if texto_extraido:
                    # Limpeza inteligente: remove quebras de linha no meio de frases
                    # mas mantém onde há pontuação ou tópicos
                    texto_limpo = re.sub(r'(?<![.!?:●])\n', ' ', texto_extraido)
                    texto_limpo = re.sub(r' +', ' ', texto_limpo)
                    
                    texto_completo += texto_limpo.strip() + "\n\n"
            else:
                print(f"Aviso: A página {indice + 1} não existe.")

        # Geração do arquivo .txt
        nome_txt = caminho_pdf.replace(".pdf", "_extraido.txt")
        with open(nome_txt, "w", encoding="utf-8") as arquivo_txt:
            arquivo_txt.write(texto_completo)
        
        print(f"\n✅ Sucesso! Arquivo salvo como: {nome_txt}")
        return texto_completo

    except Exception as e:
        return f"Erro inesperado: {e}"

if __name__ == "__main__":
    print("--- DocuMaster PDF Extractor (Versão Full) ---")
    arquivo_usuario = input("Digite o nome do arquivo PDF (ex: teste.pdf): ")
    
    # Interface de escolha restaurada
    opcao = input("Deseja ler (1) Tudo ou (2) Páginas específicas? ")

    if opcao == "2":
        entrada_paginas = input("Digite as páginas separadas por vírgula (ex: 1,3): ")
        # Transforma "1,3" em [1, 3]
        lista = [int(p.strip()) for p in entrada_paginas.split(",")]
        resultado = extrair_texto_pdf(arquivo_usuario, lista)
    else:
        resultado = extrair_texto_pdf(arquivo_usuario)

    print("\n--- Conteúdo Extraído ---")
    print(resultado)