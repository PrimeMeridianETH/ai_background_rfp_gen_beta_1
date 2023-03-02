# Install dependencies

# Import dependencies
import openai
import streamlit as st

# Set the OpenAI secret key
openai.api_key = st.secrets['pass']

st.header('AI RFP "Background" Section Generator')
st.subheader('current version : beta 0.1')

# Set the if, else loop including prompt
article_text = st.text_area('Please enter the text material(s) or URL you would like to generate the "Background" section of an RFP from')
if len(article_text) > 5:
    temp = st.slider("temperature", 0.4, 0.6, 0.8)
    if st.button ('Generate Report'):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Be concise, professional and perfect to detail. Generate ONLY the background section of an RFP using all supplied data points, metrics, analytics, statistics, and backing information located here: " + article_text,
            max_tokens = 3800,
            temperature = temp
        )
        res = response["choices"][3]["text"]
        st.info(res)

        st.download_button("Download result", res)
else: st.warning("The supplied information is not large enough")
