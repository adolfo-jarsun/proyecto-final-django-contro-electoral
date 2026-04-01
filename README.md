# 🗳️ Proyecto Django - Sistema de Control Electoral

## 📌 Descripción

Este proyecto consiste en el desarrollo de un **Sistema de Control Electoral** implementado con el framework **Django** y **Django Rest Framework (DRF)**.

El objetivo principal es gestionar y registrar información relacionada con procesos electorales, como actas, votos y resultados, permitiendo su administración y consulta mediante una API REST.

---

## 🎯 Propósito

Demostrar los conocimientos adquiridos en el desarrollo de aplicaciones web utilizando Django, incluyendo:

* Modelado de datos
* Validaciones personalizadas
* Administración de datos
* Desarrollo de APIs REST

---

## ⚙️ Tecnologías Utilizadas

* Python
* Django
* Django Rest Framework
* PostgreSQL / SQLite (según configuración)
* Git & GitHub

---

## 📂 Estructura del Proyecto

El proyecto contiene al menos una aplicación Django encargada de la lógica del sistema electoral.

Ejemplo de estructura:

```
proyecto/
│
├── app_control_electoral/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── admin.py
│
├── proyecto/
│   ├── settings.py
│   ├── urls.py
│
├── requirements.txt
└── manage.py
```

---

## 🧩 Modelos Implementados

La aplicación incluye al menos **4 modelos**, por ejemplo:

* Acta Electoral
* Mesa
* Votante / Elector
* Resultado

---

## ✅ Validaciones Personalizadas

Se implementaron al menos **2 validaciones personalizadas**, tales como:

* Validación de número de votos no negativo
* Validación de consistencia entre votos emitidos y registrados

---

## 🛠️ Administración (Django Admin)

Se registraron al menos **2 modelos** en el panel administrativo de Django para su gestión, permitiendo:

* Crear registros
* Editar datos
* Eliminar información

---

## 🌐 API REST (Django Rest Framework)

Se implementaron al menos:

### 🔹 3 Endpoints tipo ViewSet / GenericAPIView

Ejemplo:

* `/api/actas/`
* `/api/mesas/`
* `/api/resultados/`

---

### 🔸 1 API personalizada

Ejemplo:

* Endpoint para obtener resultados consolidados
* Endpoint para cálculo de votos totales

---

## 📦 Archivo de Dependencias

El proyecto incluye el archivo:

```
requirements.txt
```

Este contiene todas las librerías necesarias para ejecutar el sistema.

---

## 🚀 Instalación y Ejecución

### 1. Clonar repositorio

```
git clone <URL_DEL_REPOSITORIO>
cd proyecto
```

### 2. Crear entorno virtual

```
python -m venv venv
```

### 3. Activar entorno

```
venv\Scripts\activate   (Windows)
source venv/bin/activate (Linux/Mac)
```

### 4. Instalar dependencias

```
pip install -r requirements.txt
```

### 5. Migraciones

```
python manage.py migrate
```

### 6. Ejecutar servidor

```
python manage.py runserver
```

---

## 👥 Integrantes

Si el proyecto fue realizado en grupo, consultar el archivo:

```
INTEGRANTES.md
```

---

## 📌 Notas Finales

* El proyecto cumple con los requerimientos del **Módulo V - Django**
* Se valoró la implementación práctica y la organización del código
* Se aplicaron buenas prácticas en el desarrollo de APIs REST

---

## 🔗 Repositorio

El proyecto se encuentra disponible en un repositorio público de GitHub.

---

## 🧠 Autor

Desarrollado como parte de la formación en Django.

---
