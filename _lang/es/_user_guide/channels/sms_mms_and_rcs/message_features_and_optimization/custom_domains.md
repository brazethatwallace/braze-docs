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

> Esta página explica cómo configurar tus propios dominios personalizados en el panel de Braze. Los dominios personalizados te permiten usar un enlace acortado con tu marca que refleje la identidad de tu marca en lugar de un enlace acortado genérico o el dominio de Braze (`brz.ai`), lo que mejora la confianza del usuario y la interacción con las campañas a través de enlaces SMS.

Los dominios personalizados de autoservicio te permiten configurar y administrar tus propios dominios personalizados para SMS, RCS y WhatsApp directamente desde tu panel de Braze. Puedes añadir, supervisar y administrar fácilmente hasta 10 dominios personalizados en un solo lugar.

## Ventajas de los dominios personalizados de autoservicio {#benefits-of-self-serve-custom-domains}

- **Configuración simplificada:** Configura tus dominios en la página **Configuración de empresa**, reduciendo el tiempo de configuración.
- **Mayor transparencia:** Recibe actualizaciones en tiempo real sobre el estado de configuración de tu dominio a través de banners en el dashboard.
- **Notificaciones proactivas:** Recibe alertas inmediatas cuando tu dominio personalizado esté conectado o si se produce algún error de configuración.

## Requisitos de dominio {#domain-requirements}

- Los dominios deben ser adquiridos, poseídos y administrados por ti. Esto se puede hacer a través de un registrador de dominios, como GoDaddy, Amazon Route 53 o Google Domains.
- El dominio utilizado para esta característica debe ser:
  - Único (diferente de tu dominio de sitio web)
  - No puede usarse para alojar ningún contenido web
    - También puedes usar subdominios únicos. Por ejemplo, el dominio `braze.com` podría tener subdominios como `sms.braze.com` o `whatsapp.braze.com`.

## Delegar tu dominio personalizado {#delegating-your-custom-domain}

Requerimos que delegues tu dominio personalizado a Braze para que podamos facilitar el enrutamiento adecuado y la compatibilidad de infraestructura con nuestros servicios de acortamiento de enlaces y seguimiento de clics. Cuando delegas tu dominio a Braze, gestionamos automáticamente la renovación del certificado para evitar una interrupción en el servicio.

## Añadir un dominio personalizado {#adding-a-custom-domain}

1. En Braze, ve a **Configuración de empresa** > **SMS/RCS and Messaging Apps Domains**.
![Página "SMS/RCS and Messaging Apps Domains" con varios dominios listados.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2. Selecciona **Add Domain** para iniciar la configuración de un nuevo dominio personalizado.
3. Introduce el dominio personalizado que has adquirido en nuestro campo de entrada dentro de la aplicación, que utiliza nuestra lógica de validación existente para el formato correcto, luego selecciona **Next** y **Submit**.

![Botón "Add Domain" en la página "SMS/RCS and Messaging Apps Domains".]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4. Haz que tu equipo técnico (como ingeniería o TI) actualice tu configuración de DNS con los detalles del registro de DNS de Cloudflare que se muestran. Tu equipo técnico debe actualizar tus registros de DNS con estos detalles en un plazo de 45 días.
  - Si necesitas tiempo adicional para actualizar tus registros de DNS, puedes reiniciar el proceso y generar un nuevo conjunto de registros de DNS para tu dominio.

Braze consultará tu configuración de DNS aproximadamente cada 30 minutos para comprobar si hay actualizaciones.

![Sección "Registro de DNS" con 3 pasos a completar para terminar de configurar tu dominio.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
El progreso de tu dominio se guarda automáticamente. Si necesitas salir a mitad del proceso, puedes retomarlo más tarde seleccionando la entrada de dominio pendiente en la página **SMS/RCS and Messaging Apps Domains**.
{% endalert %}

### Administración y uso continuos {#ongoing-management-and-usage}

Una vez verificado tu dominio, tus dominios personalizados aparecerán en la tabla de la página **SMS/RCS and Messaging Apps Domains** con indicadores de estado. Puedes usar inmediatamente los dominios conectados en múltiples grupos de suscripción, espacios de trabajo y a través de los canales SMS, RCS y WhatsApp.

![Lista de dominios personalizados y estados.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

La supervisión en vivo te alertará en el panel de Braze si alguno de tus dominios activos tiene un problema, para que tus enlaces personalizados sigan siendo utilizables. Si encuentras algún problema, consulta los detalles del error en la aplicación o ponte en contacto con el [Soporte]({{site.baseurl}}/braze_support/) de Braze para obtener asistencia.

## Asignar dominios personalizados a grupos de suscripción {#assigning-custom-domains-to-subscription-groups}

Una vez configurados, los dominios personalizados se pueden asignar a uno o varios grupos de suscripción de SMS, RCS y WhatsApp.

1. Ve a **Audiencia** > **Administración del grupo de suscripción**.
2. Busca y selecciona tu grupo de suscripción en la lista.
3. En **Detalles del grupo de suscripción**, selecciona tu dominio personalizado en el desplegable **Link Shortening Domain**.

Las campañas enviadas con el acortamiento de enlaces activado usarán el dominio asignado asociado a tu grupo de suscripción de SMS, RCS o WhatsApp.

![Vista previa del creador de mensajes SMS con un dominio de enlace acortado diferente al dominio en el cuadro "Message".]({% image_buster /assets/img/custom_domain2.png %})

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Se pueden compartir los dominios delegados entre múltiples grupos de suscripción? {#can-delegated-domains-be-shared-across-multiple-subscription-groups}

Sí. Un solo dominio se puede usar con múltiples grupos de suscripción. Para hacerlo, selecciona el dominio para cada grupo de suscripción con el que deba estar asociado.

### ¿Se pueden compartir los dominios delegados entre múltiples espacios de trabajo? {#can-delegated-domains-be-shared-across-multiple-workspaces}

Sí. Los dominios se pueden asociar con grupos de suscripción en múltiples espacios de trabajo, siempre que los espacios de trabajo estén contenidos dentro de la misma empresa.

### ¿Cuántos dominios personalizados puedo añadir? {#how-many-custom-domains-can-i-add}

Puedes añadir hasta 10 dominios personalizados por dashboard.

### ¿Qué sucede si no actualizo mis registros de DNS en un plazo de 45 días? {#what-happens-if-i-dont-update-my-dns-records-within-45-days}

Aunque los detalles de tu registro de DNS de Cloudflare expirarán después de 45 días, puedes reiniciar el proceso de configuración con el mismo dominio y Braze generará un nuevo conjunto de registros de DNS para ampliar tu ventana de configuración.

### ¿Se me notificará si hay un error durante el proceso de actualización de DNS? {#will-i-be-notified-if-there-is-an-error-during-the-dns-update-process}

Sí. Si hay un error, recibirás un banner en el panel de Braze con los detalles del problema junto con los pasos para resolverlo.

### ¿Puedo usar un dominio personalizado en múltiples canales? {#can-i-use-a-custom-domain-across-multiple-channels}

Sí. Una vez verificado un dominio personalizado, se puede usar en todos los grupos de suscripción de SMS, RCS y WhatsApp en todos los espacios de trabajo dentro de un dashboard.

### ¿Qué pasa si tengo preguntas o necesito más soporte? {#what-if-i-have-questions-or-need-further-support}

Para obtener orientación más detallada sobre la configuración y administración de dominios personalizados, incluidos los pasos de solución de problemas y los requisitos técnicos, [ponte en contacto con Soporte]({{site.baseurl}}/braze_support/).