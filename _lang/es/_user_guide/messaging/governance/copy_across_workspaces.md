---
nav_title: Copiar entre espacios de trabajo
article_title: Copiar entre espacios de trabajo
page_order: 3
alias: "/copying_to_workspaces/"
page_type: reference
description: "Este artículo de referencia ofrece un resumen de cómo copiar Campaigns, Canvas y páginas de destino a diferentes espacios de trabajo."
tool:
    - Campaigns
    - Canvas
---

# Copiar Campaigns, Canvas y páginas de destino entre espacios de trabajo {#copy-campaigns-canvases-and-landing-pages-across-workspaces}

> Copiar Campaigns, Canvas y páginas de destino entre espacios de trabajo te permite agilizar la creación de contenido utilizando contenido existente de un espacio de trabajo diferente como punto de partida. Esta página explica cómo copiar Campaigns, Canvas y páginas de destino a diferentes espacios de trabajo y enumera lo que se copia y lo que no.

Cuando copias una Campaign, un Canvas o una página de destino a un espacio de trabajo diferente, la copia permanece como borrador hasta que la edites y lances la Campaign o el Canvas, o publiques la página de destino. Esto te ayuda a conservar y desarrollar tus estrategias de mensajería exitosas.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
La copia de Campaigns entre espacios de trabajo está disponible de forma general. Actualmente no se admite la compatibilidad de canales para Content Cards.
{% endalert %}

Puedes copiar Campaigns entre espacios de trabajo para estos canales compatibles: SMS, mensajes dentro de la aplicación, notificaciones push, correo electrónico y webhooks. También puedes copiar plantillas de correo electrónico, conmutadores de características y Content Blocks. Ten en cuenta que las campañas multicanal con canales no compatibles no se pueden copiar a un espacio de trabajo diferente.

Para copiar una Campaign a un espacio de trabajo diferente:

1. Selecciona el icono de engranaje <i class="fas fa-cog"></i> junto a la Campaign seleccionada.
2. Selecciona **Copiar al espacio de trabajo**.
3. Después de copiar, revisa y prueba tu Campaign para confirmar que todos los campos funcionan correctamente.

{% endtab %}
{% tab canvas %}

{% alert important %}
La copia de Canvas entre espacios de trabajo está disponible de forma general. Actualmente no se admiten los siguientes canales: LINE, Content Cards y WhatsApp.
{% endalert %}

Puedes copiar Canvas entre espacios de trabajo para estos canales compatibles: correo electrónico, mensajes dentro de la aplicación, push, webhooks y SMS.

Para copiar un Canvas a un espacio de trabajo diferente:

1. Selecciona el menú <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;junto al Canvas seleccionado.
2. Selecciona **Copiar al espacio de trabajo**.
3. Después de copiar, revisa y prueba tu Canvas para confirmar que todos los campos funcionan correctamente.

Al copiar un Canvas con pasos de Audience Sync, la configuración no se copia al espacio de trabajo de destino, pero los pasos del recorrido sí.

{% endtab %}
{% tab landing pages %}

Puedes copiar páginas de destino entre espacios de trabajo.

Para copiar una página de destino a un espacio de trabajo diferente:

1. Ve a **Mensajería** > **Páginas de destino**.
2. Selecciona el menú <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;junto a la página de destino seleccionada.
3. Selecciona **Copiar al espacio de trabajo**.
4. Revisa y prueba tu página de destino para confirmar que todos los campos funcionan correctamente.

{% endtab %}
{% endtabs %}

## Qué se copia entre espacios de trabajo {#whats-copied-across-workspaces}

Ten en cuenta que las siguientes tablas cubren campos de Campaigns y Canvas, y no son una lista exhaustiva de lo que se copia entre espacios de trabajo y lo que se omite. Como práctica recomendada, verifica los detalles de la Campaign, el Canvas y la página de destino, y prueba para confirmar que tu mensaje funciona como se espera.

Las páginas de destino se copian como borradores. Antes de publicar una página de destino copiada, revisa la URL de la página, la configuración de dominio personalizado, el manejo de envío de formularios y cualquier referencia de Liquid o específica del espacio de trabajo.

{% alert note %}
Las traducciones no se copian cuando se copian Campaigns de correo electrónico, Canvas o plantillas entre espacios de trabajo. Después de copiar, vuelve a introducir o cargar las traducciones en el espacio de trabajo de destino.
{% endalert %}

### Detalles {#details}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Descripción | Territorios |
| Tipo | Etiquetas |
| Acciones (anidadas) | Segments y filtros |
| Comportamientos de conversión (anidados) | [Aprobaciones]({{site.baseurl}}/user_guide/messaging/governance/approvals) |
| Configuraciones de tiempo en silencio | Planificación de desencadenamiento |
| Configuraciones de limitación de frecuencia | Resúmenes de Campaign |
| Estado de suscripción del destinatario |  |
| Planificación recurrente |  |
| Es transaccional |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalles" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Descripción | Territorios |
| Tipo | Etiquetas |
| Acciones (anidadas) | Segments y filtros |
| Comportamientos de conversión (anidados) | [Aprobaciones]({{site.baseurl}}/user_guide/messaging/governance/approvals) |
| Configuraciones de tiempo en silencio | Planificación de desencadenamiento |
| Configuraciones de limitación de frecuencia | Resúmenes de Canvas |
| Estado de suscripción del destinatario |  |
| Planificación recurrente | Criterios de salida |
| Es transaccional |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalles" }

Los criterios de filtro de los pasos en Canvas (por ejemplo, los pasos de [división de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)) no se copian al espacio de trabajo de destino. Reconfigura esos filtros después de copiar.

{% endtab %}
{% endtabs %}

### Comportamientos de conversión {#conversion-behaviors}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID de espacio de trabajo |
| Interacción con la Campaign | ID de Campaign |
| Nombre de evento personalizado |  |
| Nombre de producto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamientos de conversión" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID de espacio de trabajo |
| Interacción con Canvas | ID de Canvas |
| Nombre de evento personalizado |  |
| Nombre de producto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamientos de conversión" }

{% endtab %}
{% endtabs %}

### Acciones {#actions}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID de espacio de trabajo |
| Interacción con la Campaign | ID de Campaign |
| Nombre de evento personalizado |  |
| Nombre de producto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acciones" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID de espacio de trabajo |
| Interacción con Canvas | ID de Canvas |
| Nombre de evento personalizado |  |
| Nombre de producto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acciones" }

{% endtab %}
{% endtabs %}

### Variaciones de mensaje {#message-variations}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Porcentaje de envío | ID de API |
| Tipo | ID de grupo semilla |
|  | ID de plantilla de enlace |
|  | ID de grupo de usuarios internos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variaciones de mensaje" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Porcentaje de envío | ID de API |
| Tipo | ID de grupo semilla |
|  | ID de plantilla de enlace |
|  | ID de grupo de usuarios internos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variaciones de mensaje" }

{% endtab %}
{% endtabs %}


### Variación de mensaje de correo electrónico {#email-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Cuerpo del correo electrónico | Dirección del remitente |
| Extras del mensaje | Responder a |
| Título | CCO |
| Asunto | Plantilla de enlace |
|  | Aliasing de enlaces |
|  | Traducciones |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variación de mensaje de correo electrónico" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Cuerpo del correo electrónico | Dirección del remitente |
| Extras del mensaje | Responder a |
| Título | CCO |
| Asunto | Plantilla de enlace |
|  | Aliasing de enlaces |
|  | Traducciones |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variación de mensaje de correo electrónico" }

{% endtab %}
{% endtabs %}

### Cuerpo del correo electrónico {#email-body}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Texto plano | Aliasing de enlaces |
| Contenido HTML y de arrastrar y soltar | Traducciones |
| Preencabezado |  |
| CSS en línea |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cuerpo del correo electrónico" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Texto plano | Aliasing de enlaces |
| Contenido HTML y de arrastrar y soltar | Traducciones |
| Preencabezado |  |
| CSS en línea |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cuerpo del correo electrónico" }

{% endtab %}
{% endtabs %}

### Plantillas de correo electrónico {#email-templates}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Cuerpo del correo electrónico | ID de API |
| Descripción | ID de imagen |
| Asunto | Territorios |
| Encabezados | Etiquetas |
| | Traducciones |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de correo electrónico" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Cuerpo del correo electrónico | ID de API |
| Descripción | ID de imagen |
| Asunto | Territorios |
| Encabezados | Etiquetas |
| | Traducciones |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de correo electrónico" }

{% endtab %}
{% endtabs %}

### Content Blocks

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Nombre | Aliasing de enlaces |
| Descripción | Claves de API |
| Contenido | Territorios |
| Contenido HTML y de arrastrar y soltar | Etiquetas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Nombre | Aliasing de enlaces |
| Descripción | Claves de API |
| Contenido | Territorios |
| Contenido HTML y de arrastrar y soltar | Etiquetas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% endtabs %}

### Variación de mensaje SMS {#sms-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Cuerpo | Servicio de mensajería |
| Acortamiento de enlaces | Elementos multimedia VCF |
| Seguimiento de clics |  |
| Elementos multimedia |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variación de mensaje SMS" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Cuerpo | Servicio de mensajería |
| Acortamiento de enlaces | Elementos multimedia VCF |
| Seguimiento de clics |  |
| Elementos multimedia |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variación de mensaje SMS" }

{% endtab %}
{% endtabs %}

## Copiar mensajes que contienen Liquid {#copying-messages-that-contain-liquid}

Las referencias de Liquid dentro de los cuerpos de los mensajes se copian al espacio de trabajo de destino, pero es posible que no funcionen como se espera. Esto significa que si un Canvas del espacio de trabajo A se copia al espacio de trabajo B, el espacio de trabajo B no puede hacer referencia a los detalles del espacio de trabajo A, incluidas las referencias de Liquid. Por ejemplo, campos como las acciones desencadenantes, los filtros de audiencia y los criterios de filtro de [división de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) no se copian.

Ten en cuenta las siguientes referencias de Liquid con dependencias al copiar Campaigns, Canvas y páginas de destino entre espacios de trabajo:

- Etiquetas de elementos de catálogo
- Etiquetas de contenido conectado
- Content Blocks
- Atributos personalizados
- Centros de preferencias
- Recomendaciones de productos
- Etiquetas de estado de suscripción
- Etiquetas de vales y promociones

## Copiar mensajes con conmutadores de características {#copying-messages-with-feature-flags}

Para copiar una Campaign de conmutador de características y un Canvas con un paso de conmutador de características entre espacios de trabajo, asegúrate de que el espacio de trabajo de destino tenga un [experimento de conmutador de características]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurado con un ID que coincida con el conmutador de características referenciado en la Campaign original o el paso de conmutador de características referenciado en el Canvas original.

Si copias una Campaign o un Canvas que tiene un paso de conmutador de características con un ID de conmutador de características que no existe en el espacio de trabajo de destino, el paso de conmutador de características se copiará pero su contenido no.

## Copiar mensajes con Content Blocks {#copying-messages-with-content-blocks}

Cuando copias una Campaign entre espacios de trabajo, los Content Blocks no se copian. Sin embargo, se puede hacer referencia a un Content Block en el espacio de trabajo de destino si existe un bloque con el mismo nombre. Alternativamente, puedes crear el Content Block (o estas referencias de Liquid) en el espacio de trabajo de destino para evitar errores al lanzar una Campaign.

Para los Canvas que hacen referencia a un Content Block, el Content Block debe copiarse primero al espacio de trabajo de destino.