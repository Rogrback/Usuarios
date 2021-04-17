# Usuarios
Gestor de usuarios desarrollado con el framework Django de Python, su funcionalidad se abarca en la gestión de usuarios.

# Funcionalidad

## Registro de Usuario
Se le pide principalmente al usuario un nombre de usuario con el que se va a identificar, contraseña y correo.

![image](https://user-images.githubusercontent.com/53346752/115107926-4aae0880-9f33-11eb-9a6e-3fad8ac2ce68.png)

Posteriormente se le enviará un código de registro a su correo registrado y luego validarlo en el sistema para finalmente estar registrado. 
 
![image](https://user-images.githubusercontent.com/53346752/115107968-821cb500-9f33-11eb-8454-28c762e26bdd.png)


## Login de Usuario
El usuario ingresa el nombre de usuario y contraseña para autenticarse y acceder al panel principal

![image](https://user-images.githubusercontent.com/53346752/115108025-cdcf5e80-9f33-11eb-8e68-d3620c7d057e.png)

## Panel de Usuario
Dentro del panel principal se visualiza las acciones de "Cerrar sesión" y "Actualizar datos"

![image](https://user-images.githubusercontent.com/53346752/115108034-dcb61100-9f33-11eb-9e14-f920b719be1e.png)

## Actualizar datos
Al querer actualizar datos el sistema pide la contraseña actual y la nueva con la que se reemplazará.

![image](https://user-images.githubusercontent.com/53346752/115108125-5d750d00-9f34-11eb-8bc6-c1cf09f02b24.png)

Ingresamos los datos solicitados para que nos redigira a la vista del login de usuario.

![image](https://user-images.githubusercontent.com/53346752/115108095-3c142100-9f34-11eb-9a4d-f075aa5cad92.png)

## Cerrar sesión
Al cerrar sesión nos redigirá a la vista del login de usuario.

# Detalle extra del gestor de usuarios
En este gestor de usuarios se usa unaclase interna de Django llamado AbstracBaseUser en el modelo de Usuario para utilizar las funciones de registro, login y logout. Dicha clase hereda todos el motor de usuario que utiliza el Administrador de Django lo cuál ya viene la implementado la seguridad interna y el hasheo de contraseñas (ciertamente es un método que debemos llamar para el uso de éste).

Así como, una clase de Django llamado Mixin que tiene la función de habilitar el panel principal siempre cuando el usuario esté autenticado. Pongamos en contexto la utilidad de esta clase Mixin, cualquiera que no esté logueado puede colocar la ruta del panel principal y acceder sin estar autenticado, entonces acá es cuando participa la clase Mixin que se encarga de acceder al panel principal solo cuando el usuario esté autenticado.





