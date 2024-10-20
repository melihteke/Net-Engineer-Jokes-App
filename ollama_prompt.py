import ollama

def ask_ollama(prompt_content):
    stream = ollama.chat(
        model='llama3:latest',
        messages=[{'role': 'user', 'content': f'{prompt_content}'}],
        stream=True,
    )

    full_answer = []
    for chunk in stream:
        full_answer.append(chunk['message']['content'])

    return ''.join(full_answer)
