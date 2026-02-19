from pypdf import PdfReader

def extrair_texto_pdf(caminho_pdf):
    leitor = PdfReader(caminho_pdf)
    texto_completo = ""

    for pagina in leitor.pages:
        texto_completo += pagina.extract_text() + "\n"  # Adiciona uma nova linha entre as páginas

    return texto_completo

if __name__ == "__main__":
    caminho = "seu_arquivo_pdf.pdf"  # Substitua pelo caminho do seu arquivo PDF
    resultado = extrair_extrair_texto_pdf(caminho)
    print(resultado)