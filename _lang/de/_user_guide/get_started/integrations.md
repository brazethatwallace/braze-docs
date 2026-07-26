---
nav_title: Integration
article_title: Onboarding – Überblick über die Integration
page_order: 8
page_type: reference
description: "Dieser Referenzartikel beschreibt kurz die erforderlichen Integrationsschritte für Ihre Entwicklerabteilung."

---

# Integration {#integration}

> Die Integration mit Braze ist ein lohnender Prozess. Aber Sie sind klug. Sie sind **hier**. Offensichtlich wissen Sie das bereits. Was Sie aber wahrscheinlich noch nicht wissen: Sie und Ihr Entwicklerteam begeben sich auf eine gemeinsame Journey, die technisches Fachwissen, strategische Planung und eine einheitliche Kommunikation erfordert, um die Koordinierung zwischen Ihnen beiden zu erleichtern.

{% alert note %}
Beachten Sie, dass der Inhalt dieses Artikels nicht für E-Mails gilt. Sehen Sie sich dazu den Abschnitt [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup) an.
{% endalert %}

## Die technische Seite des Integrationsprozesses {#the-technical-side-of-the-integration-process}

Vielleicht denken Sie jetzt: „Meine Entwickler:innen sind echte Zauberkünstler! Sie können alles, also lasse ich sie meistens einfach gewähren!“ Und sie sind es wahrscheinlich und können es wahrscheinlich auch! Aber es gibt keinen Grund, warum Sie nicht wissen sollten, was sie hinter den Kulissen tun. In der Tat wäre es für den gesamten Prozess hilfreich, wenn Sie wüssten, wann Sie mit Informationen einspringen und worauf Sie achten müssen, wenn man Sie fragt: „Können Sie mir den API-Schlüssel und den API-Endpunkt schicken?“

Was tun sie also, wenn sie Braze in Ihre App oder Website integrieren? Eine gute Frage!

### 1. Schritt: Sie implementieren das Braze SDK {#step-1-they-implement-the-braze-sdk}

Das Braze SDK (Software-Development-Kit) dient dazu, Informationen mit Ihrer App oder Website auszutauschen. Ihre Entwickler:innen verbinden unsere Anwendungen im Wesentlichen miteinander. Dazu benötigen sie einige wichtige Informationen:

* Ihre [API-Schlüssel]({{site.baseurl}}/api/api_key)
* Ihr [SDK-Endpunkt]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)
  * Braze stellt keine benutzerdefinierten Endpunkte mehr zur Verfügung. Verwenden Sie daher die vordefinierten SDK-Endpunkte. Wenn Sie einen bereits existierenden benutzerdefinierten Endpunkt erhalten haben, finden Sie hier die Einrichtungsschritte für die [Android-]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration#step-5-optional-custom-endpoint-setup), [iOS-]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) und [Web-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#initializing-the-sdk).

Sie können diese Informationen entweder direkt weitergeben oder Ihrem Entwicklerteam Zugang zu Braze geben, indem Sie ein Konto für sie erstellen.

{% alert warning %}
Stellen Sie sicher, dass Sie und Ihr Entwicklerteam in Braze nicht versehentlich die Zugangsdaten Ihres Unternehmens ändern. Denn das kann zu Problemen bei der Implementierung und sogar zur Kontosperrung führen.
{% endalert %}

### 2. Schritt: Sie implementieren die von Ihnen gewünschten Messaging-Kanäle {#step-2-they-implement-your-desired-messaging-channels}

Braze bietet viele Optionen, um mit Ihren Nutzer:innen in Kontakt zu treten, und jede erfordert eine eigene Einrichtung oder Anpassung, damit sie so funktioniert, wie Sie es wünschen. An dieser Stelle wird die Kommunikation mit Ihren Entwickler:innen entscheidend.

Teilen Sie Ihren Entwickler:innen mit, welche Kanäle Sie verwenden möchten, um sicherzustellen, dass die Implementierung effizient und in der richtigen Reihenfolge erfolgt.

| Kanal | Details |
|---|---|
| In-App-Nachrichten | Erfordert die SDK-Implementierung sowie diese kanalspezifischen Schritte. |
| Push | Erfordert eine SDK-Implementierung für die korrekte Handhabung von Messaging-Zugangsdaten und Push-Token. |
| E-Mail | Dies ist ein völlig anderer Prozess. Weitere Einzelheiten zur Integration finden Sie im Abschnitt [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup). |
| Content Cards | Um mit [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards) zu beginnen, wenden Sie sich bitte an Ihren Braze-geschäftskunden-Success-Manager. |
| SMS und MMS | Weitere Einzelheiten zur Integration finden Sie im Abschnitt [SMS-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending). |
| Webhooks | Erfordert eine SDK-Implementierung sowie kanalspezifische Schritte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2. Schritt: Sie implementieren die von Ihnen gewünschten Messaging-Kanäle" }

{% alert tip %}
Mit Braze können Sie für jeden Kanal barrierefreie Messaging-Kampagnen erstellen. Stellen Sie gemeinsam mit Ihren Entwickler:innen sicher, dass Sie bei der Implementierung die Standards der Barrierefreiheit einhalten.
{% endalert %}

### 3. Schritt: Daten einrichten {#step-3-they-set-up-your-data}

Braze ist kein One-Trick-Pony. Hier geht es nicht nur um das Versenden von E-Mails oder Push-Nachrichten. Es geht darum, personalisierte geschäftskunden Journeys zu erstellen, die für jede Nutzerin und jeden Nutzer einzigartig sind. Diese geschäftskunden Journeys basieren auf Aktionen in Ihrer App oder auf Ihrer Website – und Sie bestimmen, welche das sind! Die nächste Aufgabe Ihrer Entwickler:innen besteht darin, dafür zu sorgen, dass die in Ihrer App oder Website durchgeführten Aktionen von Braze erfasst werden.

Was müssen Sie also tun, um ihnen diese Informationen zu geben?

1. Arbeiten Sie mit Ihrem Marketingteam zusammen, um Kampagnen, Ziele, Attribute und Events festzulegen, die Sie verfolgen wollen. Definieren Sie diese Anwendungsfälle und teilen Sie sie mit Ihren Teams.
2. Definieren Sie Ihre angepassten Datenanforderungen ([angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) usw.).
3. Diskutieren Sie dann, wie diese Daten getrackt werden sollen (getriggert durch das SDK usw.).
4. Legen Sie fest, wie viele [Workspaces]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces) Sie benötigen. Ihre Entwickler:innen müssen wissen, wie sie diese Workspaces [testen und konfigurieren]({{site.baseurl}}/user_guide/get_started/workspaces) können.

Wenn Sie alles geklärt haben, informieren Sie Ihr Entwicklerteam. Es nimmt diese Informationen auf und implementiert Ihre [angepassten Daten]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data). Vielleicht müssen Sie sogar [einige Nutzer:innen importieren]({{site.baseurl}}/user_guide/audience/manage_audience/import_users). Sie sollten auch die [Benennungskonventionen für Events]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions) kennen.

### 4. Schritt: Anpassung nach Ihren Wünschen {#step-4-they-customize-based-on-what-you-want}

Wenn Sie Dinge wie API-getriggerte Starts und Connected-Content beabsichtigen, besprechen Sie das mit Ihrem Braze-Ansprechpartner und Ihrem Entwicklerteam, damit Sie auch Daten von außerhalb Ihrer App und Braze in Ihren Nachrichten verwenden können.

### 5. Schritt: Gemeinsame QA Ihrer Implementierung {#step-5-you-both-perform-qa-on-your-implementation}

Arbeiten Sie mit Ihrem Entwicklerteam zusammen, um sicherzustellen, dass alles funktioniert. Versenden Sie [Testnachrichten]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages), nutzen Sie unsere [Test-Apps für Android]({{site.baseurl}}/developer_guide/references?tab=android) und [Test-Apps für iOS]({{site.baseurl}}/developer_guide/references?tab=swift) und gehen Sie auf Nummer sicher, bevor Sie mit dem Versand beginnen!

Wir haben sogar spezielle Anweisungen zum [Testen Ihrer Android- oder FireOS-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration#test-your-basic-integration) und zum Testen von [Push für iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing).

## Nach der Implementierung {#after-implementation}

Denken Sie daran, dass eine abgeschlossene Implementierung nicht automatisch bedeutet, dass Sie Millionen von Nachrichten auf einmal versenden können. Das Versenden von einer Million Push-Nachrichten könnte Ihre App zum Absturz bringen, wenn alle Nutzer:innen gleichzeitig auf denselben Link klicken. Wir empfehlen Ihnen, die Kapazität Ihrer internen Infrastruktur für die Bearbeitung von Anfragen von Braze zu besprechen, bevor Sie auf die Schaltfläche **Senden** klicken. Auf dieser Grundlage können Sie dann Ihre [Rate-Limits]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) festlegen.

![Logo der Braze-Firebrands-Community]({% image_buster /assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Wenn Sie sich mit Braze vertraut gemacht haben, können Sie bei Braze Firebrands mitmachen! Braze Firebrands ist unsere geschäftskunden-Engagement-Community. Wir wollen Vordenker:innen und Pionier:innen zusammenbringen, die Braze nutzen, um ihr Kundenerlebnis und ihr Marketing zu modernisieren. Möchten Sie mehr erfahren? [Jetzt mitmachen](https://brazefirebrands.splashthat.com/).