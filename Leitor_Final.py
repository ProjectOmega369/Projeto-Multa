import re
import ExtrairDados

def main():
    
    termos_chave = [
        {"nome": "nome_pessoa", "pesquisar": "NOME DO PROPRIETÁRIO"},
        {"nome": "placa_veiculo", "pesquisar": "PLACA"},
        {"nome": "marca_veiculo", "pesquisar": "MARCA"},
        {"nome": "especie", "pesquisar": "ESPÉCIE"},
        {"nome": "infracao", "pesquisar": "INFRAÇÃO"},
        {"nome": "endereco_infracao", "pesquisar": "LOCAL"},
        {"nome": "data_infracao", "pesquisar": "DATA DA INFRAÇÃO"},
        {"nome": "hora_infracao", "pesquisar": "HORA"},
        {"nome": "velocidade_regulamentada", "pesquisar": "VELOCIDADE REGULAMENTADA"},
        {"nome": "velocidade_media", "pesquisar": "VELOCIDADE MEDIDA"},
        {"nome": "velocidade_considerada", "pesquisar": "VELOCIDADE CONSIDERADA"},
        {"nome": "enquadramento", "pesquisar": "ENQUADRAMENTO"},
        {"nome": "artigo_ctb", "pesquisar": "ARTIGO DO CTB"},
        {"nome": "natureza", "pesquisar": "NATUREZA"},
        {"nome": "pontuacao", "pesquisar": "PONTUAÇÃO"},
        {"nome": "numero_ait", "pesquisar": "Nº AIT"},
        {"nome": "data_limite_ind_condutor", "pesquisar": "DATA LIMITE IND. CONDUTOR / DEFESA AUTUAÇÃO"},
        {"nome": "nro_infraest", "pesquisar": "NRO. INFRAEST"},
        {"nome": "identificacao_equipamento", "pesquisar": "IDENTIFICAÇÃO DO EQUIPAMENTO"},
        {"nome": "afericao_certificacao", "pesquisar": "AFERIÇÃO / CERTIFICAÇÃO"},
        {"nome": "agente_transito", "pesquisar": "AGENTE DE TRÂNSITO"}
    ]

    doc_texto = "ASSINATURA DO CONDUTOR / INFRATOR DATA ASSINATURA DO PROPRIETÁRIO DO VEÍCULOPLACADZC1234MARCATOYOTAESPÉCIEPASSAGEIRONOME DO PROPRIETÁRIOMARIANA ALVES DA SILVAINFRAÇÃOTRANSITAR EM VELOCIDADE SUPERIOR A MAXIMA PERMITIDA EM ATE 20%LOCALRUA BANDEIRANTES (CENTRO), NUMERO 272 – CENTRO, MARÍLIA-SPCOD. LOC. EQUIP.5375DATA DA INFRAÇÃO10/02/2024HORA09:52DATA DA EMISSÃO12/02/2024VELOCIDADE REGULAMENTADA KM/H50VELOCIDADE MEDIDA KM/H70VELOCIDADE CONSIDERADA KM/H63ENQUADRAMENTO74550ARTIGO DO CTBARTIGO 218 INCISO INATUREZAMEDIAPONTUAÇÃO4Nº AITJV-A3-660149-9DATA LIMITE IND. CONDUTOR / DEFESA AUTUAÇÃO25/02/2024NRO. INFRAEST9016353284IDENTIFICAÇÃO DO EQUIPAMENTOSPL-R4R2217AFERIÇÃO / CERTIFICAÇÃO15/08/2023AGENTE DE TRÂNSITO006767Cópia desta imagem poderá ser obtida nos endereços abaixo:Posto DSV instalado no DETRANDEPTO DE OPERAÇÃO DO SISTEMA VIÁRIO - DSVINFORMAÇÕES IMPORTANTESSr. Proprietário, não sendo o responsável pelo cometimento da infração, preencha os dados abaixo e envie pelocorreio ao DEPARTAMENTO DE OPERAÇÃO DO SISTEMA VIÁRIO, INDICAÇÃO DE CONDUTOR,Rua Sumidouro, 740 - Pinheiros - SP CEP 05428-900, até a data estipulada abaixo.ATENÇÃOA Indicação do Condutor só produzirá efeito se encaminhada até 13/01/2017 e estiver corretamente preenchida, sem rasuras, com as assinaturas originais, do condutor, e do proprietário do veiculo, eacompanhada de cópia simples e legível da Carteira Nacional de Habilitação, ou Permissão para Dirigir do condutor indicado, e cópia simples e legível de documento de identidade (RG, CREA, OAB, ETC)do proprietário do veículo ou seu representante legal.Em resumo, a IDENTIFICAÇÃO DO CONDUTOR DO VEÍCULO QUANDO DA INFRAÇÃO , deverá:1 - Conter a assinatura original do proprietário.2 - Conter a assinatura original do infrator, conforme acima descrito.3 - Estar acompanhada de fotocópia simples, legível e em tamanho natural da Carteira Nacional de Habilitação, ou Permissão para Dirigir do Infrator.4 - Estar acompanhada de fotocópia simples, legível e em tamanho natural de documento de identidade (RG, CREA, OAB, ETC) do proprietário do veículo ou seu representante legal.Não realizada a Indicação do Condutor, o proprietário do veículo será responsabilizado, além do pagamento da multa, pelos pontos relativos à infração cometida.No caso do veículo pertencer a pessoa jurídica, a não indicação do condutor responsável pela infração resultará na aplicação de nova penalidade de multa, independente daquela originada pela infração doveículo.Na impossibilidade da coleta da assinatura do condutor indicado, o proprietário deverá anexar cópia de documento onde conste cláusula de responsabilidade por quaisquer infrações cometidas na conduçãodo veículo, bem como pela pontuação delas decorrentes.IDENTIFICAÇÃO DO CONDUTOR DO VEÍCULO QUANDO DA INFRAÇÃONOMENÚMERO DO REGISTRO CNH ESTADO NÚMERO DO CPF NÚMERO DO RG ESTADOENDEREÇOBAIRRO CEP MUNICÍPIO ESTADONOTIFICAÇÃO DE AUTUAÇÃO DEINFRAÇÃO DE TRÂNSITODEPTO DE OPERAÇÃO DO SISTEMA VIÁRIO - DSVINDICAÇÃO DO CONDUTORINFORMAÇÕES ÚTEIS DEFESA DA AUTUAÇÃOEm que situação apresentar? Após receber esta Notificação de Autuação, sempre que houver erro flagrante (local inexistente, impossibilidade do cometimento da infração pelo tipo doveículo ou divergência de características entre o seu e o veículo autuado).Quando? No mesmo prazo da indicação de condutor, acima indicado.Como? Em forma de requerimento, ao diretor do DSV, para a caixa postal 11090, CEP 05422-970, com cópia simples dos seguintes documentos:- Notificação de Autuação ou Auto de Infração de Trânsito;- Certificado de registro e licenciamento do veículo CRLV, ou certificado de registro de veículo CRV;- Sendo o proprietário do veículo pessoa física, a Carteira Nacional de Habilitação ou Documento de Identificação que comprove a assinatura do requerente (condutor ou proprietário);- Sendo o proprietário do veículo pessoa jurídica, um documento comprovando a representação do requerente (Estatuto, Contrato Social, Procuração, etc);- Sendo o requerente o Condutor indicado, além do formulário da indicação, a Carteira Nacional de Habilitação ou Permissão para Dirigir;- Outros que comprovem o erro na Notificação de Autuação ou no Auto de Infração de Trânsito.ATENÇÃO: A comissão que julga a DEFESA DA AUTUAÇÃO, não analisa os motivos pelos quais a infração foi cometida.Portanto quaisquer outros tipos de argumentos deverão ser apresentados oportunamente na forma de Recurso, quando do recebimento da Notificação da Penalidade (multa), para ser julgado pelaJARI - Junta Administrativa de Recursos e Infrações.A interposição da defesa da autuação não desobriga o proprietário do veículo de fazer a indicação do condutor, se cabível. O proprietário do veículo será comunicado do julgamento através de avisode resultado a ser enviado através do correio. Caso prefira entregar pessoalmente, tanto a Defesa como a Indicação de Condutor, utilizar um dos postos abaixo MEDIANTE RETIRADA DE SENHA ESUJEITO A ESPERA PARA ATENDIMENTO , de segunda-feira à sexta-feira, exceto feriados, das 8h às 18h.. Shopping Interlar - Av Interlagos Nº 2.225.. Shopping Aricanduva - Av. Aricanduva Nº 5555.. DETRAN- AV. do Estado Nº 900.NÚMERO DO AIITJV-A3-660149-9PLACADZC1234DATA DA EMISSÃO12/02/2018"

    texto = doc_texto

    


    def adicionar_espacos_apos_termos(texto):
        for termo_chave in termos_chave:
            termo_pesquisar = termo_chave["pesquisar"]
            texto = re.sub(r'(\S)(' + re.escape(termo_pesquisar) + r')(\S)', r'\1 \2 \3', texto)
            texto = re.sub(r'(\S)(' + re.escape(termo_pesquisar) + r')', r'\1 \2', texto)
            texto = re.sub(r'(' + re.escape(termo_pesquisar) + r')(\S)', r'\1 \2', texto)
        texto = re.sub(r'([a-z])([A-Z0-9])', r'\1 \2', texto)
        texto = re.sub(r'([A-Z])([A-Z][a-z])', r'\1 \2', texto)
        texto = re.sub(r'([0-9])([A-Z])', r'\1 \2', texto)
        texto = re.sub(r'(\.)([A-Z])', r'\1 \2', texto)
        texto = re.sub(r'(,)([A-Z])', r'\1 \2', texto)
        texto = re.sub(r'(\w+-SP)(COD)', r'\1 \2', texto)
        return texto

    def quebra_linha(texto):
        for termo in termos_chave:
            termo_pesquisar = termo["pesquisar"]
            if termo != "DATA DA INFRAÇÃO":
                texto = re.sub(r'(\b' + re.escape(termo_pesquisar) + r'\b)', r'\n\1', texto)
        texto = re.sub(r"DATA DA\s*\nINFRAÇÃO", "DATA DA INFRAÇÃO", texto)
        texto = re.sub(r"([A-Z][A-Z]+-[A-Z][A-Z]+) (COD\. LOC\. EQUIP\.)", r"\1\n\2", texto)
        return texto
    
    
    texto_espaço = adicionar_espacos_apos_termos(texto)
    texto_formatado = quebra_linha(texto_espaço)
    texto_formatado = re.sub(r"(COD\. LOC\. EQUIP\.\d{4})( DATA DA INFRAÇÃO)", r"\1\n\2", texto_formatado)

    dados_extraidos = ExtrairDados.extrair_dados(texto_formatado, termos_chave)

    for chave, valor in dados_extraidos.items():
    # Imprimir cada chave e seu valor correspondente
     print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()









