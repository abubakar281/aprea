from dataclasses import dataclass
import email
from pickle import FALSE
import re
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import us,As,P_S,media_ser,apm_ser, person_ser, company_ser,comment_ser
from .models import Publications, user,artical,media,Aprea_memberships, license_Person, license_Company,artical_comments
from django.shortcuts import render
from .utils import render_to_pdf
from django.http import HttpResponse
from django.contrib import messages
import base64
from .emails import send_otp_via_mail
from django.shortcuts import redirect
# Create your views here.


class signup(APIView):
    def post(self,request):
        try:
            user.objects.get(email=request.data['email'])
            return Response("User Already Exsit")
        except:
            serializer=us(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response("User signup Successfully")
            else:
                return Response(serializer.errors)


class createArtical(APIView):
    def post(self,request):
        try:
            print(request.data)
            artical.objects.get(title=request.data['title'])
            return Response("Artical Already Exsit")
        except:
            s=As(data=request.data)
            if(s.is_valid()):
                s.save()
                return Response("data Saved Successfulluy")
            else:
                 return Response(s.errors)

    def get(self,request):
        a=artical.objects.all()
        sa=As(a,many=True)
        return Response(sa.data)



def homepage(request):
    if(request.POST):
        data={
            'email':request.POST['email'],
            'password':request.POST['password'],
        }
        try:
            us=user.objects.get(email=data['email'],password=data['password'])
            if(us):
                if us.is_varified==False:
                    request.session['email']=data['email']
                    send_otp_via_mail(data['email'])
                    return redirect('/otp')
                else:
                    login_user={'email':us.email,'first_name':us.first_name,'last_name':us.last_name}
                    request.session['user']=login_user
                    return redirect('/homepage')
        except:
            messages.success(request,'wrong credintiel')
    a=artical.objects.all()[:2].filter()
    sa=As(a,many=True)
    b=artical.objects.all()[2:].filter()
    sb=As(b,many=True)
    publications=Publications.objects.all()
    publication_serializer=P_S(publications,many=True)
    if 'user' in request.session:
        return render(request,"base/homepage.html",{
            'articals':sa.data,
            'articals1':sb.data,
            'publications':publication_serializer.data,
            'user':request.session['user'],
        })
    else:
        return render(request,"base/homepage.html",{
            'articals':sa.data,
            'articals1':sb.data,
            'publications':publication_serializer.data,
        })

def membership(request):
    data=Aprea_memberships.objects.all()
    members=apm_ser(data,many=True)
    if 'user' in request.session:
        return render(request,'base/membership.html',{
            'membership':members.data,
            'user':request.session['user'],
        })
    else:
        return render(request, 'base/membership.html', {
            'membership': members.data

        })


def license(request):
    if 'user' in request.session:
        
        return render(request, 'base/license.html', {
            'license': True,
            'user':request.session['user'],
        })
    else:
        return render(request, 'base/license.html', {
            'license': True

        })


def insights(request):
    a=artical.objects.all()[:4].filter()
    sa=As(a,many=True)
    publications=Publications.objects.all()
    publication_serializer=P_S(publications,many=True)
    if 'user' in request.session:
        return render(request, 'base/insights.html', {
            'articals':sa.data,
            'publications':publication_serializer.data,
            'user':request.session['user'],
        })
    else:
        return render(request, 'base/insights.html', {
            'articals':sa.data,
            'publications':publication_serializer.data

        })


def medi(request):
    mediaa=media.objects.all()
    m_s=media_ser(mediaa,many=True)
    if 'user' in request.session:
        return render(request,'base/media.html',{
            'media':m_s.data,
            'user':request.session['user'],
        })
    else:
        return render(request, 'base/media.html', {
            'media': m_s.data
        })


def about(request):
    if(request.POST):
        data={
            'email':request.POST['email'],
            'password':request.POST['password'],
        }
        try:
            us=user.objects.get(email=data['email'],password=data['password'])
            if(us):
                if us.is_varified==False:
                    request.session['email']=data['email']
                    send_otp_via_mail(data['email'])
                    return redirect('/otp')
                else:
                    login_user={'email':us.email,'first_name':us.first_name,'last_name':us.last_name}
                    request.session['user']=login_user
                    return redirect('/about')
        except:
            messages.success(request,'wrong credintiel')
    a=artical.objects.all()[:2].filter()
    sa=As(a,many=True)
    b=artical.objects.all()[2:].filter()
    sb=As(b,many=True)
    publications=Publications.objects.all()
    publication_serializer=P_S(publications,many=True)
    if 'user' in request.session:
        return render(request, 'base/about.html', {
        'articals':sa.data,
        'articals1':sb.data,
        'publications':publication_serializer.data,
        'user':request.session['user']
    })
    else:
        return render(request, 'base/about.html', {
            'articals':sa.data,
            'articals1':sb.data,
            'publications':publication_serializer.data,

        })


def contributions(request):
    if(request.POST):
        data={
            'email':request.POST['email'],
            'password':request.POST['password'],
        }
        try:
            us=user.objects.get(email=data['email'],password=data['password'])
            if(us):
                if us.is_varified==False:
                    request.session['email']=data['email']
                    send_otp_via_mail(data['email'])
                    return redirect('/otp')
                else:
                    login_user={'email':us.email,'first_name':us.first_name,'last_name':us.last_name}
                    request.session['user']=login_user
                    return redirect('/contributions')
        except:
            messages.success(request,'wrong credintiel')
    if 'user' in request.session:
        return render(request,'base/contributions.html',{
            'user':request.session['user']
        })
    else:
        return render(request, 'base/contributions.html', {
            'contributions': True

        })




def uploader(request):
    return render(request, 'base/upload.html', {
        'uploader': True

    })

def sign(request):
    if(request.POST):
        dat={
                'first_name':request.POST['firstname'],
                'last_name':request.POST['lastname'],
                'email':request.POST['email'],
                'phonenumber':request.POST['phonenumber'],
                'password':request.POST['password'],
                }
        try:
            user.objects.get(email=dat['email'])
            messages.success(request,'Email Already Exsited Go To Login')
        except:
            u=us(data=dat)
            if(u.is_valid()):
                u.save()
                request.session['email']=dat['email']
                send_otp_via_mail(dat['email'])
                return redirect('/otp')
            else:
                messages.success(request,u.errors)
    return render(request,'base/signup.html',{
        })
    


def signin(request):
    if 'user' in request.session:
        return redirect('/homepage')
    if(request.POST):
        data={
            'email':request.POST['email'],
            'password':request.POST['password'],
        }
        try:
            us=user.objects.get(email=data['email'],password=data['password'])
            if(us):
                if us.is_varified==False:
                    request.session['email']=data['email']
                    send_otp_via_mail(data['email'])
                    return redirect('/otp')
                else:
                    login_user={'email':us.email,'first_name':us.first_name,'last_name':us.last_name}
                    request.session['user']=login_user
                    return redirect('/homepage')
        except:
            messages.success(request,'wrong credintiel')
    return render(request,'base/signin.html',{
    })

def conform_otp(request):
    if 'email' in request.session:
        if request.POST:
            otp=request.POST['f']+request.POST['s']+request.POST['t']+request.POST['fr']+request.POST['fv']+request.POST['sx']
            u=user.objects.get(email=request.session['email'])
            if(u.otp==otp):
                u.is_varified=True
                u.save()
                login_user={'email':u.email,'first_name':u.first_name,'last_name':u.last_name}
                request.session['user']=login_user
                return redirect('/homepage')
            else:
                print('wrong')
        return render(request,'base/otp.html',{})
    else:
        return redirect('/homepage')
    

def iin(request):
    if 'user' in request.session:
         return render(request,'base.html',{
        'user':request.session['user']
    })
    else:
        return render(request,'base.html',{
            'in':True
        })


def publication(request,id,*args, **kwargs):
    publicat=Publications.objects.get(id=id)
    p_s=P_S(publicat)
    if 'user' in request.session:
        return render(request,'base/blogpage.html',{
                'blog':p_s.data,
                'user':request.session['user']
            })    
    else:
        return render(request,'base/blogpage.html',{
            'blog':p_s.data
        })          


def articals(request,id,*args, **kwargs):
    try:
        if request.POST and request.POST['social_user_name']:
            context={
                'artical_id':id,
                'user_name':request.POST['social_user_name'],
                'email':request.POST['email'],
                'user_image':request.POST['social_user_pic'],
                'comment':request.POST['message']
            }
            new_comment=comment_ser(data=context)
            if new_comment.is_valid():
                new_comment.save()
    except:
        if request.POST and request.session['user']:
            context={
                'artical_id':id,
                'user_name':request.session['user']['first_name']+' '+request.session['user']['last_name'],
                'email':request.session['user']['email'],
                'user_image':'https://cdn-icons-png.flaticon.com/512/149/149071.png',
                'comment':request.POST['message']
            }
            new_comment=comment_ser(data=context)
            if new_comment.is_valid():
                new_comment.save()
    a=artical.objects.get(id=id)
    art_ser=As(a)
    comments=artical_comments.objects.filter(artical_id=id)
    all_coments=comment_ser(comments,many=True)
    if 'user' in request.session:
        return render(request,'base/blogpage.html',{
            'blog':art_ser.data,
            'comments':all_coments.data,
            'user':request.session['user']
        })
    else:
        return render(request,'base/blogpage.html',{
            'comments':all_coments.data,
            'blog':art_ser.data
        })


def presantation(request):
    return render(request,'base/presantation.html',{
        'pre':True
    })

def registermember(request):
    if request.POST:
        print(request.POST)

    return render(request,'base/registermember.html',{
        'registermember':True
    })


def page(request):
    if request.POST:
        data={
            'name':request.POST['first_name'],
            'last':request.POST['last_name']
        }
        pdf = render_to_pdf('base/page.html',data)
        return HttpResponse(pdf, content_type='application/pdf')


def signout(request):
    del request.session['user']
    return redirect('/')



def licensing_brokers(request):
    if 'user' in request.session:
        return render(request,'base/docs/licensing_brokers.html',{
            'user':request.session['user']
        })
    else:
        return render(request,'base/docs/licensing_brokers.html')
    


def education_stkholdr(request):
    if 'user' in request.session:
        return render(request,'base/docs/education_stakeholders.html',{
            'user':request.session['user']
        })
    else:
        return render(request,'base/docs/education_stakeholders.html')
    


def documenting_rei(request):
    if 'user' in request.session:
        return render(request,'base/docs/documenting_rei.html',{
            'user':request.session['user']
        })
    else:
        return render(request,'base/docs/documenting_rei.html')



def pakistan_rep(request):
    if 'user' in request.session:
        return render(request,'base/docs/pakistan_rep.html',{
            'user':request.session['user']
        })
    else:
        return render(request,'base/docs/pakistan_rep.html')
    

#it only show the erorr page if the url consist of single '/' like 'aprea.pk/abc' but 'aprea.pk/ad/ad/a/a' show 404 page not found

def error(request, slug):
    if 'user' in request.session:
        return render(request, 'base/error.html', {
            'message': slug,
            'user':request.session['user']
        })
    else:
         return render(request, 'base/error.html', {
            'message': slug,
        })


# def error_404_view(request, exception):
#     if 'user' in request.session:
#         return render(request, 'base/error.html', {
#             # 'message': slug,
#             'user':request.session['user']
#         })
#     else:
#          return render(request, 'base/error.html', {
#             # 'message': slug,
#         })


def ftel(request):
    if request.POST and request.POST['type']=='freelance':
        dat={'type_of_person':request.POST['type'],
        'lp_full_name':request.POST['FullName'],
        'lp_last_name':request.POST['LastName'],
        'lp_cnic':request.POST['cnic'],
        'lp_date_expiry':request.POST['date_of_expiriy'],
        'lp_date_birth':request.POST['date_of_birth'],
        'lp_email':request.POST['email'],
        'lp_address':request.POST['address'],
        'lp_phone':request.POST['phone_number'],
        'lp_job_type':request.POST['profession'],
        'lp_person_img':request.FILES['profile'],
        'lp_cnic_front':request.FILES['cnic-front'],
        'lp_cnic_back':request.FILES['cnic-back'],
        }
        pp=person_ser(data=dat)
        if pp.is_valid ():
            pp.save()
            p=license_Person.objects.get(lp_cnic=dat['lp_cnic'])
            p_s=person_ser(p)
            pdf = render_to_pdf('base/license/dashboard.html',p_s.data)
            p.delete()
            return HttpResponse(pdf, content_type='application/pdf')
        else:
            print(pp.errors)
    elif request.POST and request.POST['type']=='full_time_employer':
        dat={'type_of_person':request.POST['type'],
        'lp_full_name':request.POST['FullName'],
        'lp_last_name':request.POST['LastName'],
        'lp_cnic':request.POST['cnic'],
        'lp_date_expiry':request.POST['date_of_expiriy'],
        'lp_date_birth':request.POST['date_of_birth'],
        'lp_email':request.POST['email'],
        'lp_address':request.POST['address'],
        'lp_phone':request.POST['phone_number'], 
        'lp_person_img':request.FILES['profile'],
        'lp_cnic_front':request.FILES['cnic-front'],
        'lp_cnic_back':request.FILES['cnic-back'],
        }
        company_data={
            'lc_province':request.POST['province'],
            'lc_city':request.POST['City'],
            'lc_area':request.POST['area'],
            'lc_name':request.POST['company_name'],
            'lc_contact_no':request.POST['company_number'],
            'lc_address':request.POST['office_address'],
            'lc_website':request.POST['office_web']
            }

        print(company_data)
    return render(request,'base/license/ftel.html')


from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException



client_config = Configuration(
            host= "https://jdmw64.api.infobip.com",
            api_key={"APIKeyHeader": "19fda983a1c6f4e22586b0cb1c9ae886-599ab52f-1da0-464f-ac00-f6274d603748"},
            api_key_prefix={"APIKeyHeader": "App"},
        )
api_client = ApiClient(client_config)



def dashboard(request):
    sms_request = SmsAdvancedTextualRequest(
            messages=[
                SmsTextualMessage(
                    destinations=[
                        SmsDestination(
                            to="923058232080",
                        ),
                    ],
                    _from="InfoSMS",
                    text="sorry for disturbing you!",
                )
            ])
    SendSmsApi(api_client).send_sms_message(sms_advanced_textual_request=sms_request)
    return render(request,'base/license/dashboard.html')

