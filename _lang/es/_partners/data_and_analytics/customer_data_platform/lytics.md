---
nav_title: Lytics
article_title: Lytics
description: "Este artículo de referencia cubre la integración de Braze y Lytics. Lytics es una plataforma empresarial de datos de los clientes para especialistas en marketing, analistas y tecnólogos. Esta integración permite a las marcas sincronizar y mapear sus datos de Lytics directamente con Braze."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics](https://www.lytics.com/) es la CDP or plataforma de datos de los clientes or plataforma de datos de los clientes (CDP or plataforma de datos de los clientes) elegida por la próxima generación de empresas centradas en el cliente. Las soluciones Lytics Decision Engine, Conductor y Cloud Connect ofrecen a los especialistas en marketing y a los equipos de datos la oportunidad de llevar a cabo la resolución de identidades, la orquestación y la optimización de campañas en tiempo real y respetando la privacidad.

_Esta integración está mantenida por Lytics._

## Sobre la integración {#about-the-integration}

La integración de Braze y Lytics proporciona una visión unificada de tus clientes para habilitar una potente personalización e impulsar campañas optimizadas utilizando la mejor orquestación de acciones y decisiones.

La integración permite a las marcas:

- Exportar audiencias a Braze directamente desde Lytics
- Enviar eventos de Campaigns o Canvas de Braze a Lytics en tiempo real para campañas personalizadas y para construir perfiles de usuario enriquecidos

## Ejemplos {#use-cases}

Conecta Braze a Lytics para [importar](#importing-data-from-braze-to-lytics) correo electrónico, servicio de mensajes cortos y actividad push para enriquecer los perfiles de usuario de Lytics. Si utilizas Braze y Lytics juntos, también puedes [exportar](#integration) las audiencias de Lytics basadas en comportamientos y multicanal para crear recorridos del cliente en Braze altamente personalizados utilizando datos propios.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Lytics | Se necesita una cuenta de Lytics para aprovechar esta integración. |
| Número de cuenta Lytics | Es necesario un número de cuenta de Lytics para configurar la URL del endpoint del webhook. |
| Token de la API de Lytics | Un token de REST or transferencia de estado representacional API de Lytics con permisos de administrador de datos. <br><br> Se puede crear dentro del panel de Lytics desde **Account Settings Console** > **Access Tokens** > **Create New Token**. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permiso `users.track`. <br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Instancia de Braze | Tu [instancia de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Ponte en contacto con tu administrador de incorporación de Braze para obtener esta información si no estás seguro. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Esta sección describe cómo exportar datos de Lytics a Braze.

### Paso 1: Crear una autorización {#step-1-create-an-authorization}

En Lytics, navega hasta el panel **Authorization** dentro de la consola **Data** en la barra de navegación. Selecciona **Create New Authorization** y busca y selecciona **Braze**.

En el mensaje **Configure Authorization** que aparece, proporciona una etiqueta y una descripción e introduce tu clave de API REST or transferencia de estado representacional y tu instancia de Braze. Selecciona **Complete** cuando hayas terminado.

![Mensaje de configuración de autorización de Lytics para Braze con campos para etiqueta, descripción, clave de API REST e instancia de Braze.]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### Paso 2: Crear un nuevo trabajo {#step-2-create-a-new-job}

En Lytics, navega hasta el panel **Jobs** dentro de la consola **Data** en la barra de navegación. Selecciona **Create New Job** y busca y selecciona **Braze**. En la ventana **Select Job Type** que aparece, selecciona **Export Audience**.

![Mensaje de selección de tipo de trabajo de Lytics para un nuevo trabajo de Braze con Export Audience seleccionado.]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

A continuación, elige una autorización dentro de las opciones de **Select Authorization**.

![Paso de selección de autorización de Lytics mostrando la autorización de Braze a utilizar para el trabajo de exportación.]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### Paso 3: Configurar el trabajo {#step-3-configure-the-job}

Dentro del mensaje **Configure Job**, proporciona una etiqueta y una descripción opcional. A continuación, en la entrada **Braze External User ID Field**, selecciona el campo de Lytics que contiene el ID externo de usuario de Braze (`braze_id`). El siguiente paso es el más importante: en el mismo cuadro de diálogo, selecciona las audiencias que vas a exportar a Braze mediante el SELECTOR de audiencias.

Por último, elige la opción preferida para la casilla **Existing Users**. Si dejas marcada esta casilla, se añadirán los usuarios que ya existan en la audiencia de Lytics seleccionada. Si no está marcada, los usuarios solo se exportarán a Braze cuando entren o salgan de la audiencia una vez iniciado el flujo de trabajo.

{% alert note %}
Al marcar esta casilla, todos los usuarios existentes en la audiencia seleccionada serán enviados a Braze. Si tu tarificación de Braze incluye puntos de datos, controla el uso de puntos de datos en consecuencia.
{% endalert %}

Selecciona **Complete** cuando hayas terminado para iniciar la exportación y guardar.

![Resumen del trabajo de exportación de Lytics mostrando el control Complete y las opciones para guardar o ejecutar la exportación de audiencia a Braze.]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

Una vez configurado el trabajo de exportación, Lytics enviará las audiencias seleccionadas a Braze a través de la integración nativa. A continuación se muestra un ejemplo de audiencia con la estructura JSON de la audiencia enviada a Braze.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

Se creará un nuevo usuario en Braze para cualquier `external_id` incluido en la exportación de audiencia que aún no exista en Braze.

## Importar datos de Braze a Lytics {#importing-data-from-braze-to-lytics}

Puedes importar datos de audiencia de Braze a Lytics utilizando los siguientes métodos:

- [Utilizando webhooks](#using-webhooks)
- [Desde un archivo CSV](#from-a-csv-file)

### Utilizando webhooks {#using-webhooks}

#### Paso 1: Crear un token de API de Lytics {#step-1-create-a-lytics-api-token}

Navega hasta el menú de cuenta de Lytics seleccionando tu nombre de cuenta y selecciona **Access Tokens** en el menú desplegable. A continuación, selecciona **Create API Token**.

![Pantalla de tokens de acceso de Lytics con Create API Token seleccionado desde el menú de cuenta.]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

Introduce un nombre, una descripción opcional y un periodo de caducidad del token. A continuación, activa el ámbito **Data Administrador** para los permisos de API y selecciona **Generate Token**. Copia el token y guárdalo en un lugar seguro.

![Permisos del token de API de Lytics con el ámbito Data Manager habilitado antes de generar el token.]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### Paso 2: Configurar la URL del webhook de Lytics {#step-2-configure-the-lytics-webhook-url}

La URL del webhook de Lytics la utiliza Braze para enviar un mensaje a la API de Lytics desde Braze. Este mensaje puede utilizarse para personalizar tus campañas en Lytics o para enriquecer tu perfil de cliente de Lytics. Es necesario añadir los dos parámetros siguientes en la URL del webhook de Lytics:

- Número de cuenta Lytics
- Token de la API de Lytics

Configura la URL de tu webhook como se indica a continuación:

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

Sustituye `<ACCOUNT-NUMBER>` por tu número de cuenta y `<LYTICS-API-TOKEN>` por tu token de la API de Lytics.

#### Paso 3: Crear un webhook en Braze {#step-3-create-a-webhook-on-braze}

En Braze, crea una nueva [campaña webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook). Añade la URL del webhook de Lytics en el campo **Webhook URL**.

Tras definir el tipo de solicitud (método HTTP `POST`) y configurar el resto de detalles del webhook, tu webhook está listo para ser probado y desplegado. Aquí tienes un cuerpo de muestra de la solicitud POST después de configurar el webhook en Braze:

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "Alex",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@example.com",
  "braze_id": "xxxxxx"
}
```

### Desde un archivo CSV {#from-a-csv-file}

Esta sección describe cómo importar datos de usuario de Braze de un segmento a Lytics.

#### Paso 1: Crear una autorización

En Lytics, navega hasta el panel **Authorization** dentro de la consola **Data** en la barra de navegación. Selecciona **Create New Authorization** y busca y selecciona **Custom Integrations**.

Selecciona el tipo preferido de autorización SFTP en función de tus requisitos empresariales y de seguridad. Se admiten los siguientes tipos de autorización para importar archivos a Lytics mediante SFTP:

- Client SFTP Server Authorization
- Client SFTP Server Authorization with PGP Private Key
- Lytics Managed SFTP Server Authorization

Las autorizaciones SFTP de clave pública son solo para exportación SFTP.

![Opciones de método de autorización SFTP de Lytics para importación de Custom Integrations, incluyendo opciones de servidor del cliente y gestionado por Lytics.]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

En el mensaje **Configure Authorization** que aparece, proporciona una etiqueta y una descripción y completa el resto de requisitos de configuración. Selecciona **Complete** cuando hayas terminado.

#### Paso 2: Exportar los datos de tu segmento a CSV {#step-2-export-your-segment-data-to-csv}

En Braze, ve a **Audiencia** > **Segments**. Localiza el segmento que deseas exportar y, a continuación, selecciona <i class="fas fa-gear" aria-label="Configuración"></i> y luego **Exportación de datos de usuario a CSV**. Puedes exportar hasta 500.000 usuarios en un segmento. Para más detalles, consulta [Exportar datos de segmento a CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

#### Paso 3: Configurar un trabajo de importación CSV {#step-3-configure-a-csv-import-job}

En Lytics, navega hasta el panel **Jobs** dentro de la consola **Data** en la barra de navegación. Selecciona **Create New Job** y busca y selecciona **Custom Integrations**.

A continuación, selecciona el tipo de trabajo. Para importar archivos CSV de Braze a Lytics, selecciona **Import CSV** como tipo de trabajo.

![Configuración de trabajo de Custom Integrations de Lytics con Import CSV seleccionado como tipo de trabajo.]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

Por último, introduce una etiqueta y una descripción opcional para el trabajo y configura cualquier otro detalle necesario. Selecciona **Complete** para iniciar y guardar el trabajo.