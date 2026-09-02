---
nav_title: "Abo-Gruppen"
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

<a id="subscription-group-states"></a>

## Abo-Gruppenstatus {#subscription-group-states}
{: #sms-subscription-states}

Es gibt zwei Abo-Status für SMS- und RCS-Nutzer:innen: `subscribed` und `unsubscribed`. Der Abo-Status einer Nutzer:in wird auf Ebene der Abo-Gruppe gespeichert und ist nicht abo-gruppenübergreifend geteilt. Das bedeutet, dass eine Nutzer:in für eine transaktionale Abo-Gruppe `subscribed` und gleichzeitig für eine Werbe-Abo-Gruppe `unsubscribed` sein kann. Für Marken stellt diese Trennung der Status sicher, dass sie weiterhin relevante SMS- und RCS-Nachrichten an ihre Nutzer:innen senden können.

| Status | Definition |
| --------- | ---------- |
| Abonniert | Die Nutzer:in ist für den Empfang von SMS und RCS einer bestimmten Abo-Gruppe abonniert. Eine Nutzer:in kann abonniert werden, indem ihr Abo-Status über die Braze-Abo-API aktualisiert wird oder indem sie ein Opt-in-Schlüsselwort per SMS sendet. Eine Nutzer:in muss für eine SMS- oder RCS-Abo-Gruppe abonniert sein, um SMS, RCS oder beides zu empfangen. Wenn [Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) aktiviert ist, müssen Nutzer:innen ihre Opt-in-Absicht bestätigen, bevor ihr Abo-Status auf `Subscribed` aktualisiert wird. |
| Abgemeldet | Die Nutzer:in hat sich explizit vom Messaging Ihrer SMS- und RCS-Abo-Gruppe und der Senderufnummern innerhalb der Abo-Gruppe abgemeldet. Sie können sich abmelden, indem sie ein Opt-out-Schlüsselwort per SMS senden, oder Sie können Nutzer:innen über die [Braze-Abo-API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) abmelden. Nutzer:innen, die sich von einer SMS- und RCS-Abo-Gruppe abgemeldet haben, erhalten keine SMS oder RCS mehr von Senderufnummern, die zu dieser Abo-Gruppe gehören. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abo-Gruppenstatus" }

### Status einer Nutzer:in festlegen {#set-a-users-state}

Wenn eine Telefonnummer in einem Kundenprofil aktualisiert wird, erbt die neue Telefonnummer den Abo-Gruppenstatus der Nutzer:in. Wenn die Telefonnummer auf eine Nummer aktualisiert wird, die bereits in Braze existiert, wird der Abo-Status dieser vorhandenen Telefonnummer übernommen.

Wenn beispielsweise Nutzer:in A eine Telefonnummer hat, die für mehrere Abo-Gruppen abonniert ist, und diese Telefonnummer dann zu Nutzer:in B hinzugefügt wird, ist Nutzer:in B für dieselben Abo-Gruppen abonniert. Um zu verhindern, dass eine Nutzer:in die vorhandenen Abos übernimmt, können Sie die Abo-Gruppen der alten Nummer über die Braze REST API zurücksetzen, wenn eine Nutzer:in ihre Nummer ändert. Wenn mehrere Nutzer:innen diese Telefonnummer teilen, werden alle abgemeldet.

Um den Abo-Gruppenstatus einer Nutzer:in festzulegen, verwenden Sie eine der folgenden Methoden:

- **REST API:** Verwenden Sie den [`/subscription/status/set`-Endpunkt]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/), um Nutzerprofile programmatisch mit der Braze REST API festzulegen. Jede Anfrage kann zwischen 1 und 25 Abo-Gruppen enthalten.
- **SDK-Integration:** Nutzer:innen können einer E-Mail- oder SMS- und RCS-Abo-Gruppe mit `addToSubscriptionGroup` und `removeFromSubscriptionGroup` für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) oder [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup) hinzugefügt oder daraus entfernt werden. SDK-Methoden ersetzen keine regulatorischen Opt-in- oder Opt-out-Abläufe, die über Schlüsselwörter und die REST API gesteuert werden.
- **IAM-Formular zur Telefonnummernerfassung:** Telefonnummern von Nutzer:innen können über das Template zur Telefonnummernerfassung im Drag-and-drop-Editor für In-App-Nachrichten gesammelt werden.
- **Automatische Verarbeitung bei Opt-in/Opt-out:** Wenn Nutzer:innen ein Standard-Opt-in- oder Opt-out-[Schlüsselwort]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) per SMS senden, setzt und aktualisiert Braze den Abo-Status der Nutzer:innen automatisch.
- **Nutzerimport:** Nutzer:innen können über **Import Users** in E-Mail- oder SMS- und RCS-Abo-Gruppen hinzugefügt werden. Wenn Sie den Abo-Gruppenstatus aktualisieren, müssen diese zwei Spalten in Ihrer CSV vorhanden sein: `subscription_group_id` und `subscription_state`. Weitere Informationen finden Sie unter [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).
- **Braze-Dashboard:** Wählen Sie **Nutzersuche** in der Seitenleiste, öffnen Sie das Profil einer Nutzer:in und aktualisieren Sie SMS- oder RCS-Abo-Gruppen unter **Contact Settings** im Tab **Engagement**.
- **Cloud Data Ingestion (CDI):** Fügen Sie `subscription_group_id` und `subscription_state` in synchronisierte Zeilen ein. Siehe [Tabelleneinrichtung für Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).
- **User-Update-Schritt:** Aktualisieren Sie den Abo-Status in einem Canvas mit einem [User-Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt. Siehe [Status einer Nutzer:in in einem Canvas aktualisieren](#update-a-users-state-in-a-canvas) für Hinweise zum Timing.

#### Status einer Nutzer:in in einem Canvas aktualisieren {#update-a-users-state-in-a-canvas}

Wenn Sie den Abo-Gruppenstatus einer Nutzer:in im Rahmen eines Canvas-Flows aktualisieren, verwenden Sie einen [User-Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt anstelle eines Webhooks. Der User-Update-Schritt wartet, bis die Verarbeitung abgeschlossen ist, bevor die Nutzer:in zum nächsten Schritt weitergeleitet wird. So verwenden nachfolgende Messaging-Schritte den aktualisierten Abo-Status.

Wenn Sie einen Webhook zur Aktualisierung von Abo-Gruppen verwenden, wird die Nutzer:in weitergeleitet, sobald der Webhook gesendet wurde – nicht wenn die Abo-Änderung vollständig verarbeitet ist. Dies kann eine Race-Condition erzeugen, bei der ein nachfolgender SMS-Schritt ausgeführt wird, bevor die Nutzer:in abonniert ist, was dazu führt, dass die Nachricht bei einem Teil der Nutzer:innen fehlschlägt. Wenn Sie einen Webhook verwenden müssen, fügen Sie vor dem nächsten Messaging-Schritt einen Verzögerungsschritt von mindestens 1 Minute hinzu.

{% multi_lang_include api/orphaned_subscription_states.md %}

### Abo-Gruppe einer Nutzer:in prüfen {#check-a-users-group}

Um die Abo-Gruppe einer Nutzer:in zu prüfen, verwenden Sie eine der folgenden Methoden:

- **Kundenprofil:** Auf einzelne Nutzerprofile können Sie über das Braze-Dashboard zugreifen, indem Sie **Nutzersuche** in der Seitenleiste auswählen. Hier können Sie Nutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Nutzer-ID suchen. Innerhalb eines Nutzerprofils können Sie im Tab „Engagement“ die SMS- und RCS-Abo-Gruppen einer Nutzer:in einsehen.
- **REST API:** Der Abo-Gruppenstatus einzelner Nutzerprofile kann über den [Endpunkt „Abo-Gruppen einer Nutzer:in auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) oder den [Endpunkt „Abo-Gruppenstatus einer Nutzer:in auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) mit der Braze REST API eingesehen werden.

## Nachrichten mit einer Abo-Gruppe senden {#send-messages-with-a-subscription-group}

Um eine SMS- oder RCS-Campaign über Braze zu starten, wählen Sie eine Abo-Gruppe aus dem Dropdown **SMS/MMS/RCS Variants** aus. Nach der Auswahl wird automatisch ein Zielgruppenfilter zu Ihrer Campaign oder Ihrem Canvas hinzugefügt, sodass nur Nutzer:innen mit dem Status `subscribed` in der ausgewählten Abo-Gruppe in der Zielgruppe enthalten sind.

Bevor Nutzer:innen Nachrichten von einer Campaign oder einem Canvas erhalten können, müssen sie die ausgewählte Abo-Gruppe abonniert haben. Falls der Versand bei ansonsten gültigen Nutzer:innen fehlschlägt, überprüfen Sie deren Abo-Status mithilfe einer der Methoden unter [Status einer Nutzer:in festlegen](#set-a-users-state). Informationen zu Double-Opt-in-Anforderungen finden Sie unter [Abo-Gruppenstatus](#sms-subscription-states).

{% alert important %}
In Übereinstimmung mit internationalen [Telekommunikationsvorschriften und -richtlinien]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) sendet Braze niemals SMS oder RCS an Nutzer:innen, die die ausgewählte Abo-Gruppe nicht abonniert haben.
{% endalert %}

![SMS-Composer mit geöffnetem Dropdown für Abo-Gruppen, wobei „Messaging Service A for SMS“ hervorgehoben ist.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Best Practices für SMS-Abo-Gruppen {#sms-subscription-group-best-practices}

Erstellen Sie separate SMS-Abo-Gruppen für jeden Nachrichtenzweck (z. B. transaktional versus Marketing) und für jeden Workspace. Wenn Sie in mehreren Ländern tätig sind, sollten Sie separate Gruppen nach Region einrichten, um lokale Compliance-Regeln zu unterstützen – beispielsweise die Einschränkungen Brasiliens für Zeitfenster von Werbesendungen.

## Abo-Gruppen aktivieren {#enable-subscription-groups}

Um Abo-Gruppen für SMS, MMS oder RCS zu aktivieren, beachten Sie die folgenden Hinweise:

{% tabs local %}
{% tab SMS %}
Während Ihres SMS-Onboarding-Prozesses richtet ein Braze-Onboarding-Manager:in Abo-Gruppen für Ihr Dashboard-Konto ein. Er arbeitet mit Ihnen zusammen, um festzulegen, wie viele Abo-Gruppen Sie benötigen, und fügt die entsprechenden Sende-Telefonnummern zu Ihren Abo-Gruppen hinzu. Die Zeitrahmen für die Einrichtung einer Abo-Gruppe hängen von der Art der Telefonnummern ab, die Sie hinzufügen. Shortcode-Anträge können beispielsweise zwischen 8 und 12 Wochen dauern, während Langcodes innerhalb eines Tages eingerichtet werden können. Wenn Sie Fragen zur Einrichtung Ihres Braze-Dashboards haben, wenden Sie sich an Ihre Braze-Vertretung.
{% endtab %}

{% tab MMS %}
Um eine MMS-Nachricht zu senden, muss mindestens eine Nummer in Ihrer Abo-Gruppe für den MMS-Versand aktiviert sein. Dies wird durch ein Tag neben der Abo-Gruppe angezeigt.

![Abo-Gruppen-Dropdown mit hervorgehobenem Eintrag „Messaging Service A for SMS“. Dem Eintrag ist das Tag „MMS“ vorangestellt.]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Ein RCS-verifizierter Sender muss in Ihrer Abo-Gruppe vorhanden sein, bevor Sie eine RCS-Nachricht senden können.

Es gibt zwei Möglichkeiten, einen RCS-verifizierten Sender hinzuzufügen:
- Ihn einer bestehenden Abo-Gruppe hinzufügen
- Eine neue RCS-Abo-Gruppe erstellen
Die Wahl hängt weitgehend von den RCS-Anwendungsfällen ab, die Sie interessieren.

Je nach Ihrer Integration kann Braze RCS-verifizierte Sender zu Ihren bestehenden SMS-Abo-Gruppen hinzufügen oder neue Abo-Gruppen für Sie einrichten. In beiden Fällen begleitet Ihr CSM Sie durch ein nahtloses und effizientes SMS-Traffic-Upgrade.
{% endtab %}
{% endtabs %}

## Natürlichsprachige Abmeldungen in der Agent Console verarbeiten {#handle-natural-language-opt-outs-in-the-agent-console}

Für ein umfassendes Abo-Management können Sie Abmeldeabsichten erfassen, die außerhalb von Standard- oder angepassten Schlüsselwörtern liegen (wie z. B. „Bitte schreiben Sie mir nicht mehr“). Indem Sie einen KI-Agenten erstellen, können Sie Sentimentanalyse nutzen, um diese Anfragen automatisch zu erkennen und darauf zu reagieren.

### Einrichtung {#setup}

1. Erstellen Sie in der [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents) einen „SMS Sentiment Analysis Agent“.

{% alert tip %}
Verwenden Sie [Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), um bei der anfänglichen Agentenkonfiguration zu unterstützen.
{% endalert %}

{: start="2"}
2. Erstellen Sie ein aktionsbasiertes Canvas, das durch **Send an SMS inbound message** ausgelöst wird, innerhalb der Schlüsselwortkategorie **Other**.
3. Fügen Sie den [Agentenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) zum Canvas hinzu, um die Abmeldeabsicht zu erkennen.
4. Fügen Sie einen nachfolgenden SMS-[Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) hinzu, um die Anfrage zu bestätigen: „Es sieht so aus, als möchten Sie sich von SMS abmelden, daher werden wir Sie abmelden. Falls dies ein Versehen war, senden Sie START, um sich wieder anzumelden.“
5. Fügen Sie einen [Nutzer:innen-Aktualisierungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) hinzu, um den Status der Nutzer:in in der jeweiligen SMS-Abo-Gruppe auf „Abgemeldet“ zu ändern.

{% alert note %}
Die Nutzung der Agent Console verbraucht Nachrichten- oder Aktionsguthaben.
{% endalert %}

## SMS-Datenverkehr auf RCS migrieren {#migrate-sms-traffic-to-rcs}

Wenn Sie separate SMS- und RCS-Abo-Gruppen haben, können Sie Nutzer:innen mithilfe eines einstufigen Canvas von SMS auf RCS migrieren.

Braze empfiehlt, dass Sie zunächst RCS-Nachrichten an kleinere Nutzergruppen testen und im Laufe der Zeit mehr Nutzer:innen in die RCS-Abo-Gruppe migrieren. Wenn Sie beispielsweise 1.000.000 Nutzer:innen in einer SMS-Abo-Gruppe abonniert haben, könnte das so aussehen: Zunächst migrieren Sie alle Nutzer:innen in die neue Abo-Gruppe und segmentieren dann auf eine kleinere Zielgruppe von 50.000 bis 100.000 (5–10 %), um die RCS-Nachrichten zu testen.

### Schritt 1: Canvas erstellen und den Eintrittsplan ausfüllen {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Erstellen Sie ein Canvas und geben Sie ihm einen leicht erkennbaren Namen (z. B. „SMS-RCS Abo-Gruppen-Nutzertransfer“). Planen Sie dann die Campaign zu einem für Sie passenden Zeitpunkt.

### Schritt 2: Zielgruppe definieren {#step-2-define-your-audience}
{: #step-2-define-your-audience}

Definieren Sie Ihre Zielgruppe mit einer der folgenden Methoden. Gehen Sie anschließend zum Schritt **Sendeeinstellungen** und wählen Sie **Nutzer:innen, die abonniert oder angemeldet sind**.

| Methode                          | Beschreibung                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Segment erstellen**         | Erstellen Sie ein Segment, das alle Nutzer:innen in einer Abo-Gruppe oder eine Teilmenge mithilfe von Segmentierungsfiltern enthält (z. B. zufällige 5–10 %). Segments werden vor jedem Versand aktualisiert, um Ihre aktuelle Nutzerbasis widerzuspiegeln.        |
| **Campaign- oder Canvas-Filter anwenden** | Verfeinern Sie die Zielgruppe im Schritt **Zielgruppe** Ihrer Campaign oder Ihres Canvas. Passen Sie die Targeting-Optionen an, ohne die Seite zu verlassen, für zusätzliche Flexibilität.                                         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Zielgruppe definieren" }

### Schritt 3: Schritt „Nutzer-Update“ konfigurieren {#step-3-configure-a-user-update-step}

Fügen Sie Ihrem Canvas einen Schritt „Nutzer-Update“ hinzu. Öffnen Sie im Schritt den **Erweiterten JSON-Editor** und geben Sie Folgendes ein (für das Feld zur eindeutigen Nutzeridentifikation empfehlen wir die Verwendung des Feldes `braze_id`):

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
Bei Verwendung von `use_double_opt_in_logic` muss bereits ein Kundenprofil vorhanden sein, damit der Abo-Status aktualisiert werden kann. Wenn dem angegebenen Bezeichner kein Kundenprofil zugeordnet ist, wird der Abo-Status nicht aktualisiert.
{% endalert %}

![„Nutzer-Update-Objekt“, das den oben angegebenen JSON-Code enthält.]({% image_buster /assets/img/sms/user_update_object.png %})

### Schritt 4: Canvas testen {#step-4-test-the-canvas}

Wir empfehlen dringend, [Ihr Canvas zu testen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases), um zu bestätigen, dass es wie erwartet funktioniert, bevor Sie es an Ihre breitere Zielgruppe senden.

### Schritt 5: Canvas starten {#step-5-launch-your-canvas}

Nachdem Sie Ihr Canvas erfolgreich getestet haben, starten Sie es für Ihre ausgewählte Teilmenge von Nutzer:innen!

Um zu bestätigen, dass Ihre Nutzer:innen erfolgreich migriert wurden, empfehlen wir, einige einzelne Nutzerprofile zu überprüfen, die aktualisiert wurden. Suchen Sie im Tab **Engagement** nach **Kontakteinstellungen** und scrollen Sie, um die Abo-Gruppen anzuzeigen, die die Nutzer:in abonniert hat. Der Schalter für die RCS-Abo-Gruppe sollte jetzt aktiviert sein.

Informationen zur Einrichtung von RCS-Sendern und Abo-Gruppen finden Sie auch unter [RCS einrichten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Best Practices {#best-practices}

### Separate Abo-Gruppen einrichten {#designate-separate-subscription-groups}

- **Nachrichtentyp:** Erstellen Sie separate Abo-Gruppen für jeden Nachrichtentyp, z. B. transaktional und Marketing.
- **Workspace:** Erstellen Sie separate Abo-Gruppen für jeden Workspace, um Klarheit und Übersichtlichkeit zu gewährleisten.

Betrachten Sie das folgende Beispiel mit vier Abo-Gruppen in zwei Workspaces:

- **Produktions-Workspace**
  - Marketing - PROD für SMS
  - Transaktional - PROD für SMS
- **Entwicklungs-Workspace (zum Testen)**
  - Marketing - DEV für SMS
  - Transaktional - DEV für SMS

### Klare Namenskonventionen verwenden {#use-clear-naming-conventions}

Wählen Sie aussagekräftige und klare Namen für Abo-Gruppen, damit beim Erstellen von SMS-Campaigns die richtige Gruppe ausgewählt wird.

### Gruppen nach Land trennen {#separate-groups-by-country}

SMS-Vorschriften variieren je nach Land. Wir empfehlen, SMS-Abo-Gruppen nach Land zu trennen. So können Sie die Compliance-Standards in allen Regionen einhalten, in die Sie Nachrichten senden.

Für jede Abo-Gruppe können Sie außerdem unter **Geographic Permissions** eine Länder-Allowlist konfigurieren, sodass SMS, MMS und RCS nur an genehmigte Regionen gesendet werden. Weitere Informationen finden Sie unter [Geografische Berechtigungen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions).

In Brasilien ist es beispielsweise verboten, Marketing-Nachrichten außerhalb der Zeiten von 9 bis 21 Uhr Ortszeit zu senden, und das Land erstreckt sich über drei Zeitzonen. Um diese Vorschriften einzuhalten, könnten Sie separate Gruppen für den Versand von Nachrichten nach Brasilien und in die USA einrichten. So wird verhindert, dass Nutzer:innen in Brasilien Marketing-Nachrichten während verbotener Zeiten erhalten.