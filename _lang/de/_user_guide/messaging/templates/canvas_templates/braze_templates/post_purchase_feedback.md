---
nav_title: Feedback nach dem Kauf
article_title: Feedback nach dem Kauf
page_order: 6
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie ein Braze-Canvas-Template verwenden, um personalisierte Erlebnisse zu orchestrieren, die es Ihnen ermöglichen, auf Feedback zu reagieren und eine Beziehung zu Ihren Nutzer:innen aufzubauen."
tool: Canvas
---

# Feedback nach dem Kauf {#post-purchase-feedback}

> Verwenden Sie das Template für Feedback nach dem Kauf, um wichtige Insights darüber zu gewinnen, wie Ihre Kund:innen mit Ihrer Marke interagieren, und stellen Sie sicher, dass sie weiterhin positive Erfahrungen machen. Durch den Einsatz personalisierter Kommunikation und einer strukturierten Abfolge von Nachrichten können Sie Ihre Kundenbeziehungen weiter aufbauen und pflegen.

Dieser Artikel führt Sie durch einen Anwendungsfall für das Template **Post-Purchase Feedback**, das für die Conversion-Phase des Nutzerlebenszyklus konzipiert ist. Am Ende werden Sie ein Canvas erstellt haben, das Nutzer:innen dazu ermutigt, Feedback für Ihre App abzugeben.

## Voraussetzungen {#prerequisites}

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Ein [angepasstes Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes), das als Referenz für die Ergebnisse der Feedback-Umfrage dient.
- Eine konfigurierte [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) mit den Partnern und Zielgruppen, die Sie verwenden.

## Das Template an Ihre Bedürfnisse anpassen {#tailoring-the-template-to-your-needs}

Nehmen wir an, wir arbeiten für Decorumsoft, einen Entwickler mobiler Videospiele. Wir verwenden das Template für Feedback nach dem Kauf, um Rückmeldungen zu unserem neuesten Videospiel-Launch, Proxy War 3: War of Thirst, zu erfassen. Anhand dieses Feedbacks werden wir unsere Entwicklungspläne für das Erweiterungspaket Liquid Mirage gestalten.

Bevor wir das Canvas erstellen, richten wir die Integration [Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) ein, damit wir Nutzerdaten aus Braze zu Google Audiences hinzufügen können, um Werbeanzeigen basierend auf Verhaltens-Triggern, Segmentierung und mehr zu senden.

Um auf das Template für Feedback nach dem Kauf zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Use a Canvas template** > **Braze templates**. Wählen Sie dann neben **Post-Purchase Feedback** die Option **Apply Template**. Jetzt können wir das Template durchgehen und an unsere Bedürfnisse anpassen.

### 1. Schritt: Canvas-Details einrichten {#step-1-set-up-canvas-details}

Passen wir die Canvas-Details an, um unser Ziel widerzuspiegeln.

1. Wählen Sie **Edit** neben dem Template-Namen.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas auf kürzlich aktive Nutzer:innen abzielt.
3. Aktualisieren Sie die Beschreibung, um anzugeben, dass das Canvas Nutzer:innen dazu ermutigen soll, Feedback abzugeben.
4. Fügen Sie den Tag **Feedback** hinzu, um auf der Canvas-Startseite danach filtern zu können.

![Der neue Name und die neue Beschreibung für das Canvas. Die neue Beschreibung lautet: „Ein Canvas für Feedback nach dem Kauf, um das Interesse an der kommenden Erweiterung für PWD3, Liquid Mirage, zu ermitteln.“]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### 2. Schritt: Konversions-Events zuweisen {#step-2-assign-conversion-events}

Als Nächstes weisen wir unsere Konversions-Events zu. Aktualisieren Sie das **Primary Conversion Event - A** auf **Make a specific purchase** und wählen Sie **Proxy War**.

![Der Abschnitt „Assign Conversion Events“ für den Konversions-Event-Typ des Kaufs des Proxy-War-Spielprodukts.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

Wir behalten die Conversion-Frist des Templates von drei Tagen bei, da wir unsere neuesten Nutzer:innen ansprechen möchten.

### 3. Schritt: Einen Entry-Zeitplan festlegen {#step-3-set-an-entry-schedule}

1. Behalten Sie den Entry-Zeitplan-Typ als **Action-Based** bei.
2. Legen Sie die **Start Time** für das Einstiegsfenster auf das Datum des Spiel-Launches fest.

### 4. Schritt: Bestimmen, wer das Canvas betritt {#step-4-determine-who-enters-the-canvas}

Unsere Zielgruppe für Feedback sind Nutzer:innen, die kürzlich Proxy War 3 gekauft haben.

1. Wählen Sie unser Zielsegment „Purchased Proxy War 3“ aus, das aus Nutzer:innen besteht, die das Spiel gekauft haben.
2. Wählen Sie einen Filter, um Nutzer:innen einzuschließen, die „Proxy War 3“ mehr als „0“ Mal gekauft haben.

![Ein Segment namens „Purchased Proxy War 3“, das Nutzer:innen segmentiert, die das Spiel gekauft haben.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3. Aktualisieren Sie die Eingangskontrollen, damit Nutzer:innen nach der maximalen Dauer des Canvas nicht erneut eintreten können.

### 5. Schritt: Sendeeinstellungen auswählen {#step-5-select-your-send-settings}

Wir behalten die Standard-Abo-Einstellungen bei, sodass wir nur an Nutzer:innen senden, die Nachrichten oder Benachrichtigungen abonniert haben oder sich dafür angemeldet haben.

Da wir beim Versand achtsam sein möchten, wählen wir **Enable Quiet Hours**, um zwischen 23 Uhr und 10 Uhr in der Zeitzone unserer Nutzer:innen kein Feedback anzufordern und nur zum nächsten verfügbaren Zeitpunkt zu senden.

![Der Schritt „Send Settings“ richtet sich an Nutzer:innen, die abonniert oder angemeldet sind. Ruhezeiten sind aktiviert.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

Für unser Beispiel überspringen wir die anderen Einstellungen (Frequency-Capping und Seed-Gruppen).

### 6. Schritt: Ihr Canvas anpassen {#step-6-customize-your-canvas}

Als Nächstes bauen wir unser Canvas auf, indem wir die Messaging-Kanäle und den Inhalt anpassen, der an Nutzer:innen gesendet wird. Da wir nur über E-Mail, In-App-Nachricht und Webhook-Kanäle Feedback einholen, gehen wir das Template durch und entfernen die SMS-Varianten aus den Nachrichtenschritten.

Wir beginnen unsere Anpassung, indem wir jede Messaging-Komponente durchgehen und den Inhalt aktualisieren. Unser angepasstes Attribut als Referenz ist `Experience Feedback`.

1. Wählen Sie im Canvas-Builder den ersten Nachrichtenschritt in der User Journey aus.
2. Wählen Sie die **E-Mail**-Variante.
3. Füllen Sie die **Sending info** mit einem Betreff aus, der Nutzer:innen zu Feedback ermutigt.
4. Wählen Sie **Edit message**, um die E-Mail-Nachricht des Templates durch unsere Feedback-Umfrage-Nachricht zu ersetzen. Dazu gehört das Ersetzen der Links für jeden Call-to-Action, um zu erfassen, welche Option ausgewählt wurde. Dies wird im Aktions-Pfad-Schritt unserer User Journey referenziert.

{% alert tip %}
Sie können [Canvas-Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) verwenden, um die Nachrichten in Ihrem Canvas basierend auf dem Produkt, auf das Sie sich beziehen, anzupassen.
{% endalert %}

#### Feedback-Umfrage einrichten {#set-up-feedback-survey}

Als Nächstes müssen wir die Details für die **In-App Messages**-Variante ausfüllen. Hier müssen wir unser angepasstes Attribut `Experience Feedback` angeben, das die Stimmung unseres Nutzer-Feedbacks anzeigt. (Wir werden dies auch im nachfolgenden Aktions-Pfad-Schritt referenzieren.)

1. Wählen Sie im selben ersten Nachrichtenschritt die **In-App Messages**-Variante aus. Wir behalten die Nachrichteneinstellungen bei.
2. Für die Überschrift und den Text verwenden wir eine Formulierung, die Nutzer:innen ermutigt, ehrlich über ihre Erfahrung mit Proxy War 3 zu berichten.
3. Da wir möchten, dass ihre Umfrageantworten in ihren Profilen protokolliert werden, behalten wir die Umfrage als **Single-choice selection** und **Log attributes upon submission** bei.
4. Wählen Sie für jede der drei Umfrageoptionen **Experience Feedback** als unser angepasstes Attribut.
5. Wir behalten die Attributwerte im Nutzerprofil bei, da diese Werte mit unserem angepassten Attribut übereinstimmen.

![Eine Umfrage, die Nutzer:innen fragt, ob sie ihren kürzlichen Kauf von Proxy War 3 genossen haben, mit drei Optionen: „Loved it“, „It was OK“ und „Not for me“.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### Den Aktions-Pfad aufbauen {#build-out-the-action-path}

Mithilfe unseres angepassten Attributs `Experience Feedback` und der Attributwerte aus dem vorherigen Abschnitt aktualisieren wir den Aktions-Pfad des Templates, um ihn an unser Attribut und unsere Werte anzupassen.

![Die Gruppe „Good feedback“ für den Aktions-Pfad-Schritt, die Nutzer:innen einschließt, die in unserer Umfrage mit „Loved it“ geantwortet haben.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### Ad-Retargeting einrichten {#set-up-ad-retargeting}

Wir stellen sicher, dass unsere Google Audience Sync in unserem **Ad Retargeting**-Schritt eingerichtet ist. Dazu gehört die Auswahl unseres Werbekontos, einer bestehenden Zielgruppe und der Option, Nutzer:innen zur Zielgruppe hinzuzufügen.

### Webhook-Support-Fälle einrichten {#set-up-webhook-support-cases}

Als Nächstes richten wir den Webhook ein, um potenzielle Support-Fälle auszulösen. Dies kann besonders aufschlussreich in Kombination mit der Analyse unseres Nutzer-Feedbacks sein.

Für den Nachrichtenschritt namens **Support Case Creation** aktualisieren wir das Template, um einen Webhook für Nutzer:innen zu erstellen, die mit ihrem Kauf unzufrieden sind und eine Rückerstattung wünschen.

![Ein Webhook, der Support-Fälle für Kund:innen erstellt, die eine negative Stimmung haben und eine Rückerstattung für ihren Kauf von Proxy War 3 wünschen.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### 6. Schritt: Das Canvas testen und starten {#step-6-test-and-launch-the-canvas}

Nachdem wir unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, wählen Sie **Launch Canvas**, um das Canvas zu starten. Jetzt können wir Nutzer:innen gezielt mit einer personalisierten User Journey ansprechen, um sie basierend auf ihrem kürzlichen Kauf von Proxy War 3 zur Teilnahme an unserer Feedback-Umfrage zu ermutigen!

{% alert tip %}
Schauen Sie sich unsere [Checkliste vor und nach dem Launch]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) an, um zu erfahren, was Sie vor und nach dem Start eines Canvas beachten sollten.
{% endalert %}