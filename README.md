# CS50-WIKI

Wiki project is based on CS50 Web programming course and built with Django web framework in python programming language.

## Feauters

- Build a web application that reads Markdown files and presents the content of that file to the user
- Create new Markdown file with Title and Description of the Markdown entry
- Search for specifc Title.
- View random entry from the application



## Tech

Technologies that have been used:

- Python3 (3.10.4)
- Django Web Framework (4.1.1)
- Markdown
- HTML5
- CSS
- Sqlite

## Installation


CLone the repository into your local device
```
git clone https://github.com/ahmadalshawakri/CS50-WIKI.git
cd CS50-WIKI
```
Install the dependencies
```
pip3 install django==4.1.1
pip3 install markdown
```

Start the server

```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
