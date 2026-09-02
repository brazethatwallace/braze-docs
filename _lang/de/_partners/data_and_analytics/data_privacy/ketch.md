---
title: Ketch
nav_title: Ketch
description: "Dieser Referenzartikel behandelt die Integration von Braze und Ketch. Ketch bietet vereinfachte Datenschutzoperationen sowie vollständige, dynamische Datenkontrolle und -intelligenz."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com) ermöglicht es Unternehmen, verantwortungsvoll mit ihren Daten umzugehen. Ketch bietet vereinfachte Datenschutzoperationen sowie vollständige, dynamische Datenkontrolle und -intelligenz.

_Diese Integration wird von Ketch gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Ketch ermöglicht es Ihnen, die Kommunikationspräferenzen Ihrer Kund:innen im Ketch-Präferenzzentrum zu steuern und diese Änderungen automatisch an Braze weiterzugeben.

{% alert note %}
Sie suchen eine Anleitung zur Erstellung von Abo-Gruppen? Sehen Sie sich unsere Artikel für <a href='/docs/user_guide/message_building_by_channel/Kurzmitteilungsdienst or SMS/sms_subscription_group/'>Kurzmitteilungsdienst or SMS-Abo-Gruppen</a> und <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>E-Mail-Abo-Gruppen</a> an.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
|---|---|
| Ketch-Konto | Zum Aktivieren dieser Integration ist ein [Ketch-Konto](https://www.ketch.com) mit Admin-Rechten erforderlich. |
| Braze-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit den Berechtigungen `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe` und `email.blacklist`. <br><br> Dieser kann im Braze-Dashboard erstellt werden (**Entwicklungskonsole** > **Representational State Transfer-API-Schlüssel** > **Neuen API-Schlüssel erstellen**). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1. Schritt: Braze-Verbindung einrichten {#step-1-set-up-the-braze-connection}

1. Navigieren Sie in Ihrer [Ketch-Instanz](https://app.ketch.com) zu **Data Systems** und wählen Sie **Braze** aus. Klicken Sie dann auf **New Connection**.
2. Geben Sie Ihrer Braze-Verbindung einen identifizierbaren Namen, der in API-basierten Prozessen verwendet wird, um auf diese Verbindung zu verweisen. Beachten Sie, dass auch ein Code für diese Verbindung erstellt wird. Dieser Code sollte über alle Verbindungen hinweg eindeutig sein.
3. Bestätigen Sie die Identitätszuordnung Ihrer Nutzer:innen. Standardmäßig ordnet Ketch Nutzeridentitäten über die E-Mail-Adresse oder über die `external_id` in Braze zu.
4. Fügen Sie den Braze-API-Schlüssel hinzu und geben Sie den API-Endpunkt an. Beachten Sie, dass dieser [API-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) davon abhängt, welche Braze-Instanz Ihr Unternehmen verwendet.

### 2. Schritt: Abo-Einstellungen konfigurieren {#step-2-configure-subscription-preferences}

1. Gehen Sie zu **Policy Center > Subscriptions**. Wenn Sie den Tab „Subscriptions“ unter **Policy Center** nicht sehen, vergewissern Sie sich, dass Sie Zugriff auf das Marketing-Präferenzzentrum haben, und überprüfen Sie, ob Sie über die richtigen Kontoberechtigungen für den Zugriff auf diesen Bereich des Produkts verfügen.
2. Klicken Sie auf **Create New Subscription**, um ein neues Thema zu erstellen. Jedes Abo hat einen Namen und einen Code.
3. Fügen Sie die Kanäle für den Versand Ihrer Abo-Themen hinzu. Jeder Kanal wird im Marketing-Präferenzzentrum für Ihre Nutzer:innen angezeigt. Sie können auch festlegen, wie das Ketch-Präferenzzentrum ein bestimmtes Opt-in- oder Opt-out-Signal orchestrieren soll.
4. Wählen Sie die Braze-Verbindung aus, die Sie für die Orchestrierung der Opt-in- und Opt-out-Signale verwenden möchten.
5. Geben Sie die Braze-`subscription_group_id` für die Abo-Gruppe ein, an die Sie die Ketch-Nutzerpräferenzen senden möchten.

![Braze-Abo-Gruppen-ID.]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
Um Opt-in- und Opt-out-Signale von Nutzer:innen zu erfassen und zu orchestrieren, müssen die Identitäten korrekt konfiguriert sein. Ketch empfiehlt, E-Mail als Bezeichner für die Orchestrierung der Nutzerpräferenzsignale für diese Integration zu konfigurieren.
{% endalert %}


### 3. Schritt: Identitäten konfigurieren {#step-3-configure-identities}

Nutzer:innen können das Marketing-Präferenzzentrum nur dann sehen, wenn Ketch die Marketing-Präferenzidentität dieser Person bestätigen kann. Wenn Ketch die Identität nicht korrekt erfassen kann, wird die Seite mit den Marketing-Einstellungen nicht angezeigt, da Ketch die Nutzerpräferenzen nicht verwalten kann.

1. Um die Marketing-Präferenzidentität zu konfigurieren, gehen Sie in Ketch auf die Seite **Settings** und klicken Sie auf **Identity space**. Sie müssen entweder einen neuen Identitätsraum erstellen oder einen bestehenden Identitätsraum bearbeiten, um diesen als Marketing-Präferenzidentität zuzuweisen. Vergewissern Sie sich, dass der auf der Property eingesetzte Ketch-Tag diesen Identitätsraum korrekt erfasst.
2. Gehen Sie zu **Experience Server** > **Properties** und bearbeiten Sie die gewünschte Property. Stellen Sie unter der Datenschicht für diese Property sicher, dass der angepasste Identitätsraum aktiviert ist. Konfigurieren Sie dann, wie die Marketing-Präferenzidentität auf dieser Website erfasst werden soll.
3. Nachdem Sie den Identitätsraum konfiguriert haben, testen Sie, ob das Präferenzzentrum angezeigt wird, indem Sie es auf der Website öffnen, auf der der Ketch-Tag bereitgestellt wurde.