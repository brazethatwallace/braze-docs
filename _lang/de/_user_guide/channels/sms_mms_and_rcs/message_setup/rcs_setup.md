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

Die Einrichtung von RCS ist genauso unkompliziert wie die Einrichtung von SMS. Lesen Sie weiter, um zu erfahren, wie Sie mit dem Versand von reichhaltigen und interaktiven Nachrichten beginnen können.

## 1. Schritt: Eignungskriterien erfüllen {#step-1-meet-the-eligibility-criteria}

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
3. Sie müssen eine oder mehrere RCS-SKUs in Ihrem Vertrag erwerben.

## 2. Schritt: Einen RCS-verifizierten Sender registrieren {#step-2-register-an-rcs-verified-sender}

Bevor Sie RCS-Nachrichten senden können, müssen Sie einen RCS-verifizierten Sender registrieren. Dies ist die Darstellung Ihrer Marke, die Nutzer:innen auf ihren Mobilgeräten sehen werden, einschließlich des Namens Ihrer Marke, Ihres Logos, eines Verifizierungs-Badges und eines optionalen Slogans. Der RCS-verifizierte Sender stärkt das Vertrauen der Kund:innen und bestätigt, dass Ihre Nachrichten von einer authentifizierten Quelle stammen.

![Ein Beispiel für einen RCS-verifizierten Sender in einer RCS-Nachricht namens „Cat Failz Cafe“.]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Nachdem Sie die RCS-SKU(s) zu Ihrem Bestellformular hinzugefügt haben, wird Braze benachrichtigt und kontaktiert Sie mit den Informationen zur RCS-Sender-Registrierung. Das Format dieser Informationen hängt von den Ländern ab, in die Sie RCS-Nachrichten senden möchten.

Wenn Sie Ihre ausgefüllten Formulare an Braze übermittelt haben, schließen wir den Registrierungsprozess in Ihrem Namen ab.

### Schritt 2.1: SMS-Fallbacks für RCS-Abo-Gruppen einrichten {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

Da die aktuelle Carrier-Abdeckung je nach Land variiert und die Hardware- und Software-Unterstützung der Nutzer:innen individuell unterschiedlich ist, ist SMS-Fallback eine Schlüsselkomponente für ein erfolgreiches RCS-Programm. Wir empfehlen, SMS-Fallback einzurichten. Wenn ein Carrier RCS nicht unterstützt oder das Gerät einer Nutzerin oder eines Nutzers keine RCS-Nachrichten empfangen kann, wird Ihre Nachricht durch SMS-Fallback trotzdem zugestellt, sodass Sie keinen wichtigen Moment mit Ihren Nutzer:innen verpassen.

Wir empfehlen dringend, Ihre aktuelle SMS-Opt-in-Erfahrung, Abo-Gruppen und Zielgruppen-Segmentierung zu überprüfen, bevor Sie Ihre erste RCS-Kampagne bereitstellen. Bei Bedarf steht Ihnen Ihr Customer-Success-Manager jederzeit zur Verfügung, um Sie zu beraten und durch den Einrichtungsprozess zu begleiten.

#### Wie SMS-Fallback mit Ereignissen und Segmentierung funktioniert {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab Ereignisverhalten %}

Wenn Sie SMS-Fallback mit RCS verwenden, hängt das Ereignisverhalten davon ab, ob die Nachricht erfolgreich über RCS gesendet wird oder auf SMS zurückfällt:

- **Wenn der RCS-Versand erfolgreich ist:** Sie erhalten ein RCS-Sendeereignis und ein RCS-Zustellungsereignis.
- **Wenn der RCS-Versand auf SMS zurückfällt:** Sie erhalten ein RCS-Sendeereignis, ein RCS-Ablehnungsereignis und ein SMS-Zustellungsereignis. Das SMS-Zustellungsereignis hat `IS_SMS_FALLBACK=TRUE`.

{% endtab %}
{% tab Segmentierungsverhalten %}

Für SMS und RCS werden [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) für empfangene Nachrichten (wie [Nachricht von Campaign erhalten]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#received-message-from-campaign) und [Nachricht von Canvas-Schritt erhalten]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#received-message-from-canvas-step)) ausgewertet, wenn eine Nachricht gesendet wird, nicht wenn sie das Gerät der Nutzerin oder des Nutzers erreicht. Bei aktiviertem SMS-Fallback können Nutzer:innen diese Filter weiterhin erfüllen, wenn eine RCS-Nachricht abgelehnt wird und auf SMS zurückfällt, oder wenn die Fallback-SMS nicht auf dem Gerät der Nutzerin oder des Nutzers zugestellt wird.

{% endtab %}
{% endtabs %}

### Zeitrahmen für die Carrier-Genehmigung {#timeline-for-carrier-approval}

Der Zeitrahmen für die Carrier-Genehmigung variiert je nach Land und kann auch innerhalb eines Landes unterschiedlich sein. Beachten Sie, dass sich der RCS-Markt noch in den Anfängen befindet, sodass sich die Prozesse bei Carriern und Aggregatoren schnell weiterentwickeln. In den Vereinigten Staaten schätzt Braze, dass die Bearbeitungszeit für die Carrier-Genehmigung eines RCS-verifizierten Senders in der Regel im Bereich von 4–6 Wochen liegt, wobei ein Test-Sender typischerweise innerhalb einer Woche genehmigt wird.

Wenn Ihr RCS-verifizierter Sender genehmigt wurde, aktualisiert unser Operations-Team Ihre Abo-Gruppen nach Bedarf, um zu bestätigen, dass der RCS-Sender darin enthalten ist.

## 3. Schritt: Abo-Gruppen einrichten {#step-3-set-up-subscription-groups}

Abhängig von Ihrer Integration kann Braze RCS-verifizierte Sender zu Ihren bestehenden SMS-Abo-Gruppen hinzufügen oder neue einrichten. Detaillierte Einrichtungsanweisungen finden Sie unter [SMS- und RCS-Abo-Gruppen]({{site.baseurl}}/sms_rcs_subscription_groups/).

## SMS-Traffic zu RCS migrieren {#migrating-sms-traffic-to-rcs}

Wenn Sie separate SMS- und RCS-Abo-Gruppen haben, können Sie Nutzer:innen mithilfe eines einstufigen Canvas von SMS zu RCS migrieren.

Braze empfiehlt, den RCS-Versand zunächst mit kleineren Nutzervolumen zu testen und im Laufe der Zeit mehr Nutzer:innen in die RCS-Abo-Gruppe zu migrieren. Wenn Sie beispielsweise 1.000.000 Nutzer:innen haben, die eine SMS-Abo-Gruppe abonniert haben, könnte dies so aussehen, dass Sie zunächst alle Nutzer:innen in die neue Abo-Gruppe migrieren und dann ein kleineres Segment von 50.000 bis 100.000 (5–10 %) auswählen, um die RCS-Nachrichten zu testen.

### 1. Schritt: Einen Canvas erstellen und den Entry-Zeitplan ausfüllen {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Erstellen Sie einen Canvas und geben Sie ihm einen leicht identifizierbaren Namen (z. B. „SMS-RCS Abo-Gruppen-Nutzertransfer“). Planen Sie den Canvas dann zu einem für Sie passenden Zeitpunkt.

### 2. Schritt: Ihre Zielgruppe definieren {#step-2-define-your-audience}

Definieren Sie Ihre Zielgruppe mit einer der folgenden Methoden. Gehen Sie dann zum Schritt **Sendeeinstellungen** und wählen Sie **Nutzer:innen, die abonniert oder angemeldet sind**.

| Methode | Beschreibung |
|---------|-------------|
| **Ein Segment erstellen** | Erstellen Sie ein Segment, das alle Nutzer:innen in einer Abo-Gruppe oder eine Teilmenge mithilfe von Segmentierungsfiltern enthält (z. B. zufällige 5–10 %). Segmente werden vor jedem Versand aktualisiert, um Ihre aktuelle Nutzerbasis widerzuspiegeln. |
| **Kampagnen- oder Canvas-Filter anwenden** | Verfeinern Sie die Zielgruppe im Schritt **Zielgruppe** Ihrer Kampagne oder Ihres Canvas. Passen Sie die Targeting-Optionen an, ohne die Seite zu verlassen, für zusätzliche Flexibilität. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2. Schritt: Ihre Zielgruppe definieren" }

### 3. Schritt: Einen Nutzeraktualisierungs-Schritt konfigurieren {#step-3-configure-a-user-update-step}

Fügen Sie Ihrem Canvas einen Nutzeraktualisierungs-Schritt hinzu. Öffnen Sie im Schritt den **Advanced JSON Editor** und geben Sie Folgendes ein (für das Feld zur eindeutigen Nutzeridentifikation empfehlen wir die Verwendung des Feldes `braze_id`):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

![„User Update Object“, das den zuvor genannten JSON-Code enthält.]({% image_buster /assets/img/sms/user_update_object.png %})

### 4. Schritt: Den Canvas testen {#step-4-test-the-canvas}

Wir empfehlen dringend, [Ihren Canvas zu testen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases/), um sicherzustellen, dass er wie erwartet funktioniert, bevor Sie ihn an Ihre breitere Zielgruppe senden.

### 5. Schritt: Ihren Canvas starten {#step-5-launch-your-canvas}

Nachdem Sie Ihren Canvas erfolgreich getestet haben, starten Sie ihn für Ihre Teilmenge von Nutzer:innen!

Um zu bestätigen, dass Ihre Nutzer:innen erfolgreich migriert wurden, empfehlen wir, einige einzelne Nutzerprofile zu überprüfen, die aktualisiert wurden. Suchen Sie im Tab **Engagement** nach **Contact Settings** und scrollen Sie, um die Abo-Gruppen anzuzeigen, die die Nutzerin oder der Nutzer abonniert hat. Der Schalter für die RCS-Abo-Gruppe sollte jetzt aktiviert sein.