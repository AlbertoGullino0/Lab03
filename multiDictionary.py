import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self) -> None:
        #Qua mi serve per inizializzare i 3 dizionari
       self.diz_ita = d.Dictionary()
       self.diz_eng = d.Dictionary()
       self.diz_spa = d.Dictionary()

        #Qui carico i vari dizionari, così da semplificare la ricerca successiva
       self.diz_ita.loadDictionary("resources/Italian.txt")
       self.diz_eng.loadDictionary("resources/English.txt")
       self.diz_spa.loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        if language == "english":
            dizionario = self.diz_eng.dict
        elif language == "italian":
            dizionario = self.diz_ita.dict
        elif language == "spanish":
            dizionario = self.diz_spa.dict

        risultati = []

        for parola in words:
        #creo richword, ovvero una parola che ha anche la carratteristica corretta o errata
            rw_obj = rw.RichWord(parola)
            if parola in dizionario:
                rw_obj.corretta = True
            else:
                rw_obj.corretta = False
            risultati.append(rw_obj)

        return risultati



