import google.generativeai as genai
from semantic_kernel import Kernel
from agents.technical_agent import handle_technical_query
from agents.billing_agent import handle_billing_query
from utils.document_loader import extract_text_from_pdf
from utils.hybrid_search import HybridSearch

# --- Config ---
genai.configure(api_key="YOUR_GEMINI_API_KEY")
kernel = Kernel()
kernel.add_text_completion_service("gemini", genai.GenerativeModel("gemini-pro"))
kernel.register_semantic_function("TechnicalSupport", "You are a technical support agent... respond in detail.")
kernel.register_semantic_function("BillingSupport", "You are a billing support agent... respond clearly.")

# --- Data Load ---
tech_text = extract_text_from_pdf("technical_doc.pdf")
biz_text = extract_text_from_pdf("business_doc.pdf")

tech_search = HybridSearch(tech_text.split("\n"))
biz_search = HybridSearch(biz_text.split("\n"))

# --- Input ---
query = input("Enter your query: ")
if any(word in query.lower() for word in ["payment", "invoice", "charge"]):
    context = {"docs": "\n".join(biz_search.search(query))}
    print(handle_billing_query(kernel, query, context))
else:
    context = {"docs": "\n".join(tech_search.search(query))}
    print(handle_technical_query(kernel, query, context))
