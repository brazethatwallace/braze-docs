---
nav_title: Kampagne erstellen
article_title: Kampagne erstellen
page_order: 1
page_type: tutorial
description: "Erfahren Sie, wie Sie eine Braze-Messaging-Kampagne vom Verfassen bis zum Start erstellen – einschließlich Multichannel-Versand – und wie Sie die Zustellung planen, Zielgruppen definieren, Konversions-Events zuweisen, Tests senden und starten."
tool: Campaigns
---

# Kampagne erstellen {#create-a-campaign}

> Verwenden Sie Campaigns, wenn Sie Verbraucher:innen mit einem einzelnen Messaging-Schritt über einen oder mehrere unterstützte Kanäle erreichen möchten. Für mehrstufige Journeys verwenden Sie [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

## Voraussetzungen {#prerequisites}

Um eine Kampagne zu erstellen und zu starten, benötigen Sie die Berechtigungen „Kampagnen bearbeiten“ und „Kampagnen starten“. Eine vollständige Liste der Workspace-Berechtigungen und wie sie im Dashboard angezeigt werden, finden Sie unter [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

### Bevor Sie beginnen {#before-you-begin}

- Erstellen oder wählen Sie die [Segmente]({{site.baseurl}}/user_guide/audience/segments) aus, die festlegen, wer Ihre Nachrichten erhalten soll.
- Lesen Sie [Kampagnen-Grundlagen]({{site.baseurl}}/user_guide/messaging/campaigns/campaign_basics), damit Messaging-Kanäle, Zustellungstypen und Conversion Goals zu Ihrem Anwendungsfall passen.
- Für eine geführte Anleitung zu Zustellung, Targeting und Conversions absolvieren Sie den Braze-Lernkurs [Campaign Setup](https://learning.braze.com/campaign-setup-delivery-targeting-conversions).

## Kampagnen-Composer {#campaign-composer}

Im Kampagnen-Composer definieren Sie Zustellung, Zielgruppen, Conversions und Starteinstellungen. Entscheiden Sie, ob Sie eine Einzelkanal- oder Multichannel-Kampagne erstellen, bevor Sie fortfahren.

{% tabs %}
{% tab Einzelkanal %}

Eine Einzelkanal-Kampagne erreicht Nutzer:innen über einen Messaging-Kanal pro Start.

### Was ist anders {#whats-different}

#### Conversions und Reporting {#single-channel-conversions}

Bei Einzelkanal-Kampagnen verfolgt Braze [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), die Sie der Kampagne zuweisen, anhand der Sends dieses Kanals. Informationen zu Attributionsfenstern und Zählregeln finden Sie unter [Conversion-Tracking-Regeln]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules).

Das [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) und die Sendelimits des Workspace gelten weiterhin.

### Einzelkanal-Kampagne erstellen {#create-a-single-channel-campaign}

So erstellen Sie eine Kampagne:

1. Gehen Sie zu **Messaging** > **Campaigns**.
2. Wählen Sie **Kampagne erstellen**.
3. Wählen Sie den [Kanal]({{site.baseurl}}/user_guide/channels), der zu Ihrem Anwendungsfall passt.
4. Verfassen und prüfen Sie im [Schritt „Verfassen“](#step-1-compose-messages) den Text für diesen Kanal.

Jede Kampagne verwendet jeweils einen Kanaltyp. Fügen Sie Varianten hinzu, wenn Sie kreative Aufteilungen vergleichen oder [A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing) durchführen möchten.

{% endtab %}
{% tab Multichannel %}

Eine Multichannel-Kampagne erreicht Nutzer:innen über mehr als einen Messaging-Kanal in einem einzigen Start. Senden Sie beispielsweise eine E-Mail und eine Push-Benachrichtigung zusammen.

{% alert note %}
[In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages) sind in Multichannel-Kampagnen nicht verfügbar. Erstellen Sie stattdessen eine Einzelkanal-Kampagne oder ein Canvas.
{% endalert %}

### Was ist anders

#### Kontrollgruppen {#multichannel-control-groups}

Kampagnen-Kontrollgruppen vergleichen Varianten innerhalb eines Kanals (z. B. E-Mail A versus E-Mail B). Sie werden nicht verwendet, um ganze Kanäle innerhalb einer Multichannel-Kampagne zu vergleichen. Um Kanäle, Kreativmaterial oder Timing gemeinsam über eine Journey hinweg zu testen, verwenden Sie [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

#### Conversions und Reporting {#multichannel-conversions}

Bei Multichannel-Kampagnen verfolgt Braze [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) pro Kanal. Wenn Nutzer:innen nach dem Empfang von Nachrichten über mehr als einen Kanal konvertieren, kann Braze diese Conversion über diese Kanäle hinweg attribuieren. Conversion-Zahlen können *Unique Users* übersteigen, und Raten können 100 % überschreiten. Die vollständigen Regeln finden Sie unter [Conversion-Tracking-Regeln]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules).

Rate-Limits für Sends, die mehrere Kanäle umfassen, werden unter [Multichannel-Kampagnen und Canvases]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases) beschrieben. Workspace-weite Regeln (einschließlich der Anrechnung von Multichannel-Sends auf Obergrenzen) finden Sie unter [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Multichannel-Kampagne erstellen {#create-a-multichannel-campaign}

1. Gehen Sie zu **Messaging** > **Campaigns**.
2. Wählen Sie **Kampagne erstellen**.
3. Wählen Sie **Multichannel**.
4. Wählen Sie im [Schritt „Verfassen“](#step-1-compose-messages) **Kanal hinzufügen** und wählen Sie jeden benötigten Kanal aus. Wählen Sie die Kanalsymbole, um zwischen den Composern zu wechseln, während Sie den Text für jeden Kanal verfassen.

{% endtab %}
{% endtabs %}

## 1. Schritt: Nachrichten verfassen {#step-1-compose-messages}

### Kampagnendetails {#campaign-details}

Verwenden Sie die folgenden Felder, um Metadaten zu erfassen, die Ihrem Team helfen, die Kampagne zu finden und zu verwalten.

| Feld | Zweck |
| --- | --- |
| Name | Verwenden Sie einen aussagekräftigen Namen, der das Kampagnenziel widerspiegelt. |
| Beschreibung | Optional. Erklären Sie die Absicht oder verlinken Sie Briefings für Mitarbeitende. |
| Team | Optional. Weisen Sie [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) zu, damit die richtigen Gruppen diesen Send bearbeiten oder darüber berichten können. |
| Tags | Optional. Fügen Sie [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu, um in Listen und Tools wie dem [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) zu filtern. |
| Campaign-ID | Wo im Composer oder in der Zusammenfassung angezeigt, kopieren Sie diesen Bezeichner für API-Aufrufe, Reporting und Integrationen, die eine bestimmte Kampagne referenzieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kampagnendetails" }

### Kanäle und Editoren {#channels-and-editors}

Verfassen Sie in diesem Schritt kanalspezifische Inhalte. Eine ausführliche Anleitung finden Sie unter [Kanäle]({{site.baseurl}}/user_guide/channels) – öffnen Sie den Artikel für den von Ihnen gewählten Kanal.

### Varianten {#variants}

Fügen Sie Varianten hinzu, wenn Sie kreative oder Zustellungsaufteilungen vergleichen möchten. Hintergrundinformationen zu Experimenten und Kontrollgruppen finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn jede Variante ähnlichen Textinhalt verwendet, verfassen Sie die Nachricht, **bevor** Sie zusätzliche Varianten hinzufügen. Verwenden Sie dann **Copy from Variant** aus dem Menü **Variante hinzufügen**, um Arbeit über Varianten oder Kanäle hinweg wiederzuverwenden.
{% endalert %}

## 2. Schritt: Zustellung planen {#step-2-schedule-delivery}

Wählen Sie, wann Nutzer:innen berechtigt werden, die Kampagne zu erhalten:

| Zustellungstyp | Zusammenfassung |
| --- | --- |
| [Geplante Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery) | Senden Sie zu einem bestimmten Zeitpunkt oder in einem bestimmten Rhythmus. |
| [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) | Senden Sie, wenn Nutzer:innen Verhaltensweisen ausführen oder von Ihnen definierte Bedingungen erfüllen. |
| [API-getriggerte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) | Senden Sie, wenn Ihre Systeme Braze aufrufen, um die Kampagne für berechtigte Nutzer:innen zu triggern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2. Schritt: Zustellung planen" }

Informationen zu Planungskonzepten in Braze finden Sie unter [Kampagne planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

### Zustellungs-Kontrollgruppen {#delivery-controls}

Je nach Zustellungstyp können Sie die [Wiederberechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) anpassen (ob Nutzer:innen erneut in die Kampagne eintreten dürfen) und die [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)-Regeln des Workspace berücksichtigen. Sie können auch [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) konfigurieren, damit Nachrichten nicht während eingeschränkter Zeitfenster gesendet werden.

## 3. Schritt: Zielgruppen definieren {#step-3-target-audiences}

Definieren Sie unter **Target Audiences**, wer berechtigt ist, die Kampagne zu erhalten. Alle Targeting-Optionen, UI-Anleitungen und Screenshots finden Sie unter [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users).

### Targeting-Optionen {#targeting-options}

In diesem Abschnitt können Sie Nutzer:innen ansprechen, indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Berechtigte Nutzer:innen müssen weiterhin den Trigger oder die Kriterien erfüllen, die Sie im Schritt **Zustellung planen** definiert haben. Die Zielgruppe ist wie ein Warteraum – nur Personen, die sich bereits darin befinden, können weitergehen, wenn die nächste Aktion eintritt.

[Unterdrückungslisten]({{site.baseurl}}/user_guide/audience/suppression_lists) des Workspace schließen gelistete Nutzer:innen automatisch aus, es sei denn, Sie erlauben eine Ausnahme für diese Kampagne.

### Zielgruppen-Zusammenfassung {#audience-summary}

Nach dem Hinzufügen von Segmenten oder Filtern zeigt die **Zielgruppen-Zusammenfassung** eine Vorschau der Segment-Population, einschließlich der Anzahl der Nutzer:innen innerhalb dieses Segments, die über Ihre ausgewählten Kanäle erreichbar sind. Die Erreichbarkeitszahlen spiegeln Ihre Workspace-Daten, Kanaleinrichtung und Filter wider. Beachten Sie, dass die genaue Segment-Zugehörigkeit immer vor dem Nachrichtenversand berechnet wird. Bei sehr großen Zielgruppen zeigt Braze möglicherweise Schätzungen an, bis Sie exakte Statistiken berechnen.

### Nutzer:innen-Suche {#user-lookup}

Nach dem Hinzufügen von Segmenten oder Filtern können Sie testen, ob Ihre Zielgruppe wie erwartet eingerichtet ist, indem Sie nach Nutzer:innen suchen, um zu bestätigen, ob sie den Segmentkriterien entsprechen. Suchen Sie dazu im Abschnitt **User Lookup** nach der `external_id` oder `braze_id` von Nutzer:innen. Eine Suche nach E-Mail-Adresse ist hier nicht möglich. Weitere Informationen finden Sie unter [Segmente testen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).

Wenn Nutzer:innen den Segment-, Filter- und App-Kriterien entsprechen, wird dies durch einen Hinweis bestätigt. Wenn Nutzer:innen einen Teil oder alle Segment-, Filter- oder App-Kriterien nicht erfüllen, werden die fehlenden Kriterien zur Fehlerbehebung aufgelistet.

### An diese Nutzer:innen senden {#send-to-these-users}

Verwenden Sie bei abo-basierten Kanälen (E-Mail, SMS und ähnliche) **An diese Nutzer:innen senden**, um Ihre Kampagne nur an Nutzer:innen mit einem bestimmten Abo-Status zu senden, z. B. an diejenigen, die abonniert und für E-Mail angemeldet sind.

### Sendevolumen begrenzen {#limit-send-volume}

Sie können die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten. Dies dient als Prüfung, die unabhängig von Ihren Kampagnenfiltern ist. Weitere Informationen finden Sie unter [Maximale Nutzer:innen-Obergrenze festlegen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#setting-a-maximum-user-cap).

### Senderate dieser Kampagne begrenzen {#limit-the-rate-at-which-this-campaign-sends}

Wenn Sie erwarten, dass große Kampagnen einen Anstieg der Nutzer:innen-Aktivität verursachen und Ihre Server überlasten, können Sie ein Rate-Limit pro Minute für den Nachrichtenversand festlegen. Das bedeutet, dass Braze innerhalb einer Minute nicht mehr als Ihre Rate-Limit-Einstellung sendet. Weitere Informationen finden Sie unter [Rate-Limiting der Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting).

### A/B-Tests {#ab-testing}

Sie können einen [multivariaten oder A/B-Test]({{site.baseurl}}/user_guide/messaging/ab_testing) für jede Kampagne erstellen, die einen einzelnen Kanal anspricht, auch wenn der einzelne Kanal mehrere Geräte umfasst. Wenn Sie beispielsweise multivariate oder A/B-Tests für eine Push-Kampagne verwenden möchten, können Sie nur iOS-Geräte oder nur Android-Geräte ansprechen – nicht beide Gerätetypen in derselben Kampagne.

Für Push-, E-Mail- und Webhook-Kampagnen, die für einen einmaligen Versand geplant sind, können Sie auch eine [Optimierung]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) verwenden. Eine Optimierung reserviert einen Teil Ihrer Zielgruppe vom A/B-Test und hält ihn für einen zweiten optimierten Versand zurück, der auf den Ergebnissen des ersten Tests basiert.

## 4. Schritt: Konversions-Events zuweisen {#step-4-assign-conversion-events}

[Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) messen Ergebnisse, nachdem Nutzer:innen Ihre Kampagne erhalten haben (oder in die Kontrollgruppe eingetreten sind). Braze verwendet standardmäßig **Starts Session** innerhalb eines kurzen Zeitfensters (drei Tage). Sie können Konversions-Events definieren, die zu Ihren KPIs passen – bis zu vier Events pro Kampagne.

Nach dem Start können Sie das [Conversions-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) verwenden, um Conversion-Trends über mehrere Campaigns oder Canvases hinweg zu analysieren, Kanäle zu vergleichen und Datumsbereiche, Attributionsmethoden und Aufschlüsselungen an einem Ort anzupassen.

{% alert important %}
Sie können nach dem Start der Kampagne keine Konversions-Events mehr hinzufügen oder entfernen. Bestätigen Sie die Events vor dem Start.
{% endalert %}

## 5. Schritt: Zusammenfassung prüfen und starten {#step-5-review-summary-and-launch}

Der Schritt **Zusammenfassung prüfen** zeigt Planung, Zielgruppe, Varianten und Messaging-Einstellungen. Bevor Sie Ihre Kampagne starten:

1. Bestätigen Sie, dass Segmente, Varianten und Zustellungseinstellungen Ihrer Absicht entsprechen.
2. [Senden Sie Testnachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages), um Darstellung und Verhalten auf Ihren Testgeräten oder bei internen Empfänger:innen zu überprüfen.

Wenn Sie bereit sind, wählen Sie **Kampagne starten**.

### Genehmigungen {#approvals}

Wenn Ihr Workspace Genehmigungen verwendet, muss ein Teammitglied mit der Berechtigung zur Genehmigung von Kampagnen diese vor dem Start freigeben. Weitere Informationen finden Sie unter [Genehmigungen für Campaigns und Canvases]({{site.baseurl}}/user_guide/messaging/governance/approvals).

## Verwandte Artikel {#related-articles}

- [Entwerfen und bearbeiten]({{site.baseurl}}/user_guide/messaging/design_and_edit)
- [A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing)
- [Wissenswertes vor dem Senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)
- [Kampagnen-Analytics]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics)