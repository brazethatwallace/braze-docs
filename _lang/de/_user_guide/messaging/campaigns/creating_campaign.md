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

Um eine Campaign zu erstellen und zu starten, benötigen Sie die Berechtigungen „Campaigns bearbeiten“ und „Campaigns starten“. Eine vollständige Liste der Workspace-Berechtigungen und wie sie im Dashboard angezeigt werden finden Sie unter [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

### Bevor Sie beginnen {#before-you-begin}

- Erstellen oder wählen Sie die [Segmente]({{site.baseurl}}/user_guide/audience/segments) aus, die festlegen, wer Ihre Nachrichten erhalten soll.
- Lesen Sie [Campaign-Grundlagen]({{site.baseurl}}/user_guide/messaging/campaigns/campaign_basics), damit Messaging-Kanäle, Zustellungsarten und Konversions-Ziele zu Ihrem Anwendungsfall passen.
- Für eine geführte Anleitung zu Zustellung, Targeting und Konversionen absolvieren Sie den Braze-Lernkurs [Campaign Setup](https://learning.braze.com/campaign-setup-delivery-targeting-conversions).
- Bitten Sie Operator, Ihnen beim Entwurf Ihrer Campaign auf Basis eines Briefings zu helfen oder Targeting- und Zustellungsoptionen zu verfeinern. Weitere Informationen finden Sie unter [Was Sie mit Operator tun können]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#campaigns-and-audiences).

## Campaign-Composer {#campaign-composer}

Im Campaign-Composer definieren Sie Zustellung, Zielgruppen, Konversionen und Starteinstellungen. Entscheiden Sie zunächst, ob Sie eine Einzelkanal- oder Mehrkanal-Campaign erstellen möchten, bevor Sie fortfahren.

{% tabs %}
{% tab Einzelkanal %}

Eine Einzelkanal-Campaign erreicht Nutzer:innen über einen einzelnen Messaging-Kanal pro Start.

### Was ist anders? {#whats-different}

#### Konversionen und Berichte {#single-channel-conversions}

Bei Einzelkanal-Campaigns verfolgt Braze [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), die Sie der Campaign zuweisen, anhand der Sends dieses Kanals. Informationen zu Attributionsfenstern und Zählregeln finden Sie unter [Regeln für das Konversions-Tracking]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules).

Die [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)-Einstellungen und Sendelimits des Workspace gelten weiterhin.

### Einzelkanal-Campaign erstellen {#create-a-single-channel-campaign}

So erstellen Sie eine Campaign:

1. Gehen Sie zu **Messaging** > **Campaigns**.
2. Wählen Sie **Create campaign** aus.
3. Wählen Sie den [Kanal]({{site.baseurl}}/user_guide/channels) aus, der zu Ihrem Anwendungsfall passt.
4. Schreiben und prüfen Sie im [Compose-Schritt](#step-1-compose-messages) den Text für diesen Kanal.

Jede Campaign verwendet jeweils einen Kanaltyp. Fügen Sie Varianten hinzu, wenn Sie kreative Aufteilungen vergleichen oder [A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing) durchführen möchten.

{% endtab %}
{% tab Mehrkanal %}

Eine Mehrkanal-Campaign erreicht Nutzer:innen über mehr als einen Messaging-Kanal in einem einzigen Start. Senden Sie beispielsweise eine E-Mail und eine Push-Benachrichtigung gleichzeitig.

{% alert note %}
[In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages) sind in Mehrkanal-Campaigns nicht verfügbar. Erstellen Sie stattdessen eine Einzelkanal-Campaign oder ein Canvas.
{% endalert %}

### Was ist anders?

#### Kontrollgruppen {#multichannel-control-groups}

Kontrollgruppen von Campaigns vergleichen Varianten innerhalb eines Kanals (zum Beispiel E-Mail A versus E-Mail B). Sie werden nicht verwendet, um ganze Kanäle innerhalb einer Mehrkanal-Campaign zu vergleichen. Um Kanäle, Kreativinhalte oder Timing kanalübergreifend in einer Journey zu testen, verwenden Sie [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

#### Konversionen und Berichte {#multichannel-conversions}

Bei Mehrkanal-Campaigns verfolgt Braze [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) pro Kanal. Wenn Nutzer:innen nach dem Erhalt von Nachrichten über mehr als einen Kanal konvertieren, kann Braze diese Konversion den jeweiligen Kanälen zuordnen. Die Konversionszahlen können *Unique Users* übersteigen, und Raten können 100 % überschreiten. Die vollständigen Regeln finden Sie unter [Regeln für das Konversions-Tracking]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules).

Rate-Limits für Sends über mehrere Kanäle werden unter [Mehrkanal-Campaigns und Canvase]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases) beschrieben. Workspace-weite Regeln (einschließlich der Anrechnung von Mehrkanal-Sends auf Limits) finden Sie unter [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Mehrkanal-Campaign erstellen {#create-a-multichannel-campaign}

1. Gehen Sie zu **Messaging** > **Campaigns**.
2. Wählen Sie **Create campaign** aus.
3. Wählen Sie **Multichannel** aus.
4. Wählen Sie im [Compose-Schritt](#step-1-compose-messages) **Add channel** aus und wählen Sie jeden benötigten Kanal. Wählen Sie die Kanal-Symbole aus, um zwischen den Composern zu wechseln, während Sie den Text für jeden Kanal verfassen.

{% endtab %}
{% endtabs %}

## Schritt 1: Nachrichten verfassen {#step-1-compose-messages}

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
Wenn jede Variante ähnlichen Textinhalt verwendet, verfassen Sie die Nachricht, **bevor** Sie zusätzliche Varianten hinzufügen. Verwenden Sie dann **Von Variante kopieren** aus dem Menü **Variante hinzufügen**, um Arbeit über Varianten oder Kanäle hinweg wiederzuverwenden.
{% endalert %}

## Schritt 2: Zustellung planen {#step-2-schedule-delivery}

Wählen Sie, wann Nutzer:innen berechtigt werden, die Kampagne zu erhalten:

| Zustellungstyp | Zusammenfassung |
| --- | --- |
| [Geplante Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery) | Senden Sie zu einem bestimmten Zeitpunkt oder in einem bestimmten Rhythmus. |
| [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) | Senden Sie, wenn Nutzer:innen Verhaltensweisen ausführen oder von Ihnen definierte Bedingungen erfüllen. |
| [API-getriggerte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) | Senden Sie, wenn Ihre Systeme Braze aufrufen, um die Kampagne für berechtigte Nutzer:innen zu Trigger or triggern or triggern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Zustellung planen" }

Informationen zu Planungskonzepten in Braze finden Sie unter [Kampagne planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

### Zustellungskontrollen {#delivery-controls}

Je nach Zustellungstyp können Sie die [Wiederberechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) anpassen (ob Nutzer:innen erneut in die Kampagne eintreten dürfen) und die [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)-Regeln des Workspace berücksichtigen. Sie können auch [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) konfigurieren, damit Nachrichten nicht während eingeschränkter Zeitfenster gesendet werden.

## Schritt 3: Zielgruppen definieren {#step-3-target-audiences}

Definieren Sie unter **Zielgruppen**, wer berechtigt ist, die Campaign zu erhalten. Alle Targeting-Optionen, UI-Anleitungen und Screenshots finden Sie unter [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users).

### Targeting-Optionen {#targeting-options}

In diesem Abschnitt können Sie Nutzer:innen ansprechen, indem Sie Segments oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Berechtigte Nutzer:innen müssen weiterhin den Trigger or triggern oder die Kriterien erfüllen, die Sie im Schritt **Zustellung planen** definiert haben. Die Zielgruppe ist wie ein Warteraum – nur Personen, die sich bereits darin befinden, können weitergehen, wenn die nächste Aktion eintritt.

[Unterdrückungslisten]({{site.baseurl}}/user_guide/audience/suppression_lists) des Workspace schließen gelistete Nutzer:innen automatisch aus, es sei denn, Sie erlauben eine Ausnahme für diese Campaign.

### Zielgruppen-Zusammenfassung {#audience-summary}

Nach dem Hinzufügen von Segments oder Filtern zeigt die **Zielgruppen-Zusammenfassung** eine Vorschau der Segment-Population, einschließlich der Anzahl der Nutzer:innen innerhalb dieses Segments, die über Ihre ausgewählten Kanäle erreichbar sind. Die Erreichbarkeitszahlen spiegeln Ihre Workspace-Daten, Kanaleinrichtung und Filter wider. Beachten Sie, dass die genaue Segment-Zugehörigkeit immer vor dem Nachrichtenversand berechnet wird. Bei sehr großen Zielgruppen zeigt Braze möglicherweise Schätzungen an, bis Sie exakte Statistiken berechnen.

{% alert note %}
Wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group) eingerichtet haben, ist die angezeigte Anzahl erreichbarer Nutzer:innen in der Zielgruppe Ihrer Campaign kleiner als die Anzahl erreichbarer Nutzer:innen, die für dasselbe Segment angezeigt wird. Das liegt daran, dass die Campaign Nutzer:innen in der globalen Kontrollgruppe ausschließt, die Segment-Zählung hingegen nicht.
{% endalert %}

### Nutzer:innen-Suche {#user-lookup}

Nach dem Hinzufügen von Segments oder Filtern können Sie testen, ob Ihre Zielgruppe wie erwartet eingerichtet ist, indem Sie nach Nutzer:innen suchen, um zu bestätigen, ob sie den Segmentkriterien entsprechen. Suchen Sie dazu im Abschnitt **Nutzer:innen-Suche** nach der `external_id` oder `braze_id` von Nutzer:innen. Eine Suche nach E-Mail-Adresse ist hier nicht möglich. Weitere Informationen finden Sie unter [Segmente testen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).

Wenn Nutzer:innen den Segment-, Filter- und App-Kriterien entsprechen, wird dies durch einen Hinweis bestätigt. Wenn Nutzer:innen einen Teil oder alle Segment-, Filter- oder App-Kriterien nicht erfüllen, werden die fehlenden Kriterien zur Fehlerbehebung aufgelistet.

### An diese Nutzer:innen senden {#send-to-these-users}

Verwenden Sie bei abo-basierten Kanälen (E-Mail, Kurzmitteilungsdienst or SMS und ähnliche) die Option **An diese Nutzer:innen senden**, um Ihre Campaign nur an Nutzer:innen mit einem bestimmten Abo-Status zu senden, z. B. an diejenigen, die abonniert und für E-Mail angemeldet sind.

### Sendevolumen begrenzen {#limit-send-volume}

Sie können die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten. Dies dient als Prüfung, die unabhängig von Ihren Campaign-Filtern ist. Weitere Informationen finden Sie unter [Maximale Nutzer:innen-Obergrenze festlegen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#setting-a-maximum-user-cap).

### Senderate dieser Campaign begrenzen {#limit-the-rate-at-which-this-campaign-sends}

Wenn Sie erwarten, dass große Campaigns einen Anstieg der Nutzer:innen-Aktivität verursachen und Ihre Server überlasten, können Sie ein Rate-Limit pro Minute für den Nachrichtenversand festlegen. Das bedeutet, dass Braze innerhalb einer Minute nicht mehr als Ihre Rate-Limit-Einstellung sendet. Weitere Informationen finden Sie unter [Rate-Limiting der Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting).

### A/B-Tests {#ab-testing}

Sie können einen [multivariaten oder A/B-Test]({{site.baseurl}}/user_guide/messaging/ab_testing) für jede Campaign erstellen, die einen einzelnen Kanal anspricht, auch wenn der einzelne Kanal mehrere Geräte umfasst. Wenn Sie beispielsweise multivariate oder A/B-Tests für eine Push-Campaign verwenden möchten, können Sie nur iOS-Geräte oder nur Android-Geräte ansprechen – nicht beide Gerätetypen in derselben Campaign.

Aktivieren Sie bei unterstützten Campaigns mit Einmalversand und Mehrfachversand die Option [Mit BrazeAI<sup>TM</sup> optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), um die Verteilung Ihrer Varianten automatisch zu optimieren.

## Schritt 4: Konversions-Events zuweisen {#step-4-assign-conversion-events}

[Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) messen Ergebnisse, nachdem Nutzer:innen Ihre Kampagne erhalten haben (oder in die Kontrollgruppe eingetreten sind). Braze verwendet standardmäßig **Starts Session** innerhalb eines kurzen Zeitfensters (drei Tage). Sie können Konversions-Events definieren, die zu Ihren KPIs passen – bis zu vier Events pro Kampagne.

Nach dem Start können Sie das [Conversions-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) verwenden, um Conversion-Trends über mehrere Campaigns oder Canvase hinweg zu analysieren, Kanäle zu vergleichen und Datumsbereiche, Attributionsmethoden und Aufschlüsselungen an einem Ort anzupassen.

{% alert important %}
Sie können nach dem Start der Kampagne keine Konversions-Events mehr hinzufügen oder entfernen. Bestätigen Sie die Events vor dem Start.
{% endalert %}

## Schritt 5: Zusammenfassung prüfen und starten {#step-5-review-summary-and-launch}

Der Schritt **Zusammenfassung prüfen** zeigt Planung, Zielgruppe, Varianten und Messaging-Einstellungen. Bevor Sie Ihre Kampagne starten:

1. Bestätigen Sie, dass Segmente, Varianten und Zustellungseinstellungen Ihrer Absicht entsprechen.
2. [Senden Sie Testnachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages), um Darstellung und Verhalten auf Ihren Testgeräten oder bei internen Empfänger:innen zu überprüfen.

Wenn Sie bereit sind, wählen Sie **Kampagne starten**.

### Genehmigungen {#approvals}

Wenn Ihr Workspace Genehmigungen verwendet, muss ein Teammitglied mit der Berechtigung zur Genehmigung von Kampagnen diese vor dem Start freigeben. Weitere Informationen finden Sie unter [Genehmigungen für Campaigns und Canvase]({{site.baseurl}}/user_guide/messaging/governance/approvals).

## Verwandte Artikel {#related-articles}

- [Gestalten und bearbeiten]({{site.baseurl}}/user_guide/messaging/design_and_edit)
- [A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing)
- [Vor dem Senden beachten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)
- [Campaign-Analytics]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics)