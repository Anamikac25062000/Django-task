from django.shortcuts import render, redirect
from myapp.models import Book, UploadFile
from myapp.forms import(
    BookForm,
    RegularFileUploadForm,
    ModelFileUploadForm
)

def book_form(request):
    form_book = BookForm
    if request.method == 'POST':
        form_book = BookForm(request.POST, request.FILES)
        if form_book.is_valid():
            form_book.save()
            return book_details(request)
    return render(request, 'book_form.html', {'form_book': form_book})

def book_details(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books':books})


def upload_file_regular_form(request):
    form = RegularFileUploadForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data['title']
            doc = form.cleaned_data['doc']
            UploadFile.objects.create(title=title, doc=doc)
            return redirect(file_list)
    else:
        form = ModelFileUploadForm()
    return render(request, 'file_upload_form.html', {'form': form})


def upload_file_model_form(request):
    if request.method == 'POST':
        form = ModelFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(file_list)
    else:
        form = ModelFileUploadForm()
    return render(request,'file_model_form.html',{'form':form})


def file_list(request):
    files = UploadFile.objects.all()
    return render(request, 'file_list.html',{'files':files})

