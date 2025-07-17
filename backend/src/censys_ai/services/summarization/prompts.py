DATASET_PROMPT_TEMPLATE = """
You are an expert cybersecurity analyst. Summarize the following Censys {dataset_type} dataset, 
highlighting key insights, risks, and notable findings.\n\n
DATASET:\n{dataset}\n\n
Return a concise summary suitable for a technical security report.
"""

MULTIPLE_DATASET_PROMPT_TEMPLATE = """
You are an expert cybersecurity analyst. Summarize the following Censys datasets, 
highlighting key insights, risks, and notable findings.\n\n

HOST DATASET:\n{hosts_dataset}\n\n

WEB PROPERTY DATASET:\n{web_property_dataset}\n\n

CERTIFICATE DATASET:\n{certificate_dataset}\n\n

Return a concise summary suitable for a technical security report.
"""
