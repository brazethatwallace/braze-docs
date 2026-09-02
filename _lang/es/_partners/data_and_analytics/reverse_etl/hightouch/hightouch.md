---
nav_title: Hightouch
article_title: Hightouch
description: "Este artículo de referencia describe la asociación entre Braze y Hightouch, una plataforma para sincronizar los datos de tus clientes desde tu almacén a las herramientas empresariales."
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch](https://hightouch.io) es una moderna plataforma de integración de datos que te permite sincronizar datos de clientes, productos o propietarios desde tu almacén o lago de datos a cualquier aplicación de tu elección, todo ello sin ayuda de tus equipos de TI o ingeniería.

La integración de Braze y Hightouch te permite crear mejores campañas en Braze con datos de clientes actualizados procedentes de tu almacén de datos. Al sincronizar automáticamente los datos de los clientes en Braze, ya no tendrás que preocuparte por la coherencia de los datos y podrás centrarte en crear experiencias de cliente de primera clase.

Esta integración también te permite [importar cohortes de usuarios a Braze]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import), enviando campañas específicas basadas en datos que solo pueden existir en tu almacén.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Hightouch | Se necesita una cuenta Hightouch para beneficiarse de esta asociación.
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track` y `users.export.ids`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST or transferencia de estado representacional de Braze  | La URL de tu endpoint REST or transferencia de estado representacional. Tu endpoint dependerá de la [URL de Braze para tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints).<br><br>Hightouch necesita el nombre del clúster en el que se encuentra tu instancia de Braze. Por ejemplo, si tu endpoint de Braze es `https://rest.iad-01.braze.com`, solo necesitas `iad-01`.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

* Sincroniza datos sobre usuarios y cuentas en Braze para crear campañas hiperpersonalizadas.
* Actualiza automáticamente tus segmentos de Braze con datos frescos de tu almacén.
* Ofrece mejores experiencias incorporando a Braze datos de otros puntos de intervención con el cliente.
* Importa cohortes de usuarios a Braze, lo que te permitirá enviar campañas y Canvas específicos.

## Integración {#integration}

### Paso 1: Crea tu destino Hightouch Braze {#step-1-create-your-hightouch-braze-destination}

1. En la plataforma Hightouch, en la sección **Destinations**, haz clic en **Add destination**.
2. Selecciona **Braze** en la lista de destinos disponibles.
3. Proporciona tu endpoint REST de Braze (excluyendo "https://rest.") y tu clave de API REST de Braze.<br><br>![Formulario de configuración del destino Braze en Hightouch con campos de endpoint y clave de API.]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

### Paso 2: Sincronización de objetos y eventos {#step-2-object-and-event-syncing}

Hightouch permite sincronizar tanto objetos de usuario como eventos.

| Destino | Descripción | Modos admitidos |
|---|---|---|
| Objeto | Sincroniza los registros con objetos como usuarios u organizaciones en tu destino. | Upsert o actualizar |
| Eventos | Sincroniza los registros como eventos en tu destino; esto suele hacerse en forma de llamada de seguimiento. | Seguimiento de eventos o seguimiento de compras |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Sincronización de objetos y eventos" }

{% alert note %}
Consulta [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption) para obtener más información sobre cómo afectan las sincronizaciones al registro de los puntos de datos.
{% endalert %}

#### Sincronización de objetos Braze {#syncing-braze-objects}

Puedes sincronizar objetos Hightouch (campos de usuario) con los campos predeterminados o personalizados equivalentes de Braze. También puedes realizar la correspondencia de registros para ayudar a unificar los datos en las dos plataformas.

#### Sincronización de eventos Braze {#syncing-braze-events}

Hightouch te permite realizar un seguimiento de los datos de eventos y compras y sincronizarlos con Braze. En Hightouch se pueden configurar varias opciones que afectarán al comportamiento de la sincronización, como la configuración de los datos de seguimiento y la definición de un comportamiento de usuario inexistente.

{% alert important %}
Encontrarás más instrucciones sobre la sincronización de objetos y eventos en [la documentación de Hightouch](https://hightouch.io/docs/destinations/braze/).
{% endalert %}



## Demostración de integración {#integration-demo}

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" title="Demostración de integración de Hightouch" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>