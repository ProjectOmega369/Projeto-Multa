import re
import ExtrairDados

#Precisei colocar está lista ou "dicionario" pois ele realize espaços mas ainda assim ficava algumas partes
#Juntas como MARCAESPECIEPASSAGEIRO, então fiz essa lista com as chaves ou campos das informações para depois
#Adicionar espaço entre elas
termos_chave = [
        "PLACA", "MARCA", "ESPÉCIE", "NOME DO PROPRIETÁRIO", "INFRAÇÃO", "LOCAL",
        "NUMERO", "DATA DA INFRAÇÃO", "HORA", "DATA DA EMISSÃO", "VELOCIDADE REGULAMENTADA",
        "VELOCIDADE MEDIDA", "VELOCIDADE CONSIDERADA", "ENQUADRAMENTO", "ARTIGO DO CTB",
        "NATUREZA", "PONTUAÇÃO", "Nº AIT", "DATA LIMITE IND. CONDUTOR / DEFESA AUTUAÇÃO",
        "NRO. INFRAEST", "IDENTIFICAÇÃO DO EQUIPAMENTO", "AFERIÇÃO / CERTIFICAÇÃO",
        "AGENTE DE TRÂNSITO"
    ]

doc_texto = "ASSINATURA DO CONDUTOR / INFRATOR DATA ASSINATURA DO PROPRIETÁRIO DO VEÍCULOPLACAFFD2155MARCACHEVROLETESPÉCIEPASSAGEIRONOME DO PROPRIETÁRIOJORGE ROGERIO MALBOROINFRAÇÃOTRANSITAR EM VELOCIDADE SUPERIOR A MAXIMA PERMITIDA EM ATE 20%LOCALAV.RIO BRANCO – ALTO CAFEZAL, MARÍLIA-SPCOD. LOC. EQUIP.5375DATA DA INFRAÇÃO11/04/2024HORA03:23DATA DA EMISSÃO13/04/2024VELOCIDADE REGULAMENTADA KM/H40VELOCIDADE MEDIDA KM/H67VELOCIDADE CONSIDERADA KM/H60ENQUADRAMENTO74552ARTIGO DO CTBARTIGO 218 INCISO INATUREZAMEDIAPONTUAÇÃO4Nº AITJV-A3-660149-9DATA LIMITE IND. CONDUTOR / DEFESA AUTUAÇÃO20/04/2024NRO. INFRAEST9016353284IDENTIFICAÇÃO DO EQUIPAMENTOSPL-R4R2217AFERIÇÃO / CERTIFICAÇÃO15/08/2023AGENTE DE TRÂNSITO005213Cópia desta imagem poderá ser obtida nos endereços abaixo:Posto DSV instalado no DETRANDEPTO DE OPERAÇÃO DO SISTEMA VIÁRIO - DSVINFORMAÇÕES IMPORTANTESSr. Proprietário, não sendo o responsável pelo cometimento da infração, preencha os dados abaixo e envie pelocorreio ao DEPARTAMENTO DE OPERAÇÃO DO SISTEMA VIÁRIO, INDICAÇÃO DE CONDUTOR,Rua Sumidouro, 740 - Pinheiros - SP CEP 05428-900, até a data estipulada abaixo.ATENÇÃOA Indicação do Condutor só produzirá efeito se encaminhada até 13/01/2017 e estiver corretamente preenchida, sem rasuras, com as assinaturas originais, do condutor, e do proprietário do veiculo, eacompanhada de cópia simples e legível da Carteira Nacional de Habilitação, ou Permissão para Dirigir do condutor indicado, e cópia simples e legível de documento de identidade (RG, CREA, OAB, ETC)do proprietário do veículo ou seu representante legal.Em resumo, a IDENTIFICAÇÃO DO CONDUTOR DO VEÍCULO QUANDO DA INFRAÇÃO , deverá:1 - Conter a assinatura original do proprietário.2 - Conter a assinatura original do infrator, conforme acima descrito.3 - Estar acompanhada de fotocópia simples, legível e em tamanho natural da Carteira Nacional de Habilitação, ou Permissão para Dirigir do Infrator.4 - Estar acompanhada de fotocópia simples, legível e em tamanho natural de documento de identidade (RG, CREA, OAB, ETC) do proprietário do veículo ou seu representante legal.Não realizada a Indicação do Condutor, o proprietário do veículo será responsabilizado, além do pagamento da multa, pelos pontos relativos à infração cometida.No caso do veículo pertencer a pessoa jurídica, a não indicação do condutor responsável pela infração resultará na aplicação de nova penalidade de multa, independente daquela originada pela infração doveículo.Na impossibilidade da coleta da assinatura do condutor indicado, o proprietário deverá anexar cópia de documento onde conste cláusula de responsabilidade por quaisquer infrações cometidas na conduçãodo veículo, bem como pela pontuação delas decorrentes.IDENTIFICAÇÃO DO CONDUTOR DO VEÍCULO QUANDO DA INFRAÇÃONOMENÚMERO DO REGISTRO CNH ESTADO NÚMERO DO CPF NÚMERO DO RG ESTADOENDEREÇOBAIRRO CEP MUNICÍPIO ESTADONOTIFICAÇÃO DE AUTUAÇÃO DEINFRAÇÃO DE TRÂNSITODEPTO DE OPERAÇÃO DO SISTEMA VIÁRIO - DSVINDICAÇÃO DO CONDUTORINFORMAÇÕES ÚTEIS DEFESA DA AUTUAÇÃOEm que situação apresentar? Após receber esta Notificação de Autuação, sempre que houver erro flagrante (local inexistente, impossibilidade do cometimento da infração pelo tipo doveículo ou divergência de características entre o seu e o veículo autuado).Quando? No mesmo prazo da indicação de condutor, acima indicado.Como? Em forma de requerimento, ao diretor do DSV, para a caixa postal 11090, CEP 05422-970, com cópia simples dos seguintes documentos:- Notificação de Autuação ou Auto de Infração de Trânsito;- Certificado de registro e licenciamento do veículo CRLV, ou certificado de registro de veículo CRV;- Sendo o proprietário do veículo pessoa física, a Carteira Nacional de Habilitação ou Documento de Identificação que comprove a assinatura do requerente (condutor ou proprietário);- Sendo o proprietário do veículo pessoa jurídica, um documento comprovando a representação do requerente (Estatuto, Contrato Social, Procuração, etc);- Sendo o requerente o Condutor indicado, além do formulário da indicação, a Carteira Nacional de Habilitação ou Permissão para Dirigir;- Outros que comprovem o erro na Notificação de Autuação ou no Auto de Infração de Trânsito.ATENÇÃO: A comissão que julga a DEFESA DA AUTUAÇÃO, não analisa os motivos pelos quais a infração foi cometida.Portanto quaisquer outros tipos de argumentos deverão ser apresentados oportunamente na forma de Recurso, quando do recebimento da Notificação da Penalidade (multa), para ser julgado pelaJARI - Junta Administrativa de Recursos e Infrações.A interposição da defesa da autuação não desobriga o proprietário do veículo de fazer a indicação do condutor, se cabível. O proprietário do veículo será comunicado do julgamento através de avisode resultado a ser enviado através do correio. Caso prefira entregar pessoalmente, tanto a Defesa como a Indicação de Condutor, utilizar um dos postos abaixo MEDIANTE RETIRADA DE SENHA ESUJEITO A ESPERA PARA ATENDIMENTO , de segunda-feira à sexta-feira, exceto feriados, das 8h às 18h.. Shopping Interlar - Av Interlagos Nº 2.225.. Shopping Aricanduva - Av. Aricanduva Nº 5555.. DETRAN- AV. do Estado Nº 900.NÚMERO DO AIITJV-A3-660149-9PLACAFFD2155DATA DA EMISSÃO13/04/2024"

texto = doc_texto

def adicionar_espacos_apos_termos(texto):
    # Lista de termos chave que devem ser seguidos por um espaço
    
    
    # Adiciona espaço após cada termo chave
    for termo in termos_chave:

        texto = re.sub(r'(\S)(' + re.escape(termo) + r')(\S)', r'\1 \2 \3', texto)
        texto = re.sub(r'(\S)(' + re.escape(termo) + r')', r'\1 \2', texto)
        texto = re.sub(r'(' + re.escape(termo) + r')(\S)', r'\1 \2', texto)

    

    
    # Adiciona espaços entre letras minúsculas e maiúsculas, e entre números e letras
    texto = re.sub(r'([a-z])([A-Z0-9])', r'\1 \2', texto)
    texto = re.sub(r'([A-Z])([A-Z][a-z])', r'\1 \2', texto)
    texto = re.sub(r'([0-9])([A-Z])', r'\1 \2', texto)
    
    # Adiciona espaço após pontos e vírgulas, se necessário
    texto = re.sub(r'(\.)([A-Z])', r'\1 \2', texto)
    texto = re.sub(r'(,)([A-Z])', r'\1 \2', texto)

    texto = re.sub(r'(\w+-SP)(COD)', r'\1 \2', texto)

    
    
    return texto



def quebra_linha(texto):
    for termo in termos_chave:
        if termo != "DATA DA INFRAÇÃO":
            texto = re.sub(r'(\b' + re.escape(termo) + r'\b)', r'\n\1', texto)
    
    texto = re.sub(r"DATA DA\s*\nINFRAÇÃO","DATA DA INFRAÇÃO", texto)

    texto = re.sub(r"([A-Z][A-Z]+-[A-Z][A-Z]+) (COD\. LOC\. EQUIP\.)", r"\1\n\2", texto)
    
    return texto



# Adiciona espaços após termos chave
texto_espaço = adicionar_espacos_apos_termos(doc_texto)

# Realize a Quebra de Linhas 
texto_formatado = quebra_linha(texto_espaço)


texto_formatado = re.sub(r"(COD\. LOC\. EQUIP\.\d{4})( DATA DA INFRAÇÃO)", r"\1\n\2", texto_formatado)

# Extrai os dados
dados_extraidos = ExtrairDados.extrair_dados(texto_formatado)



# Exibe os dados extraídos
for chave, valor in dados_extraidos.items():
 print(f"{chave}: {valor}")









