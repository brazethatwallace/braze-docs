---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "Este artículo de referencia describe la asociación entre Braze y Dynamics 365 Customer Insights, una plataforma líder de datos de clientes empresariales, que te permite exportar segmentos de clientes a Braze para utilizarlos en campañas o Canvas."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights

> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) es una plataforma líder de datos de clientes empresariales que ofrece experiencias de cliente personalizadas con una visión de 360 grados de tus clientes.

_Esta integración la mantiene Dynamics 365 Customer Insights._

## Sobre la integración {#about-the-integration}

La integración de Braze y Dynamics 365 Customer Insights te permite exportar segmentos de clientes a Braze para utilizarlos en campañas o Canvas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Dynamics 365 Customer Insights | Se necesita una cuenta de [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) para aprovechar esta asociación. Necesitarás acceso como administrador para ver y editar conexiones dentro de tu cuenta de Dynamics 365 Customer Insights para acceder a los plugins necesarios. |
| Clave de API REST or transferencia de estado representacional de Braze | Se necesita una clave de API REST or transferencia de estado representacional de Braze con los permisos `users.track` y `users.export.segment`. <br><br> Puede crearse en el dashboard de Braze desde **Settings** > **API Keys**. |
| Identificadores de perfiles coincidentes | Los perfiles de cliente unificados en los segmentos exportados contienen un campo que representa una dirección de correo electrónico y un `external_id` de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Establecer la conexión con Braze {#step-1-set-up-braze-connection}

En Customer Insights, ve a **Admin > Connections**. A continuación, selecciona **Add connections** y elige **Braze** para configurar la conexión.

1. Dale a tu conexión un nombre reconocible en el campo **Display name**.
2. Elige quién puede utilizar esta conexión. Si dejas este campo en blanco, el valor predeterminado será Administrators. Para más información, consulta [Allow contributors to use a connection for exports](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Proporciona tu clave de API de Braze y el punto de conexión REST or transferencia de estado representacional en el formato `rest.iad-03.braze.com`.
4. Selecciona **I agree** para confirmar la conformidad de los datos y la privacidad.
5. Selecciona **Connect** para inicializar la conexión con Braze.
6. Selecciona **Add yourself as export user** e introduce tus credenciales de Customer Insights.
7. Selecciona **Save** para completar la conexión.

### Paso 2: Crear un Segment en Braze {#step-2-create-a-braze-segment}

1. En Braze, ve a **Audience** > **Segments**.
2. Crea un segmento de los usuarios que quieres que Microsoft actualice a través de Dynamics 365 Customer Insights.
3. Captura el **API Identifier** del segmento.

### Paso 3: Configurar una exportación {#step-3-configure-an-export}

Puedes configurar esta exportación si tienes acceso a una conexión de este tipo. Para más información, consulta el [resumen de exportaciones](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. En Customer Insights, ve a **Data > Exports**. Para crear una nueva exportación, selecciona **Add destination**.
2. En el campo **Connection for export**, selecciona una conexión para la sección Braze. Si no ves el nombre de esta sección, no hay conexiones de este tipo disponibles para ti.
3. Proporciona el identificador de API del segmento en Braze.
4. En la sección **Data matching**, en el campo **Email**, selecciona el campo que representa la dirección de correo electrónico de un cliente. A continuación, en el campo **Braze Customer ID**, selecciona el campo que representa el ID de Braze del cliente. También puedes seleccionar un campo adicional opcional para cotejar los datos.
  a. Si mapeas el `external_id` en Braze con el campo Braze Customer ID en Customer Insights, los registros existentes se actualizarán en Braze al exportar.
  b. Si mapeas un campo ID diferente que no representa el `external_id` de un registro en Braze, o un campo vacío, se crearán nuevos registros en Braze al exportar.
5. Por último, selecciona los segmentos que quieras exportar y selecciona **Save**.

Ten en cuenta que guardar una exportación no la ejecuta inmediatamente. Esta exportación se ejecutará con cada [actualización programada](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab). También puedes [exportar datos bajo demanda](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand).


### Uso de esta integración {#using-this-integration}

Una vez que tus segmentos se hayan exportado correctamente a Braze, podrás encontrarlos como atributos personalizados en los perfiles de usuario. El atributo personalizado se denominará con el identificador de API del segmento de Braze que se introdujo al configurar la conexión de exportación. Por ejemplo, `"Segment_API_Identifier": "0000-0000-0000"`

Para crear un segmento de estos usuarios en Braze, ve a **Segments**, crea un nuevo segmento y selecciona **Custom Attributes** como filtro. Desde aquí, puedes elegir el atributo personalizado sincronizado con Dynamics 365. Una vez creado el segmento, puedes seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

{% alert note %}
Para más información sobre esta integración, visita el [artículo de Microsoft sobre la integración](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) con Braze.
{% endalert %}