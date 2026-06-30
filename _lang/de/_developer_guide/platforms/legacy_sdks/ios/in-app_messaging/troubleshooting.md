---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung bei In-App-Nachrichten für iOS
platform: iOS
page_order: 7
description: "Dieser Referenzartikel behandelt mögliche Themen zur Fehlerbehebung bei iOS In-App-Nachrichten."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Fehlerbehebung bei In-App-Nachrichten {#troubleshoot-in-app-messages}

## Impressionen {#impressions}

### Impressions- oder Klick-Analytics werden nicht protokolliert {#impression-or-click-analytics-arent-being-logged}

Wenn Sie einen Delegaten für In-App-Nachrichten so festgelegt haben, dass die Anzeige von Nachrichten oder Klickaktionen manuell gesteuert wird, müssen Sie Klicks und Impressionen für die In-App-Nachricht manuell protokollieren.

#### Impressionen sind niedriger als erwartet {#impressions-are-lower-than-expected}

Die Synchronisierung der Trigger mit dem Gerät beim Start der Sitzung nimmt einige Zeit in Anspruch, sodass es zu einer Race-Condition kommen kann, wenn Nutzer:innen ein Event oder einen Kauf direkt nach dem Start einer Sitzung protokollieren. Ein möglicher Workaround könnte darin bestehen, die Campaign so zu ändern, dass sie beim Start der Sitzung getriggert wird, und dann nach dem beabsichtigten Event oder Kauf zu segmentieren. Beachten Sie, dass dies die In-App-Nachricht beim nächsten Sitzungsstart nach Eintreten des Events zustellen würde.

## Die erwartete In-App-Nachricht wurde nicht angezeigt {#expected-in-app-message-did-not-display}

Die meisten Probleme mit In-App-Nachrichten lassen sich in zwei Hauptkategorien unterteilen: Zustellung und Anzeige. Um herauszufinden, warum eine erwartete In-App-Nachricht nicht auf Ihrem Gerät angezeigt wurde, sollten Sie zunächst sicherstellen, dass die [In-App-Nachricht an das Gerät zugestellt wurde](#troubleshooting-in-app-message-delivery), und dann [die Anzeige der Nachricht überprüfen](#troubleshooting-in-app-message-display).

### Zustellung von In-App-Nachrichten {#troubleshooting-in-app-message-delivery}

Das SDK fordert beim Start der Sitzung In-App-Nachrichten von den Braze-Servern an. Um zu überprüfen, ob In-App-Nachrichten an Ihr Gerät zugestellt werden, müssen Sie sicherstellen, dass In-App-Nachrichten sowohl vom SDK angefordert als auch von den Braze-Servern zurückgegeben werden.

#### Prüfen Sie, ob Nachrichten angefordert und zurückgegeben werden {#check-if-messages-are-requested-and-returned}

1. Fügen Sie sich als [Testnutzer:in]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) im Dashboard hinzu.
2. Richten Sie eine In-App-Nachrichten-Campaign ein, die auf Ihre Nutzer:in ausgerichtet ist.
3. Stellen Sie sicher, dass in Ihrer Anwendung eine neue Sitzung stattfindet.
4. Überprüfen Sie anhand der [Event-Nutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), ob Ihr Gerät zu Beginn der Sitzung In-App-Nachrichten anfordert. Suchen Sie die SDK-Anfrage, die mit dem Sitzungsstart-Event Ihrer Testnutzer:in verknüpft ist.
  - Wenn Ihre App getriggerte In-App-Nachrichten anfordern sollte, sollten Sie `trigger` im Feld **Requested Responses** unter **Response Data** sehen.
  - Wenn Ihre App originale In-App-Nachrichten anfordern sollte, sollten Sie `in_app` im Feld **Requested Responses** unter **Response Data** sehen.
5. Überprüfen Sie anhand der [Event-Nutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), ob die korrekten In-App-Nachrichten in den Antwortdaten zurückgegeben werden.<br>![Event-Nutzerprotokolleinträge für In-App-Nachrichtenanfragen.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Fehlerbehebung bei nicht angeforderten Nachrichten {#troubleshoot-messages-not-being-requested}

Wenn Ihre In-App-Nachrichten nicht angefordert werden, kann es sein, dass Ihre App die Sitzungen nicht korrekt verfolgt, da In-App-Nachrichten beim Start der Sitzung aktualisiert werden. Vergewissern Sie sich außerdem, dass Ihre App tatsächlich eine Sitzung gemäß der Sitzungs-Timeout-Semantik Ihrer App startet:

![Die in den Event-Nutzerprotokollen gefundene SDK-Anfrage, die ein erfolgreiches Sitzungsstart-Ereignis anzeigt.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### Fehlerbehebung bei nicht zurückgegebenen Nachrichten {#troubleshoot-messages-not-being-returned}

Wenn Ihre In-App-Nachrichten nicht zurückgegeben werden, liegt wahrscheinlich ein Problem mit dem Targeting Ihrer Campaign vor:

- Ihr Segment enthält Ihre Nutzer:in nicht.
  - Überprüfen Sie den Tab [**Engagement**]({{ site.baseurl }}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) Ihrer Nutzer:in, um sicherzustellen, dass das korrekte Segment unter **Segments** angezeigt wird.
- Ihre Nutzer:in hat die In-App-Nachricht bereits erhalten und war nicht berechtigt, sie erneut zu erhalten.
  - Überprüfen Sie die [Einstellungen für die erneute Berechtigung der Campaign]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) im Schritt **Delivery** des **Campaign Composers** und stellen Sie sicher, dass die Einstellungen für die erneute Berechtigung mit Ihrer Testkonfiguration übereinstimmen.
- Ihre Nutzer:in hat die Häufigkeitsbegrenzung für die Campaign erreicht.
  - Überprüfen Sie die [Frequency-Capping-Einstellungen]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) der Campaign und stellen Sie sicher, dass diese mit Ihrer Testkonfiguration übereinstimmen.
- Wenn es in der Campaign eine Kontrollgruppe gab, könnte Ihre Nutzer:in in die Kontrollgruppe gefallen sein.
  - Sie können überprüfen, ob dies geschehen ist, indem Sie ein Segment mit einem Filter für empfangene Kampagnenvarianten erstellen, bei dem die Kampagnenvariante auf **Control** eingestellt ist, und überprüfen, ob Ihre Nutzer:in in dieses Segment fällt.
  - Wenn Sie Campaigns für Integrationstests erstellen, achten Sie darauf, keine Kontrollgruppe hinzuzufügen.

### Anzeige von In-App-Nachrichten {#troubleshooting-in-app-message-display}

Wenn Ihre App erfolgreich In-App-Nachrichten anfordert und empfängt, diese aber nicht angezeigt werden, verhindert möglicherweise eine geräteseitige Logik die Anzeige:

- Getriggerte In-App-Nachrichten werden auf Grundlage des [minimalen Zeitintervalls zwischen Triggern]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/in-app_message_delivery#minimum-time-interval-between-triggers) begrenzt, das standardmäßig 30 Sekunden beträgt.
- Wenn Sie einen Delegaten zum Anpassen der Handhabung von In-App-Nachrichten festgelegt haben, überprüfen Sie Ihren Delegaten, um sicherzustellen, dass er die Anzeige der In-App-Nachrichten nicht beeinträchtigt.
- Fehlgeschlagene Bild-Downloads verhindern die Anzeige von In-App-Nachrichten mit Bildern. Bild-Downloads schlagen immer fehl, wenn das `SDWebImage`-Framework nicht korrekt integriert ist. Überprüfen Sie Ihre Geräteprotokolle, um sicherzustellen, dass Bild-Downloads nicht fehlschlagen.
- Wenn die Ausrichtung des Geräts nicht mit der in der In-App-Nachricht angegebenen Ausrichtung übereinstimmt, wird die In-App-Nachricht nicht angezeigt. Vergewissern Sie sich, dass Ihr Gerät die korrekte Ausrichtung hat.