---
nav_title: Autenticación y seguridad
article_title: Autenticación y seguridad de la API de mensajería
page_order: 1
page_type: reference
description: "Aprende a autenticar de forma segura las solicitudes de la API de mensajería."
hidden: true
---

# Autenticación y seguridad de la API de mensajería {#messaging-api-authentication-and-security}

{% alert important %}
Esta página está en versión beta. Las características y la documentación de la API de mensajería están sujetas a cambios.
{% endalert %}

La API de mensajería utiliza claves de API REST del lado del cliente. Estas claves son distintas de las claves de API REST privadas utilizadas para las solicitudes de la REST API de Braze del lado del servidor.

## Claves de API REST del lado del cliente {#client-side-rest-api-keys}

Las claves de API REST del lado del cliente están limitadas a un espacio de trabajo y restringidas a los permisos de la API de mensajería. Puedes integrar estas claves en las aplicaciones del cliente.

{% alert important %}
Utiliza solo una clave de API REST del lado del cliente en una aplicación del cliente. Nunca expongas una clave de API REST privada del lado del servidor en código del lado del cliente.
{% endalert %}

Para crear una clave de API REST del lado del cliente:

1. Ve a **Configuración** > **API e identificadores** > **Claves de API** en el panel de Braze.
2. Selecciona **Crear clave de API**.
3. En **Tipo de clave**, selecciona **Cliente**.
4. Asigna el permiso `banners.sync` para recuperar Banners, el permiso `banners.track` para reportar eventos de Banner, o ambos.

## Autenticación de solicitudes {#authenticating-requests}

Envía la clave de API REST del lado del cliente como un token bearer en el encabezado `Authorization`:

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

Utiliza HTTPS y el [endpoint REST]({{site.baseurl}}/api/basics#endpoints) de tu instancia de Braze.

## Identidad del usuario {#user-identity}

Una clave de API REST del lado del cliente autentica la aplicación que realiza la llamada y el espacio de trabajo, no al usuario. El `external_user_id` en una solicitud identifica al usuario asociado con el contenido y los eventos de Banner.

Aplica los controles de autorización de tu aplicación antes de realizar solicitudes a la API de mensajería.

## Errores de autenticación {#authentication-errors}

Los errores de autenticación y permisos pueden variar según el endpoint. Consulta la tabla de códigos de estado de cada endpoint y la [gestión de errores de la API de mensajería]({{site.baseurl}}/api/messaging_api/error_handling).