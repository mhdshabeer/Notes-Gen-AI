import ollama

def generate_notes(text):
    """Processes extracted text using DeepSeek LLM and returns structured study notes."""
    prompt = f"""
    You are an AI assistant that converts lecture slides into structured study notes.
    Given the extracted text, summarize the key points, highlight important concepts,
    and organize the information using headings, bullet points, and subheadings.

    Here is the extracted content:

    {text}

    Generate structured notes:
    """

    response = ollama.chat(model="deepseek", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

