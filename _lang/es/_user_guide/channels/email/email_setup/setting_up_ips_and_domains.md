---
nav_title: Configurar direcciones IP y dominios
article_title: Configurar direcciones IP y dominios
page_order: 0
page_type: tutorial
channel: email
description: "Este artículo práctico explica cómo configurar direcciones IP, pools de IP, dominios y subdominios para enviar correos electrónicos con Braze."
---

# Configurar direcciones IP y dominios {#set-up-ips-and-domains}

> Este artículo te guía a través de los requisitos y pasos necesarios para configurar tus direcciones IP y pools, así como los dominios y subdominios necesarios antes de que puedas empezar a enviar correos electrónicos con Braze.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
A partir de 2026, Braze utiliza Amazon Simple Email Service (SES) como el proveedor de servicios de correo electrónico (ESP) predeterminado para nuevas configuraciones de correo electrónico. Para más detalles, consulta [Configuración de Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).
{% endalert %}

## Método 1: Configuración de correo electrónico en autoservicio {#method-1-self-service-email-setup}

Este método configura tus dominios de envío y seguimiento para una empresa. Primero deberás consultar con el equipo de incorporación de Braze y enviar la siguiente información a tu representante de Braze para que se añadan tus pools de IP y direcciones IP:

- Tus dominios y subdominios elegidos
- El número aproximado de correos electrónicos que envías cada mes, lo que ayuda a determinar cuántas IP necesitas
- Cómo prefieres asignar tus dominios de envío a tus pools de IP asignados

### Requisitos previos {#prerequisites}

Para utilizar la configuración de correo electrónico en autoservicio, confirma que cumples los siguientes requisitos previos:

- Eres un cliente nuevo en proceso de incorporación.
- Tienes el permiso de nivel de empresa "Edit Domain Settings".

### Paso 1: Iniciar la configuración {#step-1-begin-setup}

1. Ve a **Configuración** > **Email Self Serve** en **Configuración de la empresa**.
2. Selecciona **Start setup**.

### Paso 2: Añadir y verificar un dominio de envío {#step-2-add-and-verify-a-sending-domain}

Un dominio de envío se utiliza en la dirección "de" al enviar un correo electrónico.

1. Introduce un dominio de envío y selecciona **Submit**.
2. Añade los registros TXT y CNAME de la parte inferior de la página a tu proveedor de DNS.

![Sección de registros de DNS que muestra los registros TXT y CNAME para copiar en tu sistema de gestión de dominios.]({% image_buster /assets/img/email_setup/dns_records.png %})

{: start="3"}
3. Regresa al panel de Braze y selecciona **Verify**.

Pide a tus ingenieros y desarrolladores que añadan estos registros de DNS donde sea necesario. Para explicaciones detalladas sobre cómo funcionan los registros de DNS en los proveedores de servicios de correo electrónico de Braze, incluidos SPF, DKIM, DMARC y las estructuras de registros específicas de cada ESP, consulta [Comprender los registros de DNS]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/understanding_dns_records).

{% multi_lang_include channels/email/dns_records.md %}

Si la verificación falla y crees que tus registros de DNS son correctos, ponte en contacto con el soporte de Braze para obtener ayuda.

{% alert important %}
El dominio de envío debe ser subordinado a un dominio que poseas. Por ejemplo, si posees "example.com", un subdominio podría ser "mail.example.com", lo que te permite utilizar la dirección de envío "@mail.example.com".
{% endalert %}

### Paso 3: Añadir y verificar un dominio de seguimiento {#step-3-add-and-verify-a-tracking-domain}

Un dominio de seguimiento se utiliza para envolver los enlaces en tus correos electrónicos con fines de seguimiento de clics y marca. Esto es visible para tus destinatarios cuando pasan el cursor sobre los enlaces de tu correo electrónico o hacen clic en ellos. Braze recomienda que coincida con tu dominio de envío.

1. Introduce un dominio de seguimiento y selecciona **Submit**.
2. Añade los registros CNAME de la parte inferior de la página a tu proveedor de DNS.
3. Regresa al panel de Braze y selecciona **Verify**.

### Paso 4: Añadir una dirección IP {#step-4-add-an-ip-address}

Braze genera un registro A para asociar tu dirección IP con tu subdominio de envío en una configuración llamada DNS inverso (rDNS). Añade el registro A en tu proveedor de DNS y luego selecciona **Set up rDNS** para mejorar la capacidad de entrega.

Para añadir o editar tus direcciones IP para un pool de IP, ponte en contacto con el soporte de Braze.

#### Pools de IP con más de una IP dedicada {#ip-pools-with-more-than-one-dedicated-ip}

Cuando un pool de IP contiene múltiples direcciones IP dedicadas, Braze y tu proveedor de servicios de correo electrónico distribuyen los envíos grandes entre esas IP para mejorar la capacidad y la capacidad de entrega. La distribución es aproximada: no todos los mensajes de una Campaign utilizan todas las IP, y los envíos más pequeños pueden parecer desiguales entre las direcciones. SendGrid a menudo procesa el correo en bloques (del orden de aproximadamente 1500 mensajes por bloque), por lo que el volumen no siempre se divide en una proporción estricta uno a uno entre las IP. Si envías habitualmente un volumen diario muy alto, consulta el dimensionamiento del pool con tu contacto de incorporación o de éxito del cliente de Braze.

### Próximos pasos {#next-steps}

Una vez completada la verificación de tu remitente, Braze recomienda el calentamiento de IP para que tus mensajes lleguen a los buzones de entrada de destino a una tasa consistentemente alta. Utiliza el [calentamiento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming) para ayudarte a configurar y monitorear tu programa de calentamiento.

Después de completar esta configuración, consulta con el equipo de incorporación de Braze para confirmar si tus dominios y el [calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) están funcionando.

## Método 2: Dominios verificados {#method-2-verified-domains}

Los dominios verificados te permiten otorgar a Braze el control de un subdominio específico para que Braze pueda automatizar la configuración de correo electrónico y el seguimiento de clics HTTPS. Con la delegación de dominios DNS, Braze gestiona los registros de DNS necesarios para el envío de correo electrónico y el seguimiento de clics. Por ejemplo, si tu subdominio es "mail.example.com", puedes delegarlo a Braze para configurar tus dominios de envío y seguimiento.

{% alert important %}
Actualmente, los dominios verificados solo son compatibles con Amazon SES. Si utilizas SendGrid o SparkPost, esta característica no está disponible.<br><br>Los dominios verificados solo son compatibles con correo electrónico. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

### Configuración {#setup}

#### Paso 1: Coordinar con Braze {#step-1-coordinate-with-braze}

Envía la siguiente información a tu representante de Braze:

- Tus dominios y subdominios elegidos
- Cómo prefieres asignar tus dominios a tus pools de IP
- El número aproximado de correos electrónicos que planeas enviar cada mes en cada subdominio, lo que ayuda a determinar cuántas IP necesitas para tus pools de IP
- Cualquier problema previo de capacidad de entrega que deba señalarse

#### Paso 2: Braze configura la información {#step-2-braze-configures-information}

Después de recibir tu correo electrónico, Braze añade el número esperado de IP y pools de IP. Una vez que se hayan añadido los pools de IP y las direcciones IP, sigue los pasos en [Dominios verificados]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/verified_domains).