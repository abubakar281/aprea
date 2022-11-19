from distutils.command.upload import upload
from unicodedata import name
from django.urls import path
from . import views
from .views import education_stkholdr, licensing_brokers, page, presantation,articals, publication,registermember, contributions, homepage, iin, insights, medi, about, membership, license, homepage, sign, signin, signout, uploader

urlpatterns = [
    path("signups",views.signup.as_view()),
    path('homepage', homepage, name="homepage"),
    path('', homepage, name="homepage"),
    path('media', medi, name="media"),
    path('contributions', contributions, name="contributions"),
    path('about', about, name="about"),
    path('memberships', membership, name="membership"),
    path('license', views.ftel, name="license"),
    path('insights', insights, name="insights"),
    path('createartical',views.createArtical.as_view()),
    path('upload',uploader,name='uploader'),
    path('signup',sign,name='signup'),
    path('signin',signin,name='signin'),
    path('publications/<int:id>/',publication,name='publications'),
    path('articals/<int:id>/',articals,name='articals'),
    # path('in',iin,name='in'),
    path('presantation',presantation,name='presantation'),
    path('registermember',registermember,name='registermember'),
    # path('page/',page,name='page'),
    path('otp',views.conform_otp,name='otp'),
    path('signout',views.signout,name='signout'),
    path('licensing_brokers',views.licensing_brokers,name='licensing_brokers'),
    path('education_stakeholders',views.education_stkholdr,name='education_stakeholders'),
    path('documenting_rei',views.documenting_rei,name='documenting_rei'),
    path('pakistan_rep',views.pakistan_rep,name='pakistan_rep'),
    path('ftel',views.ftel,name='full_time_employee_license'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('<slug>', views.error, name="error"),
]

