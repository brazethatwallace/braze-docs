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

## Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#create-new-campaign-push}

{% alert tip %}
Sie sind sich nicht sicher, ob Sie eine Campaign oder ein Canvas verwenden sollen? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Für Campaigns, die mehrere Kanäle ansprechen, wählen Sie **Multichannel**. Andernfalls wählen Sie **Push-Benachrichtigung**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.

{% alert tip %}
Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach bestimmten Tags filtern.
{% endalert %}

{: start="5"}
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie für Ihre Campaign benötigen. Sie können für jede hinzugefügte Variante unterschiedliche Plattformen, Nachrichtentypen und Layouts wählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann **Von Variante kopieren** aus dem Dropdown **Variante hinzufügen** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}
{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## Schritt 2: Push-Plattformen auswählen {#step-2-select-push-platforms}

Wählen Sie als Nächstes aus, welche Kombination aus Plattform und mobilem Gerät die Push-Benachrichtigung erhalten soll. Mit dieser Auswahl können Sie die Zustellung einer Push-Benachrichtigung auf eine bestimmte Gruppe von Apps beschränken.

Je nach Ihren vorherigen Auswahlen gibt es verschiedene Möglichkeiten:

| Vorherige Auswahl | Optionen |
| --- | --- |
| Push-Benachrichtigungs-Campaign | Wählen Sie eine oder mehrere Plattformen und Geräte aus. Wenn Sie mehrere Geräte und Plattformen ansprechen möchten, wird die Bearbeitungsoberfläche so optimiert, dass Sie eine Nachricht für alle ausgewählten Plattformen verfassen können. Unter [Push-Nachrichten für mehrere Plattformen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push) erfahren Sie, was in dieser Bearbeitungsoberfläche anders ist. |
| Mehrkanalige Campaign | Wählen Sie **Add Messaging Channel** aus, um zusätzliche Push-Plattformen hinzuzufügen. Da die Plattformauswahl für jede Variante spezifisch ist, können Sie das Nachrichten-Engagement pro Plattform testen. |
| Canvas | Wählen Sie in Ihrem Nachrichtenschritt **+ Add more** aus, um zusätzliche Push-Plattformen hinzuzufügen. Ähnlich wie bei mehrkanaligen Campaigns ist die Plattformauswahl für jede Variante spezifisch. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Push-Plattformen auswählen" }

## Schritt 3: Benachrichtigungstyp auswählen (iOS und Android) {#step-3-select-notification-type-ios-and-android}

Wenn Sie eine plattformübergreifende Push-Campaign erstellen und Web und/oder Kindle auswählen, wird der Benachrichtigungstyp automatisch auf **Standard-Push** gesetzt und kann nicht geändert werden.

![Benachrichtigungstyp mit „Standard-Push“ als Beispiel ausgewählt.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Andernfalls wählen Sie für iOS und Android Ihren Benachrichtigungstyp aus:

- Standard-Push
- [Push-Storys]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) (unterstützt auf Android + iOS)
- Inline-Bild (nur Android)

Wenn Sie Bilder in Ihre Push-Campaign aufnehmen möchten, lesen Sie die folgenden Anleitungen zum Erstellen einer Rich-Benachrichtigung für [iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications) oder [Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications).

## Schritt 4: Push-Nachricht verfassen {#step-4-compose-your-push-message}

Jetzt ist es an der Zeit, Ihre Push-Nachricht zu schreiben! Im Tab **Verfassen** können Sie alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht bearbeiten.

![Tab „Verfassen“ beim Erstellen einer Push-Benachrichtigung.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

Der Inhalt des Tabs **Verfassen** variiert je nach dem im vorherigen Schritt gewählten Benachrichtigungstyp, kann aber eine der folgenden Optionen umfassen:

### Benachrichtigungskanal oder -gruppe (iOS und Android) {#notification-channel-or-group-ios-and-android}

Weitere Informationen zu plattformspezifischen Benachrichtigungsoptionen finden Sie unter [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options) oder [Android-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_options).

### Sprache {#language}

Fügen Sie Text in mehreren Sprachen hinzu, indem Sie den Button **Sprachen hinzufügen** verwenden. Wir empfehlen, Ihre Sprachen auszuwählen, bevor Sie Ihren Inhalt schreiben, damit Sie Ihren Text an der richtigen Stelle im Liquid einfügen können. Eine vollständige Liste der verfügbaren Sprachen finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/localization?tab=android).

Wenn Sie Text in einer Sprache hinzufügen, die von rechts nach links geschrieben wird, beachten Sie, dass das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten weitgehend davon abhängt, wie Dienstanbieter sie darstellen. Best Practices für die Erstellung von Rechts-nach-links-Nachrichten, die möglichst korrekt angezeigt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Titel und Text {#title-and-body}

{% tabs local %}
{% tab iOS %}
Beginnen Sie mit der Eingabe im Nachrichtenfeld und beobachten Sie, wie eine Vorschau im daneben befindlichen Vorschaufenster erscheint. Push-Nachrichten müssen als reiner Text formatiert sein.

Fügen Sie eine Überschrift über das Feld **Titel** hinzu. Um Ihre Push-Benachrichtigung personalisiert und gezielt zu gestalten, können Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) verwenden.
{% endtab %}

{% tab Android %}
Beginnen Sie mit der Eingabe im Nachrichtenfeld und beobachten Sie, wie eine Vorschau im daneben befindlichen Vorschaufenster erscheint. Push-Nachrichten müssen als reiner Text formatiert sein.

Um Ihre Push-Benachrichtigung personalisiert und gezielt zu gestalten, können Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) verwenden.

{% alert important %}
Sie **können** keine Android-Push-Nachricht ohne einen Titel senden&#8212;Sie können jedoch stattdessen ein einzelnes Leerzeichen eingeben. Beachten Sie, dass Ihre Nachricht als stille Push-Benachrichtigung gesendet wird, wenn sie nur ein einzelnes Leerzeichen enthält. Weitere Informationen finden Sie unter [Stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Brauchen Sie Hilfe beim Verfassen überzeugender Texte? Nutzen Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnlichen Marketingtext zur Verwendung in Ihren Nachrichten.

![Button „KI-Texter starten“ im Textfeld des Push-Composers.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

### Bild {#image}

Sofern unterstützt, wird Ihr App-Symbol automatisch als Bild für Ihre Push-Benachrichtigung hinzugefügt. Sie haben außerdem die Möglichkeit, Rich-Benachrichtigungen zu senden, die mehr Anpassungsmöglichkeiten in Ihren Push-Benachrichtigungen bieten, indem zusätzliche Inhalte über den Text hinaus hinzugefügt werden.

Weitere Hinweise zur Verwendung von Bildern in Ihren Push-Benachrichtigungen finden Sie in den folgenden Artikeln:

- [Rich-Benachrichtigungen für iOS erstellen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications)
- [Rich-Benachrichtigungen für Android erstellen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Klickverhalten {#on-click-behavior}

Legen Sie mit **Klickverhalten** fest, was passiert, wenn Nutzer:innen auf den Text einer Push-Benachrichtigung tippen. Sie können beispielsweise Kund:innen dazu auffordern, Ihre App zu öffnen, sie zu einer bestimmten Web-URL weiterleiten oder sogar eine bestimmte Seite Ihrer App über einen [Deeplink]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) öffnen.

Hier können Sie auch Button-Aktionen innerhalb Ihrer Push-Benachrichtigung einrichten, wie zum Beispiel:

- Akzeptieren/Ablehnen
- Ja/Nein
- Bestätigen/Abbrechen
- Mehr

### Sendeoptionen {#sending-options}

Wenn Nutzer:innen Ihre App auf mehreren Geräten installiert haben, wird Ihre Push-Nachricht standardmäßig an alle Geräte mit einem gültigen Push-Token gesendet. Falls gewünscht, können Sie **Zuletzt verwendetes Gerät** auswählen.

![Checkbox für Geräteoptionen, um diese Push-Benachrichtigung nur an das zuletzt verwendete Gerät der Nutzer:innen zu senden.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Es gibt einige Feinheiten bei dieser Einstellung. Wenn diese Option aktiviert ist, begrenzt Braze mehrfache Sendungen, außer wenn eine Campaign auf mehrere Plattformen abzielt, z. B. sowohl iOS als auch Android. Wenn Nutzer:innen Ihre App sowohl auf einem iOS- als auch auf einem Android-Gerät haben, erhalten sie eine Push-Benachrichtigung für beide Plattformen. Wenn das zuletzt verwendete Gerät von Nutzer:innen nicht [Push-aktiviert]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled) ist, wird die Nachricht nicht gesendet.

Standardmäßig sendet Braze Nachrichten an jedes Gerät von Nutzer:innen, das ein gültiges Push-Token besitzt. Für iOS können Sie Ihre Reichweite weiter eingrenzen, indem Sie Benachrichtigungen nur an iPad-Geräte oder nur an iPhone- und iPod-Geräte senden.

Falls gewünscht, können Sie das Push-Ziel auf **Zuletzt verwendetes Gerät** setzen.

#### Zuletzt verwendetes Gerät {#most-recently-used-device}

„Zuletzt verwendet“ ist ein technischer Status, kein verhaltensbezogener. Da Braze standardmäßig alle Geräte anspricht, schränkt der Wechsel zu dieser Einstellung Ihre Reichweite erheblich ein und stützt sich ausschließlich auf den Status des einzelnen Geräts mit dem neuesten Token.

Das zuletzt verwendete Gerät wird anhand des Geräts mit dem zuletzt aktualisierten Push-Token bestimmt, nicht anhand des Geräts mit der letzten Sitzung.
* Wenn ein Push-Token eines neuen Geräts über die API zu einem Kundenprofil hinzugefügt wird, gilt dieses Gerät sofort als das zuletzt verwendete, auch wenn die Nutzer:innen noch keine Sitzung darauf gestartet haben.
* Wenn das zuletzt verwendete Gerät von Nutzer:innen nicht [Push-aktiviert]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled) ist, wird die Nachricht überhaupt nicht gesendet.

Mehrfache Sendungen können weiterhin auftreten, wenn eine Campaign auf verschiedene Plattformen abzielt, z. B. sowohl iOS als auch Android. Wenn Nutzer:innen die App auf beiden Plattformen haben, können sie eine Push-Benachrichtigung für beide Plattformen erhalten.

Für iOS können Sie das Messaging weiter einschränken, indem Sie Push-Benachrichtigungen nur an iPad-Geräte oder nur an iPhone- und iPod-Geräte senden.

## Schritt 5: Vorschau anzeigen und Nachricht testen (optional) {#step-5-preview-and-test-your-message-optional}

Das Testen ist wohl einer der wichtigsten Schritte. Nachdem Sie Ihre perfekte Push-Nachricht verfasst haben, testen Sie sie, bevor Sie sie versenden. Wählen Sie den Tab **Test** aus, um zwischen verschiedenen Optionen zum Testen Ihrer Push-Nachricht zu wählen. Unter **Testempfänger:innen** können Sie eine Inhalts-Testgruppe oder einzelne Nutzer:innen auswählen. Sie können auch **Nachricht als Nutzer:in in der Vorschau anzeigen** verwenden, um einen Eindruck davon zu bekommen, wie Ihre Nachricht auf dem Mobilgerät für zufällige Nutzer:innen, vorhandene Nutzer:innen, benutzerdefinierte Nutzer:innen oder mehrsprachige Nutzer:innen aussehen könnte.

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=push).

## Schritt 6: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie den Rest Ihrer Campaign. In den folgenden Abschnitten erfahren Sie, wie Sie unsere Tools optimal für die Erstellung von Push-Benachrichtigungen nutzen können.

### Zustellungszeitplan oder Trigger wählen {#choose-delivery-schedule-or-trigger}

Push-Nachrichten können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen finden Sie unter [Zeitplanung Ihrer Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Bei aktionsbasierter Zustellung können Sie außerdem die Dauer der Campaign und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) festlegen.

In diesem Schritt können Sie auch Zustellungskontrollen festlegen, z. B. ob Nutzer:innen erneut [berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) werden können, die Campaign zu erhalten, oder ob [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)-Regeln aktiviert werden sollen.

### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes müssen Sie [Nutzer:innen als Zielgruppe auswählen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segmente oder Filter verwenden, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau auf die ungefähre Größe der Segmentpopulation. Detaillierte Zielgruppenstatistiken für die von Ihrer Campaign angesprochenen Kanäle sind in der Fußzeile verfügbar. Um zu sehen, welcher Prozentsatz Ihrer Nutzerbasis angesprochen wird und welchen LTV dieses Segment hat, wählen Sie **Zusätzliche Statistiken anzeigen**.

{% multi_lang_include audience/target_audiences.md %}

{% details Warum stimmt meine Kennzahl „Insgesamt erreichbare Nutzer:innen“ nicht mit der Summe aller Kanäle überein? %}

Wenn Sie die insgesamt erreichbaren Nutzer:innen für Ihre gefilterte Zielgruppe betrachten, fällt Ihnen möglicherweise auf, dass die Summe der einzelnen Spalten kleiner ist als die Gesamtzahl der erreichbaren Nutzer:innen. Diese Abweichung entsteht in der Regel dadurch, dass eine Reihe von Nutzer:innen zwar für das Segment oder die Filter der Campaign qualifiziert sind, aber nicht per Push erreichbar sind (z. B. weil sie keine gültigen oder aktiven [Push-Token]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#push-tokens) haben).

{% enddetails %}

![Tabelle mit detaillierten Zielgruppenstatistiken für erreichbare Nutzer:innen.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Beachten Sie, dass die genaue Segmentzugehörigkeit immer berechnet wird, bevor die Nachricht gesendet wird.

Sie können Ihre Campaign auch so einrichten, dass sie nur an Nutzer:innen mit einem bestimmten [Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions) gesendet wird, z. B. an Nutzer:innen, die Push-Nachrichten abonniert haben und per Opt-in zugestimmt haben.

Optional können Sie die Zustellung auch auf eine bestimmte Anzahl von Nutzer:innen innerhalb des Segments beschränken oder es erlauben, dass Nutzer:innen bei einer Wiederholung der Campaign dieselbe Nachricht zweimal erhalten.

#### Multichannel-Campaigns mit E-Mail und Push {#multichannel-campaigns-with-email-and-push}

Bei Multichannel-Campaigns, die sowohl E-Mail- als auch Push-Kanäle ansprechen, möchten Sie Ihre Campaign möglicherweise so einschränken, dass nur Nutzer:innen die Nachricht erhalten, die ausdrücklich per Opt-in zugestimmt haben (unter Ausschluss von abonnierten oder abgemeldeten Nutzer:innen). Nehmen wir beispielsweise an, Sie haben drei Nutzer:innen mit unterschiedlichen Opt-in-Status:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Wählen Sie dazu unter **Zusammenfassung der Zielgruppe** die Option, diese Campaign nur an „Nutzer:innen mit Opt-in“ zu senden. Diese Option stellt sicher, dass nur Nutzer:innen mit Opt-in Ihre E-Mail erhalten, und Braze sendet Ihre Push-Nachrichten standardmäßig nur an Nutzer:innen, die Push-fähig sind.

{% alert important %}
Fügen Sie bei dieser Konfiguration im Schritt **Zielgruppen** keine Filter hinzu, die die Zielgruppe auf einen einzelnen Kanal beschränken (z. B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

### Konversions-Events wählen {#choose-conversion-events}

Mit Braze können Sie nachverfolgen, wie oft Nutzer:innen bestimmte Aktionen ausführen, sogenannte [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), nachdem sie eine Campaign erhalten haben. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn Nutzer:innen die angegebene Aktion ausführen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Weitere Informationen zum Aufbau des restlichen Canvas, einschließlich multivariater Tests und [Optimieren mit BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), finden Sie unter [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

{% endtab %}
{% endtabs %}

## Schritt 7: Überprüfen und bereitstellen {#review-and-deploy-push}

Nachdem Sie den letzten Teil Ihrer Campaign oder Ihres Canvas fertiggestellt haben, überprüfen Sie die Details. Bei Campaigns gibt Ihnen die letzte Seite eine Zusammenfassung der von Ihnen entworfenen Campaign. Bestätigen Sie alle relevanten Details, stellen Sie sicher, dass Sie Ihre Nachricht getestet haben, und senden Sie sie ab – dann beobachten Sie, wie die Daten eintreffen!

Lesen Sie als Nächstes [Push-Berichte]({{site.baseurl}}/user_guide/channels/push/reporting), um zu erfahren, wie Sie auf die Ergebnisse Ihrer Push-Campaign zugreifen können. Für Push-Benachrichtigungen können Sie Statistiken zur Anzahl der gesendeten, zugestellten, gebouncten, geöffneten und direkt geöffneten Nachrichten einsehen.

### Fehlerbehebung {#troubleshooting}

#### Klickverhalten

Wenn Sie das Standard-Klickverhalten für Ihre SDK-Version verwenden und beim Auswählen einer Push-Benachrichtigung mit einer Web-URL diese in der App statt im Webbrowser geöffnet wird, lesen Sie die folgenden Integrationsleitfäden zur Handhabung von Push-Benachrichtigungen:

- [Swift]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#swift_step-2-enable-push-capabilities)
- [Android]({{site.baseurl}}/developer_guide/push_notifications#android_step-1-register-braze-firebase-messaging-service)

{% alert important %}
Sie müssen Ihr Delegate-Objekt mit `center.delegate = self` synchron zuweisen, bevor Ihre App den Start abgeschlossen hat, vorzugsweise in `application:didFinishLaunchingWithOptions:`. Andernfalls kann es passieren, dass Ihre App eingehende Push-Benachrichtigungen verpasst. Weitere Informationen finden Sie in der [Apple-Dokumentation zu `UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate).
{% endalert %}