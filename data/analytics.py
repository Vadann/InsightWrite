class analytics:
    def __init__(self, aID: int, uID:int, days:int, pKEY:str, 
                 nKEY:str, d:str, m:int):
        self.analytics_id = aID
        self.user_id = uID
        self.days_of_journaling = int
        self.positive_keywords = pKEY
        self.negative_keywords = nKEY
        self.date_window_weekly = d
        self.mood = m
