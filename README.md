# Prueba técnica - Desarrollador Python - Componente 1
###  Backend created with Djando & DjangoRestfulFramework

## Installation
After clone repo.
```sh
$ cd into..
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ python3 backend/manage.py migrate
(env) $ python3 backend/manage.py runserver
```
## Endpoints


Sign Up endpoint `http://127.0.0.1:8000/api/Seguridad/signup/`:

* This route has 2 endpoints:
    * `GET` retrieve all users created.
        * response
        ```javascript
        [
            {
            "id": 1,
            "UserAccess": "administrator",
            "PassAccess": "administrator",
            "TokenAccess": "administrator",
            "ExpirationAccess": "2024-01-01"
            },
            ...
        ]        
        ```
 	* `POST` allow to create new users.
 	    * Params: UserAccess(string) & PassAcess(string) 
 	    * Sucess Response
 	    ```javascript
        []
        ```
Login endpoint `http://127.0.0.1:8000/api/Seguridad/login/`:

* This route has 1 endpoint:
 	* `POST` Do login validating user and password.
 	    * Params: UserAccess(string) & PassAcess(string)
 	    * Sucess Response
 	    ```javascript
        {
          "estado": "true",
          "descripcionRespuesta": "",
          "token": "cf3b8cba-fdc1-4dbb-b8f1-690a2b8409a6"
        }
        ```
        * Unsuccessful Response
        ```javascript
        {
          "estado": "false",
          "descripcionRespuesta": "Usuario o contrasena incorrecto"
        }
        ```