# Ollivander's Shop API REST

Este proyecto se basa en una API REST hecha con Python usando el microframework Flask, implementando una conexion a una base de datos en MongoDB Atlas.

El proyecto también incluye un client-side que consume los endpoints de la API.

> A continuación, vamos a dar las instrucciones necesarias que te permitirán obtener una copia del proyecto en funcionamiento.


### Pre-requisitos

- `Python3`
- `pip3`
- `Git`

## Instalación

Hay dos formas de hacer la instalación de nuestro proyecto, a continuación serán explicadas paso a paso.
### Instalación Manual:

- Instalar dependencia entorno virtual Python:

    `$ sudo apt-get install python3.8-venv`

- Crea un directorio y sitúate en él:

    ```bash
    $ mkdir ./ollivanders_shop
    $ cd ollivanders_shop
    ```

- Clona el repositorio:

    `$ git clone https://github.com/JuampaMolina/ollivanders_shop`

- Inicializa el entorno virtual e instala dependencias:

    ```bash
    $ python3.8 -m venv venv
    $ source venv/bin/activate
    (venv) $ pip3 install -r requirements.txt
    ```


### Instalación como distribución:

- Crea un directorio y sitúate en él:

    ```Bash
    $ mkdir ./ollivanders_shop
    $ cd ollivanders_shop
    ```

- Clona el repositorio:

    `$ git clone https://github.com/JuampaMolina/ollivanders_shop`

- Inicializa el entorno virtual y actívalo.

    ```bash
    $ python3.8 -m venv venv
    $ source venv/bin/activate
    ```

- Instala el proyecto con el wheel:

    `$ pip3 install API_REST_OllivandersShop-1.0.0-py3-none-any.whl`


### Ejecutar la aplicación:

1. Primero de todo debemos de tener una base de datos MongoDB a la que conectarnos, una vez creada obtén el driver para la conexion y escribe la URI en el fichero `db_engine.py` en:

    ```Python
    connect(
    	host='URI' )
    ```

2. Activa el entorno virtual:

    `$ source venv/bin/activate`

3. Configura las variables de entorno FLASK:

    ```Bash
    $ export FLASK_APP=app.py
    $ export FLASK_EN=development
    ```
4. Comprueba la disponibilidad del puerto de acceso a MongoDB:

    `$ curl portquiz.net:27017`

5. Para inicializar la base de datos con un inventario y usuarios por defecto ejecuta la siguiente orden:

    `$ flask init-db`

6. Ejecuta la app para que corra en el localhost:

    `$ flask run --host 0.0.0.0`

## API Documentation
### Modules

#### Domain
Almacena un único archivo que contiene toda la lógica del dominio, en este caso la lógica del inventario y los tipos de ítems.

#### Controller
Es el módulo encargado de gestionar las peticiones a los endpoints dependiendo del método HTTP Rest utilizado. En las clases necesarias también definimos un parseRequest para tener control sobre los argumentos que nos llegan y trabajar con ellos.

#### Services
Este módulo es una capa intermedia entre controller y repository. Contiene un solo archivo con los métodos  que llaman a los de repository y nos encargamos de devolver una response adecuada dependiendo de lo que nos devuelvan.

#### Repository
En este módulo encontramos todo lo relacionado con la base de datos, se compone de los siguientes archivos:

- db.py:
Aquí se encuentran todos los métodos que interactúan con la base de datos, a los que accedemos mediante los endpoints.

- db_engine.py:
En este archivo hemos aislado las conexiones a la base de datos y el método que la puebla con los items y usuarios iniciales.

- models.py:
Definimos la estructura de los documentos, tanto de los usuarios como de los items.

- factory.py:
Contiene un método que procesa los items para convertirlos en objetos y así poder hacer el updateQuality.

## Endpoints and methods
#### /inventory
##### GET
Devuelve una lista de todos los documentos de la colección inventario.

```
	[
	    {
	        "name": "Aged Brie",
	        "sell_in": 2,
	        "quality": 0
	    },
	    {
	        "name": "+5 Dexterity Vest",
	        "sell_in": 10,
	        "quality": 20
	    },
	    {
	        "name": "Elixir of the Mongoose",
	        "sell_in": 5,
	        "quality": 7
	    },
	    {
	        "name": "Sulfuras, Hand of Ragnaros",
	        "sell_in": 0,
	        "quality": 80
	    },
	    {
	        "name": "Sulfuras, Hand of Ragnaros",
	        "sell_in": -1,
	        "quality": 80
	    },
	    {
	        "name": "Backstage Pass",
	        "sell_in": 15,
	        "quality": 20
	    },
	    {
	        "name": "Backstage Pass",
	        "sell_in": 10,
	        "quality": 49
	    },
	    {
	        "name": "Backstage Pass",
	        "sell_in": 5,
	        "quality": 49
	    },
	    {
	        "name": "Conjured Mana Cake",
	        "sell_in": 3,
	        "quality": 6
	    }
	]
```
> /inventory

### /item/name/<name>
#### GET
Devuelve una lista de documentos de la colección inventario, cuyo nombre coincide con el indicado.

```
	[
	    {
	        "name": "Aged Brie",
	        "sell_in": 2,
	        "quality": 0
	    }
	]
```
> /item/name/Aged Brie

### /item/sell\_in/\<sell_in>
#### GET
Devuelve una lista de documentos de la colección inventario, cuyo sell in es menor o igual al indicado.


```
	[
	    {
	        "name": "Aged Brie",
	        "sell_in": 2,
	        "quality": 0
	    },
	    {
	        "name": "Sulfuras, Hand of Ragnaros",
	        "sell_in": 0,
	        "quality": 80
	    },
	    {
	        "name": "Sulfuras, Hand of Ragnaros",
	        "sell_in": -1,
	        "quality": 80
	    },
	    {
	        "name": "Conjured Mana Cake",
	        "sell_in": 3,
	        "quality": 6
	    }
	]
```
> /item/sell_in/3

### /item/quality/<quality>
#### GET
Devuelve una lista de documentos de la colección inventario, cuya quality es igual a la indicada.

```
	[
	    {
	        "name": "Sulfuras, Hand of Ragnaros",
	        "sell_in": 0,
	        "quality": 80
	    },
	    {
	        "name": "Sulfuras, Hand of Ragnaros",
	        "sell_in": -1,
	        "quality": 80
	    }
	]
```
> /item/quality/80

### /item
#### POST
Añade un nuevo item en la colección inventory.

```
{
	"message": "Item Test added successfully"
}
```
> /item?name=Test&sell_in=4&quality=10

#### DELETE
Elimina un item en la colección inventory

```
{
	"message": "Item Test deleted successfully"
}
```
> /item?name=Test&sell_in=4&quality=10

### /user
#### GET
Devuelve una lista de todos los documentos de la colección users.

```
[
    {
        "user_name": "Charlos",
        "email": "charlos@gmail.com",
        "password": "test",
        "credit": 50,
        "inventory": []
    },
    {
        "user_name": "Juampa",
        "email": "juampa@gmail.com",
        "password": "test",
        "credit": 50,
        "inventory": []
    }
]
```
#### POST
Añade un nuevo usuario a la colección users.

```
{
	"message": "User Test added successfully"
}
```
> /user?user_name=Test&email=test@gmail.com&password=test

### /buy
#### PUT
Añade un item del inventario a la propiedad inventory del usuario, al usuario se le resta del credito la quality del item.

```
{
	"message": "Congratulations Charlos! +5 Dexterity Vest buyed successfully"
}
```
> /buy?user_name=Charlos&password=test&name=+5 Dexterity Vest&sell_in=10&quality=20

### /user/inventory
Devuelve una lista con los items que posee un usuario

```
[
	{
        "name": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20
	}
]
```
> /user/inventory?user_name=Charlos&password=test

#### /update_quality
##### GET
Devuelve una lista de todos los documentos de la colección inventario con su calidad actualizada.

```
[
    {
        "name": "Aged Brie",
        "sell_in": 1,
        "quality": 1
    },
    {
        "name": "Elixir of the Mongoose",
        "sell_in": 4,
        "quality": 6
    },
    {
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": 0,
        "quality": 80
    },
    {
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": -1,
        "quality": 80
    },
    {
        "name": "Backstage Pass",
        "sell_in": 14,
        "quality": 21
    },
    {
        "name": "Backstage Pass",
        "sell_in": 9,
        "quality": 50
    },
    {
        "name": "Backstage Pass",
        "sell_in": 4,
        "quality": 50
    },
    {
        "name": "Conjured Mana Cake",
        "sell_in": 2,
        "quality": 4
    }
]
```
> /update_quality

## Contenerización con Docker:

You can pull the image from DockerHUB! [Ollivanders-Shop-API image](https://hub.docker.com/r/charlos16v/ollivanders-shop-api).

Para llevar a cabo el deployment de la API en un contenedor, hemos generado una imagen a partir de un Dockerfile, la cual contiene todo el código fuente de la API y todas las dependencias necesarias para su funcionamiento.

```dockerfile
# Vamos a ejecutar la api en una ligera distribución de Linux llamada Alpine.
FROM alpine:3.10

# Instalamos python3 y pip3 en el SO.
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# Se crea el directorio /app donde alojaremos el codigo fuente.
WORKDIR /app

# Copiamos el codigo fuente dentro del directorio /app.
COPY . /app

# Ejecutamos pip3 de forma que instalará todas las dependencias de "requirements.txt".
RUN pip3 --no-cache-dir install -r requirements.txt

# Ejecutamos la aplicación flask con python3.
CMD ["python3", "app.py"]
```

## Autores

- Carlos Uriel Domínguez Ruiz-Diaz
- Juan Pastor Ruiz Molina

## License

Este proyecto está bajo Licencia MIT - Para información más detallada mirar archivo `LICENSE`.

## Tecnologías y herramientas utilizadas

### Tecnologías

- Python
- Flask
- MongoDB
- HTML5 y CSS3
- JavaScript
- Git
- Markdown
- Docker


### Herramientas

- PyCharm
- Postman
- Visual Studio Code
- MongoDB Compass

## Conclusiones
Pensamos que ambos entendimos relativamente bien el concepto de API, pero el hecho de ponerlo en práctica y trabajar con las request, procesar las responses y demás nos ha hecho comprenderlo mucho mejor. También al hacer el refactor al ORM nos quedó más claro que en una API era esencial mantener las cosas lo más simples posibles. Terminamos el proyecto con algo de experiencia adquirida trabajando con Mongo Engine, Postman y Docker entre otros.

### Posibles mejoras
#### Responses
Mejorar las responses para hacer que sean más homogéneas. Hemos tratado de devolver los datos en el módulo repository y generar la response en el módulo service, pero en ocasiones nos hemos visto obligados a utilizar aborts y devolver una response desde repository.

#### Usuarios
Perfeccionar el sistema de usuarios para poder iniciar sesión y mantenerla iniciada, así el sitio reconocería el usuario automáticamente.

Un sistema de venta de items entre los usuarios, para poder vender los items adquiridos y recuperar créditos.

#### Frontend
Consideramos que ha faltado planificación y orden a la hora de realizar el front, al dejarlo para el final nos hemos topado con algunos pequeños problemas que han hecho que hagamos cosas en el front que posiblemente hubieran estado mejor en el back.

Los estilos deberían ser más reutilizables y no tan redundantes en muchos casos, para evitar repetir código.

No hemos conseguido mantener un solo archivo .js para todas las páginas, había fragmentos de código que al no estar encapsulados en una función se ejecutaban de igual forma en todas las páginas y producía problemas.

### Principales dificultades encontradas
Comenzamos el proyecto haciendo una conexión directa con la base de datos, sin pasar por un ORM. A la hora de refactorizar y pasar a utilizar Mongo Engine nos dimos cuenta que no era tan sencillo e implicaba conocer los términos del objeto global, app context, etc. Poner esto en práctica fue un poco frustrante al principio porque no comprendíamos del todo como funcionaban, o más bien, cómo implementarlo en nuestra estructura actual, respetando la separación de las capas y demás.
