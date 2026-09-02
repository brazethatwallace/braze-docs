---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "Este artículo de referencia describe la asociación entre Braze y Certona, una solución de personalización omnicanal en tiempo real que ofrece personalización en todo el ciclo de vida del cliente. Utiliza Certona con el socio de Contenido conectado de Braze para insertar fácilmente recomendaciones de contenido en campañas multicanal."
page_type: partner
search_tag: Partner

---

# Certona

> La plataforma de [Certona](https://www.certona.com/) impulsa la personalización a lo largo del ciclo de vida del cliente. Desde campañas de correo electrónico altamente individualizadas hasta recomendaciones de productos basadas en aprendizaje automático, Certona te garantiza que estás aprovechando el poder de la personalización.

_Esta integración está mantenida por Certona._

## Sobre la integración {#about-the-integration}

La integración de Braze y Certona utiliza las recomendaciones de productos de aprendizaje automático de Certona en Campaigns y Canvas de Braze a través de Contenido conectado.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| [Cuenta Certona](https://manage.certona.com/) | Se necesita una cuenta Certona para beneficiarse de esta asociación. |
| [Punto de conexión de la REST or transferencia de estado representacional API de Certona](https://manage.certona.com/) | Este punto de conexión se utiliza directamente en tu mensaje de Campaign de Braze para extraer contenido recomendado basado en el ID de usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Utiliza la REST or transferencia de estado representacional API de Certona para insertar contenido personalizado en tus mensajes. Para ello, añade la siguiente plantilla de Contenido conectado a tu creador de mensajes de Braze junto con tu punto de conexión de la REST or transferencia de estado representacional API de Certona.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

A continuación, define el contenido que deseas llamar, como texto o imágenes relevantes. Por ejemplo, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![Imagen de una campaña push con Contenido conectado relacionado con Certona incluido en el cuerpo del mensaje.]({% image_buster /assets/img/certona.png %})

Una vez que hayas puesto este mensaje en el cuerpo del creador de mensajes, previsualiza tu llamada a Contenido conectado para asegurarte de que has mostrado la información correcta.

![Una imagen que muestra la pestaña "Prueba", animando a los usuarios a probar a fondo su mensaje antes de enviarlo.]({% image_buster /assets/img/certona2.png %})