from django.shortcuts import render,redirect
from .forms import RegistrationForm,ReceiptForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Receipt
# Create your views here.

@login_required(login_url="/login/")
def listView(request): 
    # check the method of the request
    # in case of post method
    # the delete button must be clicked
    # get the id of the receipt to be deleted
    # get the instance 
    # delete it 
    # rerender the page

    # else get all the instances or receipts ownd by the user
    # render the receipts in the receipts page

    if request.method == "POST":
        if "delete" in request.POST:
            pk = request.POST.get("delete")
            Receipt.objects.get(author=request.user.id,id=pk).delete()
    receipts = Receipt.objects.filter(author = request.user)
   
    return render(request,"receipt/listReceipt.html",{"receipts":receipts})

@login_required(login_url="/login/")
def detailView(request,pk):    
    if(request.method == "GET"):
        try:
            receipts = Receipt.objects.get(author = request.user ,id = pk)
            print(receipts)
            return render(request,"receipt/detailReceipt.html",{"receipt":receipts})
        except:
            return redirect("/receipts")

@login_required(login_url="/login/")
def edit_recipt(request,pk):
    if pk == None:
        # you can't access this page without an id
        return redirect("/receipts")

    if(request.method == "GET"):
        try:
            # get the receipt to be edited
            # populate an new form
            # render the form

            receipt = Receipt.objects.get(author= request.user.id,id=pk)
            form = ReceiptForm(instance=receipt)
            return render(request,"receipt/edit_receipt.html",{"form":form,"data":receipt})
        except Exception as e:
            # this receipt may not exist or the user don't own it
            print(e)
            return redirect("/receipts")
    if(request.method == "POST"):
        try:
            # ge tthe receipt to be edited
            # populate a form with the posted data and the old data
            # save the form
            # redirect to /receipts/

            receipt = Receipt.objects.get(author = request.user.id,id = pk)
            form = ReceiptForm(request.POST,instance=receipt)
            form.save()
            return redirect("/receipts")           

        except Exception as e:
            print(e)
            return redirect("/receipts")            
            
@login_required(login_url="/login/")
def addRecipt(request,pk=None):
    if(request.method=="GET"):
        # create an empty form
        # render the form

        form = ReceiptForm()
        return render(request,"receipt/add_receipt.html",{"form":form})
    elif(request.method == "POST"):
        # create new form populated with the posted data
        # validate the form
        # save the form
        # redirect to /receipts/

        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.author = request.user
            receipt.save()
            return  redirect("/receipts/")

def signup(request):
    # create a form populated with the posted data
    # validate the form 
    # create a new user
    # redirect to /receipts/
    #     
    if(request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(type(user))
            login(request ,user)
            return redirect("/home")
        
    # create an empty signup form
    # render the form
    else:
        form = RegistrationForm()
        return render(request,"registration/signup.html",{"form":form})