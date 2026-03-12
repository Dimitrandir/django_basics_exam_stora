from django.shortcuts import render, redirect, get_object_or_404
from STORA.accounts.models import Employee
from STORA.accounts.forms import AccountsForms


def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}

    return render(request,'accounts/employee_list.html', context)

def employee_add(request):
    if request.method == 'POST':
        form = AccountsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = AccountsForms()

    context = {'form':form}
    return render(request, 'accounts/employee_add.html', context)


def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    context = {'employee': employee}
    return render(request, 'accounts/employee_details.html', context)


def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = AccountsForms(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = AccountsForms(instance=employee)

    context = {'employee':employee, 'form': form}
    return render(request, 'accounts/employee_edit.html', context)

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')

    else:
        context = {'employee': employee}
        return render(request,'accounts/product_confirm_delete.html', context)









