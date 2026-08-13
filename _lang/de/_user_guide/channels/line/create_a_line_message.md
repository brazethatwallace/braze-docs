---
nav_title: LINE-Nachricht erstellen
article_title: LINE-Nachricht erstellen
page_order: 1
description: "Dieser Artikel beschreibt, wie Sie eine LINE-Nachricht als Campaign oder Canvas erstellen."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# LINE-Nachricht erstellen {#create-a-line-message}

> Mit LINE-Campaigns können Sie Ihre Kund:innen direkt erreichen und programmatisch mit ihnen chatten. Sie können Liquid und andere dynamische Inhalte nutzen, um ein persönliches Erlebnis für Ihre Nutzer:innen zu schaffen und eine Umgebung zu fördern, die ein unaufdringliches Nutzererlebnis mit Ihrer Marke unterstützt und verbessert.

## Voraussetzungen {#prerequisites}

Bevor Sie eine LINE-Nachricht erstellen, führen Sie die folgenden Schritte aus:

1. Lesen Sie die LINE-Übersicht.
2. Machen Sie sich mit den Richtlinien, Limits und Content-Regeln vertraut.
3. [Richten Sie Ihre LINE-Verbindung ein]({{site.baseurl}}/user_guide/channels/line/line_setup).

Der Versand von LINE-Nachrichten über Braze wird von den Message- oder Action-Credits Ihres Kontos abgezogen.

## Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen {#step-1-choose-where-to-build-your-message}

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Campaign oder ein Canvas gesendet werden soll? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

**Schritte:**

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **LINE** oder, für Campaigns, die auf mehrere Kanäle abzielen, **Multichannel Campaign**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten.
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Campaign benötigen, und benennen Sie sie. Sie können für jede hinzugefügte Variante unterschiedliche Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie weitere Varianten hinzufügen. Sie können dann im Dropdown **Variante hinzufügen** die Option **Von Variante kopieren** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Schritte:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## Schritt 2: Ihre LINE-Nachricht verfassen {#step-2-compose-your-line-message}

Verfassen Sie Ihre Nachricht und verwenden Sie bei Bedarf Personalisierung (z. B. Liquid oder Connected-Content). LINE erlaubt bis zu fünf Nachrichtenblasen pro Nachricht, die in jedem der verfügbaren Nachrichtenlayouts gestaltet werden können: Text, Bild, Rich-Nachricht oder kartenbasierte Nachricht.

![LINE-Composer mit einer Nachricht in der Vorschau.]({% image_buster /assets/img/line/line_composer.png %})

### Tipps {#tips}

#### Liquid verwenden {#using-liquid}

Wenn Sie Liquid verwenden möchten, stellen Sie sicher, dass Sie einen Standardwert für Ihre Personalisierung angeben. So wird verhindert, dass Empfänger:innen mit unvollständigen Nutzerprofilen einen leeren Platzhalter erhalten. Anstatt beispielsweise die Nachricht „Hallo, !“ zu erhalten, könnte die Nachricht „Hallo, neue:r Abonnent:in!“ lauten.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Rechts-nach-links-Nachrichten erstellen {#creating-right-to-left-messages}

Das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten hängt weitgehend davon ab, wie Dienstanbieter sie darstellen. Best Practices für die Erstellung von Rechts-nach-links-Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Schritt 3: Vorschau anzeigen und Nachricht testen {#step-3-preview-and-test-your-message}

Wechseln Sie zum Tab **Test**, um eine Test-LINE-Nachricht an Content-Testgruppen oder einzelne Nutzer:innen zu senden, oder zeigen Sie eine Vorschau der Nachricht als Nutzer:in direkt in Braze an.

![Der Tab „Tests“ mit einer Vorschau einer Testnachricht.]({% image_buster /assets/img/line/test_preview.png %})

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line).

## Schritt 4: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie den Rest Ihrer Campaign. In den folgenden Abschnitten finden Sie weitere Details zur optimalen Nutzung unserer Tools zum Erstellen von LINE-Nachrichten.

### Zustellungszeitplan oder Trigger wählen {#choose-delivery-schedule-or-trigger}

LINE-Nachrichten können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen zu Zeitplan- und Trigger-Optionen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Sie können Zustellungskontrollen festlegen, z. B. Nutzer:innen erlauben, [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) für den Empfang der Campaign zu werden, oder [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)-Regeln aktivieren. Bei aktionsbasierter Zustellung können Sie auch die Dauer der Campaign und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) festlegen.

### Zielgruppe zusammenstellen {#choose-users-to-target}

[Stellen Sie Ihre Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segments oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie sollten bereits die Abo-Gruppe ausgewählt haben, die Nutzer:innen nach der Ebene oder Kategorie der Kommunikation eingrenzt, die sie mit Ihnen wünschen.

Wählen Sie die größere Zielgruppe aus Ihren Segments aus und grenzen Sie dieses Segment optional mit unseren [Filtern]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) weiter ein. Sie erhalten automatisch eine Momentaufnahme der ungefähren Segment-Population. Beachten Sie, dass die genaue Segment-Zugehörigkeit immer vor dem Versand der Nachricht berechnet wird.

### Konversions-Events wählen {#choose-conversion-events}

Braze ermöglicht es Ihnen, nachzuverfolgen, wie oft Nutzer:innen bestimmte Aktionen, sogenannte [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), nach dem Empfang einer Campaign ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Campaign zu messen. Zum Beispiel:

- Wenn Sie Geotargeting verwenden, um eine LINE-Nachricht zu triggern, deren Endziel ein Kauf durch die Nutzer:innen ist, setzen Sie das Konversions-Event auf `Purchase`.
- Wenn Sie versuchen, die Nutzer:innen in Ihre App zu bringen, setzen Sie das Konversions-Event auf `Starts Session`.

Sie können auch benutzerdefinierte Konversions-Events basierend auf Ihrem spezifischen Anwendungsfall festlegen. Werden Sie kreativ und überlegen Sie, wie Sie den Erfolg dieser Campaign messen möchten.

{% endtab %}
{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihres Canvas. Weitere Details zum Erstellen des restlichen Canvas, zur Nutzung multivariater Tests und der intelligenten Auswahl und mehr finden Sie unter [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

## Schritt 5: Überprüfen und bereitstellen {#step-5-review-and-deploy}

Nachdem Sie den letzten Teil Ihrer Campaign oder Ihres Canvas fertiggestellt haben, überprüfen Sie die Details, testen Sie alles und senden Sie es ab!

Lesen Sie als Nächstes den Artikel [LINE-Reporting]({{site.baseurl}}/line/reporting), um zu erfahren, wie Sie auf die Ergebnisse Ihrer LINE-Campaigns zugreifen können.