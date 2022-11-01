from django.shortcuts import render
from django.conf import settings
import requests
from django.shortcuts import redirect
import json
# from django.contrib.auth.models import User
ms_identity_web = settings.MS_IDENTITY_WEB

def index(request):
    if request.identity_context_data.authenticated:

        # all_Request = testRequest.objects.all()
        # status_wait= all_Request.filter(docStatus__startswith='w')
        # print(results[0]['picture_url'])

        if request.session.get('pic') is None or request.session.get('empID') is None:
            request.session['pic'],request.session['empID'] = getpic()
            print("set value pic and empID")
        # print("line 22",request.session.get('pic'))
        # print("line 23",request.session.get('empID'))
        pic_url = request.session.get('pic')
        empID = request.session.get('empID')

        data = get_data("Wait",empID)
        # data = data_request("All")
        # superusers = User.objects.filter(is_superuser=True)
        # print(superusers)
        return render(request, 'auth/inbox.html', context={'pic_url' : pic_url,'all_data' : data})

    else:
        # print('index page')
        return redirect('sign_in')

def dashboard(request):
    if request.identity_context_data.authenticated:

        if request.session.get('pic') is None or request.session.get('empID') is None:
            request.session['pic'],request.session['empID'] = getpic()
            print("set value pic and empID")
        # print("line 22",request.session.get('pic'))
        # print("line 23",request.session.get('empID'))
        pic_url = request.session.get('pic')
        empID = request.session.get('empID')
        data = get_data("All",empID)
        # print("line 43",request.session.get('pic'))
        # print(data)
        return render(request, 'auth/dashboard.html',{'pic_url' : pic_url,'all_data' : data})

    else:
        return redirect('sign_in')

def history(request):
    if request.identity_context_data.authenticated:

    #     all_Request = testRequest.objects.all()
    #     status_test= all_Request.filter(docStatus__startswith='a' ) | all_Request.filter(docStatus__startswith='r' )
        if request.session.get('pic') is None or request.session.get('empID') is None:
            request.session['pic'],request.session['empID'] = getpic()
            print("set value pic and empID")
        # print("line 22",request.session.get('pic'))
        # print("line 23",request.session.get('empID'))
        pic_url = request.session.get('pic')
        empID = request.session.get('empID')
        data = get_data("A_C",empID)
        return render(request, 'auth/history.html',{'pic_url' : pic_url,'all_data' : data})
    else:
        
        return redirect('sign_in')

def contact(request):
    if request.identity_context_data.authenticated:
        if request.session.get('pic') is None or request.session.get('empID') is None:
            request.session['pic'],request.session['empID'] = getpic()
            print("set value pic and empID")
        # print("line 22",request.session.get('pic'))
        # print("line 23",request.session.get('empID'))
        pic_url = request.session.get('pic')
        # empID = request.session.get('empID')
        # data = url_pic("All",empID)
        return render(request, 'auth/contact.html',{'pic_url' : pic_url})
    else:
        return redirect('sign_in')

def get_data(status,empID):
    try:
        ms_identity_web.acquire_token_silently()      
        authZ = f'Bearer {ms_identity_web.id_data._access_token}'
        # print(authZ)
        # result1 = requests.get(graph, headers={'Authorization': authZ}).json()
        # print(empID)
        mydas_api = "https://e-accounting-dev.siamkubota.co.th/web-api/api/esesiesform/getDataEXP"
        hed = {'Authorization': authZ , 'Content-Type': 'application/json'}
        payload = json.dumps({
        "department": "",
        "requesterCode": "",
        "requesterDate": "",
        "lastUpdate": "",
        "system": "",
        "docStatus": "WaitForApprove,WaitForInitial,Complete,Cancel",
        "attachment": "",
        "approverCode": "empID", #empID
        "pageSize": 100,
        "pageIndex": 0
        })
        # print(payload)
        result_api = requests.post(mydas_api, headers=hed,data=payload).json()
        # result_api['data'][0]['picturesystem'] = '/static/image/contactlist/myDAS.png'
        # print(len(result_api['data']))
        data_use = []
        # j = 0
        for i in result_api['data']:
            if i['attachment'] == True:
                i['attachment'] = '✔'
            elif i['attachment'] == False :
                i['attachment'] = '-'
            i['approverCode'] = i['approverCode'] or ""
            i['approverNameTH'] = i['approverNameTH'] or ""
            i['approverNameEN'] = i['approverNameEN'] or ""
            i['approveUrl'] = i['approveUrl'] or ""
            i['rejectUrl'] = i['rejectUrl'] or ""
            if i['system'] == 'EXP':
                 i['picturesystem'] = '/static/image/contactlist/MyDAS.png'
            if i['docStatus'] == 'WaitForApprove':
                i['color'] = '#027779' #da5a34
            elif i['docStatus'] == 'WaitForInitial':
                i['color'] = '#da5a34' #027779
            i["requestDate"] = changedatetime(i["requestDate"])
            i["lastUpdate"] = changedatetime(i["lastUpdate"])
            # print(j)
            # j=j+1
            
        if status.startswith("All"):
            for i in result_api['data']:
                if i["docStatus"] != "Draft":
                    data_use.append(i)
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
                if i["docStatus"] == "WaitForApprove" or i["docStatus"] == "WaitForInitial":
                    data_use.append(i)
        elif status.startswith("A_C") :
            for i in result_api['data']:
                if i["docStatus"] == "Complete" or  i["docStatus"] == "Cancel":
                    data_use.append(i)
    
        return data_use
    except Exception as e: print("Error ",e)

def getpic():
    ms_identity_web.acquire_token_silently()
    graph = 'https://graph.microsoft.com/v1.0/me?$select=id,employeeId'        
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    # print(authZ)
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

    return pic_url,empid

def changedatetime(datetime):
    # datetime = "2019-10-15T00:00:00"
    y_m_d = datetime.split("T")[0]
    y = y_m_d.split("-")[0]
    m = y_m_d.split("-")[1]
    d = y_m_d.split("-")[2]
    date = d +"/"+ m + "/" + y
    return date
