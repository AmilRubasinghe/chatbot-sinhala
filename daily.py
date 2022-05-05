import requests

def dailyData():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['local_new_cases'], "time": data['update_date_time']}
    print (message)
    return message

def dailyNewCases():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['local_new_cases'], "time": data['update_date_time']}
    print (message)
    return message
def dailyTotalCases():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['local_total_cases'], "time": data['update_date_time']}
    print (message)
    return message
def dailyNoOfIndividuals():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['local_total_number_of_individuals_in_hospitals'], "time": data['update_date_time']}
    print (message)
    return message
def dailyTotalDeath():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['local_deaths'], "time": data['update_date_time']}
    print (message)
    return message
def dailyTodayDeades():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['local_new_deaths'], "time": data['update_date_time']}
    print (message)
    return message
def dailyRecovered():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['local_recovered'], "time": data['update_date_time']}
    print (message)
    return message
def dailyTotalpcrTest():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['total_pcr_testing_count'], "time": data['update_date_time']}
    print (message)
    return message
def dailylocalActiveCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['local_active_cases'], "time": data['update_date_time']}
    print (message)
    return message

def dailyglobalActiveCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['global_total_cases'], "time": data['update_date_time']}
    return message
def dailyglobalNewCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['global_new_cases'], "time": data['update_date_time']}
    return message
def dailyGlobalDeathsCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['global_deaths'], "time": data['update_date_time']}
    return message
def dailyGlobalNewDeathCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['global_new_deaths'], "time": data['update_date_time']}
    return message
def dailyGlobalRecoveryCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = {"value":data['global_recovered'], "time": data['update_date_time']}
    return message