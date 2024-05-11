#!pip install google-generativeai
#!pip install PyPDF2


import streamlit as st
import google.generativeai as genai
import PyPDF2
import tempfile

# Configuração do modelo 
genai.configure(api_key="SUA CHAVE")

model_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 0,
}

safety = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=model_config,
    safety_settings=safety,
)

# Instruções iniciais para o modelo
instrucoes = {
    "role": "user",
    "parts": [
        """Existe uma documentação técnicas de desenvolvimento de software, baseado em mudanças fiscais.
Esta documentação é composta por regras de negócio e questões técnicas (que abrangem tipos de arquivo, webservices de integração, segurança de desenvolvimento). Exemplo de documentação:

Regras de negócios:
1. Regra de calculo ICMS:
A regra de calculo do campo valor do ICMS se dá por uma base de calculo que é um percentual do valor do item. Caso a base seja de 100%, minha alíquota é calculada no valor total do produto.

Questões técnicas:
1. Devem ser criadas as seguintes colunas na tabela na base de dados, para comportar os novos campos:
ALTER TABLE tabela ADD icms currency;

2. A TAG no XML se encontra em <ICMS>

------

Baseado no modelo da documentação de desenvolvimento, sumarize o conteúdo desta nota técnica anexada. Foque no que precisaria ser desenvolvido ou alterado em um sistema, ou no caso, o que o contribuinte precisa emitir. Traga data de homologação e produção se tiver. Caso a documentação seja uma alteração apenas de validações do governo, ignore explicando que não há alterações pro contribuinte."""
    ],
}

chat = model.start_chat(history=[instrucoes])


def extrair_texto_pdf(arquivo):
    with open(arquivo, "rb") as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        texto = ""
        for num_pagina in range(len(leitor_pdf.pages)):
            pagina = leitor_pdf.pages[num_pagina]
            texto += pagina.extract_text()
    return texto


# Interface Streamlit
st.title("Análise de Documentos Fiscais com Gemini")

arquivo_pdf = st.file_uploader("Selecione o arquivo PDF", type="pdf")

if arquivo_pdf is not None:
    # Salvar o arquivo temporariamente
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(arquivo_pdf.getvalue())
        temp_path = temp_file.name
    # Extrair texto do PDF
    conteudo_arquivo = extrair_texto_pdf(temp_path)

    if conteudo_arquivo:
        response = chat.send_message(conteudo_arquivo)
        st.write(response.text)

    if st.button("Analisar PDF"):
        response = chat.send_message(conteudo_arquivo)
        st.write(response.text)   

if st.button("Encerrar"):
    st.stop()