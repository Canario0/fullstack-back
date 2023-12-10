# Entrega Final Modulo 1

## Instalacion
Esta entrega esta preparada para trabajar con entornos virtuales de python.
Para descargar las dependencias es tan sencillo como ejecutar:

```bash
pipenv install
```

Una vez se tenga las dependencias se puede ejecutar con:
```bash
pipenv run flask run
```
## Configuracion
Como localmente tengo una configuracion que difiere un
con la de los requisitos, he preparado un fichero `.env`
que permite modificar la ruta de redirección. De esta
manera el codigo se puede adaptar a multiples configuraciones
sin realizar cambios en el mismo.
