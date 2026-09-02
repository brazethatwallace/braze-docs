---
nav_title: Präferenzzentrum
article_title: Präferenzzentrum
page_order: 8
layout: dev_guide
guide_top_header: "Präferenzzentrum"
guide_top_text: "Ein E-Mail-Präferenzzentrum ermöglicht es Nutzer:innen, ihre Benachrichtigungspräferenzen für E-Mail-Campaigns und Newsletter über eine gebrandete Seite in Ihrer App oder auf Ihrer Website zu verwalten. Lesen Sie diese Artikel, um zu erfahren, wie Sie ein Präferenzzentrum mit der <a href='/docs/api/endpoints/preference_center'>Braze-Präferenzzentrum-API</a> oder dem Drag-and-Drop-Editor erstellen und verwalten können, einschließlich Abo-Gruppen, Opt-in-Status und Anpassung der gehosteten Seite."
description: "Diese Landing-Page enthält Artikel zum Braze E-Mail-Präferenzzentrum und zur Verwendung der Präferenzzentrum-API."
channel:
  - email

guide_featured_title: "Artikel in diesem Abschnitt"
guide_featured_list:
- name: API-E-Mail-Präferenzzentrum
  link: /docs/user_guide/audience/subscription_preferences/preference_center/api_preference_center
  image: /assets/img/braze_icons/list.svg
- name: Drag-and-Drop-E-Mail-Präferenzzentrum
  link: /docs/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center
  image: /assets/img/braze_icons/mail-01.svg

---

{% multi_lang_include alerts/tip_alerts.md alert="Landing pages manage subscriptions" %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was ist ein E-Mail-Präferenzzentrum? {#what-is-an-email-preference-center}

Ein E-Mail-Präferenzzentrum ist eine gehostete Seite, auf der Nutzer:innen ihren E-Mail-Abo-Status Update or aktualisieren or aktualisieren und Nachrichtenkategorien auswählen können. Braze unterstützt API-basierte und Drag-and-Drop-Präferenzzentren.

### Sollte ich die Präferenzzentrum-API oder den Drag-and-Drop-Editor verwenden? {#should-i-use-the-preference-center-api-or-the-drag-and-drop-editor}

Verwenden Sie das [Drag-and-Drop-E-Mail-Präferenzzentrum]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center) für eine schnellere Einrichtung mit weniger Code. Verwenden Sie das [API-E-Mail-Präferenzzentrum]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/api_preference_center), wenn Sie die volle Kontrolle über Layout, Hosting und angepasste Logik benötigen.