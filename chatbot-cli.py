#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from chatbot import chatbot


def main():
    # listen
    zufallsantworten = ["oh wirklich...",
                        "Interessant",
                        "das kann man so sehen",
                        "ich verstehe"]
    reaktionen = {"hallo": "aber hallo", " geht": "was verstehst du darunter", "schmeckt es": "ich habe keinen Geschmackssinn."}

    # Ausgabe Begrüßung
    print("willkommen beim Chatbot (v2)")
    print("zum Beenden geben Sie bye ein")
    print("worüber wollen Sie sprechen")
    print("")

    # Chatbot-Objekt
    bot = chatbot(reaktionen, zufallsantworten)

    # Logik
    nutzereingabe = ""
    while nutzereingabe != "bye":
        nutzereingabe = ""
        while nutzereingabe == "":
            nutzereingabe = input("Ihre Frage oder Antwort: ")
        if nutzereingabe == "bye":
            break
        bot.set_Message(nutzereingabe)
        print(bot.get_Response())

    # Ausgabe Verabschiedung
    print("Bis zum nächsten Mal")


main()
