from django.shortcuts import render,HttpResponse,redirect
from.models import FeedBack,User,MedicineRequest,ShopDetail
from django.contrib import messages


def user_edit_profile(request):
   if request.method=='GET':
      user_email=request.session["user_key"]
      user_obj=User.objects.get(email=user_email)
      user_dict={"user_info":user_obj}
      return render(request,'medi_app/user/user_edit_profile.html',user_dict)
   
   if request.method=='POST':
      profile_pic=request.FILES.get("pic")
      user_phone=request.POST["phone"]
      user_name=request.POST["name"]
      user_email=request.session["user_key"]
      user_obj=User.objects.get(email=user_email)
      if profile_pic is not None:
         user_obj.pic_name=profile_pic # if user ki pic is not none then return new or the unchanged profile pic so that old image remains as it is
      user_obj.name=user_name
      user_obj.phone=user_phone
      user_obj.save()
      messages.success(request," Profile Updated Successfully")
      return redirect("user_home")








def update_status(request,id):
   if request.method=="GET":
      medicine_obj=MedicineRequest.objects.get(id=id)
      medicine_obj.medicine_status="RECIEVED"
      medicine_obj.save()
      messages.success(request,"status updated")
      return redirect("update_medicine")
     
   
 
   





def update_medicine(request):
   if request.method=="GET":
          user_email=request.session["user_key"]  ###getting email from seesion
          medicine_list= MedicineRequest.objects.filter(user_email=user_email)
      
          medicine_dict={"medicine_detail": medicine_list}
          return render (request,'medi_app/user/update_medicine.html',medicine_dict)

def medicine_request(request):
   if  request.method=="GET":
        user_email=request.session["user_key"]  ###getting email from seesion
       # user_obj=User.objects.get(email=user_email)#####when need email on the page to be there
        user_dict={"user_detail": user_email}
        return render(request,'medi_app/user/medicine_request.html',user_dict)


   if request.method=="POST":
      user_email=request.POST["email"]
      whatsapp_num=request.POST["number"]
      medicine_name=request.POST["med-name"]
      doc=request.POST["doc-name"]
      user_message=request.POST["message"]
      medicine_request_obj=MedicineRequest(user_email=user_email,user_whatsapp=whatsapp_num,medicine_name=medicine_name,refer_doctor_name=doc,user_message=user_message)
      medicine_request_obj.save()
      messages.success(request,"Medicine Request successfully")
      return render( request,'medi_app/user/medicine_request.html')
      

    
   



def view_map(request):
    data = ShopDetail.objects.all()  # Fetch all users from the database
    user_data = []

    for user in data:
        user_data.append({
          
            'shop_name': user.shop_name,
            'lat': user.location_lat,
            'log': user.location_long,
            "icon_class":"fas fa-home",
            "description":user.description,
            
        })
    
 
    return render(request, 'medi_app/user/view_map.html', {
        'users': user_data,
    })

   




def user_logout(request):
   request.session.flush()#flush function kills/destroys the session
   messages.success(request,"Successfully Logged Out,Thank you")
   return redirect("login form")

def reg_form(request):

      if request.method=="GET":###http protocol's method

       return render(request,'medi_app/user/user_registration.html')
      if request.method=="POST":
       user_name= request.POST["name"]#### it will read data from textbox
       user_email=request.POST["email"]
       user_password=request.POST["password"]
       user_phone=request.POST["phone"]
       user_pic=request.FILES.get("profile_pic")
       reg_form_obj=User(name=user_name,email=user_email, password=user_password,phone=user_phone,pic_name=user_pic)
       reg_form_obj.save()### it will store data into data base table
       messages.success(request,"👍 Thank You For Your Registration👍")
     #   return render(request,'medi_app/user/user_registration.html')#### when we dont take any data then only we write it
       return redirect("login form")### logical name of url endpoint
      
def login_form(request):
     if request .method=="GET":
      return render (request, 'medi_app/user/user_login.html')
     if request.method=="POST":
        user_email=request.POST["email"]
        user_pass=request.POST["password"]
        userList=User.objects.filter(email=user_email,password=user_pass) #### filtering the login data 

        if len(userList)>0:
           user_object =userList[0]
           ###session
           request.session["user_key"]=user_email
          #  request.session["user_role"]="user" #### just for understanding that we can give manay role for authenthication 
           return redirect("user_home") 
        else:
           messages.error(request,"💀invalid credentials")
           return redirect("login form")


def user_feedback(request):
    if request.method=="GET":###http protocol's method
      user_email=request.session["user_key"]  ###getting email from seesion
      user_obj=User.objects.get(email=user_email)#####when need email on the page to be there
      user_dict={"user_detail": user_obj}
      return render(request,'medi_app/user/user_feedback.html',user_dict)
    if request.method=="POST":
       user_name= request.POST["name"]#### it will read data from textbox
       user_email=request.POST["email"]
       user_query=request.POST["query"]
       user_rating=request.POST["rating"]
       user_pic=request.POST["pic_path"]
       feedback_obj=FeedBack(email=user_email,name=user_name, rating=user_rating,query=user_query,user_pic=user_pic)
       feedback_obj.save()### it will store data into data base table
       messages.success(request,"👍 Thank You For Your Feedback👍")
     #   return render(request,'medi_app/user/user_feedback.html')#### when we dont take any data then only we write it
       return redirect("feedback form")### logical name of url endpoint
        
def user_home(request):
     if request.method=="GET":  
#### fetch/get the value from session 
       user_email=request.session ["user_key"]
       user_obj =User.objects.get(email=user_email)

       ####sending object from view to template(html)as we have to show the details of user for which get will be used
       ## create a dictionary and bind object with a key  and then send the dictionary (WAY TO GO FROM VIEW TO TEMPLATE (HTML))

       user_dict={"user_info": user_obj}
       

     return render(request,'medi_app/user/user_home.html',user_dict)