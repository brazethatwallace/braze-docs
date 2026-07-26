---
nav_title: Abo-Gruppen
article_title: SMS- und RCS-Abo-Gruppen
page_order: 4
description: "Dieser Referenzartikel behandelt Abo-Gruppen, Abo-Status und den Einrichtungsprozess von Abo-Gruppen für SMS-, MMS- und RCS-Kanäle."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS

---

# SMS-, MMS- und RCS-Abo-Gruppen {#sms-mms-and-rcs-subscription-groups}

> Abo-Gruppen bilden die Grundlage für den Versand von SMS-, MMS- und RCS-Nachrichten über Braze. Eine Abo-Gruppe ist eine Sammlung von [Sendeentitäten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) (wie RCS-verifizierte Absender, SMS-Shortcodes, SMS-Langcodes oder alphanumerische SMS-Absender-IDs), die für einen bestimmten Nachrichtenzweck verwendet werden. Wenn eine Marke beispielsweise sowohl transaktionale als auch werbliche SMS-Nachrichten versenden möchte, müssen zwei Abo-Gruppen mit separaten Pools von Sendetelefonnummern in Ihrem Braze-Dashboard eingerichtet werden.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Abo-Gruppenstatus {#subscription-group-states}

Es gibt zwei Abo-Status für SMS- und RCS-Nutzer:innen: `subscribed` und `unsubscribed`. Der Abo-Status einer Nutzer:in befindet sich auf Abo-Gruppenebene und wird nicht über Abo-Gruppen hinweg geteilt. Das bedeutet, dass eine Nutzer:in bei einer transaktionalen Abo-Gruppe `subscribed` sein kann, aber bei einer werblichen `unsubscribed`. Für Marken stellt diese Trennung der Status sicher, dass sie weiterhin relevante SMS- und RCS-Nachrichten an ihre Nutzer:innen senden können.

| Status | Definition |
| --------- | ---------- |
| Abonniert | Nutzer:in ist für den Empfang von SMS und RCS aus einer bestimmten Abo-Gruppe angemeldet. Eine Nutzer:in kann abonniert werden, indem der Abo-Status über die Braze-Abo-API aktualisiert wird oder indem ein Opt-in-Schlüsselwort per SMS gesendet wird. Eine Nutzer:in muss bei einer SMS- oder RCS-Abo-Gruppe abonniert sein, um SMS, RCS oder beides zu empfangen. Wenn [Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) aktiviert ist, müssen Nutzer:innen ihre Opt-in-Absicht bestätigen, bevor ihr Abo-Status auf `Subscribed` aktualisiert wird. |
| Abgemeldet | Nutzer:in hat sich ausdrücklich vom Nachrichtenempfang Ihrer SMS- und RCS-Abo-Gruppe und den darin enthaltenen Sendetelefonnummern abgemeldet. Die Abmeldung kann durch Senden eines Opt-out-Schlüsselworts per SMS erfolgen, oder Sie können Nutzer:innen über die [Braze-Abo-API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) abmelden. Nutzer:innen, die von einer SMS- und RCS-Abo-Gruppe abgemeldet sind, erhalten keine SMS oder RCS mehr von Sendetelefonnummern, die zu dieser Abo-Gruppe gehören.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abo-Gruppenstatus" }

### Status einer Nutzer:in festlegen {#set-a-users-state}

Wenn eine Telefonnummer in einem Nutzerprofil aktualisiert wird, übernimmt die neue Telefonnummer den Abo-Gruppenstatus der Nutzer:in. Wenn die Telefonnummer auf eine Nummer aktualisiert wird, die bereits in Braze existiert, wird der Abo-Status dieser bestehenden Telefonnummer übernommen.

Wenn beispielsweise Nutzer:in A eine Telefonnummer hat, die bei mehreren Abo-Gruppen abonniert ist, und diese Telefonnummer dann zu Nutzer:in B hinzugefügt wird, wird Nutzer:in B bei denselben Abo-Gruppen abonniert. Um zu verhindern, dass eine Nutzer:in die bestehenden Abos übernimmt, können Sie die Abo-Gruppen der alten Nummer über die Braze REST API zurücksetzen, wenn eine Nutzer:in die Nummer ändert. Wenn mehrere Nutzer:innen diese Telefonnummer teilen, werden alle abgemeldet.

Um den Abo-Gruppenstatus einer Nutzer:in festzulegen, verwenden Sie eine der folgenden Methoden:

- **REST API:** Nutzerprofile können programmatisch über den [`/subscription/status/set`-Endpunkt]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) mithilfe der Braze REST API festgelegt werden.
- **SDK-Integration:** Nutzer:innen können über die Methode `addToSubscriptionGroup` für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) oder [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup) zu einer E-Mail- oder SMS- und RCS-Abo-Gruppe hinzugefügt werden.
- **Telefonnummernerfassung per IAM-Formular:** Nutzertelefonnummern können über das Telefonnummernerfassungs-Template im Drag-and-Drop-Editor für In-App-Nachrichten erfasst werden.
- **Automatische Verarbeitung bei Opt-in/Opt-out:** Wenn Nutzer:innen ein Standard-Opt-in- oder Opt-out-[Schlüsselwort]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) per SMS senden, setzt und aktualisiert Braze den Abo-Status der Nutzer:innen automatisch.
- **Nutzerimport:** Nutzer:innen können über **Nutzer:innen importieren** zu E-Mail- oder SMS- und RCS-Abo-Gruppen hinzugefügt werden. Beim Aktualisieren des Abo-Gruppenstatus müssen diese zwei Spalten in Ihrer CSV-Datei vorhanden sein: `subscription_group_id` und `subscription_state`. Weitere Informationen finden Sie unter [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).

#### Status einer Nutzer:in in einem Canvas aktualisieren {#update-a-users-state-in-a-canvas}

Wenn Sie den Abo-Gruppenstatus einer Nutzer:in als Teil eines Canvas-Flows aktualisieren, verwenden Sie einen [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt anstelle eines Webhooks. Der Nutzeraktualisierung-Schritt wartet, bis die Verarbeitung abgeschlossen ist, bevor die Nutzer:in zum nächsten Schritt weitergeleitet wird, sodass nachfolgende Messaging-Schritte den aktualisierten Abo-Status verwenden.

Wenn Sie einen Webhook zum Aktualisieren von Abo-Gruppen verwenden, wird die Nutzer:in weitergeleitet, sobald der Webhook gesendet wurde – nicht wenn die Abo-Änderung fertig verarbeitet ist. Dies kann eine Race-Condition verursachen, bei der ein nachfolgender SMS-Schritt ausgeführt wird, bevor die Nutzer:in abonniert ist, was dazu führt, dass die Nachricht für einen Teil der Nutzer:innen fehlschlägt. Wenn Sie einen Webhook verwenden müssen, fügen Sie vor dem nächsten Messaging-Schritt einen Verzögerungsschritt von mindestens 1 Minute hinzu.

#{% multi_lang_include api/orphaned_subscription_states.md %}

### Gruppe einer Nutzer:in prüfen {#check-a-users-group}

Um die Abo-Gruppe einer Nutzer:in zu prüfen, verwenden Sie eine der folgenden Methoden:

- **Nutzerprofil:** Auf einzelne Nutzerprofile kann über das Braze-Dashboard zugegriffen werden, indem Sie in der Seitenleiste **Nutzersuche** auswählen. Hier können Sie Nutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Nutzer-ID suchen. Innerhalb eines Nutzerprofils können Sie unter dem Tab „Engagement“ die SMS- und RCS-Abo-Gruppen einer Nutzer:in einsehen.
- **REST API:** Die Abo-Gruppen einzelner Nutzerprofile können über den [Endpunkt „Abo-Gruppen von Nutzer:innen auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) oder den [Endpunkt „Abo-Gruppenstatus der Nutzer:innen auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) mithilfe der Braze REST API eingesehen werden.

## Nachrichten mit einer Abo-Gruppe senden {#send-messages-with-a-subscription-group}

Um eine SMS- oder RCS-Campaign über Braze zu starten, wählen Sie eine Abo-Gruppe aus dem Dropdown-Menü **SMS/MMS/RCS Variants** aus. Nach der Auswahl wird automatisch ein Zielgruppenfilter zu Ihrer Campaign oder Ihrem Canvas hinzugefügt, der sicherstellt, dass nur Nutzer:innen, die bei der ausgewählten Abo-Gruppe `subscribed` sind, zur Zielgruppe gehören.

{% alert important %}
In Übereinstimmung mit internationalen [Telekommunikations-Compliance-Richtlinien und -Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) wird Braze niemals SMS oder RCS an Nutzer:innen senden, die nicht bei der ausgewählten Abo-Gruppe abonniert sind.
{% endalert %}

![SMS-Composer mit geöffnetem Abo-Gruppen-Dropdown und „Messaging Service A for SMS“ von der Nutzer:in hervorgehoben.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Best Practices für SMS-Abo-Gruppen {#sms-subscription-group-best-practices}

Entwerfen Sie separate SMS-Abo-Gruppen für jeden Nachrichtenzweck (z. B. transaktional versus Marketing) und für jeden Workspace. Wenn Sie in mehreren Ländern tätig sind, sollten Sie separate Gruppen nach Region in Betracht ziehen, um lokale Compliance-Regeln zu unterstützen – beispielsweise die Einschränkungen Brasiliens für werbliche Sendefenster.

## Abo-Gruppen aktivieren {#enable-subscription-groups}

Um Abo-Gruppen für SMS, MMS oder RCS zu aktivieren, beachten Sie Folgendes:

{% tabs local %}
{% tab SMS %}
Während Ihres SMS-Onboarding-Prozesses richtet ein Braze-Onboarding-Manager Abo-Gruppen für Ihr Dashboard-Konto ein. Er wird mit Ihnen zusammenarbeiten, um festzulegen, wie viele Abo-Gruppen Sie benötigen, und die entsprechenden Sendetelefonnummern zu Ihren Abo-Gruppen hinzufügen. Die Zeitrahmen für die Einrichtung einer Abo-Gruppe hängen von der Art der Telefonnummern ab, die Sie hinzufügen. Beispielsweise können Shortcode-Anträge zwischen 8 und 12 Wochen dauern, während Langcodes innerhalb eines Tages eingerichtet werden können. Wenn Sie Fragen zur Einrichtung Ihres Braze-Dashboards haben, wenden Sie sich an Ihre Braze-Vertretung für Support.
{% endtab %}

{% tab MMS %}
Um eine MMS-Nachricht zu senden, muss mindestens eine Nummer in Ihrer Abo-Gruppe für den MMS-Versand aktiviert sein. Dies wird durch ein Tag neben der Abo-Gruppe angezeigt.

![Abo-Gruppen-Dropdown mit hervorgehobenem „Messaging Service A for SMS“. Der Eintrag ist mit dem Tag „MMS“ versehen.]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Ein RCS-verifizierter Absender muss in Ihrer Abo-Gruppe vorhanden sein, bevor Sie eine RCS-Nachricht senden können.

Es gibt zwei Möglichkeiten, einen RCS-verifizierten Absender hinzuzufügen:
- Zu einer bestehenden Abo-Gruppe hinzufügen
- Eine neue RCS-Abo-Gruppe erstellen
Die Wahl hängt weitgehend von den RCS-Anwendungsfällen ab, die Sie interessieren.

Je nach Ihrer Integration kann Braze RCS-verifizierte Absender zu Ihren bestehenden SMS-Abo-Gruppen hinzufügen oder neue Abo-Gruppen für Sie einrichten. In beiden Fällen wird Ihr geschäftskunden-Success-Manager Sie durch ein nahtloses und effizientes SMS-Traffic-Upgrade begleiten.
{% endtab %}
{% endtabs %}

## Opt-outs in natürlicher Sprache in der Agentenkonsole verarbeiten {#handle-natural-language-opt-outs-in-the-agent-console}

Für ein umfassendes Abo-Management können Sie Opt-out-Absichten erfassen, die außerhalb von Standard- oder angepassten Schlüsselwörtern liegen (z. B. „Bitte schreiben Sie mir nicht mehr“). Durch das Erstellen eines KI-Agenten können Sie Sentimentanalyse nutzen, um diese Anfragen automatisch zu erkennen und darauf zu reagieren.

### Einrichtung {#setup}

1. Erstellen Sie in der [Agentenkonsole]({{site.baseurl}}/user_guide/brazeai/agents) einen „SMS-Sentimentanalyse-Agenten“.

{% alert tip %}
Verwenden Sie [Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), um bei der anfänglichen Agentenkonfiguration zu unterstützen.
{% endalert %}

{: start="2"}
2. Erstellen Sie einen aktionsbasierten Canvas, der durch **Send an SMS inbound message** ausgelöst wird, innerhalb der Schlüsselwortkategorie **Other**.
3. Fügen Sie den [Agentenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) zum Canvas hinzu, um die Opt-out-Absicht zu erkennen.
4. Fügen Sie einen nachfolgenden SMS-[Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) hinzu, um die Anfrage zu bestätigen: „Es sieht so aus, als möchten Sie sich von SMS abmelden, daher werden wir Sie abmelden. Falls dies ein Fehler war, senden Sie START, um sich wieder anzumelden.“
5. Fügen Sie einen [Nutzeraktualisierung-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) hinzu, um den Status der Nutzer:in in der jeweiligen SMS-Abo-Gruppe auf „Abgemeldet“ zu ändern.

{% alert note %}
Die Nutzung der Agentenkonsole verbraucht Message oder Action Credits.
{% endalert %}

## SMS-Traffic zu RCS migrieren {#migrate-sms-traffic-to-rcs}

Wenn Sie separate SMS- und RCS-Abo-Gruppen haben, können Sie Nutzer:innen mithilfe eines einstufigen Canvas von SMS zu RCS migrieren.

Braze empfiehlt, zunächst RCS an kleinere Nutzervolumen zu testen und im Laufe der Zeit mehr Nutzer:innen in die RCS-Abo-Gruppe zu migrieren. Wenn Sie beispielsweise 1.000.000 Nutzer:innen haben, die bei einer SMS-Abo-Gruppe abonniert sind, könnte dies so aussehen: Zuerst alle Nutzer:innen in die neue Abo-Gruppe migrieren und dann ein kleineres Segment von 50.000 bis 100.000 (5–10 %) zum Testen der RCS-Nachrichten auswählen.

### Schritt 1: Canvas erstellen und den Entry-Zeitplan ausfüllen {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Erstellen Sie einen Canvas und geben Sie ihm einen leicht erkennbaren Namen (z. B. „SMS-RCS Abo-Gruppen-Nutzertransfer“). Planen Sie die Campaign dann zu einem für Sie passenden Zeitpunkt.

### Schritt 2: Zielgruppe definieren {#step-2-define-your-audience}
{: #step-2-define-your-audience}

Definieren Sie Ihre Zielgruppe mit einer der folgenden Methoden. Gehen Sie dann zum Schritt **Sendeeinstellungen** und wählen Sie **Nutzer:innen, die abonniert oder angemeldet sind**.

| Methode | Beschreibung |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Segment erstellen** | Erstellen Sie ein Segment, das alle Nutzer:innen in einer Abo-Gruppe oder eine Teilmenge mithilfe von Segmentierungsfiltern enthält (z. B. zufällige 5–10 %). Segmente werden vor jedem Versand aktualisiert, um Ihre aktuelle Nutzerbasis widerzuspiegeln. |
| **Campaign- oder Canvas-Filter anwenden** | Verfeinern Sie die Zielgruppe im Schritt **Zielgruppe** Ihrer Campaign oder Ihres Canvas. Passen Sie die Targeting-Optionen an, ohne die Seite zu verlassen, für zusätzliche Flexibilität. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Zielgruppe definieren" }

### Schritt 3: Nutzeraktualisierung-Schritt konfigurieren {#step-3-configure-a-user-update-step}

Fügen Sie Ihrem Canvas einen Nutzeraktualisierung-Schritt hinzu. Öffnen Sie im Schritt den **Advanced JSON Editor** und geben Sie Folgendes ein (für das Feld zur eindeutigen Nutzeridentifikation empfehlen wir die Verwendung des Feldes `braze_id`):

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

![„Nutzeraktualisierung-Objekt“ mit dem zuvor genannten JSON-Code.]({% image_buster /assets/img/sms/user_update_object.png %})

### Schritt 4: Canvas testen {#step-4-test-the-canvas}

Wir empfehlen dringend, [Ihren Canvas zu testen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases), um sicherzustellen, dass er wie erwartet funktioniert, bevor Sie ihn an Ihre breitere Zielgruppe senden.

### Schritt 5: Canvas starten {#step-5-launch-your-canvas}

Nachdem Sie Ihren Canvas erfolgreich getestet haben, starten Sie ihn für Ihre Teilmenge von Nutzer:innen!

Um zu bestätigen, dass Ihre Nutzer:innen erfolgreich migriert wurden, empfehlen wir, einige einzelne Nutzerprofile zu überprüfen, die aktualisiert wurden. Suchen Sie im Tab **Engagement** nach **Contact Settings** und scrollen Sie, um die Abo-Gruppen anzuzeigen, bei denen die Nutzer:in abonniert ist. Der Schalter für die RCS-Abo-Gruppe sollte jetzt aktiviert sein.

Informationen zur Einrichtung von RCS-Absendern und Abo-Gruppen finden Sie auch unter [RCS einrichten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Best Practices {#best-practices}

### Separate Abo-Gruppen festlegen {#designate-separate-subscription-groups}

- **Nachrichtentyp:** Erstellen Sie separate Abo-Gruppen für jeden Nachrichtentyp, z. B. transaktional und Marketing.
- **Workspace:** Erstellen Sie separate Abo-Gruppen für jeden Workspace, um Klarheit und Organisation zu gewährleisten.

Betrachten Sie das folgende Beispiel mit vier Abo-Gruppen über zwei Workspaces:

- **Produktions-Workspace**
  - Marketing – PROD für SMS
  - Transaktional – PROD für SMS
- **Entwicklungs-Workspace (zum Testen)**
  - Marketing – DEV für SMS
  - Transaktional – DEV für SMS

### Klare Namenskonventionen verwenden {#use-clear-naming-conventions}

Wählen Sie beschreibende und klare Abo-Gruppennamen, damit beim Erstellen von SMS-Campaigns die richtige Gruppe ausgewählt wird.

### Gruppen nach Land trennen {#separate-groups-by-country}

SMS-Vorschriften variieren je nach Land. Wir empfehlen, SMS-Abo-Gruppen nach Land zu trennen. Dies hilft Ihnen, Compliance-Standards in allen Regionen einzuhalten, in denen Sie Nachrichten versenden.

Für jede Abo-Gruppe können Sie außerdem unter **Geographic Permissions** eine Länder-Allowlist konfigurieren, sodass SMS, MMS und RCS nur an genehmigte Regionen gesendet werden. Weitere Informationen finden Sie unter [Geografische Berechtigungen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions).

In Brasilien ist es beispielsweise verboten, Marketing-Nachrichten außerhalb der Zeiten von 9:00 bis 21:00 Uhr Ortszeit zu versenden, und das Land erstreckt sich über drei Zeitzonen. Um diese Vorschriften einzuhalten, könnten Sie separate Gruppen für den Nachrichtenversand nach Brasilien und in die USA einrichten. Dies verhindert, dass Nutzer:innen in Brasilien Marketing-Nachrichten während verbotener Zeiten erhalten.