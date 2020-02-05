from django.shortcuts import render, redirect
from .forms import UserForm, EmployeeForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from IMS.custom_decorators import role_required, admin_only

# Create your views here.
@login_required
@role_required(allowed_roles=['Admin', 'HR'])
def employee_list(request):
    employees = User.objects.all()
    # Pagination
    paginator = Paginator(employees, 1)
    page = request.GET.get('page')
    paged_employees = paginator.get_page(page)
    context = {
        "employees": paged_employees,
    }
    return render(request, "employees/employee_list.html", context)

@login_required
@role_required(allowed_roles=['Admin', 'HR'])
def employee_detail(request, employee_id):
    single_employee = User.objects.get(id=employee_id)
    context = {
        "single_employee": single_employee
    }
    return render(request, "employees/employee_detail.html", context)

@login_required
@role_required(allowed_roles=['Admin', 'HR'])
def add_employee(request):
    if request.method == "POST":
        user_forms = UserForm(request.POST)
        if user_forms.is_valid():
            user_forms.save()
            return redirect("employee_list")
    else:
        user_forms = UserForm()
    context = {
        "user_forms": user_forms
    }
    return render(request, "employees/add_employee.html", context)

@login_required
@role_required(allowed_roles=['Admin', 'HR'])
def edit_employee(request, employee_id):
    employee_edit = User.objects.get(id=employee_id)
    edit_employee_forms = UserForm(instance=employee_edit)

    if request.method == "POST":
        edit_employee_forms = UserForm(request.POST, request.FILES or None, instance=employee_edit)

        if edit_employee_forms.is_valid():
            edit_employee_forms.save()
            return redirect("employee_list")

    context = {
        "edit_employee_forms": edit_employee_forms
    }
    return render(request, "employees/edit_employee.html", context)

@login_required
@role_required(allowed_roles=['Admin', 'HR'])
def delete_employee(request, employee_id):
    employee_delete = User.objects.get(id=employee_id)
    if request.method == "POST":
        employee_delete.delete()
        return redirect("employee_list")
    context = {
        "employee_delete": employee_delete
    }
    return render(request, "employees/delete_employee.html", context)

@login_required
def account_settings(request):
    employee_settings = request.user.profile
    forms = EmployeeForm(instance=employee_settings)
    if request.method == "POST":
        forms = EmployeeForm(request.POST, request.FILES, instance=employee_settings)
        if forms.is_valid():
            forms.save()
            return redirect("profile_settings")
    context = {
        "forms": forms
    }
    return render(request, "employees/account_settings.html", context)

@login_required
def profile_settings(request):
    employee_profile = request.user.profile
    context = {
        "employee_profile": employee_profile
    }
    return render(request, "employees/profile_settings.html", context)

