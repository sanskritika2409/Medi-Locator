from django.shortcuts import render,HttpResponse
from.models import Contact,FeedBack

# Create your views here.
def all_feedback(request):
    
  feedback_list=FeedBack.objects.all()####it will fetch all the data from the object model 
  feedback_dict={
     
     "feedback_key":feedback_list
  }######here it is fulll list

  return render (request,"medi_app/html/all_feedback.html",feedback_dict)





def home (request):
    # return HttpResponse("<h1> This is home page </h1>")
    return render (request,'medi_app/html/index.html')
def about_us(request):
     return render (request,'medi_app/html/about_us.html')
def contact_us (request):
    if request.method=="GET":###http protocol's method

      return render(request,'medi_app/html/contactus.html')
    if request.method=="POST":
       user_name= request.POST["name"]#### it will read data from textbox
       user_email=request.POST["email"]
       user_question=request.POST["question"]
       user_phone=request.POST["phone"]
       contact_us_obj=Contact(email=user_email,name=user_name,phone=user_phone,question=user_question)
       contact_us_obj.save()### it will store data into data base table
       return render(request,'medi_app/html/contactus.html')
    




     

    