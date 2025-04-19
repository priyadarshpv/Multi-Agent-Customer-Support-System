# Multi-Agent Customer Support System using Semantic Kernel and Gemini API

This project implements an intelligent, multi-agent customer support system capable of handling both technical and billing-related queries. It leverages document understanding, semantic search, and LLM-powered response generation using Google Gemini and Semantic Kernel.

---

## 🧠 Key Features

- 🤖 **Multi-Agent Support**:
  - Technical Support Agent
  - Billing Support Agent

- 📄 **PDF Document Parsing**:
  - Extracts and indexes sections from technical/business PDFs.

- 🔍 **Semantic + Keyword Search**:
  - Hybrid approach using `SentenceTransformer` and keyword scoring.

- 💬 **LLM-Driven Response Generation**:
  - Contextual responses from Gemini (1.5 Flash) via Semantic Kernel.

---

## 🔧 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-agent-support-system.git
cd multi-agent-support-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your PDF Files

Place your technical and business PDF documents in the desired directory and update the paths in `main.py`.

### 4. Configure API Key

Replace your Gemini API key in the line:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

---

## 🚀 Run the Project

```bash
python main.py
```

---

## 📁 File Structure

```
.
├── main.py                  # Main application logic
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

---

## ✨ Sample Queries

- "How to handle 5GB file uploads?"
- "Duplicate charge of $199 on invoice #12345"
- "Dashboard widgets not loading"
- "Payment status shows pending after 48 hours"

---

## 📜 License

This project is licensed under the MIT License.
```

