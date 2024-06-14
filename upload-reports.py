import requests
import sys

file_name = sys.argv[1]
scan_type = ''

if file_name == 'gitleaks.json':
    scan_type = 'Gitleaks Scan'
elif file_name == 'trivyfs.json' or file_name == 'trivyimg.json':
    scan_type = 'Trivy Scan'
elif file_name == 'dependency-check-report.xml':
    scan_type = 'Dependency Check Scan'    

headers = {
  'Authorization' : 'Token 548afd6fab3bea9794a41b31da0e9404f733e222'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
  'active': True,
  'verified': True,
  'scan_type': scan_type,
  'minimum_severity': 'Low',
  'engagement': 18
}

files = {
  'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code ==201:
  
  # print(file_name, "Scan results uploaded to DEFECT-DOJO successfully...!!")
  # print(f"{file_name}  Scan results uploaded to DEFECT-DOJO successfully...!!")

  print("{} Scan results uploaded to DEFECT-DOJO successfully...!!".format(file_name))

else:
  print(f'Failed to upload scan results: {response.content}') 


