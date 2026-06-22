---
nav_title: Linkrunner
article_title: Linkrunner
alias: /partners/linkrunner/
description: "Este artículo de referencia describe la asociación entre Braze y Linkrunner, una plataforma de análisis y atribución móvil que te permite importar datos de atribución para comprender mejor tus campañas de adquisición de usuarios."
page_type: partner
search_tag: Partner

---

# Linkrunner

> [Linkrunner](https://linkrunner.io/) es una plataforma de análisis y atribución móvil que te ayuda a rastrear y analizar tus campañas de adquisición de usuarios.

_Esta integración es mantenida por Linkrunner._

## Acerca de la integración {#about-the-integration}

La integración de Braze y Linkrunner te permite importar datos de atribución para comprender mejor qué campañas están impulsando la adquisición y la interacción de usuarios.

## Requisitos previos {#prerequisites}

Lo siguiente es necesario antes de comenzar:

| Requisito | Descripción |
|---|---|
| Cuenta de Linkrunner | Se requiere una cuenta de Linkrunner para aprovechar esta asociación. |
| Aplicación iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de tu plataforma, es posible que se requieran fragmentos de código en tu aplicación. |
| SDK de Linkrunner | Debes instalar el [SDK de Linkrunner](https://docs.linkrunner.io/introduction). |
| SDK de Braze | Debes integrar el [SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Mapear los ID de usuario {#step-1-map-user-ids}

Si utilizas la función `changeUser` del SDK de Braze, pasa el mismo ID de usuario en el parámetro `userData` de la función `signup` del SDK de Linkrunner.

Si no utilizas `changeUser`, pasa el `brazeDeviceId` en el parámetro `userData` de la función `signup` del SDK de Linkrunner. Obtén el `brazeDeviceId` del SDK de Braze.

{% tabs local %}
{% tab Android (Kotlin) %}
```kotlin
val userData = UserDataRequest(
    id = "123", // Your user ID
    // ...other user fields
    brazeDeviceId = "BRAZE_DEVICE_ID", // Braze device ID from the Braze SDK (Required if you are not using the changeUser function)
)

LinkRunner.getInstance().signup(userData = userData)
```
{% endtab %}

{% tab iOS (Swift) %}
```swift
let userData = UserData(
    id: "123", // Your user ID
    // ...other user fields
    brazeDeviceId: "BRAZE_DEVICE_ID" // Braze Device ID from the Braze SDK (Required if you are not using the changeUser function)
)

try await LinkrunnerSDK.shared.signup(userData: userData)
```
{% endtab %}
{% endtabs %}

### Paso 2: Crear una clave de API en Braze {#step-2-create-api-key-in-braze}

En tu dashboard de Braze, ve a **Configuración** > **Configuración y pruebas** > **API e identificadores** > **Claves de API**.

1. Selecciona **Crear clave de API**.
2. En **Datos de usuario**, selecciona los siguientes permisos:
   - `users.track`
   - `users.export.ids`
3. Guarda la clave de API.
4. Copia la clave de API y el punto de conexión REST. Pega estos valores en Linkrunner en el siguiente paso. Trata la clave de API como un secreto y no la compartas públicamente.

### Paso 3: Configurar Braze en el dashboard de Linkrunner {#step-3-configure-braze-in-linkrunners-dashboard}

1. En Linkrunner, ve a **Integraciones** en el panel izquierdo.
2. En **Análisis**, selecciona **Configurar** para Braze.
3. Introduce la clave de API y el punto de conexión REST que copiaste en el paso 2.

Para más información, consulta la [documentación de Linkrunner](https://docs.linkrunner.io/analytics-integrations/braze).

### Paso 4: Ver los datos de atribución de usuarios {#step-4-view-user-attribution-data}

Linkrunner envía `lr_campaign` y `lr_ad_network` como atributos personalizados. Consulta estos datos en la sección **Atributos personalizados** del perfil de usuario en el dashboard de Braze.

## Datos de atribución de Facebook y X (anteriormente Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Los datos de atribución de campañas de Facebook y X (anteriormente Twitter) no están disponibles a través de nuestros socios. Estas fuentes de medios no permiten que sus socios compartan datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.