from django.shortcuts import render,HttpResponse,redirect
from.models import ShopOwner,ShopDetail,MedicineRequest
from django.contrib import messages


def owner_edit_profile(request):
   if request.method=='GET':
      owner_email=request.session["owner_key"]
      owner_obj=ShopOwner.objects.get(email=owner_email)
      owner_dict={"owner_info":owner_obj}
      return render(request,'medi_app/shopowner/owner_edit_profile.html',owner_dict)
   
   if request.method=='POST':
      profile_pic=request.FILES.get("pic")
      owner_phone=request.POST["phone"]
      owner_name=request.POST["name"]
      owner_email=request.session["owner_key"]
      owner_obj=ShopOwner.objects.get(email=owner_email)
      if profile_pic is not None:
         owner_obj.pic_name=profile_pic # if user ki pic is not none then return new or the unchanged profile pic so that old image remains as it is
      owner_obj.name=owner_name
      owner_obj.phone=owner_phone
      owner_obj.save()
      messages.success(request," Profile Updated Successfully")
      return redirect("home page") ##### logical name of page is enterd








def view_medicine_request(request):
   if request.method=="GET":
      medicine_list=MedicineRequest.objects.filter(medicine_status="REQUESTED")
      medicine_dict={"medicine_request":medicine_list}

      return render(request,'medi_app/shopowner/view_medicine_request.html',medicine_dict)
      




def map_location(request):
   if request.method=="GET":
      return render(request,'medi_app/shopowner/map_location.html')
   if request.method=="POST":
      owner_email=request.session["owner_key"]
      owner_obj =ShopOwner.objects.get(email=owner_email)
      print(owner_obj)
      longitude=request.POST["longitude"]
      latitude=request.POST["lat"]
      print(longitude)
      print(latitude)
      shop_detail_obj= ShopDetail.objects.get(owner=owner_obj)

      shop_detail_obj.location_lat=latitude
      shop_detail_obj.location_long=longitude  ##### saved like this to know that the longitude and latitude is of a particular owner
      shop_detail_obj.save()
       


   owner_dict={"owner_info": owner_obj}

   return render(request,'medi_app/shopowner/owner_home.html',owner_dict)
 

 
       
    
   
   
def view_shopkeeper(request):
   if request.method=="GET":

    return render(request,'medi_app/user/view_shopkeeper.html')
    
   
def shop_detail(request):
   if request.method=="GET":
      return render (request,'medi_app/shopowner/shop_detail.html')
   if request.method=="POST":
   
      Shopname=request. POST["name"]
      gstno=request. POST["number"]
      description=request.POST["description"]
      phone=request. POST["phone"]
      city=request. POST["city"]
      address=request. POST["address"]
      email=request.session["owner_key"] ###for getting a person's email
      owner_obj=ShopOwner.objects.get(email=email)  ###second email is of upr joh bni , first wla model mei joh hai
      shop_detail_obj=ShopDetail(owner=owner_obj,shop_name=Shopname,gst_number=gstno,description=description,phone_no=phone,city=city,address=address)
      shop_detail_obj.save()
      messages.success(request,"👍 Thank You For Your details👍")
      return redirect("map_location")
      
       



def owner_logout(request):
   request.session.flush()#flush function kills/destroys the session
   messages.success(request,"Successfully Logged Out,Thank you")
   return redirect("owner_login_form")



def  owner_reg(request):

      if request.method=="GET":###http protocol's method

       return render(request,'medi_app/shopowner/owner_registration.html')
      if request.method=="POST":
       owner_name= request.POST["name"]#### it will read data from textbox
       owner_email=request.POST["email"]
       owner_password=request.POST["password"]
       owner_phone=request.POST["phone"]
       owner_pic=request.FILES.get("profile_pic")
      owner_reg_obj=ShopOwner(name=owner_name,email=owner_email, password=owner_password,phone=owner_phone,pic_name=owner_pic)
      owner_reg_obj.save()### it will store data into data base table
      messages.success(request,"👍 Thank You For Your Registration👍")
     #   return render(request,'medi_app/user/user_registration.html')#### when we dont take any data then only we write it
      return redirect("owner_login_form")### logical name of url endpoint
      
def owner_login(request):
     if request .method=="GET":
      return render (request, 'medi_app/shopowner/owner_login.html')
     if request.method=="POST":
        email=request.POST["owner_email"]
        password=request.POST["owner_pass"]
        ownerList=ShopOwner.objects.filter(email=email,password=password)

        if len(ownerList)>0:
           owner_object =ownerList[0]
           ###session
           request.session["owner_key"]=email
           messages.success(request,"👍 ThankYou Your location registerd sucssesfully 👍")

          #  request.session["user_role"]="user" #### just for understanding that we can give manay role for authenthication 
           return redirect("home page") 
        else:
           messages.error(request,"💀invalid credentials")
           return redirect("owner_login_form")

        
def owner_home(request):
     if request.method=="GET":  
#### fetch/get the value from session 
       owner_email=request.session["owner_key"]
       owner_obj =ShopOwner.objects.get(email=owner_email)

       ####sending object from view to template(html)as we have to show the details of user for which get will be used
       ## create a dictionary and bind object with a key  and then send the dictionary (WAY TO GO FROM VIEW TO TEMPLATE (HTML))

       owner_dict={"owner_info": owner_obj}
       

     return render(request,'medi_app/shopowner/owner_home.html',owner_dict)
     
