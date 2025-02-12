from .models import StudyGroup


def study_groups(request):
    if request.user.is_authenticated:
        return {
            'groups': StudyGroup.objects.filter(members=request.user) | StudyGroup.objects.filter(
                owner=request.user)
        }
    return {'groups': []}
