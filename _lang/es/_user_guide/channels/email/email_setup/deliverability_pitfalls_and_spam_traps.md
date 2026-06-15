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
| Denuncias de correo no deseado | Cuando un cliente marca tu correo electrónico como correo no deseado. |
| Tasa de rebote alta | Cuando tu correo electrónico no se puede entregar de forma consistente porque la dirección del destinatario no es válida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cómo evitar las trampas de correo no deseado {#how-to-avoid-spam-traps}

Estas trampas se pueden evitar si configuras un proceso de adhesión voluntaria confirmada. Al enviar un correo electrónico inicial de adhesión voluntaria y pedir a los clientes que verifiquen que desean recibir tus mensajes, te aseguras de que tus destinatarios quieren saber de ti y de que estás enviando a direcciones reales y válidas. Aquí tienes formas adicionales de evitar las trampas de correo no deseado:

1. Envía un correo electrónico de doble adhesión voluntaria. Este es un correo electrónico que requerirá que los usuarios confirmen sus opciones de suscripción haciendo clic en un enlace.
2. Como práctica recomendada, implementa una [política de desactivación]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/).
3. **Nunca compres listas de correo electrónico.**

{% alert tip %}
Los equipos de éxito del cliente y capacidad de entrega de Braze pueden ayudarte a seguir las prácticas recomendadas para maximizar la capacidad de entrega en todo el mundo.
{% endalert %}

## Quitar una dirección de correo electrónico de tu lista de rebotes o correo no deseado {#remove-an-email-address-from-your-bounce-or-spam-list}

Puedes quitar los correos electrónicos rebotados y los correos electrónicos de tu lista de correo no deseado de Braze con los siguientes puntos de conexión:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)

## Mejorar la capacidad de entrega de correo electrónico {#improve-email-deliverability}

Para conocer las prácticas recomendadas para mejorar la capacidad de entrega de tu correo electrónico, consulta [Mejorar la capacidad de entrega de correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/).