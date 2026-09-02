---
nav_title: "RCS-Einrichtung"
article_title: "RCS-Einrichtung"
page_order: 1
alias: /rcs_setup/
description: "Dieser Referenzartikel behandelt die Voraussetzungen, die erforderlich sind, um RCS einzurichten und in Betrieb zu nehmen."
page_type: reference
channel:
  - RCS
---

# RCS einrichten {#set-up-rcs}

> Dieser Artikel behandelt die Voraussetzungen, die erforderlich sind, um Ihren RCS-Kanal einzurichten und in Betrieb zu nehmen.

Die Einrichtung von RCS ist genauso unkompliziert wie die Einrichtung von Kurzmitteilungsdienst or SMS. Lesen Sie weiter, um zu erfahren, wie Sie mit dem Versand von reichhaltigen und interaktiven Nachrichten beginnen können.

## Schritt 1: Eignungskriterien erfüllen {#step-1-meet-the-eligibility-criteria}

Um mit Braze RCS-Nachrichten senden zu können, muss Ihr Unternehmen vorab drei Kriterien erfüllen:

1. Ihr aktueller Braze-Vertrag muss Message oder Action Credits beinhalten.
2. Sie müssen Ihre RCS-Nachrichten an eines der folgenden von Braze unterstützten Länder senden:
- Vereinigte Staaten
- Vereinigtes Königreich
- Deutschland
- Mexiko
- Schweden
- Spanien
- Singapur
- Brasilien
- Frankreich
- Italien
- Kolumbien
3. Sie müssen eine oder mehrere RCS-SKU(s) in Ihrem Vertrag erwerben.

## Schritt 2: Einen RCS-verifizierten Sender Registrierung or registrieren {#step-2-register-an-rcs-verified-sender}

Bevor Sie RCS-Nachrichten senden können, müssen Sie einen RCS-verifizierten Sender Registrierung or registrieren. Dies ist die Darstellung Ihrer Marke, die Nutzer:innen auf ihren Mobilgeräten sehen, einschließlich des Namens Ihrer Marke, Ihres Logos, eines Verifizierungs-Badges und eines optionalen Slogans. Der RCS-verifizierte Sender stärkt das Vertrauen der Kund:innen und bestätigt, dass Ihre Nachrichten von einer authentifizierten Quelle stammen.

![Ein Beispiel für einen RCS-verifizierten Sender in einer RCS-Nachricht namens „Cat Failz Cafe“.]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Nachdem Sie die RCS-SKU(s) zu Ihrem Bestellformular hinzugefügt haben, wird Braze benachrichtigt und kontaktiert Sie mit den Informationen zur RCS-Sender-Registrierung. Das Format dieser Informationen hängt von den Ländern ab, in die Sie RCS-Nachrichten senden möchten.

Wenn Sie Ihre ausgefüllten Formulare an Braze übermittelt haben, schließt Braze den Registrierungsprozess in Ihrem Namen ab.

### Schritt 2.1: Kurzmitteilungsdienst or SMS-Fallbacks für RCS-Abo-Gruppen einrichten {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

Da die aktuelle Carrier-Abdeckung je nach Land variiert und die Hardware- und Software-Unterstützung der Nutzer:innen individuell unterschiedlich ist, ist Kurzmitteilungsdienst or SMS-Fallback heute eine Schlüsselkomponente für ein erfolgreiches RCS-Programm. Wir empfehlen, Kurzmitteilungsdienst or SMS-Fallback einzurichten. Wenn ein Carrier RCS nicht unterstützt oder das Gerät einer Nutzerin oder eines Nutzers keine RCS-Nachrichten empfangen kann, sendet Kurzmitteilungsdienst or SMS-Fallback Ihre Nachricht trotzdem, sodass Sie keinen wichtigen Moment mit Ihren Nutzer:innen verpassen.

Wir empfehlen dringend, Ihre aktuelle Kurzmitteilungsdienst or SMS-Opt-in-Erfahrung, Abo-Gruppen und Zielgruppen-Segmentierung zu überprüfen, bevor Sie Ihre erste RCS-Campaign bereitstellen. Bei Bedarf steht Ihnen Ihr CSM or Customer-Success-Manager or Customer-Success-Manager:in jederzeit zur Verfügung, um Sie zu beraten und durch den Einrichtungsprozess zu begleiten.

#### Wie Kurzmitteilungsdienst or SMS-Fallback mit Events und Segmentierung funktioniert {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab Event-Verhalten %}

Wenn Sie Kurzmitteilungsdienst or SMS-Fallback mit RCS verwenden, hängt das Event-Verhalten davon ab, ob die Nachricht erfolgreich über RCS gesendet wird oder auf Kurzmitteilungsdienst or SMS zurückfällt:

- **Wenn der RCS-Versand erfolgreich ist:** Sie erhalten ein RCS-Versand-Event und ein RCS-Zustellungs-Event.
- **Wenn der RCS-Versand auf Kurzmitteilungsdienst or SMS zurückfällt:** Sie erhalten ein RCS-Versand-Event, ein RCS-Ablehnungs-Event und ein Kurzmitteilungsdienst or SMS-Zustellungs-Event. Das Kurzmitteilungsdienst or SMS-Zustellungs-Event hat `IS_SMS_FALLBACK=TRUE`.

{% endtab %}
{% tab Segmentierungsverhalten %}

Für Kurzmitteilungsdienst or SMS und RCS werten [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) für empfangene Nachrichten (wie [Nachricht von Campaign erhalten]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-campaign) und [Nachricht von Canvas-Schritt erhalten]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step)) aus, wann eine Nachricht gesendet wird, nicht wann sie das Gerät der Nutzerin oder des Nutzers erreicht. Bei aktiviertem Kurzmitteilungsdienst or SMS-Fallback können Nutzer:innen diese Filter weiterhin erfüllen, wenn eine RCS-Nachricht abgelehnt wird und auf Kurzmitteilungsdienst or SMS zurückfällt, oder wenn die Fallback-Kurzmitteilungsdienst or SMS nicht an das Gerät der Nutzerin oder des Nutzers zugestellt wird.

{% endtab %}
{% endtabs %}

### Zeitrahmen für die Carrier-Genehmigung {#timeline-for-carrier-approval}

Der Zeitrahmen für die Carrier-Genehmigung variiert je nach Land und kann auch innerhalb eines Landes unterschiedlich sein. Beachten Sie, dass sich der RCS-Markt noch in einem frühen Stadium befindet, sodass sich die Prozesse bei Carriern und Aggregatoren schnell weiterentwickeln. In den Vereinigten Staaten schätzt Braze, dass die Bearbeitungszeit für die Carrier-Genehmigung eines RCS-verifizierten Senders in der Regel im Bereich von 4–6 Wochen liegt, wobei ein Test-Sender in der Regel innerhalb einer Woche genehmigt wird.

Wenn Ihr RCS-verifizierter Sender genehmigt ist, aktualisiert unser Operations-Team Ihre Abo-Gruppen nach Bedarf, um zu bestätigen, dass der RCS-Sender in ihnen enthalten ist.

## Schritt 3: Abo-Gruppen einrichten {#step-3-set-up-subscription-groups}

Je nach Integration kann Braze RCS-verifizierte Absender zu Ihren bestehenden Kurzmitteilungsdienst or SMS-Abo-Gruppen hinzufügen oder neue einrichten. Detaillierte Einrichtungsanweisungen finden Sie unter [Kurzmitteilungsdienst or SMS- und RCS-Abo-Gruppen]({{site.baseurl}}/sms_rcs_subscription_groups).

## Kurzmitteilungsdienst or SMS-Datenverkehr zu RCS migrieren {#migrating-sms-traffic-to-rcs}

Wenn Sie separate Kurzmitteilungsdienst or SMS- und RCS-Abo-Gruppen haben, können Sie Nutzer:innen mithilfe eines einstufigen Canvas von Kurzmitteilungsdienst or SMS zu RCS migrieren. Eine Schritt-für-Schritt-Anleitung finden Sie unter [Kurzmitteilungsdienst or SMS-Datenverkehr zu RCS migrieren]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#migrate-sms-traffic-to-rcs).