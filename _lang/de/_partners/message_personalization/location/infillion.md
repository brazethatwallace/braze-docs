---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Infillion, die es Ihnen ermöglicht, die Relevanz Ihres Marketings mithilfe von Standortdaten zu perfektionieren."
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/) ermöglicht es Ihnen, die Relevanz Ihres Marketings mithilfe von Standortdaten zu perfektionieren. Das Standort-SDK in Kombination mit Geofencing-Software und Beacons ermöglicht relevante, personalisierte und standortbezogene mobile Erlebnisse.

Kombinieren Sie Ihre Beacon- oder Geofence-Unterstützung mit den Targeting- und Messaging-Features von Braze, um mehr über die physischen Aktionen Ihrer Nutzer:innen zu erfahren und ihnen entsprechende Nachrichten zu senden. Diese Partnerschaftsintegration eröffnet eine Reihe von Anwendungsfällen für:

- **Marketing:** Versenden Sie kontextuell relevante Nachrichten und gestalten Sie erlebnisorientierte Verbraucher-Journeys.
- **Wettbewerbsanalyse:** Richten Sie Trigger an konkurrierenden Standorten ein, um Verbrauchertrends und -muster zu verstehen.
- **Audience Insights:** Verstehen Sie das Besuchsverhalten Ihrer Nutzer:innen und segmentieren Sie auf der Grundlage dieser Erkenntnisse weiter.

{% alert note %}
Diese Integration funktioniert für Infillion Beacons und Infillion Geofence-Lösungen gleichermaßen.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| [Infillion-Manager:in-Konto](https://manager.gimbal.com/login/users/sign_in) | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Infillion-Manager:in-Konto. |
| [Infillion Location SDK](https://docs.gimbal.com/index.html) | Das Infillion Location SDK ermöglicht makro- und mikrostandortbasierte mobile Erlebnisse unter Verwendung von Proximity Beacons und Geofences, die es Ihnen ermöglichen, effektiver mit Ihren App-Nutzer:innen zu kommunizieren. Sie müssen das SDK implementiert und Geofences (oder Beacons) eingerichtet haben. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDK-Integration

Um Braze und Infillion zu integrieren, müssen Sie das Infillion Location SDK implementieren und ein Infillion-Manager:in-Konto erstellen. Die folgenden Integrationen für Android, FireOS und iOS erstellen ein eindeutiges angepasstes Event für jeden neuen Ort, den ein:e Nutzer:in betritt. Diese Events können dann für das Triggern und Retargeting in Ihren Campaigns und Canvases verwendet werden.

Wenn Sie voraussichtlich mehr als 50 Orte erstellen werden, empfehlen wir Ihnen, ein allgemeines angepasstes Event `Places Entered` zu erstellen und den Ortsnamen als Event-Eigenschaft hinzuzufügen.

1. Integrieren Sie das [Infillion SDK](https://manager.gimbal.com/sdk_downloads) für Android und iOS in Ihre App, indem Sie die Anweisungen in der [Infillion-Dokumentation](https://docs.gimbal.com/) befolgen.
2. Verwenden Sie die [Place-REST-API](https://docs.gimbal.com/rest.html) von Infillion, um `places` der Nutzer:innen abzurufen.
3. Verknüpfen Sie Ihr Infillion-Konto mit Braze, indem Sie den Braze [REST-API-Schlüssel](https://manager.gimbal.com/apps) eingeben.
4. Richten Sie [angepasste Events]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) im Braze SDK ein. Sie können Infillion mit Braze für [Android und FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons) und [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons) integrieren.
5. Protokollieren Sie Eigenschaften für diese Events (Ortsname, Verweildauer).
6. Verwenden Sie diese Eigenschaften und Events zum Triggern von Campaigns und Canvases in Braze.