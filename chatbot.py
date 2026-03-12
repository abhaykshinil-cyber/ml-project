import anthropic

client = anthropic.Anthropic()
messages = []

print("Claude Chatbot (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() in ("quit", "exit"):
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    print("Claude: ", end="", flush=True)
    with client.messages.stream(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=messages,
    ) as stream:
        response_text = ""
        for text in stream.text_stream:
            print(text, end="", flush=True)
            response_text += text

    print()
    messages.append({"role": "assistant", "content": response_text})
