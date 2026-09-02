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

Vielleicht denken Sie: „Meine Entwickler:innen sind großartig! Sie können alles, also überlasse ich es normalerweise einfach ihnen!“ Und das stimmt wahrscheinlich auch! Aber es gibt keinen Grund, warum Sie nicht wissen sollten, was sie hinter den Kulissen tun. Tatsächlich würde es dem gesamten Prozess helfen, wenn Sie wüssten, wann Sie mit Informationen einspringen sollten und worauf Sie achten müssen, wenn sie fragen: „Können Sie mir den API-Schlüssel und den API-Endpunkt schicken?“

Was tun sie also, wenn sie Braze in Ihre App oder Website integrieren? Schön, dass Sie fragen!

### Schritt 1: Sie implementieren das Braze SDK {#step-1-they-implement-the-braze-sdk}

Das Braze SDK (Software-Development-Kit) ist die Methode, mit der wir Informationen an Ihre App oder Website senden und von dort empfangen. Ihre Entwickler:innen verbinden im Wesentlichen unsere Apps miteinander. Dafür benötigen sie einige wichtige Informationen:

* Ihre [API-Schlüssel]({{site.baseurl}}/api/basics)
* Ihren [SDK-Endpunkt]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)
  * Braze stellt keine angepassten Endpunkte mehr bereit, verwenden Sie daher die vordefinierten SDK-Endpunkte. Falls Sie einen bereits bestehenden angepassten Endpunkt erhalten haben, finden Sie hier die Einrichtungsschritte für die Integration mit [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) und [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#initializing-the-sdk).

Sie können diese Informationen entweder direkt weitergeben oder ihnen Zugang zu Braze gewähren, indem Sie ein Konto für sie erstellen.

{% alert warning %}
Stellen Sie sicher, dass Sie und Ihre Entwickler:innen die Zugangsdaten des Unternehmens in Braze nicht unwissentlich oder unbeabsichtigt ändern, da dies zu Problemen während des Implementierungsprozesses führen oder einen oder mehrere von Ihnen aus Ihren Konten aussperren könnte.
{% endalert %}

### Schritt 2: Sie implementieren Ihre gewünschten Messaging-Kanäle {#step-2-they-implement-your-desired-messaging-channels}

Braze bietet viele Möglichkeiten, um mit Ihren Nutzer:innen in Kontakt zu treten, und jede erfordert eine eigene Einrichtung oder Anpassung, damit sie so funktioniert, wie Sie es möchten. Hier wird die Kommunikation mit Ihren Entwickler:innen entscheidend.

Teilen Sie Ihren Entwickler:innen unbedingt mit, welche Kanäle Sie nutzen möchten, damit die Implementierung effizient und in der richtigen Reihenfolge erfolgt.

| Kanal | Details |
|---|---|
| In-App-Nachrichten | Erfordert die SDK-Implementierung sowie diese kanalspezifischen Schritte. |
| Push | Erfordert die SDK-Implementierung für den ordnungsgemäßen Umgang mit Messaging-Zugangsdaten und Push-Token. |
| E-Mail | Dies ist ein völlig anderer Prozess. Weitere Informationen zur Integration finden Sie im Abschnitt [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup). |
| Content Cards | Um mit [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards) zu beginnen, wenden Sie sich an Ihren Braze Customer-Success-Manager. |
| SMS & MMS | Weitere Informationen zur Integration finden Sie im Abschnitt [SMS-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending). |
| Webhooks | Erfordert die SDK-Implementierung sowie kanalspezifische Schritte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Sie implementieren Ihre gewünschten Messaging-Kanäle" }

{% alert tip %}
Sie können Braze nutzen, um barrierefreie Messaging-Kampagnen über jeden Kanal zu erstellen. Arbeiten Sie mit Ihren Entwickler:innen zusammen, um sicherzustellen, dass Sie die Barrierefreiheitsstandards in Ihrer Implementierung einhalten.
{% endalert %}

### Schritt 3: Sie richten Ihre Daten ein {#step-3-they-set-up-your-data}

Braze ist kein Einzweck-Werkzeug. Es geht nicht nur um das Versenden von E-Mails oder Push-Nachrichten. Es geht darum, personalisierte Customer Journeys zu erstellen, die für jede Nutzerin und jeden Nutzer einzigartig sind. Die Customer Journeys basieren auf ihren Aktionen innerhalb Ihrer App oder Website, und Sie legen fest, was diese sind! Die nächste Aufgabe Ihrer Entwickler:innen besteht darin sicherzustellen, dass Aktionen innerhalb Ihrer App oder Website von Braze erfasst werden.

Was müssen Sie also tun, um ihnen diese Informationen bereitzustellen?

1. Arbeiten Sie mit Ihrem Marketing-Team zusammen, um Campaigns, Ziele, Attribute und Events zu definieren, die Sie verfolgen möchten. Definieren Sie diese Anwendungsfälle und teilen Sie sie mit Ihren Teams.
2. Definieren Sie Ihre Anforderungen an angepasste Daten ([angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) usw.).
3. Besprechen Sie anschließend, wie diese Daten getrackt werden sollen (z. B. über das SDK ausgelöst).
4. Legen Sie fest, wie viele [Workspaces]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces) Sie benötigen. Ihre Entwickler:innen müssen wissen, wie sie diese Workspaces [testen und konfigurieren]({{site.baseurl}}/user_guide/get_started/workspaces) können.

Sobald Sie all diese Informationen zusammengetragen haben, teilen Sie sie mit Ihren Entwickler:innen. Sie werden diese Informationen nutzen und Ihre [angepassten Daten]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) implementieren. Möglicherweise müssen Sie auch [einige Nutzer:innen importieren]({{site.baseurl}}/user_guide/audience/manage_audience/import_users). Darüber hinaus sollten Sie sich mit den [Event-Namenskonventionen]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions) vertraut machen.

### Schritt 4: Sie passen auf Basis Ihrer Anforderungen an {#step-4-they-customize-based-on-what-you-want}

Wenn Sie Funktionen wie API-getriggertes Senden und Connected Content nutzen möchten, besprechen Sie dies sowohl mit Ihrem Braze-Kontakt als auch mit Ihren Entwickler:innen, um sicherzustellen, dass Daten, die sich außerhalb Ihrer App und Braze befinden, in Ihre Nachrichten einfließen können.

### Schritt 5: Sie führen gemeinsam eine QA Ihrer Implementierung durch {#step-5-you-both-perform-qa-on-your-implementation}

Arbeiten Sie mit Ihren Entwickler:innen zusammen, um sicherzustellen, dass alles funktioniert. Senden Sie [Testnachrichten]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages), verwenden Sie unsere [Test-Apps für Android]({{site.baseurl}}/developer_guide/references?tab=android) und [Test-Apps für iOS]({{site.baseurl}}/developer_guide/references?tab=swift), und überprüfen Sie jeden Punkt, bevor Sie mit dem Senden beginnen!

Wir haben sogar spezielle Anleitungen zum [Testen Ihrer Android- oder FireOS-Integration]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android) und zum Testen von [Push für iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing).

## Nach der Implementierung {#after-implementation}

Beachten Sie, dass das Ende der Implementierung nicht gleichbedeutend mit dem grünen Licht ist, sofort eine Million Nachrichten auf einmal zu versenden. Der Versand einer Million Push-Nachrichten könnte Ihre App zum Absturz bringen, wenn alle Kund:innen gleichzeitig auf denselben Link klicken. Wir empfehlen, vor dem Klicken auf den **Senden**-Button die Kapazität Ihres internen Setups für die Verarbeitung von Anfragen von Braze zu besprechen. Anschließend können Sie Ihr [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) entsprechend festlegen.

![Braze Firebrands Community-Logo]({% image_buster /assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Wenn Sie sich mit der Nutzung von Braze vertraut gemacht haben, sollten Sie in Betracht ziehen, ein Braze Firebrand zu werden! Mit Braze Firebrands, unserer Customer-Engagement-Community, bauen wir eine Gemeinschaft von Vorreiter:innen auf, die Braze nutzen, um ihr Kundenerlebnis und Marketing zu modernisieren. Möchten Sie mehr erfahren? [Jetzt beitreten](https://brazefirebrands.splashthat.com/).