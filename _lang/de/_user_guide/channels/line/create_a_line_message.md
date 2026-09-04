---
nav_title: LINE-Nachricht erstellen
article_title: LINE-Nachricht erstellen
page_order: 1
description: "Erstellen Sie eine LINE-Nachricht und konfigurieren Sie kanalspezifische Nachrichtentypen, Felder, Klick-Tracking, Zustellungseinstellungen und Verhalten."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - LINE
alias: /line/create/
---

# LINE-Nachricht erstellen {#create-a-line-message}

> Erstellen Sie personalisierte LINE-Nachrichten in Campaigns oder Canvas. Wählen Sie aus Text-, Bild-, Rich- und kartenbasierten Nachrichten und kombinieren Sie bis zu fünf Nachrichten in einem Versand.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

| Voraussetzung | Beschreibung |
| --- | --- |
| LINE-Verbindung | Schließen Sie das [LINE-Setup]({{site.baseurl}}/user_guide/channels/line/line_setup) ab und prüfen Sie die Richtlinien, Limits und Inhaltsregeln des Kanals. |
| Campaign oder Canvas | Verwenden Sie eine Campaign für eine einzelne gezielte Nachricht oder Canvas für eine mehrstufige User Journey. |
| Nachrichtenplanung | Bereiten Sie Ihre Inhalte, Bilder, Links und Abo-Gruppe vor. |
| Nachrichten- oder Aktionsguthaben | Bestätigen Sie, dass Ihr Konto über verfügbare Guthaben verfügt. Der Versand von LINE-Nachrichten über Braze verwendet diese Guthaben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen für LINE-Nachrichten" }

## Nachricht erstellen {#create-a-message}

### Schritt 1: Wählen Sie aus, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **LINE** oder, für Campaigns, die auf mehrere Kanäle abzielen, **Multichannel Campaign**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden und die Verwendung Ihrer Campaigns in Berichten.
5. Fügen Sie Varianten für Ihre Campaign hinzu und benennen Sie sie. Jede Variante kann unterschiedliche Nachrichtentypen und Layouts verwenden. Weitere Informationen finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn Ihre Kampagnenvarianten ähnliche Inhalte haben, verfassen Sie zuerst die erste Nachricht, bevor Sie weitere Varianten hinzufügen. Dann können Sie im Dropdown **Variante hinzufügen** die Option **Von Variante kopieren** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### Schritt 2: Abo-Gruppe auswählen {#step-2-select-a-subscription-group}

Wählen Sie die **Abo-Gruppe** aus, die dem LINE-Kanal zugeordnet ist, über den die Nachricht gesendet wird. Eine Abo-Gruppe ist erforderlich, bevor Sie den Editor starten können.

Alle Varianten in einer LINE-Campaign müssen dieselbe Abo-Gruppe verwenden. Weitere Informationen zu LINE-Abo-Status finden Sie unter [LINE-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

### Schritt 3: LINE-Nachricht verfassen {#step-3-compose-your-line-message}

Wählen Sie **Editor starten** und ziehen Sie dann Nachrichtentypen per Drag-and-Drop in den Editor. Kombinieren Sie bis zu fünf Nachrichten in einem Versand und ordnen Sie sie in der Reihenfolge an, in der die Nutzer:innen sie erhalten.

![LINE-Composer mit einer Nachricht, die in der Vorschau angezeigt wird.]({% image_buster /assets/img/line/line_composer.png %})

#### Nachrichtentypen {#message-types}

| Nachrichtentyp | Felder und Einstellungen | Grenzen und Verhalten |
| --- | --- | --- |
| **Text** | Nachrichtentext mit Emojis, Liquid und URLs | Bis zu 5.000 Zeichen. |
| **Bild** | Bild aus der Medienbibliothek oder einer URL, einschließlich einer dynamischen URL | Bild-URLs können bis zu 2.000 Zeichen enthalten. Eigenständige Bildnachrichten unterstützen keine Klick-Aktionen. |
| **Rich-Nachricht** | Bild, alternativer Text, Template und antippbare Bereiche mit URI-Aktionen | Alternativer Text kann bis zu 400 Zeichen enthalten. Fügen Sie zwischen ein und 50 antippbare Bereiche hinzu. Aktionsbeschriftungen können bis zu 100 Zeichen enthalten, und jede URI kann bis zu 1.000 Zeichen enthalten. |
| **Kartenbasierte Nachricht** | Bis zu 10 Karten mit optionalem Bild und Kopfzeile, erforderlichem Textkörper und URI-Aktionen | Alternativer Text kann bis zu 400 Zeichen enthalten. Eine Kopfzeile kann bis zu 40 Zeichen enthalten. Ein Textkörper kann bis zu 60 Zeichen mit Bild oder Kopfzeile oder 120 Zeichen ohne beides enthalten. Jede Karte erfordert zwischen ein und drei Aktionen mit Beschriftungen von bis zu 20 Zeichen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="LINE-Nachrichtentypen, Felder und Grenzen" }

Zeichenbegrenzungen schließen Liquid-Syntax aus.

Für Bildspezifikationen, Rich-Nachricht-Templates, Karussell-Bildeinstellungen und Beispiele siehe [LINE-Nachrichtentypen]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/message_types).

{% alert note %}
Kartenbasierte Nachrichten wenden dieselben optionalen Felder und die gleiche Anzahl von Aktionen auf jede Karte an. Wenn beispielsweise eine Karte ein Bild und zwei Aktionen enthält, muss jede Karte ein Bild und zwei Aktionen enthalten.
{% endalert %}

#### Klickverhalten {#on-click-behavior}

Für antippbare Bereiche in Rich-Nachrichten und Karten wählen Sie **URI** für **Klickverhalten** und geben Sie dann das Ziel unter **URL öffnen** ein. Wählen Sie, ob die URL innerhalb von LINE geöffnet wird.

#### Personalisierung {#personalization}

Verwenden Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) oder [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), um Text, Bilder und URLs zu personalisieren. Fügen Sie einen Standardwert für die Liquid-Personalisierung ein, damit Profile mit unvollständigen Daten keine leeren Inhalte erhalten.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Für Sprachen, die von rechts nach links geschrieben werden, siehe [Nachrichten von rechts nach links erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Schritt 4: Klick-Tracking konfigurieren {#step-4-configure-click-tracking}

Im Tab **Einstellungen** verwenden Sie **Klick-Tracking**, um Links zum Sendezeitpunkt zu kürzen und zu tracken. Klick-Tracking ist standardmäßig für neue Nachrichten aktiviert und gilt für HTTP- und HTTPS-URLs in Text-, Rich- und kartenbasierten Nachrichten.

Braze verwendet `https://brz.ai` oder die für die Abo-Gruppe konfigurierte benutzerdefinierte Domain. Sie können getrackte URLs mit Liquid personalisieren. Für die Einrichtung nach Nachrichtentyp, Testverhalten, benutzerdefinierte Domains und Retargeting siehe [LINE-Klick-Tracking]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/line_click_tracking).

### Schritt 5: Nachricht in der Vorschau anzeigen und testen {#step-5-preview-and-test-your-message}

Gehen Sie zum Tab **Vorschau und Test**, um die Nachricht als Nutzer:in in der Vorschau anzuzeigen oder eine Test-LINE-Nachricht an eine Inhaltstest-Gruppe oder einzelne Nutzer:innen zu senden.

![Der Tab „Vorschau und Test“ mit einer Vorschau einer Testnachricht.]({% image_buster /assets/img/line/test_preview.png %})

Für Testanforderungen und Schritte siehe [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line).

### Schritt 6: Den Rest Ihrer Campaign oder Ihres Canvas erstellen {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Zustellungszeitplan oder Trigger auswählen {#choose-a-delivery-schedule-or-trigger}

Stellen Sie LINE-Nachrichten zu einem geplanten Zeitpunkt oder als Reaktion auf eine Aktion oder einen API-Trigger zu. Für Zeitplan- und Trigger-Optionen siehe [Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Konfigurieren Sie Zustellungskontrollen wie [Wiederberechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) und [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Für aktionsbasierte Zustellung legen Sie die Campaign-Dauer und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) fest.

#### Zielgruppe zusammenstellen {#choose-users-to-target}

[Stellen Sie Ihre Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segmente und Filter auswählen. Braze berechnet die exakte Segment-Mitgliedschaft vor dem Senden der Nachricht.

LINE kontrolliert den Abo-Status jedes/jeder Nutzer:in. Nutzer:innen müssen eine `native_line_id` haben und dem LINE-Kanal folgen, der der ausgewählten Abo-Gruppe zugeordnet ist, um die Nachricht zu empfangen. Weitere Details finden Sie unter [LINE-Abo-Status]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line).

#### Konversions-Events auswählen {#choose-conversion-events}

Verwenden Sie [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), um Aktionen zu messen, nachdem Nutzer:innen die Campaign erhalten haben. Legen Sie ein Konversionsfenster von bis zu 30 Tagen fest.

{% endtab %}
{% tab Canvas %}

Vervollständigen Sie die verbleibenden Abschnitte Ihres Canvas. Für Entry-Zeitpläne, Zielgruppen-Einstellungen und Sendesteuerungen siehe [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

Sie können eingehende LINE-Nachrichten verwenden, um einen Canvas basierend auf Trigger-Wörtern zu starten oder zu verzweigen. Für Verhaltens- und Großschreibungsanforderungen siehe [LINE-Nutzer:innen kontaktieren]({{site.baseurl}}/user_guide/channels/line/message_users).

{% endtab %}
{% endtabs %}

### Schritt 7: Überprüfen und bereitstellen {#step-7-review-and-deploy}

Nachdem Sie Ihre Campaign oder Ihren Canvas fertiggestellt haben, überprüfen Sie die Details und testen Sie die Nachricht, bevor Sie sie senden.

Nach dem Start verwenden Sie [LINE-Reporting]({{site.baseurl}}/user_guide/channels/line/reporting), um die Performance der Nachricht zu überprüfen.

## Wissenswerte Hinweise {#things-to-know}

- Eine LINE-Nachricht kann zwischen einer und fünf Nachrichten-Bubbles enthalten.
- Eine Abo-Gruppe entspricht einem LINE-Kanal, und alle Varianten in einer Campaign müssen dieselbe Abo-Gruppe verwenden.
- LINE ist die maßgebliche Quelle für den Abo-Status. Nutzer:innen, die dem ausgewählten LINE-Kanal nicht folgen, erhalten die Nachricht nicht.
- LINE berechnet Öffnungs- und klickbezogene Statistiken nur, wenn mehr als 20 Nutzer:innen das Event an einem bestimmten Tag ausführen.