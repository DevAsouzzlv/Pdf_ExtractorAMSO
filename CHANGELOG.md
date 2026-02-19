# Histórico de Alterações (Changelog) 📜

## [1.2.0] - 2024-05-24
### Adicionado
- **Contagem de Páginas:** O sistema agora detecta e exibe o total de páginas do PDF antes do processamento.
- **Visualização Prévia (Preview):** O texto extraído é exibido diretamente no terminal para conferência imediata.
- **Salvamento Opcional:** Implementada lógica de decisão (s/n) para que o usuário escolha se deseja gerar o arquivo `.txt`.
- **UX Adaptativa:** Função de limpeza de terminal compatível com Windows (cls) e Linux/Mac (clear).

### Melhores Práticas
- **Ajuste de Índices:** Tratamento lógico para alinhar a contagem humana (página 1) com o índice do sistema (0).
- **Estilização CLI:** Adicionado banner de boas-vindas para melhor identidade visual da aplicação.

## [1.1.0] - 2024-05-23
### Adicionado
- **Limpeza com Regex:** Implementação de Expressões Regulares para remover quebras de linha indevidas e melhorar a fluidez do texto.
- **Exportação Automática:** O sistema agora gera um arquivo `.txt` automaticamente após a extração.
- **Interface Interativa:** Menu CLI para o usuário escolher entre leitura total ou parcial via teclado.
- **Estrutura Profissional:** Organização das pastas `src/` e `docs/`.

### Removido
- Scripts de teste obsoletos e redundantes da raiz do projeto.

## [1.0.0] - 2024-05-22
### Adicionado
- Função de extração completa de texto de PDFs.
- Filtro para extração de páginas específicas.
- Tratamento de erro para arquivos inexistentes.
- Verificação de segurança para PDFs criptografados.