---
nav_title: Centro de entrega
article_title: Centro de entrega
alias: "/deliverability_center/"
page_order: 4
description: "Este artículo de referencia explica cómo configurar el Centro de entrega, una característica que permite a los especialistas en marketing ver la reputación de sus dominios de envío de correo electrónico y sus IP, y comprender su capacidad de entrega de correo electrónico."
channel:
  - email

---

# Centro de entrega {#deliverability-center}

> El Centro de entrega proporciona más información sobre el rendimiento de tu correo electrónico al admitir el uso de [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) para rastrear datos sobre los correos electrónicos enviados y recopilar datos sobre tu dominio de envío.

La capacidad de entrega del correo electrónico es el núcleo del éxito de una campaña. Usando el Centro de entrega en el dashboard de Braze, puedes ver tus dominios por **IP Reputation** o **Delivery Errors** para descubrir y solucionar cualquier problema potencial con la capacidad de entrega del correo electrónico.

Para acceder al Centro de entrega, necesitas los [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) del siguiente desplegable para tu espacio de trabajo.

{% details Permisos de usuario para el Centro de entrega %}

- Ver Campaigns
- Editar Campaigns
- Archivar Campaigns
- Ver Canvas
- Editar Canvas
- Archivar Canvas
- Ver reglas de limitación de frecuencia
- Editar reglas de limitación de frecuencia
- Ver priorización de mensajes
- Editar priorización de mensajes
- Ver Content Blocks
- Ver conmutadores de características
- Editar conmutadores de características
- Archivar conmutadores de características
- Ver Segments
- Editar Segments
- Ver plantillas de IAM
- Editar plantillas de IAM
- Archivar plantillas de IAM
- Ver plantillas de correo electrónico
- Editar plantillas de correo electrónico
- Archivar plantillas de correo electrónico
- Ver plantillas de Webhook
- Editar plantillas de Webhook
- Archivar plantillas de Webhook
- Ver plantillas de enlaces de correo electrónico
- Editar plantillas de enlaces de correo electrónico
- Ver activos de la Biblioteca de medios
- Editar activos de la Biblioteca de medios
- Eliminar activos de la Biblioteca de medios
- Ver ubicaciones
- Editar ubicaciones
- Archivar ubicaciones
- Ver códigos promocionales
- Editar códigos promocionales
- Exportar códigos promocionales
- Ver centros de preferencias
- Editar centros de preferencias
- Ver informes
- Editar informes
- Ver datos de uso

{% enddetails %}

## Configura tu cuenta de Google Postmaster {#set-up-your-google-postmaster-account}

Antes de conectarte al Centro de entrega, necesitarás configurar una cuenta de Google Postmaster Tools. Puedes usar una cuenta de Gmail personal o de trabajo para configurar tu Google Postmaster.

1. Ve al [panel de Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. En la esquina inferior derecha, selecciona <i class="fas fa-plus-circle"></i> **Add domain**.
3. Introduce tu dominio raíz (principal) para autenticar tu correo electrónico. Asegúrate de que el registro TXT esté vinculado a este dominio raíz (principal), **no** al subdominio que estás usando a través de Braze. Verificar el dominio raíz (principal) te permite agregar subdominios posteriormente en Postmaster Tools sin crear registros TXT adicionales. Por ejemplo, al verificar `braze.com`, puedes agregar después `demo.braze.com` como un subdominio separado en Postmaster Tools para ver métricas a nivel de subdominio.
4. Google genera un registro TXT que se puede agregar directamente al DNS de tu dominio. Esto generalmente lo gestiona quien administra tu DNS. Para obtener información y orientación sobre cómo actualizar tu DNS específico, consulta [Verificar tu dominio (pasos específicos del host)](https://support.google.com/a/topic/1409901).
5. Selecciona **Next**. <br>![Un ejemplo de dominio "demo.braze.com" para autenticar un correo electrónico.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Después de agregar el registro TXT al DNS, vuelve al panel de Google Postmaster Tools y selecciona **Verify**. Este paso confirma que eres el propietario del dominio, para que puedas acceder a las métricas de capacidad de entrega de Gmail en tu cuenta de Postmaster. <br>![Un mensaje para verificar la propiedad del dominio "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})
7. Después de verificar el dominio raíz (principal), agrega tus subdominios de envío a Google Postmaster.

{% alert note %}
Si tus subdominios no aparecen en el Centro de entrega de Google Postmaster, esto puede deberse a que solo se agregó el dominio raíz (principal) a Google Postmaster. Después de verificar los dominios raíz en Google Postmaster, puedes agregar tus subdominios, que se verifican automáticamente. Este proceso permite que Google informe sobre métricas a nivel de subdominio, que luego se pueden importar al Centro de entrega de Braze.
{% endalert %}

## Integrar Google Postmaster {#integrating-google-postmaster}

Antes de configurar tu Centro de entrega, verifica que tus dominios se hayan [agregado a Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

Sigue estos pasos para integrar con Google Postmaster y configurar tu Centro de entrega:

1. Ve a **Analytics** > **Email Performance**.
2. Selecciona la pestaña **Deliverability Center**. <br>![Un Centro de entrega con Google Postmaster sin conectar.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Selecciona **Connect with Google Postmaster**.
4. Selecciona tu cuenta de Google y luego selecciona **Allow** para que Braze pueda ver las métricas de tráfico de correo electrónico de los dominios registrados en Postmaster Tools.

Tus dominios verificados se muestran en el Centro de entrega.

![Dos dominios verificados para Google Postmaster con una reputación media y baja.]({% image_buster /assets/img_archive/deliverability_center2.png %})

También puedes acceder a Google Postmaster en el dashboard de Braze yendo a **Integraciones de socios** > **Socios tecnológicos** > **Google Postmaster**. Después de la integración, Braze obtiene datos de reputación y errores de los últimos 30 días. Es posible que los datos no estén disponibles de inmediato y podrían tardar varios minutos en cargarse.

### Autorización no válida o expirada {#invalid-or-expired-authorization}

Si recibes una alerta de que las credenciales de autorización de Google Postmaster Tools no son válidas, el envío de correo electrónico desde Braze **no** se ve afectado. Solo se interrumpe la conexión entre Braze y Google Postmaster, lo que detiene la sincronización de datos de reputación y errores de Gmail con el Centro de entrega hasta que te reconectes.

Para restaurar la integración, ve a **Integraciones de socios** > **Socios tecnológicos**, abre **Google Postmaster**, selecciona **Disconnect** y luego sigue el flujo de conexión nuevamente (los mismos pasos que en [Integrar Google Postmaster](#integrating-google-postmaster)).

### Métricas y definiciones {#metrics-and-definitions}

Las siguientes métricas y definiciones se aplican a Google Postmaster Tools.

#### Reputación de IP {#ip-reputation}

Para ayudarte a comprender las calificaciones de reputación de IP, consulta esta tabla:

| Calificación de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de generar pocas quejas de correo no deseado (como usuarios que hacen clic en el botón "spam"). |
| Media/Aceptable | Conocido por generar interacción positiva, pero ocasionalmente recibe quejas de correo no deseado. La mayoría de los correos electrónicos de este dominio se envían al buzón de entrada, excepto cuando aumentan las quejas de correo no deseado. |
| Baja | Conocido por recibir tasas elevadas de quejas de correo no deseado regularmente. Es probable que los correos electrónicos de este remitente se filtren a la carpeta de correo no deseado. |
| Mala | Tiene un historial de recibir tasas elevadas de quejas de correo no deseado. Los correos electrónicos de este dominio casi siempre se rechazan en el momento de la conexión o se filtran a la carpeta de correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reputación de IP" }

#### Reputación de dominio {#domain-reputation}

Usa la siguiente tabla para ayudarte a monitorear y comprender las calificaciones de reputación de tu dominio y evitar que tus correos se filtren a la carpeta de correo no deseado.

| Calificación de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de muy pocas quejas de correo no deseado. Cumple con las directrices de remitente de Gmail. Los correos electrónicos rara vez se filtran a la carpeta de correo no deseado. Tiene un buen historial de una tasa de correo no deseado muy baja. Cumple con las [directrices de remitente de Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Media/Aceptable | Conocido por generar interacción positiva, pero ocasionalmente ha recibido un bajo volumen de quejas de correo no deseado. La mayoría de los correos electrónicos de este dominio llegan al buzón de entrada (excepto cuando hay un aumento notable en los niveles de correo no deseado). |
| Baja | Conocido por recibir quejas de correo no deseado regularmente. Es probable que los correos electrónicos de este remitente se filtren a la carpeta de correo no deseado. |
| Mala | Tiene un historial de recibir tasas elevadas de quejas de correo no deseado. Los correos electrónicos de este dominio casi siempre se rechazan en el momento de la conexión o se filtran a la carpeta de correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reputación de dominio" }

#### Autenticación {#authentication}

Usa el panel de autenticación para revisar el porcentaje de correos electrónicos que han pasado Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) y Domain-based Message Authentication, Reporting and Conformance (DMARC).

| Tipo de gráfico | Definición |
| ----- | ---------- |
| SPF | Muestra el porcentaje de correos electrónicos que pasaron SPF en comparación con todos los correos electrónicos del dominio que intentaron SPF. Esto excluye cualquier correo falsificado. |
| DKIM | Muestra el porcentaje de correos electrónicos que pasaron DKIM en comparación con todos los correos electrónicos del dominio que intentaron DKIM. |
| DMARC | Muestra el porcentaje de correos electrónicos que pasaron la alineación DMARC en comparación con todos los correos electrónicos recibidos del dominio que pasaron SPF o DKIM. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autenticación" }

#### Cifrado {#encryption}

Consulta esta tabla para comprender qué porcentaje de tu tráfico de entrada y salida está cifrado.

| Término | Definición |
| ----- | ---------- |
| TLS de entrada | Muestra el porcentaje de correo entrante (a Gmail) que pasó TLS en comparación con todo el correo recibido de ese dominio. |
| TLS de salida | Muestra el porcentaje de correo saliente (de Gmail) aceptado a través de TLS en comparación con todo el correo enviado a ese dominio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cifrado" }

Para más ideas sobre cómo mejorar la capacidad de entrega, lee [Problemas de capacidad de entrega y trampas de correo no deseado]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Asegúrate de consultar nuestras [Mejores prácticas de correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/) para conocer lo que debes verificar antes de enviar una campaña de correo electrónico.

## Configurar Microsoft Smart Network Data Services (SNDS) {#set-up-microsoft-smart-network-data-services-snds}

Si Microsoft es tu proveedor principal de buzón de entrada, puedes usar esta integración para acceder y ver tus datos de reputación de Microsoft. De esta manera, puedes monitorear el estado de tus IP para ayudar a determinar cómo se están recibiendo tus correos electrónicos.

{% alert important %}
Si no ves tus datos en el Centro de entrega, ponte en contacto con [Soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support/) con una lista de tus direcciones IP.
{% endalert %}

![Un ejemplo de resultados de Microsoft SNDS, incluyendo IP de muestra, destinatarios, comandos RCPT, comandos DATA, resultado del filtro, tasa de quejas, período de inicio y fin de mensajes trampa e impactos de trampas de correo no deseado.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Métricas y definiciones

Las siguientes métricas se aplican a Microsoft SNDS.

#### Destinatarios {#recipients}

Esta métrica se refiere al número de destinatarios en los mensajes transmitidos por la IP.

#### Comandos DATA {#data-commands}

Esta métrica rastrea el número de comandos DATA enviados por la IP. Los comandos DATA son parte del protocolo SMTP utilizado para enviar correo.

#### Resultados del filtro {#filter-results}

Consulta esta tabla para comprender los resultados del filtro.

| Resultado | Definición |
| ----- | ---------- |
| Verde | Considerado correo no deseado por el filtro de correo no deseado de Microsoft hasta el 10% del período de tiempo dado. |
| Amarillo | Considerado correo no deseado por el filtro de correo no deseado de Microsoft entre el 10% y el 90% del período de tiempo dado. |
| Rojo | Considerado correo no deseado por el filtro de correo no deseado de Microsoft más del 90% del período de tiempo dado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Resultados del filtro" }

#### Tasa de quejas {#complaint-rate}

Esta es la fracción de tiempo en que un mensaje recibido desde la IP es reportado como queja por un usuario de Hotmail o Windows Live durante el período de actividad. Los usuarios tienen la opción de reportar casi todos los mensajes como correo no deseado a través de la interfaz web de usuario.

Para calcular la tasa de quejas, divide el número de quejas entre el número de destinatarios del mensaje.

| Resultado | Definición |
| ----- | ---------- |
| Menos del 0.3% | La tasa de quejas ideal. |
| Más del 0.3% | Revisa tu proceso de registro y asegúrate de que tu enlace para cancelar suscripción funcione. También considera si el correo podría personalizarse mejor para tu audiencia. |
| Más del 100% | Ten en cuenta que SNDS muestra las quejas del día en que se reportaron, no retroactivamente contra el día en que se entregó el correo que generó la queja. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tasa de quejas" }

#### Impactos de trampas de correo no deseado {#spam-trap-hits}

Los impactos de trampas de correo no deseado son el número de mensajes enviados a "cuentas trampa", que son cuentas mantenidas por Outlook.com que no solicitan ningún correo. Es probable que cualquier mensaje enviado a estas cuentas trampa se considere correo no deseado, por lo que es importante monitorear esta métrica para asegurarte de que sea baja. Un número bajo de impactos de trampas de correo no deseado significa que los mensajes no se envían a estas cuentas y se están enviando a cuentas reales.

{% alert tip %}
Si estás buscando registros relacionados con uno de tus dominios verificados en Braze, ten en cuenta que el Centro de entrega muestra tus datos de Google Postmaster o Microsoft SNDS, lo que significa que es probable que alguna de las plataformas no tenga datos para compartir con Braze. Alternativamente, intenta mantener un envío de correo electrónico consistente, ya que esto puede llevar a una reputación más alta.
{% endalert %}