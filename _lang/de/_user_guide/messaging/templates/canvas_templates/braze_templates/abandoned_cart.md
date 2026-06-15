---
nav_title: Warenkorb-Abbruch
article_title: Warenkorb-Abbruch
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie ein Braze-Canvas-Template verwenden, um Nutzer:innen in Echtzeit anzusprechen und sie zu ermutigen, ihre Käufe abzuschließen."
tool: Canvas
---

# Warenkorb-Abbruch {#abandoned-intent}

> Sprechen Sie Nutzer:innen in Echtzeit an, um sie zu ermutigen, ihre Käufe abzuschließen, solange die Produkte noch präsent sind. Dieses API-getriggerte Template nimmt Nutzer:innen sofort auf, wenn sie einen Warenkorb abbrechen, sendet zeitnahe Erinnerungen über den optimalen Kanal (E-Mail, SMS oder In-App-Nachricht), prüft an zwei Stellen der Journey, ob der Kauf abgeschlossen wurde, und synchronisiert Nutzer:innen, die nicht konvertieren, mit Werbe-Zielgruppen für Retargeting.

In diesem Artikel führen wir Sie durch einen Anwendungsfall für das Template **Abandoned Intent**, das für die Überlegungsphase des Nutzer:innen-Lebenszyklus vorgesehen ist. Nach diesem Artikel haben Sie eine User-Journey angepasst, die Käufe von Nutzer:innen fördert, die nach dem Hinzufügen von Artikeln zu ihren Warenkörben keine Käufe getätigt haben.

{% alert tip %}
Verwenden Sie [BrazeAI Operator<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/operator/), um dieses Template einzurichten und anzupassen. Wählen Sie **BrazeAI Operator<sup>TM</sup>** neben Ihrem Nutzerprofil, während Sie Ihr Canvas erstellen oder bearbeiten. Beschreiben Sie dann Ihr Ziel, z. B. „Hilf mir, das Abandoned-Intent-Template zu konfigurieren, um Nutzer:innen erneut anzusprechen, die ihren Warenkorb abgebrochen haben“.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Ein separates Canvas für die Post-Purchase-User-Journey, da ein Kauf in diesem Canvas dazu führt, dass Nutzer:innen das Canvas verlassen.
- Eine konfigurierte [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) mit den Partnern und Zielgruppen, die Sie verwenden.

## Das Template an Ihre Bedürfnisse anpassen {#tailoring-the-template-to-your-needs}

Nehmen wir an, wir arbeiten bei Kitchenerie, einer Einzelhandelsmarke, die auf Küchenartikel spezialisiert ist, und unser Ziel ist es, Nutzer:innen erneut anzusprechen, die das neueste Produkt „Enormous Paper Plate“ in ihren Warenkorb gelegt, aber ihren Kauf nicht abgeschlossen haben.

Bevor wir das Canvas erstellen, richten wir die Integration [Braze Audience Sync zu Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) ein, damit wir Nutzerdaten von Braze zu Facebook Audiences hinzufügen können, um Werbeanzeigen basierend auf Verhaltens-Triggern, Segmentierung und mehr zu senden.

Das Template **Abandoned Intent** folgt diesem Ablauf: Kauf prüfen, sofortige Erinnerung senden, warten, zum optimalen Kanal weiterleiten, Follow-up senden, erneut prüfen und Nicht-Konvertierer retargeten. Es enthält die folgenden Schritte:

| Canvas-Schritt | Name des Template-Schritts | Zweck |
|---|---|---|
| Aktionspfade | Made purchase? | Erste Abschlussprüfung; Nutzer:innen, die bereits gekauft haben, verlassen das Canvas. |
| Nachricht | Itemized Reminder | Sofortige Warenkorb-Erinnerung, die direkt nach dem Eintritt gesendet wird. |
| Verzögerung | Delay | 30-minütige Wartezeit, damit das Follow-up ankommt, solange das Produkt noch präsent ist. |
| Zielgruppenpfade | Intelligent Channel split | Leitet Nutzer:innen basierend auf dem [intelligenten Kanal]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/)-Ranking zu E-Mail oder SMS weiter. |
| Nachricht | Abandoned Cart Email, Abandoned Cart SMS und Abandoned Cart In-App Message | Kanalspezifische Follow-ups. Der intelligente Kanal wählt zwischen E-Mail und SMS; die In-App-Nachricht wird auf einem separaten Pfad im Template gesendet. |
| Aktionspfade | Made purchase? (2) | Zweite Abschlussprüfung vor dem Retargeting. |
| Audience Sync | Ad Retargeting | Synchronisiert Nicht-Konvertierer mit Werbe-Zielgruppen (z. B. Facebook) für kanalübergreifendes Retargeting. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritte des Abandoned-Intent-Templates" }

### 1. Schritt: Details einrichten {#step-1-set-up-the-details}

Wenden wir das Canvas-Template an und aktualisieren die Details, um unser Ziel widerzuspiegeln.

1. Gehen Sie zu **Messaging** > **Canvas**.
2. Wählen Sie **Create Canvas** > **Use a Canvas Template**.
3. Wählen Sie den Tab **Braze templates** und dann **Apply Template** neben **Abandoned Intent**.
4. Aktualisieren Sie die Beschreibung, um anzugeben, dass das Canvas Nutzer:innen ermutigen soll, Käufe aus der neuesten saisonalen Küchenartikel-Kollektion abzuschließen.
5. Fügen Sie den Tag **Intent** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### 2. Schritt: Konversions-Events zuweisen {#step-2-assign-your-conversion-events}

Das Template setzt **Primary Conversion Event - A** standardmäßig auf **Makes Purchase (Legacy)** mit der Auswahl **Make any purchase (Legacy)**. Da unser Fokus auf unserem Produkt „Enormous Paper Plate“ liegt, passen wir das Konversions-Event wie folgt an:

1. Wählen Sie **Make a specific purchase (Legacy)**.
2. Geben Sie unter **Product name** den Wert **Enormous Paper Plate** ein.

![Primäres Konversions-Event – A mit dem Conversion-Typ „Makes Purchase“ und dem Produktnamen „Enormous Paper Plate“. Es gibt eine 3-Tage-Conversion-Frist.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

{% alert note %}
Wenn Ihr Workspace das Konversions-Event **Places order** verwendet, können kaufbezogene Optionen mit **(Legacy)** im Label erscheinen. Die Schritte in diesem Artikel verwenden den Legacy-Kauf-Conversion-Ablauf.
{% endalert %}

### 3. Schritt: Entry-Zeitplan festlegen {#step-3-set-an-entry-schedule}

Das Template **Abandoned Intent** verwendet einen **API-Triggered**-Entry-Zeitplan, damit Sie Nutzer:innen in das Canvas aufnehmen können, sobald sie ihren Warenkorb abbrechen. Das passt zu unserem Anwendungsfall, da wir reagieren möchten, solange das Produkt noch präsent ist.

1. Behalten Sie **API-Triggered** als Entry-Zeitplan-Typ bei.
2. Notieren Sie sich die Canvas-ID und verwenden Sie den [`/canvas/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/), um Nutzer:innen hinzuzufügen, wenn Ihre App oder Website einen Warenkorb-Abbruch erkennt.
3. Optional können Sie [Kontext-Variablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) (wie Produktname oder Warenkorb-Details) übergeben, um nachfolgende Nachrichten zu personalisieren.

Wenn Sie stattdessen einen aktionsbasierten Eintritt bevorzugen, wählen Sie **Action-Based** und einen Trigger, der zu der Art passt, wie Ihre Marke Warenkorb-Abbrüche erfasst – zum Beispiel **Perform Custom Event** für ein protokolliertes `abandoned_cart`-Event.

### 4. Schritt: Festlegen, wer das Canvas betritt {#step-4-determine-who-enters-the-canvas}

Als Nächstes definieren wir unsere Zielgruppe als Nutzer:innen, die in den letzten 90 Tagen ausschließlich online bei uns eingekauft haben. Dies hilft uns, unsere Zielgruppe auf Nutzer:innen einzugrenzen, von denen wir wissen, dass sie mit unseren Produkten interagieren.

![„Online Shoppers Segment - 90 Days“ als Segment der Nutzer:innen, die für dieses Canvas angesprochen werden sollen.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Wir belassen die Eintrittskontrollen wie sie sind, sodass Nutzer:innen dieses Canvas nicht erneut betreten dürfen und es keine Begrenzung für die Anzahl der Personen gibt, die dieses Canvas potenziell betreten können.

Das Template legt standardmäßig keine globalen Austrittskriterien fest. Stattdessen verlassen Nutzer:innen das Canvas, wenn sie in den Aktionspfade-Schritten **Made purchase?** einen Kauf tätigen, die wir in [Schritt 6](#step-6-customize-your-canvas) anpassen.

### 5. Schritt: Sendeeinstellungen auswählen {#step-5-select-your-send-settings}

Wir behalten die Standard-Abo-Einstellungen bei, sodass wir nur an Nutzer:innen senden, die Nachrichten oder Benachrichtigungen abonniert haben oder sich dafür angemeldet haben, und belassen die anderen Einstellungen wie sie sind.

### 6. Schritt: Canvas anpassen {#step-6-customize-your-canvas}

Passen Sie die Canvas-Schritte in der Reihenfolge an, in der Nutzer:innen sie durchlaufen:

#### Kauf beim Eintritt prüfen {#check-for-purchase-at-entry}

1. Wählen Sie den Aktionspfade-Schritt **Made purchase?** und dann die Aktionsgruppe **Made purchase**.
2. Wählen Sie unter **Make Purchase** die Option **Make a specific purchase (Legacy)** und wählen Sie **Enormous Paper Plate** als Produkt. Nutzer:innen, die dieses Produkt kaufen, verlassen das Canvas.

#### Sofortige Erinnerung senden {#send-the-immediate-reminder}

1. Wählen Sie den Nachrichten-Schritt **Itemized Reminder** und dann **Edit message**, um die erste Erinnerungs-E-Mail anzupassen. Diese Nachricht wird sofort nach dem Eintritt gesendet, vor der Verzögerung.
2. Belassen Sie den **Delay**-Schritt wie er ist. Das Template verwendet eine 30-minütige Verzögerung, bevor Follow-up-Nachrichten gesendet werden, um Nutzer:innen Zeit zu geben, den Checkout abzuschließen, solange das Produkt noch präsent ist.

{% alert tip %}
Sie können [Canvas-Kontext-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) verwenden, um die Nachrichten in Ihrem Canvas basierend auf dem Produkt, auf das Sie sich beziehen, anzupassen.
{% endalert %}

#### Zum optimalen Kanal weiterleiten {#route-to-the-optimal-channel}

1. Überprüfen Sie den Zielgruppenpfade-Schritt **Intelligent Channel split**. Dieser leitet Nutzer:innen basierend auf dem [intelligenten Kanal]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/)-Ranking zu **Abandoned Cart Email** oder **Abandoned Cart SMS** weiter. Passen Sie die Pfade bei Bedarf an.
2. Passen Sie die Schritte **Abandoned Cart Email**, **Abandoned Cart SMS** und **Abandoned Cart In-App Message** an. Wählen Sie bei jedem Schritt **Edit message**, um den Text und die Nachricht für den jeweiligen Kanal zu aktualisieren. Die In-App-Nachricht läuft auf einem separaten Pfad vom Intelligent-Channel-Split und wird nicht durch das Intelligent-Channel-Ranking ausgewählt.

#### Nicht-Konvertierer retargeten {#retarget-non-converters}

1. Wählen Sie den Aktionspfade-Schritt **Made purchase? (2)** und dann die Aktionsgruppe **Made purchase**.
2. Wählen Sie **Make a specific purchase (Legacy)** und wählen Sie **Enormous Paper Plate** als Produkt. Nutzer:innen, die hier kaufen, verlassen das Canvas, bevor sie das Retargeting erreichen.
3. Wählen Sie den Audience-Sync-Schritt **Ad Retargeting** und konfigurieren Sie ihn für die Synchronisierung mit Facebook. Nutzer:innen, die diesen Schritt erreichen, haben nicht gekauft – synchronisieren Sie sie mit Ihrer Werbe-Zielgruppe für kanalübergreifendes Retargeting.

### 7. Schritt: Canvas testen und starten {#step-7-test-and-launch-the-canvas}

Nachdem Sie das Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, wählen Sie **Launch Canvas**, um das Canvas zu starten. Jetzt können wir Nutzer:innen gezielt mit einer personalisierten User-Journey ansprechen, um sie zu ermutigen, das Produkt zu kaufen, das sie in ihren Warenkorb gelegt haben!

{% alert tip %}
Schauen Sie sich unsere [Checkliste vor und nach dem Start]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) an, um zu erfahren, was Sie vor und nach dem Start eines Canvas beachten sollten.
{% endalert %}