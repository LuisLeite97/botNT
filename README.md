# Sumarizador de Notas Técnicas de DF-e 

## Motivo
Este projeto foi criado na imersão IA Alura. A proposta é utilizar a IA Gemini para resumir notas técnicas de DF-e (Documentos Fiscais Eletrônicos, qu).
DF-e são documentos que indicam operações fiscais, o mais conhecido é a NF-e e NFC-e, que em ordem são a Nota Fiscal Eletrônica e a Nota Fiscal do Consumidor ou Cupom Fiscal.
Visto que esses documentos costumam ser extensos e são criados pra toda alteração na estrutura e regras de emissão de documentos como nota fiscal, o objetivo do projeto é utilizar a IA Gemini para resumir em tópicos importantes do documento enviado para a IA, isto é realizado com um pré-promtp inserido no histórico para contextualização.
Estes documentos são voltados a contadores, softwarehouses e contribuintes em geral. Em suma, o projeto visa facilitar para softwarehouses/desenvolvedores terem um resumo da documentação de X documentação do governo.

## Funcionamento
O projeto utilizou a lib Streamlit do Python para uma visualização simples dos componentes. O fluxo se inicia com o envio de um pdf da Nota Técnica, a abertura do canal de comunicação com IA se inicia com um prompt já inserido anteriormente, que vai contextualizar a IA sobre o que são DF-es, NT-es e o objetivo final que é a extração visando o desenvolvimento de uma aplicação fiscal.

## Instruções Adicionais
1. **Rodando o App:**
   - Clone ou baixe o repositório para sua máquina local.
   - Confira se as libs estão instaladas, principalmente o Streamlit. Caso contrario, a instação é simples: !pip install streamlit
   - Para rodar a aplicação basta acessar o diretório do .py via CMD e executar o comando Streamlit run gemini_NT.py
   - Uma forma simplificada é executando o .bat contendo a instrução de execução.
   
2. **Funcionamento:**
   - O funcionamento é simples, bastando enviar uma Nota Técnicas no input especifico.
   - Localização das NT:
   - NFe: https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=
   - CTe: https://www.cte.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Y0nErnoZpsg=
     
