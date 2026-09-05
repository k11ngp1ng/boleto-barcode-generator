import os
from barcode import ITF
from barcode.writer import ImageWriter
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def linha_digitable_para_codigo_barras(linha):
    """
    Remove pontuação e converte linha digitável bancária (47 dígitos) 
    para a representação de 44 dígitos do código de barras ITF (Interleaved 2 of 5).
    """
    limpo = ''.join(filter(str.isdigit, linha))
    
    # Se for linha digitável padrão de boleto bancário (47 dígitos)
    if len(limpo) == 47:
        # Extrai os blocos do código de barras de 44 dígitos
        banco_moeda = limpo[0:4]
        dv_geral = limpo[32]
        fator_valor = limpo[33:47]
        campo1 = limpo[4:9]
        campo2 = limpo[10:20]
        campo3 = limpo[21:31]
        
        # Junta na estrutura original do código de barras de 44 dígitos
        return f"{banco_moeda}{dv_geral}{fator_valor}{campo1}{campo2}{campo3}"
    
    # Se já for o código de barras direto (44 dígitos) ou outro formato
    return limpo

def gerar_pdf_boletos(txt_entrada="boletos.txt", pdf_saida="codigos_de_barras.pdf"):
    if not os.path.exists(txt_entrada):
        print(f"Erro: O arquivo '{txt_entrada}' não foi encontrado.")
        return

    doc = SimpleDocTemplate(pdf_saida, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []
    styles = getSampleStyleSheet()
    
    estilo_titulo = ParagraphStyle('Titulo', parent=styles['Heading2'], spaceAfter=6)
    estilo_texto = ParagraphStyle('Texto', parent=styles['Normal'], spaceAfter=15, fontSize=9)

    pasta_temp = "temp_barcodes"
    os.makedirs(pasta_temp, exist_ok=True)

    with open(txt_entrada, 'r') as f:
        linhas = [l.strip() for l in f.readlines() if l.strip()]

    for i, linha in enumerate(linhas, 1):
        codigo_44 = linha_digitable_para_codigo_barras(linha)
        
        # Gera a imagem do código de barras no formato ITF
        caminho_img_base = os.path.join(pasta_temp, f"barcode_{i}")
        itf = ITF(codigo_44, writer=ImageWriter())
        caminho_img = itf.save(caminho_img_base, options={
            'module_height': 15.0,
            'module_width': 0.2,
            'quiet_zone': 2.0,
            'write_text': False
        })

        # Adiciona os elementos no PDF
        story.append(Paragraph(f"<b>Boleto #{i}</b>", estilo_titulo))
        story.append(RLImage(caminho_img, width=400, height=50))
        story.append(Paragraph(f"Linha Digitável: {linha}", estilo_texto))
        story.append(Spacer(1, 15))

    doc.build(story)
    
    # Limpa imagens temporárias
    for arquivo in os.listdir(pasta_temp):
        os.remove(os.path.join(pasta_temp, arquivo))
    os.rmdir(pasta_temp)

    print(f"Sucesso! PDF gerado em: {pdf_saida}")

if __name__ == "__main__":
    gerar_pdf_boletos()