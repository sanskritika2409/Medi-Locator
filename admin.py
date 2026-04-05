from django.contrib import admin

# Register your models here.
from . models import FeedBack,Contact,User,ShopOwner,ShopDetail,MedicineRequest

#inheritance of sub class from super below ModelAdmin is superclass
#class banake ke inherit and take all those variables from model u want admin to see
class FeedBack_Admin(admin.ModelAdmin):
     list_display=["name","email","rating","query","date"]

class Contact_Admin(admin.ModelAdmin):
     list_display=["name","email","phone","question","date"]

class User_Admin(admin.ModelAdmin):
     list_display=["name","email","phone"]

class ShopOwner_Admin(admin.ModelAdmin):
     list_display=["name","email","phone"]

class ShopDetail_Admin(admin.ModelAdmin):
     list_display=["owner","shop_name","phone_no","gst_number","address","city"]

class MedicineRequest_Admin(admin.ModelAdmin):
     list_display=["user_email","user_whatsapp","medicine_name","refer_doctor_name","medicine_status","user_message"]

admin.site.register(FeedBack,FeedBack_Admin)###binding the data
admin.site.register(Contact,Contact_Admin)
admin.site.register(User,User_Admin)
admin.site.register(ShopOwner,ShopOwner_Admin)
admin.site.register(ShopDetail,ShopDetail_Admin)
admin.site.register(MedicineRequest,MedicineRequest_Admin)


admin.site.site_header="Medilocator Dashboard"
admin.site.site_title="Find Nearby Pharmacy"
admin.site.index_title="Pharmacy Nearby"

