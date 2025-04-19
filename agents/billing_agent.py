from semantic_kernel import Kernel

def handle_billing_query(kernel: Kernel, query: str, context: dict):
    return kernel.invoke("BillingSupport", query=query, context_vars=context)
