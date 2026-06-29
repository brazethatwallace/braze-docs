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
| Berechtigungen für Shopify-Shop-Besitzer:innen oder Mitarbeiter:innen | {::nomarkdown}<ul><li>Zugang zu allen allgemeinen Einstellungen und den Einstellungen des Online-Shops.</li><li> Zusätzliche Admin-Berechtigungen:<ul><li>Bestellungen: Anzeigen</li><li>Kund:innen: Lesen/Schreiben</li><li>Kundenereignisse anzeigen (Web Pixels)</li><li>Einstellungen verwalten</li><li>Von Mitarbeiter:innen/Kollaborateur:innen entwickelte Apps anzeigen</li><li>Apps und Kanäle verwalten/installieren</li><li>Angepasste Pixel verwalten/hinzufügen</li></ul></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## Wie Sie integrieren {#how-to-integrate}

Braze bietet zwei Integrationsoptionen für Shopify-Händler, die auf die unterschiedlichen Bedürfnisse von E-Commerce-Unternehmen zugeschnitten sind: **Standardintegration** und **angepasste Integration**.

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

## So funktioniert die Integration {#how-the-integration-works}

Wenn Sie in Ihren Konfigurationseinstellungen bereits den [historischen Backfill]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) eingerichtet und aktiviert haben, beginnt die erste Datensynchronisierung sofort.

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

Nach der anfänglichen Datensynchronisierung verfolgt Braze kontinuierlich neue Daten und Updates direkt von Shopify und den Braze SDKs.

{% alert note %}
Wenn Sie bereits Kund:in von Braze sind und über aktive Campaigns oder Canvases verfügen, finden Sie wichtige Informationen unter [Shopify historischer Backfill]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill). Um zu sehen, welche spezifischen Kundendaten zurückgefüllt werden, lesen Sie [Shopify-Features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).
{% endalert %}

### Nutzer:innen- und Datensynchronisierung {#user-and-data-syncing}

Nachdem die Integration aktiv ist, sammelt Braze über die Shopify-Integration Nutzerdaten aus zwei wichtigen Quellen:
- **Shopify Web Pixel API und App-Einbettungen:** Dies ermöglicht das Braze Web SDK und das Javascript SDK für On-Site-Tracking, Identitätsmanagement, E-Commerce-Verhaltensdaten und Messaging-Kanäle wie In-App-Nachrichten.
- **Shopify-Webhooks:** E-Commerce-Verhaltensdaten, Produktsynchronisierung und Abonnent:innen-Erfassung

Beim Onboarding der Integration müssen Sie auswählen, wann die Braze SDKs initialisiert und auf Ihrer Shopify-Website geladen werden sollen:
- Beim Website-Besuch (z. B. bei Sitzungsbeginn)
    - **Was es bewirkt:** Tracking anonymer Nutzer:innen – wie z. B. Gastkäufer:innen – um mehr Daten für eine tiefere Personalisierung zu erhalten
- Bei der Kontoregistrierung (z. B. bei der Kontoanmeldung)
    - **Was es bewirkt:** Verhindert das Tracking anonymer Nutzer:innen für einen konservativeren, datenschutzorientierten Ansatz, sodass die Aktivitäten der Nutzer:innen erst *nach* der Anmeldung in ihrem Konto verfolgt werden

{% alert note %}
- Website-Besuche (Sitzungen) werden auf Ihre monatlich aktiven Nutzer:innen (MAU) angerechnet.
- Die Versionen des Braze Web SDK und des JavaScript SDK werden automatisch auf v5.4.0 gesetzt.
{% endalert %}

Braze nutzt die Shopify-Integration, um mehrere Bezeichner zu unterstützen, die das Tracking Ihrer Nutzer:innen von ihrem Gasteinkauf bis zu ihrer Identifizierung ermöglichen:

| Braze-Bezeichner | Beschreibung |
| --- | --- |
| Braze `device_id` | Eine zufällig generierte ID, die im Browser gespeichert wird und die Aktivitäten anonymer Nutzer:innen über Braze SDKs verfolgt. |
| Warenkorb-Token-Nutzer-Alias | Ein Alias, den Braze zum Tracking von Warenkorb-Update-Ereignissen erstellt. Dieses Token wird mit dem Shopify-Warenkorb-Token erstellt. |
| Checkout-Token-Nutzer-Alias | Ein Alias, den Braze erstellt, wenn Nutzer:innen den Checkout-Prozess starten. Dieses Token wird mit dem Shopify-Checkout-Token erstellt.<br><br> Wenn Kund:innen Shop Pay als beschleunigte Checkout-Option verwenden, kann Shopify bestimmte Standard-Checkout-Ereignisse umgehen und verhindern, dass Braze die Daten erhält, die zum Hinzufügen des Checkout-Token-Alias benötigt werden. |
| Shopify-Kunden-ID-Alias | Die Shopify-Kunden-ID wird als Alias zugewiesen, wenn die externe ID bei der Kontoanmeldung oder bei einer Bestellung zugewiesen wird. |
| Braze `external_id` | Ein eindeutiger Bezeichner, der das Tracking von Kund:innen über verschiedene Geräte und Plattformen hinweg unterstützt. Dies sorgt für ein konsistentes Nutzererlebnis und verbessert die Analytics, indem verhindert wird, dass mehrere Profile entstehen, wenn Nutzer:innen das Gerät wechseln oder die App neu installieren.<br><br>Die Shopify-Integration unterstützt die folgenden `external_id`-Typen: <br><br>{::nomarkdown}<ul><li>Shopify-Kunden-ID (Standard)</li><li>Angepasste externe ID</li><li>Gehashte E-Mail (SHA-256)</li><li>Gehashte E-Mail (SHA-1)</li><li>Gehashte E-Mail (MD5)</li><li>E-Mail</li></ul>{:/}Braze weist Ihren Nutzer:innen eine `external_id` zu, indem die changeUser-Methode innerhalb der SDKs aufgerufen wird, wenn: <br><br>{::nomarkdown}<ul><li>Nutzer:innen sich anmelden oder ein Konto erstellen</li><li>Eine Bestellung aufgegeben wird</li></ul>{:/}<br> Weitere Informationen darüber, was passiert, wenn Sie einem anonymen Profil eine `external_id` zuweisen, finden Sie unter [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>Braze nutzt die `external_id` auch, um nachgelagerte E-Commerce-Verhaltensdaten von Shopify-Webhooks zuzuordnen.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen- und Datensynchronisierung" }

Für die Integration müssen die Braze SDKs und die Shopify-Dienste zusammenarbeiten, damit die Shopify-Daten in nahezu Echtzeit den richtigen Nutzer:innen zugeordnet und getrackt werden können. Weitere Einzelheiten zu den Daten, die durch die Integration getrackt werden, finden Sie unter [Shopify-Daten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

{% alert note %}
- Wenn Sie die Integration testen, empfehlen wir Ihnen, den Inkognito-Modus zu verwenden oder Ihre Cookies zu löschen, um die Braze `device_id` zurückzusetzen und das Verhalten anonymer Nutzer:innen zu simulieren.
- Auch wenn eine Shopify-Kunden-ID generiert wird, wenn eine E-Mail-Adresse in die Shopify-Newsletter-Fußzeile eingegeben wird oder während des Checkout-Prozesses bevor eine Bestellung aufgegeben wird, ist diese Kunden-ID nicht über Shopify Web Pixels zugänglich. Aus diesem Grund kann Braze die Methode `changeUser` in diesen beiden Situationen nicht verwenden.
{% endalert %}

### Synchronisierung der Opt-ins für E-Mail- und SMS-Marketing von Shopify {#syncing-shopify-email-and-sms-marketing-opt-ins}

Wenn Sie die Abonnent:innen-Erfassung in Ihren Konfigurationseinstellungen aktivieren, müssen Sie für jeden Shop, den Sie mit Braze verbinden, eine Abo-Gruppe zuweisen. Das bedeutet, dass Ihre Kund:innen der Abo-Gruppe Ihres Shops entweder als „abonniert“ oder als „abgemeldet“ kategorisiert werden.

Der Opt-in-Status des Shopify-Marketings für E-Mail- und SMS-Marketing kann auf folgende Weise aktualisiert werden:
- **Manuelles Update:** Sie können den Opt-in-Status für E-Mail- oder SMS-Marketing manuell in Ihrem Shopify-Admin ändern.
- **Shopify-Newsletter-Fußzeile:** Wenn Nutzer:innen ihre E-Mail-Adresse in der Standard-Newsletter-Fußzeile von Shopify eingeben, wird ihr Opt-in-Status aktualisiert.
- **Checkout-Prozess:** Wenn Nutzer:innen ihren Opt-in-Status während des Bestellvorgangs aktualisieren.

{% alert note %}
Der Opt-in-Status für E-Mail-Marketing von Shopify ändert nicht den [globalen E-Mail-Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions) von Nutzer:innen in Braze. Der Standard-Abo-Status bei der Erstellung eines Nutzerprofils ist „abonniert“. Denken Sie daran, die Abo-Gruppe als Teil Ihrer Campaign- oder Canvas-Eingangskriterien zu verwenden.
{% endalert %}

Diese Tabelle zeigt, welche Opt-in-Status von Shopify-Marketing mit den Status innerhalb Ihrer Braze-Abo-Gruppe korrelieren.

| Shopify-Marketing-Opt-in-Status | Braze-Abo-Gruppen-Status |
| --- | --- |
| E-Mail ist abonniert | Abonniert |
| E-Mail ist abgemeldet | Abgemeldet |
| E-Mail wartet auf Bestätigung | Abgemeldet |
| E-Mail ist ungültig | Abgemeldet |
| SMS abonniert | Abonniert |
| SMS abgemeldet | Abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Synchronisierung der Opt-ins für E-Mail- und SMS-Marketing von Shopify" }

### Registrierungsformulare {#sign-up-forms}

#### Shopify-Newsletter-Fußzeile {#shopify-newsletter-footer}

Nutzer:innen, die ihre E-Mail-Adresse in die Shopify-Newsletter-Fußzeile eingeben, durchlaufen einen dieser Workflows:

##### Nutzer:innen, die sich nicht in ihr Konto eingeloggt haben {#users-who-havent-logged-into-their-account}

1. Braze empfängt einen eingehenden Shopify-Webhook, wenn Kund:innen erstellt oder aktualisiert werden.
2. Braze erstellt ein Nutzerprofil, das die E-Mail-Adresse und den Shopify-Kunden-ID-Alias enthält, die mit diesen Nutzer:innen verknüpft sind.
3. Das Braze SDK aktualisiert das anonyme Profil mit der E-Mail-Adresse.

{% alert note %}
Dies kann zu einem doppelten Profil führen, bis sich Nutzer:innen selbst identifizieren, indem sie ihr Konto erstellen, sich bei ihrem Konto anmelden oder eine Bestellung aufgeben. Braze bietet Tools für die Massenzusammenführung, mit denen Sie den Abgleich von doppelten Profilen automatisieren können. Weitere Informationen finden Sie unter [Doppelte Nutzer:innen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).
{% endalert %}

##### Nutzer:innen, die sich bereits in ihrem Konto angemeldet haben {#users-who-have-already-logged-into-their-account}

Braze erstellt ein Nutzerprofil mit der E-Mail-Adresse und dem Shopify-Kunden-ID-Alias, die mit diesen Nutzer:innen verknüpft sind. Braze aktualisiert die E-Mail-Adresse der angemeldeten Nutzer:innen nicht, da wir davon ausgehen, dass Shopify diese Informationen bereits bereitgestellt hat.

#### Braze-Registrierungsformulare {#braze-sign-up-forms}

Braze bietet zwei Arten von Templates für Registrierungsformulare:
- **[E-Mail-Registrierungsformulare]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/email_capture):** Erstellen Sie diese mit dem Drag-and-Drop-Editor.
- **[Traditionelles E-Mail-Erfassungsformular]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form):** Ein einfacheres Formular zur Erfassung von E-Mail-Adressen.

Wenn Sie diese Templates für Registrierungsformulare verwenden, aktualisiert Braze automatisch den globalen E-Mail-Abo-Status im Nutzerprofil. Weitere Einzelheiten zum Umgang mit dem globalen E-Mail-Abo-Status, einschließlich Informationen zur E-Mail-Validierung, finden Sie in der Dokumentation für den jeweiligen Formular-Template-Typ.

{% alert note %}
- Stellen Sie sicher, dass Ihre Campaign oder Ihr Canvas Eingangskriterien enthält, die sowohl den globalen E-Mail-Abo-Status als auch die Abo-Gruppe umfassen, die mit Ihrem Shopify-Shop verbunden ist. So können Sie sicherstellen, dass Sie die richtige Zielgruppe ansprechen.
- Braze sammelt über In-Browser-Nachrichten Informationen über Besucher:innen, wie z. B. E-Mail-Adressen und Telefonnummern. Diese Informationen werden dann an die Shopify Visitor API gesendet, erstellen aber kein Kundenprofil in Shopify. Weitere Einzelheiten finden Sie unter [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Registrierungsformulare von Drittanbietern {#third-party-sign-up-forms}

Wenn Sie eine Drittanbieter-Plattform oder ein Shopify-Plugin für Ihre Registrierungsformulare verwenden, müssen Sie mit Ihren Entwickler:innen zusammenarbeiten, um den Braze-SDK-Code zu integrieren, damit die E-Mail-Adresse und der globale E-Mail-Abo-Status aus den Formularübermittlungen erfasst werden. Mehr erfahren Sie unter [Einrichtung der Shopify-Standardintegration]({{site.baseurl}}/shopify_standard_integration) und [Einrichtung der angepassten Shopify-Integration]({{site.baseurl}}/shopify_custom_integration).

### Produktsynchronisierung {#product-syncing}

Braze unterstützt die Möglichkeit, die Produkte Ihres Shopify-Shops in einen Braze-Katalog zu synchronisieren. Weitere Einzelheiten finden Sie unter [Shopify-Produktsynchronisierungen]({{site.baseurl}}/shopify_catalogs).

## Anfragen betroffener Personen {#data-subject-requests}

Im Rahmen der Shopify-Integration der Braze-Plattform empfängt Braze automatisch [die Compliance-Webhooks von Shopify](https://shopify.dev/docs/apps/build/privacy-law-compliance/). Da die Kund:innen jedoch die Verantwortlichen für die Daten ihrer Endnutzer:innen sind, müssen sie alle erforderlichen Maßnahmen ergreifen, um Anfragen betroffener Personen in Bezug auf Endnutzerdaten in Braze (einschließlich der über die Shopify-Integration erhaltenen Endnutzerdaten) zu bearbeiten. Weitere Einzelheiten finden Sie in unserer Dokumentation zur [technischen Unterstützung beim Datenschutz]({{site.baseurl}}/dp-technical-assistance).