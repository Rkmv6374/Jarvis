from chatbot import Chat, register_call
import wikipedia

@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query)
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple options, return the summary of the first option
        return wikipedia.summary(e.options[0])
    except Exception:
        return "I don't know about " + query

def main():
    chatbot = Chat()

    first_question = "Hi, how are you?"
    while True:
        response = chatbot.converse(first_question)
        # print("Chatbot:", response)
        user_input =
        first_question = chatbot.converse(user_input)
        # print(first_question)

if __name__ == "__main__":
    main()
