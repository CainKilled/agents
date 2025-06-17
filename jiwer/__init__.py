class _Identity:
    def __call__(self, text):
        return text

ToLowerCase = ExpandCommonEnglishContractions = RemoveKaldiNonWords = RemoveWhiteSpace = RemoveMultipleSpaces = Strip = ReduceToSingleSentence = ReduceToListOfListOfWords = _Identity()

class Compose(list):
    def __call__(self, text):
        for t in self:
            text = t(text)
        return text

def wer(ref, hyp, reference_transform=None, hypothesis_transform=None):
    return 0.0
