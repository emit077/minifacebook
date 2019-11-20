from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User_data, Requiest_list, Posted_data, Likes, Comments, OTP
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import redirect
from shutil import copyfile
from django.db.models import Q
from django.contrib.auth.models import auth
from django.contrib import messages
import http.client
import random
# Create your views here.


def home(request):  # home page is
    try:
        if request.session['userid']:
            return Share(request)
        return render(request, 'blog/home.html')
    except KeyError:
        pass
    return render(request, 'blog/home.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        mobile_no = request.POST.get('mobile', None)
        if name == "" or name == None:
            messages.warning(
                request, 'please Enter Name')
            return redirect('blog-register_form')
        if mobile_no == "" or mobile_no == None:
            messages.warning(
                request, 'please Enter  valid mobile number')
            return redirect('blog-register_form')
        if password == "" or password == None:
            messages.warning(
                request, 'please Enter  valid  paasword')
            return redirect('blog-register_form')
        UD = User_data.objects.filter(mobile_no=mobile_no)
        if UD.count() > 0:
            messages.warning(
                request, "Mobile number already exist")
            return redirect('blog-register_form')

        userentry = User_data()
        userentry.name = name
        userentry.mobile_no = mobile_no
        userentry.password = password
        userentry.creation_date = timezone.now()
        userentry.save()

        otp = random.randint(1000, 9999)
        print(otp)
        otps=OTP()
        otps.mobile_no=mobile_no
        otps.otp=otp
        otps.save()
        messages.success(
            request, " successfully register,Now Login")
        return redirect('blog-login_form')
        # user = user.objects.create_user(
        #     username=mobile_no, password=password)
        # user.save()

        # msg authentication
        # Authentication = "303565AGyn1zL4jlj5dcbac5c"
        # Mobile = "8305050674"
        # conn = http.client.HTTPSConnection("api.msg91.com")
        # payload = ""
        # headers = {'content-type': "application/json"}
        # conn.request("POST", "/api/v5/otp?invisible=1&otp=OTP%20to%20send%20and%20verify.2020%20If%20not%20sent%2C%20OTP%20will%20be%20generated.&userip=IPV4%20User_data%20IP&authkey=303565AGyn1zL4jlj5dcbac5c%20Key&email=Email%20ID&mobile=8305050674%20Number&template_id=5dcbb6b0d6fc0549a955d997%20ID&otp_length=&otp_expiry=", payload, headers)
        # res = conn.getresponse()
        # data = res.read()
        # print(data.decode("utf-8"))

        conn = http.client.HTTPSConnection("api.msg91.com")

        payload = ""

        headers = {'content-type': "application/json"}

        conn.request("POST", "/api/v5/otp?invisible=1&otp=OTP%20to%20send%20and%20verify.%20If%20not%20sent%2C%20OTP%20will%20be%20generated.&userip=IPV4%20User%20IP&authkey=303565AGyn1zL4jlj5dcbac5c&email=Email%20ID&mobile=Mobile%20Number&template_id=5dcbb6b0d6fc0549a955d997&otp_length=&otp_expiry=", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

    else:
        return home(request)


def register_form(request):
    return render(request, 'blog/register.html')


def login_form(request):
    return render(request, 'blog/login.html',{"hide":"hide"})


def verify_mobile_number(request):
    return render(request, 'blog/login.html')


def login(request):
    mobile_no = request.POST.get('mobile', None)
    print  (mobile_no)
    if mobile_no == None or mobile_no == "":
        messages.warning(
            request, 'please Enter  Mobile no')
        return redirect('blog-login_form')
    try:
        user = User_data.objects.filter(mobile_no=mobile_no)
        if user.count() > 0:
            userdata = User_data.objects.get(mobile_no=mobile_no)
            if userdata.password == request.POST.get('password', None):
                request.session['name'] = userdata.name
                request.session['userid'] = userdata.id
                con_request = Requiest_list.objects.filter(
                    requested_to=userdata.id, status="PENDING")
                requests = con_request.count()
                data = Posted_data.objects.order_by('-posted_on')
                return redirect('blog-user_post')
            else:
                messages.warning(
                    request, 'incorrect mobile number or password')
                # return HttpResponse("invalid password", status=401)
                return redirect('blog-login_form')
                # return render(request, 'blog/login.html', {'data': "incorrect mobile number or password"})
        else:
            messages.warning(
                request, 'incorrect mobile number or password')
            return redirect('blog-login_form')
    except KeyError:
        messages.warning(
            request, 'incorrect mobile number or password')
        return redirect('blog-login_form')


def forgetpass(request):
    return render(request, 'blog/forgetpass.html')

def sentotp(request):
    mobile_no = request.POST.get('mobile', None)
    if mobile_no==None or mobile_no=="":
        mobile_no = request.GET.get('mobile_no', None)
    print(mobile_no)
    if mobile_no:
        listuser= OTP.objects.filter(mobile_no=mobile_no)
        randomOTP = random.randint(1000, 9999)
        print(randomOTP)
        print(listuser.count())
        if listuser.count()==0:
            otps=OTP()
            otps.mobile_no=mobile_no
            otps.otp=randomOTP
            otps.save()
            messages.success(
            request, 'OTP send Successfully')
            return render(request, 'blog/validateotp.html', {'mobile_no':mobile_no})
        else:
            objOTP=OTP.objects.get(mobile_no=mobile_no)
            objOTP.otp=randomOTP
            objOTP.save()
            messages.success(
                request, 'OTP send Successfully')
            return render(request, 'blog/validateotp.html', {'mobile_no':mobile_no})
    else:
        messages.warning(
            request, 'PLease Enter mobile no')
        return redirect("blog-forgetpass")
    
    
def validateOTP(request):
    mobile_no = request.POST.get('mobile', None)
    rOTP = request.POST.get('otp', None)
    print(rOTP)
    listotps=OTP.objects.filter(mobile_no=mobile_no).order_by('-time')
    if listotps.count()>0:
        objOTP=listotps.first()
        # objOTP=OTP.objects.get(mobile_no=mobile_no)
        if objOTP.otp==rOTP:
            messages.info(
            request, 'OTP Verified')
            return render(request, 'blog/newpassword.html', {'mobile_no':mobile_no})
        else:
            messages.warning(
            request, 'Invalid OTP')
        return render(request, 'blog/validateotp.html', {'mobile_no':mobile_no})
    else:
        messages.warning(
            request, 'invalid mobile no')
        return render(request, 'blog/validateotp.html', {'mobile_no':mobile_no})
   
        
    
def newpassword(request):
    mobile_no = request.POST.get('mobile', None)
    password = request.POST.get('password', None)
    listuser=User_data.objects.filter(mobile_no=mobile_no)
    if listuser.count()>0:
        objuser= User_data.objects.get(mobile_no=mobile_no);
        objuser.password=password
        objuser.save()
        messages.success(
                request, 'Password Reset Successfully')
        return redirect('blog-login_form')
    
def resetpass(request):
    mobile_no = request.GET.get('mobile_no', None)
    password = request.GET.get('password', None)
    user = User_data.objects.filter(mobile_no=mobile_no)
    if user.count() > 0:
        userdata = User_data.objects.get(mobile_no=mobile_no)
        userdata.password = password
        userdata.save()
        print("hello")
        messages.success(
                request, 'Password Reset Successfully')
        return login_form(request)
    else:
        print("hello")
        messages.warning(
                request, 'User Not Exist')
        return forgetpass(request)


def user_post(request):
    print('its postdata')
    id = request.session.get('userid', None)
    print(id)
    if id:
        alreadyliked = Likes.objects.filter(liked_by_id=id)
        listliked = []
        print(alreadyliked.count())
        for item in alreadyliked:
            listliked.append(item.post.id)
        userinfo = User_data.objects.get(id=id)
        friendlist = Requiest_list.objects.filter(
            Q(requested_by_id=id, status="ACCEPTED") | Q(requested_to_id=id, status="ACCEPTED"))
        arr = []
        if friendlist.count() > 0:
            for item in friendlist:
                if item.requested_to_id == id:
                    arr.append(item.requested_by.id)
                    # print()
                else:
                     arr.append(item.requested_to.id)
        post_data = Posted_data.objects.filter(
            Q(posted_by_id__in=arr)|Q(posted_by_id=id)).order_by('-posted_on')

        data = Posted_data.objects.all().order_by('-posted_on')
        con_request = Requiest_list.objects.filter(
            requested_to=id, status="PENDING")
        requests = con_request.count()
        request.session['recount'] = requests
        if data.count() > 0:
            return render(request, 'blog/share.html', {'data': post_data, 'username': userinfo.name, 'userid': userinfo.id, 'requests': requests, "listliked": listliked})
        else:
            return render(request, 'blog/share.html', {'userinfo': userinfo})
    else:
        return redirect('blog-home')

def Logout(request):
    try:
        # del request.session['name']
        # del request.session['userid']
        # return render(request, 'blog/home.html')
        return delete_session(request)
    except KeyError:
        pass
    return render(request, 'blog/home.html')


def Share(request):
    return user_post(request)
    # if request.session['userid']:
    #     data = Posted_data.objects.all().order_by('-posted_on')
    #     if data.count() > 0:
    #         return render(request, 'blog/share.html', {'data': data, 'hide': "hide"})
    #     else:
    #         return HttpResponse("no notes found."+str(id))
    # else:
    #     return render(request, 'blog/home.html')


def Save_notes(request):  # saving the notes
    postdata = Posted_data()
    postdata.posted_by_id = request.session['userid']
    if request.GET['type'] == "text":
        postdata.text = request.GET['notes']
    if request.GET['type'] == "image":
        postdata.text = request.GET['image']
    postdata.posted_on = timezone.now()
    postdata.save()
    return user_post(request)



def Delete_notes(request):  # deleting  notes
    # postdata = blog_data.objects.get(id=request.GET['id'])
    # postdata.delete()
    return Share(request)





def SearchUser(request):
    searchTerm = request.GET.get('searchTerm', None)
    userid = request.session['userid']
    try:
        val = int(searchTerm)
        listuserdata = User_data.objects.filter(
            mobile_no__icontains=val).exclude(id=userid)
    except ValueError:
        listuserdata = User_data.objects.filter(
            name__icontains=searchTerm).exclude(id=userid)
    return render(request, 'blog/searchlist.html', {'data': listuserdata})

# session handling-------------------------------------------#############
def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(
            request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')


def delete_session(request):
    try:
        del request.session['name']
        del request.session['userid']
        return redirect('blog-home')
        # return render(request, 'blog/home.html')
    except KeyError:
        pass
    # return render(request, "Helo")
    return redirect('blog-user_post')


def userprofile(request,name,id):
    print(name)
    myid= request.session.get('userid', None)
    if  myid:
        if id != None and id != "":
            profile_data = User_data.objects.get(id=id)
            already_requested=Requiest_list.objects.filter(Q(requested_by=id)
                                                | Q(requested_to=id))
            print(already_requested)
            connected=[]
            if already_requested.count()>0:
                for item in already_requested:
                    if item.requested_to==id:
                        connected.append(item.requested_by.id)
                    else:
                        connected.append(item.requested_to.id)
            friendlist = Requiest_list.objects.filter(Q(requested_by=id, status="ACCEPTED")
                                                | Q(requested_to=id, status="ACCEPTED"))
            arr=[]
            if friendlist.count() > 0:
                for item in friendlist:
                    if item.requested_to_id==id:
                        arr.append(item.requested_by.id)
                    else:
                        arr.append(item.requested_to.id)
            myfriends= User_data.objects.filter(id__in=arr)
            return render(request, 'blog/userprofile.html', {'profile_data': profile_data,'friendlist':myfriends,'myid':myid ,'connected':connected})
        else:
            messages.warning(
                    request, 'profile not found')
    else:
        return redirect('blog-home')        


def upadteprofile(request):
    print("updateprofile")
    image=request.FILES["image"]
    print(image)
    myid = request.session['userid']
    if myid:
        profile=User_data.objects.get(id=myid)
        profile.image=image
        profile.save()
        return HttpResponse("image saved")
    else:
        return HttpResponse("image not saved")

def con_request(request):
    id = request.GET['requested_to']
    myid = request.session['userid']
    requestentry = Requiest_list()
    requested_by = myid
    requested_to = id
    RL = Requiest_list.objects.filter(requested_by=myid, requested_to=id)
    if RL.count() > 0:
        return HttpResponse(" Allready Requested")
    else:
        requestentry.requested_by_id = int(requested_by)
        requestentry.requested_to_id = requested_to
        requestentry.request_date = timezone.now()
        requestentry.Accept_date = timezone.now()
        requestentry.request_status = "PENDING"
        requestentry.save()
        # instence.requested_by=requested_by
        # instence.save()
        return HttpResponse("Request send successfully")


def accept_reject_request(request):
    id = request.GET.get('requested_by', None)
    myid = request.session['userid']
    print(myid)
    print(id)
    RL = Requiest_list.objects.filter(requested_by_id=id, requested_to_id=myid, status="PENDING")
    if RL.count()>0:
        RL = Requiest_list.objects.get(requested_by_id=id, requested_to_id=myid )
        if request.GET['status'] == 'accept':
            RL.status = "ACCEPTED"
            RL.save()
            return HttpResponse("Request accepted")
            request.session['recount']=request.session['recount']+1
        else:
            RL.status = "REJECTED"
            RL.save()
            return HttpResponse("Request rejected")
            request.session['recount']=request.session['recount']-1
    else:
        return HttpResponse("Request Not Found")

def conrequiestList(request):
    id = request.session['userid']
    con_request = Requiest_list.objects.filter(
        requested_to=id, status="PENDING")
    cnt = con_request.count()
    arr = []
    for item in con_request:
        arr.append(item.requested_by.id)
    userdata = User_data.objects.filter(id__in=arr)
    return render(request, 'blog/friendrequest.html', {'userdata': userdata,})
    # for item in userdata:
    #     result += "<p>" + item.name
    #     result += "<input type='button' class='btn btn-outline-info' value='accept' onclick='accepted("+str(
    #         item.id)+")' style='margin-left:120px'/>"
    #     result += "<input type='button' class='btn btn-outline-danger' value='reject' onclick='reject(" + \
    #         str(item.id)+")' /></p>"
    # result += "</ul>"
    # return JsonResponse(result, safe=False)
    # return HttpResponse(userdata.count())


def comment_save(request):
    id = request.GET.get('id', None)
    text = request.GET.get('newcomment', None)
    Comments_data = Comments()
    Comments_data.post_id = id
    Comments_data.comments_by_id = request.session['userid']
    Comments_data.comment = text
    Comments_data.date_time = timezone.now()
    Comments_data.save()
    PDs=Posted_data.objects.filter(id=id)
    if PDs.count()>0:
        PD=Posted_data.objects.get(id=id)
        PD.comments_count=PD.comments_count+1
        PD.save()
        CB=Comments.objects.filter(post_id=id).order_by('-date_time')[0:5]
        return render(request, 'blog/commentlist.html', {'comment_list': CB})

    # return Share(request)


def like_post(request):
    myid = request.session['userid']
    id = request.GET.get('id', None)
    LDCheak = Likes.objects.filter(liked_by=myid, post_id=id)
    if LDCheak.count() < 1:
        LD = Likes()
        LD.post_id = id
        LD.liked_by_id = request.session['userid']
        LD.date_time = timezone.now()
        LD.save()
        PDs= Posted_data.objects.filter(id=id)
        if PDs.count()>0:
            PD= Posted_data.objects.get(id=id)
            PD.likes_count=int(PD.likes_count)+1
            PD.save()
            return HttpResponse("liked")
    else:
        return HttpResponse("already liked")
    # return HttpResponse("already liked"+str(id)+"/"+str(myid))
    # return Share(request)


def friendlist(request):
    id = request.session['userid']
    friendlist = Requiest_list.objects.filter(Q(requested_by=id, status="ACCEPTED")
                                              | Q(requested_to=id, status="ACCEPTED"))
    arr=[]
    if friendlist.count() > 0:
        for item in friendlist:
            if item.requested_to_id==id:
                arr.append(item.requested_by.id)
            else:
                arr.append(item.requested_to.id)
    myfriends= User_data.objects.filter(id__in=arr)
    if myfriends.count()>0:
        return render(request, 'blog/friends.html', {'friendlist':myfriends})
    else:
        messages.warning(
                request, 'No Ftiends Friends found')
        return  HttpResponse('No Ftiends Friends found')
    

def likedby(request):
    postid = request.GET.get('id', None)
    LB = Likes.objects.filter(post_id=postid)
    return render(request, 'blog/likedby.html',{'LB':LB})

    # result = "<ul>"
    # for item in LB:
    #     result += "<p>"+item.liked_by.name+"</p>"
    # result += "</ul>"
    # return JsonResponse(result, safe=False)
    # return HttpResponse(str(LB.count()))


def commentsby(request):
    postid = request.GET.get('id', None)
    CB = Comments.objects.filter(post_id=postid)
    if CB.count() < 1:
        result = "no momments found"
        return JsonResponse(result, safe=False)
    else:
        return render(request, 'blog/commentlist.html', {'comment_list': CB})
