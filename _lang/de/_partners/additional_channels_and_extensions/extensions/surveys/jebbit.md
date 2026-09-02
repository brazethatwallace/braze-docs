---
nav_title: Jebbit
article_title: Jebbit
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Jebbit, einer PaaS, die es Ihnen erlaubt, E-Mails und Attribute von Nutzer:innen aus Ihren Jebbit-Kampagnen als Nutzerdaten in Realtime an Braze zu übergeben."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/) ist eine PaaS, die es Ihnen erlaubt, ansprechende Erlebnisse für Nutzer:innen zu erstellen, um First-Party-Daten zu erfassen.

_Diese Integration wird von Jebbit gepflegt._

## Über die Integration {#about-the-integration}

Mit der Integration von Braze und Jebbit können Sie E-Mails und Attribute von Nutzer:innen aus Ihren Jebbit-Kampagnen als Nutzerdaten in Realtime an Braze weitergeben. Diese Daten können dann für Marketing-Initiativen wie personalisierte E-Mail-Kampagnen und Trigger or triggern verwendet werden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Jebbit-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Jebbit-Konto. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit allen Nutzerdaten-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Representational State Transfer-Endpunkt | Ihre URL für den Representational State Transfer-Endpunkt. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Wenn Sie eine Integration mit Jebbit anfragen, teilen Sie mit, ob bestimmte Fristen eingehalten werden müssen. Stellen Sie außerdem sicher, dass Sie die Attribute Ihrer Jebbit-Erlebnisse, die Sie an Braze weitergeben möchten, zugeordnet haben.

### 1. Schritt: API-Zugangsdaten bereitstellen {#step-1-provide-api-credentials}

Stellen Sie Jebbit Ihre API-Zugangsdaten in einer Textdatei über eine Dropbox-Dateianfrage zur Verfügung.
Senden Sie Ihre Datei über die folgende [Dropbox-URL](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx).

### 2. Schritt: Testübertragung bestätigen {#step-2-confirm-test-submission}

Ein Jebbit-Ingenieur, der für Ihre Integration zuständig ist, wird eine Testübertragung von Jebbit zu Braze durchführen, damit Sie sehen können, wie die Daten in Ihrer Braze-Umgebung aussehen werden. Dies ist der letzte Schritt zur Aktivierung der Integration. Jetzt, wo Ihre Jebbit-Daten eingerichtet sind, nutzen Sie sie, um Ihre Marketing-Initiativen voranzutreiben.

{% alert note %}
Die Attribut-ID, die Sie in Jebbit festgelegt haben, bestimmt, wie der Name des Attributfelds in Braze angezeigt wird.
{% endalert %}

## Anpassung {#customization}

Wir unterstützen derzeit speziell die Endpunkte für [Nutzerdaten]({{site.baseurl}}/api/endpoints/user_data/), aber Anfragen für andere Endpunkte können ebenfalls unterstützt werden.

Die Namen der Attributfelder können auch nach Ihren Wünschen angepasst werden.

Wenn Sie zusätzliche Attribute von Jebbit in Braze wünschen, ordnen Sie das neue Attribut in Ihrem Jebbit-Konto zu. Das Attribut wird automatisch in Braze angezeigt, sobald Sie Daten für dieses Attribut erfassen.