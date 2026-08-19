---
nav_title: Descripciones de Action Credits de Braze
permalink: "/message_credits_descriptions/"
hidden: true
noindex: true
hide_toc: true
---

# Descripciones de Action Credits de Braze {#braze-action-credits-descriptions}

> Los Action Credits proporcionan una estructura flexible que te permite acceder fácilmente a mensajería multicanal y productos avanzados de IA, maximizando tu presupuesto de marketing. Comienza interactuando en un solo canal o región y amplía tu combinación fácilmente para incluir agentes de IA a medida que tu modelo de negocio, base de clientes y estrategias de participación evolucionen.

Los Action Credits se pueden aplicar en cualquiera de los canales y características presentados en esta página.

Ten en cuenta que el "ratio de créditos" referenciado en esta página se define como el número exacto de Action Credits necesarios para realizar la acción especificada.

## Tabla de contenidos {#table-of-contents}

- [Detalles del canal de correo electrónico](#email-channel-details)
- [Detalles de los canales SMS, MMS y RCS](#sms-mms-and-rcs-channel-details)
  - [Segmentos del mensaje SMS](#sms-segments)
  - [Mensajes MMS](#mms-messages)
  - [Tipos de RCS](#rcs-types)
- [Detalles del canal de WhatsApp](#whatsapp-channel-details)
  - [Desglose por región de facturación](#billing-region-breakdown)
- [Detalles de Agent Console](#agent-console-details)
- [Detalles de canales adicionales](#additional-channel-details)
  - [LINE](#line)
  - [KakaoTalk](#kakaotalk)
  - [Content Cards](#content-cards)
  - [Banners](#banners)
  - [Audience Sync](#audience-sync)
  - [Archivado de mensajes](#message-archiving)
  - [Webhooks](#webhooks)

## Detalles del canal de correo electrónico {#email-channel-details}

Las proporciones de créditos de correo electrónico se denominan en incrementos de mil correos electrónicos enviados (CPM) desde la plataforma Braze.

{% alert note %}
Consulta nuestra [documentación de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email) para obtener más información sobre nuestro canal de correo electrónico.
{% endalert %}

## Detalles del canal SMS, MMS y RCS {#sms-mms-and-rcs-channel-details}

Las proporciones de créditos de SMS y MMS se denominan en incrementos de segmentos enviados desde la plataforma Braze. Las proporciones de créditos de RCS se denominan en incrementos de tipos Básico y Multimedia enriquecida, o tipos Único y Multimedia enriquecida entregados desde la plataforma Braze. Tanto los tipos entrantes como los salientes se facturan.

{% alert note %}
Cuando corresponda para estos canales, las tarifas del operador se facturan por separado (a mes vencido) y no se consideran parte de los Créditos de acción.
{% endalert %}

### Segmentos de SMS {#sms-segments}

La industria de SMS cuenta los mensajes en segmentos del mensaje SMS. Un segmento del mensaje es una agrupación de hasta un número definido de caracteres (160 para codificación GSM-7; 67 para codificación UCS-2) que se enviará en un único despacho de SMS. Si envías un SMS con 161 caracteres usando codificación GSM-7, se enviarán dos (2) segmentos del mensaje. Enviar múltiples segmentos del mensaje generará cargos adicionales.

### Mensajes MMS {#mms-messages}

Para MMS, el límite del mensaje es de 5 MB (esto incluye el activo multimedia y el tamaño del cuerpo del mensaje). Para mayor seguridad, Braze recomienda no exceder los 600 KB para tu activo multimedia e incluir también un cuerpo de mensaje.

### Tipos de RCS {#rcs-types}

RCS es la próxima generación de SMS y MMS. Ofrece los beneficios de un canal directo y de alta participación como SMS, con capacidades más ricas que los consumidores modernos esperan, como contenido enriquecido (imágenes, videos, documentos), envío verificado y con marca, características interactivas como respuestas y acciones sugeridas, y más.

{% multi_lang_include pricing/rcs_billing_message_types.md %}

{% alert note %}
Consulta nuestra [documentación de SMS y MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms) para obtener más información sobre nuestras ofertas de la familia SMS.
{% endalert %}

## Detalles del canal de WhatsApp {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## Desglose por región de facturación {#billing-region-breakdown}

### Norteamérica {#north-america}

Estados Unidos, Canadá

### Resto de África {#rest-of-africa}

Argelia, Angola, Benín, Botsuana, Burkina Faso, Burundi, Camerún, Chad, Congo, Eritrea, Etiopía, Gabón, Gambia, Ghana, Guinea-Bisáu, Costa de Marfil, Kenia, Lesoto, Liberia, Libia, Madagascar, Malaui, Malí, Mauritania, Marruecos, Mozambique, Namibia, Níger, Ruanda, Senegal, Sierra Leona, Somalia, Sudán del Sur, Sudán, Suazilandia, Tanzania, Togo, Túnez, Uganda, Zambia

### Resto de Asia-Pacífico {#rest-of-asia-pacific}

Afganistán, Australia, Bangladés, Camboya, China, Japón, Laos, Mongolia, Nepal, Nueva Zelanda, Papúa Nueva Guinea, Filipinas, Sri Lanka, Taiwán, Tayikistán, Tailandia, Turkmenistán, Uzbekistán, Vietnam

### Resto de Europa Central y Oriental {#rest-of-central-eastern-europe}

Albania, Armenia, Azerbaiyán, Bielorrusia, Bulgaria, Croacia, República Checa, Georgia, Grecia, Letonia, Lituania, Macedonia, Moldavia, Serbia, Eslovaquia, Eslovenia, Ucrania

### Resto de América Latina {#rest-of-latin-america}

Bolivia, Costa Rica, República Dominicana, Ecuador, El Salvador, Guatemala, Haití, Honduras, Jamaica, Nicaragua, Panamá, Paraguay, Puerto Rico, Uruguay, Venezuela

### Resto de Oriente Medio {#rest-of-middle-east}

Baréin, Irak, Jordania, Kuwait, Líbano, Omán, Yemen

### Resto de Europa Occidental {#rest-of-western-europe}

Austria, Bélgica, Dinamarca, Finlandia, Irlanda, Noruega, Portugal, Suecia, Suiza

{% alert note %}
Consulta nuestra [documentación de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp) para obtener más información sobre nuestras ofertas de WhatsApp.
{% endalert %}

## Detalles de Agent Console {#agent-console-details}

Las proporciones de créditos de Agent Console se expresan en incrementos de mil (1000) invocaciones realizadas desde la plataforma Braze. Una invocación se registra cuando un agente inicia una llamada a un LLM. De forma predeterminada, tu contrato incluye una asignación de invocaciones según lo especificado por tu edición de plataforma para cada período de tu plazo de suscripción. Las invocaciones adicionales se cobrarán según tu formulario de pedido.

{% alert note %}
Consulta nuestra [documentación de Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) para obtener más información sobre Agent Console.
{% endalert %}

## Detalles adicionales del canal {#additional-channel-details}

### LINE {#line}

Las tasas de crédito de LINE se denominan en incrementos de mensajes LINE enviados desde la plataforma Braze.

{% alert note %}
Consulta nuestra [documentación de LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line) para obtener más información sobre el uso de LINE con Braze.
{% endalert %}

### KakaoTalk {#kakaotalk}

Las tasas de crédito de KakaoTalk se denominan en incrementos de mensajes KakaoTalk enviados desde la plataforma Braze.

{% alert note %}
Consulta nuestra [documentación de KakaoTalk]({{site.baseurl}}/kakaotalk) para obtener más información sobre el uso de KakaoTalk con Braze.
{% endalert %}

### Content Cards {#content-cards}

Las tasas de crédito de Content Cards se denominan en incrementos de mil impresiones únicas diarias.

Braze se reserva el derecho de cobrar créditos por Content Cards en función del número de Content Cards enviadas si el cliente no configura Content Cards para registrar impresiones únicas de acuerdo con las directrices de Braze. Esto se considerará aplicable si, dentro de los seis (6) meses posteriores al primer envío de Content Cards, el cliente ha:
- Enviado más de cinco millones (5 000 000) de Content Cards, Y ADEMÁS
    - Cero (0) impresiones registradas
    - Una proporción de envíos a impresiones únicas diarias superior a cien (100)

{% alert note %}
Consulta nuestra [documentación de Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) para obtener más información sobre Content Cards de Braze.
{% endalert %}

### Banners {#banners}

Las tasas de crédito de Banners se denominan en incrementos de mil impresiones únicas diarias.

{% alert note %}
Consulta nuestra [documentación de Banner]({{site.baseurl}}/developer_guide/banner_cards) para obtener más información sobre Banners de Braze.
{% endalert %}

### Audience Sync {#audience-sync}

Las tasas de crédito de Audience Sync se denominan en incrementos de mil sincronizaciones totales de usuarios. De forma predeterminada, tu contrato incluye cinco millones de sincronizaciones de usuarios por cada periodo de tu plazo de suscripción. Las sincronizaciones de usuarios adicionales se cobrarán según tu formulario de pedido.

{% alert note %}
Consulta nuestra [documentación de Canvas]({{site.baseurl}}/partners/canvas_steps) para obtener más información sobre Canvas Audience Sync y los partners disponibles.
{% endalert %}

### Archivado de mensajes {#message-archiving}

Las tasas de crédito de archivado de mensajes se denominan en incrementos de mil mensajes archivados en los canales push, correo electrónico y SMS/MMS.

{% alert note %}
Consulta nuestra [documentación de archivado de mensajes]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving#message-archiving) para obtener más información sobre el archivado de mensajes.
{% endalert %}

### Webhooks {#webhooks}

Las tasas de crédito de webhooks se denominan en incrementos de mil webhooks enviados correctamente desde la plataforma Braze. De forma predeterminada, tu contrato incluye cien mil webhooks por cada periodo de tu plazo de suscripción. Los webhooks adicionales se cobrarán según tu formulario de pedido.

{% multi_lang_include pricing/webhook_failed_requests_billing.md credit_name='Action Credits' %}

{% alert note %}
Consulta nuestra [documentación de webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) para obtener más información sobre webhooks de Braze.
{% endalert %}