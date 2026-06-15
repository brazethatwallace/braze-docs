---
nav_title: Configuración de Amazon SES
article_title: Configuración de Amazon SES
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo configurar Amazon SES como tu proveedor de servicios de correo electrónico."
channel: email
---

# Configuración de Amazon SES {#amazon-ses-setup}

> Braze utiliza Amazon Simple Email Service (SES) como proveedor de servicios de correo electrónico predeterminado durante la configuración inicial de correo electrónico. Si la configuración que necesitas no se ajusta a las características de Amazon SES, ponte en contacto con el soporte de Braze para completar la configuración en SparkPost o SendGrid.

## Requisitos previos {#prerequisites}

Antes de comenzar la configuración de Amazon SES, confirma que tienes lo siguiente:

- Nombres de dominio de envío
- Nombres de pools de IP (como marketing, transaccional, staging)
- El número de direcciones IP para cada pool de IP
- Sufijo preferido para los dominios de seguimiento de clics (como "clicks" o "click", "links" o "link")

## Ejemplo de configuración {#setup-example}

Una configuración típica de Amazon SES se ve de la siguiente manera:

- **Nombre de subcuenta:** braze
- **Clúster:** eu-02

| Pool de IP | Número de IPs | Conjunto de configuración | Dominio de envío | Dominio de seguimiento de clics |
| --- | --- | --- | --- | --- |
| `eu02_braze_marketing` | 1 IP | `eu02_braze_marketing_set1` | `demo.braze.com` | `clicks.demo.braze.com` |
| `eu02_braze_transactional` | 1 IP | `eu02_braze_transactional_set1` | `dev.braze.com` | `clicks.dev.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Ejemplo de configuración" }

{% alert note %}
El clúster y el nombre de subcuenta se añaden automáticamente a los pools de IP y los conjuntos de configuración.
{% endalert %}

## Ejemplos de configuración de dominios de seguimiento de clics {#click-tracking-domain-configuration-examples}

Las siguientes tablas son ejemplos de posibles configuraciones de dominios de seguimiento de clics según tu preferencia de marca.

### Un dominio de seguimiento de clics para cada dominio de envío {#one-click-tracking-domain-for-each-sending-domain}

| Pool de IP de marketing | Conjunto de configuración | Subdominios de envío | Dominios de seguimiento de clics |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set1 | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set2 | `email2.example.com` | `clicks.email2.example.com` |
| braze_marketing - 1 IP | braze_marketing_set3 | `email3.example.com` | `clicks.email3.example.com` |
| braze_marketing - 1 IP | braze_marketing_set4 | `email4.example.com` | `clicks.email4.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Un dominio de seguimiento de clics para cada dominio de envío" }

### Un dominio de seguimiento de clics para todos los dominios de envío {#one-click-tracking-domain-for-all-sending-domains}

Esto se basa en la regla de que el dominio de seguimiento de clics debe coincidir con al menos un dominio de envío del conjunto de configuración.

| Pool de IP de marketing | Conjunto de configuración | Subdominios de envío | Dominios de seguimiento de clics |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email2.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email3.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email4.example.com` | `clicks.email1.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Un dominio de seguimiento de clics para todos los dominios de envío" }

## Consideraciones {#considerations}

- Los pools de IP en Amazon SES solo alojan la dirección IP en sí, mientras que los conjuntos de configuración alojan los dominios de envío y el dominio de seguimiento de clics.
- Cada conjunto de configuración solo puede tener un pool de IP asignado a la vez, pero se pueden crear múltiples conjuntos de configuración que utilicen el mismo pool de IP con diferentes dominios de envío.
- Amazon SES gestiona los registros rDNS y A de forma interna, ya que mantiene relaciones estrechas con los proveedores de buzón de entrada para ayudar a reconocer las direcciones IP.
- Cada dominio de envío tiene un identificador MAIL FROM asociado para ayudar con las validaciones SPF.
    - El valor para cada dominio de envío es "e".
    - El valor MAIL FROM no cambia la dirección del remitente que ven tus clientes.
- El inicio y el fin del periodo de mensajes trampa no están disponibles si utilizas Amazon SES como tu proveedor de servicios de correo electrónico.

## Próximos pasos {#next-steps}

- [Configurar SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/)