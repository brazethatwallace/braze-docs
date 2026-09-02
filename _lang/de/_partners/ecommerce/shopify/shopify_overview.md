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
| Berechtigungen als Shopify-Shop-Inhaber:in oder Mitarbeiter:in | {::nomarkdown}<ul><li>Zugriff auf alle Allgemeinen und Online-Shop-Einstellungen.</li><li> Zusätzliche Admin-Berechtigungen:<ul><li>Bestellungen: Anzeigen</li><li>Kund:innen: Lesen/Schreiben</li><li>Kundenereignisse anzeigen (Web Pixels)</li><li>Einstellungen verwalten</li><li>Von Mitarbeiter:innen/Kollaborateur:innen entwickelte Apps anzeigen</li><li>Apps und Kanäle verwalten/installieren</li><li>Angepasste Pixels verwalten/hinzufügen</li></ul></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## Integration {#how-to-integrate}

Braze bietet zwei Integrationsoptionen für Shopify-Händler, die auf die unterschiedlichen Anforderungen von E-Commerce-Unternehmen zugeschnitten sind: **Standard-Integration** und **Angepasste Integration**.

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

## Funktionsweise der Integration {#how-the-integration-works}

Wenn Sie den [historischen Backfill]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) in Ihren Konfigurationseinstellungen bereits eingerichtet und aktiviert haben, beginnt die initiale Datensynchronisierung sofort.

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

Nach der initialen Datensynchronisierung wird Braze kontinuierlich neue Daten und Aktualisierungen direkt von Shopify und den Braze SDKs erfassen.

{% alert note %}
Wenn Sie bereits Braze-Kund:in sind und aktive Campaigns oder Canvases betreiben, lesen Sie bitte [Shopify historischer Backfill]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) für wichtige Informationen. Welche spezifischen Kundendaten zurückgefüllt werden, erfahren Sie unter [Shopify-Features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).
{% endalert %}

### Nutzer:innen- und Datensynchronisierung {#user-and-data-syncing}

Nachdem die Integration aktiv ist, sammelt Braze Nutzerdaten aus zwei Hauptquellen über die Shopify-Integration:
- **Shopify Web Pixel API und App-Embeds:** Dies ermöglicht das Braze Web SDK und JavaScript SDK für On-Site-Tracking, Identitätsverwaltung, E-Commerce-Verhaltensdaten und Messaging-Kanäle wie In-App Messages.
- **Shopify-Webhooks:** E-Commerce-Verhaltensdaten, Produktsynchronisierung und Abonnent:innen-Erfassung

Während des Integrations-Onboardings müssen Sie festlegen, wann die Braze SDKs auf Ihrer Shopify-Website initialisiert und geladen werden:
- Beim Seitenbesuch (z. B. Sitzungsbeginn)
    - **Was es bewirkt:** Trackt anonyme Nutzer:innen – wie Gastbesucher:innen – um mehr Daten für tiefere Personalisierung zu erfassen
- Bei der Kontoregistrierung (z. B. Kontoanmeldung)
    - **Was es bewirkt:** Verhindert anonymes Nutzer:innen-Tracking für einen konservativeren, datenschutzorientierten Ansatz, sodass Nutzeraktivitäten erst *nach* der Anmeldung im Konto getrackt werden

{% alert note %}
- Website-Besuche (Sitzungen) zählen zu Ihren MAU-Kontingenten (monatlich aktive Nutzer:innen).
- Die Versionen des Braze Web SDK und JavaScript SDK werden automatisch auf v6.8.0 gesetzt. Sie können Ihre SDK-Version jederzeit in den Integrationseinstellungen aktualisieren.
{% endalert %}

Braze nutzt die Shopify-Integration zur Unterstützung mehrerer Bezeichner, die Ihre Nutzer:innen von ihrem Gast-Shopping-Erlebnis bis zur Identifizierung als bekannte Nutzer:innen verfolgen:

| Braze-Bezeichner | Beschreibung |
| --- | --- |
| Braze `device_id` | Eine zufällig generierte ID, die im Browser gespeichert wird und anonyme Nutzeraktivitäten über Braze SDKs verfolgt. |
| Warenkorb-Token / Textbaustein-Nutzer-Alias | Ein Alias, den Braze erstellt, um Warenkorb-Aktualisierungsereignisse zu verfolgen. Dieses Token / Textbaustein wird mithilfe des Shopify-Warenkorb-Tokens erstellt. |
| Checkout-Token / Textbaustein-Nutzer-Alias | Ein Alias, den Braze erstellt, wenn Nutzer:innen den Checkout-Prozess starten. Dieses Token / Textbaustein wird mithilfe des Shopify-Checkout-Tokens erstellt.<br><br> Wenn Kund:innen Shop Pay als beschleunigten Checkout verwenden, kann Shopify bestimmte standardmäßige Checkout-Ereignisse überspringen und verhindern, dass Braze die für das Hinzufügen des Checkout-Token / Textbaustein-Alias erforderlichen Daten erhält. |
| Shopify-Kunden-ID-Alias | Die Shopify-Kunden-ID wird als Alias zugewiesen, wenn die externe ID bei der Kontoanmeldung oder bei einer Bestellung vergeben wird. |
| Braze `external_id` | Ein eindeutiger Bezeichner, der dabei hilft, Kund:innen über Geräte und Plattformen hinweg zu verfolgen. Dies sorgt für ein konsistentes Nutzererlebnis und verbessert Analytics, indem mehrfache Profile verhindert werden, wenn Nutzer:innen Geräte wechseln oder die App neu installieren.<br><br>Die Shopify-Integration unterstützt die folgenden `external_id`-Typen: <br><br>{::nomarkdown}<ul><li>Shopify-Kunden-ID (Standard)</li><li>Angepasste externe ID</li><li>Gehashte E-Mail (SHA-256)</li><li>Gehashte E-Mail (SHA-1)</li><li>Gehashte E-Mail (MD5)</li><li>E-Mail</li></ul>{:/}Braze weist Ihren Nutzer:innen eine `external_id` zu, indem die changeUser-Methode innerhalb der SDKs aufgerufen wird, wenn: <br><br>{::nomarkdown}<ul><li>Nutzer:innen sich anmelden oder ein Konto erstellen</li><li>Eine Bestellung aufgegeben wird</li></ul>{:/}<br> Weitere Informationen dazu, was passiert, wenn Sie einem anonymen Profil eine `external_id` zuweisen, finden Sie unter [Kundenprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>Braze nutzt die `external_id` außerdem, um nachgelagerte E-Commerce-Verhaltensdaten aus Shopify-Webhooks zuzuordnen.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen- und Datensynchronisierung" }

Die Integration erfordert, dass Braze SDKs und Shopify-Dienste zusammenarbeiten, um Shopify-Daten nahtlos den richtigen Nutzer:innen nahezu in Echtzeit zuzuordnen. Weitere Details zu den über die Integration getrackten Daten finden Sie unter [Shopify-Daten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

{% alert note %}
- Wenn Sie die Integration testen, empfehlen wir Ihnen, den Inkognito-Modus zu verwenden oder Ihre Cookies zu löschen, um die Braze `device_id` zurückzusetzen und das Verhalten anonymer Nutzer:innen zu simulieren.
- Obwohl eine Shopify-Kunden-ID generiert wird, wenn eine E-Mail-Adresse in die Shopify-Newsletter-Fußzeile eingegeben oder während des Checkout-Prozesses vor einer Bestellung erfasst wird, ist diese Kunden-ID über Shopify Web Pixels nicht zugänglich. Aus diesem Grund kann Braze die `changeUser`-Methode in diesen beiden Situationen nicht verwenden.
{% endalert %}

### Synchronisierung von Shopify E-Mail- und SMS-Marketing-Opt-ins {#syncing-shopify-email-and-sms-marketing-opt-ins}

Wenn Sie die Abonnent:innen-Erfassung in Ihren Konfigurationseinstellungen aktivieren, müssen Sie für jeden Shop, den Sie mit Braze verbinden, eine Abo-Gruppe zuweisen. Das bedeutet, dass Ihre Kund:innen entweder als „subscribed“ oder „unsubscribed“ in der Abo-Gruppe Ihres Shops kategorisiert werden.

Der Shopify Marketing-Opt-in-Status für E-Mail- und SMS-Marketing kann auf folgende Weise aktualisiert werden:
- **Manuelle Aktualisierung:** Sie können den E-Mail- oder SMS-Marketing-Opt-in-Status von Nutzer:innen manuell in Ihrem Shopify-Admin ändern.
- **Shopify-Newsletter-Fußzeile:** Wenn Nutzer:innen ihre E-Mail-Adresse in die Standard-Newsletter-Fußzeile von Shopify eingeben, wird ihr Opt-in-Status aktualisiert.
- **Checkout:** Die Zustimmung wird beim Checkout erfasst, wenn Nutzer:innen das Marketing-Kontrollkästchen aktivieren und den Checkout fortsetzen, indem sie beim einseitigen Checkout **Pay now** oder beim dreiseitigen Checkout **Continue to shipping** auswählen.

{% alert note %}
Der E-Mail-Marketing-Opt-in-Status von Shopify ändert nicht den [globalen E-Mail-Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions) in Braze. Der standardmäßige Abo-Status bei der Erstellung eines Nutzerprofils ist „subscribed“. Denken Sie daran, die Abo-Gruppe als Teil Ihrer Campaign- oder Canvas-Eintrittskriterien zu verwenden.
{% endalert %}

Diese Tabelle zeigt, welche Shopify-Marketing-Opt-in-Status mit den Statuswerten in Ihrer Braze-Abo-Gruppe korrelieren.

| Shopify-Marketing-Opt-in-Status | Braze-Abo-Gruppenstatus |
| --- | --- |
| E-Mail ist subscribed | Subscribed |
| E-Mail ist unsubscribed | Unsubscribed |
| E-Mail wartet auf Bestätigung | Unsubscribed |
| E-Mail ist ungültig | Unsubscribed |
| SMS subscribed | Subscribed |
| SMS unsubscribed | Unsubscribed |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Synchronisierung von Shopify E-Mail- und SMS-Marketing-Opt-ins" }

### Registrierungsformulare {#sign-up-forms}

#### Shopify-Newsletter-Fußzeile {#shopify-newsletter-footer}

Nutzer:innen, die ihre E-Mail-Adresse in die Shopify-Newsletter-Fußzeile eingeben, durchlaufen einen der folgenden Workflows:

##### Nutzer:innen, die nicht in ihrem Konto angemeldet sind {#users-who-havent-logged-into-their-account}

1. Braze empfängt einen eingehenden Shopify-Webhook, wenn Kund:innen erstellt oder aktualisiert werden.
2. Braze erstellt ein Kundenprofil mit der E-Mail-Adresse und dem Shopify-Kunden-ID-Alias, die mit diesen Nutzer:innen verknüpft sind.
3. Das Braze SDK aktualisiert das anonyme Profil mit der E-Mail-Adresse.

{% alert note %}
Dies kann zu einem doppelten Profil führen, bis sich die Nutzer:innen identifizieren, indem sie ein Konto erstellen, sich anmelden oder eine Bestellung aufgeben. Braze bietet Bulk-Zusammenführungstools, die Ihnen helfen, die Bereinigung doppelter Profile zu automatisieren. Weitere Details finden Sie unter [Doppelte Nutzer:innen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).
{% endalert %}

##### Nutzer:innen, die bereits in ihrem Konto angemeldet sind {#users-who-have-already-logged-into-their-account}

Braze erstellt ein Kundenprofil mit der E-Mail-Adresse und dem Shopify-Kunden-ID-Alias, die mit diesen Nutzer:innen verknüpft sind. Braze aktualisiert die E-Mail-Adresse der angemeldeten Nutzer:innen nicht, da wir davon ausgehen, dass Shopify diese Information bereits bereitgestellt hat.

#### Braze-Registrierungsformulare {#braze-sign-up-forms}

Braze bietet zwei Arten von Registrierungsformular-Templates:
- **[E-Mail-Registrierungsformulare]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/email_capture):** Erstellen Sie diese mit dem Drag-and-Drop-Editor.
- **[E-Mail-Erfassungsformular im klassischen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form):** Ein einfacheres Formular zur Erfassung von E-Mail-Adressen.

Wenn Sie diese Registrierungsformular-Templates verwenden, aktualisiert Braze automatisch den globalen E-Mail-Abo-Status im Kundenprofil. Weitere Details zur Handhabung des globalen E-Mail-Abo-Status, einschließlich Informationen zur E-Mail-Validierung, finden Sie in der Dokumentation für den jeweiligen Formular-Template-Typ.

{% alert note %}
- Stellen Sie sicher, dass die Eintrittskriterien Ihrer Campaign oder Ihres Canvas sowohl den globalen E-Mail-Abo-Status als auch die Abo-Gruppe enthalten, die mit Ihrem Shopify-Shop verbunden sind. Dies hilft sicherzustellen, dass Sie die richtige Zielgruppe ansprechen.
- Braze erfasst Besucher:innen-Informationen wie E-Mail-Adressen und Telefonnummern über In-Browser-Nachrichten. Diese Informationen werden dann an die Shopify Visitor API gesendet, erstellen jedoch kein Kundenprofil in Shopify. Weitere Details finden Sie unter [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Registrierungsformulare von Drittanbietern {#third-party-sign-up-forms}

Wenn Sie eine Drittanbieter-Plattform oder ein Shopify-Plugin für Ihre Registrierungsformulare verwenden, müssen Sie mit Ihren Entwickler:innen zusammenarbeiten, um Braze-SDK-Code zu integrieren, der E-Mail-Adressen und den globalen E-Mail-Abo-Status aus Formulareinreichungen erfasst. Weitere Informationen finden Sie unter [Shopify-Standard-Integrations-Setup]({{site.baseurl}}/shopify_standard_integration) und [Shopify-Custom-Integrations-Setup]({{site.baseurl}}/shopify_custom_integration).

### Produktsynchronisierung {#product-syncing}

Braze unterstützt die Synchronisierung der Produkte Ihres Shopify-Shops in einen Braze-Katalog. Weitere Details finden Sie unter [Shopify-Produktsynchronisierungen]({{site.baseurl}}/shopify_catalogs).

## Anfragen betroffener Personen {#data-subject-requests}

Im Rahmen der Shopify-Integration der Braze-Plattform empfängt Braze automatisch [Shopifys Compliance-Webhooks](https://shopify.dev/docs/apps/build/privacy-law-compliance/). Da Kund:innen jedoch die Datenverantwortlichen für die Daten ihrer Endnutzer:innen sind, müssen Kund:innen alle erforderlichen Maßnahmen ergreifen, um Anfragen betroffener Personen in Bezug auf Endnutzerdaten in Braze (einschließlich über die Shopify-Integration empfangener Endnutzerdaten) zu bearbeiten. Weitere Informationen finden Sie in unserer Dokumentation zur [technischen Unterstützung beim Datenschutz]({{site.baseurl}}/dp-technical-assistance).