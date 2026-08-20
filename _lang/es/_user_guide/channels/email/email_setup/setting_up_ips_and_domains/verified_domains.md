---
nav_title: Dominios verificados
article_title: Dominios verificados
page_order: 0
page_type: tutorial
channel: email
description: "Este artículo práctico explica cómo configurar dominios verificados para que Braze pueda gestionar el DNS del envío de correo electrónico y el seguimiento de clics HTTPS."
toc_headers: h2
---

# Dominios verificados {#verified-domains}

> Los dominios verificados te permiten otorgar a Braze el control de un subdominio específico para automatizar la configuración de correo electrónico y el seguimiento HTTPS. Con la delegación de dominio DNS, Braze gestiona los registros de DNS necesarios para el envío de correo electrónico y el seguimiento de clics. Por ejemplo, si tu subdominio es "mail.example.com", puedes delegarlo a Braze para configurar tus dominios de envío y seguimiento.

{% alert important %}
Actualmente, los dominios verificados solo son compatibles con Amazon SES. Si utilizas SendGrid o SparkPost, esta característica no está disponible.<br><br>Los dominios verificados solo son compatibles con correo electrónico. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

## Beneficios {#benefits}

- Incorporación más rápida: automatizar estos pasos reduce el tiempo de incorporación del correo electrónico.
- Menos coordinación: ya no necesitas trabajar con soporte de Braze para las tareas de configuración de dominio, lo que te acerca a una experiencia completamente de autoservicio.
- Gestión automatizada de SSL: Braze se encarga de la creación y renovación de certificados SSL, lo que elimina un punto común de fallo y trabajo manual. Proteger tus enlaces con SSL es una práctica recomendada estándar: los destinatarios confían más en los enlaces seguros, y la capa adicional de autenticación ayuda a proteger tus datos.
- Menos errores de configuración: los flujos de incorporación guiados y la validación automatizada reemplazan la configuración manual de DNS, que es propensa a errores, por lo que tienes menos posibilidades de configurar registros incorrectamente y afectar la configuración del correo electrónico.
- Monitoreo proactivo: Braze monitorea tus registros de DNS y te notifica cuando detecta problemas, en lugar de esperar a que surjan fallos.

## Consideraciones {#considerations}

Antes de comenzar, ten en cuenta los siguientes detalles:

- Elige un subdominio dedicado. Después de completar la delegación de dominio, Braze gestiona todos los registros de DNS de ese subdominio. Braze recomienda delegar un subdominio en lugar del dominio principal de tu marca, porque delegar un dominio principal significa que pierdes visibilidad y control sobre él. Si deseas usar un dominio principal, utiliza uno que no se use en ningún otro lugar.
- La delegación de NS (servidor de nombres) es necesaria para que Braze pueda gestionar los registros de DNS de tu subdominio, como SPF, DKIM y seguimiento HTTPS, sin que tengas que configurar cada uno manualmente.

{% alert note %}
La delegación CNAME no es compatible. {% multi_lang_include product_feedback_cta.md context="gap" feature="CNAME delegation for verified domains" %}
{% endalert %}

- Planifica un subdominio de envío de al menos tres niveles. Dado que Braze crea un subdominio bajo tu dominio delegado (como "mail.example.com"), tu dominio de envío debe tener al menos tres niveles de profundidad. Un ejemplo es "e.mail.example.com".
- Braze gestiona tus registros de DNS. Una vez completada la delegación, Braze es responsable de los registros de DNS en el subdominio delegado. No modifiques estos registros por tu cuenta, ya que esto puede causar un problema con el envío de correo electrónico.
- El permiso "Edit Domain Settings" es necesario para configurar dominios verificados.

## Paso 1: Añadir el dominio verificado {#step-1-add-the-verified-domain}

1. Ve a **Configuración** > **Dominios verificados** > **Añadir dominio verificado**.
2. Introduce el subdominio y el nombre raíz. Por ejemplo, si estás delegando el subdominio "mail.example.com" a Braze, el nombre raíz es "example.com" y el subdominio es "mail".
3. Confirma que el subdominio que eliges no está en uso en otro lugar y no tiene registros de DNS en conflicto.
4. Selecciona **Añadir** para recibir los registros TXT y NS.

## Paso 2: Configurar los registros de DNS {#step-2-configure-dns-records}

Después de enviar el dominio verificado, Braze genera los registros de DNS necesarios que debes añadir a tu proveedor de DNS. Este paso puede requerir que te coordines con tu equipo de TI o DNS. Tienes 30 días para que los registros sean verificados antes de que expiren. Después de eso, necesitas repetir la configuración.

{% alert tip %}
Confirma que los cuatro registros NS estén explícitamente presentes usando el comando `dig` y que el dominio se valide en el panel antes de considerar la configuración como completa. La verificación de DNS expira después de 30 días.
{% endalert %}

## Paso 3: Verificar el dominio {#step-3-verify-the-domain}

Después de que los registros de DNS se hayan propagado, Braze verifica que los registros estén presentes y correctamente configurados en un plazo de 24 horas. Tras una verificación exitosa:

- El estado del dominio se actualiza a **Verificado**.
- Braze envía un correo electrónico notificándote que el dominio está listo.
- El dominio aparece como activo en la lista de **Dominios verificados**.

Una vez que un subdominio se ha delegado correctamente, crea dominios de correo electrónico como tus dominios de envío y seguimiento yendo a **Añadir dominio personalizado**. Luego, serás dirigido a la página de **Verificación de remitente** para finalizar tu configuración. Para ver los pasos detallados, consulta [Autoservicio de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/email_self_serve).