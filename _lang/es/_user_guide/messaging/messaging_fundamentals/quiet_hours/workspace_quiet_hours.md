---
nav_title: Horas tranquilas del espacio de trabajo
article_title: Horas tranquilas del espacio de trabajo
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre las horas tranquilas del espacio de trabajo, cómo Braze gestiona los mensajes durante el periodo de silencio y cómo interactúan las horas tranquilas con la sincronización inteligente."
---

# Horas tranquilas del espacio de trabajo {#workspace-quiet-hours}

> Las horas tranquilas del espacio de trabajo te permiten establecer una ventana de horas tranquilas predeterminada para un canal de mensajería en todo tu espacio de trabajo. Cada Campaign y Canvas que envía en ese canal respeta automáticamente la ventana, por lo que no necesitas configurar las horas tranquilas en cada Campaign o Canvas de forma individual.

Las horas tranquilas del espacio de trabajo son independientes de las horas tranquilas a nivel de Campaign y Canvas, que siguen aplicándose cuando las configuras. Usa las horas tranquilas del espacio de trabajo para el caso predeterminado (por ejemplo, un requisito de cumplimiento en todos los envíos de SMS). Mantén las horas tranquilas a nivel de Campaign y Canvas para las excepciones.

{% alert important %}
Las horas tranquilas del espacio de trabajo están actualmente disponibles en acceso anticipado. Las opciones de configuración pueden cambiar antes de la disponibilidad general. Contacta a tu equipo de cuenta de Braze para solicitar acceso.
{% endalert %}

## Cómo funciona {#how-it-works}

- **Una ventana por canal:** Cada canal admite una única ventana de horas tranquilas del espacio de trabajo, definida por una hora de inicio y una hora de fin.
- **Zona horaria local:** Al igual que las horas tranquilas a nivel de Campaign y Canvas, las horas tranquilas del espacio de trabajo se aplican en la zona horaria local de cada destinatario, no en la zona horaria de tu empresa.
- **Retenido para entrega posterior:** Un mensaje que de otro modo se enviaría durante la ventana se retiene y se entrega más tarde, o se cancela, según el tipo de Campaign. Consulta [Qué sucede con un mensaje retenido](#what-happens-to-a-held-message). Las horas tranquilas nunca modifican el contenido del mensaje. Solo afectan la sincronización.
- **Duración máxima de la ventana:** Una ventana de horas tranquilas no puede superar las 20 horas. Este límite existe para evitar pausar accidentalmente todos los envíos en un canal (por ejemplo, configurando la hora de inicio y la hora de fin con el mismo valor).

### Canales compatibles {#supported-channels}

Puedes configurar una ventana de horas tranquilas del espacio de trabajo para cualquiera de los siguientes canales:

- Content Cards
- Correo electrónico
- KakaoTalk
- LINE
- Push
   - Esto cubre todas las plataformas push en tu espacio de trabajo. No hay opción para configurar horas tranquilas diferentes para plataformas individuales (por ejemplo, iOS frente a Android).
- SMS/MMS/RCS
- Webhook
- WhatsApp

## Requisitos previos {#prerequisites}

Para crear o actualizar las horas tranquilas del espacio de trabajo, necesitas el permiso "Editar horas tranquilas".

| Permiso | Acceso |
|---|---|
| Editar horas tranquilas | Crear y actualizar las horas tranquilas del espacio de trabajo. |
| Ver horas tranquilas | Ver la configuración de horas tranquilas del espacio de trabajo sin editarla. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permisos de horas tranquilas" }

Los permisos existentes de edición de Campaigns y Canvas no se ven afectados. Los usuarios con esos permisos aún pueden editar las horas tranquilas a nivel de Campaign o Canvas.

## Configurar las horas tranquilas del espacio de trabajo {#set-up-workspace-quiet-hours}

### Configurar la ventana del espacio de trabajo {#configure-the-workspace-window}

1. Ve a **Configuración** > **Horas tranquilas**.
2. Selecciona **Agregar horas tranquilas**.
3. Selecciona un canal y luego ingresa una hora de inicio y una hora de fin. Un canal puede tener como máximo una ventana de horas tranquilas del espacio de trabajo a la vez.
4. (Opcional) Para agregar otro canal, selecciona **Agregar horas tranquilas** de nuevo.
5. Guarda tus cambios.

![La página de configuración de horas tranquilas del espacio de trabajo con ventanas de horas tranquilas para SMS y correo electrónico, cada una con una hora de inicio y una hora de fin, y una opción de agregar horas tranquilas.]({% image_buster /assets/img/quiet_hours/workspace_quiet_hours_settings.png %}){: style="max-width:90%;"}

Las actualizaciones de las horas tranquilas del espacio de trabajo se registran en un registro de cambios, incluyendo quién realizó el cambio y cuándo, ya que esta configuración afecta a cada Campaign y Canvas en el canal.

### Aplicar o anular en una Campaign o Canvas {#apply-or-override-in-a-campaign-or-canvas}

Después de guardar, la ventana de horas tranquilas del espacio de trabajo aparece en el editor de Campaigns y Canvas para cada canal que tenga una ventana. Puedes mantener el valor predeterminado del espacio de trabajo, o desactivarlo y aplicar una ventana específica de la Campaign o Canvas en su lugar, de la misma manera en que te excluyes de una limitación de frecuencia a nivel de espacio de trabajo.

1. Selecciona **Enforce quiet hours for this campaign** (o el equivalente de Canvas).
2. Selecciona **Use workspace quiet hours** para aplicar el valor predeterminado del espacio de trabajo, o selecciona **Use custom quiet hours** para establecer una ventana específica de la Campaign o Canvas.
3. Para revisar la ventana del espacio de trabajo para los canales en uso, selecciona **View quiet hours**.

![La sección de horas tranquilas de una Campaign con la opción Enforce quiet hours for this campaign seleccionada, Use workspace quiet hours seleccionado y la ventana del espacio de trabajo de correo electrónico de 8:00 PM a 8:00 AM expandida.]({% image_buster /assets/img/quiet_hours/campaign_workspace_quiet_hours.png %}){: style="max-width:70%;"}

## Precedencia: horas tranquilas del espacio de trabajo frente a las de Campaign o Canvas {#precedence-workspace-versus-campaign-or-canvas-quiet-hours}

Para cualquier Campaign o Canvas dado, solo una configuración de horas tranquilas está activa a la vez (horas tranquilas del espacio de trabajo, una ventana específica de Campaign o Canvas, o ninguna). Una ventana de horas tranquilas a nivel de Campaign o Canvas siempre tiene precedencia sobre la configuración predeterminada del espacio de trabajo.

La forma en que se aplican las horas tranquilas también depende de cuándo se creó la Campaign o el Canvas:

- **Campaigns y Canvas existentes** (creados antes de activar las horas tranquilas del espacio de trabajo): si la Campaign o el Canvas no tiene su propia ventana de horas tranquilas, la ventana de horas tranquilas del espacio de trabajo para ese canal se aplica automáticamente. Si ya tiene una ventana a nivel de Campaign o Canvas, esa ventana sigue aplicándose.
- **Nuevas Campaigns y Canvas:** cuando creas una Campaign o un Canvas, puedes usar las horas tranquilas predeterminadas del espacio de trabajo, establecer una ventana personalizada a nivel de Campaign o Canvas, o desactivar las horas tranquilas por completo.

| Configuración presente | Qué horas tranquilas se aplican |
|---|---|
| La Campaign o el Canvas tiene su propia ventana de horas tranquilas | Se aplica la ventana a nivel de Campaign o Canvas. Las horas tranquilas del espacio de trabajo se ignoran para esa Campaign o Canvas. |
| La Campaign o el Canvas no tiene su propia ventana de horas tranquilas, y existe una ventana de horas tranquilas del espacio de trabajo para el canal que utiliza | La ventana de horas tranquilas del espacio de trabajo se aplica automáticamente. Esto incluye Campaigns y Canvas existentes que nunca configuraron horas tranquilas. |
| La Campaign o el Canvas tiene las horas tranquilas desactivadas | No se aplican horas tranquilas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Precedencia de horas tranquilas" }

### Qué sucede con un mensaje retenido {#what-happens-to-a-held-message}

Lo que sucede con un mensaje que cae dentro de una ventana de horas tranquilas depende del tipo de entrega de la Campaign o el Canvas:

- **Campaigns y Canvas basados en acciones:** la alternativa puede ser **Cancelar mensaje** o **Enviar en el próximo horario disponible**, las mismas opciones que las horas tranquilas a nivel de Campaign y Canvas.
- **Campaigns programadas con una hora de envío fija:** la alternativa es **Cancelar mensaje**. Braze no retrasa un envío a hora fija hasta el siguiente horario disponible, ya que eso podría concentrar un gran volumen de mensajes en una ventana de envío comprimida una vez que terminen las horas tranquilas.
- **Campaigns que usan sincronización inteligente:** no se necesita una alternativa separada. Braze ya tiene en cuenta la ventana de horas tranquilas del espacio de trabajo en el momento óptimo de envío que calcula para cada usuario, por lo que los mensajes no se programan dentro de la ventana en primer lugar.
- **Campaigns activadas por API y Campaigns de API:** la alternativa es **Cancelar mensaje** de forma predeterminada.

### Campaigns activadas por API y Campaigns de API {#api-triggered-and-api-campaigns}

Las horas tranquilas funcionan de manera diferente para las Campaigns activadas por API y las Campaigns de API.

#### Campaigns activadas por API {#api-triggered-campaigns}

Las Campaigns activadas por API siguen las mismas opciones de horas tranquilas que otras Campaigns en el panel. Puedes usar las horas tranquilas predeterminadas del espacio de trabajo, establecer una ventana personalizada a nivel de Campaign o desactivar las horas tranquilas en la configuración de la Campaign. No existe un parámetro de API `ignore_workspace_quiet_hours` para los envíos activados por API.

Para envíos programados activados por API que usan `at_optimal_time`, las horas tranquilas del espacio de trabajo ya se tienen en cuenta en el momento óptimo de envío, de manera similar a la [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

#### Campaigns de API {#api-campaigns}

Las Campaigns de API no pueden usar horas tranquilas a nivel de Campaign. Solo se aplica la ventana de horas tranquilas del espacio de trabajo. Para enviar durante esa ventana, incluye el parámetro opcional `ignore_workspace_quiet_hours` en tu solicitud de API.

### Exclusiones {#exclusions}

Los siguientes elementos nunca son retenidos por las horas tranquilas del espacio de trabajo, independientemente del canal:

- Mensajes de correo transaccional
- Respuestas automáticas de SMS (por ejemplo, respuestas a las palabras clave `STOP` o `HELP`)
- Envíos de prueba y envíos de grupo semilla

## Otras consideraciones {#other-considerations}

- **Envíos programados en la hora de la empresa:** Las horas tranquilas del espacio de trabajo se basan en la zona horaria local de cada destinatario, pero la hora de envío de una Campaign programada puede estar configurada en la zona horaria de tu empresa. Esa diferencia significa que una hora de envío que parece correcta en la hora de la empresa podría caer dentro de las horas tranquilas para algunos destinatarios. Revisa los detalles de las horas tranquilas del espacio de trabajo que se muestran en el editor de la Campaign antes de enviar.
- **Entrega después de que terminan las horas tranquilas:** Si una audiencia grande fue retenida durante la ventana, esos mensajes pueden volverse elegibles para enviarse todos a la vez cuando la ventana se cierra. Planifica para esto cuando un canal tiene una audiencia amplia y una ventana de horas tranquilas prolongada.
- **Independiente de la limitación de frecuencia y los límites de velocidad:** Las horas tranquilas del espacio de trabajo se aplican de forma independiente de la limitación de frecuencia y los límites de velocidad. Un mensaje que supera esos controles aún puede ser retenido por las horas tranquilas, y un mensaje retenido por las horas tranquilas sigue siendo evaluado contra los límites de velocidad una vez que está listo para enviarse.
- **La sincronización inteligente anula las horas tranquilas del espacio de trabajo para Campaigns multicanal basadas en acciones. Para limitar las horas de envío, configura horas tranquilas personalizadas en su lugar.

## Configuración relacionada {#related-settings}

- [Horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours): La versión existente de esta característica, por Campaign y por Canvas. Las horas tranquilas del espacio de trabajo no la reemplazan; establecen el valor predeterminado que se aplica cuando un Campaign o Canvas no configura su propia ventana.
- [Sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing): Calcula un horario de envío óptimo por usuario. Cuando se habilita junto con las horas tranquilas del espacio de trabajo, estas se tienen en cuenta en ese cálculo.
- [Límites de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Controles de entrega independientes que se aplican de forma independiente de las horas tranquilas.