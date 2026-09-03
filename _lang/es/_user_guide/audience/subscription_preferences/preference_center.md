---
nav_title: Centro de preferencias
article_title: Centro de preferencias
page_order: 8
layout: dev_guide
guide_top_header: "Centro de preferencias"
guide_top_text: "Un centro de preferencias de correo electrónico permite a los usuarios gestionar sus preferencias de notificación para campañas de correo electrónico y boletines informativos desde una página con tu marca en tu aplicación o sitio web. Consulta estos artículos para crear y administrar un centro de preferencias con la <a href='/docs/api/endpoints/preference_center'>API del centro de preferencias de Braze</a> o el editor de arrastrar y soltar, incluyendo grupos de suscripción, estados de adhesión voluntaria y personalización de páginas alojadas."
description: "Esta página de destino incluye artículos sobre el centro de preferencias de correo electrónico de Braze y cómo usar la API del centro de preferencias."
channel:
  - email

guide_featured_title: "Artículos de la sección"
guide_featured_list:
- name: Centro de preferencias de correo electrónico con API
  link: /docs/user_guide/audience/subscription_preferences/preference_center/api_preference_center
  image: /assets/img/braze_icons/list.svg
- name: Centro de preferencias de correo electrónico con arrastrar y soltar
  link: /docs/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center
  image: /assets/img/braze_icons/mail-01.svg

---

{% multi_lang_include alerts/tip_alerts.md alert="Landing pages manage subscriptions" %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué es un centro de preferencias de correo electrónico? {#what-is-an-email-preference-center}

Un centro de preferencias de correo electrónico es una página alojada donde los usuarios actualizan el estado de su suscripción de correo electrónico y eligen categorías de mensajes. Braze admite centros de preferencias creados con API y con el editor de arrastrar y soltar.

### ¿Debo usar la API del centro de preferencias o el editor de arrastrar y soltar? {#should-i-use-the-preference-center-api-or-the-drag-and-drop-editor}

Usa el [centro de preferencias de correo electrónico con arrastrar y soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center) para una configuración más rápida con menos código. Usa el [centro de preferencias de correo electrónico con API]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/api_preference_center) cuando necesites control total sobre el diseño, el alojamiento y la lógica personalizada.