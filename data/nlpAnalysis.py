class nlpAnalysis:
    def __init__(self, nID:int, jID:int, s:int, k:str, t:str):
        self.nlp_ID = nID
        self.journal_ID = jID
        self.sentiment_score = s
        self.keywords = k
        self.tokens = t