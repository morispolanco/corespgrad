import gradio as gr
import openai

# Configura tu clave de API de OpenAI
openai.api_key = "TU_CLAVE_DE_API_DE_OPENAI"

# Función para corregir el texto utilizando GPT-3
def corregir_texto(texto):
    # Llama a la API de OpenAI para obtener la corrección del texto
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=texto,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )
    # Obtiene la respuesta generada por GPT-3
    correccion = respuesta.choices[0].text.strip()
    return correccion

# Interfaz de Gradio
def interfaz():
    texto_input = gr.inputs.Textbox(label="Texto a corregir")
    texto_output = gr.outputs.Textbox(label="Texto corregido")

    gr.Interface(
        fn=corregir_texto,
        inputs=texto_input,
        outputs=texto_output,
        title="Corrección de Texto en Español",
        description="Esta aplicación utiliza GPT-3 para corregir textos en español.",
        theme="default"
    ).launch()

# Ejecuta la interfaz de Gradio
interfaz()
