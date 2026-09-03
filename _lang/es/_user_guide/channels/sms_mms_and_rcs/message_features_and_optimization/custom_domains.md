---
nav_title: Dominios personalizados de autoservicio
article_title: Dominios personalizados de autoservicio
page_order: 2
description: "Esta página explica cómo usar dominios personalizados con el acortamiento de enlaces para personalizar la apariencia de tus URL acortadas."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Dominios personalizados de autoservicio {#self-serve-custom-domains}

> Esta página explica cómo configurar tus propios dominios personalizados en el panel de Braze. Los dominios personalizados te permiten usar un enlace acortado con tu marca que refleje la identidad de tu marca en lugar de un enlace acortado genérico o el dominio de Braze (`brz.ai`), lo que mejora la confianza del usuario y la participación en Campaigns a través de enlaces SMS.

Con los dominios personalizados de autoservicio, puedes configurar y administrar tus propios dominios personalizados para SMS, RCS y WhatsApp directamente desde tu panel de Braze. Puedes añadir, supervisar y administrar fácilmente hasta 10 dominios personalizados en un solo lugar.

## Beneficios de los dominios personalizados de autoservicio {#benefits-of-self-serve-custom-domains}

- **Configuración simplificada:** Configura tus dominios en la página **Configuración de la empresa**, reduciendo el tiempo de configuración.
- **Mayor transparencia:** Recibe actualizaciones en tiempo real sobre el estado de configuración de tu dominio a través de banners en el panel.
- **Notificaciones proactivas:** Recibe alertas inmediatas cuando tu dominio personalizado esté conectado o si ocurre algún error de configuración.

## Requisitos de dominio {#domain-requirements}

- Los dominios deben ser adquiridos, propiedad tuya y gestionados por ti. Esto se puede hacer a través de un registrador de dominios, como GoDaddy, Amazon Route 53 o Cloudflare.
- El dominio utilizado para esta característica debe ser:
  - Único (diferente de tu dominio de sitio web)
  - No se puede utilizar para alojar ningún contenido web
    - También puedes usar subdominios únicos. Por ejemplo, el dominio `braze.com` podría tener subdominios como `sms.braze.com` o `whatsapp.braze.com`.

## Delegación de tu dominio personalizado {#delegating-your-custom-domain}

Necesitamos que delegues tu dominio personalizado a Braze para que podamos facilitar el enrutamiento adecuado y la compatibilidad de infraestructura con nuestros servicios de acortamiento de enlaces y seguimiento de clics. Cuando delegas tu dominio a Braze, gestionamos automáticamente la renovación del certificado para evitar una interrupción en el servicio.

{% alert important %}
Si tus registros de DNS no se actualizan en un plazo de 45 días, el token de configuración caduca. Reinicia la configuración del dominio desde **Dominios de SMS/RCS y aplicaciones de mensajería** para generar nuevos registros de DNS.
{% endalert %}

## Añadir un dominio personalizado {#adding-a-custom-domain}

1. En Braze, ve a **Configuración de la empresa** > **Dominios de SMS/RCS y aplicaciones de mensajería**.
![Página "Dominios de SMS/RCS y aplicaciones de mensajería" con varios dominios listados.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2. Selecciona **Añadir dominio** para iniciar la configuración de un nuevo dominio personalizado.
3. Introduce el dominio personalizado que hayas adquirido en el campo de entrada de la aplicación, que utiliza nuestra lógica de validación existente para el formato correcto, y luego selecciona **Siguiente** y **Enviar**.

![Botón "Añadir dominio" en la página "Dominios de SMS/RCS y aplicaciones de mensajería".]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4. Pide a tu equipo técnico (como ingeniería o TI) que actualice la configuración de DNS con los detalles del registro de DNS de Cloudflare que se muestran. Tu equipo técnico debe actualizar tus registros de DNS con estos detalles en un plazo de 45 días.
  - Si necesitas más tiempo para actualizar tus registros de DNS, puedes reiniciar el proceso y generar un nuevo conjunto de registros de DNS para tu dominio.

Braze consulta tu configuración de DNS aproximadamente cada 30 minutos para comprobar si hay actualizaciones.

![Sección "Registro de DNS" con 3 pasos a completar para terminar de configurar tu dominio.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
El progreso de tu dominio se guarda automáticamente. Si necesitas salir a mitad del proceso, puedes retomarlo más tarde seleccionando la entrada del dominio pendiente en la página **Dominios de SMS/RCS y aplicaciones de mensajería**.
{% endalert %}

### Gestión y uso continuos {#ongoing-management-and-usage}

Una vez verificado tu dominio, tus dominios personalizados aparecerán en la tabla de la página **Dominios de SMS/RCS y aplicaciones de mensajería** con indicadores de estado. Puedes usar inmediatamente los dominios conectados en múltiples grupos de suscripción, espacios de trabajo y a través de los canales SMS, RCS y WhatsApp.

![Lista de dominios personalizados y estados.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

La monitorización en vivo te alerta en el panel de Braze si alguno de tus dominios activos tiene un problema, para que tus enlaces personalizados sigan siendo utilizables. Si encuentras algún problema, consulta los detalles del error en la aplicación o contacta con el [soporte]({{site.baseurl}}/braze_support) de Braze para obtener ayuda.

## Asignación de dominios personalizados a grupos de suscripción {#assigning-custom-domains-to-subscription-groups}

Una vez configurados, los dominios personalizados pueden asignarse a uno o varios grupos de suscripción de SMS, RCS y WhatsApp.

1. Ve a **Audiencia** > **Gestión de grupos de suscripción**.
2. Busca y selecciona tu grupo de suscripción en la lista.
3. En **Detalles del grupo de suscripción**, selecciona tu dominio personalizado en el desplegable **Dominio de acortamiento de enlaces**.

Las Campaigns enviadas con el acortamiento de enlaces activado utilizan el dominio asignado asociado a tu grupo de suscripción de SMS, RCS o WhatsApp.

![Vista previa del creador de mensajes SMS con un dominio de enlace acortado que es diferente del dominio en el cuadro "Mensaje".]({% image_buster /assets/img/custom_domain2.png %})

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Se pueden compartir dominios delegados entre varios grupos de suscripción? {#can-delegated-domains-be-shared-across-multiple-subscription-groups}

Sí. Un solo dominio se puede utilizar con varios grupos de suscripción. Para ello, selecciona el dominio para cada grupo de suscripción con el que deba estar asociado.

### ¿Se pueden compartir dominios delegados entre varios espacios de trabajo? {#can-delegated-domains-be-shared-across-multiple-workspaces}

Sí. Los dominios se pueden asociar con grupos de suscripción en varios espacios de trabajo, siempre que los espacios de trabajo estén contenidos dentro de la misma empresa.

### ¿Cuántos dominios personalizados puedo añadir? {#how-many-custom-domains-can-i-add}

Puedes añadir hasta 10 dominios personalizados por panel. Braze puede configurar un límite superior para tu empresa previa solicitud.

Los dominios en estado **Pendiente** o **Error** cuentan para este límite. Elimínalos o resuelve el error en la página **SMS/RCS and Messaging Apps Domains**.

No puedes eliminar un dominio que esté asignado como **Link Shortening Domain** en un grupo de suscripción. Primero reasigna el dominio en cada grupo de suscripción y luego elimina el dominio.

### ¿Qué sucede si no actualizo mis registros de DNS en un plazo de 45 días? {#what-happens-if-i-dont-update-my-dns-records-within-45-days}

Aunque los detalles de tu registro de DNS de Cloudflare caducarán después de 45 días, puedes reiniciar el proceso de configuración con el mismo dominio y Braze generará un nuevo conjunto de registros de DNS para ampliar tu ventana de configuración.

### ¿Se me notifica si hay un error durante el proceso de actualización de DNS? {#am-i-notified-if-there-is-an-error-during-the-dns-update-process}

Sí. Si hay un error, recibirás un banner en el panel de Braze con los detalles del problema junto con los pasos para resolverlo.

### ¿Puedo usar un dominio personalizado en varios canales? {#can-i-use-a-custom-domain-across-multiple-channels}

Sí. Una vez verificado un dominio personalizado, se puede utilizar en todos los grupos de suscripción de SMS, RCS y WhatsApp en todos los espacios de trabajo dentro de un panel.

### ¿Qué pasa si tengo preguntas o necesito más ayuda? {#what-if-i-have-questions-or-need-further-support}

Para obtener orientación más detallada sobre la configuración y gestión de dominios personalizados, incluidos los pasos de solución de problemas y los requisitos técnicos, [contacta con soporte]({{site.baseurl}}/braze_support).