#!/usr/bin/env python
# coding: utf-8

# # web app

# In[2]:


#Importando bibliotecas
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle
import streamlit as st

#Indicando sidebar
st.markdown('### __Observação: para mais informações, clique na seta no canto esquerdo superior da tela__ ')

#Indicando do que se trata a web app
st.sidebar.subheader('Projeto de portfólio de Ciência de Dados')
st.sidebar.title('Menu')
pag = st.sidebar.selectbox('Selecione a página', ('Interagir com a inteligência'), ('Sobre o projeto'))

st.sidebar.markdown('Feito por : Bruno Rodrigues')

st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/bruno-rodrigues-carloto)")
st.sidebar.markdown("- [Medium](https://https://br-cienciadedados.medium.com)")
st.sidebar.markdown("- [Github](https://https://github.com/brunnosjob)")

if pag == 'Interação com a inteligência':
    
    st.header('Simulação')
    st.markdown(' ')
    usuario =  st.text_input('Me informe seu nome para termos uma interação melhor.')
    st.markdown('---')
    #Criando variáveis 
    st.subheader('Seja bem-vindx à área Good Bank Loan')

    renda = st.number_input('Me informe sua renda.')
    idade = st.number_input('Agora, preciso saber da sua idade.', 18)
    emprestimo = st.number_input('Qual o valor de empréstimo do seu interesse?', 0.0, 10000.00)
    st.markdown('Sem juros')
    parcela = st.radio('Selecione a quantidade de parcela',(1, 2, 3, 4, 5))
    mensalidade = (round((emprestimo/parcela),2))
    st.write('Se o empréstimo for aprovado, a mensalidade fica de R$ {} por mês'.format(mensalidade))

    #Aplicando a inteligência
    st.header('Resultado')
    st.subheader('Aguarde o processamento dos dados')
    #Carregando modelos

    #Classificador
    with open('decision_tree_classifier_fintech.pkl', 'rb') as f:
        standard_classificacao, tree_tomek = pickle.load(f)


    #Geração de conjunto de dados
    #Criando dataframe para dados de cliente fictício
    cliente_classificacao = [[renda, idade, emprestimo]]
    cliente_classificacao_df = pd.DataFrame(cliente_classificacao)

    #Transformação: StandardScaler - classificação
    #Padronizando os dados
    cliente_standard = standard_classificacao.transform(cliente_classificacao_df)

    #Estimando - classificando
    classificacao = tree_tomek.predict(cliente_standard)

    #Condição e apresentação
    if classificacao == 0:
         
        if emprestimo >= 100 and emprestimo <= 330:
            st.write('{}, pedimos desculpas! Infelizmente não podemos comprometer a sua renda. Zelamos por você.'.format(usuario))
            st.write('Obrigado pela preferência')
    
        elif renda < 350:
            st.write('{}, pedimos desculpas! Infelizmente não podemos comprometer a sua renda. Zelamos por você.'.format(usuario))
            st.write('Obrigado pela preferência')
            
        elif emprestimo < 100:
            st.write('{}, pedimos desculpas! Nossas ofertas de crédito são a partir de R$ 100,00.'.format(usuario))
            st.write('Obrigado pela preferência!')
    
        elif mensalidade >= (renda * 0.3):
            st.write('{}, sua solicitação de empréstimo no valor de R$ {} foi aprovada. Parabéns!'.format(usuario, emprestimo))
            st.write('Mas, atenção! Você está comprometendo mais de 30% de sua renda.')
            st.write('Esses 30% são o limite alerta para se contratar créditos.')
            st.write('A mensalidade ficou no valor de R$ {} por mês'.format(mensalidade))
        
            if st.button('Posso confirmar a transferência'):
                st.write('Já efetuamos a transferência. Confira! Agradecemos sua preferência!')
            
        
        elif mensalidade <= (renda * 0.3):
            st.write('{}, sua solicitação de no valor R$ {} foi aprovada. Parabéns!'.format(usuario, emprestimo))
            st.write('A mensalidade ficou no valor de R$ {} por mês'.format(mensalidade))
        
            if st.button('Posso confirmar a transferência'):
                st.write('Já efetuamos a transferência. Confira! Agradecemos sua preferência!')            
    
    if classificacao == 1:
    
        if emprestimo >= 100 and emprestimo <= 330:
           st.write('{}, pedimos desculpas! Infelizmente não podemos comprometer sua renda. Zelamos por você.'.format(usuario))
           st.write('Obrigado pela preferência')
        
        elif renda < 350:
            st.write('{}, pedimos desculpas! Infelizmente não podemos comprometer a sua renda. Zelamos por você.'.format(usuario))
            st.write('Obrigado pela preferência')
    
        elif emprestimo < 100:
            st.write('{}, pedimos desculpas. Sua solicitação de empréstimo no valor de R$ {} não foi aprovada.'.format(usuario, emprestimo))
            st.write('Mas gostarias de informar também que nossas ofertas de crédito são a partir de R$ 100,00.')
            st.write('Obrigado pela preferência!')
    
        elif mensalidade <= (renda * 0.3):
            st.write('{}, lamentamos! Sua soliciatação de empréstimo no valor de R$ {} não foi aprovada.'.format(usuario, emprestimo))
            st.write('Tente um valor menor.')             
                         
        elif mensalidade >= (renda * 0.3):
            st.write('{}, Sua soliciatação de empréstimo no valor de R$ {} não foi aprovada.'.format(usuario, emprestimo))
            st.write('Tente um valor menor.')                       

elif pag == 'Sobre o projeto':
    
    st.title('Projeto de portfólio de Ciência de Dados')
    st.markdown(' ')
    st.markdown('### Machine learning para serviços financeiros tecnológicos')
      
