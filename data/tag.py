class tag: #potentially just porting it to journalEntry with 
            #tag_name and tag_color
    def __init__(tID:int, jID:int, n:str, c:str):
        tag_ID = tID
        journal_ID = jID #same as the ID of the entry it is assigned to
        tag_name = n
        tag_color = c
    def setTagName(n:str):
        tag_name = n
    def setTagColor(c:str):
        tag_color = c