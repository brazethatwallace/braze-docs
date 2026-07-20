---
nav_title: API de personalización de Hightouch
article_title: API de personalización de Hightouch
description: "Este artículo de referencia describe la integración entre Braze y la API de personalización de Hightouch, un servicio gestionado para alojar una API de datos de baja latencia basada en cualquier conjunto de datos de tu almacén de datos en la nube. Este artículo de referencia repasa los casos de uso que resuelve la API de personalización de Hightouch, los datos con los que trabaja, cómo configurarla y cómo integrarla con Braze."
page_type: partner
search_tag: Partner
---

# API de personalización de Hightouch {#hightouch-personalization-api}

> La [API de personalización](https://hightouch.com/docs/destinations/personalization-api) de Hightouch es un servicio gestionado que te permite alojar una API de datos de baja latencia basada en cualquier conjunto de datos de tu almacén de datos en la nube.

![Diagrama de arquitectura de la API de personalización de Hightouch que muestra el flujo de datos desde un almacén de datos a través de Hightouch hacia aplicaciones móviles, experiencias web y correos electrónicos dinámicos.]({% image_buster /assets/img/hightouch/cohort7.png %})

La integración de Braze y Hightouch te permite utilizar la API con [contenido conectado de Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) para extraer datos actualizados de clientes u objetos en tus Campaigns o Canvas en el momento del envío.

La API de personalización de Hightouch proporciona un endpoint REST para utilizar en tu configuración de Braze. En concreto, puedes utilizar la oferta de contenido conectado de Braze para realizar una solicitud GET a la API de personalización y recuperar toda la información relacionada con un identificador concreto. Los datos expuestos por esta API pueden representar datos de clientes, productos o cualquier otro objeto.

![Diagrama que muestra datos de Snowflake, BigQuery y Redshift fluyendo a través de la API de personalización de Hightouch hacia el contenido conectado de Braze.]({% image_buster /assets/img/hightouch/cohort6.png %})

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| [Cuenta de Hightouch](https://app.hightouch.com/login) con la API de personalización activada | Se necesita una [cuenta de nivel empresarial](https://hightouch.com/pricing) de Hightouch para beneficiarse de esta asociación. |
| Casos de uso definidos | Antes de configurar la API, debes determinar tu caso de uso para esta integración. Consulta la siguiente lista de casos de uso comunes. |
| Datos almacenados en un almacén de datos en la nube u otra fuente | Hightouch se integra con [más de 25 orígenes de datos](https://hightouch.com/integrations) |
| Clave de API de Hightouch | Se puede crear en **Hightouch > Settings > API keys > Add API key**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% tabs %}
{% tab Use Cases %}

### Casos de uso {#use-cases}

Antes de empezar, es útil planificar exactamente cómo quieres utilizar la API de personalización.

Los casos de uso más comunes son:
- **Recomendaciones de productos** para agilizar la incorporación de recomendaciones de productos personalizadas en plantillas de correo electrónico, Campaigns o experiencias dentro de la aplicación
- **Impulsar Campaigns de marketing personalizadas** enriqueciendo los puntos de intervención de marketing con recomendaciones dinámicas de productos
- **Ofrecer personalización en la aplicación o en la web**, por ejemplo, resultados de búsqueda personalizados, precios basados en cohortes y mensajería, recomendaciones de artículos o ubicaciones de las tiendas más cercanas
- **Recomendaciones basadas en datos financieros o médicos**: los datos financieros tienen requisitos estrictos que Hightouch cumple mediante sus [estrictas políticas de seguridad de datos](https://hightouch.com/docs/security/overview#compliance). Con Hightouch, puedes crear segmentos de clientes basados en datos financieros o médicos sin exponer los atributos subyacentes utilizados en tus criterios de segmentación.

{% endtab %}
{% tab Datasets %}

### Conjuntos de datos {#datasets}

La API de personalización actúa como una caché para los datos seleccionados en tu almacén, por lo que ya deberías tener los datos de recomendación almacenados allí. Si es necesario, puedes utilizar Hightouch para transformarlos según una plantilla. Este tipo de datos incluye:
- Metadatos del usuario, como región geográfica, edad u otra información demográfica
- Acciones o eventos del usuario, incluidas compras anteriores, páginas vistas, clics, etc.

{% endtab %}
{% endtabs %}

## Integración {#integration}

### Paso 1: Conectar el origen de datos a Hightouch {#step-1-connect-data-source-to-hightouch}

Las [fuentes](https://hightouch.com/docs/getting-started/concepts#sources) de Hightouch son el lugar donde residen los datos empresariales de tu organización. En este caso, es dondequiera que se almacenen los datos de tus usuarios.
1. En Hightouch, ve a **Sources Overview > Add Source**. Selecciona tu almacén de datos como fuente.<br><br>
2. Introduce las credenciales pertinentes; estas variarán en función de la fuente.

Para más detalles, consulta la [documentación](https://hightouch.com/docs) de la fuente correspondiente.

### Paso 2: Modelar los datos {#step-2-model-data}

Los modelos de Hightouch definen qué datos extraer de tu fuente. Para configurar un nuevo modelo, sigue estos pasos:

1. En Hightouch, ve a [**Models overview**](https://app.hightouch.com/models) > **Add model** y selecciona la fuente que acabas de conectar. <br><br>
2. A continuación, elige un [método de modelado](https://hightouch.com/docs/models/creating-models). Como toda tu información debe estar unida en una sola tabla, puedes utilizar el selector visual de tablas para definirla. Como alternativa, puedes escribir SQL para incluir solo las columnas que desees o basarte en tus modelos dbt, Looker Looks o libros de trabajo Sigma existentes.<br><br>
3. Antes de continuar, previsualiza tu modelo para asegurarte de que consulta los datos que te interesan. Por defecto, Braze limita la vista previa a los 100 primeros registros. Una vez validados los datos, haz clic en **Continue**.<br><br>
4. Nombra tu modelo, por ejemplo, "Recomendaciones de usuarios".<br><br>
5. Por último, selecciona una clave primaria y haz clic en **Finish**. Una clave primaria debe ser una columna con identificadores únicos. Este es también el campo que utilizarás para llamar a la API de personalización y recuperar las recomendaciones de un usuario en particular.

### Paso 3: Configurar la API de personalización {#step-3-configure-personalization-api}

Preparar la API para recibir solicitudes tiene dos pasos:
- Habilitar la API de personalización en las regiones más cercanas a tu infraestructura
- Crear sincronizaciones para definir qué modelos deben materializarse en la caché gestionada por Hightouch

Sigue estas instrucciones para completar ambos:

1. En Hightouch, ve a [**Destinations**](https://app.hightouch.com/destinations) y selecciona la API de personalización de Hightouch creada para ti. Si no tienes habilitado este destino, ponte en contacto con [el soporte de Hightouch](mailto:friends@hightouch.com).<br><br>
2. A continuación, selecciona la región adecuada. Seleccionar la región más cercana a tu infraestructura reducirá tus tiempos de respuesta. Si no ves una región cercana a tu infraestructura, ponte en contacto con [el soporte de Hightouch](mailto:friends@hightouch.com).<br><br>
3. Ve a la [página de resumen de **Syncs**](https://app.hightouch.com/syncs) y haz clic en el botón **Add sync**. A continuación, selecciona el modelo correspondiente y el destino que hayas configurado previamente.<br><br>
4. Introduce un nombre alfanumérico para la colección. Las colecciones son conceptualmente similares a las tablas de las bases de datos. Cada una debe representar un tipo de datos concreto, como clientes o facturas. Los nombres de las colecciones deben ser alfanuméricos y formarán parte de tu endpoint de la API de personalización.<br><br>
5. A continuación, especifica qué columna de tu modelo debe servir como índice primario para las búsquedas de registros. Este campo debe identificar de forma exclusiva cada registro de la colección y suele coincidir con la clave primaria de tu modelo. La API de personalización admite búsquedas en varios índices. Por ejemplo, puede que quieras recuperar perfiles de clientes utilizando `user_id`, `anonymous_id` o `email_address`. Para activar varios índices, ponte en contacto con [el soporte de Hightouch](mailto:friends@hightouch.com).<br><br>
6. Utiliza el mapeador de campos para especificar qué columnas de tu modelo deben incluirse en la carga útil de la respuesta de la API. Puedes cambiar el nombre de estos campos y utilizar el mapeador avanzado para aplicar transformaciones utilizando el lenguaje de plantillas Liquid.<br><br>
7. Selecciona el [comportamiento de eliminación](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior) adecuado para tu caso de uso.<br><br>
8. Por último, haz clic en **Continue** y selecciona un [calendario de sincronización](https://hightouch.com/docs/syncs/schedule-sync-ui).

Hightouch sincronizará ahora los datos de tu almacén con una base de datos gestionada y los expondrá a través de la API de personalización.

### Paso 4: Llamar a la API de personalización a través del contenido conectado de Braze {#step-4-call-personalization-api-through-braze-connected-content}

Una vez que hayas configurado tu instancia de la API de personalización, puedes utilizarla como un endpoint de contenido conectado de Braze.

Se puede acceder a la API en `https://personalization.{region}.hightouch.com`, por ejemplo, `https://personalization.us-west-2.hightouch.com`.

La información está disponible utilizando este endpoint `/v1/collections/:collection_name/records/:index_key/:index_value`.

Por ejemplo, puedes incluir este fragmento en una Campaign o Canvas:

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Puedes utilizar plantillas Liquid para hacer referencia a las propiedades devueltas en la carga útil JSON y utilizarlas en tu mensajería.

Para el siguiente ejemplo de carga útil:

```json
{
    "user_id": 12345,
    "full_name": "Alex Smith",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ]
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Alex Lee",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    }
}
```

Las siguientes referencias de Liquid devolverían estos datos de ejemplo:

| Plantilla Liquid | Ejemplo devuelto |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %} | Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %} | San Francisco, CA |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %} | Universal Language |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 4: Llamar a la API de personalización a través del contenido conectado de Braze" }

## Solución de problemas {#troubleshooting}

Si tienes alguna pregunta, ponte en contacto con [el soporte de Hightouch](mailto:friends@hightouch.com) para obtener ayuda.