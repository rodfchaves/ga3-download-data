from config import *
from functions import *

FILENAME = '-system-'

reportRequestOne={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:sessions'}, 
                  {'expression': 'ga:users'}, 
                  {'expression': 'ga:newUsers'}, 
                  {'expression': 'ga:bounces'}, 
                  {'expression': 'ga:sessionDuration'},
                  {'expression': 'ga:goal1Completions'},
                  {'expression': 'ga:goal2Completions'},
                  {'expression': 'ga:goal3Completions'},
                  {'expression': 'ga:goalCompletionsAll'}, 
                  {'expression': 'ga:goalValueAll'}
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                    {'name': 'ga:screenResolution'}
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}


reportRequestTwo={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:goal4Completions'},
                  {'expression': 'ga:goal5Completions'},
                  {'expression': 'ga:goal6Completions'},
                  {'expression': 'ga:goal7Completions'},
                  {'expression': 'ga:goal8Completions'},
                  {'expression': 'ga:goal9Completions'},
                  {'expression': 'ga:goal10Completions'},
                  {'expression': 'ga:goal11Completions'},
                  {'expression': 'ga:goal12Completions'},
                  {'expression': 'ga:goal13Completions'}
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                    {'name': 'ga:screenResolution'}  
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}
  

reportRequestThree={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [

                  {'expression': 'ga:goal14Completions'},
                  {'expression': 'ga:goal15Completions'},
                  {'expression': 'ga:goal16Completions'},
                  {'expression': 'ga:goal17Completions'},
                  {'expression': 'ga:goal18Completions'},
                  {'expression': 'ga:goal19Completions'},
                  {'expression': 'ga:goal20Completions'},
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                    {'name': 'ga:screenResolution'}  
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestFour={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:transactions'},
                  {'expression': 'ga:transactionRevenue'},
                  {'expression': 'ga:transactionShipping'},
                  {'expression': 'ga:transactionTax'},
                  {'expression': 'ga:totalValue'},
                  {'expression': 'ga:itemQuantity'},
                  {'expression': 'ga:uniquePurchases'},
                  {'expression': 'ga:revenuePerItem'},
                  {'expression': 'ga:itemRevenue'},                 
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                    {'name': 'ga:screenResolution'}         
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestFive={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:totalPublisherImpressions'},
                  {'expression': 'ga:totalPublisherCoverage'},
                  {'expression': 'ga:totalPublisherMonetizedPageviews'},
                  {'expression': 'ga:totalPublisherViewableImpressionsPercent'},
                  {'expression': 'ga:totalPublisherClicks'},
                  {'expression': 'ga:totalPublisherRevenue'},
                  {'expression': 'ga:totalPublisherECPM'},
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                    {'name': 'ga:screenResolution'}        
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}

#Old System - Language

reportRequestOne={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:sessions'}, 
                  {'expression': 'ga:users'}, 
                  {'expression': 'ga:newUsers'}, 
                  {'expression': 'ga:bounces'}, 
                  {'expression': 'ga:sessionDuration'},
                  {'expression': 'ga:goal1Completions'},
                  {'expression': 'ga:goal2Completions'},
                  {'expression': 'ga:goal3Completions'},
                  {'expression': 'ga:goalCompletionsAll'}, 
                  {'expression': 'ga:goalValueAll'}
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}


reportRequestTwo={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:goal4Completions'},
                  {'expression': 'ga:goal5Completions'},
                  {'expression': 'ga:goal6Completions'},
                  {'expression': 'ga:goal7Completions'},
                  {'expression': 'ga:goal8Completions'},
                  {'expression': 'ga:goal9Completions'},
                  {'expression': 'ga:goal10Completions'},
                  {'expression': 'ga:goal11Completions'},
                  {'expression': 'ga:goal12Completions'},
                  {'expression': 'ga:goal13Completions'}
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}
  

reportRequestThree={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [

                  {'expression': 'ga:goal14Completions'},
                  {'expression': 'ga:goal15Completions'},
                  {'expression': 'ga:goal16Completions'},
                  {'expression': 'ga:goal17Completions'},
                  {'expression': 'ga:goal18Completions'},
                  {'expression': 'ga:goal19Completions'},
                  {'expression': 'ga:goal20Completions'},
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestFour={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:transactions'},
                  {'expression': 'ga:transactionRevenue'},
                  {'expression': 'ga:transactionShipping'},
                  {'expression': 'ga:transactionTax'},
                  {'expression': 'ga:totalValue'},
                  {'expression': 'ga:itemQuantity'},
                  {'expression': 'ga:uniquePurchases'},
                  {'expression': 'ga:revenuePerItem'},
                  {'expression': 'ga:itemRevenue'},                 
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestFive={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:totalPublisherImpressions'},
                  {'expression': 'ga:totalPublisherCoverage'},
                  {'expression': 'ga:totalPublisherMonetizedPageviews'},
                  {'expression': 'ga:totalPublisherViewableImpressionsPercent'},
                  {'expression': 'ga:totalPublisherClicks'},
                  {'expression': 'ga:totalPublisherRevenue'},
                  {'expression': 'ga:totalPublisherECPM'},
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:language'},
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}

#Old System - Screen Resolution

reportRequestOne={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:sessions'}, 
                  {'expression': 'ga:users'}, 
                  {'expression': 'ga:newUsers'}, 
                  {'expression': 'ga:bounces'}, 
                  {'expression': 'ga:sessionDuration'},
                  {'expression': 'ga:goal1Completions'},
                  {'expression': 'ga:goal2Completions'},
                  {'expression': 'ga:goal3Completions'},
                  {'expression': 'ga:goalCompletionsAll'}, 
                  {'expression': 'ga:goalValueAll'}
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:screenResolution'}
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}


reportRequestTwo={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:goal4Completions'},
                  {'expression': 'ga:goal5Completions'},
                  {'expression': 'ga:goal6Completions'},
                  {'expression': 'ga:goal7Completions'},
                  {'expression': 'ga:goal8Completions'},
                  {'expression': 'ga:goal9Completions'},
                  {'expression': 'ga:goal10Completions'},
                  {'expression': 'ga:goal11Completions'},
                  {'expression': 'ga:goal12Completions'},
                  {'expression': 'ga:goal13Completions'}
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:screenResolution'}  
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}
  

reportRequestThree={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [

                  {'expression': 'ga:goal14Completions'},
                  {'expression': 'ga:goal15Completions'},
                  {'expression': 'ga:goal16Completions'},
                  {'expression': 'ga:goal17Completions'},
                  {'expression': 'ga:goal18Completions'},
                  {'expression': 'ga:goal19Completions'},
                  {'expression': 'ga:goal20Completions'},
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:screenResolution'}  
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestFour={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:transactions'},
                  {'expression': 'ga:transactionRevenue'},
                  {'expression': 'ga:transactionShipping'},
                  {'expression': 'ga:transactionTax'},
                  {'expression': 'ga:totalValue'},
                  {'expression': 'ga:itemQuantity'},
                  {'expression': 'ga:uniquePurchases'},
                  {'expression': 'ga:revenuePerItem'},
                  {'expression': 'ga:itemRevenue'},                 
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:screenResolution'}         
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestFive={
  'reportRequests': [
  {
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
    'metrics': [
                  {'expression': 'ga:totalPublisherImpressions'},
                  {'expression': 'ga:totalPublisherCoverage'},
                  {'expression': 'ga:totalPublisherMonetizedPageviews'},
                  {'expression': 'ga:totalPublisherViewableImpressionsPercent'},
                  {'expression': 'ga:totalPublisherClicks'},
                  {'expression': 'ga:totalPublisherRevenue'},
                  {'expression': 'ga:totalPublisherECPM'},
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:screenResolution'}        
                  ],
    'pageToken': '0',
    'pageSize': PAGE_SIZE          
  }]
}



def main():
  
  analytics = initialize_analyticsreporting()
  response_one = get_report(analytics, reportRequestOne)
  response_two = get_report(analytics, reportRequestTwo)
  response_three = get_report(analytics, reportRequestThree)
  response_four = get_report(analytics, reportRequestFour)
  response_five = get_report(analytics, reportRequestFive)

  try:
    data_one = response_one['reports'][0]['data']['rows']
    download_csv(data_one, 1, reportRequestOne, FILENAME)
  except Exception as e:
    print ('Error - System - One: ', str(e))

  try:
    data_two = response_two['reports'][0]['data']['rows']
    download_csv(data_two, 2, reportRequestTwo, FILENAME)
  except Exception as e:
    print ('Error - System - Two: ', str(e))

  try:
    data_three = response_three['reports'][0]['data']['rows']
    download_csv(data_three, 3, reportRequestThree, FILENAME)
  except Exception as e:
    print ('Error - System - Three: ', str(e))
  
  try:
    data_four = response_four['reports'][0]['data']['rows']
    download_csv(data_four, 4, reportRequestFour, FILENAME)
  except Exception as e:
    print ('Error - System - Four: ', str(e))

  try:
    data_five = response_five['reports'][0]['data']['rows']
    download_csv(data_five, 5, reportRequestFive, FILENAME)
  except Exception as e:
    print ('Error - System - Five: ', str(e))

  
 
if __name__ == '__main__':
  main()
