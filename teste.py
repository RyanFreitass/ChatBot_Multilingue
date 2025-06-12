import google.generativeai as genai



API_KEY = \
"AIzaSyA-l_NXJHAOCqbO4SkWIEgtWCpS7LOSfF8"




genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

chat = model.start_chat()



while True:

    userInput = input("You : ")

    if userInput.lower() == "exit":

        break

    response = chat.send_message(userInput)

    print("Chatbot: ", response.text)