![BeFast Banner](./assets/images/banner.jpg)

La API de BeFast creada con Python con colaboración de [Kanna](https://github.com/bony24) y Kurizu.

## Iniciando el proyecto

Antes de empezar con todo el código lo primero es iniciar el programa para poder hacer las pruebas de la forma que más te pueda acomodar, por lo que lo haremos de una forma sencilla, lo primero sera clonar el repositorio en nuestro equipo lo que se hace de la siguiente manera.

```git
git clone https://github.com/damkandev/befast-api.git
```

una vez lo hayamos clonado lo que haremos sera ingresar al directorio usando el tradicional comando de change directory:

```console
cd ./befast-api
```

y lo primero sera instalar los requerimientos que nos pedira python haciendo uso del siguiente comando:

```console
pip install requirements.txt
```

luego además tenemos que tener un programa que nos ayude a iniciar el servidor y la base de datos, en nuestro caso usaremos [Laragon](https://laragon.org/download/index.html) y para visualizar la base de datos haremos uso de [DBeaver](https://dbeaver.io/) que personalmente recomendamos por su facilidad para ver los DER y datos.

para iniciar la base de datos iremos a laragon y presionaremos en el botón de `start all` que de forma muy rapida iniciara los servicios necesarios, luego iremos a DBeaver y realizaremos una conexión a localhost que es en dodne tenemos la base de datos, por defecto suele ser en el puerto `3306`.

Una vez hecho esto iremos a nuestro código y ejecutaremos el siguiente comando de la libreria uvicorn.

```console
uvicorn main:app --reload
```

puedes ver más documentacion dando [click aquí](./docs/)
