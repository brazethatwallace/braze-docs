---
nav_title: Audiencias de AppsFlyer
article_title: Audiencias de AppsFlyer
alias: /partners/appsflyer_audiences/
description: "Este artículo de referencia describe la asociación entre Braze y AppsFlyer Audiences, una característica de la plataforma AppsFlyer que te permite crear y conectar eficazmente segmentos de audiencia con redes de socios."
page_type: partner
search_tag: Partner

---

# Audiencias de AppsFlyer {#appsflyer-audiences}

> Este artículo describe cómo importar cohortes de usuarios de AppsFlyer a Braze mediante la integración de [AppsFlyer Audiences](https://www.appsflyer.com/product/audiences/). Para más información sobre la integración de AppsFlyer y sus otras funcionalidades, como la atribución móvil, consulta el [artículo principal sobre AppsFlyer]({{site.baseurl}}/partners/message_orchestration/deeplinking/appsflyer/appsflyer/).

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de AppsFlyer | Se necesita una cuenta de AppsFlyer para aprovechar esta asociación. |
| Aplicación iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de tu plataforma, es posible que se requieran fragmentos de código en tu aplicación. Encontrarás más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| SDK or kit de desarrollo de software de AppsFlyer | Además del SDK or kit de desarrollo de software de Braze necesario, debes instalar el [SDK or kit de desarrollo de software de AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de la importación de datos {#data-import-integration}

### Paso 1: Configurar el SDK or kit de desarrollo de software de AppsFlyer {#step-1-configure-the-appsflyer-sdk}

Para utilizar esta integración, debes pasar el ID externo de Braze del usuario a AppsFlyer utilizando la función `setPartnerData()` del SDK or kit de desarrollo de software de AppsFlyer:

#### Android
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### Paso 2: Obtener la clave de importación de datos de Braze {#step-2-get-the-braze-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **AppsFlyer**.

Aquí puedes encontrar el punto de conexión REST y generar tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente. La clave de importación de datos y el punto de conexión REST se utilizan en el siguiente paso cuando se configura un postback en el dashboard de AppsFlyer.<br><br>![La casilla "Importación de datos mediante importación de cohortes" en la página de tecnología de AppsFlyer. En este cuadro, se te muestra la clave de importación de datos y el punto de conexión REST.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### Paso 3: Configurar una conexión de Braze en AppsFlyer Audiences {#step-3-configure-a-braze-connection-in-appsflyer-audiences}

1. En [AppsFlyer Audiences](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections), ve a la pestaña **Connections** y haz clic en **Add partner connection**.
2. Selecciona Braze como socio y dale un nombre a la conexión.
3. Proporciona la clave de importación de datos y el punto de conexión REST or transferencia de estado representacional de Braze.
4. Guarda la conexión, y estará disponible para vincularla a cualquier audiencia nueva o existente.

![Página de configuración de la conexión de socios de la plataforma de audiencias de AppsFlyer. La parte inferior de las imágenes muestra que la casilla de ID externo de Braze está marcada.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### Paso 4: Uso de cohortes de AppsFlyer Audiences en Braze {#step-4-using-appsflyer-audiences-cohorts-in-braze}

Una vez que se ha cargado una audiencia de AppsFlyer en Braze, puedes utilizarla como filtro al definir segmentos en Braze seleccionando el filtro **AppsFlyer Cohorts**.

![Filtro de atributos de usuario "AppsFlyer Cohorts" seleccionado.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Solo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

## Coincidencia de usuarios {#user-matching}

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden coincidir por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.