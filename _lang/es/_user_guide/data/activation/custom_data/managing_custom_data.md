---
nav_title: Gestionar datos personalizados
article_title: Gestionar datos personalizados
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo gestionar eventos y atributos personalizados: rellenar previamente, añadir descripciones y etiquetas, gestionar propiedades del evento, forzar tipos de datos y marcar atributos como PII."
---

# Gestionar datos personalizados {#manage-custom-data}

> Esta página explica cómo rellenar previamente datos personalizados en tus campañas y segmentos, gestionar eventos y atributos personalizados y sus propiedades, y configurar tipos de datos. Para bloquear y eliminar datos personalizados, consulta [Bloquear datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

Para saber cómo gestionar atributos personalizados en particular (incluyendo añadir descripciones, añadir etiquetas y marcar atributos como PII), consulta [Gestionar atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes).

## Rellenar previamente datos personalizados {#pre-populate-custom-data}

Puede haber ocasiones en las que quieras configurar campañas y segmentos utilizando datos personalizados antes de que tu equipo de desarrollo haya integrado esos datos personalizados. Braze te permite rellenar previamente eventos y atributos personalizados en el dashboard antes de que estos datos comiencen a rastrearse, de modo que estos eventos y atributos estén disponibles para su uso en desplegables y como parte del proceso de creación de campañas.

Para rellenar previamente eventos y atributos personalizados, haz lo siguiente:

1. Ve a **Configuración de datos** > **Eventos personalizados** o **Atributos personalizados** o **Productos**.

![Navega hasta Atributos personalizados, Eventos personalizados o Productos.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2. Para añadir un atributo personalizado, un evento o un producto, ve a la página correspondiente y selecciona **Añadir atributos personalizados**, **Añadir eventos personalizados** o **Añadir productos**.<br><br>Para los atributos personalizados, selecciona un [tipo de datos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) para este atributo (por ejemplo, booleano o cadena). El tipo de datos de un atributo determina los filtros de segmentación disponibles para ese atributo. <br><br>![Añadir nuevo atributo o evento]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3. Selecciona **Guardar**.

### Nombrar eventos y atributos personalizados {#naming-custom-events-and-custom-attributes}

Los eventos y atributos personalizados distinguen entre mayúsculas y minúsculas. Ten esto en cuenta cuando tu equipo de desarrollo integre estos eventos o atributos personalizados más adelante. Deben nombrar los eventos o atributos personalizados exactamente como los nombraste aquí, o Braze generará un evento o atributo personalizado diferente.

## Gestión de propiedades {#managing-properties}

Después de crear un evento personalizado o un producto, selecciona **Administrar propiedades** de ese evento o producto para añadir nuevas propiedades, bloquear propiedades existentes y ver qué campañas o Canvas utilizan esta propiedad en un [evento desencadenante]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Propiedades personalizadas para un evento personalizado.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Para bloquear propiedades de eventos o productos, usa el menú de acciones en la página de propiedades. Para bloquear atributos personalizados, eventos o productos por completo, consulta [Bloquear datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

Para que estos atributos personalizados, eventos, productos o propiedades del evento añadidos sean rastreables, debes pedir a tu equipo de desarrollo que los cree en el SDK or kit de desarrollo de software utilizando el nombre exacto que usaste para añadirlos anteriormente. O puedes utilizar la [API]({{site.baseurl}}/api/basics) de Braze para importar datos sobre ese atributo. Después de eso, el atributo personalizado, evento u otro será accionable y se aplicará a tus usuarios.

{% include alerts/note_alerts.md alert='Manage custom data storage' %}

## Detección de tipos de datos entre entornos {#data-type-detection-across-environments}

Braze detecta automáticamente el tipo de datos de un atributo personalizado basándose en el primer valor que recibe. Si tu entorno de desarrollo envía primero un valor numérico como `100`, el atributo se almacena como número. Si el primer valor de tu entorno de producción llega como una cadena (como `"100"` entre comillas), el atributo se almacena como cadena.

Para evitar esto, asegúrate de que tu integración envíe tipos de datos coherentes en todos los entornos. Si ya se ha establecido el tipo incorrecto, puedes forzar el tipo de datos correcto en **Configuración de datos** > **Atributos personalizados** usando el [desplegable de tipo de datos](#forcing-data-type-comparisons).

## Forzar la comparación de tipos de datos {#forcing-data-type-comparisons}

Braze reconoce automáticamente los tipos de datos de los atributos que se le envían. Sin embargo, en el caso de que se apliquen varios tipos de datos a un mismo atributo, puedes forzar el tipo de datos de cualquier atributo para que Braze sepa cuál es. Selecciónalo en el desplegable de la columna **Tipo de datos**.

{% alert note %}
A partir del 30 de marzo de 2026, la detección automática solo establece un tipo de datos en la ingesta inicial. Para cambiar el tipo de datos después de la ingesta inicial, actualízalo manualmente siguiendo los pasos a continuación.
{% endalert %}

{% alert note %}
Forzar tipos de datos no se aplica a las propiedades del evento ni a las propiedades de la compra.
{% endalert %}

![Desplegable de tipo de datos de atributos personalizados]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Si eliges forzar el tipo de datos de un atributo, cualquier dato que entre y no sea del tipo especificado se convertirá a ese tipo. Si tal conversión es imposible (por ejemplo, que una cadena que contiene letras se convierta en un número), los datos se ignorarán. Cualquier dato ingerido antes del cambio de tipo seguirá almacenándose como el tipo antiguo (y, por tanto, puede no ser segmentable), y aparecerá una advertencia junto al atributo en los perfiles de los usuarios afectados.
{% endalert %}

### Datos existentes después de un cambio de tipo {#existing-data-after-a-type-change}

Forzar un cambio de tipo de datos solo afecta a los nuevos datos que llegan a Braze. Cualquier dato ingerido antes del cambio de tipo seguirá almacenándose como el tipo antiguo y puede no ser segmentable con los filtros del nuevo tipo. Aparecerá una advertencia en los perfiles de los usuarios afectados. Para los nuevos datos entrantes, si un valor no coincide con el tipo forzado, Braze puede convertirlo al tipo forzado (por ejemplo, la cadena `"100"` al número `100`); los valores que no se puedan convertir se ignoran y no actualizan el atributo.

Si necesitas que todos los datos de usuario existentes coincidan con el nuevo tipo, debes reenviar los valores del atributo para esos usuarios a través del SDK or kit de desarrollo de software, la API o una importación CSV. No existe una conversión masiva automática para los datos existentes.

### Coerción de tipos de datos {#data-type-coercion}

| Tipo de datos forzado | Descripción |
|------------------|-------------|
| Booleano | Las entradas `1`, `true`, `t` (sin distinguir mayúsculas de minúsculas) se almacenan como `true` |
| Booleano | Las entradas `0`, `false`, `f` (sin distinguir mayúsculas de minúsculas) se almacenan como `false` |
| Número | Los números enteros o flotantes (como `1`, `1.5`) se almacenan como números |
| Número | Las cadenas numéricas (como `"100"` o `"3.14"`) se pueden convertir a números cuando el atributo se fuerza a **Número** |
| Cadena | Los valores numéricos se pueden convertir a su forma de cadena cuando el atributo se fuerza a **Cadena** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Coerción de tipos de datos" }

Para obtener más información sobre las opciones de filtro que ofrecen las diferentes comparaciones de tipos de datos, consulta [Configuración de informes]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting). Para obtener más información sobre los diferentes tipos de datos disponibles, consulta [Tipos de datos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types).

{% alert note %}
Los datos enviados a Braze son inmutables y no pueden eliminarse ni modificarse después de que Braze los haya recibido. Sin embargo, puedes utilizar cualquiera de los pasos enumerados en las secciones anteriores para ejercer control sobre lo que estás rastreando en tu dashboard. Para bloquear o eliminar datos personalizados, consulta [Bloquear datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).
{% endalert %}