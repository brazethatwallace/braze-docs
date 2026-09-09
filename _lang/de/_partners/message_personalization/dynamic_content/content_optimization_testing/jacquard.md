---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Jacquard Dynamic Optimisation, die Braze-Currents und Connected-Content nutzt, um über Webhooks Klick-Tracking-Informationen von Ihren Abonnent:innen zu sammeln. Jacquard verknüpft diese Ereignisse dann mit Ihren Sprachvarianten zur Realtime-Sprachoptimierung."
page_type: partner
search_tag: Partner
---

# Jacquard Dynamic Optimisation

> [Jacquard](https://www.jacquard.com/) vereint KI, Computerlinguistik und den Geist der Kundenorientierung, um die Markensprache in großem Umfang über Kanäle hinweg einzusetzen, die an die Stimme Ihrer Marke angepasst sind.

Dynamic Optimisation, powered by Jacquard X, nutzt Braze-Currents und Connected-Content, um über Webhooks Klick-Tracking-Informationen von Ihren Abonnent:innen zu sammeln. Jacquard verknüpft diese Ereignisse dann mit Ihren Sprachvarianten zur Realtime-Sprachoptimierung.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Jacquard-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Jacquard-Konto](https://www.jacquard.com/). |
| Jacquard Connect Server Token | Ein langer String von Zeichen, der als Passwort für Ihre Braze-Campaign dient, um auf Ihre Jacquard-Sprache zuzugreifen.<br><br>Sie können dies bei Ihrem Jacquard CSM anfragen, falls Sie es nicht bereits erhalten haben. |
| Currents | Um Daten zu Currents exportieren zu können, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Jacquard Amazon S3-Anmeldedaten anfragen {#step-1-request-jacquard-amazon-s3-credentials}

Sie benötigen Jacquard, um einen dedizierten Amazon S3-Bucket einzurichten, der Ihre Klick-Tracking-Ereignisse von Braze empfängt. Kontaktieren Sie Ihren Jacquard CSM, um diesen Prozess zu starten. Wenn der Bucket erstellt wurde, erhalten Sie eindeutige Zugangsdaten, um Ihren Current zu erstellen.

### 2. Schritt: Current erstellen {#step-2-create-current}

1. Wählen Sie in Braze **Currents > Neu erstellen > Amazon S3-Datenexport**.
2. Benennen Sie dann Ihren Current und geben Sie eine Kontakt-E-Mail-Adresse ein.
3. Fügen Sie Ihre Jacquard AWS-Zugriffsschlüssel-ID und den geheimen Zugriffsschlüssel in das Feld für die Zugangsdaten ein. Fügen Sie dann „phrasee-braze-currents-exports“ als AWS S3-Bucket-Name hinzu.
4. Fügen Sie schließlich den AWS S3-Bucket-Ordner hinzu, den Sie von Ihrem Jacquard CSM erhalten haben. Es wird wahrscheinlich der Name Ihres Unternehmens sein.
5. Aktivieren Sie unter **Allgemeine Einstellungen** das Kästchen „Ereignisse von anonymen Nutzer:innen einbeziehen“ und unter **Engagement-Ereignisse verwalten** das Kästchen „E-Mail-Klick“.
6. Wenn Sie fertig sind, wählen Sie **Current starten**.

### 3. Schritt: Entfernung von persönlich identifizierbaren Informationen (PII) anfragen {#step-3-request-to-remove-personally-identifiable-information-pii}

Wenden Sie sich als Nächstes an Ihr Braze-Kontoteam, um sicherzustellen, dass keine personenbezogenen Daten an Jacquard übermittelt werden.

Standardmäßig enthält der Current bestimmte PII-Attribute wie E-Mail und Adresse. Jacquard kann und wird keine PII erhalten. Daher ist es wichtig, dass Sie eine Anfrage an Ihr Braze-Kontoteam stellen, um dies für alle an Jacquard weitergegebenen Ereignisdaten zu deaktivieren.

### 4. Schritt: Jacquard X Code-Snippets {#step-4-jacquard-x-code-snippets}

Wenden Sie sich an Ihr Jacquard-Kontoteam, um die erforderlichen Code-Snippets zu erhalten.

Diese Snippets verwenden [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) und ziehen, nachdem sie in Ihren E-Mails platziert wurden, dynamisch Sprache und ein Tracking-Pixel ein, sodass Jacquard Ihre Sprache in Realtime mit Jacquard X optimieren kann.