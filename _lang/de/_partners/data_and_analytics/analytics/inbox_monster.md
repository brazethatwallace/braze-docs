---
nav_title: Inbox Monster
article_title: Inbox Monster
alias: /partners/inbox_monster/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Inbox Monster, einem Online-Tool für E-Mail-Marketing, das es Braze-Kund:innen erlaubt, leistungsstarke Insights zur Zustellbarkeit und kreative Analysen zu nutzen, um die Performance des Posteingangs zu verbessern."
page_type: partner
search_tag: Partner

---

# Inbox Monster

> [Inbox Monster](https://inboxmonster.com/) ist eine Plattform für Posteingangssignale, die Unternehmensmarken dabei hilft, bei jedem Versand den Posteingang zu erreichen. Es handelt sich um eine integrierte Suite von Lösungen für Zustellbarkeit, kreatives Rendering und SMS-Überwachung, die moderne Teams im Bereich CRM (CRM) befähigt und die Angst vor dem Versand beendet.

Die Integration von Braze und Inbox Monster erlaubt es Ihnen, manuelle Seedlist-Tests zu eliminieren, die Erstellung leistungsstarker und umsetzbarer Signale für die Platzierung im Posteingang zu automatisieren, den Prozess der Überprüfung und Freigabe von E-Mail-Kreativmaterial zu vereinfachen und wertvolle Insights zur Zustellbarkeit zu erhalten. Sie können auch nahtlos E-Mail-Templates für kreative Diagnosen und Gerätevorschauen importieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Inbox-Monster-Plattformkonto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Konto auf der Inbox-Monster-Plattform. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den folgenden Berechtigungen: <br> - `messages.send` <br> - `templates.email.create`<br> - `templates.email.update` <br> - `templates.email.info`<br> - `templates.email.list` <br><br> Und mit den folgenden freigegebenen IPs: <br> - `3.136.16.19` <br> - `3.140.233.31`<br> - `18.220.127.138` <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** auf dem Tab **API-Schlüssel** erstellt werden. |
| Braze-App-Bezeichner | Ein Braze-App-Bezeichner. <br><br>Diesen finden Sie im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** auf dem Tab **App-Bezeichner**. |
| Braze-Endpunkt | [Ihr Braze-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) entspricht der URL Ihres Braze-Dashboards.<br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Um Inbox Monster zu integrieren, folgen Sie den Schritten unter [Integration mit Inbox Monster](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3).

## Nutzung {#usage}

Wie Sie geplante Posteingangstests über Inbox Monster versenden können, erfahren Sie unter [Geplante Posteingangstests](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e).