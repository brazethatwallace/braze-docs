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

Wenn Sie einen In-App-Nachrichten-Delegaten eingerichtet haben, um die Nachrichtenanzeige oder Klickaktionen manuell zu verarbeiten, müssen Sie Klicks und Impressionen für die In-App-Nachricht manuell protokollieren.

#### Impressionen sind niedriger als erwartet {#impressions-are-lower-than-expected}

Trigger or triggern benötigen Zeit, um sich beim Sitzungsstart mit dem Gerät zu synchronisieren, sodass eine Race-Condition auftreten kann, wenn Nutzer:innen ein Event oder einen Kauf direkt nach dem Sitzungsstart protokollieren. Ein möglicher Workaround wäre, die Campaign so umzustellen, dass sie beim Sitzungsstart ausgelöst wird, und dann nach dem beabsichtigten Event oder Kauf zu segmentieren. Beachten Sie, dass die In-App-Nachricht in diesem Fall beim nächsten Sitzungsstart nach dem Auftreten des Events zugestellt wird.

## Erwartete In-App-Nachricht wurde nicht angezeigt {#expected-in-app-message-did-not-display}

Die meisten Probleme mit In-App-Nachrichten lassen sich in zwei Hauptkategorien unterteilen: Zustellung und Anzeige. Um zu ermitteln, warum eine erwartete In-App-Nachricht auf Ihrem Gerät nicht angezeigt wurde, sollten Sie zunächst sicherstellen, dass die [In-App-Nachricht an das Gerät zugestellt wurde](#troubleshooting-in-app-message-delivery), und dann die [Anzeige der Nachricht untersuchen](#troubleshooting-in-app-message-display).

### Zustellung von In-App-Nachrichten {#troubleshooting-in-app-message-delivery}

Das SDK or Software-Development-Kit fordert bei Sitzungsbeginn In-App-Nachrichten von den Braze-Servern an. Um zu prüfen, ob In-App-Nachrichten an Ihr Gerät zugestellt werden, müssen Sie sicherstellen, dass In-App-Nachrichten sowohl vom SDK or Software-Development-Kit angefordert als auch von den Braze-Servern zurückgegeben werden.

#### Prüfen, ob Nachrichten angefordert und zurückgegeben werden {#check-if-messages-are-requested-and-returned}

1. Fügen Sie sich als [Testnutzer:in]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) im Dashboard hinzu.
2. Richten Sie eine In-App-Nachricht-Campaign ein, die auf Ihre:n Nutzer:in ausgerichtet ist.
3. Stellen Sie sicher, dass in Ihrer Anwendung eine neue Sitzung beginnt.
4. Verwenden Sie die [Event-Nutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), um zu prüfen, ob Ihr Gerät bei Sitzungsbeginn In-App-Nachrichten anfordert. Suchen Sie die SDK or Software-Development-Kit-Anfrage, die mit dem Sitzungsstart-Ereignis Ihrer:Ihres Testnutzer:in verknüpft ist.
  - Wenn Ihre App getriggerte In-App-Nachrichten anfordern sollte, sollten Sie `trigger` im Feld **Requested Responses** unter **Response Data** sehen.
  - Wenn Ihre App ursprüngliche In-App-Nachrichten anfordern sollte, sollten Sie `in_app` im Feld **Requested Responses** unter **Response Data** sehen.
5. Verwenden Sie die [Event-Nutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), um zu prüfen, ob die korrekten In-App-Nachrichten in den Antwortdaten zurückgegeben werden.<br>![Event-Nutzerprotokolleinträge für In-App-Nachricht-Anfragen.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Fehlerbehebung, wenn Nachrichten nicht angefordert werden {#troubleshoot-messages-not-being-requested}

Wenn Ihre In-App-Nachrichten nicht angefordert werden, verfolgt Ihre App möglicherweise Sitzungen nicht korrekt, da In-App-Nachrichten beim Sitzungsbeginn aktualisiert werden. Stellen Sie außerdem sicher, dass Ihre App basierend auf der Sitzungs-Timeout-Semantik Ihrer App tatsächlich eine Sitzung startet:

![Die in den Event-Nutzerprotokollen gefundene SDK or Software-Development-Kit-Anfrage, die ein erfolgreiches Sitzungsstart-Ereignis anzeigt.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### Fehlerbehebung, wenn Nachrichten nicht zurückgegeben werden {#troubleshoot-messages-not-being-returned}

Wenn Ihre In-App-Nachrichten nicht zurückgegeben werden, liegt wahrscheinlich ein Problem mit dem Campaign-Targeting vor:

- Ihr Segment enthält Ihre:n Nutzer:in nicht.
  - Überprüfen Sie den Tab [**Engagement**]({{ site.baseurl }}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) Ihrer:Ihres Nutzer:in, um zu sehen, ob das korrekte Segment unter **Segments** angezeigt wird.
- Ihre:Ihr Nutzer:in hat die In-App-Nachricht bereits erhalten und war nicht erneut berechtigt, sie wieder zu empfangen.
  - Überprüfen Sie die [Einstellungen zur erneuten Berechtigung der Campaign]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) im Schritt **Delivery** des **Campaign Composer** und stellen Sie sicher, dass die Einstellungen zur erneuten Berechtigung mit Ihrer Testkonfiguration übereinstimmen.
- Ihre:Ihr Nutzer:in hat das Frequency Cap für die Campaign erreicht.
  - Überprüfen Sie die [Frequency-Cap-Einstellungen]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) der Campaign und stellen Sie sicher, dass sie mit Ihrer Testkonfiguration übereinstimmen.
- Falls die Campaign eine Kontrollgruppe enthielt, ist Ihre:Ihr Nutzer:in möglicherweise in die Kontrollgruppe gefallen.
  - Sie können prüfen, ob dies geschehen ist, indem Sie ein Segment mit einem Filter für empfangene Campaign-Varianten erstellen, bei dem die Kampagnenvariante auf **Control** gesetzt ist, und überprüfen, ob Ihre:Ihr Nutzer:in in dieses Segment gefallen ist.
  - Wenn Sie Campaigns für Integrationstests erstellen, stellen Sie sicher, dass Sie auf das Hinzufügen einer Kontrollgruppe verzichten.

### Anzeige von In-App-Nachrichten {#troubleshooting-in-app-message-display}

Wenn Ihre App In-App-Nachrichten erfolgreich anfordert und empfängt, diese aber nicht angezeigt werden, verhindert möglicherweise eine geräteseitige Logik die Anzeige:

- Getriggerte In-App-Nachrichten unterliegen einer Ratenbegrenzung basierend auf dem [Mindestzeitintervall zwischen Trigger or triggern or triggern]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/in-app_message_delivery#minimum-time-interval-between-triggers), das standardmäßig 30 Sekunden beträgt.
- Wenn Sie einen Delegate zur Anpassung der Verarbeitung von In-App-Nachrichten eingerichtet haben, überprüfen Sie Ihren Delegate, um sicherzustellen, dass er die Anzeige von In-App-Nachrichten nicht beeinträchtigt.
- Fehlgeschlagene Bild-Downloads verhindern die Anzeige von In-App-Nachrichten mit Bildern. Bild-Downloads schlagen immer fehl, wenn das `SDWebImage`-Framework nicht korrekt integriert ist. Überprüfen Sie die Geräteprotokolle, um sicherzustellen, dass Bild-Downloads nicht fehlschlagen.
- Wenn die Geräteausrichtung nicht mit der in der In-App-Nachricht festgelegten Ausrichtung übereinstimmte, wird die In-App-Nachricht nicht angezeigt. Stellen Sie sicher, dass sich Ihr Gerät in der richtigen Ausrichtung befindet.