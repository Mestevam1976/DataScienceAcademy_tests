#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios Cap02

# In[2]:


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista_01 = [1,2,3,4,5,6,7,8,9,10]
print(lista_01)


# In[3]:


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista_02 = [12, 'objetos', '10', True, 4+2]
print(lista_02)


# In[4]:


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string_01 = 'Márcio '
string_02 = 'Estevam'
string_03 = string_01 + string_02
print(string_03)


# In[11]:


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla_01 = (1,2,2,3,4,4,4,5)

print(tupla_01.count(4))


# In[12]:


# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict_01 = {}
dict_01


# In[13]:


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict_02 = {'key_01': 1, 'key_02': 2, 'key_03': 3}
dict_02


# In[18]:


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dict_02['key_04'] = 4
dict_02


# In[20]:


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dict_03 = {'lista_01':[1,2], 'key_05': 5, 'key_06': 6}
dict_03


# In[21]:


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

lista_03 = ['texto_01', (23, 'gama'), {'key_07': 7, 'key_08': 8}, 3.14]
lista_03


# In[23]:


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
         
frase[0:18]


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>

# Parabéns se você chegou até aqui. Use o voucher PYTHONDSA9642 para comprar qualquer curso ou Formação da DSA com 5% de desconto.
