from pypdf import PdfReader
import re

def extrair_dados(texto_extraido):
    texto_formatado = texto_extraido
    # Inicializa um dicionário para armazenar os dados extraídos
    dados = {}
    
    # Define regex patterns para os termos chave e seus valores
    padroes = {
        "PLACA": r"PLACA\s+([^\n]+)",
        "MARCA": r"MARCA\s+([^\n]+)",
        "ESPÉCIE": r"ESPÉCIE\s+([^\n]+)",
        "NOME DO PROPRIETÁRIO": r"NOME DO PROPRIETÁRIO\s+([^\n]+)",
        "INFRAÇÃO": r"INFRAÇÃO\s+([^\n]+)",
        "LOCAL": r"LOCAL\s+([^\n]+)",
        "DATA DA INFRAÇÃO": r"DATA DA INFRAÇÃO\s+(\d{2}/\d{2}/\d{4})",
        "HORA": r"HORA\s+([^\n]+)",
        "DATA DA EMISSÃO": r"DATA DA EMISSÃO\s+(\d{2}/\d{2}/\d{4})",
        "VELOCIDADE REGULAMENTADA": r"VELOCIDADE REGULAMENTADA\s+KM/H(\d+)",
        "VELOCIDADE MEDIDA": r"VELOCIDADE MEDIDA\s+KM/H(\d+)",
        "VELOCIDADE CONSIDERADA": r"VELOCIDADE CONSIDERADA\s+KM/H(\d+)",
        "ENQUADRAMENTO": r"ENQUADRAMENTO\s+([^\n]+)",
        "ARTIGO DO CTB": r"ARTIGO DO CTB\s+([^\n]+)",
        "NATUREZA": r"NATUREZA\s+([^\n]+)",
        "PONTUAÇÃO": r"PONTUAÇÃO\s+([^\n]+)",
        "Nº AIT": r"Nº AIT\s+([^\n]+)",
        "DATA LIMITE IND. CONDUTOR / DEFESA AUTUAÇÃO": r"DATA LIMITE IND. CONDUTOR / DEFESA AUTUAÇÃO\s+([^\n]+)",
        "NRO. INFRAEST": r"NRO. INFRAEST\s+([^\n]+)",
        "IDENTIFICAÇÃO DO EQUIPAMENTO": r"IDENTIFICAÇÃO DO EQUIPAMENTO\s+([^\n]+)",
        "AFERIÇÃO / CERTIFICAÇÃO": r"AFERIÇÃO / CERTIFICAÇÃO\s+([^\n]+)",
        "AGENTE DE TRÂNSITO": r"AGENTE DE TRÂNSITO\s+(\d+)"
    }
    
    # Para cada padrão, encontra e armazena o valor correspondente no dicionário
    for chave, padrao in padroes.items():
        match = re.search(padrao, texto_formatado)
        if match:
            dados[chave] = match.group(1).strip()

    return dados