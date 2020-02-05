from .models import Profile

def total_employee_count(request):
    total_employee = Profile.objects.count()
    return {"total_employee_count": total_employee}

