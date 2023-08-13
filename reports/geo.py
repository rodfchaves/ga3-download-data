from configs.rpz_test import *
from functions import *

FILENAME = '-geo-'

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
                    {'name': 'ga:country'}, 
                    {'name': 'ga:region'},
                    {'name': 'ga:metro'},
                    {'name': 'ga:city'}                          
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
                    {'name': 'ga:country'}, 
                    {'name': 'ga:region'},
                    {'name': 'ga:metro'},
                    {'name': 'ga:city'}                                
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
                    {'name': 'ga:country'}, 
                    {'name': 'ga:region'},
                    {'name': 'ga:metro'},
                    {'name': 'ga:city'}                          
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
                    {'name': 'ga:country'}, 
                    {'name': 'ga:region'},
                    {'name': 'ga:metro'},
                    {'name': 'ga:city'}      
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
                    {'name': 'ga:country'}, 
                    {'name': 'ga:region'},
                    {'name': 'ga:metro'},
                    {'name': 'ga:city'}         
                  ],
    'pageToken': PAGE_TOKEN,
    'pageSize': PAGE_SIZE          
  }]
}


def main():
  
  analytics = initialize_analyticsreporting()
  get_report(analytics, reportRequestOne, 1, FILENAME)
  get_report(analytics, reportRequestTwo, 2, FILENAME)
  get_report(analytics, reportRequestThree, 3, FILENAME)
  get_report(analytics, reportRequestFour, 4, FILENAME)
  get_report(analytics, reportRequestFive, 5, FILENAME)
  
 
if __name__ == '__main__':
  main()
