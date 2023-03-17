import streamlit as st

st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-72GDV7JH3D"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-72GDV7JH3D');
</script>
""", unsafe_allow_html=True)

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