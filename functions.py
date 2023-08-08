from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import csv
from datetime import datetime
from config import *
import os

def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics


def get_report(analytics, reportRequests):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(body=reportRequests).execute()


def download_csv(response, num, reportRequest, filename):
  # Create a CSV file
  view = VIEW_ID.split(':')[1] + filename #change this to change the name of the file you want to save
  fileformat = '.csv'
  fieldnames = []
  
  #Create a folder to save the csv files
  folder_path = "csv/" + VIEW_ID.split(':')[1]
  if os.path.exists(folder_path) == False:
    os.mkdir(folder_path)

  with open('csv/' + VIEW_ID.split(':')[1] + '/' + view + '-' + START_DATE + ' to ' + END_DATE + '-' + str(num) + '-' + str(PAGE_TOKEN) + fileformat, 'w', newline='') as file:
    for headers in reportRequest['reportRequests'][0]['dimensions']:
      fieldnames.append(headers['name'].replace('ga:', ''))

    for headers in reportRequest['reportRequests'][0]['metrics']:
      if 'Completions' in headers['expression']: 
        head = headers['expression']    
        fieldnames.append(goals_names[head])
      else:
        fieldnames.append(headers['expression'].replace('ga:', ''))
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in response:
      date_format = "%Y%m%d"
      date_string = row['dimensions'][0]
      try:       
        parsed_date = datetime.strptime(date_string, date_format).date()
      except ValueError:
        parsed_date = date_string

      fn = 0
      i = 0 
      row_to_write = {}

      while i < len(row['dimensions']):
        if  fieldnames[fn] == 'date':
          row_to_write[fieldnames[fn]] = parsed_date
        else:
          the_row = row['dimensions'][i]
          row_to_write[fieldnames[fn]] = the_row.encode('UTF-8',errors='strict')
        i += 1
        fn += 1        

      i = 0
      while i < len(row['metrics'][0]['values']):
        the_row = row['metrics'][0]['values'][i]
        row_to_write[fieldnames[fn]] = the_row
        i += 1
        fn += 1
        
      writer.writerow(row_to_write)