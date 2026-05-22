---
nav_title: Warenkorb-Abbruch
article_title: Warenkorb-Abbruch
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie ein Braze-Canvas-Template verwenden, um Nutzer:innen in Echtzeit anzusprechen und sie zu ermutigen, ihre Käufe abzuschließen."
tool: Canvas
---

# Warenkorb-Abbruch {#abandoned-cart}

> Sprechen Sie Nutzer:innen in Echtzeit an, um sie zu ermutigen, ihre Käufe abzuschließen. Verwenden Sie dieses Template, um eine User-Journey zu erstellen, die sich auf den Versand zeitnaher, personalisierter Nachrichten konzentriert, die Nutzer:innen an ihre abgebrochenen Warenkörbe erinnern, indem Produktvorteile hervorgehoben und Anreize wie Rabattcodes angeboten werden.

In diesem Artikel führen wir Sie durch einen Anwendungsfall für das Template **Abandoned Intent**, das für die Überlegungsphase des Nutzer:innen-Lebenszyklus vorgesehen ist. Nach diesem Artikel haben Sie eine User-Journey angepasst, die Käufe von Nutzer:innen fördert, die nach dem Hinzufügen von Artikeln zu ihren Warenkörben keine Käufe getätigt haben.

## Voraussetzungen {#prerequisites}

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Ein separates Canvas für die Post-Purchase-User-Journey, da ein Kauf in diesem Canvas dazu führt, dass Nutzer:innen das Canvas verlassen.
- Eine konfigurierte [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) mit den Partnern und Zielgruppen, die Sie verwenden.

## Das Template an Ihre Bedürfnisse anpassen {#tailoring-the-template-to-your-needs}

Nehmen wir an, wir arbeiten bei Kitchenerie, einer Einzelhandelsmarke, die auf Küchenartikel spezialisiert ist, und unser Ziel ist es, Nutzer:innen erneut anzusprechen, die das neueste Produkt „Enormous Paper Plate“ in ihren Warenkorb gelegt, aber ihren Kauf nicht abgeschlossen haben.

Bevor wir das Canvas erstellen, richten wir die Integration [Braze Audience Sync zu Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) ein, damit wir Nutzerdaten von Braze zu Facebook Audiences hinzufügen können, um Werbeanzeigen basierend auf Verhaltens-Triggern, Segmentierung und mehr zu senden.

Um auf das Abandoned-Intent-Template zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Use a Canvas template** > **Braze templates**. Wählen Sie dann neben **Abandoned Intent** die Option **Apply Template**. Jetzt können wir das Template durchgehen und an unsere Bedürfnisse anpassen.

### 1. Schritt: Details einrichten {#step-1-set-up-the-details}

Passen wir die Canvas-Details an, um unser Ziel widerzuspiegeln.

1. Wählen Sie **Edit** neben dem Template-Namen.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas auf Nutzer:innen mit abgebrochenen Warenkörben abzielt.
3. Aktualisieren Sie die Beschreibung, um anzugeben, dass das Canvas Nutzer:innen ermutigen soll, Käufe aus der neuesten saisonalen Küchenartikel-Kollektion abzuschließen.
4. Fügen Sie den Tag **Abandon Cart** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### 2. Schritt: Konversions-Events zuweisen {#step-2-assign-your-conversion-events}

Als Nächstes weisen wir unser Konversions-Event zu. Da unser Fokus auf unserem Produkt „Enormous Paper Plate“ liegt, gehen wir für **Primary Conversion Event A** wie folgt vor:

1. Wählen Sie für den **Conversion event type** die Option **Makes Purchase**.
2. Wählen Sie **Make a specific purchase**. Damit können wir einen bestimmten Produktnamen auswählen.
3. Wählen Sie **Enormous Paper Plate**.

![Primäres Konversions-Event – A mit dem Conversion-Typ „Makes Purchase“ und dem Produktnamen „Enormous Paper Plate“. Es gibt eine 3-Tage-Conversion-Frist.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### 3. Schritt: Entry-Zeitplan festlegen {#step-3-set-an-entry-schedule}

Während der Entry-Zeitplan dieses Templates auf **API-Triggered** eingestellt ist, profitiert unser Anwendungsfall mehr von einem aktionsbasierten Eintritt für dieses Canvas, da wir uns auf Nutzer:innen konzentrieren möchten, die ihren Warenkorb abgebrochen haben (was eine Aktion ist).

1. Wählen Sie **Action-Based** als Entry-Zeitplan-Typ.
2. Wählen Sie **Abandoned Cart** als Trigger.
3. Wählen Sie für das Eintrittsfenster das Startdatum.
4. Wählen Sie die Option, Nutzer:innen in ihrer Ortszeit eintreten zu lassen. Dies kann unsere Nachrichten relevant halten und zu höherem Engagement führen, wenn Nachrichten zu optimalen Zeiten gesendet werden.

![Ein aktionsbasiertes Canvas, das auf Nutzer:innen abzielt, die ihren Warenkorb abgebrochen haben, mit dem Eintrittsfenster 15. Oktober 2024, 15:20 Uhr in der Ortszeit der Nutzer:innen.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### 4. Schritt: Festlegen, wer das Canvas betritt {#step-4-determine-who-enters-the-canvas}

Als Nächstes definieren wir unsere Zielgruppe als Nutzer:innen, die in den letzten 90 Tagen ausschließlich online bei uns eingekauft haben. Dies hilft uns, unsere Zielgruppe auf Nutzer:innen einzugrenzen, von denen wir wissen, dass sie mit unseren Produkten interagieren.

![„Online Shoppers Segment - 90 Days“ als Segment der Nutzer:innen, die für dieses Canvas angesprochen werden sollen.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Wir belassen die Eintrittskontrollen wie sie sind, sodass Nutzer:innen dieses Canvas nicht erneut betreten dürfen und es keine Begrenzung für die Anzahl der Personen gibt, die dieses Canvas potenziell betreten können.

Für die Austrittskriterien verlassen Nutzer:innen das Canvas, wenn sie den „Enormous Paper Plate“ gekauft haben. Auf diese Weise erhalten sie keine weiteren Nachrichten über einen Artikel, den sie bereits gekauft haben.

![Austrittskriterien, die festlegen, dass Nutzer:innen, die einen bestimmten Kauf für den „Enormous Paper Plate“ tätigen, das Canvas verlassen.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### 5. Schritt: Sendeeinstellungen auswählen {#step-5-select-your-send-settings}

Wir behalten die Standard-Abo-Einstellungen bei, sodass wir nur an Nutzer:innen senden, die Nachrichten oder Benachrichtigungen abonniert haben oder sich dafür angemeldet haben, und belassen die anderen Einstellungen wie sie sind.

### 6. Schritt: Canvas anpassen {#step-6-customize-your-canvas}

Jetzt erstellen wir unser Canvas, indem wir die Template-Schritte anpassen:

1. Wählen Sie den Aktionspfade-Schritt und dann den Aktionsgruppen-Namen **Made purchase**.
2. Wählen Sie für **Make Purchase** die Option **Make A Specific Purchase** und wählen Sie **Enormous Paper Plate** als Produkt. Ähnlich wie bei den Austrittskriterien verlassen Nutzer:innen, die dieses Produkt kaufen, das Canvas.

![Aktionsgruppe „Made purchase“, die das Canvas verlässt, wenn Nutzer:innen den „Enormous Paper Plate“ kaufen.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3. Wählen Sie im Nachrichten-Schritt **Edit message**, um die E-Mail anzupassen, die an unsere Nutzer:innen gesendet wird und sie über die Artikel in ihrem abgebrochenen Warenkorb informiert.
4. Belassen Sie den Verzögerungs-Schritt wie er ist.
5. In den Nachrichten-Schritten nach dem Zielgruppenpfad-Schritt passen wir die E-Mail- und SMS-Nachricht an, die unsere Nutzer:innen erhalten werden. Hier möchten wir unsere Nutzer:innen mit personalisiertem Messaging zum Kauf von Produkten ermutigen.

![Eine Vorschau der SMS-Nachricht, die Nutzer:innen erhalten werden: „Hi there, you left the enormous paper plate behind in your cart! Complete your purchase now and step up your hosting game. Use code MYPLATE at checkout for 20 percent off your order!“]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6. Wählen Sie im nächsten Aktionspfade-Schritt die Aktionsgruppe **Made purchase**. Wählen Sie dann **Make a specific purchase** und wählen Sie **Enormous Paper Plate** als Produkt. Dieser Schritt spiegelt den ersten Aktionspfade-Schritt wider, indem Nutzer:innen, die unser Produkt gekauft haben, das Canvas verlassen, damit sie keine weiteren Nachrichten erhalten.
7. Stellen Sie sicher, dass unser Audience-Sync-Schritt für die Synchronisierung mit Facebook eingerichtet ist. Dies wird zusätzlich beim Ad-Retargeting helfen.

{% alert tip %}
Sie können [Canvas-Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) verwenden, um die Nachrichten in Ihrem Canvas basierend auf dem Produkt, auf das Sie sich beziehen, anzupassen.
{% endalert %}

### 7. Schritt: Canvas testen und starten {#step-7-test-and-launch-the-canvas}

Nachdem Sie unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, wählen Sie **Launch Canvas**, um das Canvas zu starten. Jetzt können wir Nutzer:innen gezielt mit einer personalisierten User-Journey ansprechen, um sie zu ermutigen, das Produkt zu kaufen, das sie in ihren Warenkorb gelegt haben!

{% alert tip %}
Schauen Sie sich unsere [Checkliste vor und nach dem Start]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) an, um zu erfahren, was Sie vor und nach dem Start eines Canvas beachten sollten.
{% endalert %}