from django.urls import path, register_converter
from app.converters import DtConverter
from app.views import file_list, file_content

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

register_converter(DtConverter, 'format')


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),  # для детальной информации смотрите HTML-шаблоны в директории templates
    path('<format:date>/', file_list, name='file_list'),    # задайте необязательный параметр "date"
    path('files/<str:name>/', file_content, name='file_content'),
]
