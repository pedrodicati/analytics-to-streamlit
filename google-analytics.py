import streamlit as st

# Cabeçalho do aplicativo
st.header("Análise do Usuário")

# Obter a entrada do usuário
idade = st.number_input("Digite sua idade:")
sexo = st.selectbox("Selecione seu sexo:", options=["Masculino", "Feminino"])

# Realizar análise básica
if idade < 18:
    st.write("Você é menor de idade.")
else:
    st.write("Você é maior de idade.")
    
if sexo == "Masculino":
    st.write("Você é do sexo masculino.")
else:
    st.write("Você é do sexo feminino.")