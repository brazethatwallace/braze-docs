---
nav_title: Shopify Übersicht
article_title: Shopify Übersicht
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Shopify, einem globalen Handelsunternehmen, die es Ihnen erlaubt, Ihren Shopify-Shop nahtlos mit Braze zu verbinden, um ausgewählte Shopify-Webhooks an Braze weiterzugeben. Nutzen Sie die kanalübergreifenden Strategien von Braze und Canvas, um Kund:innen zum Abschluss ihrer Käufe zu bewegen oder Nutzer:innen auf der Grundlage ihrer früheren Käufe erneut anzusprechen."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Shopify-Übersicht {#shopify-overview}

> [Shopify](https://www.shopify.com/) ist ein weltweit führendes Handelsunternehmen, das zuverlässige Tools für die Gründung, das Wachstum, das Marketing und die Verwaltung von Unternehmen jeder Größe bereitstellt. Shopify macht den Handel für alle besser – mit einer Plattform und Diensten, die auf Zuverlässigkeit ausgelegt sind und Verbraucher:innen überall ein besseres Einkaufserlebnis bieten.

Die Integration von Braze in Shopify bietet eine leistungsstarke Lösung für E-Commerce-Unternehmen, die ihr Customer-Engagement verbessern und personalisiertes Marketing betreiben möchten. Diese Integration verbindet die robusten E-Commerce-Funktionen von Shopify nahtlos mit unserer fortschrittlichen Customer-Engagement-Plattform und ermöglicht es Ihnen, Ihren Nutzer:innen gezielte, relevante und zeitnahe Nachrichten auf der Grundlage von Realtime-Einkaufsverhalten und Transaktionsdaten zuzustellen.

## Anforderungen {#requirements}

| Anforderung | Beschreibung |
| --- | --- |
| Shopify-Shop | Sie haben einen aktiven Shopify-Shop. |
| Shopify-Shop-Inhaber:in oder Mitarbeiter:innen-Berechtigungen | {::nomarkdown}<ul><li>Zugriff auf alle allgemeinen und Online-Shop-Einstellungen.</li><li> Zusätzliche Admin-Berechtigungen:<ul><li>Bestellungen: Anzeigen</li><li>Kund:in: Lesen/Schreiben</li><li>Kundenereignisse anzeigen (Web Pixels)</li><li>Einstellungen verwalten</li><li>Von Mitarbeiter:innen/Mitarbeitenden entwickelte Apps anzeigen</li><li>Apps und Kanäle verwalten/installieren</li><li>Angepasste Pixels verwalten/hinzufügen</li></ul></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## So integrieren Sie {#how-to-integrate}

Braze bietet Shopify-Händlern zwei Integrationsoptionen, die auf die vielfältigen Anforderungen von E-Commerce-Unternehmen zugeschnitten sind: **Standardintegration** und **Angepasste Integration**.

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

## So funktioniert die Integration {#how-the-integration-works}

Wenn Sie die [historische Nachfüllung]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) in Ihren Konfigurationseinstellungen bereits eingerichtet und aktiviert haben, beginnt die erste Datensynchronisierung sofort.

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

Nach der ersten Datensynchronisierung verfolgt Braze kontinuierlich neue Daten und Aktualisierungen direkt von Shopify und Braze SDKs.

{% alert note %}
Wenn Sie bereits Braze-Kund:in sind und aktive Campaigns oder Canvases haben, lesen Sie [Shopify historische Nachfüllung]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) für wichtige Informationen. Um zu sehen, welche spezifischen Kundendaten nachgefüllt werden, lesen Sie [Shopify-Features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).
{% endalert %}

### Nutzer:innen- und Datensynchronisierung {#user-and-data-syncing}

Nachdem die Integration aktiv ist, erfasst Braze Nutzerdaten aus zwei Hauptquellen über die Shopify-Integration:
- **Shopify Web Pixel API und App-Einbettungen:** Dies betreibt das Braze Web SDK und JavaScript SDK zur Unterstützung von On-Site-Tracking, Identitätsverwaltung, E-Commerce-Verhaltensdaten und Messaging-Kanälen wie In-App-Nachrichten.
- **Shopify-Webhooks:** E-Commerce-Verhaltensdaten, Produktsynchronisierung und Abonnent:innen-Erfassung

Während des Integrations-Onboardings müssen Sie auswählen, wann die Braze SDKs initialisiert und Ihre Shopify-Website geladen werden:
- Beim Website-Besuch (z. B. Sitzungsstart)
    - **Was es bewirkt:** Verfolgt anonyme Nutzer:innen – wie Gast-Käufer:innen – um auf mehr Daten für tiefere Personalisierung zuzugreifen
- Bei der Kontoregistrierung (z. B. Kontoanmeldung)
    - **Was es bewirkt:** Verhindert anonymes Nutzer:innen-Tracking für einen konservativeren, datenschutzorientierten Ansatz, sodass Nutzer:innenaktivitäten erst *nach* der Anmeldung im Konto verfolgt werden

{% alert note %}
- Website-Besuche (Sitzungen) werden auf Ihre monatlich aktive Nutzer:innen (MAU)-Kontingente angerechnet.
- Die Versionen des Braze Web SDK und JavaScript SDK werden automatisch auf v6.8.0 gesetzt. Sie können Ihre SDK-Version jederzeit über die Integrationseinstellungen aktualisieren.
{% endalert %}

Braze nutzt die Shopify-Integration zur Unterstützung mehrerer Bezeichner, die Ihre Nutzer:innen von ihrem Gast-Einkaufserlebnis bis hin zu identifizierten Nutzer:innen verfolgen:

| Braze-Bezeichner | Beschreibung |
| --- | --- |
| Braze `device_id` | Eine zufällig generierte ID, die im Browser gespeichert wird und anonyme Nutzer:innenaktivitäten über Braze SDKs verfolgt. |
| Warenkorb-Token-Nutzer-Alias | Ein Alias, den Braze erstellt, um Warenkorb-Aktualisierungsereignisse zu verfolgen. Dieses Token wird mithilfe des Shopify-Warenkorb-Tokens erstellt. |
| Checkout-Token-Nutzer-Alias | Ein Alias, den Braze erstellt, wenn Nutzer:innen den Checkout-Prozess starten. Dieses Token wird mithilfe des Shopify-Checkout-Tokens erstellt.<br><br> Wenn Kund:innen Shop Pay als beschleunigte Checkout-Option verwenden, kann Shopify bestimmte Standard-Checkout-Ereignisse umgehen und verhindern, dass Braze die Daten erhält, die zum Hinzufügen des Checkout-Token-Alias benötigt werden. |
| Shopify-Kunden-ID-Alias | Die Shopify-Kunden-ID wird als Alias zugewiesen, wenn die externe ID bei der Kontoanmeldung zugewiesen wird oder wenn eine Bestellung aufgegeben wird. |
| Braze `external_id` | Ein eindeutiger Bezeichner, der hilft, Kund:innen geräte- und plattformübergreifend zu verfolgen. Dies sorgt für ein konsistentes Nutzererlebnis und verbessert die Analytics, indem mehrere Profile verhindert werden, wenn Nutzer:innen das Gerät wechseln oder die App neu installieren.<br><br>Die Shopify-Integration unterstützt die folgenden `external_id`-Typen: <br><br>{::nomarkdown}<ul><li>Shopify-Kunden-ID (Standard)</li><li>Benutzerdefinierte externe ID</li><li>Gehashte E-Mail (SHA-256)</li><li>Gehashte E-Mail (SHA-1)</li><li>Gehashte E-Mail (MD5)</li><li>E-Mail</li></ul>{:/}Braze weist Ihren Nutzer:innen eine `external_id` zu, indem die changeUser-Methode innerhalb der SDKs aufgerufen wird, wenn: <br><br>{::nomarkdown}<ul><li>Nutzer:innen sich anmelden oder ein Konto erstellen</li><li>Eine Bestellung aufgegeben wird</li></ul>{:/}<br> Weitere Informationen darüber, was passiert, wenn Sie einem anonymen Profil eine `external_id` zuweisen, finden Sie unter [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>Braze nutzt die `external_id` auch, um nachgelagerte E-Commerce-Verhaltensdaten aus Shopify-Webhooks zuzuordnen.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen- und Datensynchronisierung" }

Die Integration erfordert, dass Braze SDKs und Shopify-Dienste zusammenarbeiten, um Shopify-Daten in nahezu Realtime angemessen zu verfolgen und den richtigen Nutzer:innen zuzuordnen. Weitere Details zu den über die Integration verfolgten Daten finden Sie unter [Shopify-Daten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

{% alert note %}
- Wenn Sie die Integration testen, empfehlen wir Ihnen, den Inkognito-Modus zu verwenden oder Ihre Cookies zu löschen, um die Braze `device_id` zurückzusetzen und das Verhalten anonymer Nutzer:innen zu simulieren.
- Obwohl eine Shopify-Kunden-ID generiert wird, wenn eine E-Mail-Adresse in die Shopify-Newsletter-Fußzeile eingegeben oder während des Checkout-Prozesses vor einer Bestellung erfasst wird, ist diese Kunden-ID nicht über Shopify Web Pixels zugänglich. Aus diesem Grund kann Braze die `changeUser`-Methode in diesen beiden Situationen nicht verwenden.
{% endalert %}

### Synchronisierung von Shopify E-Mail- und SMS-Marketing-Opt-ins {#syncing-shopify-email-and-sms-marketing-opt-ins}

Wenn Sie die Abonnent:innen-Erfassung in Ihren Konfigurationseinstellungen aktivieren, müssen Sie für jeden Shop, den Sie mit Braze verbinden, eine Abo-Gruppe zuweisen. Das bedeutet, dass Ihre Kund:innen entweder als „abonniert“ oder „abgemeldet“ in der Abo-Gruppe Ihres Shops kategorisiert werden.

Der Shopify-Marketing-Opt-in-Status für E-Mail- und SMS-Marketing kann auf folgende Weise aktualisiert werden:
- **Manuelle Aktualisierung:** Sie können den E-Mail- oder SMS-Marketing-Opt-in-Status von Nutzer:innen manuell in Ihrem Shopify-Admin ändern.
- **Shopify-Newsletter-Fußzeile:** Wenn Nutzer:innen ihre E-Mail-Adresse in die Standard-Newsletter-Fußzeile von Shopify eingeben, wird ihr Opt-in-Status aktualisiert.
- **Checkout:** Die Einwilligung der Nutzer:innen wird beim Checkout erfasst, wenn sie das Marketing-Kontrollkästchen auswählen und den Checkout fortsetzen, indem sie **Pay now** beim einseitigen Checkout oder **Continue to shipping** beim dreiseitigen Checkout auswählen.

{% alert note %}
Der E-Mail-Marketing-Opt-in-Status von Shopify ändert nicht den [globalen E-Mail-Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions) von Nutzer:innen in Braze. Der Standard-Abo-Status bei der Erstellung eines Nutzerprofils ist „subscribed“. Denken Sie daran, die Abo-Gruppe als Teil Ihrer Campaign- oder Canvas-Eintrittskriterien zu verwenden.
{% endalert %}

Diese Tabelle zeigt, welche Shopify-Marketing-Opt-in-Status mit den Status in Ihrer Braze-Abo-Gruppe korrelieren.

| Shopify-Marketing-Opt-in-Status | Braze-Abo-Gruppen-Status |
| --- | --- |
| E-Mail ist abonniert | Subscribed |
| E-Mail ist abgemeldet | Unsubscribed |
| E-Mail wartet auf Bestätigung | Unsubscribed |
| E-Mail ist ungültig | Unsubscribed |
| SMS abonniert | Subscribed |
| SMS abgemeldet | Unsubscribed |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Synchronisierung von Shopify E-Mail- und SMS-Marketing-Opt-ins" }

### Registrierungsformulare {#sign-up-forms}

#### Shopify-Newsletter-Fußzeile {#shopify-newsletter-footer}

Nutzer:innen, die ihre E-Mail-Adresse in die Shopify-Newsletter-Fußzeile eingeben, durchlaufen einen der folgenden Workflows:

##### Nutzer:innen, die sich nicht in ihrem Konto angemeldet haben {#users-who-havent-logged-into-their-account}

1. Braze empfängt einen eingehenden Shopify-Webhook, wenn Kund:innen erstellt oder aktualisiert werden.
2. Braze erstellt ein Nutzerprofil mit der E-Mail-Adresse und dem Shopify-Kunden-ID-Alias, die mit diesen Nutzer:innen verknüpft sind.
3. Das Braze SDK aktualisiert das anonyme Profil mit der E-Mail-Adresse.

{% alert note %}
Dies kann zu einem doppelten Profil führen, bis sich die Nutzer:innen identifizieren, indem sie ein Konto erstellen, sich in ihr Konto einloggen oder eine Bestellung aufgeben. Braze bietet Werkzeuge zur Massenzusammenführung, um die Bereinigung doppelter Profile zu automatisieren. Weitere Details finden Sie unter [Doppelte Nutzer:innen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).
{% endalert %}

##### Nutzer:innen, die sich bereits in ihrem Konto angemeldet haben {#users-who-have-already-logged-into-their-account}

Braze erstellt ein Nutzerprofil mit der E-Mail-Adresse und dem Shopify-Kunden-ID-Alias, die mit diesen Nutzer:innen verknüpft sind. Braze aktualisiert die E-Mail-Adresse der angemeldeten Nutzer:innen nicht, da wir davon ausgehen, dass Shopify diese Informationen bereits bereitgestellt hat.

#### Braze-Registrierungsformulare {#braze-sign-up-forms}

Braze bietet zwei Arten von Registrierungsformular-Templates:
- **[E-Mail-Registrierungsformulare]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/email_capture):** Erstellen Sie diese mit dem Drag-and-Drop-Editor.
- **[Traditionelles Editor-E-Mail-Erfassungsformular]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form):** Ein einfacheres Formular zur Erfassung von E-Mail-Adressen.

Wenn Sie diese Registrierungsformular-Templates verwenden, aktualisiert Braze automatisch den globalen E-Mail-Abo-Status im Nutzerprofil. Weitere Details zur Handhabung des globalen E-Mail-Abo-Status, einschließlich Informationen zur E-Mail-Validierung, finden Sie in der Dokumentation für den jeweiligen Formular-Template-Typ.

{% alert note %}
- Stellen Sie sicher, dass Sie Eintrittskriterien in Ihre Campaign oder Ihr Canvas aufnehmen, die sowohl den globalen E-Mail-Abo-Status als auch die Abo-Gruppe umfassen, die mit Ihrem Shopify-Shop verbunden sind. Dies hilft sicherzustellen, dass Sie die richtige Zielgruppe ansprechen.
- Braze erfasst Besucher:inneninformationen wie E-Mail-Adressen und Telefonnummern über In-Browser-Nachrichten. Diese Informationen werden dann an die Shopify Visitor API gesendet, erstellen aber kein Kundenprofil in Shopify. Weitere Details finden Sie unter [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Registrierungsformulare von Drittanbietern {#third-party-sign-up-forms}

Wenn Sie eine Drittanbieter-Plattform oder ein Shopify-Plugin für Ihre Registrierungsformulare verwenden, müssen Sie mit Ihren Entwickler:innen zusammenarbeiten, um Braze SDK-Code zu integrieren, der die E-Mail-Adresse und den globalen E-Mail-Abo-Status aus Formularübermittlungen erfasst. Weitere Informationen finden Sie unter [Shopify-Standard-Integrationseinrichtung]({{site.baseurl}}/shopify_standard_integration) und [Shopify-benutzerdefinierte Integrationseinrichtung]({{site.baseurl}}/shopify_custom_integration).

### Produktsynchronisierung {#product-syncing}

Braze unterstützt die Möglichkeit, die Produkte Ihres Shopify-Shops in einen Braze-Katalog zu synchronisieren. Weitere Details finden Sie unter [Shopify-Produktsynchronisierungen]({{site.baseurl}}/shopify_catalogs).

## Anfragen betroffener Personen {#data-subject-requests}

Im Rahmen der Shopify-Integration der Braze-Plattform empfängt Braze automatisch [Shopifys Compliance-Webhooks](https://shopify.dev/docs/apps/build/privacy-law-compliance/). Da jedoch die Kund:innen die Datenverantwortlichen für die Daten ihrer Endnutzer:innen sind, müssen Kund:innen alle erforderlichen Maßnahmen ergreifen, um Anfragen betroffener Personen in Bezug auf Endnutzer:innen-Daten in Braze (einschließlich über die Shopify-Integration empfangener Endnutzer:innen-Daten) zu bearbeiten. Weitere Informationen finden Sie in unserer Dokumentation zur [technischen Unterstützung beim Datenschutz]({{site.baseurl}}/dp-technical-assistance).