# Description of the task

Create a `RESTful API` for the attached OpenAPI schema called `openapi-schema.json`.

Requirements:
- Python 3.9 or 3.10;
- Django 3.2 or 4.
- The latest version of Django Rest Framework.

# Instructions for launching the project

1) Create the virtual environment: `python -m venv venv`.
2) Activate the virtual environment: `source venv/bin/activate`.
3) Install all packages in the virtual environment: `pip install -r requirements.txt`.
4) Run the migrate command to push the migrations to the database: `python manage.py migrate`.
5) Launch the project: `python manage.py runserver 3000`.

# Tests

This command `python manage.py test` will run written tests and give the following result:

```                                             
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.032s

OK
Destroying test database for alias 'default'...
```

# Results

The [POSTMAN](https://www.postman.com/) tool was used to manual testing of the API. There is a `c02_tit.postman_collection.json` file in the root of the project that can be used to repeat these requests in this utility.

1. `GET` request. Get a list of all persons.

![](https://github.com/nurzhannogerbek/c02_tit/tree/master/screenshots/1.png)

2. `GET` request. Get the information of a certain person by id. The result of the request is successful.

![](https://github.com/nurzhannogerbek/c02_tit/tree/master/screenshots/2.png)

3. `GET` request. Get the information of a certain person by id. The result of the request is unsuccessful.

![](https://github.com/nurzhannogerbek/c02_tit/tree/master/screenshots/3.png)

4. `POST` request. Create a new person. The result of the request is successful.

![](https://github.com/nurzhannogerbek/c02_tit/tree/master/screenshots/4.png)

5. `POST` request. Create a new person. The result of the request is unsuccessful cause the person with such email is exist.

![](https://github.com/nurzhannogerbek/c02_tit/tree/master/screenshots/5.png)

6. `POST` request. Create a new person. The result of the request is unsuccessful cause some fields were missing in Request Body.

![](https://github.com/nurzhannogerbek/c02_tit/tree/master/screenshots/6.png)

7. `PUT` request. Update the information of a certain person by id. The result of the request is successful.

![](https://github.com/nurzhannogerbek/c02_tit/tree/master/screenshots/7.png)

8. `DELETE` request. Delete the information of a certain person by id. The result of the request is successful.

![](https://github.com/nurzhannogerbek/c02_tit/tree/master/screenshots/8.png)
