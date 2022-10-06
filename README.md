# [Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/)

The tool aims to provide a powerful data table interface using the developer's minimum amount of code For newcomers, Django is a leading backend framework used to code from simple websites and API's to complex eCommerce solutions.
The presentation layer uses `Simple-DataTables` and Vanilla JS code to render the information.

- 👉 [Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/) - product page
- 👉 [Django Dynamic DataTables](https://www.youtube.com/watch?v=TrTI2jG2LCw) - video presentation
- 🚀 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br />

## Video Presentation 

https://user-images.githubusercontent.com/51070104/194324059-e9c35df3-9467-438f-95e7-61cd16b8fae2.mp4

<br />

## How It Works

The `Dynamic DataTables` tool aims to enable a powerful data table interface on top of any Django codebase with a minimum effort. Here are the steps:

- `Define a new model` in the project (an old one can be also used)
- `Execute the database migration` to create/update the associated tables
- `Update the configuration` to enable the Dynamic Data Table service over the model
- `Start` the app
- Access the `Dynamic DataTable` provided on op of the model

For instance, if the new model managed by the Dynamic DatTable Service is called `books`, the associate API is exposed at `/datatb/books/`

<br />

| Status | Item | info | 
| --- | --- | --- |
| ✅ | New Models Definition in `apps/models` | - |
| ✅ | The app is saved in `apps/dyn_datatables` | - |
| ✅ | Models enabled in `core/settings.py` via `DYNAMIC_DATATB` variable | - |
| ✅ | The project exposes automaticaly a view powered by `Simple-DataTables` JS Library | - |
| ✅ | Path of the service: `/datatb/products/` | In case the new model is `Products` | - | 
| ✅ | The page exposes the controls: `Items per page`, `Search`, `Server Side Pagination`  | - |

<br />

---
[Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/) - Developer tool provided by [AppSeed](https://appseed.us)
