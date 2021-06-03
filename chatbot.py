import random

zufallsantworten = ["oh wirklich. . .", "Interresant", "Das kann man so shen.", "Ich verstehe"]
reaktionen =   {"hallo": "aber Hallo",
		"geht": "Was verstehst du darunter",
		"schmeckt": "Ich habe keinen Geschmackssinn"}

print("Willkommen beim Chatbot (v1)")
print("Worueber wollen Sie srechen")
print("Zum Beenden geben Sie bye ein")
print("")

nutzereingabe = ""
	while nutzereingabe != "bye":
		nutzereingabe = ""
		while nutzereingabe == "":
			nutzereingabe = input("Ihre Frage oder Antwort: ")

		nutzereingabe = nutzereingabe.lower()
		nutzerwoerter = nutzereingabe.split()

	intelligentAntworten = False
	for einzelwoerter in nutzerwoerter:
		if einzelwoerter in reaktionen:
			print(reaktionen[einzelwoerter])
			intelligentAntworten = True
	if not intelligentAntworten:
		print(random.choice(zufallsantworten))
print("einen schoenen Tag.")
