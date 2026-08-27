---
nav_title: SSL en Braze
article_title: SSL en Braze
page_order: 5
page_type: reference
description: "Este artículo de referencia trata sobre SSL, para qué se utiliza y cómo se utiliza en Braze."
channel: email
---

# SSL en Braze {#ssl-at-braze}

> Una capa de conexión segura (SSL) cifra una URL con HTTPS en lugar de HTTP. HTTPS indica que existe un certificado SSL o TLS válido y de confianza y que el sitio web es seguro para visitar.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## ¿Por qué es importante SSL? {#why-is-ssl-important}

La mayoría de los dominios no requieren SSL, pero Braze recomienda encarecidamente el uso de SSL por las siguientes razones.

Proteger tu sitio web y tus enlaces con SSL es una práctica común incluso para empresas que no manejan directamente información sensible de clientes. Los usuarios confían más en los enlaces protegidos con SSL, y la capa adicional de autenticación ayuda a proteger tus datos.

### Necesario para el seguimiento de clics y aperturas {#necessary-for-click-and-open-tracking}

Braze transforma tus enlaces utilizando tu subdominio de seguimiento de enlaces con marca para rastrear clics y aperturas. De forma predeterminada, estos enlaces comienzan con HTTP. Los usuarios con navegadores o extensiones que restringen el tráfico no seguro pueden tener dificultades para pasar a través de la redirección antes de llegar a la URL de destino, incluso si la URL es segura. Esto puede causar imágenes rotas y un seguimiento impreciso. Aplica SSL al subdominio de seguimiento de enlaces para confirmar redirecciones seguras.

## Requisitos {#requirements}

### Navegador {#browser}

Los principales navegadores, como Google Chrome, restringen el tráfico a través de URL no seguras para proteger a los usuarios. Usar SSL ayuda a confirmar que el contenido es de confianza y minimiza problemas como enlaces rotos e imágenes en correos electrónicos.

### Dominios HSTS {#hsts-domains}

Si tienes un dominio con HTTP Strict Transport Security (HSTS), configura SSL y un CDN para enviar los certificados de seguridad requeridos. Sin SSL, los enlaces de imágenes y web se rompen.

## Adquirir un certificado SSL {#acquire-an-ssl-certificate}

Adquiere un certificado SSL a través de un tercero, generalmente una red de entrega de contenido (CDN). Una CDN aloja el certificado y lo sirve al navegador cuando un usuario hace clic en un enlace, redirigiendo el tráfico a través de la CDN para aplicar los certificados antes de enviarlo a SendGrid o SparkPost.

Para iniciar la configuración SSL, contacta a tu administrador de éxito de cliente de Braze para comenzar una configuración completa de correo electrónico de Braze.

Después de que Braze inicie la configuración, sigue estos pasos:

1. Braze te proporcionará registros de DNS para agregar a tu registro de dominio.
2. Braze verificará si los registros se han agregado correctamente a tu registro.
3. Después de esto, selecciona una CDN y obtén certificados SSL de un proveedor externo.
4. En este punto, configura tu CDN. Ten en cuenta que Braze no puede ayudar con la solución de problemas de configuración de la CDN. Contacta a tu proveedor de CDN para obtener asistencia adicional.
5. Contacta a tu administrador de éxito de cliente para activar SSL.

## ¿Qué es un CDN y por qué lo necesito? {#what-is-a-cdn-and-why-do-i-need-it}

Una red de entrega de contenido (CDN) es una plataforma de servidores que ayuda a garantizar tiempos de carga rápidos del contenido en múltiples medios, al tiempo que también gestiona certificados de seguridad.

{% alert important %}
La configuración del CDN siempre se realiza después de que tus registros de DNS hayan sido validados por Braze. Si aún no has iniciado este paso, contacta a tu administrador de éxito de cliente para obtener más información sobre cómo empezar.
{% endalert %}

Para el seguimiento de clics y aperturas, los partners de entrega transforman los enlaces usando un subdominio de marca y el CDN aplica el certificado SSL a esos enlaces transformados. Los partners a menudo deben presentar certificados válidos al navegador del destinatario para que los enlaces y las imágenes se muestren correctamente. Dado que Braze no solicita ni gestiona certificados, debes configurar esto a través de un CDN.

{% alert note %}
Si no puedes o no quieres usar los CDN enumerados para el seguimiento SSL de clics y aperturas, puedes configurar una configuración SSL personalizada. Los CDN alternativos o los proxies personalizados pueden resultar en una configuración más compleja. Consulta la documentación de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) y [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

### Recursos adicionales {#additional-resources}

{% alert important %}
Para solucionar problemas con la configuración de tu CDN, contacta a tu proveedor de CDN o consulta [Solución de problemas]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting) para orientación general.
{% endalert %}

Consulta los siguientes recursos de los partners ESP sobre cómo configurar ciertos CDN. Aunque tu CDN específico puede no estar en la lista, debes asegurarte de que tu CDN tenga la capacidad de aplicar certificados SSL.

Cuando configures el dominio de seguimiento de clics de tu CDN, habilita el encabezado `X-Forwarded-Host` para prevenir posibles problemas de seguridad, como ataques de encabezado de host. Consulta la documentación de tu CDN o tu equipo de soporte para conocer los pasos.

| Partner | CDN | Documentación |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Uso de HTTPS con CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Comenzar con SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Configuración de TLS con certificados gestionados por Fastly](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [Cómo configurar SSL personalizado](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Certificados SSL gestionados por Google](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [Cómo configurar SSL para el seguimiento de clics usando CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [Uso de CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Uso de Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [Uso de KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Guía paso a paso con AWS CloudFront](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Guía paso a paso con Cloudflare](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Guía paso a paso con Fastly](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Guía paso a paso con Google Cloud Platform](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Guía paso a paso con Microsoft Azure](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recursos adicionales" }

### Amazon SES

Si estás usando Amazon SES como tu ESP, consulta **Opción 2: Configuración de un dominio HTTPS** en la [documentación de Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) y especifica el dominio de seguimiento de AWS por región según tu clúster de Braze:

- **Clústeres de Braze en EE. UU.:** `r.us-east-1.awstrack.me`
- **Clústeres de Braze en la UE:** `r.eu-central-1.awstrack.me`

{% alert important %}
Cuando configures el dominio de seguimiento de clics de tu CDN, habilita el encabezado `X-Forwarded-Host` para prevenir posibles problemas de seguridad, como ataques de encabezado de host. Consulta a tu proveedor de CDN para conocer los pasos.
{% endalert %}

## Patrones de URL de seguimiento de clics y aperturas {#click-and-open-tracking-url-patterns}

Tu proveedor de servicios de correo electrónico (ESP) reescribe cada enlace rastreado para que apunte a tu dominio de seguimiento de clics y luego añade un prefijo de ruta que marca la solicitud como un clic o apertura rastreados. Braze no construye estas rutas. Tu ESP las añade cuando reescribe el enlace. Para reglas de CDN o proxy, listas de seguridad permitidas o manejo de enlaces en aplicaciones móviles, usa la documentación de tu ESP como fuente de referencia.

| ESP | Patrones de ruta | Documentación del ESP |
| --- | --- | --- |
| SendGrid | `/wf/click?upn=...` para clics rastreados y `/uni/wf/click?upn=...` para enlaces que marcas como enlaces universales. Dependiendo de tu configuración, los enlaces de marca también pueden usar `/ls/click` (firmado largo) o `/ss/` (acortado). | [Enlaces universales](https://www.twilio.com/docs/sendgrid/ui/sending-email/universal-links) y [enlaces acortados](https://support.sendgrid.com/hc/en-us/articles/44375837088795-How-to-Know-if-my-Links-Are-Shortened-by-SendGrid) |
| SparkPost | `/f/` para clics rastreados y `/q/` para aperturas rastreadas. Los enlaces que establecen una ruta personalizada `data-msys-sublink` siguen el formato `/f/{custom_path}/`. | [Vínculos profundos](https://docs.sparkpost.com/docs/tech-resources/deep-links-self-serve) |
| Amazon SES | `/CL0/{encodedUrl}/{index}/{messageId}/{hmac}` para clics rastreados. Los enlaces que establecen el atributo `ses:custom-path` siguen el formato `/CL1/{customPath}/{encodedUrl}/...`. | [Dominios personalizados de apertura y clic](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Patrones de URL de seguimiento de clics y aperturas por ESP" }

Por ejemplo, si tu dominio de seguimiento de clics es `clicks.example.com` y tu ESP es SparkPost, un clic rastreado se resuelve a una URL que comienza con `https://clicks.example.com/f/`.

{% alert important %}
Tu ESP es el propietario de estos prefijos de ruta y puede cambiarlos o añadir nuevos, por lo que Braze no puede garantizar una lista permanente o exhaustiva. Cuando tus herramientas de seguridad lo permitan, incluye en la lista de permitidos tu dominio completo de seguimiento de clics en lugar de rutas individuales, y confirma los patrones actuales en la documentación de tu ESP.
{% endalert %}

Para manejar estas rutas en tu aplicación móvil, consulta [Enlaces universales y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

## Solución de problemas {#troubleshooting}

Si bien deberías manejar la configuración del CDN, los certificados y los problemas de proxy con tu CDN, usa estos consejos para identificar problemas comunes de seguimiento de clics SSL. Para obtener orientación sobre la solución de problemas, consulta [Solución de problemas]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting).