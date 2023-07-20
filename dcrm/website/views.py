from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm, AddDealForm, AddNoteForm
from .models import Record, Deal, Task




def home(request):
    records = Record.objects.all()
    deals = Deal.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in!")
            return redirect('home')
        else:
            messages.success(request, "Error. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records, 'deals':deals})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out...")
    return redirect('home')


def contact(request):
    records = Record.objects.all()
    if request.user.is_authenticated:
        return render(request, 'contact.html', {'records':records})
    else:
        messages.success(request, "You must be logged in to view records.")
        return redirect('home')



def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view records.")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Deleted.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete records.")
        return redirect('home')
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Added")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')
    

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated.")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')
    

def deal(request):
    deals = Deal.objects.all()
    if request.user.is_authenticated:
        return render(request, 'deal.html', {'deals':deals})
    else:
        messages.success(request, "You must be logged in to view deals.")
        return redirect('home')
    

def add_deal(request):
    form1 = AddDealForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form1.is_valid():
                add_deal = form1.save()
                messages.success(request, "Added")
                return redirect('deal')
        return render(request, 'add_deal.html', {'form1':form1})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')
    

def deal_record(request, pk):
    if request.user.is_authenticated:
        deal_record = Deal.objects.get(id=pk)
        return render(request, 'deal_record.html', {'deal_record':deal_record})
    else:
        messages.success(request, "You must be logged in to view records.")
        return redirect('home')
    

def update_deal(request, pk):
    if request.user.is_authenticated:
        current_deal = Deal.objects.get(id=pk)
        form1 = AddDealForm(request.POST or None, instance=current_deal)
        if form1.is_valid():
            form1.save()
            messages.success(request, "Updated.")
            return redirect('deal')
        return render(request, 'update_deal.html', {'form1':form1})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')
    

def delete_deal(request, pk):
    if request.user.is_authenticated:
        delete_it = Deal.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Deleted.")
        return redirect('deal')
    else:
        messages.success(request, "You must be logged in to delete records.")
        return redirect('deal')
    
def add_note(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form2 = AddNoteForm(request.POST or None, instance=current_record)
        if form2.is_valid():
            form2.save()
            messages.success(request, "Added note.")
            return redirect('home')
        return render(request, 'add_note.html', {'form2':form2})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')

def task_list(request):
    tasks = Task.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            for task in tasks:
                task_id = str(task.id)
                if task_id in request.POST:
                    task.completed = True
                else:
                    task.completed = False
                task.save()
        return render(request, 'task_list.html', {'tasks':tasks})
    else:
        messages.success(request, "You must be logged in to view deals.")
        return redirect('home')

def add_task(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            Task.objects.create(name=name)
            messages.success(request, "Added")
        return redirect('task_list')
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')

def delete_task(request, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(pk=task_id)
        task.delete()
        messages.success(request, "Deleted")
        return redirect('task_list')
    else:
        messages.success(request, "You must be logged in to delete records.")
        return redirect('deal')

