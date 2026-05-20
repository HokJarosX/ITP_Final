from abc import ABC, abstractmethod

class Filter(ABC):
    def __init__(self, transcriptions = None, goal = ""):
        self._transcriptions = transcriptions or []
        self._goal = goal

    @abstractmethod
    def apply(self):
        pass



class FilterCategory(Filter):
    def __init__(self, transcriptions = None, goal = ""):
        super().__init__(transcriptions, goal)

    def apply(self):
        result = []
        for transcription in self._transcriptions:
            if transcription.getCategory() == self._goal:
                result.append(transcription)
        return result