---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für September 2019."
---

# September 2019

## Braze App innerhalb von OneLogin {#braze-app-within-onelogin}

Kund:innen können innerhalb von [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin) einfach Braze für SP- oder IdP-initiierte Anmeldungen suchen und auswählen. Das bedeutet, dass Kund:innen keine angepasste Anwendung in OneLogin hinzufügen müssen. Dies sollte dazu führen, dass bestimmte Einstellungen wie Attribute, die seit der Einführung von SAML SSO aufgetaucht sind, vorausgefüllt werden.

## Rokt Calendar-Partnerschaft {#rokt-calendar-partnership}

[Rokt Calendar]({{site.baseurl}}/partners/home) bietet Braze-Kund:innen die Möglichkeit, ihre personalisierten Marketing-Initiativen aufeinander abzustimmen und personalisierte Inhalte auf den Kalender der Endnutzer:innen auszuweiten. So wird das Erlebnis für die Endnutzer:innen nahtloser und die Kundenbindung an die Dienste unserer Kund:innen wird weiter ausgebaut. Kund:innen werden in der Lage sein, …

- eine Kalendereinladung über die Braze-Plattform zu senden, um ein Datum vorzumerken und die Kommunikation zu erweitern,
- eine bestehende Einladung zu aktualisieren, wenn sich der Inhalt des Ereignisses geändert hat.

## Passkit-Partnerschaft {#passkit-partnership}

Mit [Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit) können Braze-Kund:innen ihr Customer-Engagement auf mobile Wallets ausweiten. Sie werden in der Lage sein, personalisierte Wallet-Campaigns zu erstellen und dabei die leistungsstarke Segmentierung von Braze zu nutzen und neben Kanälen wie Push, In-App-Nachrichten und mehr zu orchestrieren.

## Rückgabe des Dispatch-ID-Werts über Messaging-Endpunkte {#dispatch-id-value-return-via-messaging-endpoints}

Die `dispatch_id` einer Nachricht wird in den folgenden Antworten der Messaging-Endpunkte enthalten sein:
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#send-messages-immediately-using-the-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging)

Auf diese Weise können Kund:innen, die transaktionales Messaging nutzen, den Aufruf über Currents zurückverfolgen.

## Canvas Changelogs

Haben Sie sich schon einmal gefragt, wer in Ihrem Konto an einem Canvas arbeitet? Dann haben wir gute Neuigkeiten! Sie können jetzt auf Canvas Changelogs zugreifen.

![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog1.png %})
![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog2.png %})