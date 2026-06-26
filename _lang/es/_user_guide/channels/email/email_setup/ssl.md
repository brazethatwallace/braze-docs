---
nav_title: SSL en Braze
article_title: Resumen de SSL
page_order: 5
page_type: reference
description: "Este artículo de referencia trata sobre SSL, para qué se utiliza y cómo se utiliza en Braze."
channel: email

---

# SSL en Braze {#ssl-at-braze}

> Una capa de conexión segura (SSL) cifra una URL con HTTPS en lugar de HTTP. HTTPS indica que existe un certificado SSL o TLS válido y de confianza y que el sitio web es seguro para visitar.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## ¿Por qué es importante SSL? {#why-is-ssl-important}

La mayoría de los dominios no requieren SSL, pero Braze recomienda encarecidamente utilizar SSL por los siguientes motivos.

Proteger tu sitio web y tus enlaces con SSL es una práctica habitual incluso para las empresas que no manejan directamente información confidencial de sus clientes. Los usuarios confían más en los enlaces protegidos con SSL, y la capa adicional de autenticación ayuda a proteger tus datos.

### Necesario para el seguimiento de clics y aperturas {#necessary-for-click-and-open-tracking}

Braze transforma tus enlaces utilizando tu subdominio de seguimiento de enlaces de marca para realizar el seguimiento de clics y aperturas. De forma predeterminada, estos enlaces comienzan con HTTP. Los usuarios con navegadores o extensiones que restringen el tráfico no seguro pueden tener dificultades para pasar por la redirección antes de la URL de destino, incluso si la URL es segura. Esto puede provocar imágenes rotas y un seguimiento inexacto. Aplica SSL al subdominio de seguimiento de enlaces para confirmar que las redirecciones son seguras.

## Requisitos {#requirements}

### Navegador {#browser}

Los principales navegadores, como Google Chrome, restringen el tráfico a través de URL no seguras para proteger a los usuarios. Usar SSL ayuda a confirmar que el contenido es de confianza y minimiza problemas como enlaces e imágenes rotos en los correos electrónicos.

### Dominios HSTS {#hsts-domains}

Si tienes un dominio con HTTP Strict Transport Security (HSTS), configura SSL y un CDN para enviar los certificados de seguridad requeridos. Sin SSL, los enlaces de imágenes y web se rompen.

## Obtener un certificado SSL {#acquire-an-ssl-certificate}

Obtén un certificado SSL a través de un tercero, generalmente una red de entrega de contenido (CDN). Un CDN aloja el certificado y lo sirve al navegador cuando un usuario hace clic en un enlace, redirigiendo el tráfico a través del CDN para aplicar los certificados antes de enviarlo a SendGrid o SparkPost.

Para iniciar la configuración de SSL, ponte en contacto con tu administrador del éxito del cliente de Braze para iniciar una configuración completa de correo electrónico de Braze.

Después de que Braze inicie la configuración, sigue estos pasos:

1. Braze proporcionará registros de DNS para agregar a tu registro de dominio.
2. Braze verificará si los registros se han agregado correctamente a tu registro.
3. Después de esto, selecciona un CDN y obtén certificados SSL de un proveedor externo.
4. En este punto, configura tu CDN. Ten en cuenta que Braze no puede ayudar con la solución de problemas de configuración del CDN. Ponte en contacto con tu proveedor de CDN para cualquier asistencia adicional.
5. Ponte en contacto con tu administrador del éxito del cliente para activar SSL.

## ¿Qué es un CDN y por qué lo necesito? {#what-is-a-cdn-and-why-do-i-need-it}

Una red de entrega de contenido (CDN) es una plataforma de servidores que ayuda a garantizar tiempos de carga rápidos del contenido en múltiples medios, al mismo tiempo que gestiona los certificados de seguridad.

{% alert important %}
La configuración del CDN siempre se realiza después de que Braze valide tus registros de DNS. Si aún no has iniciado este paso, ponte en contacto con tu administrador del éxito del cliente para obtener más información sobre cómo empezar.
{% endalert %}

Para el seguimiento de clics y aperturas, los socios de entrega transforman los enlaces usando un subdominio de marca y el CDN aplica el certificado SSL a esos enlaces transformados. Los socios a menudo deben presentar certificados válidos al navegador del destinatario para que los enlaces y las imágenes se muestren correctamente. Dado que Braze no solicita ni gestiona certificados, debes configurar esto a través de un CDN.

{% alert note %}
Si no puedes o no quieres usar los CDN listados para el seguimiento de clics y aperturas con SSL, puedes establecer una configuración SSL personalizada. Los CDN alternativos o proxies personalizados pueden resultar en una configuración más compleja. Consulta la documentación de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) y [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

### Recursos adicionales {#additional-resources}

{% alert important %}
Para la solución de problemas de configuración de tu CDN, ponte en contacto con tu proveedor de CDN o consulta [Solución de problemas]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting/) para obtener orientación general.
{% endalert %}

Consulta los siguientes recursos de los socios ESP sobre cómo configurar ciertos CDN. Aunque tu CDN específico puede no estar listado, debes asegurarte de que tu CDN tenga la capacidad de aplicar certificados SSL.

Cuando configures el dominio de seguimiento de clics de tu CDN, habilita el encabezado `X-Forwarded-Host` para prevenir posibles problemas de seguridad como ataques de encabezado de host. Consulta la documentación del CDN o tu equipo de soporte para los pasos a seguir.

| Socio | CDN | Documentación |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Usar HTTPS con CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Comenzar con SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Configurar TLS con certificados que Fastly gestiona](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [Cómo configurar SSL personalizado](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Certificados SSL gestionados por Google](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [Cómo configurar SSL para seguimiento de clics usando CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [Usar CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Usar Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [Usar KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Guía paso a paso con AWS CloudFront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Guía paso a paso con Cloudflare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Guía paso a paso con Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Guía paso a paso con Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Guía paso a paso con Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recursos adicionales" }

### Amazon SES

Si estás usando Amazon SES como tu ESP, consulta **Opción 2: Configurar un dominio HTTPS** en la [documentación de Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) y especifica el dominio de seguimiento de AWS por región según tu clúster de Braze:

- **Clústeres de Braze en EE. UU.:** `r.us-east-1.awstrack.me`
- **Clústeres de Braze en la UE:** `r.eu-central-1.awstrack.me`

{% alert important %}
Cuando configures el dominio de seguimiento de clics de tu CDN, habilita el encabezado `X-Forwarded-Host` para prevenir posibles problemas de seguridad como ataques de encabezado de host. Consulta a tu proveedor de CDN para los pasos a seguir.
{% endalert %}

## Solución de problemas {#troubleshooting}

Aunque debes gestionar la configuración del CDN, los certificados y los problemas de proxy con tu CDN, usa estos consejos para identificar problemas comunes de seguimiento de clics con SSL. Para obtener orientación sobre la solución de problemas, consulta [Solución de problemas]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting/).