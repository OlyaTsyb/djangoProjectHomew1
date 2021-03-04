from django.shortcuts import render


def home(request):
    return render(request, 'html1.html')


eq = 0


def calc(request, num, znak, num2):
    if znak == '+':
        eq = f'{num} + {num2} = {num + num2}'
    elif znak == '-':
        eq = f'{num} - {num2} = {num - num2}'
    elif znak == ':' and num2:
        eq = f'{num} : {num2} = {num / num2}'
    elif znak == '*':
        eq = f'{num} * {num2} = {num * num2}'
    else:
        eq = 'wrong'
    return render(request, 'html2.html', {"res": eq})
