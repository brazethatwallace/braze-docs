---
nav_title: Datentransformation
article_title: Datentransformation
page_order: 2
layout: dev_guide
guide_top_header: "Datentransformation"
guide_top_text: "Braze Datentransformation erlaubt es Ihnen, Webhook-Integrationen zu erstellen und zu verwalten, um den Datenfluss von externen Plattformen in Braze zu automatisieren. Diese neu integrierten Nutzerdaten können dann für noch anspruchsvollere Marketing-Anwendungsfälle genutzt werden. Braze Datentransformation kann Ihre Datenintegration beschleunigen, selbst wenn Sie nur wenig Erfahrung mit der Programmierung haben, und kann die Abhängigkeit Ihres Teams von manuellen API-Aufrufen, Integrations-Tools von Drittanbietern oder sogar Customer Data Platforms ersetzen."
page_type: landing
description: "Auf dieser Landing-Page finden Sie Artikel über Braze Datentransformation, u. a. wie Sie eine Datentransformation erstellen und Anwendungsfälle."
alias: /data_transformation/

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: Transformation erstellen
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation
    image: /assets/img/braze_icons/flip-forward.svg
  - name: Anwendungsfälle
    link: /docs/user_guide/data/unification/data_transformation/use_cases
    image: /assets/img/braze_icons/users-01.svg
---

## Funktionsweise {#how-it-works}

Viele moderne Plattformen verfügen über „Webhooks“ oder Realtime-API-Benachrichtigungen, um Informationen über ein neues Ereignis oder neue Daten von einer Plattform zur anderen zu senden. Datentransformation bietet:

* Eine Braze-URL-Adresse, um solche Webhooks zu empfangen.
* Funktionen zur Transformation der Webhook-Nutzdaten mit JavaScript-Code, um gültige Anfragen an verschiedene Braze-API-Endpunkte zu erstellen, einschließlich Braze `/users/track` oder `/catalogs`. Für das Ziel `/users/track` können Sie beispielsweise wählen, welche Informationen vom Webhook verwendet werden sollen und wie die Daten in den Braze-Nutzerprofilen als Nutzerattribute, Ereignisse oder Käufe dargestellt werden sollen.
* Protokollierung zur Qualitätssicherung, Fehlerbehebung und Überwachung der Performance Ihrer Transformationen.

Das Endergebnis ist eine Webhook-Integration, die eine Quellplattform Ihrer Wahl anbindet, indem sie deren Webhooks in Braze-Updates umwandelt.

{% details More on webhooks %}
Webhooks sind Realtime-Benachrichtigungen, die über eine HTTP-POST-Anfrage an ein bestimmtes Ziel gesendet werden. Webhooks werden häufig verwendet, um Daten von einem Punkt zu einem anderen zu senden, wobei der Webhook Daten über eine stattgefundene Aktion und die an dieser Aktion beteiligten Personen übermitteln kann.

Eine Umfrageplattform kann zum Beispiel einen Webhook an ein Ziel Ihrer Wahl senden, sobald eine Umfrageantwort auf ein Online-Formular eingeht. Oder eine Kundendienstplattform kann einen Webhook an ein Ziel ihrer Wahl senden, wenn ein Kundendienst-Ticket erstellt wird.
{% enddetails %}

## Datentransformationsebenen {#data-transformation-tiers}

Die folgende Tabelle beschreibt die Unterschiede zwischen der kostenlosen und der Pro-Version von Datentransformation.

| Bereich | Kostenlose Version | Data Transformation Pro |
|----|----|----|
| Aktive Transformationen | Bis zu 5 pro Unternehmen | Bis zu 55 pro Unternehmen |
| Pro Monat | 300.000 eingehende Anfragen pro Monat | 10.300.000 eingehende Anfragen pro Monat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Datentransformationsebenen" }

{% alert important %}
Um ein Upgrade auf Data Transformation Pro anzufordern, wenden Sie sich an Ihren Braze Account Manager oder wählen Sie den Button **Request Upgrade** im Braze-Dashboard.
{% endalert %}

### Rate-Limits {#rate-limits}

Das Rate-Limit für Braze Datentransformationen liegt bei 1.000 eingehenden Anfragen pro Minute und Workspace. Wenn Sie Data Transformation Pro haben und ein höheres Rate-Limit benötigen, wenden Sie sich an Ihren Braze Account Manager.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was wird mit Braze Datentransformation synchronisiert? {#what-gets-synced-with-braze-data-transformation}

Alle Daten, die die externe Plattform in einem Webhook zur Verfügung stellt, können mit Braze synchronisiert werden. Je mehr eine externe Plattform über Webhooks sendet, desto mehr Möglichkeiten haben Sie, auszuwählen, was synchronisiert werden soll.

### Ich bin Marketer. Benötige ich Entwickler:innen-Ressourcen, um Braze Datentransformation zu verwenden? {#im-a-marketer-do-i-need-developer-resources-to-use-braze-data-transformation}

Wir würden uns freuen, wenn auch Entwickler:innen dieses Feature nutzen würden, aber Sie müssen keine:r sein, um es zu verwenden! Marketer können Transformationen auch ohne Entwickler:innen-Ressourcen erfolgreich einrichten.

### Kann ich Braze Datentransformation auch dann verwenden, wenn meine externe Plattform als Bezeichner nur eine E-Mail-Adresse oder Telefonnummer angibt? {#can-i-still-use-braze-data-transformation-if-my-external-platform-only-gives-an-email-address-or-phone-number-as-an-identifier}

Ja. Sie können Ihre Transformationen zum Update des Endpunkts `/users/track` mit der [E-Mail-Adresse oder Telefonnummer als Bezeichner]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-email-address) verwenden.

Dies funktioniert, indem Sie `email` oder `phone` als Bezeichner-Eigenschaft im Transformationscode anstelle von `external_id` oder `braze_id` verwenden. Der [Beispiel-Transformationscode]({{site.baseurl}}/user_guide/data/unification/data_transformation/use_cases#example-transformation-code) verwendet diese Funktionalität.

{% alert note %}
Nutzer:innen von Braze Datentransformation im Early Access, die vor April 2023 begonnen haben, kennen vielleicht die Funktion `get_user_by_email`, die bei diesem Anwendungsfall hilfreich war. Diese Funktion ist inzwischen veraltet.
{% endalert %}

### Protokolliert Braze Datentransformation Datenpunkte? {#does-braze-data-transformation-log-data-points}

Ja, in den meisten Fällen. Braze Datentransformation erstellt letztlich einen `/users/track`-Aufruf, der die gewünschten Attribute, Ereignisse und Käufe schreibt. Diese protokollieren Datenpunkte auf die gleiche Weise, als ob der `/users/track`-Aufruf unabhängig erfolgt wäre. Sie haben die Kontrolle darüber, wie viele Datenpunkte protokolliert werden, je nachdem, wie Sie Ihre Transformation schreiben.

### Wie kann ich Hilfe bei der Einrichtung meines Anwendungsfalls oder bei meinem Transformationscode erhalten? {#how-can-i-get-help-setting-up-my-use-case-or-with-my-transformation-code}

Wenden Sie sich an Ihren Braze Account Manager, wenn Sie weitere Hilfe benötigen.