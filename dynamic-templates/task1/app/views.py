import csv
from django.shortcuts import render


def inflation_view(request):
    # чтение csv-файла и заполнение контекста
    list_data = []
    template_name = 'inflation.html'
    with open('inflation_russia.csv', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';', quotechar='"')
        new_list = [[element or '-' for element in row] for row in reader]
    context = {'data': new_list}
    return render(request, template_name, context)
