import openai
import streamlit as st
import os

# Configurar clave secreta desde Streamlit Cloud
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Generador Casos de Prueba", layout="centered")
st.title("🧠 Generador Inteligente de Casos de Prueba para Historias Clínicas")

st.markdown("""
Ingresa un requerimiento funcional o cambio en el sistema de historias clínicas. La IA generará automáticamente una tabla con sugerencias de casos de prueba funcionales.
""")

input_text = st.text_area("✍️ Describe el requerimiento o cambio:", height=200)

if st.button("Generar Casos de Prueba") and input_text:
    with st.spinner("Analizando con ChatGPT..."):
        prompt = f"""
Eres un experto en QA. A partir del siguiente requerimiento funcional del sistema de historias clínicas, genera una tabla con al menos 3 casos de prueba. Cada caso debe incluir: pasos detallados, datos de entrada y resultado esperado.

Requerimiento: {input_text}

Formato:
1. Caso #
- Pasos:
- Datos:
- Resultado Esperado:
"""

        respuesta = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=700
        )

        resultado = respuesta.choices[0].message.content

        st.markdown("### 📋 Casos de Prueba Sugeridos")
        st.text_area("Resultado generado:", resultado, height=300)
        st.download_button("📥 Descargar como TXT", resultado, file_name="casos_prueba.txt")
