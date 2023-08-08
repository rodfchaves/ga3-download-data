from config import *
from functions import *

FILENAME = '-device-'

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
                    {'name': 'ga:browser'},
                    {'name': 'ga:operatingSystem'}, 
                    {'name': 'ga:operatingSystemVersion'},
                    {'name': 'ga:mobileDeviceBranding'}, 
                    {'name': 'ga:mobileDeviceModel'},
                    {'name': 'ga:browserSize'},
                    {'name': 'ga:mobileDeviceInfo'},  
                  ],
    'pageToken': PAGE_TOKEN,
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
                    {'name': 'ga:browser'},
                    {'name': 'ga:operatingSystem'}, 
                    {'name': 'ga:operatingSystemVersion'},
                    {'name': 'ga:mobileDeviceBranding'}, 
                    {'name': 'ga:mobileDeviceModel'},
                    {'name': 'ga:browserSize'},
                    {'name': 'ga:mobileDeviceInfo'},  
                  ],
    'pageToken': PAGE_TOKEN,
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
                  {'expression': 'ga:goal20Completions'}
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:browser'},
                    {'name': 'ga:operatingSystem'}, 
                    {'name': 'ga:operatingSystemVersion'},
                    {'name': 'ga:mobileDeviceBranding'}, 
                    {'name': 'ga:mobileDeviceModel'},
                    {'name': 'ga:browserSize'},
                    {'name': 'ga:mobileDeviceInfo'},  
                  ],
    'pageToken': PAGE_TOKEN,
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
                    {'name': 'ga:browser'},
                    {'name': 'ga:operatingSystem'}, 
                    {'name': 'ga:operatingSystemVersion'},
                    {'name': 'ga:mobileDeviceBranding'}, 
                    {'name': 'ga:mobileDeviceModel'},
                    {'name': 'ga:browserSize'},
                    {'name': 'ga:mobileDeviceInfo'},  
                  ],
    'pageToken': PAGE_TOKEN,
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
                    {'name': 'ga:browser'},
                    {'name': 'ga:operatingSystem'}, 
                    {'name': 'ga:operatingSystemVersion'},
                    {'name': 'ga:mobileDeviceBranding'}, 
                    {'name': 'ga:mobileDeviceModel'},
                    {'name': 'ga:browserSize'},
                    {'name': 'ga:mobileDeviceInfo'}          
                  ],
    'pageToken': PAGE_TOKEN,
    'pageSize': PAGE_SIZE          
  }]
}

#Old System - Mobile Device

reportRequestSix={
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
                    {'name': 'ga:mobileDeviceBranding'}, 
                    {'name': 'ga:mobileDeviceModel'},
                    {'name': 'ga:mobileDeviceInfo'},                      
                  ],
    'pageToken': PAGE_TOKEN,
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestSeven={
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
                    {'name': 'ga:mobileDeviceBranding'}, 
                    {'name': 'ga:mobileDeviceModel'},
                    {'name': 'ga:mobileDeviceInfo'},  
                  ],
    'pageToken': PAGE_TOKEN,
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestEight={
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
                  {'expression': 'ga:goal20Completions'}
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:mobileDeviceBranding'}, 
                    {'name': 'ga:mobileDeviceModel'},
                    {'name': 'ga:mobileDeviceInfo'},  
                  ],
    'pageToken': PAGE_TOKEN,
    'pageSize': PAGE_SIZE          
  }]
}

#Old System - Browser

reportRequestNine={
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
                    {'name': 'ga:browser'},
                    {'name': 'ga:operatingSystem'}, 
                    {'name': 'ga:operatingSystemVersion'},                    
                  ],
    'pageToken': PAGE_TOKEN,
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestTen={
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
                    {'name': 'ga:browser'},
                    {'name': 'ga:operatingSystem'}, 
                    {'name': 'ga:operatingSystemVersion'},  
                  ],
    'pageToken': PAGE_TOKEN,
    'pageSize': PAGE_SIZE          
  }]
}

reportRequestEleven={
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
                  {'expression': 'ga:goal20Completions'}
                ],
    'dimensions': [
                    {'name': 'ga:date'}, #do not remove this line
                    {'name': 'ga:browser'},
                    {'name': 'ga:operatingSystem'}, 
                    {'name': 'ga:operatingSystemVersion'},  
                  ],
    'pageToken': PAGE_TOKEN,
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
  response_six = get_report(analytics, reportRequestSix)
  response_seven = get_report(analytics, reportRequestSeven)
  response_eight = get_report(analytics, reportRequestEight)
  response_nine = get_report(analytics, reportRequestNine)
  response_ten = get_report(analytics, reportRequestTen)
  response_eleven = get_report(analytics, reportRequestEleven)

  try:
    data_one = response_one['reports'][0]['data']['rows']
    download_csv(data_one, 1, reportRequestOne, FILENAME)
  except Exception as e:
    print ('Error - Mobile - One: ', str(e))

  try:
    data_two = response_two['reports'][0]['data']['rows']
    download_csv(data_two, 2, reportRequestTwo, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Two: ', str(e))

  try:
    data_three = response_three['reports'][0]['data']['rows']
    download_csv(data_three, 3, reportRequestThree, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Three: ', str(e))
  
  try:
    data_four = response_four['reports'][0]['data']['rows']
    download_csv(data_four, 4, reportRequestFour, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Four: ', str(e))

  try:
    data_five = response_five['reports'][0]['data']['rows']
    download_csv(data_five, 5, reportRequestFive, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Five: ', str(e))

  try:
    data_six = response_six['reports'][0]['data']['rows']
    download_csv(data_six, 6, reportRequestSix, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Six: ', str(e))

  try:
    data_seven = response_seven['reports'][0]['data']['rows']
    download_csv(data_seven, 7, reportRequestSeven, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Seven: ', str(e))

  try:
    data_eight = response_eight['reports'][0]['data']['rows']
    download_csv(data_eight, 8, reportRequestEight, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Eight: ', str(e))

  try:
    data_nine = response_nine['reports'][0]['data']['rows']
    download_csv(data_nine, 9, reportRequestNine, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Nine: ', str(e))

  try:
    data_ten = response_ten['reports'][0]['data']['rows']
    download_csv(data_ten, 10, reportRequestTen, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Ten: ', str(e))

  try:
    data_eleven = response_eleven['reports'][0]['data']['rows']
    download_csv(data_eleven, 11, reportRequestEleven, FILENAME)
  except Exception as e:
    print ('Error - Mobile - Eleven: ', str(e))
  
 
if __name__ == '__main__':
  main()