from django.shortcuts import render
from django.conf import settings
import requests
from django.shortcuts import redirect
import json

ms_identity_web = settings.MS_IDENTITY_WEB

# pic_url = url_pic()

def index(request):
    if request.identity_context_data.authenticated:

        # print('Logged in')
        # all_Request = testRequest.objects.all()
        # status_wait= all_Request.filter(docStatus__startswith='w')
        # print(results[0]['picture_url'])
        pic_url,data = url_pic("Wait")
        # print("Before",data)
        # json.dumps(data)
        # print("After",data)
        # data = data_request("All")
        return render(request, 'auth/inbox.html', context={'pic_url' : pic_url,'all_data' : data})

    else:
        # print('index page')
        return redirect('sign_in')

def dashboard(request):
    if request.identity_context_data.authenticated:

        pic_url,data = url_pic("All")
        # print(data)
        return render(request, 'auth/dashboard.html',{'pic_url' : pic_url,'all_data' : data})

    else:
        return redirect('sign_in')

def history(request):
    if request.identity_context_data.authenticated:

    #     all_Request = testRequest.objects.all()
    #     status_test= all_Request.filter(docStatus__startswith='a' ) | all_Request.filter(docStatus__startswith='r' )
        pic_url,data = url_pic("A_C")
        return render(request, 'auth/history.html',{'pic_url' : pic_url,'all_data' : data})
    else:
        # print('index page')
        return redirect('sign_in')

def contact(request):
    if request.identity_context_data.authenticated:
        pic_url,data = url_pic("All")
        return render(request, 'auth/contact.html',{'pic_url' : pic_url})
    else:
        return redirect('sign_in')

def url_pic(status):
        ms_identity_web.acquire_token_silently()
        graph = 'https://graph.microsoft.com/v1.0/me?$select=id,employeeId'        
        authZ = f'Bearer {ms_identity_web.id_data._access_token}'
        # print(authZ)
        result1 = requests.get(graph, headers={'Authorization': authZ}).json()

        # mydas_api = "https://e-accounting-dev.siamkubota.co.th/web-api/api/esesiesform/getDataEseries" #https://e-accounting-dev.siamkubota.co.th/web-api/api/esesiesform/getDataEXP
        mydas_api = "https://e-accounting-dev.siamkubota.co.th/web-api/api/esesiesform/getDataEXP"
        hed = {'Authorization': authZ , 'Content-Type': 'application/json'}
        payload = json.dumps({
        "department": "DY34000000",
        "requesterCode": "",
        "requesterDate": "",
        "lastUpdate": "",
        "system": "",
        "docStatus": "",
        "attachment": "",
        "approverCode": "", #result1['employeeId']
        "pageSize": 20,
        "pageIndex": 0
        })
        result_api = requests.post(mydas_api, headers=hed,data=payload).json()
        # print(result_api)
        for i in result_api['data']:
            if i['attachment'] == True:
                i['attachment'] = '✔'
            else :
                i['attachment'] = '-'
            if i['approverCode'] == None:
                i['approverCode'] = 'None'
            if i['approverNameTH'] == None:
                i['approverNameTH'] = 'None'
            if i['approverNameEN'] == None:
                i['approverNameEN'] = 'None'
            if i['approveUrl'] == None:
                i['approveUrl'] = 'None'
            if i['rejectUrl'] == None:
                i['rejectUrl'] = 'None'
            # print(i["requestDate"])
            i["requestDate"] = changedatetime(i["requestDate"])
            i["lastUpdate"] = changedatetime(i["lastUpdate"])
            # print(type(i["attachment"]))
        data_use = []
        if status.startswith("All"):
            for i in result_api['data']:
                if i["docStatus"] != "Draft":
                    data_use.append(i)
                # print(i)
        elif status.startswith("Complete"):
            for i in result_api['data']:
                if i["docStatus"] == "Complete":
                    data_use.append(i)
        elif status.startswith("Cancel"):
            for i in result_api['data']:
                if i["docStatus"] == "Cancel":
                    data_use.append(i)
        elif status.startswith("Wait") :
            for i in result_api['data']:
                if i["docStatus"] == "WaitForApprove":
                    data_use.append(i)
        elif status.startswith("A_C") :
            for i in result_api['data']:
                if i["docStatus"] == "Complete" or  i["docStatus"] == "Cancel":
                    data_use.append(i)
    
        if result1['employeeId'] == None:
            empid = '00000'
        else:
            empid = result1['employeeId'] #15856

        Username = "SKCone"
        Password = "OneApi2022*"
        token_url ='https://p701apsi01-la02skc.azurewebsites.net/skcapi/token'
        body ={
            "UserName" : Username,
            "Password" : Password
        }
        result2 = requests.post(token_url,json=body).json()
        # token = result1['accessToken']
        empid_url = 'https://p701apsi01-la01skc.azurewebsites.net/skcapi/empid/' + empid
        # print(empid_url)
        auth = f'Bearer {result2["accessToken"]}'
        results = requests.get(empid_url, headers={'Authorization': auth}).json()
        if type(results) == list:
            pic_url = results[0]['picture_url']
        else:
            pic_url = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
        return pic_url,data_use

def testgetpic():
    ms_identity_web.acquire_token_silently()
    graph = 'https://graph.microsoft.com/v1.0/me?$select=id,employeeId'        
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    result1 = requests.get(graph, headers={'Authorization': authZ}).json()
    if result1['employeeId'] == None:
            empid = '00000'
    else:
            empid = result1['employeeId'] #15856

    Username = "SKCone"
    Password = "OneApi2022*"
    token_url ='https://p701apsi01-la02skc.azurewebsites.net/skcapi/token'
    body ={
        "UserName" : Username,
        "Password" : Password
    }
    result2 = requests.post(token_url,json=body).json()
    # token = result1['accessToken']
    empid_url = 'https://p701apsi01-la01skc.azurewebsites.net/skcapi/empid/' + empid
    # print(empid_url)
    auth = f'Bearer {result2["accessToken"]}'
    results = requests.get(empid_url, headers={'Authorization': auth}).json()
    if type(results) == list:
        pic_url = results[0]['picture_url']
    else:
        pic_url = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'

    return pic_url

def changedatetime(datetime):
    # datetime = "2019-10-15T00:00:00"
    y_m_d = datetime.split("T")[0]
    y = y_m_d.split("-")[0]
    m = y_m_d.split("-")[1]
    d = y_m_d.split("-")[2]
    date = d +"/"+ m + "/" + y
    return date


# @ms_identity_web.login_required
# def call_ms_graph(request):
#     ms_identity_web.acquire_token_silently()
#     graph = 'https://graph.microsoft.com/v1.0/users'
#     authZ = f'Bearer {ms_identity_web.id_data._access_token}'
#     results = requests.get(graph, headers={'Authorization': authZ}).json()

#     if 'value' in results:
#         results ['num_results'] = len(results['value'])
#         results['value'] = results['value'][:5]
#     else:
#         results['value'] =[{'displayName': 'call-graph-error', 'id': 'call-graph-error'}]
#     return render(request, 'auth/call-graph.html', context=dict(results=results))
