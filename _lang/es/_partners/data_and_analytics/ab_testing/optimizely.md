---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "Este artículo de referencia describe la asociación entre Braze y Optimizely que te permite sincronizar tus Segments de clientes, eventos y eventos de Currents de Braze con Optimizely Data Platform."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) es una plataforma líder de experiencia digital que ofrece herramientas de experimentación y gestión de contenidos para productos digitales y campañas de marketing.

La integración de Braze y Optimizely es una integración bidireccional que te permite:

{% multi_lang_include partners/ab_testing/optimizely_integration_bullets.md %}

## Requisitos previos {#prerequisites}

| Requisito                        | Descripción |
|----------------------------------|-------------|
| Cuenta de Optimizely Data Platform | Se requiere una cuenta de Optimizely Data Platform (ODP) para aprovechar esta integración. |
| Clave de API REST or transferencia de estado representacional de Braze       | Una clave de API REST or transferencia de estado representacional de Braze con los siguientes permisos: `users.track`, `users.export.segments`, `segments.list`, `campaigns.trigger.send` y `canvas.trigger.send`. |
| Currents                         | Para exportar datos de vuelta a Optimizely, necesitas tener Braze Currents configurado para tu cuenta. |
| URL y token de Optimizely        | Puedes obtenerlos navegando a tu panel de Optimizely y copiando la URL de ingesta y el token. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Configurar la integración {#step-1-configure-the-integration}

1. En el **App Directory** de Optimizely Data Platform (ODP), selecciona la aplicación **Braze** y luego selecciona **Install App**.
2. Ve a la pestaña **Settings**. En la sección **Authorization**, haz lo siguiente:
    1. Introduce la **clave de API REST or transferencia de estado representacional** de Braze.
    2. Selecciona tu **URL de instancia** de Braze.
    2. Selecciona **Verify API Key**.
3. En Braze, ve a **[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents)**.
4. Selecciona **Create New Current** > **Custom Currents Export**.
5. Configura el Current usando el endpoint y el token proporcionados en ODP. Esto es necesario para sincronizar los eventos de Braze con ODP.

![Autorización de Optimizely.]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6. En ODP, expande la sección **Segments** y selecciona segmentos específicos de la lista **Segments to Sync**, o selecciona **Import All Customers** para sincronizar todos los segmentos.
7. Añade cualquier [mapeado de campos adicional](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) que desees entre Braze y ODP.
8. Selecciona **Save**.

![Sincronización de segmentos de Braze en Optimizely.]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Debes seleccionar segmentos para importar perfiles de clientes de Braze. Si no seleccionas ningún segmento, la integración no importará ningún perfil de cliente.
{% endalert %}

### Paso 2: Mapear campos de datos {#step-2-map-data-fields}

La integración tiene mapeados de campos de datos predeterminados entre Braze y ODP. Por ejemplo, el campo **Email** en Braze está mapeado al campo **Last Seen Email** en ODP.

![Mapeado de campos de segmentos entre Optimizely y Braze.]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### Mapear campos adicionales (opcional) {#map-additional-fields-optional}

Si hay campos de datos adicionales en Braze que deseas mapear a ODP, haz lo siguiente en ODP:

1. En la sección **Segments** de la aplicación, selecciona el campo de Braze de la lista desplegable **Braze User Data Fields**.
2. Selecciona el campo de ODP de la lista desplegable **ODP Customer Fields**.
3. Selecciona **Save Field Map**.

![Guardar mapeado de campos de segmentos de Braze en Optimizely]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### Eliminar mapeados de campos no requeridos (opcional) {#delete-non-required-field-mappings-optional}

También puedes eliminar cualquier mapeado de campos de datos que no sea necesario. Haz lo siguiente en ODP:

1. En la sección **Segments** de la aplicación, selecciona el mapeado de campos que deseas eliminar de la lista desplegable **Field Map**.
2. Selecciona **Delete Field Map**.

![Eliminar mapeado de campos de segmentos de Braze en Optimizely]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### Paso 3: Sincronizar datos de Optimizely Data Platform (ODP) a Braze {#step-3-sync-data-from-optimizely-data-platform-odp-to-braze}

Después de configurar la integración, puedes configurar una activación en ODP para sincronizar los datos de clientes de ODP con Braze.

1. Ve a **Activation** > **Engage** y selecciona **Create New Campaign**.
2. Selecciona **Behavioral** para configurar una sincronización automatizada y recurrente.
3. Selecciona **Create From Scratch** y luego introduce un nombre para tu activación que represente los datos que estás sincronizando con Braze (como **Braze Data Sync**).
4. En la sección **Enrollment**, puedes sincronizar datos de clientes que coincidan con un segmento o sincronizar datos de clientes que desencadenen un evento (como cuando ODP registra que un cliente abre un correo electrónico):
   - **Clientes que coinciden con un segmento:** Selecciona el segmento deseado y luego selecciona **Next**.<br><br>![Seleccionar segmento en Optimizely]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **Clientes que desencadenan un evento:** Expande la lista desplegable **Filter** y selecciona el evento de ODP que se usará como desencadenante para esta sincronización de datos con Braze. Luego, expande **Automation Rules** y ajusta según lo desees. <br><br>![Evento desencadenante en Optimizely]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. Expande **Touchpoints**, selecciona para editar **Touchpoint 1** y luego selecciona **Braze**.
6. Expande la sección **Targeting** y luego selecciona el **Target Identifier**.
7. Selecciona una de las siguientes opciones para **Add Users To** en la sección **Configure**:
    - **Campaign:** Añade clientes a una Campaign específica en Braze. Después de elegir esta opción, debes seleccionar la Campaign de Braze.
    - **Canvas:** Añade clientes a un Canvas específico en Braze. Después de elegir esta opción, debes seleccionar el Canvas de Braze.
    - **Profile Update Only:** Actualiza solo el perfil de cliente de Braze.
8. (Opcional) Selecciona el **Number of Additional Fields** que deseas sincronizar con Braze (hasta 20).
    Luego, selecciona lo siguiente para cada lista desplegable y campo de entrada de cada campo adicional:
    - En cada lista desplegable **Field #**, selecciona el campo de Braze que deseas completar.
    - En cada **Field # Value** correspondiente, introduce el campo de ODP que deseas enviar al campo de Braze seleccionado. Por ejemplo, si seleccionaste **Company Name** de la lista desplegable **Field #**, introduce `{{customer.company_name}}` para el **Field # Value** correspondiente.
9. Selecciona **Save** y luego selecciona el nombre de tu activación en la ruta de navegación.
10. Selecciona **Select start time and schedule** en la sección **Touchpoints** si seleccionaste **Customers that match a segment** para la inscripción.
11. Completa la siguiente configuración:
    - **Recurring or Continuous:** Selecciona **Recurring**.
    - **Start Date:** Introduce la fecha en la que deseas enviar los datos a Braze.
    - **End:** El valor predeterminado es **Never**. Si deseas finalizar la sincronización de datos con Braze en una fecha específica, configúralo aquí.
    - **Repeats:** Configura como **Daily**.
    - **Repeat Every:** Configura como **1 day**.
    - **Timing:** Introduce la hora a la que deseas enviar los datos a Braze.
    - **Time Zone:** Selecciona la zona horaria en la que deseas enviar estos datos.
12. Selecciona **Apply**, **Save** y luego **Go Live**. Tu sincronización comienza en la fecha y hora de inicio designadas (o cuando ocurra el evento desencadenante).

## Solución de problemas {#troubleshooting}

### Inspeccionar eventos {#inspect-events}

Para verificar que los datos se están sincronizando correctamente de ODP a Braze, puedes inspeccionar los eventos en ODP.

1. En ODP, ve a **Account Settings** > **Event Inspector**.
2. Selecciona **Start Inspector**.
3. Cuando los datos estén disponibles en el inspector, se mostrará un número junto a **Refresh**. Selecciónalo para ver los datos.
4. Se mostrarán los datos sin procesar que ODP y Braze envían y reciben. Selecciona **View Details** para ver la versión formateada de esos datos sin procesar.
5. Los campos de datos enviados desde Braze de vuelta a ODP comienzan con `_braze`.

### Consultar los registros de actividad {#check-activity-logs}

Cada sincronización de datos también se registra en el [registro de actividad de ODP](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP):

1. Ve a **Account Settings** > **Activity Log**.
2. Filtra las categorías por **braze**.
3. Selecciona **View Details** para ver una vista formateada de los detalles del registro, incluyendo el número de coincidencias.