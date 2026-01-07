from dotenv import load_dotenv
load_dotenv()

from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS


def extract_documents_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    documents = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            documents.append(
                Document(
                    page_content=text,
                    metadata={"page": page_num}
                )
            )

    return documents

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    return splitter.split_documents(documents)

def create_faiss_index(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index")

def ask_question(question: str):
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = f"""
    Answer the question using ONLY the context below.
    If the answer is not in the context, say "I don't know".

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    sources = sorted(set(doc.metadata["page"] for doc in docs))

    return response.content, sources