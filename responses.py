import aiohttp  # vajalik hilisemaks
import random

nimekiri = ["Hästi", "halvasti", ":(,", "mega hästi"]

# Funktsioon, mis hakkab kasutajate sõnumeid käsitlema
async def handle_response(message) -> str:
    # Teeme iga sõnumi väiketäheliseks, et endal oleks kergem
    message = message.lower()

    # Kui sõnum oli !abi, saadame kasutajale vastuse
    if message == "hi":
        return "YOOOOOOOOOOOO What's Up ;D"

    elif message == "kuidas läheb":
        return nimekiri [random.randint(0,3)]

    elif message == "kes sa oled":
        return "The newest ducky pro max model"

# GPT osa (responses.py sisse)
    if message[:3] == "gpt":
        api_key = "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"
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system",
                 "content": "Vasta kui kass. Inglise keeles."},  # mis stiilis bot teile vastama peaks
                {"role": "user", "content": message[4:]}
            ]
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status:
                    response_data = await response.json()
                    return response_data["choices"][0]["message"]["content"]
                else:
                    return f"Error: {response.status}"
