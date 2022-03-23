import requests

def dailyData():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    for pcr in data['daily_pcr_testing_data']:
        if pcr['date'] == '2021-09-18':
            count = pcr['pcr_count']
            print (count)
    message = data['local_new_cases']
    print (message)
    return count, message

def dailyNewCases():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['local_new_cases']
    return message
def dailyTotalCases():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['local_total_cases']
    return message
def dailyNoOfIndividuals():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['local_total_number_of_individuals_in_hospitals']
    return message
def dailyTotalDeath():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['local_deaths']
    return message
def dailyTodayDeades():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['local_new_deaths']
    return message
def dailyRecovered():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['local_recovered']
    return message
def dailyTotalpcrTest():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['total_pcr_testing_count']
    return message
def dailylocalActiveCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['local_active_cases']
    return message

def dailyglobalActiveCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['global_total_cases']
    return message
def dailyglobalNewCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['global_new_cases']
    return message
def dailyGlobalDeathsCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['global_deaths']
    return message
def dailyGlobalNewDeathCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['global_new_deaths']
    return message
def dailyGlobalRecoveryCase():
    response = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical").json()
    data = response['data']
    message = data['global_recovered']
    return message