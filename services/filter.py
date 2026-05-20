class filter():
    def __init__(self, goal = "", transcriptions = None, where = ""):
        self._goal = goal
        self._transcription = transcriptions
        self._where = where

    def apply(self):
        result = []
        for transcription in self._transcription:
            if getattr(transcription, self._where) == self._goal:
                result.append(transcription)
        return result

class filterCategory(filter):
    def __init__(self, goal = "", transcriptions = None):
        super().__init__(goal, transcriptions, where = "_category")