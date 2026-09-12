# Gerador de Código de Barras para Boletos

Uma ferramenta em Python que converte linhas digitáveis em códigos de barras ITF e gera um PDF pronto para impressão.

## O que o projeto faz

- Lê linhas digitáveis a partir de um arquivo de texto.
- Remove pontuação e normaliza os dados de entrada.
- Converte linhas digitáveis bancárias de 47 dígitos para o código de barras de 44 dígitos.
- Gera imagens no padrão ITF (Interleaved 2 of 5).
- Organiza os códigos em um único arquivo PDF.

## Tecnologias

- Python
- python-barcode
- ReportLab

## Como executar

1. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   ```

2. Instale as dependências:

   ```bash
   pip install "python-barcode[images]" reportlab
   ```

3. Preencha o arquivo `boletos.txt` com uma linha digitável por linha.

4. Execute o gerador:

   ```bash
   python gerar_codigos.py
   ```

Ao final, o arquivo `codigos_de_barras.pdf` será criado na raiz do projeto.

## Estrutura

| Arquivo | Responsabilidade |
| --- | --- |
| `gerar_codigos.py` | Conversão, geração das imagens e montagem do PDF |
| `boletos.txt` | Entrada: uma linha digitável por linha |
| `codigos_de_barras.pdf` | Exemplo de saída gerada |

## Como a conversão funciona

Para linhas digitáveis com 47 dígitos, o script reorganiza os campos para chegar aos 44 dígitos do código de barras. Entradas que já estejam no formato de 44 dígitos são preservadas após a limpeza.

## Limitações e cuidados

- O projeto é um utilitário de estudo e não substitui a validação oficial de bancos ou sistemas de pagamento.
- Use somente dados de teste ou dados que você tenha autorização para processar.
- Antes de qualquer uso operacional, valide os códigos gerados com o ambiente responsável.

## Aprendizados

- Transformação e validação de dados textuais.
- Geração de códigos de barras e documentos PDF.
- Organização de um fluxo simples de entrada, processamento e saída.
