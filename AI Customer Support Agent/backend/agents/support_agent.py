from backend.tools.knowledge_base import knowledge_base

def detect_intent(query: str):
    query = query.lower()

    for intent, data in knowledge_base.items():
        for keyword in data["keywords"]:
            if keyword in query:
                return intent

    return "unknown"


def run_support_agent(query: str):
    intent = detect_intent(query)

    if intent == "unknown":
        return """
❓ Sorry, I couldn't understand your issue.

Please contact support@example.com for help.
"""

    return knowledge_base[intent]["response"]