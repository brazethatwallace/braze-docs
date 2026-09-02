---
nav_title: Clarisights
article_title: Clarisights
description: "Este artículo de referencia describe la asociación entre Braze y Clarisights, una plataforma de informes de marketing del rendimiento de autoservicio, que te permite importar datos de Campaigns y Canvas de Braze para conseguir una interfaz de informes unificada de marketing del rendimiento y CRM/retención."
alias: /partners/clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights](https://clarisights.com) es una plataforma autoservicio de informes de marketing del rendimiento para organizaciones basadas en datos. Integra, procesa y visualiza automáticamente todos tus datos procedentes de fuentes de marketing, analíticas y de atribución.

_Esta integración está mantenida por Clarisights._

## Sobre la integración {#about-the-integration}

La integración de Braze y Clarisights te permite importar datos de Campaigns y Canvas de Braze para conseguir una interfaz de informes unificada de marketing del rendimiento y CRM/retención.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Clarisights | Se requiere un espacio de trabajo de Clarisights para aprovechar esta asociación |
| Clave de API REST de Braze | Una clave de API REST de Braze con los siguientes permisos:  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Se puede crear en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
| Nombre del espacio de trabajo de Braze | El nombre del espacio de trabajo asociado a la clave de API de Braze. Este nombre se utilizará para identificar la integración del espacio de trabajo en Clarisights. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

Con la integración de Braze y Clarisights, los usuarios pueden crear diferentes visualizaciones y tablas para obtener información de las campañas que han creado. Algunos de los casos de uso más frecuentes son:

{% tabs %}
{% tab Mejor visibilidad %}
Mejor visibilidad del rendimiento global de Campaigns y Canvas.

![Un gráfico que muestra un ejemplo de mejor visibilidad en la plataforma Clarisights. Este gráfico incluye estadísticas de aperturas de Campaigns y Canvas, clics, envíos, conversiones, etc.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Informes detallados %}
Informes detallados para Campaigns y Canvas.

![Un gráfico que muestra informes detallados, como "total enviado por canal de envío" y "tasa de conversión".]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Paneles unificados %}
Paneles unificados para CMO y CXO.

![Un gráfico que muestra un ejemplo de paneles unificados.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Integración {#integration}

Para sincronizar datos de Braze con Clarisights, debes crear un conector de Braze y conectar espacios de trabajo de Braze.

1. En Clarisights, ve a la página **Integrations**, localiza el conector **Braze** y selecciona **+ Connect**.<br>![Una lista de los conectores disponibles en el marketplace de integraciones de Clarisights.]({{site.baseurl}}/assets/img/clarisights/integrations.png)<br><br>
2. A continuación, mediante el flujo de integración, conecta tu cuenta de Clarisights a Braze. Para ello, proporciona tu clave de API REST de Braze, el nombre del espacio de trabajo de Braze y el punto de conexión REST de Braze.<br>![Conector del espacio de trabajo de Braze en la plataforma Clarisights. Esta página tiene campos para el nombre del espacio de trabajo de Braze, la clave de API REST de Braze y el punto de conexión REST de Braze.]({{site.baseurl}}/assets/img/clarisights/braze_flow.png)<br><br>Antes de que la integración se realice correctamente, los usuarios verán los espacios de trabajo conectados en la misma página.<br>![En "Braze Accounts" encontrarás una lista de los espacios de trabajo conectados.]({{site.baseurl}}/assets/img/clarisights/connected.png)<br><br>

## Uso de esta integración {#using-this-integration}

Para incluir Braze como origen de datos en tus informes de Clarisights, ve a **Create New Report**. Asigna un nombre a tu informe y selecciona **Braze** como origen de datos en el mensaje que aparece. También puedes elegir las métricas y dimensiones que deseas incluir en el informe. Cuando hayas terminado, selecciona **Create Report**.

Los datos de Braze empezarán a fluir a partir de la siguiente importación de datos planificada. Ponte en contacto con tu administrador del éxito del cliente de Clarisights para solicitar rellenos de datos de mayor duración.

![Configuración de informes de Clarisights que muestra los campos de nombre y origen de datos. Para este ejemplo, se selecciona "Braze" como origen de datos.]({{site.baseurl}}/assets/img/clarisights/braze_report.png)

Visita Clarisights para obtener más información sobre las [métricas y dimensiones](https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions) disponibles o la [creación de informes](https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights).