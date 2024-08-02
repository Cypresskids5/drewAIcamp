import requests
import aicamp_day1


from huggingface_hub import InferenceClient

client = InferenceClient(
    "mistralai/Mistral-7B-Instruct-v0.3",
    token="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",
)

for message in client.chat_completion(
	messages=[{"role": "user", "content": "What is the capital of France?"}],
	max_tokens=500,
	stream=True,
):
    print(message.choices[0].delta.content, end="")

result = aicamp_day1.make_text(output)
print(result)