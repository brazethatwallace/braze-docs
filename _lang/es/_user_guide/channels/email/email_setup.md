---
nav_title: "Configuración"
article_title: Configuración del correo electrónico
layout: dev_guide
page_order: 0
guide_top_header: "Configuración de correo electrónico"
guide_top_text: "Braze puede ayudarte a empezar a enviar campañas de correo electrónico. Sigue nuestras guías o consulta nuestro curso de <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>incorporación de correo electrónico</a> de Braze Learning."
page_type: landing
description: "Esta página de inicio incluye recursos para empezar con las campañas de correo electrónico, incluyendo la configuración de tus IP y dominios, el calentamiento de IP, la validación de correo electrónico y más."
channel: email

guide_featured_title: "Artículos de la sección"
guide_featured_list:
- name: "Configuración de IP y dominios"
  link: /docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains
  image: /assets/img/braze_icons/target-05.svg
- name: "Calentamiento de IP"
  link: /docs/user_guide/channels/email/email_setup/ip_warming
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "Validación del correo electrónico"
  link: /docs/user_guide/channels/email/email_setup/email_validation
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "Autenticación del correo electrónico"
  link: /docs/user_guide/channels/email/email_setup/authentication
  image: /assets/img/braze_icons/user-square.svg
- name: "Importa tu lista de correo electrónico"
  link: /docs/user_guide/channels/email/email_setup/import_your_email_list
  image: /assets/img/braze_icons/list.svg
- name: "Resumen de SSL"
  link: /docs/user_guide/channels/email/email_setup/ssl
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Consentimiento y recogida de direcciones"
  link: /docs/user_guide/channels/email/email_setup/consent_and_address_collection
  image: /assets/img/braze_icons/book-closed.svg
- name: "Problemas de capacidad de entrega y trampas de correo no deseado"
  link: /docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps
  image: /assets/img/braze_icons/alert-triangle.svg
- name: "Píxel de apertura y seguimiento de clics"
  link: /docs/user_guide/channels/email/email_setup/open_pixel_and_click_tracking
  image: /assets/img/braze_icons/cursor-click-02.svg
---

## Requisitos {#requirements}

Antes de empezar a enviar correos electrónicos, hay algunas cosas que necesitas. Consulta el siguiente cuadro para saber más sobre estos requisitos.

| Requisito | Descripción | Fuente |
|---|---|---|
| Una IP (protocolo de Internet) dedicada | Una IP dedicada es una dirección de Internet única proporcionada exclusivamente a una sola cuenta de alojamiento. | Braze te proporciona IP dedicadas para garantizar el control de la reputación del remitente de tu correo electrónico. La incorporación a Braze lo configurará por ti.|
| Dominios con etiqueta sin marca | Consisten en un dominio y un subdominio. Al usar la etiqueta sin marca, puedes pasar las comprobaciones de autenticación de correo electrónico para DKIM y SPF. | El equipo de incorporación de Braze generará estos dominios por ti, pero tú debes elegir sus nombres. |
| Subdominios | Se trata de una subdivisión de un dominio (como "@news.company.com") dentro de tu dirección de correo electrónico. Tener un subdominio evitará cualquier error que pueda dañar la reputación oficial del correo electrónico de tu empresa. | El equipo de incorporación lo generará por ti, pero tú debes decidir el nombre del subdominio. No puedes usar subdominios que actualmente se estén utilizando fuera de Braze. |
| Grupos de IP | Se trata de una configuración opcional que se utiliza para separar la reputación de los distintos tipos de correo electrónico (como "promocional" y "transaccional") para evitar que la reputación de uno afecte al otro y favorecer una mayor capacidad de entrega. | El equipo de incorporación configurará los grupos por ti. Luego, al redactar tu correo electrónico, puedes ver el grupo de IP de tu correo electrónico en el paso **Público objetivo**.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos" }

## Calentamiento de IP {#ip-warming}

{% alert important %}
El calentamiento de IP es el **paso más importante** en el proceso de configuración de correo electrónico. Aunque no es tu primer paso (en realidad es el último), lo mencionamos aquí para que sepas que debes calentar tu dirección IP, de lo contrario, cualquier correo electrónico que envíes se enviará a correo no deseado o estará sujeto a otras barreras de envío.
{% endalert %}

El [calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) consiste en enviar un número relativamente pequeño de correos electrónicos en tu primer lote y luego, con el tiempo, aumentar ligeramente el volumen en los lotes siguientes hasta alcanzar tu volumen diario habitual. Esto se hace al final del proceso de configuración de correo electrónico.

Al comenzar con volúmenes más pequeños de correo electrónico, estás estableciendo un nivel de confianza con tu proveedor de correo electrónico, demostrando que solo envías correos electrónicos a usuarios relevantes. Enviar tu primer lote de correos electrónicos a tus usuarios más comprometidos puede ayudarte a ganar confianza más rápido con tu proveedor.

Después de terminar el calentamiento de tu IP, puedes [empezar a crear y enviar correos electrónicos]({{site.baseurl}}/user_guide/channels/email/html_editor)!

## Correos electrónicos transaccionales legalmente obligatorios {#legally-required-transactional-emails}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

<br><br>