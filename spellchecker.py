import time

import dictionary
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._md = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        frase_pulita = replaceChars(txtIn)
        parole = frase_pulita.split(" ")

        tempo_di_inizio = time.time()
        risultati = self._md.searchWord(parole, language)
        tempo_di_fine = time.time()

        #analisi dei risultati
        errori = 0
        print("\n--- Risultati (Using contains) ---")
        for parola_rich in risultati:
            if not parola_rich.corretta:
                print(parola_rich)
                errori += 1

        print(f"Numero di parole errate: {errori}")
        print(f"Time elapsed: {tempo_di_fine - tempo_di_inizio}")
        print("----------------------------------\n")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    text = text.lower()
    chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Sostituiamo ogni carattere speciale con una stringa vuota
    for c in chars:
        text = text.replace(c, "")

    return text