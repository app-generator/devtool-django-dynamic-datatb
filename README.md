# [Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/)

The tool aims to provide a powerful data table interface using the developer's minimum amount of code. Built on top of [Simple-DataTables](https://github.com/fiduswriter/Simple-DataTables), `Vanilla JS` and **Django** for the backend logic.

- 👉 [Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/) - product page
- 👉 [Django Dynamic DataTables](https://www.youtube.com/watch?v=TrTI2jG2LCw) - video presentation
- 🚀 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br />

> Features: 

- ✅ Modern Stack: `Django` & `VanillaJS`
- ✅ `Server-side` pagination
- ✅ Search, Filters
- ✅ Exports in PDF, CSV formats
- ✅ `MIT License` (commercial use allowed)
- ✅ Active versioning & Free [support](https://appseed.us/support/)  

<br />


![Django Dynamic DataTables - Open-Source tool provided by AppSeed.](https://user-images.githubusercontent.com/51070104/194712823-b8bf1a9e-f5d8-47b3-b7e6-a46a29f3acbe.gif)

<br />

## Quick start in `Docker`

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/devtool-django-dynamic-datatb.git
$ cd devtool-django-dynamic-datatb
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. By default a simple [Books](./apps/models.py) Model is used as sample.  

The **Dynamic UI** is live at `http://localhost:5085/datatb/books`

<br />

![Django Dynamic DataTables - Open-Source Tool for Developers.](https://user-images.githubusercontent.com/51070104/194706034-b691226d-f9fa-4c05-a828-fc947670c573.jpg)

<br />

## Video Presentation

https://user-images.githubusercontent.com/51070104/194706066-37a40b93-bc89-4d79-84b0-996dfb0f8be6.mp4

<br />

## How It Works

> 👉 **Step #1** - Define models in `apps/models.py`

By default, the project comes with a simple `Books` model: 

```python
class Book(models.Model):

    title = models.CharField(max_length=100)
```

<br />

> 👉 **Step #2** -  `Register the model` in `core/settings.py` (API_GENERATOR section)

```python
DYNAMIC_DATATB = {
    'books': "Book", # <-- Books model provided as sample
}
```

<br />

> 👉 **Step #3** - `Migrate Database`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 **Step #4** - `Access the UI` 

* Manager books via dynamic page `/datatb/books/`

<br />

---
[Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/) - Developer tool provided by [AppSeed](https://appseed.us)
