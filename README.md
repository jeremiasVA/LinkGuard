<div align="center">

# 🛡️ LinkGuard ⚡

*Protección inteligente contra enlaces maliciosos*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Security](https://img.shields.io/badge/Security-First-green.svg)]()

</div>

**LinkGuard** es una aplicación móvil que monitorea enlaces en segundo plano para detectar y bloquear enlaces maliciosos, protegiendo al usuario final de amenazas web.

## Funcionalidades
- Detectar, analizar y bloquear enlaces inseguros
- Registrar usuario de emergencia
- Actualizar datos del usuario de emergencia
- Eliminar usuario de emergencia
- Ver historial de enlaces

## Arquitectura del Proyecto
```
LinkGuard/
├── Datos/
├── Negocio/
└── Presentacion/
    └── main.py
```
La aplicación sigue una arquitectura de tres capas:

- Datos: Manejo de información y almacenamiento
- Negocio: Procesamiento de la lógica principal
- Presentación: Interfaz de usuario y control de flujo

## Desarrollo

- Lenguaje: Python
- Tipo: Aplicación de consola
- Arquitectura: Estructura modular en capas
  
## Requisitos y Ejecución
Requisitos Previos
- Python 3.7 o superior

Ejecución
```bash
python -m LinkGuard.Presentacion.main
```
