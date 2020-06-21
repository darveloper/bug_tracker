from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ticket
from .forms import TicketForm, EditTicketForm
from accounts.models import User



# def index(request):
#     tickets = Ticket.objects.all()
#     return render(request, 'home.html', {'tickets': tickets})


def add_new_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            p = Ticket.objects.create(title=title, description=description)
        form = TicketForm()
    return render(request, 'add.html', {'form': form})

def edit_ticket(request, id):
    form = EditTicketForm()
    if request.method == 'POST':
        form = EditTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.filter(id=id).update(
                title=data['title'],
                description=data['description'],
                status = 'In Progress',
                assigned_to=data['assigned_to']
            )
            form = EditTicketForm()
            return redirect('home')
    else:
        form = EditTicketForm()
    
    return render(request, 'add.html', {'form': form})

def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})

def completed_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.completed_by = ticket.assigned_to
    ticket.assigned_to = None
    ticket.status = 'Done'
    ticket.save()
    return redirect('home')

def invalid_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = 'Invalid'
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.save()
    return redirect('home')

def user_page(request, id):
    user = User.objects.get(id=id)
    current_tickets = Ticket.objects.filter(assigned_to=user)
    filed_tickets = Ticket.objects.filter(filed_by=user)
    completed_tickets = Ticket.objects.filter(completed_by=user)
    return render(request, 'userpage.html', {
        'user': user,
        'current_tickets': current_tickets,
        'filed_tickets': filed_tickets,
        'completed_tickets': completed_tickets
        })

def index(request):
    new_tickets = Ticket.objects.filter(status=Ticket.new).order_by("-date")
    in_progress_tickets = Ticket.objects.filter(status=Ticket.in_progress).order_by("-date")
    done_tickets = Ticket.objects.filter(status=Ticket.done).order_by("-date")
    invalid_tickets = Ticket.objects.filter(status=Ticket.invalid).order_by("-date")
    return render(request, 'home.html', {
        'new_tickets': new_tickets,
        'in_progress_tickets': in_progress_tickets,
        'done_tickets': done_tickets,
        'invalid_tickets': invalid_tickets
    })