from semantic_kernel import Kernel

def handle_technical_query(kernel: Kernel, query: str, context: dict):
    return kernel.invoke("TechnicalSupport", query=query, context_vars=context)
