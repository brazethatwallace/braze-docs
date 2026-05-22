---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "Este artículo de referencia describe la asociación entre Braze y Optimizely que te permite sincronizar tus segmentos de clientes, eventos y eventos de Currents de Braze con Optimizely Data Platform."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) es una plataforma líder de experiencia digital que ofrece herramientas de experimentación y gestión de contenidos para productos digitales y campañas de marketing.

La integración de Braze y Optimizely es una integración bidireccional que te permite:

- Sincronizar tus segmentos y eventos de clientes de Braze con Optimizely Data Platform (ODP) cada noche para enriquecer los perfiles, informes y la segmentación de clientes de Optimizely.
- Enviar eventos de Braze Currents desde Braze a la herramienta de informes de Optimizely.
- Sincronizar datos de clientes y eventos de ODP con Braze para enriquecer tus datos de clientes de Braze y desencadenar mensajería de Braze basada en eventos de clientes en ODP.

## Requisitos previos {#prerequisites}

| Requisito                     | Descripción |
|----------------------------------|-------------|
| Cuenta de Optimizely Data Platform | Se necesita una cuenta de Optimizely Data Platform (ODP) para aprovechar esta asociación. |
| Clave de API REST de Braze               | Una clave de API REST de Braze con los siguientes permisos: `users.track`, `users.export.segments`, `segments.list`, `campaigns.trigger.send` y `canvas.trigger.send`. |
| Currents                         | Para volver a exportar datos a Optimizely, necesitas tener Braze Currents configurado en tu cuenta. |
| URL y token de Optimizely         | Esto se puede obtener navegando a tu dashboard de Optimizely y copiando la URL de ingesta y el token. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Configura la integración {#step-1-configure-the-integration}

1. En el **App Directory** de Optimizely Data Platform (ODP), selecciona la aplicación **Braze** y luego selecciona **Install App**.
2. Ve a la pestaña **Settings**. En la sección **Authorization**, haz lo siguiente:
    1. Introduce la **REST API Key** de Braze.
    2. Selecciona la **Instance URL** de Braze.
    2. Selecciona **Verify API Key**.
3. En Braze, ve a **[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/)**.
4. Selecciona **Create New Current** > **Custom Currents Export**.
5. Configura el Current utilizando el punto de conexión y el token proporcionados en ODP. Esto es necesario para sincronizar los eventos de Braze con ODP.

![Autorización de Optimizely.]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6. En ODP, expande la sección **Segments** y selecciona segmentos específicos de la lista **Segments to Sync**, o selecciona **Import All Customers** para sincronizar todos los segmentos.
7. Añade los [mapeados de campo adicionales](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) que quieras entre Braze y ODP.
8. Selecciona **Save**.

![Sincronización de segmentos de Optimizely y Braze.]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Debes seleccionar segmentos para importar perfiles de clientes de Braze. Si no seleccionas ningún segmento, la integración no importará ningún perfil de cliente.
{% endalert %}

### Paso 2: Mapear campos de datos {#step-2-map-data-fields}

La integración tiene mapeados predeterminados de campos de datos entre Braze y ODP. Por ejemplo, el campo **Email** en Braze está mapeado al campo **Last Seen Email** en ODP.

![Campos de mapeado de segmentos de Optimizely y Braze.]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### Mapear campos adicionales (opcional) {#map-additional-fields-optional}

Si hay campos de datos adicionales en Braze que quieras mapear en ODP, haz lo siguiente en ODP:

1. En la sección **Segments** de la aplicación, selecciona el campo de Braze de la lista desplegable **Braze User Data Fields**.
2. Selecciona el campo de ODP de la lista desplegable **ODP Customer Fields**.
3. Selecciona **Save Field Map**.

![Guardar mapeados de campo de segmentos de Optimizely y Braze]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### Eliminar mapeados de campos no obligatorios (opcional) {#delete-non-required-field-mappings-optional}

También puedes eliminar los mapeados de campos de datos que no sean necesarios. Haz lo siguiente en ODP:

1. En la sección **Segments** de la aplicación, selecciona el mapeado de campos que quieras eliminar de la lista desplegable **Field Map**.
2. Selecciona **Delete Field Map**.

![Eliminar mapeados de campo de segmentos de Optimizely y Braze]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### Paso 3: Sincronizar datos de Optimizely Data Platform (ODP) con Braze {#step-3-sync-data-from-optimizely-data-platform-odp-to-braze}

Después de configurar la integración, puedes establecer una activación en ODP para sincronizar tus datos de clientes de ODP con Braze.

1. Ve a **Activation** > **Engage** y selecciona **Create New Campaign**.
2. Selecciona **Behavioral** para configurar una sincronización automatizada y recurrente.
3. Selecciona **Create From Scratch** y, a continuación, introduce un nombre para tu activación que represente los datos que vas a sincronizar con Braze (como **Braze Data Sync**).
4. En la sección **Enrollment**, puedes sincronizar los datos de los clientes que coincidan con un segmento o sincronizar los datos de los clientes que desencadenen un evento (como cuando ODP registra que un cliente abre un correo electrónico):
   - **Clientes que coinciden con un segmento:** Selecciona el segmento que desees y, a continuación, selecciona **Next**.<br><br>![Seleccionar segmento en Optimizely]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **Clientes que desencadenan un evento:** Despliega la lista desplegable **Filter** y selecciona el evento de ODP que se va a utilizar como desencadenante de esta sincronización de datos con Braze. A continuación, expande **Automation Rules** y ajústalas como desees. <br><br>![Evento desencadenante de Optimizely]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. Despliega **Touchpoints**, selecciona para editar **Touchpoint 1** y, a continuación, selecciona **Braze**.
6. Despliega la sección **Targeting** y, a continuación, selecciona el **Target Identifier**.
7. Selecciona una de las siguientes opciones para **Add Users To** en la sección **Configure**:
    - **Campaign:** Añade clientes a una Campaign específica en Braze. Después de elegir esta opción, debes seleccionar la Campaign de Braze.
    - **Canvas:** Añade clientes a un Canvas específico en Braze. Tras elegir esta opción, debes seleccionar el Canvas de Braze.
    - **Profile Update Only:** Actualiza solo el perfil de cliente de Braze.
8. (Opcional) Selecciona el **Number of Additional Fields** que quieres sincronizar con Braze (hasta 20).
    A continuación, selecciona lo siguiente para cada lista desplegable de campo adicional y campo de entrada:
    - En cada lista desplegable **Field #**, selecciona el campo de Braze que quieras rellenar.
    - En cada **Field # Value** correspondiente, introduce el campo de ODP que quieres enviar al campo de Braze seleccionado. Por ejemplo, si seleccionaste **Company Name** en la lista desplegable **Field #**, introduce `{{customer.company_name}}` para el correspondiente **Field # Value**.
9. Selecciona **Save** y, a continuación, selecciona el nombre de tu activación en la ruta de migas de pan.
10. Selecciona **Select start time and schedule** en la sección **Touchpoints** si has seleccionado **Customers that match a segment** para la inscripción.
11. Completa la siguiente configuración:
    - **Recurring or Continuous:** Selecciona **Recurring**.
    - **Start Date:** Introduce la fecha en la que quieres enviar los datos a Braze.
    - **End:** Predeterminado a **Never**. Si quieres finalizar la sincronización de datos de Braze en una fecha concreta, establécelo aquí.
    - **Repeats:** Ajústalo a **Daily**.
    - **Repeat Every:** Ajústalo a **1 day**.
    - **Timing:** Introduce la hora a la que quieres enviar los datos a Braze.
    - **Time Zone:** Selecciona la zona horaria en la que quieres enviar estos datos.
12. Selecciona **Apply**, **Save** y, a continuación, **Go Live**. Tu sincronización comienza en la fecha y hora de inicio que designes (o cuando se produzca el evento desencadenante).

## Solución de problemas {#troubleshooting}

### Inspeccionar eventos {#inspect-events}

Para verificar que los datos se sincronizan correctamente desde ODP a Braze, puedes inspeccionar los eventos en ODP.

1. En ODP, ve a **Account Settings** > **Event Inspector**.
2. Selecciona **Start Inspector**.
3. Cuando hay datos disponibles en el inspector, aparece un número junto a **Refresh**. Selecciónalo para ver los datos.
4. Se muestran los datos en bruto que ODP y Braze envían de un lado a otro. Selecciona **View Details** para ver la versión formateada de esos datos en bruto.
5. Los campos de datos enviados desde Braze a ODP empiezan por `_braze`.

### Comprobar los registros de actividad {#check-activity-logs}

Cada sincronización de datos también se registra en el [registro de actividad de ODP](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP):

1. Ve a **Account Settings** > **Activity Log**.
2. Filtra las categorías por **braze**.
3. Selecciona **View Details** para obtener una vista formateada de los detalles del registro, incluido el número de coincidencias.