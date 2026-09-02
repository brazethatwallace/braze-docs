---
nav_title: Über Tracking-Daten
article_title: Über Tracking-Daten von Landing-Pages
description: "Erfahren Sie mehr über Tracking und anonymisierte Daten für Landing-Pages in Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# Über Tracking-Daten von Landing-Pages {#about-landing-page-tracking-data}

> Erfahren Sie mehr über Tracking und anonymisierte Daten für Landing-Pages in Braze.

## Tracking-Methoden {#tracking-methods}

### Web SDK or Software-Development-Kit {#web-sdk}

Das Braze Web SDK or Software-Development-Kit wird initialisiert, wenn ein:e Nutzer:in ein Formular auf einer Landing-Page absendet. Vor dem Absenden des Formulars werden keine personenbezogenen Daten erfasst, und das SDK or Software-Development-Kit trackt Nutzer:innen nicht aktiv. Nach Abschluss der Initialisierung speichert das SDK or Software-Development-Kit keine Daten im Browser (wie Cookies, lokalen Speicher oder andere).

Das Braze Web SDK or Software-Development-Kit wird sofort initialisiert, wenn ein:e Nutzer:in über einen Link, der durch einen {% raw %}`{% landing_page_url %}`{% endraw %} Liquid-Tag in einer Braze-Nachricht generiert wurde, zur Landing-Page navigiert.

Beim Absenden eines Formulars erfasst das SDK or Software-Development-Kit die folgenden Daten:

- Formularübermittlungsereignis (Name des Ereignisses und Zeitpunkt der Übermittlung)
- Von Ihrem Team im Formular angegebene Daten (wie Name, E-Mail und Telefonnummer)
- Startzeit der Sitzung
- Geräte-ID (eine eindeutige ID, die für das Gerät generiert, aber nicht gespeichert wird)
- Land, ermittelt anhand der IP-Adresse

### Anonymisierte Daten {#anonymized-data}

Bevor ein:e Nutzer:in ein Formular absendet, bestehen die auf einer Landing-Page erfassten Daten ausschließlich aus anonymisierten, nicht identifizierbaren Informationen. Diese umfassen standardmäßige aggregierte Website-Metriken wie die Anzahl der Seitenaufrufe (Impressionen) und Klicks, die eine Landing-Page erhält.

Da diese Daten nicht mit identifizierbaren Nutzer:innen verknüpft sind, können sie nicht verwendet werden, um individuelles Nutzerverhalten zu retargeten oder zu tracken.

## Zusammenführen doppelter Nutzerprofile {#merging-duplicate-user-profiles}

Braze führt Nutzer:innen nicht automatisch anhand von Attributen wie E-Mail oder Telefonnummer zusammen, wenn ein Landing-Page-Formular abgesendet wird. Wenn ein Formular mit einer E-Mail oder Telefonnummer abgesendet wird, die mit einem bestehenden Kundenprofil or Nutzerprofil übereinstimmt, erstellt Braze ein separates Kundenprofil or Nutzerprofil.

Um doppelte Nutzerprofile zusammenzuführen, können Sie:

- Den [`/users/merge`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) Trigger or triggern or triggern, wenn ein Landing-Page-Formular abgesendet wird, um das neue Profil mit einem bestehenden Profil zusammenzuführen.
- [Massenzusammenführung]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#bulk-merging) planen, um doppelte Profile regelmäßig anhand übereinstimmender Bezeichner zusammenzuführen.