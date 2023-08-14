Google Analytics 3 is over, but you probably still have access to the data, but not for long, Google is planning to get rid of it soon, so, you should download it while you can.

This repo has the code to do just that, be aware though, some of the reports do not work for some data ranges, because Google Analytics has changed some of the metrics and dimensions throughout the years.

Because of it, some of the reports may seem duplicated depending on which date range you insert, unfortunatelly Google is not clear on which dimensions and metrics work for which date ranges, so I am unable to improve that. I suggest you download the reports and check them to make sure you do not have duplicated data in your hands.

Steps:

1. Create a service account inside Google Cloud Platform (GCP) and create and download a JSON API Key
2. Give it access to the View to Read & Analyze
    https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py
3. Enable Analytics Reporting API inside GCP
    https://console.cloud.google.com/apis/api/analyticsreporting.googleapis.com/metrics?project=test-1599759249179
4. Clone this repo
5. Change the settings, for that, go to configs/config.py and follow the instructions there (in comments).
6. Copy your JSON API Key to api-key/api-secret.json replacing whatever is inside with it.
7. Run main.py, it will create a folder "csv" and a subfolder with the VIEW_ID where the reports will be downloaded as .csv files.
