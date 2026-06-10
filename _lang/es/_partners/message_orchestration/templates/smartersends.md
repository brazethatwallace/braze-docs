---
nav_title: SmarterSends
article_title: SmarterSends
description: "Este artículo de referencia describe la asociación entre Braze y SmarterSends, una interfaz fácil de usar diseñada para que los no especialistas en marketing puedan crear, programar y desplegar campañas de correo electrónico compatibles con la marca."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends](https://smartersends.com) impulsa la personalización con campañas de marketing que las empresas pueden crear, programar y desplegar para reforzar el cumplimiento legal y de la marca con control sobre el contenido y los datos utilizados.

_Esta integración está mantenida por SmarterSends._

## Sobre la integración {#about-the-integration}

La asociación entre Braze y SmarterSends te permite combinar la potencia de Braze con el contenido hiperlocalizado propiedad de tus usuarios distribuidos para elevar tus campañas de marketing.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta SmarterSends | Se necesita una [cuenta de SmarterSends](https://smartersends.com) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con estos permisos: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} Se puede crear en el dashboard de Braze desde **Configuración** > **Claves de API**. Para mayor seguridad, añade la dirección IP de SmarterSends a la lista blanca (disponible en tu instancia). |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
| ID de Campaign de API de Braze | El [ID de Campaign de API de Braze]({{site.baseurl}}/api/api_campaigns/) es el identificador único de todas las campañas enviadas a través de SmarterSends. Se puede crear en el dashboard de Braze en **Messaging** > **Campaigns**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Con la integración de Braze y SmarterSends, puedes aprovechar las ventajas del marketing distribuido creando y ejecutando campañas de marketing en múltiples canales y ubicaciones. Estas ventajas incluyen:

1. **Mayor alcance:** Utilizar múltiples canales y ubicaciones para llegar a una audiencia más amplia y a clientes objetivo en diferentes ubicaciones, lo que se traduce en una mayor exposición de la marca.
2. **Mensajería dirigida:** Adaptar la mensajería a través de canales y ubicaciones para que resuene en las audiencias locales, con el fin de conseguir una comunicación y una interacción más eficaces con los clientes.
3. **Mejora de la coherencia de la marca:** Alinear el mensaje y la imagen de tu marca en todos los canales y ubicaciones, lo que es importante para construir una marca fuerte y reconocible.
4. **Mejor información:** Recopilar datos de varios canales y ubicaciones, proporcionando información valiosa sobre el comportamiento y las preferencias del cliente, que puede utilizarse para perfeccionar las estrategias y tácticas de marketing tanto a nivel local como global.
5. **Mayor eficiencia:** Aprovechar los puntos fuertes de los distintos canales y ubicaciones, lo que puede dar lugar a un uso más eficiente de los recursos sin dejar de alcanzar los objetivos de marketing deseados.

## Integración {#integration}

### Paso 1: Crear una clave de API REST {#step-1-create-a-rest-api-key}

1. En Braze, ve a **Configuración** > **Claves de API** y haz clic en **Crear nueva clave de API**.
2. Introduce un nombre para la clave de API.
3. Selecciona los siguientes permisos para esta clave para permitir que SmarterSends interactúe con tu espacio de trabajo de Braze.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. Añade la dirección IP de SmarterSends a la sección **Whitelist IPs**.
5. Haz clic en **Guardar clave de API**.
6. Copia y pega la clave de API con los permisos adecuados en la configuración de **Braze Email Service Provider** en SmarterSends.

### Paso 2: Crear o copiar un ID de aplicación {#step-2-create-or-copy-an-application-id}

1. En tu espacio de trabajo de Braze, ve a **Configuración** > **Configuración de la aplicación**.
2. Configura una nueva aplicación o utiliza el ID de aplicación de una aplicación existente dentro de tu espacio de trabajo. Ten en cuenta que el ID de la aplicación está etiquetado como **API Key**.
3. Copia y pega este ID en el campo **App ID** en SmarterSends.

### Paso 3: Crear una Campaign de API {#step-3-create-an-api-campaign}

Una Campaign de API permite el seguimiento de métricas de todo el correo de SmarterSends dentro de Braze y habilita a SmarterSends para desencadenar estas campañas basadas en API.

1. En Braze, [crea una Campaign de API]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. Haz clic en **Email** en **Select Message Channel** para añadir un canal de mensajería y comenzar el seguimiento de las métricas.
3. A continuación, copia y pega el ID de Campaign de Braze en el campo **Campaign ID** de SmarterSends.
4. Copia y pega el ID de variante del mensaje de Braze en el campo **Message Variant ID** en SmarterSends. Este será el ID de mensaje predeterminado que se utilizará si decides no crear un ID de mensaje para cada grupo en SmarterSends.
5. Para cada grupo que crees en SmarterSends, añade una variante de mensaje a tu Campaign de API en Braze. A continuación, copia el ID de variante del mensaje en el ID de variante del mensaje del grupo en SmarterSends.

{% alert tip %}
Crea un ID de variante de mensaje para cada grupo que crees en SmarterSends para ver las métricas de los envíos de cada grupo por separado en tu espacio de trabajo de Braze. Esto puede ser útil para identificar tendencias entre los grupos al elaborar informes en Braze.
{% endalert %}

## Personalización {#customization}

Cada instancia de SmarterSends es totalmente personalizable con los colores del logotipo de tu marca y el nombre de dominio personalizado, creando un entorno familiar. Además, para una mayor personalización, puedes definir los atributos y atributos personalizados para dirigirte a los usuarios en campañas basadas en los Segments dentro de tu espacio de trabajo de Braze.