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
from matplotlib.backends.backend_agg import RendererAgg
from PIL import Image
import pickle
import streamlit as st

#Indicando sidebar
st.markdown('*__Observação: para mais informações acerca do projeto, clique na seta no canto esquerdo superior da tela__* ')

#Indicando do que se trata a web app
st.sidebar.subheader('Projeto de portfólio de Ciência de Dados')
st.sidebar.markdown('''Leia o [artigo do projeto](https://br-cienciadedados.medium.com/projeto-de-machine-learning-ii-9c889faec8df), o qual descreve o passo a passo
do desenvolvimento do modelo de machine learning. As descrições vão desde a limpeza dos dados até à análise do desempenho dos modelos e a seleção do melhor.''')
st.sidebar.title('Menu')
pag = st.sidebar.selectbox('Selecione a página', ['Interagir com a inteligência', 'Sobre o projeto', 'Dashboard da base de dados do projeto'])

st.sidebar.markdown('Feito por : Bruno Rodrigues Carloto')

st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/bruno-rodrigues-carloto)")
st.sidebar.markdown("- [Medium](https://br-cienciadedados.medium.com)")
st.sidebar.markdown("- [Github](https://github.com/brunnosjob)")

if pag == 'Interagir com a inteligência':
    
    st.header('Seja bem-vindo ao Good Bank')
    st.subheader('Simulação')
    st.markdown(' ')
    usuario =  st.text_input('Me informe seu nome para termos uma interação melhor.')
    st.markdown(' ')

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
            st.write('{}, sua solicitação de empréstimo no valor R$ {} foi aprovada. Parabéns!'.format(usuario, emprestimo))
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
    st.markdown('''Esse é um projeto de portfólio de Ciência de Dados. Mais especificamente, esse é um projeto de machine learning classificador. 
                O objetivo específico do projeto é o desenvolvimento de um modelo de machine learning eficiente capaz de prever e classificar se um dado cliente,
                ao fazer uma solicitação de empréstimo, irá pagá-lo ou não. Tendo o modelo de machine learning uma alta eficiência, ocorre a redução de inadimplência.''')
    st.markdown('### Contextualização')
    st.markdown('''Suponhamos que o Banco Noronha é um pequeno banco e está com 30% de seus clientes inadimplentes em relação a empréstimo. Isso tem sido ruim para a empresa.
    Os empréstimos são solicitados presencialmente. Dessa forma, a diretoria chegou à conclusão que, com os sistemas atuais, a empresa continuaria tendo esse problema de inadimplência,
    portanto, a solução seria métodos melhores de avaliação de condição de clientes para liberação de empréstimo. Uma das propostas é o pequeno banco se tornar em uma fintech, passando a se chamar Good Bank, e realizar empréstimos automáticos através de aplicativo.
    A liberação de empréstimo seria feita por inteligência artificial e o alcance da empresa seria muito maior. Sendo assim, a empresa iniciou sua transformação e solicitou o desenvolvimento de uma inteligência artificial eficiente para automatizar a liberação ou negação de empréstimo.''')
    st.markdown('##### Qual seria o impacto do meu projeto de machine learning, uma subárea da inteligência artificial, na redução de inadimplência do banco, que passa a ser fintech?')
    st.markdown('''Meu modelo tem uma precisão de 97% em detectar clientes que não pagarão determinados empréstimos, ou seja, a cada 1 mil empréstimos, apenas 30 não pagariam. De 300 a cada 1 mil, cairia para 30 a cada 1 mil.
    Isso é uma redução de 90% da inadimplência.''')
    
    st.markdown('''Uma outra questão a se considerar é que o banco pode negar erradamente empréstimo a um determinado cliente que pagaria um dado empréstimo que ele mesmo solicitou. 
    Isso ocorre quando o sistema de liberação de empréstimo classifica erradamente o cliente como quem não pagará o empréstimo solicitado. Dessa forma, o banco deixa de ganhar por negar empréstimo a quem pagaria o preço pelo uso do mesmo.
    Lidando com a detecção de clientes pagadores, meu modelo tem uma precisão de 98%. Em outras palavras, a cada 1 mil clientes, meu modelo negaria empréstimo erradamente para dois clientes.
    Em termos gerais, meu modelo tem uma acurácia de 98%, ou seja, a cada mil situações, ele acerta 980, errando 20.''')
    
    st.markdown('##### Você pode interagir com o modelo')
    st.markdown('''
    1 - Clique na seta à sua esquerda, na parte superior da tela
    
    2 - No tópico Menu Selecione a Página, selecione a opção Interagir com a Inteligência
   
    3 - Basta passar as informações solicitadas
    ''')
    
elif pag == 'Dashboard da base de dados do projeto':
    st.title('Dashboard da base de dados do projeto')
    st.markdown('### Gráficos da análise exploratória')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    
    photo0 = Image.open('104.png')
    st.image(photo0, use_column_width=True)
    st.markdown('De acordo com o gráfico, banco possui uma clientela consideravelmente diversificada no tocante à renda, quando o intervalo está entre R$ 2 mil e R$ 7 mil.')
    st.markdown(' ')
       
    photo1 = Image.open('105.png')
    st.image(photo1, use_column_width=True)
    st.markdown('Segundo o gráfico, quanto maior o valor do empréstimo, menor a quantidade de clientes adquirindo esses valores.')
    st.markdown(' ')
        

    photo2 = Image.open('106.png')
    st.image(photo2, use_column_width=True)
    st.markdown('Conforme o gráfico, o banco possui uma clientela consideravelmente diversificada em relação à idade, ou seja, não há uma predominância de jovens ou de idosos.')
    st.markdown(' ')


    photo3 = Image.open('107.png')
    st.image(photo3, use_column_width=True)
    st.markdown('Segundo o gráfico, há uma maior quantidade de clientes que cumpriram com suas obrigações, pagando os empréstimos, do que clientes inadimplentes.')
    st.markdown(' ')
 

    photo4 = Image.open('109.png')
    st.image(photo4, use_column_width=True)
    st.markdown('''O gráfico evidencia que, em torno de R$ 2 mil para menos, não houve inadimplência. 
    Dessa forma, pode ser que o modelo venha a ter o comportamento de somente liberar empréstimos para jovens no valor em torno de R$ 2 mil para menos, 
    isso dependendo também da renda.''')
    st.markdown(' ')
       

    photo5 = Image.open('110.png')
    st.image(photo5, use_column_width=True)
    st.markdown('''De acordo com o gráfico, partir de aproximadamente 40 anos, os clientes são pagadores. 
    Não há clientes acima de 40 anos inadimplente. Isso evidencia a tendência à sensibilidade do modelo para com a idade e o valor do empréstimo.''')
    st.markdown(' ')
        
    photo6 = Image.open('111.png')
    st.image(photo6, use_column_width=True)
    st.markdown('''O gráfico evidencia que a relação entre renda e pagamento é de independência, 
    ou seja, há pessoas com renda igual a R$ 2000,00 que pagam seus deveres, como há as que estão inadimplentes, assim como, 
    há pessoas que ganham R$ 7000,00 que pagam seus deveres, como há as que estão inadimplentes. Em outras palavras, a renda não é um fator sensível para definir o pagamento do empréstimo.''')
    st.markdown(' ')
        

    photo7 = Image.open('112.png')
    st.image(photo7, use_column_width=True)
    st.markdown('Conforme o gráfico, a probabilidade de inadimplência entre aproximadamente os 20 anos e os 37 anos é muito maior do que de pagamento.')
    st.markdown(' ')


    photo8 = Image.open('113.png')
    st.image(photo8, use_column_width=True)
    st.markdown('Até aproximadamente R$ 4500,00, a probabilidade de pagamento é maior do que de não pagamento.')
    st.markdown(' ')
      
        
    photo = Image.open('118.png')
    st.image(photo, use_column_width=True)
    st.markdown('''O gráfico evidencia a diversidade de pagadores tanto na renda quanto na idade, porém, 
                evidencia o grupo jovem de inadimplentes, com diferentes rendas, no entanto, com idade inferior a 40 anos.''')
    
    st.markdown(' ')
    st.markdown(' ')
    st.markdown('###### Dashboard by Bruno R. Carloto')
    
