import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    database = 'railway',
    user = 'postgres',
    password = 'SYydOpWeEquRsAJbFJGHuGGSsLjoZYuO',
    host = 'roundhouse.proxy.rlwy.net',
    port = '21286',
)

class userSettings:
    def formatDate(self, month:str, day:str, year:str):
        convert = {
            'january': '01',
            'february': '02',
            'march': '03',
            'april': '04',
            'may': '05',
            'june': '06',
            'july': '07',
            'august': '08',
            'september': '09',
            'october': '10',
            'november': '11',
            'december': '12'
            }
        try:
            m = convert[month.lower()]
            return m + "/" + day + "/" + year
        except:
            raise ValueError('Not a month')

    #called when retrieving data from database
    def __init__(self, id:int, u:str, e:str, v:bool, p:str, d:str, 
                 nF:str, nL:str, b:str, t:bool, n:bool, a:bool, m:bool):
        self.user_id = id
        self.username = u
        self.email = e
        self.verifiedEmail = v
        self.password = p
        self.account_created_date = d
        self.firstName = nF
        self.lastName = nL
        self.birthday = b
        self.theme = t
        self.notifications = n
        self.analytics = a
        self.meditation_tab = m
    #called on account creation
    def __init__(self, u:str, e:str, p:str):
        self.user_id = -1 #should equal userSettings database size
        self.username = u
        self.email = e
        self.verifiedEmail = False
        self.password = p
        self.account_created_date = str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year)
        self.firstName = 'Not Registered'
        self.lastName = 'Not Registered'
        self.birthday = 'Not Registered'
        self.theme = True #true for day mode, false for night mode.
        self.notifications = True
        self.analytics = True
        self.meditation_tab = True
    def setPassword(self, p:str): 
        self.password = p
    #called once frontend confirms verification
    def verifyEmail(self): 
        self.verifiedEmail = True
    #all below called once "saved" is clicked on settings webpage
    def setNames(self, nF:str, nL:str):
        self.firstName = nF
        self.lastName = nL
    def setBirthday(self, month:str, day:str, year:str):
        self.birthday = self.formatDate(month, day, year)
    def setTheme(self, t:bool):
        self.theme = t
    def setNotifications(self, n:bool):
        self.notifications = n
    def setAnalytics(self, a:bool):
        self.analytics = a
    def setMeditation(self, m:bool):
        self.meditation_tab = m