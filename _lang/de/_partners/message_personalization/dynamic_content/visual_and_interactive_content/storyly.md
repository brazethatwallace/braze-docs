---
nav_title: Storyly
article_title: Storyly
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Storyly, einem leichtgewichtigen SDK, das es App-Besitzern ermöglicht, ihre Segmente gezielt anzusprechen und Braze mit mehr First-Party-Daten zu versorgen."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) ist ein leichtgewichtiges SDK, das Stories in Ihre App oder Website bringt. Mit einem intuitiven Designstudio, aufschlussreichen Analytics und nahtloser Konnektivität ist Storyly ein leistungsstarkes Tool zur Bereicherung des Erlebnisses der Zielgruppe.

_Diese Integration wird von Storyly gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Storyly ermöglicht es Ihnen, Ihre Segmente in Braze als Zielgruppe in der Storyly-Plattform zu verwenden. Mit dieser Integration können Sie:
- Ihre Segmente mit bestimmten Stories gezielt ansprechen
- Nutzer:innen-Attribute verwenden, um die Inhalte Ihrer Stories zu personalisieren

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Storyly-Konto | Um diese Partnerschaft nutzen zu können, ist ein Storyly-Konto erforderlich. |
| Storyly SDK | Sie müssen das [Storyly SDK](https://integration.storyly.io/) installieren. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den folgenden Berechtigungen: <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle {#use-cases}

Mit der Integration von Braze und Storyly können App-Besitzer allen Segmenten in Braze Stories zeigen und die Stories mit Nutzer:innen-Attributen personalisieren.

Einige häufige Anwendungsfälle sind:

__Braze-Segmente in Storyly gezielt ansprechen__<br>Nach Abschluss der Integration können Sie eine Storyly-Zielgruppe erstellen, die auf Ihren Braze-Segmenten basiert. Dabei kann es sich um ein demografisches oder verhaltensbezogenes Segment handeln. Sprechen Sie beispielsweise Nutzer:innen an, die an einem bestimmten Standort leben, die eine bestimmte Aktion in Ihrer App ausführen oder die sich für bestimmte Produkte interessieren – mit gezielten Stories, um die Conversion zu steigern.<br>
__Personalisierte Stories mit Nutzer:innen-Attributen__<br>Braze-Nutzer:innen-Attribute können auch in Storyly verwendet werden, um dynamische Stories zu erstellen. Dies könnte den Namen einer Nutzerin oder eines Nutzers, Produkte in einem Warenkorb oder sogar favorisierte Produkte umfassen, um den Nutzer:innen einzigartige personalisierte Stories zu liefern. Die Personalisierung trägt dazu bei, die Konversionsrate von Stories und die Engagement-Rate insgesamt zu erhöhen.

## Datenexport-Integration {#data-export-integration}

Die Integration von Braze und Storyly wird im folgenden Video erklärt:

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Stellen Sie sicher, dass Ihre Storyly-Integration angepasste Parameter enthält. Diese Parameter werden mit der Braze-Nutzer:innen-Eigenschaft `external id` abgeglichen. Die Implementierung angepasster Parameter wird hier für [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) und [Web](https://integration.storyly.io/web/personalization-customaudience.html) erläutert.

Weitere Informationen finden Sie auch in der [Storyly-Dokumentation](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly).

### 1. Schritt: Integration im Storyly-Dashboard einrichten {#step-1-set-the-integration-on-storyly-dashboard}

Eine Integration kann im **Storyly Dashboard > Settings > Integrations > Connect with Braze** erstellt werden. Hier benötigen Sie Ihren Braze-REST-API-Schlüssel und den Braze-REST-Endpunkt.

### 2. Schritt: Ihre Segmente abrufen {#step-2-get-your-segments}

Als Nächstes können Sie Braze-Segmente verwenden, um eine Storyly-Zielgruppe zu erstellen. Diese kann im **Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze** erstellt werden.

Hier stehen zwei Synchronisierungsoptionen zur Verfügung. Wählen Sie **One-time sync** für bestimmte Campaign-Stories oder **Daily Sync** für langfristige Stories.