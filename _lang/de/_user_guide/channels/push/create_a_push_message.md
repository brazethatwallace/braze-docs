---
nav_title: "Push-Nachricht erstellen"
article_title: "Push-Nachricht erstellen"
page_order: 1
page_type: tutorial
description: "Diese Tutorial-Seite behandelt die verschiedenen Komponenten bei der Erstellung einer Push-Nachricht, einschließlich Konfiguration, Versand, Targeting und mehr."
channel: push
tool:
  - Campaigns

---

# Push-Nachricht erstellen {#create-a-push-message}

> Push-Benachrichtigungen eignen sich hervorragend für zeitkritische Handlungsaufforderungen sowie zur Reaktivierung von Nutzer:innen, die die App längere Zeit nicht geöffnet haben. Erfolgreiche Push-Kampagnen führen Nutzer:innen direkt zu Inhalten und demonstrieren den Wert Ihrer App. Beispiele für Push-Benachrichtigungen finden Sie in unseren [Braze-Fallstudien](https://www.braze.com/customers).

## 1. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#create-new-campaign-push}

{% alert tip %}
Sie sind sich nicht sicher, ob Sie eine Campaign oder ein Canvas verwenden sollen? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Kampagne erstellen**.
2. Für Campaigns, die mehrere Kanäle ansprechen, wählen Sie **Multichannel**. Andernfalls wählen Sie **Push-Benachrichtigung**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) hinzu.

{% alert tip %}
Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
{% endalert %}

{: start="5"}
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie für Ihre Campaign benötigen. Sie können für jede hinzugefügte Variante unterschiedliche Plattformen, Nachrichtentypen und Layouts wählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann **Copy from Variant** aus dem Dropdown **Variante hinzufügen** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) mit dem Canvas-Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Schritt-Zeitplan]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) und legen Sie bei Bedarf eine Verzögerung fest.
4. Filtern Sie die Zielgruppe für diesen Schritt nach Bedarf. Sie können die Empfänger:innen dieses Schritts weiter eingrenzen, indem Sie Segmente angeben und zusätzliche Filter hinzufügen. Die Zielgruppenoptionen werden nach der Verzögerung zum Zeitpunkt des Nachrichtenversands überprüft.
5. Wählen Sie Ihr [Fortschrittsverhalten]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
6. Wählen Sie alle weiteren Messaging-Kanäle, die Sie mit Ihrer Nachricht kombinieren möchten.

{% endtab %}
{% endtabs %}

## 2. Schritt: Push-Plattformen auswählen {#step-2-select-push-platforms}

Wählen Sie als Nächstes, welche Plattform- und Mobilgerätekombination die Push-Benachrichtigung erhalten soll. Verwenden Sie diese Auswahl, um die Zustellung einer Push-Benachrichtigung auf eine bestimmte Gruppe von Apps zu beschränken.

Je nach Ihren vorherigen Auswahlen gibt es verschiedene Möglichkeiten:

| Vorherige Auswahl | Optionen |
| --- | --- |
| Push-Benachrichtigungs-Campaign | Wählen Sie eine oder mehrere Plattformen und Geräte aus. Wenn Sie mehrere Geräte und Plattformen ansprechen, wird Ihre Bearbeitungserfahrung für das Verfassen einer Nachricht für alle ausgewählten Plattformen optimiert. Siehe [Push-Nachrichten für mehrere Plattformen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push/), um zu verstehen, was bei dieser Bearbeitungserfahrung anders ist. |
| Multichannel-Campaign | Wählen Sie **Add Messaging Channel**, um zusätzliche Push-Plattformen hinzuzufügen. Da die Plattformauswahl variantenspezifisch ist, können Sie das Nachrichten-Engagement pro Plattform testen. |
| Canvas | Wählen Sie in Ihrem Nachrichten-Schritt **+ Add more**, um zusätzliche Push-Plattformen hinzuzufügen. Ähnlich wie bei Multichannel-Campaigns ist die Plattformauswahl variantenspezifisch. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-Plattformen auswählen" }

## 3. Schritt: Benachrichtigungstyp auswählen (iOS und Android) {#step-3-select-notification-type-ios-and-android}

Wenn Sie eine Push-Campaign für mehrere Plattformen erstellen und Web und/oder Kindle auswählen, wird der Benachrichtigungstyp automatisch auf **Standard-Push** gesetzt und kann nicht geändert werden.

![Benachrichtigungstyp mit Standard-Push als ausgewähltem Beispiel.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Andernfalls wählen Sie für iOS und Android Ihren Benachrichtigungstyp:

- Standard-Push
- [Push-Storys]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories/) (unterstützt auf Android und iOS)
- Inline-Bild (nur Android)

Wenn Sie Bilder in Ihre Push-Campaign einbinden möchten, lesen Sie die folgenden Anleitungen zum Erstellen einer Rich-Benachrichtigung für [iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/) oder [Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/).

## 4. Schritt: Push-Nachricht verfassen {#step-4-compose-your-push-message}

Jetzt ist es an der Zeit, Ihre Push-Nachricht zu schreiben! Der Tab **Verfassen** ermöglicht es Ihnen, alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht zu bearbeiten.

![Tab „Verfassen“ beim Erstellen einer Push-Benachrichtigung.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

Der Inhalt des Tabs **Verfassen** variiert je nach dem im vorherigen Schritt gewählten Benachrichtigungstyp, kann aber folgende Optionen umfassen:

### Benachrichtigungskanal oder -gruppe (iOS und Android) {#notification-channel-or-group-ios-and-android}

Weitere Informationen zu plattformspezifischen Benachrichtigungsoptionen finden Sie unter [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/) oder [Android-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_options/).

### Sprache {#language}

Fügen Sie Texte in mehreren Sprachen über den Button **Add Languages** hinzu. Wir empfehlen, Ihre Sprachen auszuwählen, bevor Sie Ihren Inhalt schreiben, damit Sie Ihren Text an der richtigen Stelle im Liquid einfügen können. Eine vollständige Liste der verfügbaren Sprachen finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Wenn Sie Text in einer Sprache hinzufügen, die von rechts nach links geschrieben wird, beachten Sie, dass das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten weitgehend davon abhängt, wie Dienstanbieter sie darstellen. Best Practices zum Erstellen von Rechts-nach-links-Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

### Titel und Text {#title-and-body}

{% tabs local %}
{% tab iOS %}
Beginnen Sie mit der Eingabe im Nachrichtenfeld und beobachten Sie, wie eine Vorschau im Vorschaufeld links erscheint. Push-Nachrichten müssen als reiner Text formatiert sein.

Fügen Sie eine Überschrift über das Feld **Title** hinzu. Um Ihren Push personalisiert und zielgerichtet zu gestalten, können Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) einbinden.
{% endtab %}

{% tab Android %}
Beginnen Sie mit der Eingabe im Nachrichtenfeld und beobachten Sie, wie eine Vorschau im Vorschaufeld links erscheint. Push-Nachrichten müssen als reiner Text formatiert sein.

Um Ihren Push personalisiert und zielgerichtet zu gestalten, können Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) einbinden.

{% alert important %}
Sie **können** keine Android-Push-Nachricht ohne Titel senden&#8212;Sie können jedoch stattdessen ein einzelnes Leerzeichen eingeben. Beachten Sie, dass Ihre Nachricht als stille Push-Benachrichtigung gesendet wird, wenn sie nur ein einzelnes Leerzeichen enthält. Weitere Informationen finden Sie unter [Stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Brauchen Sie Hilfe beim Erstellen überzeugender Texte? Probieren Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy) aus. Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte für Ihr Messaging.

![Button „KI-Textassistent starten“ im Textfeld des Push-Composers.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

### Bild {#image}

Sofern unterstützt, wird Ihr App-Symbol automatisch als Bild für Ihre Push-Benachrichtigung hinzugefügt. Sie haben auch die Möglichkeit, Rich-Benachrichtigungen zu senden, die mehr Anpassungsmöglichkeiten in Ihren Push-Benachrichtigungen bieten, indem zusätzliche Inhalte über den Text hinaus hinzugefügt werden.

Weitere Anleitungen zur Verwendung von Bildern in Ihren Push-Benachrichtigungen finden Sie in den folgenden Artikeln:

- [Rich-Benachrichtigungen für iOS erstellen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/)
- [Rich-Benachrichtigungen für Android erstellen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Klickverhalten {#on-click-behavior}

Legen Sie mit **On-Click Behavior** fest, was passiert, wenn Nutzer:innen den Text einer Push-Benachrichtigung auswählen. Sie können beispielsweise Kund:innen auffordern, Ihre Anwendung zu öffnen, Kund:innen zu einer bestimmten Web-URL weiterleiten oder sogar eine bestimmte Seite Ihrer Anwendung mit einem [Deeplink]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/) öffnen.

Hier können Sie auch Button-Aufforderungen innerhalb Ihrer Push-Benachrichtigung einrichten, wie zum Beispiel:

- Akzeptieren/Ablehnen
- Ja/Nein
- Bestätigen/Abbrechen
- Mehr

### Sendeoptionen {#sending-options}

Wenn Nutzer:innen Ihre App auf mehreren Geräten installiert haben, wird Ihre Push-Nachricht standardmäßig an alle Geräte mit einem gültigen Push-Token gesendet. Bei Bedarf können Sie **Most recently used device** auswählen.

![Kontrollkästchen für Geräteoptionen, um diesen Push nur an das zuletzt verwendete Gerät der Nutzer:innen zu senden.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Bei dieser Einstellung gibt es einige Feinheiten. Wenn diese Option ausgewählt ist, begrenzt Braze mehrfache Sendungen, außer wenn eine Campaign mehrere Plattformen anspricht, z. B. sowohl iOS als auch Android. Wenn Nutzer:innen Ihre App sowohl auf einem iOS- als auch auf einem Android-Gerät haben, erhalten sie einen Push für beide Plattformen. Wenn das zuletzt verwendete Gerät von Nutzer:innen nicht [Push-fähig]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled) ist, wird die Nachricht nicht gesendet.

Standardmäßig sendet Braze Nachrichten an jedes Gerät, das Nutzer:innen besitzen und das über ein gültiges Push-Token verfügt. Für iOS können Sie Ihre Reichweite weiter eingrenzen, indem Sie Benachrichtigungen nur an iPad-Geräte oder nur an iPhone- und iPod-Geräte senden.

Bei Bedarf können Sie das Push-Ziel auf **Most recently used device** setzen.

#### Zuletzt verwendetes Gerät {#most-recently-used-device}

„Zuletzt verwendet“ ist ein technischer Status, kein verhaltensbezogener. Da Braze standardmäßig an alle Geräte sendet, schränkt die Umstellung auf diese Einstellung Ihre Reichweite erheblich ein und stützt sich vollständig auf den Status des einzelnen Geräts mit dem neuesten Token.

Das zuletzt verwendete Gerät wird dadurch bestimmt, welches Gerät das zuletzt aktualisierte Push-Token hat, und nicht dadurch, welches Gerät die letzte Sitzung hatte.
* Wenn das Push-Token eines neuen Geräts über die API zu einem Nutzerprofil hinzugefügt wird, gilt dieses Gerät sofort als zuletzt verwendet, auch wenn die Nutzer:innen noch keine Sitzung darauf gestartet haben.
* Wenn das zuletzt verwendete Gerät von Nutzer:innen nicht [Push-fähig]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled) ist, wird die Nachricht überhaupt nicht gesendet.

Mehrfache Sendungen können weiterhin auftreten, wenn eine Campaign verschiedene Plattformen anspricht, z. B. sowohl iOS als auch Android. Wenn Nutzer:innen die App auf beiden haben, können sie einen Push für beide Plattformen erhalten.

Für iOS können Sie das Messaging weiter einschränken, indem Sie Push-Benachrichtigungen nur an iPad-Geräte oder nur an iPhone- und iPod-Geräte senden.

## 5. Schritt: Vorschau und Test Ihrer Nachricht (optional) {#step-5-preview-and-test-your-message-optional}

Das Testen ist wohl einer der wichtigsten Schritte. Nachdem Sie Ihre perfekte Push-Nachricht verfasst haben, testen Sie sie, bevor Sie sie versenden. Wählen Sie den Tab **Test**, um aus den Optionen zum Testen Ihrer Push-Nachricht zu wählen. Unter **Test Recipients** können Sie eine Inhalts-Testgruppe oder einzelne Nutzer:innen auswählen. Sie können auch **Preview message as user** verwenden, um einen Eindruck davon zu bekommen, wie Ihre Nachricht auf dem Mobilgerät für zufällige, bestehende, benutzerdefinierte oder mehrsprachige Nutzer:innen aussehen könnte.

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=push).

## 6. Schritt: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie den Rest Ihrer Campaign. In den folgenden Abschnitten finden Sie weitere Details zur optimalen Nutzung unserer Tools zum Erstellen von Push-Benachrichtigungen.

### Zustellungszeitplan oder Trigger wählen {#choose-delivery-schedule-or-trigger}

Push-Nachrichten können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Für aktionsbasierte Zustellung können Sie auch die Dauer der Campaign und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) festlegen.

In diesem Schritt können Sie auch Zustellungskontrollen festlegen, z. B. Nutzer:innen erlauben, [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns) zu werden, die Campaign zu erhalten, oder [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping)-Regeln aktivieren.

### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes müssen Sie die [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/), indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau der ungefähren Segment-Population. Detaillierte Zielgruppenstatistiken für die von Ihrer Campaign angesprochenen Kanäle sind in der Fußzeile verfügbar. Um zu sehen, welcher Prozentsatz Ihrer Nutzerbasis angesprochen wird und den Lifetime-Value für dieses Segment, wählen Sie **Show Additional Stats**.

{% multi_lang_include target_audiences.md %}

{% details Warum stimmt meine Metrik „Gesamte erreichbare Nutzer:innen“ nicht mit der Summe aller Kanäle überein? %}

Wenn Sie die gesamten erreichbaren Nutzer:innen für Ihre gefilterte Zielgruppe anzeigen, stellen Sie möglicherweise fest, dass die Summe der einzelnen Spalten kleiner ist als die gesamten erreichbaren Nutzer:innen. Diese Differenz entsteht in der Regel dadurch, dass eine Reihe von Nutzer:innen zwar für das Segment oder die Filter in der Campaign qualifiziert sind, aber nicht über Push erreichbar sind (z. B. weil sie keine gültigen oder aktiven [Push-Token]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle/#push-tokens) haben).

{% enddetails %}

![Tabelle mit detaillierten Zielgruppenstatistiken für erreichbare Nutzer:innen.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Beachten Sie, dass die genaue Segment-Zugehörigkeit immer vor dem Versand der Nachricht berechnet wird.

Sie können auch festlegen, dass Ihre Campaign nur an Nutzer:innen mit einem bestimmten [Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions/) gesendet wird, z. B. an diejenigen, die abonniert und für Push angemeldet sind.

Optional können Sie die Zustellung auch auf eine bestimmte Anzahl von Nutzer:innen innerhalb des Segments beschränken oder Nutzer:innen erlauben, dieselbe Nachricht bei einer Wiederholung der Campaign zweimal zu erhalten.

#### Multichannel-Campaigns mit E-Mail und Push {#multichannel-campaigns-with-email-and-push}

Bei Multichannel-Campaigns, die sowohl E-Mail- als auch Push-Kanäle ansprechen, möchten Sie Ihre Campaign möglicherweise so einschränken, dass nur Nutzer:innen, die ausdrücklich angemeldet sind, die Nachricht erhalten (unter Ausschluss von abonnierten oder abgemeldeten Nutzer:innen). Nehmen wir beispielsweise an, Sie haben drei Nutzer:innen mit unterschiedlichem Opt-in-Status:

- **Nutzer:in A** hat E-Mail abonniert und ist Push-fähig. Diese Person erhält die E-Mail nicht, wird aber den Push erhalten.
- **Nutzer:in B** hat sich für E-Mail angemeldet, ist aber nicht Push-fähig. Diese Person wird die E-Mail erhalten, erhält aber nicht den Push.
- **Nutzer:in C** hat sich für E-Mail angemeldet und ist Push-fähig. Diese Person wird sowohl die E-Mail als auch den Push erhalten.

Wählen Sie dazu unter **Zielgruppen-Zusammenfassung** aus, diese Campaign nur an „nur angemeldete Nutzer:innen“ zu senden. Diese Option stellt sicher, dass nur angemeldete Nutzer:innen Ihre E-Mail erhalten, und Braze sendet Ihren Push standardmäßig nur an Nutzer:innen, die Push-fähig sind.

{% alert important %}
Fügen Sie bei dieser Konfiguration im Schritt **Zielgruppe** keine Filter hinzu, die die Zielgruppe auf einen einzelnen Kanal beschränken (z. B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

### Konversions-Events wählen {#choose-conversion-events}

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen, [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), nach Erhalt einer Campaign ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Conversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Weitere Details zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und Intelligenter Auswahl und mehr finden Sie im Schritt [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## 7. Schritt: Überprüfen und bereitstellen {#review-and-deploy-push}

Nachdem Sie den letzten Teil Ihrer Campaign oder Ihres Canvas fertiggestellt haben, überprüfen Sie die Details. Bei Campaigns gibt Ihnen die letzte Seite eine Zusammenfassung der von Ihnen entworfenen Campaign. Bestätigen Sie alle relevanten Details, stellen Sie sicher, dass Sie Ihre Nachricht getestet haben, und senden Sie sie ab – dann beobachten Sie, wie die Daten eintreffen!

Lesen Sie als Nächstes [Push-Berichte]({{site.baseurl}}/user_guide/channels/push/reporting/), um zu erfahren, wie Sie auf die Ergebnisse Ihrer Push-Campaign zugreifen können. Für Push-Benachrichtigungen können Sie Statistiken zur Anzahl der gesendeten, zugestellten, gebouncten, geöffneten und direkt geöffneten Nachrichten einsehen.

### Fehlerbehebung {#troubleshooting}

#### Klickverhalten

Wenn Sie das Standard-Klickverhalten für Ihre SDK-Version verwenden und beim Auswählen einer Push-Benachrichtigung mit einer Web-URL diese in der App statt im Webbrowser geöffnet wird, lesen Sie die folgenden Integrationsleitfäden zur Handhabung von Push-Benachrichtigungen:

- [Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities)
- [Android]({{site.baseurl}}/developer_guide/push_notifications/#android_step-1-register-braze-firebase-messaging-service)

{% alert important %}
Sie müssen Ihr Delegate-Objekt mit `center.delegate = self` synchron zuweisen, bevor Ihre App den Start abgeschlossen hat, vorzugsweise in `application:didFinishLaunchingWithOptions:`. Andernfalls kann es passieren, dass Ihre App eingehende Push-Benachrichtigungen verpasst. Weitere Informationen finden Sie in der [Apple-Dokumentation zu `UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate).
{% endalert %}