import streamlit as st
from langchain import PromptTemplate
from langchain_community.llms import OpenAI
template = """
	Below is an email that may be poorly worded.
	Your goal is to:
	- Properly format the email
	- Convert the input text to a specified tone
	- Convert the input text to a specified dialect

	Here are some examples of different Tones:
	- Formal : We went to Barcelona for the weekend. We have a lot of things to tell.
	- Informal : Went to Barcelona for the weekend. Lots to tell you/

	Here are some examples of words in different dialects:
	- American English: French Fries, cotton candy, apartment, garbage, cookie
	- British English: chips, candyfloss, flag, rubbish, biscuit, green fingers
	
	Below is the tone, email and dialect:
	TONE:{tone}
	DIALECT:{dialect}
	EMAIL:{email}

	YOUR RESPONSE:
"""
prompt = PromptTemplate(
	input_variables=["tone","dialect","email"],
	template=template,
	)

def load_LLM():
	"""Logic for loading the chain you want to use should go here"""
	llm = OpenAI(temperature=.5)
	return llm

llm = load_LLM()

st.set_page_config(page_title="Globalize Email",page_icon=":robot:")
st.header("OpenAI Langchain App")

col1,col2 = st.columns(2)

with col1:
	st.markdown("This app will help to improve your email using OpenAI + Langchain")
with col2: 
	st.markdown("Let us know if this really helped you at abc@gmail.com")


st.markdown("## Enter your email content to convert here")

col1,col2 = st.columns(2)

with col1:
	option_tone = st.selectbox(
	'Which tone would you like your email to have?',
	('Formal','Informal'))

with col2: 
	option_dialect = st.selectbox(
	'Which English Dialect would you like?',
	('Americal English','British English'))

def get_text():
	input_text = st.text_area(label="", placeholder="Your email...",key="email_input")
	return input_text
email_input = get_text()

st.markdown("## Your Converted email:")

if email_input:
	prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect,email=email_input)
	
	formatted_email = llm(prompt_with_email)

	st.write(formatted_email)
