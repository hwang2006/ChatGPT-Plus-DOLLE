import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]


st.title("ChatGPT Plus Dall-E")

#user_input = st.text_input("Prompt")

with st.form("form"):
    user_input = st.text_input("Prompt")
    size = st.selectbox("Size", ["1024x1024", "512x512","256x256"])
    submit = st.form_submit_button("Submit")

if submit and user_input:
    #st.write(user_input)
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail appeareance of the input. Response it shortly."
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Waiting for ChatGPT..."):
        get_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = gpt_prompt
        )

    prompt = get_response["choices"][0]["message"]["content"]
    st.write(prompt)


    with st.spinner("Waiting for DALL-E..."):
        dolle_response = openai.Image.create(
            prompt = prompt,
            size = size
        )
    st.image(dolle_response["data"][0]["url"])