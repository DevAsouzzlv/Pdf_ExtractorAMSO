from pypdf import PdfReader

def extrair_texto_pdf(caminho_pdf, lista_paginas=None):
    try:
        # Tentamos abrir o arquivo
        leitor = PdfReader(caminho_pdf)
        
        # Requisito 3: Verificar se o PDF está criptografado (com senha)
        if leitor.is_encrypted:
            return "Erro: O arquivo PDF está protegido por senha e não pode ser lido."

        texto_completo = ""
        
        if lista_paginas is None:
            paginas_para_ler = range(len(leitor.pages))
        else:
            paginas_para_ler = [p - 1 for p in lista_paginas]

        for indice in paginas_para_ler:
            if 0 <= indice < len(leitor.pages):
                texto_completo += f"--- Página {indice + 1} ---\n"
                texto_completo += leitor.pages[indice].extract_text() + "\n"
            else:
                print(f"Aviso: A página {indice + 1} não existe no arquivo.")

        return texto_completo

    except FileNotFoundError:
        # Requisito 3: Tratamento de arquivo inexistente
        return "Erro: O arquivo não foi encontrado. Verifique o caminho digitado."
    except Exception as e:
        # Captura qualquer outro erro inesperado
        return f"Erro inesperado ao ler o PDF: {e}"
    
if __name__ == "__main__":
    # --- TESTE 1: Arquivo que existe ---
    print("--- Teste 1: Arquivo Real ---")
    caminho_real = "seu_arquivo.pdf" # Coloque um nome de arquivo que existe
    print(extrair_texto_pdf(caminho_real, [1]))

    # --- TESTE 2: Arquivo que NÃO existe (Requisito 3) ---
    print("\n--- Teste 2: Arquivo Inexistente ---")
    caminho_fantasma = "arquivo_que_nao_existe.pdf"
    print(extrair_texto_pdf(caminho_fantasma))

    # --- TESTE 3: Página fora do intervalo (Requisito 3) ---
    print("\n--- Teste 3: Página Inexistente ---")
    print(extrair_texto_pdf(caminho_real, [999]))