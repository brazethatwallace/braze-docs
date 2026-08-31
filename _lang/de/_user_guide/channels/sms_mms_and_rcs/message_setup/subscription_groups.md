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

> Abo-Gruppen bilden die Grundlage für den Versand von SMS-, MMS- und RCS-Nachrichten über Braze. Eine Abo-Gruppe ist eine Sammlung von [Sendeentitäten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) – wie RCS-verifizierte Absender, SMS-Shortcodes, SMS-Langcodes oder alphanumerische SMS-Absender-IDs –, die für einen bestimmten Nachrichtenzweck verwendet werden (z. B. transaktional oder werblich). Einen kanalübergreifenden Überblick über Abo-Gruppen finden Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Abo-Gruppenstatus {#subscription-group-states}

Es gibt zwei Abo-Status für SMS- und RCS-Nutzer:innen: `subscribed` und `unsubscribed`. Der Abo-Status einer Nutzerin oder eines Nutzers ist auf Ebene der Abo-Gruppe angesiedelt und wird nicht über Abo-Gruppen hinweg geteilt. Das bedeutet, dass Nutzer:innen in einer transaktionalen Abo-Gruppe `subscribed` sein können, aber in einer Werbe-Abo-Gruppe `unsubscribed`. Für Marken stellt diese Trennung der Status sicher, dass sie weiterhin relevante SMS- und RCS-Nachrichten an ihre Nutzer:innen senden können.

| Status | Definition |
| --------- | ---------- |
| Abonniert | Die Nutzer:in ist abonniert, um SMS und RCS von einer bestimmten Abo-Gruppe zu erhalten. Nutzer:innen können abonniert werden, indem ihr Abo-Status über die Braze-Abo-API aktualisiert wird oder indem sie ein Opt-in-Schlüsselwort per SMS senden. Nutzer:innen müssen einer SMS- oder RCS-Abo-Gruppe abonniert sein, um SMS, RCS oder beides zu erhalten. Wenn [Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) aktiviert ist, müssen Nutzer:innen ihre Opt-in-Absicht bestätigen, bevor ihr Abo-Status auf `Subscribed` aktualisiert wird. |
| Abgemeldet | Die Nutzer:in hat sich ausdrücklich vom Messaging Ihrer SMS- und RCS-Abo-Gruppe und den Sende-Telefonnummern innerhalb der Abo-Gruppe abgemeldet. Nutzer:innen können sich abmelden, indem sie ein Opt-out-Schlüsselwort per SMS senden, oder Sie können Nutzer:innen über die [Braze-Abo-API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) abmelden. Nutzer:innen, die sich von einer SMS- und RCS-Abo-Gruppe abgemeldet haben, erhalten keine SMS oder RCS mehr von Sende-Telefonnummern, die zu dieser Abo-Gruppe gehören. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abo-Gruppenstatus" }

### Status von Nutzer:innen festlegen {#set-a-users-state}

Wenn eine Telefonnummer in einem Nutzerprofil aktualisiert wird, erbt die neue Telefonnummer den Abo-Gruppenstatus der Nutzer:in. Wenn die Telefonnummer auf eine Nummer aktualisiert wird, die bereits in Braze existiert, wird der Abo-Status dieser vorhandenen Telefonnummer übernommen.

Zum Beispiel: Wenn Nutzer:in A eine Telefonnummer hat, die in mehreren Abo-Gruppen abonniert ist, und diese Telefonnummer dann zu Nutzer:in B hinzugefügt wird, ist Nutzer:in B in denselben Abo-Gruppen abonniert. Um zu verhindern, dass Nutzer:innen die bestehenden Abos erben, können Sie die Abo-Gruppen der alten Nummer über die Braze REST API zurücksetzen, wenn Nutzer:innen ihre Nummer ändern. Wenn mehrere Nutzer:innen diese Telefonnummer teilen, werden alle abgemeldet.

Um den Abo-Gruppenstatus von Nutzer:innen festzulegen, verwenden Sie eine der folgenden Methoden:

- **REST API:** Verwenden Sie den [`/subscription/status/set`-Endpunkt]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/), um Nutzerprofile programmatisch über die Braze REST API festzulegen. Jede Anfrage kann zwischen 1 und 25 Abo-Gruppen enthalten.
- **SDK-Integration:** Nutzer:innen können über `addToSubscriptionGroup` und `removeFromSubscriptionGroup` zu einer E-Mail- oder SMS- und RCS-Abo-Gruppe hinzugefügt oder daraus entfernt werden – für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) oder [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup). SDK-Methoden ersetzen nicht die regulatorischen Opt-in- oder Opt-out-Abläufe, die über Schlüsselwörter und die REST API abgewickelt werden.
- **Telefonnummernerfassung per IAM-Formular:** Telefonnummern von Nutzer:innen können über das Telefonnummernerfassungs-Template im Drag-and-Drop-Editor für In-App-Nachrichten erfasst werden.
- **Automatische Verarbeitung bei Opt-in/Opt-out:** Wenn Nutzer:innen ein standardmäßiges Opt-in- oder Opt-out-[Schlüsselwort]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) per SMS senden, setzt und aktualisiert Braze den Abo-Status der Nutzer:innen automatisch.
- **Nutzerimport:** Nutzer:innen können über **Import Users** in E-Mail- oder SMS- und RCS-Abo-Gruppen hinzugefügt werden. Beim Aktualisieren des Abo-Gruppenstatus müssen diese zwei Spalten in Ihrer CSV vorhanden sein: `subscription_group_id` und `subscription_state`. Weitere Informationen finden Sie unter [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).
- **Braze-Dashboard:** Wählen Sie **User Search** in der Seitenleiste, öffnen Sie das Profil von Nutzer:innen und aktualisieren Sie SMS- oder RCS-Abo-Gruppen unter **Contact Settings** auf dem Tab **Engagement**.
- **Cloud Data Ingestion (CDI):** Fügen Sie `subscription_group_id` und `subscription_state` in synchronisierten Zeilen ein. Siehe [Tabelleneinrichtung für Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).
- **Nutzeraktualisierungsschritt:** Aktualisieren Sie den Abo-Status in einem Canvas mit einem [Nutzeraktualisierungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Siehe [Status von Nutzer:innen in einem Canvas aktualisieren](#update-a-users-state-in-a-canvas) für Hinweise zum Timing.

#### Status von Nutzer:innen in einem Canvas aktualisieren {#update-a-users-state-in-a-canvas}

Wenn Sie den Abo-Gruppenstatus von Nutzer:innen als Teil eines Canvas-Flows aktualisieren, verwenden Sie einen [Nutzeraktualisierungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) anstelle eines Webhooks. Der Nutzeraktualisierungsschritt wartet, bis die Verarbeitung abgeschlossen ist, bevor die Nutzer:innen zum nächsten Schritt weitergeleitet werden, sodass nachfolgende Messaging-Schritte den aktualisierten Abo-Status verwenden.

Wenn Sie einen Webhook verwenden, um Abo-Gruppen zu aktualisieren, werden die Nutzer:innen weitergeleitet, sobald der Webhook gesendet wurde – nicht wenn die Abo-Änderung fertig verarbeitet ist. Dies kann eine Race-Condition verursachen, bei der ein nachfolgender SMS-Schritt ausgeführt wird, bevor die Nutzer:innen abonniert sind, wodurch die Nachricht für einen Teil der Nutzer:innen fehlschlägt. Wenn Sie einen Webhook verwenden müssen, fügen Sie vor dem nächsten Messaging-Schritt einen Verzögerungsschritt von mindestens 1 Minute hinzu.

{% multi_lang_include api/orphaned_subscription_states.md %}

### Abo-Gruppe von Nutzer:innen prüfen {#check-a-users-group}

Um die Abo-Gruppe von Nutzer:innen zu prüfen, verwenden Sie eine der folgenden Methoden:

- **Nutzerprofil:** Auf einzelne Nutzerprofile kann über das Braze-Dashboard zugegriffen werden, indem Sie **User Search** in der Seitenleiste auswählen. Hier können Sie Nutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Nutzer-ID suchen. Innerhalb eines Nutzerprofils können Sie auf dem Tab „Engagement“ die SMS- und RCS-Abo-Gruppen der Nutzer:innen einsehen.
- **REST API:** Die Abo-Gruppe einzelner Nutzerprofile kann über den [Endpunkt „Abo-Gruppen von Nutzer:innen auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) oder den [Endpunkt „Abo-Gruppenstatus von Nutzer:innen auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) mithilfe der Braze REST API eingesehen werden.

## Nachrichten mit einer Abo-Gruppe senden {#send-messages-with-a-subscription-group}

Um eine SMS- oder RCS-Campaign über Braze zu starten, wählen Sie eine Abo-Gruppe aus dem Dropdown **SMS/MMS/RCS Variants** aus. Nach der Auswahl wird automatisch ein Zielgruppenfilter zu Ihrer Campaign oder Ihrem Canvas hinzugefügt, sodass nur Nutzer:innen, die die ausgewählte Abo-Gruppe `subscribed` haben, in der Zielgruppe enthalten sind.

Bevor Nutzer:innen Nachrichten von einer Campaign oder einem Canvas erhalten können, müssen sie die ausgewählte Abo-Gruppe abonniert haben. Wenn der Versand bei ansonsten gültigen Nutzer:innen fehlschlägt, bestätigen Sie deren Abo-Status mithilfe einer der Methoden unter [Status von Nutzer:innen festlegen](#set-a-users-state). Informationen zu Double-Opt-in-Anforderungen finden Sie unter [Status der Abo-Gruppe](#subscription-group-states).

{% alert important %}
In Übereinstimmung mit internationalen [Telekommunikationsvorschriften und -richtlinien]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) sendet Braze niemals SMS oder RCS an Nutzer:innen, die die ausgewählte Abo-Gruppe nicht abonniert haben.
{% endalert %}

![SMS-Composer mit geöffnetem Dropdown für die Abo-Gruppe, wobei „Messaging Service A for SMS“ hervorgehoben ist.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Best Practices für SMS-Abo-Gruppen {#sms-subscription-group-best-practices}

Erstellen Sie separate SMS-Abo-Gruppen für jeden Nachrichtenzweck (z. B. transaktional vs. Marketing) und für jeden Workspace. Wenn Sie in mehreren Ländern tätig sind, sollten Sie separate Gruppen nach Region in Betracht ziehen, um lokale Compliance-Anforderungen zu unterstützen – beispielsweise die Einschränkungen Brasiliens für Werbezeitfenster.

## Abo-Gruppen aktivieren {#enable-subscription-groups}

Um Abo-Gruppen für SMS, MMS oder RCS zu aktivieren, beachten Sie die folgenden Hinweise:

{% tabs local %}
{% tab SMS %}
Während Ihres SMS-Onboarding-Prozesses richtet ein Braze-Onboarding-Manager:in Abo-Gruppen für Ihr Dashboard-Konto ein. Sie arbeiten mit Ihnen zusammen, um festzulegen, wie viele Abo-Gruppen Sie benötigen, und fügen die entsprechenden Sende-Telefonnummern zu Ihren Abo-Gruppen hinzu. Die Zeiträume für die Einrichtung einer Abo-Gruppe hängen von der Art der Telefonnummern ab, die Sie hinzufügen. Shortcode-Anträge können beispielsweise 8–12 Wochen dauern, während Langcodes innerhalb eines Tages eingerichtet werden können. Wenn Sie Fragen zur Einrichtung Ihres Braze-Dashboards haben, wenden Sie sich an Ihre Braze-Vertretung, um Unterstützung zu erhalten.
{% endtab %}

{% tab MMS %}
Um eine MMS-Nachricht zu senden, muss mindestens eine Nummer innerhalb Ihrer Abo-Gruppe für den MMS-Versand aktiviert sein. Dies wird durch ein Tag neben der Abo-Gruppe angezeigt.

![Abo-Gruppen-Dropdown mit hervorgehobenem Eintrag „Messaging Service A for SMS“. Der Eintrag ist mit dem Tag „MMS“ versehen.]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Ein RCS-verifizierter Absender muss in Ihrer Abo-Gruppe vorhanden sein, bevor Sie eine RCS-Nachricht senden können.

Es gibt zwei Möglichkeiten, einen RCS-verifizierten Absender hinzuzufügen:
- Ihn zu einer bestehenden Abo-Gruppe hinzufügen
- Eine neue RCS-Abo-Gruppe erstellen
Die Wahl hängt weitgehend von den RCS-Anwendungsfällen ab, die Sie nutzen möchten.

Abhängig von Ihrer Integration kann Braze RCS-verifizierte Absender zu Ihren bestehenden SMS-Abo-Gruppen hinzufügen oder neue Abo-Gruppen für Sie einrichten. In beiden Fällen begleitet Sie Ihr Customer-Success-Manager durch ein nahtloses und effizientes SMS-Traffic-Upgrade.
{% endtab %}
{% endtabs %}

## Opt-out-Absichten in natürlicher Sprache in der Agent Console verarbeiten {#handle-natural-language-opt-outs-in-the-agent-console}

Für ein umfassendes Abo-Management können Sie Abmeldeabsichten erfassen, die außerhalb von Standard- oder benutzerdefinierten Keywords liegen (z. B. „Bitte schickt mir keine SMS mehr“). Durch die Erstellung eines KI-Agenten können Sie Sentiment-Analyse nutzen, um diese Anfragen automatisch zu erkennen und darauf zu reagieren.

### Einrichtung {#setup}

1. Erstellen Sie in der [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents) einen „SMS Sentiment Analysis Agent“.

{% alert tip %}
Verwenden Sie [Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), um bei der anfänglichen Agentenkonfiguration zu unterstützen.
{% endalert %}

{: start="2"}
2. Erstellen Sie ein aktionsbasiertes Canvas, das durch **Send an SMS inbound message** innerhalb der Keyword-Kategorie **Other** getriggert wird.
3. Fügen Sie den [Agentenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) zum Canvas hinzu, um Opt-out-Absichten zu erkennen.
4. Fügen Sie einen nachfolgenden SMS-[Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) hinzu, um die Anfrage zu bestätigen: „It looks like you're trying to unsubscribe from SMS, so we are going to unsubscribe you. If this is a mistake, text START to opt back in.“
5. Fügen Sie einen [Nutzer:innen-Aktualisierungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) hinzu, um den Status der Nutzer:in in der jeweiligen SMS-Abo-Gruppe auf „Unsubscribed“ zu ändern.

{% alert note %}
Die Verwendung der Agent Console verbraucht Message- oder Action-Credits.
{% endalert %}

## SMS-Datenverkehr zu RCS migrieren {#migrate-sms-traffic-to-rcs}

Wenn Sie separate SMS- und RCS-Abo-Gruppen haben, können Sie Nutzer:innen mithilfe eines einstufigen Canvas von SMS zu RCS migrieren.

Braze empfiehlt, zunächst RCS-Nachrichten an kleinere Nutzergruppen zu senden und im Laufe der Zeit mehr Nutzer:innen in die RCS-Abo-Gruppe zu migrieren. Wenn Sie beispielsweise 1.000.000 Nutzer:innen in einer SMS-Abo-Gruppe abonniert haben, könnte dies so aussehen: Migrieren Sie zunächst alle Nutzer:innen in die neue Abo-Gruppe und segmentieren Sie dann eine kleinere Zielgruppe von 50.000 bis 100.000 (5–10 %), um die RCS-Nachrichten zu testen.

### Schritt 1: Canvas erstellen und den Entry-Zeitplan ausfüllen {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Erstellen Sie ein Canvas und geben Sie ihm einen leicht identifizierbaren Namen (z. B. „SMS-RCS Abo-Gruppen-Nutzertransfer“). Planen Sie dann die Campaign zu einem für Sie passenden Zeitpunkt.

### Schritt 2: Zielgruppe definieren {#step-2-define-your-audience}
{: #step-2-define-your-audience}

Definieren Sie Ihre Zielgruppe mit einer der folgenden Methoden. Gehen Sie anschließend zum Schritt **Sendeeinstellungen** und wählen Sie **Nutzer:innen, die abonniert oder opted-in sind** aus.

| Methode                          | Beschreibung                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Segment erstellen**         | Erstellen Sie ein Segment, das alle Nutzer:innen einer Abo-Gruppe oder eine Teilmenge mithilfe von Segmentierungsfiltern enthält (z. B. zufällige 5–10 %). Segments werden vor jedem Versand aktualisiert, um Ihre aktuelle Nutzerbasis widerzuspiegeln.        |
| **Campaign- oder Canvas-Filter anwenden** | Verfeinern Sie die Zielgruppe im Schritt **Zielgruppe** Ihrer Campaign oder Ihres Canvas. Passen Sie die Targeting-Optionen an, ohne die Seite zu verlassen, für zusätzliche Flexibilität.                                         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Zielgruppe definieren" }

### Schritt 3: Nutzer-Update-Schritt konfigurieren {#step-3-configure-a-user-update-step}

Fügen Sie Ihrem Canvas einen Nutzer-Update-Schritt hinzu. Öffnen Sie im Schritt den **Advanced JSON Editor** und geben Sie Folgendes ein (für das Feld zur eindeutigen Nutzeridentifikation empfehlen wir die Verwendung des Feldes `braze_id`):

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

{% alert important %}
Bei Verwendung von `use_double_opt_in_logic` muss bereits ein Nutzerprofil vorhanden sein, damit der Abo-Status aktualisiert werden kann. Wenn dem angegebenen Bezeichner kein Nutzerprofil zugeordnet ist, wird der Abo-Status nicht aktualisiert.
{% endalert %}

![„Nutzer-Update-Objekt“ mit dem zuvor genannten JSON-Code.]({% image_buster /assets/img/sms/user_update_object.png %})

### Schritt 4: Canvas testen {#step-4-test-the-canvas}

Wir empfehlen dringend, [Ihr Canvas zu testen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases), um sicherzustellen, dass es wie erwartet funktioniert, bevor Sie es an Ihre breitere Zielgruppe senden.

### Schritt 5: Canvas starten {#step-5-launch-your-canvas}

Nachdem Sie Ihr Canvas erfolgreich getestet haben, starten Sie es für Ihre Teilmenge an Nutzer:innen!

Um zu bestätigen, dass Ihre Nutzer:innen erfolgreich migriert wurden, empfehlen wir, einige einzelne Nutzerprofile zu überprüfen, die aktualisiert wurden. Suchen Sie im Tab **Engagement** nach **Kontakteinstellungen** und scrollen Sie, um die Abo-Gruppen anzuzeigen, bei denen die Nutzer:in abonniert ist. Der Schalter für die RCS-Abo-Gruppe sollte jetzt aktiviert sein.

Informationen zur Einrichtung von RCS-Absendern und Abo-Gruppen finden Sie auch unter [RCS einrichten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Best Practices {#best-practices}

### Separate Abo-Gruppen einrichten {#designate-separate-subscription-groups}

- **Nachrichtentyp:** Erstellen Sie separate Abo-Gruppen für jeden Nachrichtentyp, z. B. transaktional und Marketing.
- **Workspace:** Erstellen Sie separate Abo-Gruppen für jeden Workspace, um Klarheit und Übersichtlichkeit zu gewährleisten.

Betrachten Sie das folgende Beispiel mit vier Abo-Gruppen in zwei Workspaces:

- **Produktions-Workspace**
  - Marketing - PROD für SMS
  - Transactional - PROD für SMS
- **Entwicklungs-Workspace (zum Testen)**
  - Marketing - DEV für SMS
  - Transactional - DEV für SMS

### Klare Namenskonventionen verwenden {#use-clear-naming-conventions}

Wählen Sie beschreibende und eindeutige Namen für Abo-Gruppen, damit beim Erstellen von SMS-Campaigns die richtige Gruppe ausgewählt wird.

### Gruppen nach Land trennen {#separate-groups-by-country}

SMS-Vorschriften variieren je nach Land. Wir empfehlen, SMS-Abo-Gruppen nach Ländern zu trennen. So können Sie die Compliance-Standards in allen Regionen einhalten, in die Sie Nachrichten senden.

Für jede Abo-Gruppe können Sie außerdem unter **Geographic Permissions** eine Länder-Allowlist konfigurieren, damit SMS, MMS und RCS nur an genehmigte Regionen gesendet werden. Weitere Informationen finden Sie unter [Geografische Berechtigungen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions).

In Brasilien ist es beispielsweise verboten, Marketing-Nachrichten außerhalb der Zeiten von 9:00 bis 21:00 Uhr Ortszeit zu versenden, und das Land erstreckt sich über drei Zeitzonen. Um diese Vorschriften einzuhalten, könnten Sie separate Gruppen für den Versand von Nachrichten nach Brasilien und in die USA einrichten. Dadurch wird verhindert, dass Nutzer:innen in Brasilien während der verbotenen Zeiten Marketing-Nachrichten erhalten.