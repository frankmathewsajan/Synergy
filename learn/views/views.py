from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from learn.models import StudyGroup, Event



def index(request):
    if request.user.is_authenticated:
        return render(request, "learn/index.html", {
            'groups': StudyGroup.objects.all()
        })
    else:
        return redirect('login')


@login_required
def new_group(request):
    if request.method == 'POST':
        class_name = request.POST['class_name']
        description = request.POST['description']
        subject = request.POST['subject']
        owner = request.user  # Assuming the logged-in user is the owner

        # Check if a StudyGroup with the same class_name and subject already exists
        if StudyGroup.objects.filter(class_name=class_name, subject=subject).exists():
            # Optionally, add a message to inform the user
            # messages.error(request, "A group with this class name and subject already exists.")
            return redirect('group_exists')  # Replace 'group_exists' with your URL name

        # Create a new StudyGroup
        study_group = StudyGroup(
            class_name=class_name,
            description=description,
            subject=subject,
            owner=owner
        )
        study_group.save()

        # Redirect to the new group's page
        return redirect('group_detail', group_id=study_group.id)  # Replace 'group_detail' with your URL name

    return render(request, "learn/groups/new.html")


def group_detail(request, group_id):
    study_group = StudyGroup.objects.get(id=group_id)
    return render(request, "learn/groups/detail.html", {'group': study_group})


def groups(request):
    user_groups = StudyGroup.objects.filter(members=request.user) | StudyGroup.objects.filter(
        owner=request.user)
    return render(request, "learn/groups/all.html", {'group': user_groups})


def events(request):
    # Slicing the QuerySet to get only the first 11 events.
    events_data = Event.objects.all()[:11]
    return render(request, "learn/events.html", {'events': events_data})


# Uncomment or adjust these if you have such models:
# from .models import Material, ChatMessage

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # For demo purposes, if you don't have Material and ChatMessage models,
    # you can pass empty lists.
    materials = []  # Replace with: Material.objects.filter(event=event)
    chat_messages = []  # Replace with: ChatMessage.objects.filter(event=event)

    return render(request, "learn/events/detail.html", {
        'event': event,
        'materials': materials,
        'chat_messages': chat_messages,
        'user': request.user,  # This ensures the template has access to the current user.
    })
