class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                linea_pulita = line.strip()
                self._dict.append(linea_pulita)

    def printAll(self):
        for i in self._dict:
            print(i)


    @property
    def dict(self):
        return self._dict