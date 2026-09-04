---
nav_title: Problemas de capacidad de entrega y trampas de correo no deseado
article_title: Problemas de capacidad de entrega y trampas de correo no deseado
page_order: 7
page_type: reference
description: "Este artículo de referencia cubre los posibles problemas de capacidad de entrega de correo electrónico, las trampas de correo no deseado y cómo evitarlos."
channel: email

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}Problemas de capacidad de entrega y trampas de correo no deseado {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomemail-onboarding-for-pro-and-enterprise-achieving-high-deliverability-stylefloatrightwidth120pxborder0-classnoimgborderdeliverability-pitfalls-and-spam-traps}

> Este artículo cubre los problemas comunes de capacidad de entrega de correo electrónico, las trampas de correo no deseado y cómo evitarlos.

La capacidad de entrega de tu correo electrónico puede verse afectada por cualquiera de las siguientes trampas de correo no deseado:

| Tipo de trampa | Descripción |
|---|---|
| Trampas prístinas | Direcciones de correo electrónico y dominios que nunca se han utilizado. |
| Trampas recicladas | Direcciones de correo electrónico que originalmente pertenecían a usuarios reales, pero que ahora están inactivas. |
| Trampas tipográficas | Direcciones de correo electrónico que contienen erratas comunes. |
| Denuncias de correo no deseado | Cuando un consumidor marca tu correo electrónico como correo no deseado. |
| Tasa de rebote alta | Cuando tu correo electrónico no se puede entregar de forma consistente porque la dirección del destinatario no es válida. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Problemas de capacidad de entrega y trampas de correo no deseado" }

## Cómo evitar las trampas de correo no deseado {#how-to-avoid-spam-traps}

Estas trampas se pueden evitar si configuras un proceso de adhesión voluntaria confirmada. Al enviar un correo electrónico inicial de adhesión voluntaria y pedir a los suscriptores que verifiquen que desean recibir tus mensajes, te aseguras de que tus destinatarios quieren saber de ti y de que estás enviando a direcciones reales y válidas. Aquí tienes formas adicionales de evitar las trampas de correo no deseado:

1. Envía un correo electrónico de doble adhesión voluntaria. Se trata de un correo electrónico que requiere que los usuarios confirmen sus opciones de suscripción haciendo clic en un enlace.
2. Como práctica recomendada, implementa una [política de desactivación]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies).
3. **Nunca compres listas de correo electrónico.**

{% alert tip %}
Los equipos de éxito del cliente y capacidad de entrega de Braze pueden ayudarte a seguir las prácticas recomendadas para maximizar la capacidad de entrega en todo el mundo.
{% endalert %}

## Cómo resolver un bloqueo de dominio de correo electrónico gratuito en Microsoft {#how-to-resolve-a-free-email-domain-block-for-microsoft}

Microsoft rara vez desbloquea a los remitentes que tienen problemas para entregar correos a dominios de correo electrónico gratuitos (Hotmail, Live, MSN y Outlook). En su lugar, reduce tu volumen hacia esos dominios de forma agresiva y envía solo a contactos que hayan interactuado recientemente. Si no puedes identificar un grupo principal de destinatarios comprometidos, deja de enviar a esos dominios por completo.

Un ejemplo de mensaje de bloqueo de dominio de correo electrónico gratuito es:

`550 5.7.1 Unfortunately, messages from [xx.xx.xx.xx] weren't sent. Please contact your ISP since part of their network is on our block list (S3150). You can also refer your provider to: http://mail.live.com/mail/troubleshooting.aspx#errors.`

Puedes aumentar el volumen lentamente de forma similar al [calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming), prestando mucha atención a las métricas. A menudo hay una causa raíz de los problemas de capacidad de entrega que es necesario identificar y resolver. En general, se trata de una falta de permisos adecuados, una falta de higiene continua de la lista o una combinación de ambos factores.

## Eliminar una dirección de correo electrónico de tu lista de rebotes o correo no deseado {#remove-an-email-address-from-your-bounce-or-spam-list}

Puedes eliminar correos electrónicos rebotados y correos electrónicos de tu lista de correo no deseado de Braze con los siguientes endpoints:

- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## Mejorar la capacidad de entrega del correo electrónico {#improve-email-deliverability}

Para más información, consulta [Mejorar la capacidad de entrega del correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability).

## BIMI

Para BIMI (Brand Indicators for Message Identification), consulta [Autenticación de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication).