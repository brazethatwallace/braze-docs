---
nav_title: Configurar direcciones IP y dominios
article_title: Configurar direcciones IP y dominios
page_order: 0
page_type: tutorial
channel: email
description: "Este artículo te guía sobre cómo configurar tus IP y dominios para enviar correos electrónicos a través de Braze."

---

# Configurar direcciones IP y dominios {#set-up-ips-and-domains}

> Este artículo te guía a través de los requisitos y pasos necesarios para configurar tus direcciones IP y pools, así como los dominios y subdominios necesarios antes de que puedas empezar a enviar correos electrónicos con Braze.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
Puedes usar SendGrid, SparkPost o Amazon Simple Email Service (SES) como tu socio proveedor de servicios de correo electrónico (ESP). A partir de 2026, Braze utiliza Amazon SES como el ESP predeterminado para nuevas configuraciones de correo electrónico. Para más detalles, consulta [Configuración de Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses/).
{% endalert %}

## Método 1: Coordinar con Braze (recomendado) {#method-1-coordinate-with-braze-recommended}

### Paso 1: Información general {#step-1-outline-information}

Envía la siguiente información a tu representante de Braze:

* Tus dominios y subdominios elegidos
* El número aproximado de correos electrónicos que enviarás cada mes, lo que ayudará a determinar cuántas IP necesitarás
* Cómo prefieres asignar tus dominios de envío a tus IP asignadas

### Paso 2: Braze configura la información {#step-2-braze-configures-information}

Tras recibir tu correo electrónico, nos pondremos manos a la obra para configurar tus IP, dominios y subdominios, y pools de IP.

### Paso 3: Añadir registros DNS {#step-3-add-dns-records}

Una vez que tus IP, dominios, subdominios y pools de IP estén configurados, te enviaremos una lista de registros DNS. Pide a tus ingenieros y desarrolladores que añadan estos registros DNS donde sea necesario y, una vez que se hayan añadido, informa al equipo de incorporación de Braze.

{% multi_lang_include dns_records.md %}

Después de que Braze te proporcione tus registros DNS, añádelos tan pronto como tu equipo de DNS o de TI pueda. La verificación de dominio tiene un límite de tiempo, y si los registros se añaden demasiado tarde, la verificación puede fallar incluso si los registros DNS se resuelven correctamente después. Si tus registros DNS parecen correctos pero la verificación falla, ponte en contacto con el equipo de incorporación o soporte de Braze para reiniciar la verificación.

### Próximos pasos {#next-steps}

Revisaremos tu configuración y validaremos toda la información en nuestros sistemas internos. El equipo de incorporación de Braze te informará cuando estés listo para empezar, o si hay problemas con tus registros DNS que debas resolver con tu equipo de ingeniería.

## Método 2: Configuración de correo electrónico de autoservicio {#method-2-self-service-email-setup}

Este método configurará un dominio de envío, un dominio de seguimiento y una IP en total para una empresa. Si planeas configurar más, consulta con el equipo de incorporación de Braze (método 1).

{% multi_lang_include early_access_beta_alert.md feature='This self-service email setup feature' type='beta' %}
<br>Si estás usando la característica de configuración de correo electrónico de autoservicio, asegúrate de consultar también con el equipo de incorporación de Braze.

### Requisitos previos {#prerequisites}

Para usar la configuración de correo electrónico de autoservicio, debes cumplir los siguientes requisitos previos:

1. Eres un cliente nuevo en proceso de incorporación.
2. Tienes el permiso a nivel de empresa "Manage Company Settings".

### Paso 1: Iniciar la configuración {#step-1-begin-setup}

1. Ve a **Configuración** > **Configuración de administrador** en **Configuración de empresa**.
2. A continuación, selecciona la pestaña **Verificación del remitente**. Para ver esta pestaña, debes tener el permiso a nivel de empresa "Manage Company Settings".
3. Selecciona **Iniciar configuración**.

### Paso 2: Añadir y verificar un dominio de envío {#step-2-add-and-verify-a-sending-domain}

Un dominio de envío se utiliza en la dirección "de" al enviar un correo electrónico. Introduce un dominio de envío y haz clic en **Enviar**.

A continuación, añade los registros TXT y CNAME de la parte inferior de la página a tu proveedor de DNS. Luego, vuelve al panel de Braze y haz clic en **Verificar**.

![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

Si la verificación falla y crees que tus registros DNS son correctos, ponte en contacto con soporte de Braze para obtener ayuda.

{% alert important %}
El dominio de envío debe ser un subordinado de un dominio que poseas. Por ejemplo, si posees "example.com", un subdominio podría ser "mail.example.com", lo que te permite usar la dirección de envío "@mail.example.com".
{% endalert %}

### Paso 3: Añadir y verificar un dominio de seguimiento {#step-3-add-and-verify-a-tracking-domain}

Un dominio de seguimiento se utiliza para envolver los enlaces en tus correos electrónicos con fines de seguimiento de clics y branding. Esto será visible para los usuarios cuando pasen el cursor sobre los enlaces de tu correo electrónico o hagan clic en ellos. Recomendamos que coincida con tu dominio de envío.

1. Introduce un dominio de seguimiento y selecciona **Enviar**.
2. A continuación, añade los registros CNAME de la parte inferior de la página a tu proveedor de DNS.
3. Luego, vuelve al panel de Braze y selecciona **Verificar**.

### Paso 4: Añadir una dirección IP {#step-4-add-an-ip-address}

Braze genera un registro A para asociar tu dirección IP con tu subdominio de envío en una configuración llamada DNS inverso (rDNS). Añade el registro A en tu proveedor de DNS y luego haz clic en **Configurar rDNS** para mejorar la capacidad de entrega.

Ten en cuenta que los dominios adicionales que se hayan añadido no aparecen en la sección **Verificación del remitente**. Para añadir más dominios, ponte en contacto con el equipo de soporte de Braze.

### Pools de IP con más de una IP dedicada {#ip-pools-with-more-than-one-dedicated-ip}

Cuando un pool de IP contiene múltiples direcciones IP dedicadas, Braze y tu proveedor de servicios de correo electrónico distribuyen los envíos grandes entre esas IP para mejorar la capacidad y la capacidad de entrega. La distribución es aproximada: no todos los mensajes de una campaña utilizan todas las IP, y los envíos más pequeños pueden parecer desiguales entre las direcciones. SendGrid suele procesar el correo en bloques (del orden de aproximadamente 1500 mensajes por bloque), por lo que el volumen no siempre se divide en una proporción estricta de uno a uno entre las IP. Si envías habitualmente un volumen diario muy alto, consulta el dimensionamiento del pool con tu contacto de incorporación o éxito del cliente de Braze.

### Próximos pasos

Una vez que tu verificación de remitente esté completa, recomendamos el calentamiento de IP para que tus mensajes lleguen a los buzones de entrada de destino a una tasa consistentemente alta. Después de completar esta configuración, asegúrate de consultar también con el equipo de incorporación de Braze para confirmar si tus dominios y [dirección IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/) están funcionando.