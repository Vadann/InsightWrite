from datetime import datetime

class journalEntry:
    #called when retrieving data from database
    def __init__(self, jID:int, uID:int, tID:int, t:str, ed:str, 
                 lmd:str, c:str, f:str, clr:str):
            self.journal_id = jID
            self.user_id = uID
            self.tag_id = tID
            self.title = t
            self.entry_date = ed
            self.last_modified_date = lmd
            self.content = c
            self.font = f
            self.color = clr
    #called on journal entry creation
    def __init__(self, uID: int, tID:int, t:str):
        self.journal_id = -1 #should equal journal entry db size
        self.user_id = uID #should equal user_id of user that created it
        self.tag_id = 0 #0 = no tag
        self.title = t
        self.entry_date = str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year)
        self.last_modified_date = str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year)
        self.content = 'Type here...'
        self.font = 'Arial'
        self.color = 'Black'
    #called when user sets tag
    def tagID(self, tID:int): 
        self.tag_id = tID
    def setTitle(self, t:str):
        self.title = t
    #both below called when user saves journal entry, or autosave triggers
    def setModDate(self, lmd:str):
        self.last_modified_date = str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year)
    def setContent(self, txt:str):
        self.content = txt
    def setFont(self, f:str):
        self.font = f
    def setColor(self, c:str):
        self.color = c