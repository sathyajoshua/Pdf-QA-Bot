**📄 PDF Q&A Bot (RAG-based)**

An AI-powered application that allows users to upload PDF documents and ask questions.
The system answers strictly from the document content and provides source references (page numbers) for transparency.



**🚀 Features**

- Upload any PDF file
- Extracts and chunks text automatically
- Uses embeddings + FAISS for semantic search
- Answers questions using OpenAI LLM
- Shows source page numbers for every answer
- Simple and clean Streamlit UI
- No hallucinations (answers only from PDF)


**🛠 Tech Stack**

- Python
- OpenAI API
- LangChain
- FAISS
- Streamlit

**📂 Project Structure**
pdf_qa_bot/
│
├── app.py              
├── utils.py            
├── requirements.txt
├── README.md
└── .env.example


**⚙️ Setup Instructions (Local)**
1️⃣ Clone the repository
git clone https://github.com/your-username/pdf-qa-bot.git
cd pdf-qa-bot

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key

5️⃣ Run the app
streamlit run app.py

**🌐 Deployment**

This app is deployable on Streamlit Cloud with zero backend setup.

**📌 Use Cases**

- Internal company document Q&A
- Policy / SOP assistants
- Research paper analysis
- Legal or compliance documents
- Client knowledge base bots

**👨‍💻 Author**

**Sathya Joshua**
AI Engineer | Python | RAG Systems | Freelance Developer

💡 This project is designed to be lightweight, reliable, and easily customizable for client needs.
