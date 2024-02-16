import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

import streamlit as st

# Chargement des données
lemmatizer = WordNetLemmatizer()
with open('../source/intents.json', 'r') as file:
    intents = json.load(file)

words = pickle.load(open('../Linux/data_processor/words.pkl', 'rb'))
classes = pickle.load(open('../Linux/data_processor/classes.pkl', 'rb'))
model = load_model('../Linux/data_processor/chatbot_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probabilty': str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


def main():
    st.title('Chatbot with Streamlit')

    # Chat interface
    user_input = st.text_input('You: ', key='user_input')

    # Track message history
    message_history = []

    if st.button('Send'):
        if user_input.lower() in ["good bye", "bye", "quit"]:
            st.text("Chatbot: See you later !")
            message_history.append(("You", user_input))
        else:
            # Add user message to history
            message_history.append(("You", user_input))

            # Predict and respond
            ints = predict_class(user_input)
            res = get_response(ints, intents)

            # Add chatbot response to history
            message_history.append(("Chatbot", res))

    # Display messages
    for sender, message in message_history:
        if sender == "You":
            st.text_input("You:", message, key=message)
        else:
            st.text_input("Chatbot:", message, key=message)


if __name__ == '__main__':
    main()
