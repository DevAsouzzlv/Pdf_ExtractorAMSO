from pypdf import PdfReader

def extrair_texto_pdf(caminho_pdf, lista_paginas=None):
    leitor = PdfReader(caminho_pdf)
    texto_completo = ""
    
    # Se o usuário não passou páginas, vamos ler todas
    if lista_paginas is None:
        paginas_para_ler = range(len(leitor.pages))
    else:
        # Ajustamos para o índice do Python (subtraindo 1)
        paginas_para_ler = [p - 1 for p in lista_paginas]

    # Agora o loop só percorre os números que definimos acima
    for indice in paginas_para_ler:
        # Verificamos se a página existe no PDF para evitar erro
        if 0 <= indice < len(leitor.pages):
            texto_completo += f"--- Página {indice + 1} ---\n"
            texto_completo += leitor.pages[indice].extract_text() + "\n"
        else:
            print(f"Aviso: A página {indice + 1} não existe no arquivo.")

    return texto_completo

if __name__ == "__main__":
    caminho = "seu_arquivo.pdf"
    
    # Teste 1: Pegando apenas as páginas 1 e 2
    paginas_escolhidas = [1, 2] 
    
    resultado = extrair_texto_pdf(caminho, paginas_escolhidas)
    print(resultado)