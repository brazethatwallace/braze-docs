---
nav_title: Reporting
article_title: Content-Card-Reporting
page_order: 21
description: "Dieser Referenzartikel bietet eine Übersicht über die verschiedenen Content-Card-Reporting-Metriken und Analytics-Optionen, die im Braze-Dashboard verfügbar sind."
channel:
  - content cards
tool:
  - Reports

---

# Content-Card-Reporting {#content-card-reporting}

> Dieser Referenzartikel bietet eine Übersicht über die verschiedenen Content-Card-Reporting-Metriken und Analytics-Optionen, die im Braze-Dashboard verfügbar sind.

## Wann Sendungen protokolliert werden {#when-sends-are-logged}

Der Zeitpunkt eines _Gesendet_-Ereignisses für Content Cards hängt vom Zustellungstyp und der Einstellung **Kartenerstellung** ab.

### Geplante Zustellung {#scheduled-delivery}

Bei geplanten Content Cards hängt der Zeitpunkt eines _Gesendet_-Ereignisses von der Einstellung **Kartenerstellung** ab:

- **Beim Kampagnenstart:** Die Sendung wird zum geplanten Sendezeitpunkt protokolliert, wenn die Karte in den Feed der Nutzer:innen geschrieben wird. Dies geschieht unabhängig davon, ob die Nutzer:innen die App geöffnet oder die Karte angesehen haben.
- **Bei der ersten Impression:** Die Sendung wird protokolliert, wenn die App die Karte zum ersten Mal nach dem geplanten Sendezeitpunkt anfordert und die Karte on demand erstellt wird.

Wenn Ihre Kampagne auf **Bei der ersten Impression** (empfohlen) konfiguriert ist, steigt die Anzahl der _Gesendet_-Einträge in den Campaign-Analytics schrittweise an, wenn einzelne Apps die Karte anfordern. Wenn die App die Karte nie anfordert (z. B. wenn Nutzer:innen die App nie öffnen), bevor die Karte abläuft, wird keine Sendung erfasst und die Karte wird nie zugestellt. Wenn Ihre Kampagne auf **Beim Kampagnenstart** konfiguriert ist, steigt die Anzahl der _Gesendet_-Einträge in den Campaign-Analytics zum geplanten Zeitpunkt sprunghaft an.

### Aktionsbasierte Zustellung {#action-based-delivery}

Bei aktionsbasierten Content Cards wird die Sendung kurz nachdem die Nutzer:innen die auslösende Aktion ausgeführt haben protokolliert, wenn die Karte in ihren Feed geschrieben wird. Dies geschieht unabhängig davon, ob die Nutzer:innen die Karte angesehen haben.

### Filter „Campaigns erhalten“ und Retargeting {#campaigns-received-and-retargeting-filters}

Unabhängig vom Zustellungstyp oder der Einstellung **Kartenerstellung** erscheint eine Content-Card-Kampagne im Profil der Nutzer:innen unter **Campaigns erhalten** erst, nachdem sie die Karte tatsächlich in der App angesehen haben. Die Retargeting-Filter **Letzte Nachricht erhalten** und **Letzte Campaign erhalten** werden aus demselben Grund zum Zeitpunkt der Ansicht aktualisiert.

{% multi_lang_include analytics/campaign_analytics.md channel="Content Card" %}