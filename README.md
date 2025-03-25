# Ejemplo clase 3

## Inicializar Python
Instalar virtualenv

```shell
python -m venv .venv
```

Luego, inicializar el ambiente virtual:
```shell
. .venv/bin/activate
```

Finalmente, instalar dependencias:

```shell
pip install -r requirements.txt
```

## Ejecutar aplicación
```shell
# Ejemplo 1
flask --app main run

# Ejemplo 2
flask --app main_stateful run
```
