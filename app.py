import validators
import streamlit as st

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_groq import ChatGroq
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# Streamlit App
st.set_page_config(
    page_title="LangChain: Summarize Text From YT or Website",
    page_icon="📄"
)

st.title("LangChain: Summarize Text from YT or Website")
st.subheader("Summarize URL")

# Sidebar
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

prompt_template = """
Provide a concise and informative summary (max 300 words) of the following content:
{context}
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context"]
)

if st.button("Summarize the content from YT or Website"):

    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide both Groq API Key and URL")

    elif not validators.url(generic_url):
        st.error("Please enter a valid URL")

    else:
        try:
            with st.spinner("Fetching and summarizing content..."):

                # ✅ Create LLM ONLY after API key is provided
                llm = ChatGroq(
                    model_name="llama-3.1-8b-instant",
                    groq_api_key=groq_api_key
                )

                chain = create_stuff_documents_chain(llm, prompt)

                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(
                        generic_url,
                        add_video_info=True
                    )
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                    )

                docs = loader.load()
                summary = chain.invoke({"context": docs})

                st.success(summary)

        except Exception as e:
            st.exception(e)
