---
nav_title: Calculadora de facturación
article_title: Calculadora de facturación
page_order: 5
description: "Este artículo de referencia cubre qué es un segmento del mensaje SMS, cómo se cuentan para la facturación, así como aspectos a tener en cuenta al crear el texto de mensajes SMS y RCS."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# Calculadoras de facturación de SMS y RCS {#sms-and-rcs-billing-calculators}

> En Braze, los mensajes SMS se cobran por segmento del mensaje, mientras que los mensajes RCS se cobran por mensaje. Comprender qué define un segmento de SMS y los diferentes tipos de facturación de RCS te ayudará a entender cómo se te facturará y a prevenir excedentes accidentales.

## Texto de mensajes SMS y calculadora de segmentos {#sms-message-copy-and-segment-calculator}

Los mensajes SMS se cobran por segmento del mensaje. Comprender cómo se dividen los mensajes SMS es clave para entender tu facturación.

### ¿Qué es un segmento de SMS? {#what-is-an-sms-segment}

El servicio de mensajes cortos (SMS) es un protocolo de comunicación estandarizado que permite a los dispositivos enviar y recibir mensajes de texto breves. Fue diseñado para "encajar entre" otros protocolos de señalización, por lo que la longitud de los mensajes SMS está limitada a 160 caracteres de 7 bits, es decir, 1120 bits o 140 bytes. Los segmentos de mensajes SMS son los lotes de caracteres que los operadores telefónicos utilizan para medir los mensajes de texto. Los mensajes se cobran por segmento del mensaje, por lo que los clientes que utilizan SMS se benefician enormemente de comprender los matices de cómo se dividirán los mensajes.

Al crear una campaña o Canvas de SMS con Braze, los mensajes que construyes en el creador de mensajes son representativos de lo que tus usuarios pueden ver cuando el mensaje se entrega en su teléfono, pero **no son indicativos de cómo se dividirá tu mensaje en segmentos y, en última instancia, de cómo se te cobrará**. Comprender cuántos segmentos se enviarán y ser consciente de los posibles excedentes que podrían ocurrir es tu responsabilidad, pero proporcionamos algunos recursos para facilitarte esto. Consulta nuestra [calculadora de segmentos](#segment-calculator) integrada.

![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Desglose de segmentos {#segment-breakdown}

El límite de caracteres para **un segmento de SMS independiente** es de 160 caracteres (codificación [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)) o 70 caracteres (codificación [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)) según el tipo de codificación. Sin embargo, la mayoría de los teléfonos y redes admiten la concatenación, ofreciendo mensajes SMS de formato más largo de hasta 1530 caracteres (GSM-7) o 670 caracteres (UCS-2). Así que, aunque un mensaje pueda incluir varios segmentos, si no excede estos límites de concatenación, se visualizará como un solo mensaje y se reportará como tal.

Es importante tener en cuenta que **al superar el límite de caracteres de tu primer segmento, los caracteres adicionales harán que todo tu mensaje se divida y segmente según nuevos límites de caracteres**:
- **Codificación GSM-7**
    - Los mensajes que excedan el límite de 160 caracteres se segmentarán en segmentos de 153 caracteres y se enviarán individualmente, para luego ser reconstruidos por el dispositivo del destinatario. Por ejemplo, un mensaje de 161 caracteres se enviará como dos mensajes, uno con 153 caracteres y el segundo con 8 caracteres.
- **Codificación UCS-2**
    - Si incluyes caracteres no GSM como emojis, escritura china, coreana o japonesa en los mensajes SMS, esos mensajes deben enviarse mediante codificación UCS-2. Los mensajes que excedan el límite inicial de segmento de 70 caracteres harán que todo el mensaje se concatene en segmentos de 67 caracteres. Por ejemplo, un mensaje de 71 caracteres se enviará como dos mensajes, uno con 67 caracteres y el segundo con 4 caracteres.

Independientemente del tipo de codificación, cada mensaje SMS enviado por Braze tiene un límite de hasta 10 segmentos y es compatible con [plantillas Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/), [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), emojis y enlaces.

{% tabs %}
{% tab Codificación GSM-7 %}
| Número de caracteres | ¿Cuántos segmentos? |
| -------------------- | ----------------- |
| 0 - 160 caracteres | 1 segmento |
| 161 - 306 caracteres | 2 segmentos |
| 307 - 459 caracteres | 3 segmentos |
| 460 - 612 caracteres | 4 segmentos |
| 613 - 765 caracteres | 5 segmentos |
| 766 - 918 caracteres | 6 segmentos |
| 919 - 1071 caracteres | 7 segmentos |
| 1072 - 1224 caracteres | 8 segmentos |
| 1225 - 1377 caracteres | 9 segmentos |
| 1378 - 1530 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment breakdown" }
{% endtab %}
{% tab Codificación UCS-2 %}
| Número de caracteres | ¿Cuántos segmentos? |
| -------------------- | ----------------- |
| 0 - 70 caracteres | 1 segmento |
| 71 - 134 caracteres | 2 segmentos |
| 135 - 201 caracteres | 3 segmentos |
| 202 - 268 caracteres | 4 segmentos |
| 269 - 335 caracteres | 5 segmentos |
| 336 - 402 caracteres | 6 segmentos |
| 403 - 469 caracteres | 7 segmentos |
| 470 - 536 caracteres | 8 segmentos |
| 537 - 603 caracteres | 9 segmentos |
| 604 - 670 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment breakdown" }
{% endtab %}
{% endtabs %}

### Aspectos a tener en cuenta al crear tu texto {#things-to-keep-in-mind-as-you-create-your-copy}

- **Límite de caracteres por segmento**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) tiene un límite de 160 caracteres para un solo segmento de SMS. Para mensajes con más de 160 caracteres, todos los mensajes se segmentarán con un límite de 153 caracteres.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) tiene un límite de 70 caracteres por segmento del mensaje. Para mensajes con más de 70 caracteres, todos los mensajes se segmentarán con un límite de 67 caracteres.<br><br>
- **Límite de segmentos por mensaje**
    - Hay una cantidad máxima de segmentos que puedes enviar debido a las limitaciones del medio. No se pueden enviar más de **10 segmentos** de mensajes en un solo mensaje SMS de Braze.
    - Esos 10 segmentos estarán limitados a 1530 caracteres (codificación GSM-7) o 670 caracteres (codificación UCS-2).<br><br>
- **Compatible con plantillas Liquid, Contenido conectado, emojis y enlaces**
    - Las plantillas Liquid y el Contenido conectado pueden poner tu mensaje en riesgo de superar el límite de caracteres para tu tipo de codificación. Puedes usar el [filtro truncate words](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) para limitar el número de palabras que tu Liquid podría agregar al mensaje.
    - Los emojis no tienen un conteo de caracteres estándar entre todos los emojis, así que asegúrate de probar que tus mensajes se segmenten y muestren correctamente.
    - Los enlaces pueden usar muchos caracteres, lo que resulta en más segmentos del mensaje de los previstos. Aunque es posible usar acortadores de enlaces, se recomienda usarlos con códigos abreviados. Visita nuestras [preguntas frecuentes sobre SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs/) para más información.<br><br>
- **Pruebas**
    - Siempre prueba tus mensajes SMS antes de lanzarlos, especialmente al usar Liquid y Contenido conectado, ya que superar los límites del mensaje o del texto puede resultar en cargos adicionales. Ten en cuenta que los mensajes de prueba contarán para tus límites de mensajes.

### Calculadora de segmentos de SMS {#segment-calculator}
---

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

## Facturación de mensajes RCS {#rcs-message-billing}

Los mensajes RCS se facturan según su contenido y el país en el que se entrega el mensaje. Para estimar los costos con precisión, es esencial comprender los diferentes tipos de mensajes y cómo se facturan.

### Tipos de facturación de RCS {#rcs-billing-types}

Nuestra plataforma admite dos modelos de facturación principales: un modelo global y un modelo de Estados Unidos.

#### Modelo global (mercados fuera de EE. UU.) {#global-model-non-us-markets}

Los mensajes se facturan por mensaje y se clasifican como Basic o Single.

{% tabs local %}
{% tab Basic %}

Los mensajes RCS Basic son mensajes de solo texto de hasta 160 caracteres y se facturan como un solo mensaje.

{% alert note %}
Agregar botones o cualquier elemento enriquecido cambiará el tipo de mensaje a un mensaje RCS Single.
{% endalert %}

{% endtab %}
{% tab Single %}

Los mensajes RCS Single son mensajes que superan los 160 caracteres O incluyen cualquier elemento enriquecido como botones o medios. Se facturan como un solo mensaje, independientemente de la longitud del mensaje.

{% alert note %}
Enviar un mensaje de texto y un archivo multimedia por separado se factura como dos mensajes distintos.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Modelo de Estados Unidos {#united-states-model}

Los mensajes se categorizan como Rich o Rich Media.

{% tabs local %}
{% tab Mensajes Rich %}

Los mensajes Rich son mensajes de solo texto con o sin botones. Se facturan por segmento, con cada segmento limitado a 160 bytes UTF-8, lo que significa que **el número de caracteres por segmento no es fijo**. Un mensaje con solo 160 caracteres en inglés simple es un segmento, pero un mensaje con texto más largo y emojis podría ser múltiples segmentos.

{% endtab %}
{% tab Mensajes Rich Media %}

Los mensajes Rich Media incluyen un archivo multimedia (imagen, video) o una Rich Card y se facturan como un solo mensaje.

{% endtab %}
{% endtabs %}

### Creador de mensajes y dashboard de uso de créditos {#message-composer-and-credits-usage-dashboard}

Al crear tu mensaje, el creador de mensajes mostrará el tipo de facturación en tiempo real a través de una etiqueta (Basic RCS, Single RCS, Rich o Rich Media), ayudándote a rastrear los costos antes de enviar.

Tu [dashboard de uso de créditos]({{site.baseurl}}/credits_usage_dashboard/) reflejará estos tipos de facturación y proporcionará el número de segmentos utilizados para mensajes de EE. UU., ofreciendo una vista transparente del consumo de créditos de mensajes.