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

#Cabeçalho
st.header('Machine Learning para serviços financeiros eletrônicos')
st.subheader('Modelo de machine learning classificador para otimização da relação com clientes')
st.subheader('')

#Informe
st.write('Esse modelo objetiva não apenas classificar se um cliente pagará ou não pagará um empréstimo solicitado, mas, também tem a capacidade de sugerir valores e dicas viáveis aos clientes.')


#Criando variáveis 
st.write('Olá! É um prazer interagir com você nessa simulação. Espero que goste desse momento.')
usuario =  st.text_input('Gostaria de saber seu nome.')

renda = st.slider('Me informe sua renda.', 350, 10000, 0)
idade = st.slider('Agora, preciso saber da sua idade.', 18, 150, 18)
emprestimo = st.slider('Qual o valor de empréstimo do seu interesse?', 100, 10000, 0)

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

rang = []
lista_emprestimo = []
limite_receita = renda * 0.3
limite_receita = int(limite_receita)

rang = []
for i in range(emprestimo, limite_receita):
    rang.append(i)
    
limite = len(rang)
st.write(' ')
st.write('Atenção! Sendo sua renda de R$ {}; o empréstimo indicado é de no máximo aproximadamente R$ {}'.format(renda, round(renda/3.35), 2))
st.write(' ')

#Condição e apresentação
if classificacao == 0:
     
    if renda <= 330:
        st.write('{}, pedimos desculpas! Infelizmente não podemos comprometer a sua renda. Zelamos por você.'.format(usuario))
        st.write('Obrigado pela preferência')
        
    elif emprestimo < 100:
        st.write('{}, pedimos desculpas! Nossas ofertas de crédito são a partir de R$ 100,00.'.format(usuario))
        st.write('Obrigado pela preferência!')
    
    elif emprestimo >= (renda * 0.3):
        st.write('{}, seu crédito de R$ {} foi aprovado. Parabéns!'.format(usuario, emprestimo))
        st.write('Mas, atenção! Você está comprometendo mais de 30% de sua renda.')
        st.write('Esses 30% é o limite alerta para se contratar créditos.')
        
    elif emprestimo == (renda * 0.3):
        st.write('{}, seu crédito de R$ {} foi aprovado. Parabéns!'.format(usuario, emprestimo))
        
    elif emprestimo <= (renda * 0.3):
        for i in np.arange(emprestimo, (renda*0.3), 1):

            #Criando dataframe para dados de cliente fictício
            cliente_classificacao_sugestao = [[renda, idade, i]]
            cliente_classificacao_sugestao_df = pd.DataFrame(cliente_classificacao_sugestao)
            
            #Transformação: StandardScaler - classificação
            #Padronizando os dados
            cliente_standard_sugestao = standard_classificacao.transform(cliente_classificacao_sugestao_df)
            
            #Estimando - classificando
            reavaliacao = tree_tomek.predict(cliente_standard_sugestao)
            
            #Condicional de sugestão
            if reavaliacao == 0:
                lista_emprestimo.append(i)
                
                if len(lista_emprestimo) == limite:
                    if emprestimo > lista_emprestimo[-1]: 
                        st.write('{}, seu crédito de R$ {} foi aprovado. Parabéns!'.format(usuario, emprestimo))
                        st.write(' ')
                        st.write('Mas gostariamos de informar que você foi aprovado para um crédito de R$ {}.'.format(lista_emprestimo[-1]))
                        st.write('Que tal?')
                    
            elif reavaliacao == 1:
                if len(lista_emprestimo) == limite:
                    st.write('{}, seu crédito de R$ {} foi aprovado. Parabéns!'.format(usuario, emprestimo))
                    
    
if classificacao == 1:
    
    if renda <= 330:
        st.write('{}, pedimos esculpas! Infelizmente não podemos comprometer sua renda. Zelamos por você.'.format(usuario))
        st.write('Obrigado pela preferência')
    
    elif emprestimo < 100:
        st.write('{}, pedimos desculpas. Seu crédito de R$ {} foi aprovado. Parabéns!'.format(usuario, emprestimo))
        st.write('Mas gostarias de informar também que nossas ofertas de crédito são a partir de R$ 100,00.')
        st.write('Obrigado pela preferência!')
    
    elif emprestimo <= (renda * 0.3):
        for i in np.arange(100, (renda*0.3), 1):

            #Criando dataframe para dados de cliente fictício
            cliente_classificacao_sugestao = [[renda, idade, i]]
            cliente_classificacao_sugestao_df = pd.DataFrame(cliente_classificacao_sugestao)
            
            #Transformação: StandardScaler - classificação
            #Padronizando os dados
            cliente_standard_sugestao = standard_classificacao.transform(cliente_classificacao_sugestao_df)
            
            #Estimando - classificando
            reavaliacao = tree_tomek.predict(cliente_standard_sugestao)
            
            #Condicional de sugestão
            if reavaliacao == 0:
                lista_emprestimo.append(i)
                    
                    
                if len(lista_emprestimo) == limite:
                    if emprestimo > lista_emprestimo[-1]: 
                        st.write('{}, seu crédito de R$ {} não foi aprovado.'.format(usuario, emprestimo))
                        st.write(' ')
                        st.write('Mas gostariamos de informar que você foi aprovado para um crédito de R$ {}.'.format(lista_emprestimo[-1]))
                        st.write('Que tal?')
                    
            elif reavaliacao == 1:
                if len(lista_emprestimo) == limite:
                    st.write('{}, seu crédito de R$ {} não foi aprovado.'.format(usuario, emprestimo))
                    st.write('Obrigado pela preferência!')
        
        
    elif emprestimo >= (renda * 0.3):
        for i in np.arange(100, (renda*0.3), 1):

            #Criando dataframe para dados de cliente fictício
            cliente_classificacao_sugestao = [[renda, idade, i]]
            cliente_classificacao_sugestao_df = pd.DataFrame(cliente_classificacao_sugestao)
            
            #Transformação: StandardScaler - classificação
            #Padronizando os dados
            cliente_standard_sugestao = standard_classificacao.transform(cliente_classificacao_sugestao_df)
            
            #Estimando - classificando
            reavaliacao = tree_tomek.predict(cliente_standard_sugestao)
            
            #Condicional de sugestão
            if reavaliacao == 0:
                lista_emprestimo.append(i)
                        
                if len(lista_emprestimo) == limite:
                    if emprestimo > lista_emprestimo[-1]: 
                        st.write('{}, seu crédito de R$ {} não foi aprovado.'.format(usuario, emprestimo))
                        st.write(' ')
                        st.write('Mas gostariamos de informar que você foi aprovado para um crédito de R$ {}.'.format(lista_emprestimo[-1]))
                        st.write('Que tal?')
                    
            elif reavaliacao == 1:
                if len(lista_emprestimo) == limite:
                    st.write('{}, seu crédito de R$ {} não foi aprovado.'.format(usuario, emprestimo))
                    st.write('Obrigado pela preferência!')


# In[ ]:




