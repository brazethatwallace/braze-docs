---
nav_title: "Playable"
article_title: "Playable"
description: "Este artículo de referencia describe la asociación entre Braze y Playable, una plataforma de video que te permite añadir contenido de video a tus Campaigns de correo electrónico en Braze."
alias: /partners/playable/
page_type: partner
search_tag: Partner

---

# Playable

> [Playable](https://playable.video) te permite añadir contenido de video de reproducción automática a tus Campaigns de correo electrónico en Braze.

_Esta integración está mantenida por Playable._

## Acerca de la integración {#about-the-integration}

La integración de Braze y Playable te permite entregar tu mejor contenido (video de alta calidad) a tu mejor audiencia (correo electrónico), aumentando tus métricas de click-through y post-clic con contenido emocionante de alta calidad que se reproduce automáticamente dentro del buzón de entrada.

{% alert important %}
Los videos incrustados no son compatibles de forma nativa con muchos clientes de correo electrónico y pueden aumentar significativamente el tamaño del correo electrónico, lo que puede provocar que los mensajes se marquen como correo no deseado. Playable soluciona esto entregando contenido de video optimizado que funciona en todos los clientes de correo electrónico. Para más detalles sobre video en correo electrónico, consulta [¿Puedo incrustar videos en correos electrónicos?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-embed-videos-in-emails)
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Playable | Se requiere una cuenta de Playable para aprovechar esta integración. Si aún no tienes una cuenta de Playable, [suscríbete a una cuenta de Playable](https://signup.playable.video).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }
Contenido de video | Sube archivos de video a Playable o proporciona URL de video de sitios web como Facebook, Instagram, YouTube, X (anteriormente Twitter), TikTok y más. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Implementación {#implementation}

### Paso 1: Añade tu video a Playable {#step-1-add-your-video-to-playable}

En la plataforma Playable, sube archivos de video o añade videos proporcionando una URL de tu video en Facebook, Instagram, YouTube, X (anteriormente Twitter), TikTok y más.

### Paso 2: Copia el código de inserción de Playable {#step-2-copy-the-embed-code-from-playable}

Una vez subido, Playable generará un código que, al insertarlo en tu Campaign de Braze, incrustará el video en tu correo electrónico para que se reproduzca automáticamente al abrirlo. Cuando se abra tu correo electrónico, los servidores de Playable entregarán la mejor versión posible de tu video dependiendo del cliente de correo electrónico, el dispositivo, el tamaño de pantalla y las condiciones de red.

{% alert tip %}
Los videos se reproducirán automáticamente en más del 98% de los buzones de entrada, incluyendo iPhone Mail, Gmail, Apple Mail, Outlook para iOS, Outlook para Android, Outlook para Mac y versiones más recientes de Outlook 365 para Windows. Los usuarios de versiones anteriores de Outlook para Windows verán una imagen estática en su lugar.
{% endalert %}

### Paso 3: Pega el código de inserción en Braze {#step-3-paste-the-embed-code-into-braze}

Por último, pega el código en tu Campaign de correo electrónico en Braze y luego continúa diseñando, probando y publicando tu Campaign de correo electrónico.