---
nav_title: Migrar desde fuentes de datos
article_title: Migrar de fuentes de datos a códigos promocionales
page_order: 10
description: "Este artículo de referencia proporciona orientación sobre cómo migrar de fuentes de datos a códigos promocionales."
---

# Migrar de fuentes de datos a códigos promocionales

{% alert note %}
Las fuentes de datos están siendo descontinuadas. Braze recomienda que los clientes que usan fuentes de datos migren a listas de códigos promocionales.
{% endalert %}

> Esta página te guía a través de la migración de fuentes de datos a códigos promocionales. Es un proceso sencillo que implica crear manualmente listas de códigos promocionales con la información de tus fuentes de datos y actualizar las referencias de tus mensajes en consecuencia.

## Características y funcionalidad

Existen algunas diferencias entre las listas de códigos promocionales y las fuentes de datos.

| Característica   | Códigos promocionales | Fuentes de datos |
|------------------|----------------------|------------------|
| Descripciones    | Sí                   | No               |
| Fechas de expiración | Sí               | No               |
| Método de creación | Cargar un CSV       | Pegar texto      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cómo migrar

Para reemplazar una fuente de datos con una lista de códigos promocionales, haz lo siguiente:

1. Ve a **Configuración de datos** y selecciona **Crear lista de códigos promocionales**.
2. [Configura tu lista de códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes).
3. Navega a tus mensajes que anteriormente hacían referencia a la fuente de datos y actualízalos para usar la lista de códigos promocionales.