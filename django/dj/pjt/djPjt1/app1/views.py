from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import tbl_userInfo, tbl_eduImage
import json
# ip:port/app1/login/?user_id=~~~~&password=~~~~

@csrf_exempt # ip:port/app1/login   with post body json {user_id: '', password: ''}
def loginApp(request):
    if request.method == 'POST':
        r = json.loads(request.body)
        user_id = r['user_id']
        password = r['password']
    
        check = 'no'
        count = tbl_userInfo.objects.count()
        userInfo = tbl_userInfo.objects.all()
        for user in userInfo:
            if user.user_id == user_id and user.password == password:
                check = 'yes'
                break
        return HttpResponse(check)
    else:
        return HttpResponse('usePost')

@csrf_exempt # ip:port/app1/register/  with post body json  {user_id : '', password: '', email: ''}
def registerApp(request):
    if request.method == 'POST':
        r = json.loads(request.body)
        user_id_ = r['user_id']
        password_ = r['password']
        email_ = r['email']

        if tbl_userInfo.objects.filter(user_id = user_id_).exists():
            return HttpResponse('overlapID')
        
        tbl_userInfo(user_id = user_id_, password = password_, email = email_).save()
        return HttpResponse('ok')   
    else:
        return HttpResponse('usePost')

@csrf_exempt # ip:port/app1/store/name/left/opne
def storeImageApp(request, img_name, leftRight, openClose):
    if request.method == 'GET':
        img_path = "./img"
        img_path += "/"+leftRight+"/"+openClose
        
        if tbl_eduImage.objects.filter(image_name = img_name).exists():
            return HttpResponse('overlapName')

        tbl_eduImage(image_name = img_name, image_path = img_path).save()
        return HttpResponse('completeStore: '+img_path+"/"+img_name)
    else:
        return HttpResponse('useGet')

def getImageApp(request): # ip:port/getImage/
    if request.method == 'GET':
        count = tbl_eduImage.objects.count()
        if count == 0:
            return HttpResponse('no images')

        data = tbl_eduImage.objects.all()
        json_data = '{'
        num = 1
        for d in data:
            json_data += '\"'+(str)(num)+'\":{\"image_name\":\"'+d.image_name+'\",\"image_path\":\"'+d.image_path+'\"}'
            if num != count:
                json_data += ','
            num += 1
        json_data += '}'

        return HttpResponse(json_data)
#        return JsonResponse(json.dumps(data))
    else:
        return HttpResponse('useGet')
