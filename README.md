# [Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/)

The tool aims to provide a powerful data table interface using the developer's minimum amount of code For newcomers, Django is a leading backend framework used to code from simple websites and API's to complex eCommerce solutions.
The presentation layer uses `Simple-DataTables` and Vanilla JS code to render the information.

- 👉 [Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/) - product page
- 👉 [Django Dynamic DataTables](https://www.youtube.com/watch?v=TrTI2jG2LCw) - video presentation
- 🚀 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

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

- The Dynamic UI is live at `http://localhost:5085/datatb/books`

<br />

@ToDO -SSHot

<br />

## Video Presentation

@ToDO -Video

<br />

## How It Works

> 👉 **Step #1** - Define models in `apps/models.py`

By default, the project comes with a simple `Books` model: 

```python
class Book(models.Model):

    name = models.CharField(max_length=100)
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
