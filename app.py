# Requisitos: pip install openai streamlit

import openai
import streamlit as st

# Configura tu clave API en Streamlit Cloud usando st.secrets
# En local puedes usar: openai.api_key = "TU_API_KEY"
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Configuración de la página
st.set_page_config(page_title="Generador de Casos de Prueba con ChatGPT", layout="centered")
st.title("🧠 Generador Inteligente de Casos de Prueba para Historias Clínicas")

st.markdown("""
Ingresa una descripción de requerimiento o cambio solicitado por el cliente, y la IA (ChatGPT) generará automáticamente una tabla con sugerencias de casos de prueba funcionales.
""")

# Entrada de texto
input_text = st.text_area("✍️ Describe el requerimiento o cambio solicitado:", height=200)

# Botón para generar casos de prueba
if st.button("Generar Casos de Prueba") and input_text:
    with st.spinner("Analizando con ChatGPT..."):
        prompt = f"""
Eres un experto en QA. A partir del siguiente requerimiento funcional del sistema de historias clínicas, genera una tabla de al menos 3 casos de prueba. Cada caso debe incluir: paso a paso, datos de entrada y resultado esperado.

Requerimiento: {input_text}

Formato:
1. Caso #
- Pasos:
- Datos:
- Resultado Esperado:
"""

        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=700
        )

        resultado = respuesta.choices[0].message.content

        st.markdown("### 📋 Casos de Prueba Sugeridos")
        st.text_area("Resultado generado:", resultado, height=300)
        st.download_button("Descargar resultado como TXT", resultado, file_name="casos_prueba.txt")
