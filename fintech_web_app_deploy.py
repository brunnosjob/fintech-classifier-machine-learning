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

# Blog
st.sidebar.markdown('Feito por : Bruno Rodrigues')

st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/bruno-rodrigues-carloto)")
st.sidebar.markdown("- [Medium: Data Marte](https://https://br-cienciadedados.medium.com)")
st.sidebar.markdown("- [Github](https://https://github.com/brunnosjob)")

#Título
st.title('Deploy de modelo de machine learning')
st.header('Machine Learning para serviços financeiros eletrônicos')
st.subheader('')

#Informações sobre o projeto
st.markdown('### Sobre o projeto')
st.markdown('''Como projeto de portfólio de Ciência de Dados, esse modelo objetiva auxiliar as fintechs acerca de empréstimos automáticos de crédito ao cliente via aplicativo.
O papel dessa inteligência é aprovar ou negar a solicitação de empréstimo de um determinado cliente a partir de alguns dados pessoais.''')

usuario =  st.text_input('Me informe seu nome para termos uma interação melhor.')
st.markdown('---')
#Criando variáveis 
st.header('Simulação')
st.subheader('Easy Bank')

renda = st.number_input('Me informe sua renda.')
idade = st.number_input('Agora, preciso saber da sua idade.', 18)
emprestimo = st.number_input('Qual o valor de empréstimo do seu interesse?')
st.markdown('Sem juros')
parcela = st.radio('Selecione a quantidade de parcela',(1, 2, 3, 4, 5, 6))
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

st.write(' ')
st.write('Atenção! Sendo sua renda de R$ {}; o empréstimo indicado é de no máximo aproximadamente R$ {}'.format(renda, round(renda/3.35), 2))
st.write(' ')

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
        st.write('A mensalidade ficou no valor de R$ {} por mês'.format(emprestimo/parcela))
        st.write('Já efetuamos a transferência. Confira! Agradecemos sua preferência!')
        
    elif emprestimo <= (renda * 0.3):
        st.write('{}, sua solicitação de no valor R$ {} foi aprovada. Parabéns!'.format(usuario, emprestimo))
        st.write('A mensalidade ficou no valor de R$ {} por mês'.format(emprestimo/parcela))
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
    
    elif emprestimo <= (renda * 0.3):
       st.write('{}, lamentamos! Sua soliciatação de empréstimo no valor de R$ {} não foi aprovada.'.format(usuario, emprestimo))
       st.write('Tente um valor menor.')             
                         
    elif mensalidade >= (renda * 0.3):
       st.write('{}, Sua soliciatação de empréstimo no valor de R$ {} não foi aprovada.'.format(usuario, emprestimo))
       st.write('Tente um valor menor.')                       
        
