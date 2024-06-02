import requests
import time

FILES_SCANNING_URL = "https://www.virustotal.com/vtapi/v2/file/scan"
REPORTING_URL = 'https://www.virustotal.com/vtapi/v2/file/report'

# THe project's Virus Total API account's key
API_KEY = "951e0969e4f3ba02e2174d71db83821dc45127a65d8f37389c7257b6586f4609"


def ScanFile(filePath):
    # The function gets a file path to scan
    # The function returns the scan id which contain the results of the scanning

    # Open the file in binary mode
    with open(filePath, 'rb') as file:
        files = {'file': (filePath, file)}
        params = {'apikey': API_KEY}
        
        # Upload the file
        response = requests.post(FILES_SCANNING_URL, files=files, params=params)
        result = response.json()
        
        # Check if the scan was successfully initiated
        if 'scan_id' in result:
            scanId = result['scan_id']
            return scanId
        else:
            print(f"Error uploading {filePath} for scanning")
            return None
        

def GetScanReport(scanId):
    # The function gets a scan id.
    # The function returns the report of the scan.

    params = {'apikey': API_KEY, 'resource': scanId}
    
    # Polling the API for the scan report
    while True:
        try:
            response = requests.get(REPORTING_URL, params=params)
            result = response.json()
            
            # Check if the scan report is available
            if result['response_code'] == 1:
                return result
            else:
                print("Scan report not ready, waiting...")
                # Waiting before polling again
        except requests.exceptions.RequestException as e:
            print("Error making API request, please wait to another request")
            return None
        except Exception as e:
            print("An error occurred.")
            return None


def AnalyzeReport(report):
    # The function gets a report.
    # The function analyzes the report and returns True if the file is clear, otherwise False.

    # The report's header(contain integer value) that indicate the amount of av engiens that found the file Infected or Suspicious
    if type(report) != dict:
        return None
    else:
        positives = report.get('positives', 0)
    
    positives = report.get('positives', 0)
    return positives == 0


def IsFileClear(filePath, screen):
    # The function gets a file path.
    # The function return True if the file is safe, otherwise False.
    print("START SCANNING...")
    scanId = ScanFile(filePath)
    scanReport = GetScanReport(scanId)
    finalResult = AnalyzeReport(scanReport)


    while finalResult == None:
        screen.after(1000)
        scanId = ScanFile(filePath)
        scanReport = GetScanReport(scanId)
        finalResult = AnalyzeReport(scanReport)
    
    return finalResult