---
nav_title: Adobe
article_title: Adobe
description: "Esta página describe la asociación entre Braze y Adobe, una plataforma de datos de los clientes, que permite a las marcas conectar y mapear sus datos de Adobe (atributos personalizados y segmentos) con Braze en tiempo real. A continuación, las marcas pueden actuar en función de estos datos y ofrecer experiencias personalizadas y dirigidas a esos usuarios."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Construida sobre Adobe Experience Platform, la plataforma de datos de los clientes en tiempo real de Adobe reúne datos conocidos y anónimos de múltiples fuentes empresariales para crear perfiles de clientes. Estos perfiles pueden utilizarse para ofrecer experiencias personalizadas en todos los canales y dispositivos en tiempo real.

La integración de Braze y Adobe CDP conecta y mapea los datos de Adobe de tu marca (atributos personalizados y segmentos) con Braze en tiempo real. A continuación, puedes actuar sobre estos datos, entregando experiencias personalizadas y dirigidas a tus usuarios. Con Adobe, la integración es intuitiva. Basta con tomar cualquier [identidad](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en) de Adobe, mapearla a un ID externo de Braze y enviarla a la plataforma Braze. Todos los datos enviados serán accesibles en Braze a través de un nuevo atributo `AdobeExperiencePlatformSegments`.

{% alert important %}
Actualmente, la integración de Adobe Experience Platform no admite la pertenencia dinámica a audiencias. Esto significa que solo puede añadir valores a los perfiles de usuario, no eliminarlos.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Adobe | Se necesita una [cuenta de Adobe](https://account.adobe.com/) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Se puede crear en el panel de Braze desde **Settings** > **API Keys**. |
| Instancia de Braze | Tu instancia de Braze puede obtenerse a través de tu administrador de incorporación de Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints). |
| Punto de conexión REST de Braze | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% alert important %}
El envío de atributos personalizados adicionales aumentará tu uso de puntos de datos. Te sugerimos que hables con tu administrador del éxito del cliente para comprender mejor este posible aumento de puntos de datos.
{% endalert %}

## Integración {#integration}

### Paso 1: Configurar el destino Braze {#step-1-configure-braze-destination}

En la página **Settings** de Adobe, selecciona **Destinations** en **Collections**. Desde ahí, localiza el mosaico **Braze** y selecciona **Configure**.

![]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
Si ya existe una conexión con Braze, verás un botón **Activate** en la tarjeta de destino. Para obtener más información sobre la diferencia entre activar y configurar, consulta la sección de catálogo de la [documentación](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog) del espacio de trabajo de destino de Adobe.
{% endalert %}

### Paso 2: Proporcionar el token de Braze {#step-2-provide-braze-token}

En el paso **Account**, proporciona tu clave de API de Braze y selecciona **Connect to destination**.

![]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### Paso 3: Autenticación {#step-3-authentication}

A continuación, en el paso **Authentication**, introduce los datos de tu conexión con Braze:
- **Name**: introduce el nombre con el que te gustaría reconocer este destino en el futuro.
- **Destination**: introduce una descripción que te ayude a identificar este destino.
- **Endpoint instance**: introduce tu instancia de punto de conexión de Braze.
- **Marketing use case**: los casos de uso de marketing indican la intención para la que se exportarán los datos al destino. Puedes seleccionar entre los casos de uso de marketing definidos por Adobe o crear tu propio caso de uso de marketing. Para obtener más información sobre los casos de uso de marketing de Adobe, visita [Data governance in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### Paso 4: Crear destino {#step-4-create-destination}
Selecciona **Create destination**. Se ha creado tu destino. Puedes seleccionar **Save & Exit** para activar los segmentos más tarde o **Next** para continuar el flujo de trabajo y seleccionar los segmentos a activar.

### Paso 5: Activar segmentos {#step-5-activate-segments}
Activa los datos que tienes en el CDP en tiempo real de Adobe mapeando segmentos al destino Braze.

En la siguiente lista se indican los pasos generales necesarios para activar un segmento. Para obtener información detallada sobre los segmentos de Adobe y el flujo de trabajo de activación de segmentos, visita [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Selecciona y activa el destino Braze.
2. Selecciona los segmentos aplicables.
4. Configura la programación y los nombres de archivo para cada segmento que exportes.
5. Selecciona los atributos que deseas enviar a Braze.
6. Revisa y verifica la activación.

### Paso 6: Mapeado de campos {#step-6-field-mapping}

Para enviar correctamente los datos de tu audiencia desde Adobe Experience Platform a Braze, debes completar el paso de mapeado de campos. El mapeado crea un vínculo entre los campos del modelo de datos de Adobe Experience y los campos correspondientes de la plataforma Braze.

1. En el paso de mapeado, selecciona **Add new mapping**.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. En la sección de campo fuente, selecciona el botón de flecha situado junto al campo vacío para abrir la ventana de selección de campo fuente.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. En la ventana, selecciona los atributos de Adobe para mapearlos con tus atributos de Braze. <br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>A continuación, selecciona el espacio de nombres de identidad. Esta opción se utiliza para mapear un espacio de nombres de identidad de la plataforma a un espacio de nombres de Braze.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br> Elige tus campos fuente y selecciona **Select**.<br><br>
4. En la sección del campo de destino, selecciona el icono de mapeado situado junto al campo.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"} <br><br>
5. En la ventana de selección de campos de destino, puedes elegir entre tres categorías de campos de destino:<br><br>• **Select identity namespace**: utiliza esta opción para mapear espacios de nombres de identidad de la plataforma a espacios de nombres de identidad de Braze.<br>• **Select custom attributes**: utiliza esta opción para mapear atributos Adobe XDM a atributos personalizados de Braze que hayas definido en tu cuenta de Braze. <br><br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**También puedes utilizar esta opción para renombrar atributos XDM existentes en Braze.** Por ejemplo, al mapear un atributo `lastname` XDM a un atributo personalizado `Last_Name` en Braze, se creará el atributo `Last_Name` en Braze si aún no existe, y se mapeará el atributo `lastname` XDM a él. <br><br> Elige los campos de destino y selecciona **Select**.<br><br>
6. Tu mapeado de campos debería aparecer en la lista.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. Para añadir más mapeados, repite los pasos del 1 al 6, según sea necesario.

## Caso de uso {#use-case}

Supongamos que tu esquema de perfil XDM y tu instancia de Braze contienen los siguientes atributos e identidades:

|     | Esquema de perfil XDM | Instancia de Braze |
| --- | ------------------ | -------------- |
| Atributos | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identidades | - `Email`<br>- ID de anuncio de Google (`GAID`)<br>- ID de Apple para anunciantes (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Caso de uso" }

El mapeado correcto sería el siguiente:

![Mapeados de destino: IdentityMap:IDFA mapeado a IdentityMap:external_id, IdentityMap:GAID mapeado a IdentityMap:external_id, IdentityMap:Email mapeado a IdentityMap:external_id, xdm:mobilePhone.number mapeado a CustomAttribute:PhoneNumber, xdm:person.name.lastName mapeado a CustomAttribute:LastName, xdm:person.name.firstName mapeado a CustomAttribute:FirstName]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## Datos exportados {#exported-data}
Para verificar si los datos se han exportado correctamente a Braze, comprueba tu cuenta de Braze. Los segmentos de Adobe Experience Platform se exportan a Braze con el atributo `AdobeExperiencePlatformSegments`.

## Uso y gobernanza de los datos {#data-usage-and-governance}
Todos los destinos de Adobe Experience Platform cumplen las políticas de uso de datos cuando manejan tus datos. Consulta [Data governance in real-time CDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) para obtener información detallada sobre cómo Adobe Experience Platform aplica la gobernanza de datos.