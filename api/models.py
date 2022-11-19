from distutils.command.upload import upload
from email.policy import default
from django.db import models
from datetime import date

class user(models.Model):
    email=models.EmailField(max_length=254)
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64,default='nan')
    phonenumber=models.CharField(max_length=110,blank=True)
    password=models.CharField(max_length=5000000000)
    is_varified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6,blank=True)
    picture=models.ImageField(upload_to='user/',blank=True)

    def __str__(self):
        return self.email



class artical(models.Model):
    author=models.CharField(max_length=64)
    category=models.CharField(max_length=64)
    discription=models.CharField(max_length=5000)
    title=models.CharField(max_length=100)
    picture=models.ImageField(upload_to='images/')
    date=models.CharField(max_length=64,default=date.today())


    def __str__(self):
        return self.title
    


class Publications(models.Model):
    picture=models.ImageField(upload_to='publication/')
    title=models.CharField(max_length=100)
    discription=models.CharField(max_length=5000)
    url=models.URLField(max_length=2097152)
    date=models.DateField()

    def __str__(self):
        return self.title


class media(models.Model):
    picture=models.ImageField(upload_to='gallery/')
    title=models.CharField(max_length=100,default="untitled")
    url=models.URLField(max_length=2097152,blank=True,default="")

    def __str__(self):
        return self.title


class Aprea_memberships(models.Model):
    type_of_organization=models.CharField(max_length=50,choices=[('Association','Association'),('Union','Union'),('Group','Group')])
    organization_name=models.CharField(max_length=400,unique=True)
    province=models.CharField(max_length=400)
    city=models.CharField(max_length=400)
    area=models.CharField(max_length=400,blank=True)
    organization_logo=models.ImageField(upload_to='organization_logo/',blank=True)
    certificate=models.ImageField(upload_to='certifcate/',blank=True)
    register_with=models.CharField(max_length=100,blank=True)
    formed_through=models.CharField(max_length=100,blank=True,choices=[('Elections','Elections'),('By will','By will'),('Other','Other')])
    registerd_voters=models.IntegerField(default=0)
    total_agents=models.IntegerField(default=0)
    focal_person_name=models.CharField(max_length=100,blank=True)
    focal_person_number=models.IntegerField(default=0)
    office_address=models.CharField(max_length=5000,blank=True)
    nearest_landmark=models.CharField(max_length=5000,blank=True)
    website=models.URLField(blank=True)
    social_media_url=models.URLField(blank=True)

    a_member_image=models.ImageField(upload_to='members/',blank=True)
    a_cnic_front=models.ImageField(upload_to='cnic/',blank=True)
    a_cnic_back=models.ImageField(upload_to='cnic/',blank=True)
    a_member_type=models.CharField(max_length=100,choices=[
        ('President','President'),('Chairman','Chairman'),('Vice President','Vice President'),
        ('Vice Chairman','Vice Chairman'),('General Secretary','General Secretary')])
    a_full_name=models.CharField(max_length=254)
    a_cnic=models.IntegerField(default=0)
    a_date_of_issue=models.DateField(default=0)
    a_busniess_name=models.CharField(max_length=250,blank=True)
    a_email=models.EmailField(max_length=254,blank=True)
    a_contact_number=models.IntegerField(default=0)
    a_busniess_address=models.CharField(max_length=5000,blank=True)

    b_member_image=models.ImageField(upload_to='members/',blank=True)
    b_cnic_front=models.ImageField(upload_to='cnic/',blank=True)
    b_cnic_back=models.ImageField(upload_to='cnic/',blank=True)
    b_member_type=models.CharField(max_length=100,choices=[
        ('President','President'),('Chairman','Chairman'),('Vice President','Vice President'),
        ('Vice Chairman','Vice Chairman'),('General Secretary','General Secretary')])
    b_full_name=models.CharField(max_length=254)
    b_cnic=models.IntegerField(default=0)
    b_date_of_issue=models.DateField(default=0)
    b_busniess_name=models.CharField(max_length=250,blank=True)
    b_email=models.EmailField(max_length=254,blank=True)
    b_contact_number=models.IntegerField(default=0)
    b_busniess_address=models.CharField(max_length=5000,blank=True)

    c_member_image=models.ImageField(upload_to='members/',blank=True)
    c_cnic_front=models.ImageField(upload_to='cnic/',blank=True)
    c_cnic_back=models.ImageField(upload_to='cnic/',blank=True)
    c_member_type=models.CharField(max_length=100,choices=[
        ('President','President'),('Chairman','Chairman'),('Vice President','Vice President'),
        ('Vice Chairman','Vice Chairman'),('General Secretary','General Secretary')])
    c_full_name=models.CharField(max_length=254)
    c_cnic=models.IntegerField(default=0)
    c_date_of_issue=models.DateField(default=0)
    c_busniess_name=models.CharField(max_length=250,blank=True)
    c_email=models.EmailField(max_length=254,blank=True)
    c_contact_number=models.IntegerField(default=0)
    c_busniess_address=models.CharField(max_length=5000,blank=True)

    def __str__(self):
        return self.organization_name




# class organization_members(models.Model):
#     organization_name=models.ForeignKey(Aprea_membership, on_delete=models.CASCADE)
#     member_image=models.ImageField(upload_to='members/',blank=True)
#     cnic_front=models.ImageField(upload_to='cnic/',blank=True)
#     cnic_back=models.ImageField(upload_to='cnic/',blank=True)
#     member_type=models.CharField(max_length=100)
#     full_name=models.CharField(max_length=254)
#     cnic=models.IntegerField(default=0)
#     date_of_issue=models.DateField(default=0)
#     busniess_name=models.CharField(max_length=250,blank=True)
#     email=models.EmailField(max_length=254,blank=True)
#     contact_number=models.IntegerField(default=0)
#     busniess_address=models.CharField(max_length=5000,blank=True)

#     def __str__(self):
#         return self.full_name


class license_Person(models.Model):
    type_of_person=models.CharField(max_length=90)
    lp_full_name=models.CharField(max_length=128)
    lp_last_name=models.CharField(max_length=128)
    lp_cnic=models.CharField(max_length=15)
    lp_date_expiry=models.CharField(max_length=10)
    lp_date_birth=models.CharField(max_length=10)
    lp_email=models.EmailField(max_length=254,unique=True)
    lp_address=models.CharField(max_length=999)
    lp_phone=models.CharField(max_length=20)
    lp_job_type=models.CharField(max_length=99,blank=True)
    lp_person_img=models.ImageField(upload_to='license/lp_profile_img/',blank=True)
    lp_cnic_front=models.ImageField(upload_to='license/cnic/', blank=True)
    lp_cnic_back=models.ImageField(upload_to='license/cnic/', blank=True)
    
 
class license_Company(models.Model):
    lc_province=models.CharField(max_length=20)
    lc_city=models.CharField(max_length=78)
    lc_area=models.CharField(max_length=599)
    lc_name=models.CharField(max_length=200)
    lc_contact_no=models.CharField(max_length=20)
    lc_address=models.CharField(max_length=999)
    lc_website=models.CharField(max_length=1000)
    lc_logo=models.ImageField(upload_to='Comapny/logo/',blank=True)
    lc_secp=models.ImageField(upload_to='Company/doc/SECP',blank=True)
    lc_letter=models.ImageField(upload_to='Company/doc/letter',blank=True)
    lc_exprience=models.ImageField(upload_to='Company/doc/exprience',blank=True)



class artical_comments(models.Model):
    artical_id=models.IntegerField()
    user_name=models.CharField(max_length=54,blank=False)
    email=models.EmailField(max_length=254,blank=False)
    user_image=models.CharField(max_length=999999999999,blank=True)
    comment=models.CharField(max_length=98765,blank=False)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.user_name