---
nav_title: Puntuación de clientes potenciales
article_title: Crear un flujo de trabajo de puntuación de clientes potenciales
page_order: 1
page_type: reference
description: "Aprende a utilizar Braze para realizar la puntuación simple de clientes potenciales, la puntuación externa de clientes potenciales y el traspaso de clientes potenciales."
---

# Crear un flujo de trabajo de puntuación de clientes potenciales {#create-a-lead-scoring-workflow}

> Este caso de uso demuestra cómo puedes utilizar Braze para actualizar las puntuaciones de clientes potenciales de los usuarios en tiempo real y entregar automáticamente los clientes potenciales a tus equipos de ventas.

Hay dos pasos clave para crear un flujo de trabajo de puntuación de clientes potenciales en Braze:

1. Crea un Canvas de puntuación de clientes potenciales en Braze o integra una herramienta externa de puntuación de clientes potenciales:
- [Puntuación sencilla de clientes potenciales](#simple-lead-scoring)
- [Puntuación externa de clientes potenciales](#external-lead-scoring)

2. Crea una Campaign de webhook para enviar clientes potenciales cualificados a tu equipo de ventas:
- [Traspaso de clientes potenciales: cliente potencial cualificado por marketing (MQL) a ventas](#lead-handoff)

## Puntuación sencilla de clientes potenciales {#simple-lead-scoring}

### Paso 1: Crear un Canvas {#step-1-create-a-canvas}

1. Ve a **Messaging** > **Canvas** y selecciona **Create Canvas**, y luego rellena los datos básicos de tu Canvas.

2. Dale a tu Canvas un nombre relevante como "Lead Scoring Canvas" y, para encontrarlo más fácilmente, etiquétalo con algo como "Lead Management".<br><br>![Paso 1 de la creación de un Canvas con el nombre "Lead Scoring Canvas" y la etiqueta "Lead Management".]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Paso 2: Configura tus criterios de entrada {#step-2-set-up-your-entry-criteria}

1. Ve al paso **Horario de entrada** y selecciona un horario de entrada **basado en acciones**. Esto introducirá a los usuarios en el Canvas cuando realicen acciones específicas.

2. En **Opciones basadas en acciones**, añade estas dos acciones:
    - **Cambiar el valor del atributo personalizado** con el nombre de tu atributo de puntuación de clientes potenciales (como `lead score`). Si aún no has creado un atributo de puntuación de clientes potenciales, sigue los pasos de [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/). Esto introducirá a los usuarios en el Canvas cada vez que cambie su puntuación de cliente potencial.
    - **Agregar una dirección de correo electrónico**

![Paso 2 de la creación de un Canvas con el horario de entrada "Basado en acciones" y las opciones basadas en acciones de cambiar un atributo personalizado "lead score" y añadir una dirección de correo electrónico.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Paso 3: Identifica tu audiencia objetivo {#step-3-identify-your-target-audience}

#### Paso 3a: Seleccionar segmentos {#step-3a-select-segments}

Todos los usuarios son elegibles para la puntuación de clientes potenciales, por lo que puedes añadir reglas específicas de la empresa sobre a quién puntuar seleccionando a qué [segmentos]({{site.baseurl}}/user_guide/audience/segments/) de usuarios dirigirte y aplicando [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) adicionales. Por ejemplo, puedes excluir a empleados, usuarios que ya son clientes y similares.

![Paso 3 de la creación de un Canvas con opciones para seleccionar segmentos y filtros para acotar la audiencia de entrada.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Paso 3b: Establecer la reelegibilidad del Canvas {#step-3b-set-canvas-re-eligibility}

Un usuario pasará por este Canvas muchas veces a lo largo de su ciclo de vida contigo, así que asegúrate de que pueda volver a entrar tan rápido como salió la vez anterior. Esto se puede lograr mediante la configuración de reelegibilidad.

En **Controles de entrada**, haz lo siguiente:
- Selecciona **Permitir a los usuarios volver a entrar en este Canvas**.
- Selecciona **Ventana especificada**.
- Establece la reelegibilidad en "0" **segundos**.

![Sección "Controles de entrada" con selecciones para "Permitir a los usuarios volver a entrar en este Canvas" en una "Ventana especificada" de 0 segundos.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Paso 3c: Actualizar la configuración de envío {#step-3c-update-send-settings}

Dada la naturaleza operativa de este Canvas y el hecho de que no se enviarán mensajes a estos usuarios, no necesitas respetar los estados de suscripción.

En **Configuración de suscripción**, en **Enviar a estos usuarios:** selecciona **todos los usuarios, incluidos los usuarios dados de baja**.

![Paso 4 de la creación de un Canvas para configurar las opciones de envío de mensajes.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Paso 4: Construye tu Canvas {#step-4-build-your-canvas}

#### Paso 4a: Añadir una ruta de acción {#step-4a-add-an-action-path}

Bajo tu variante, selecciona <i class="fas fa-plus"></i> **Añadir** y luego selecciona **Rutas de acción**.

![Canvas con "Rutas de acción" en el menú que se abre con el icono más.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Paso 4b: Crear grupos de acción {#step-4b-create-action-groups}

Cada grupo de acción representará todas las acciones que conducen al mismo incremento o decremento de puntos. Puedes configurar hasta ocho grupos de acción. En este escenario, crearemos cuatro grupos.

Añade los siguientes grupos a tu ruta de acción:

- **Grupo 1:** Todos los eventos que cuentan para un incremento de 1 punto.
- **Grupo 2:** Todos los eventos que cuentan para un incremento de 5 puntos.
- **Grupo 3:** Todos los eventos que cuentan para un decremento de 1 punto.
- **El resto:** Las rutas de acción te permiten definir la ventana de espera para ver si un usuario realiza una acción, antes de incluirlo en un grupo de "el resto". Para la puntuación de clientes potenciales, esta es una oportunidad para disminuir la puntuación por "inactividad".

![Ruta de acción que contiene grupos de acción para sumar un punto, cinco puntos y diez puntos; restar un punto y diez puntos; y "El resto".]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### Paso 4c: Configura cada grupo para incluir los eventos pertinentes {#step-4c-configure-each-group-to-include-the-relevant-events}

En cada grupo de acción, selecciona **Seleccionar activador** y elige el evento que sumará el número de puntos para ese grupo de acción en particular. Añade más activadores para incluir todos los eventos que incrementarán en uno la puntuación de clientes potenciales. Por ejemplo, un usuario podría incrementar su puntuación en uno cuando inicia una sesión en cualquier aplicación o realiza un evento personalizado (como registrarse o unirse a un seminario web).

![Grupo de acción para añadir un punto con los activadores de "Iniciar sesión en cualquier aplicación" y "Realizar evento personalizado".]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Paso 4d: Añadir pasos de actualización de usuario {#step-4d-add-user-update-steps}

Añade un paso de Actualización de usuario a cada ruta del Canvas creada debajo de tu ruta de acción.

![Canvas que muestra la ruta de acción con rutas de actualización de usuario ramificadas para cada grupo de acción.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start="2"}
En la pestaña **Redactar** de cada paso de actualización de usuario, haz lo siguiente para los campos respectivos:

| Campo | Acción |
| --- | --- |
| **Nombre del atributo** | Selecciona el atributo de puntuación de clientes potenciales que seleccionaste en el paso 2 (`lead score`). |
| **Acción** | Cambia la acción a **Incrementar por** si la ruta aumenta la puntuación o **Decrementar por** si la ruta disminuye la puntuación. |
| **Incrementar por** o **Decrementar por** | Introduce el número de puntos que se aumentarán o disminuirán de la puntuación de clientes potenciales. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 4d: Añadir pasos de actualización de usuario" }

### Paso 5: Lanza tu Canvas {#step-5-launch-your-canvas}

¡Eso es todo! Tu Canvas de puntuación de clientes potenciales está listo para lanzarse.

## Puntuación externa de clientes potenciales {#external-lead-scoring}

Ya sea utilizando uno de nuestros [socios tecnológicos]({{site.baseurl}}/partners/home/), tu propio modelo interno de puntuación de clientes potenciales, aprendizaje automático u otra herramienta de puntuación de clientes potenciales, tenemos múltiples opciones para ti.

### Socios externos {#external-partners}

Consulta [Socios tecnológicos]({{site.baseurl}}/partners/home/) para conocer a nuestros socios B2B que ofrecen funciones de puntuación de clientes potenciales. ¿No ves tu herramienta? Puedes realizar la integración llamando a nuestro punto de conexión de la API [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#track-users).

### Modelos de datos internos de puntuación de clientes potenciales {#internal-lead-scoring-data-models}

Puedes integrar Braze con tus modelos de datos internos, incluidos los modelos de puntuación de clientes potenciales, de varias maneras. A continuación encontrarás algunos ejemplos comunes de cómo nuestros clientes se han integrado con Braze.

#### Almacén de datos en la nube integrado {#integrated-cloud-data-warehouse}

{% tabs %}
{% tab Braze como origen de datos %}

Como herramienta de marketing, Braze contiene datos extremadamente relevantes que podrían complementar el modelo interno de puntuación de clientes potenciales de tu equipo.

Por ejemplo, los datos de interacción con la mensajería (como aperturas y clics de correos electrónicos, interacción en la página de inicio y otros) pueden determinar el nivel de interacción de un cliente potencial. Puedes devolver estos datos a tu almacén de datos en la nube y hacer que estén disponibles como entrada para tus modelos de puntuación de clientes potenciales utilizando las soluciones de exportación de datos en streaming de Braze:

- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)
- [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

{% endtab %}
{% tab Braze como destino %}

Después de que tus equipos internos hayan creado y ejecutado tu modelo de puntuación de clientes potenciales, puedes volver a introducir esos datos en Braze para poder segmentar y dirigir mejor a los clientes potenciales con mensajes relevantes. Puedes hacerlo con [Ingesta de datos de Cloud de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/).

Con la Ingesta de datos de Cloud, tus equipos internos crearán una nueva tabla o vista con tus identificadores de usuario, las últimas puntuaciones de clientes potenciales y las marcas de tiempo en las que se actualizaron las puntuaciones. Braze recogerá la tabla o vista y añadirá las puntuaciones de los clientes potenciales a los perfiles de usuario.

{% endtab %}
{% endtabs %}

## Traspaso de clientes potenciales: cliente potencial cualificado por marketing (MQL) a ventas {#lead-handoff}

Nuestro enfoque recomendado para los traspasos de clientes potenciales es tener un cliente potencial o contacto correspondiente vinculado a cada usuario en Braze. Estos clientes potenciales entrarían en la cola de tus equipos de ventas cuando sus estados cambien a una etapa MQL, momento en el que Salesforce iniciaría un flujo de trabajo de enrutamiento o asignación de clientes potenciales.

Para actualizar el registro de clientes potenciales en Salesforce con el estado del cliente potencial desde Braze, recomendamos utilizar una plantilla de webhook activada.

### Paso 1: Crear una Campaign de webhook {#step-1-create-a-webhook-campaign}

### Paso 2: Configura tu webhook {#step-2-configure-your-webhook}

#### Paso 2a: Redactar webhook {#step-2a-compose-webhook}

1. Dale un nombre a tu Campaign de webhook, como "Salesforce > Actualizar cliente potencial a MQL".

2. Introduce la URL de tu webhook en el formato {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}. El ID de usuario de Braze {% raw %}`{{${user_id}}}`{% endraw %} debe coincidir con tu ID de contacto de Salesforce. Si no es así, utiliza un alias en lugar de {% raw %}`{{${user_id}}}`{% endraw %}.

3. Actualiza el **método HTTP** a **PATCH**.

4. Configura la carga útil para que solo actualice el registro de clientes potenciales en Salesforce si la puntuación del cliente potencial supera el umbral predefinido. Consulta el ejemplo de cuerpo de solicitud a continuación para una puntuación de cliente potencial superior a 100.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5. Incluye los siguientes encabezados:

| Encabezado | Contenido |
| --- | --- |
| Authorization | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>Para recuperar un token, [configura una aplicación conectada](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) para el flujo de credenciales de cliente OAuth 2.0 y luego usa contenido conectado para recuperar el bearer de Salesforce: <br><br>{% raw %}<code>{% connected_content https://[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content-Type | application/json |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2a: Redactar webhook" }

![Webhook que se compone con una URL de webhook de Salesforce, método HTTP PATCH, cuerpo de solicitud de texto sin formato y encabezados de solicitud.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Paso 2b: Programar envíos de webhooks {#step-2b-schedule-webhook-sends}

La Campaign debe activarse cada vez que cambie la puntuación del usuario. Esta Campaign se activará para cualquier usuario cuya puntuación cambie, pero solo afectará a los usuarios que no sean actualmente un MQL y que hayan superado el umbral establecido en el paso anterior.

En el paso **Programar entrega**, selecciona lo siguiente:
- Un tipo de entrega **basado en acciones**
- Una acción desencadenante de **Cambiar valor de atributo personalizado** con el nombre de tu atributo de puntuación de clientes potenciales y una acción de **cualquier nuevo valor**

#### Paso 2c: Identificar la audiencia objetivo {#step-2c-identify-target-audience}

En el paso **Target Audiences**, incluye un filtro que excluya a los usuarios cuyo estado de cliente potencial ya esté en MQL o más allá, como "`lead_status` `is none of` `MQL`".

![Opciones de segmentación de webhooks con el filtro de "lead_status" is none of "MQL".]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Paso 3: Lanzar la Campaign {#step-3-launch-campaign}

Selecciona **Launch** y observa cómo cambia el estado de tus clientes potenciales en Salesforce a medida que tus clientes cruzan el umbral de puntuación de clientes potenciales MQL.