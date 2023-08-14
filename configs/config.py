import os
from pathlib import Path

MAIN_DIRECTORY = os.path.dirname(os.getcwd())
print(MAIN_DIRECTORY)

KEY_FILE = 'api-secret.json'
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = os.path.join(MAIN_DIRECTORY, 'ga3-download-data/api-key', KEY_FILE)
VIEW_ID = 'ga:0000000' #Replace with your own view ID
START_DATE = '2022-01-01' #Replace with your own start date
END_DATE = '2022-12-31' #Replace with your own end date
PAGE_SIZE = 1000 #Replace with your own page size, max is 100000
PAGE_TOKEN = "0" #This is the pagination value, you can leave it as it is, the app will make the pagination for you.
#If you want to pass the correct name of the goals, change the value of the specific goal to the correct name you want. i.e. 'ga:goal1Completions': 'goal1Completions' to 'ga:goal1Completions': 'Purchase'
goals_names = {
    'ga:goal1Completions': 'goal1Completions',
    'ga:goal2Completions': 'goal2Completions',
    'ga:goal3Completions': 'goal3Completions',
    'ga:goal4Completions': 'goal4Completions',
    'ga:goal5Completions': 'goal5Completions',
    'ga:goal6Completions': 'goal6Completions',
    'ga:goal7Completions': 'goal7Completions',
    'ga:goal8Completions': 'goal8Completions',
    'ga:goal9Completions': 'goal9Completions',
    'ga:goal10Completions': 'goal10Completions',
    'ga:goal11Completions': 'goal11Completions',
    'ga:goal12Completions': 'goal12Completions',
    'ga:goal13Completions': 'goal13Completions',
    'ga:goal14Completions': 'goal14Completions',
    'ga:goal15Completions': 'goal15Completions',
    'ga:goal16Completions': 'goal16Completions',
    'ga:goal17Completions': 'goal17Completions',
    'ga:goal18Completions': 'goal18Completions',
    'ga:goal19Completions': 'goal19Completions',
    'ga:goal20Completions': 'goal20Completions',
    'ga:goalCompletionsAll': 'goalCompletionsAll'
} 