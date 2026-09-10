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
- Nombres de grupos de IP (como marketing, transaccional, staging)
- El número de direcciones IP para cada grupo de IP
- Sufijo preferido para los dominios de seguimiento de clics (como "clicks" o "click", "links" o "link")

## Ejemplo de configuración {#setup-example}

Una configuración típica de Amazon SES tiene el siguiente aspecto:

- **Nombre de subcuenta:** braze
- **Clúster:** eu-02

| Grupo de IP | Número de IP | Conjunto de configuración | Dominio de envío | Dominio de seguimiento de clics |
| --- | --- | --- | --- | --- |
| `eu02_braze_marketing` | 1 IP | `eu02_braze_marketing_set1` | `demo.braze.com` | `clicks.demo.braze.com` |
| `eu02_braze_transactional` | 1 IP | `eu02_braze_transactional_set1` | `dev.braze.com` | `clicks.dev.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Ejemplo de configuración" }

{% alert note %}
El clúster y el nombre de la subcuenta se añaden automáticamente a los grupos de IP y los conjuntos de configuración.
{% endalert %}

## Ejemplos de configuración de dominio de seguimiento de clics {#click-tracking-domain-configuration-examples}

Las siguientes tablas son ejemplos de posibles configuraciones de dominio de seguimiento de clics según tu preferencia de marca.

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
- Cada conjunto de configuración solo puede tener un pool de IP asignado a la vez, pero podemos crear múltiples conjuntos de configuración que pueden usar el mismo pool de IP con diferentes dominios de envío.
- Amazon SES gestiona los registros rDNS y A internamente, ya que mantienen relaciones estrechas con los proveedores de buzón de entrada para ayudar a reconocer las direcciones IP.
- Cada dominio de envío tiene un identificador MAIL FROM adjunto para ayudar con las validaciones SPF.
    - El valor para cada dominio de envío es "e".
    - El valor MAIL FROM no cambia la dirección De que ven tus clientes.
- Los campos de inicio del periodo de mensaje trampa y fin del periodo de mensaje trampa no están disponibles si usas Amazon SES como tu proveedor de servicios de correo electrónico.

## Próximos pasos {#next-steps}

{% article_tiles %}
- name: Configurar SSL
  link: /docs/user_guide/channels/email/email_setup/ssl
{% endarticle_tiles %}