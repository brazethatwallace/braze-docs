---
nav_title: Resumen
article_title: Resumen de la API de mensajería
page_order: 0
page_type: reference
description: "Obtén información sobre la API de mensajería de Braze y sus capacidades de acceso anticipado."
hidden: true
---

# Resumen de la API de mensajería {#messaging-api-overview}

La API de mensajería de Braze es un conjunto de endpoints REST para integrar las capacidades de mensajería de Braze sin un SDK de Braze. Puedes llamar a estos endpoints desde aplicaciones de cliente o servidor.

{% alert important %}
Esta página está en fase beta. Las características y la documentación de la API de mensajería están sujetas a cambios. Ponte en contacto con tu director de cuentas de Braze para solicitar acceso.
{% endalert %}

## Capacidades compatibles {#supported-capabilities}

Durante el acceso anticipado, puedes utilizar la API de mensajería para:

- [Recuperar Banners elegibles]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners) para un ID de usuario externo y un conjunto de ubicaciones
- [Informar eventos de impresión y clic de Banner]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)

La API de mensajería devuelve propiedades estructuradas de Banner para que puedas crear una interfaz personalizada. No devuelve HTML renderizado.

## Requisitos de integración {#integration-requirements}

Para integrar la API de mensajería, necesitas:

- Un espacio de trabajo con la API de mensajería habilitada
- Una clave de API REST del lado del cliente para ese espacio de trabajo
- El endpoint REST para ese espacio de trabajo
- El ID de usuario externo del usuario
- El identificador de API para la aplicación

Para obtener más información sobre las credenciales, consulta [Autenticación y seguridad]({{site.baseurl}}/api/messaging_api/authentication).

## Orientación sobre la API de mensajería y la REST API {#messaging-api-and-rest-api-guidance}

La API de mensajería utiliza los mismos endpoints REST regionales que la REST API de Braze, pero tiene un contrato de autenticación y respuesta independiente. La orientación general de la REST API sobre claves privadas del lado del servidor, cuerpos de respuesta, errores y límites de velocidad no aplica a menos que un artículo de la API de mensajería haga referencia explícita a ella.

Utiliza la documentación de endpoints de la API de mensajería como fuente de verdad para los campos de solicitud, cuerpos de respuesta, códigos de estado y límites.