from pypdf import PdfReader  # Importa a biblioteca para ler arquivos PDF
import re                    # Importa Expressões Regulares para limpeza de texto
import os                    # Importa funções do sistema (manipulação de arquivos/pastas)
import platform              # Importa para identificar se é Windows, Linux ou Mac
import sys                   # Importa para comandos de encerramento do script

def limpar_terminal():
    """Verifica o Sistema Operacional e limpa a tela do terminal."""
    if platform.system() == "Windows":
        os.system('cls')     # Comando para Windows
    else:
        os.system('clear')   # Comando para Linux/Mac

def exibir_banner():
    """Exibe o cabeçalho visual do programa."""
    limpar_terminal()
    print("=" * 50)
    print("       DOCUMASTER PDF EXTRACTOR v1.3.0 📄🚀")
    print("=" * 50)
    print()

def extrair_texto_pdf(caminho_pdf, lista_paginas=None, senha=None):
    """Função principal para extrair texto, lidando com páginas e senhas."""
    try:
        # Abre o arquivo PDF
        leitor = PdfReader(caminho_pdf)
        
        # Se o PDF estiver criptografado, usa a senha fornecida
        if leitor.is_encrypted and senha:
            leitor.decrypt(senha)
            
        total_paginas = len(leitor.pages) # Conta o total de páginas
        texto_completo = ""               # Variável que vai guardar todo o texto
        
        # Define se lê o PDF todo ou apenas páginas escolhidas
        if lista_paginas is None:
            paginas_para_ler = range(total_paginas) # range cria sequência de 0 até o total
        else:
            # Converte a página humana (1) para índice de computador (0)
            paginas_para_ler = [p - 1 for p in lista_paginas if 0 < p <= total_paginas]

        # Loop que percorre cada página selecionada
        for indice in paginas_para_ler:
            texto_extraido = leitor.pages[indice].extract_text() # Puxa o texto bruto
            if texto_extraido:
                # REGEX: Remove quebras de linha que não são final de frase
                texto_limpo = re.sub(r'(?<![.!?:●])\n', ' ', texto_extraido)
                # REGEX: Substitui espaços múltiplos por um único espaço
                texto_limpo = re.sub(r' +', ' ', texto_limpo)
                # Acumula o texto formatado na variável
                texto_completo += f"--- Página {indice + 1} ---\n{texto_limpo.strip()}\n\n"
        
        return texto_completo, total_paginas # Retorna o texto e o número de páginas

    except Exception as e:
        # Em caso de erro (como senha errada ou arquivo corrompido)
        return f"❌ Erro na extração: {e}", 0

# Início do programa
if __name__ == "__main__":
    exibir_banner()
    # Pede o nome do arquivo e remove espaços extras com .strip()
    arquivo_usuario = input("📂 Digite o nome do arquivo PDF: ").strip()
    
    # Verifica se o arquivo realmente existe na pasta
    if not os.path.exists(arquivo_usuario):
        print(f"❌ Erro: O arquivo '{arquivo_usuario}' não foi encontrado.")
    else:
        try:
            # Cria um leitor temporário para verificar metadados
            leitor_temp = PdfReader(arquivo_usuario)
            senha_atual = None # Variável para guardar a senha se houver
            
            # BLOCO DE SEGURANÇA: Verifica se o PDF tem cadeado
            if leitor_temp.is_encrypted:
                print(f"🔐 O arquivo '{arquivo_usuario}' está protegido.")
                senha_atual = input("🔑 Digite a senha para abrir o PDF: ")
                
                # Tenta abrir o "cadeado"
                status_senha = leitor_temp.decrypt(senha_atual)
                
                if status_senha == 0: # 0 significa falha (senha incorreta)
                    print("❌ Senha incorreta! Acesso negado.")
                    input("\nPressione Enter para sair...")
                    sys.exit() # Fecha o programa
                else:
                    print("✅ Arquivo desbloqueado com sucesso!")

            # Após passar pela segurança, conta as páginas
            total_de_paginas = len(leitor_temp.pages)
            
            # Mostra o menu de opções
            exibir_banner()
            print(f"📄 Arquivo: {arquivo_usuario}")
            print(f"📊 Total de páginas: {total_de_paginas}")
            print("-" * 30)
            print("Escolha uma opção:")
            print("(1) Extrair Tudo")
            print("(2) Escolher páginas específicas")
            opcao = input("\n👉 Opção: ")

            resultado = ""
            # Lógica para escolha de páginas específicas
            if opcao == "2":
                entrada = input(f"🔢 Digite as páginas entre 1 e {total_de_paginas} (ex: 1,3): ")
                # Converte a string "1,3" em uma lista de números [1, 3]
                lista = [int(p.strip()) for p in entrada.split(",")]
                # Chama a função passando a lista e a senha
                resultado, _ = extrair_texto_pdf(arquivo_usuario, lista, senha=senha_atual)
            else:
                # Chama a função para o PDF todo passando a senha
                resultado, _ = extrair_texto_pdf(arquivo_usuario, senha=senha_atual)

            # Exibe o texto extraído no terminal (Preview)
            exibir_banner()
            print("--- 📝 CONTEÚDO EXTRAÍDO ---")
            print(resultado)
            print("-" * 50)

            # Pergunta se o usuário quer salvar o resultado em disco
            decisao = input("\n💾 Deseja salvar este conteúdo em um arquivo .txt? (s/n): ").lower()
            if decisao == 's':
                # Cria o nome do arquivo TXT baseado no nome do PDF
                nome_txt = arquivo_usuario.replace(".pdf", "_extraido.txt")
                # Abre o arquivo para escrita ('w') com codificação UTF-8
                with open(nome_txt, "w", encoding="utf-8") as f:
                    f.write(resultado)
                print(f"✨ Sucesso! Arquivo '{nome_txt}' gerado.")
            else:
                print("🚫 Operação finalizada sem salvar arquivo.")

        except Exception as e:
            # Captura qualquer erro inesperado para o programa não fechar bruscamente
            print(f"❌ Ocorreu um erro inesperado: {e}")

    # Pausa o terminal para o usuário ler o resultado final
    input("\n🏁 Pressione Enter para fechar...")