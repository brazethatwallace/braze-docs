---
nav_title: Nachricht testen
article_title: Testnachrichten senden
page_order: 11.5
tool:
  - Campaigns
  - Canvas
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Testnachrichten über die verschiedenen Braze-Kanäle senden und wie Sie angepasste Event-Eigenschaften oder Nutzerattribute einbinden."
---

# Testnachrichten senden {#send-test-messages}

> Bevor Sie eine Messaging-Kampagne an Ihre Nutzer:innen senden, empfehlen wir als Best Practice, diese zu testen, um sicherzustellen, dass sie richtig aussieht und wie gewünscht funktioniert. Sie können Testnachrichten erstellen und an ausgewählte Geräte oder Teammitglieder senden, indem Sie die Tools im Braze-Dashboard verwenden.

{% alert important %}
Stellen Sie sicher, dass Sie Ihren Campaign-Entwurf nach dem Testen speichern, um das Löschen Ihrer Campaign zu vermeiden. Sie können Testnachrichten senden, ohne die Nachricht als Entwurf zu speichern.
{% endalert %}

## Schritt 1: Testnutzer:innen identifizieren {#step-1-identify-your-test-users}

Bevor Sie Ihre Messaging-Kampagne testen, ist es wichtig, Ihre Testnutzer:innen zu identifizieren. Diese Nutzer:innen können entweder bestehende Nutzer-IDs oder E-Mail-Adressen sein, oder neue Nutzer:innen, die ausschließlich zum Testen von Messaging-Kampagnen verwendet werden.

### Optional: Eine Content-Testgruppe erstellen {#optional-create-a-content-test-group}

Eine praktische Möglichkeit, Ihre Testnutzer:innen zu organisieren, ist die Erstellung einer [Content-Testgruppe]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), die eine Gruppe von Nutzer:innen enthält, die Testnachrichten von Campaigns erhalten. Sie können diese Testgruppe im Feld **Add Content Test Groups** unter **Test Recipients** in Ihrer Campaign hinzufügen und Ihre Tests starten, ohne einzelne Testnutzer:innen erstellen oder hinzufügen zu müssen.

## 2. Schritt: Kanalspezifische Testnachrichten senden {#step-2-send-channel-specific-test-messages}

Informationen zum Senden von Testnachrichten finden Sie im folgenden Abschnitt für den jeweiligen Kanal.

{% tabs local %}
{% tab Banner %}

{% alert important %}
Bevor Sie Banner-Nachrichten in Braze testen können, müssen Sie eine Banner-Campaign in Braze erstellen. Vergewissern Sie sich außerdem, dass die Platzierung, die Sie testen möchten, bereits [in Ihrer App oder Website platziert]({{site.baseurl}}/developer_guide/banners/placements) ist.
{% endalert %}

Nachdem Sie Ihre Banner-Nachricht erstellt haben, können Sie eine Vorschau anzeigen oder eine Testnachricht senden.

1. Entwerfen Sie Ihre Banner-Nachricht.
2. Wählen Sie **Vorschau**, um eine Vorschau Ihres Banners anzuzeigen oder eine Testnachricht zu senden.
3. Um eine Testnachricht zu senden, fügen Sie entweder eine Content-Testgruppe oder eine oder mehrere einzelne Nutzer:innen als **Testempfänger:innen** hinzu und wählen Sie dann **Test senden**.

Sie können Ihre Testnachricht bis zu 5 Minuten lang auf dem Gerät anzeigen.

![Vorschau-Tab des Banner-Composers.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Bitte beachten Sie, dass Ihre Vorschau aufgrund von Unterschieden in der Hardware möglicherweise nicht mit der endgültigen Darstellung auf dem Gerät der Nutzer:innen identisch ist.
{% endalert %}

### Test-Checkliste {#test-checklist}

- Ist Ihre Banner-Campaign einer Platzierung zugeordnet?
- Werden die Bilder und Medien auf den gewünschten Gerätetypen und Bildschirmgrößen wie erwartet angezeigt und verhalten sie sich entsprechend?
- Leiten Ihre Links und Buttons die Nutzer:innen an die richtige Stelle weiter?
- Funktioniert Liquid wie erwartet? Haben Sie einen Standardattributwert für den Fall festgelegt, dass Liquid keine Informationen zurückgibt?
- Ist Ihr Text klar, prägnant und korrekt?

{% endtab %}
{% tab Content-Card %}

{% alert important %}
Um einen Test an [Content-Testgruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) oder einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten aktiviert sein und ein gültiger Push-Token / Textbaustein für die Testnutzer:innen registriert sein, bevor Sie den Test senden. Für iOS-Nutzer:innen müssen Sie auf die von Braze gesendete Push-Benachrichtigung tippen, um die Test-Content-Card anzuzeigen. Dieses Verhalten gilt nur für Test-Content-Cards.
{% endalert %}

Test-Content-Cards werden über eine Push-Benachrichtigung zugestellt. Die Karte wird in der Push-Payload verpackt, und das SDK extrahiert und speichert sie lokal, wenn der Push empfangen wird.

Dieser Prozess umgeht das normale Kartenzustellungssystem, weshalb Push aktiviert sein muss, auch wenn Sie eine Content-Card testen.

Test-Content-Cards laufen ungefähr fünf Minuten nach dem Senden ab.

Nachdem Sie Ihre Content-Card erstellt haben, können Sie eine Test-Content-Card an Ihre App senden, um in Echtzeit zu sehen, wie sie aussieht.

1. Entwerfen Sie Ihre Content-Card.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Testgruppe oder einzelne Nutzer:innen aus, die diese Testnachricht erhalten sollen.
3. Wählen Sie **Test senden**, um Ihre Content-Card an Ihre App zu senden.

![Test-Content-Card]({% image_buster /assets/img/contentcard_test.png %})

### Vorschau {#preview}

Sie können eine Vorschau Ihrer Karte anzeigen, während Sie sie im Tab **Vorschau** erstellen. Dies sollte Ihnen helfen, sich vorzustellen, wie Ihre endgültige Nachricht aus der Perspektive Ihrer Nutzer:innen aussehen wird.

{% alert note %}
Im Tab **Vorschau** Ihres Composers stimmt die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät der Nutzer:innen überein. Wir empfehlen, immer eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und angepassten Attribute korrekt generiert werden.
{% endalert %}

### Test-Checkliste

- Sind Ihre Testnutzer:innen für Push mit einem gültigen Push-Token / Textbaustein angemeldet?
- Werden die Bilder und Medien wie erwartet angezeigt und verhalten sie sich entsprechend?
- Funktioniert Liquid wie erwartet? Haben Sie einen [Standardattributwert]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) festgelegt, falls Liquid keine Informationen zurückgibt?
- Ist Ihr Text klar, prägnant und korrekt?
- Leiten Ihre Links die Nutzer:innen an die richtige Stelle weiter?
- Sind Ihre Testnutzer:innen für Push mit einem gültigen Push-Token / Textbaustein angemeldet?

### Fehlerbehebung bei fehlerhaften Bildern {#troubleshooting-broken-images}

Wenn ein Content-Card-Bild nicht gerendert wird oder fehlerhaft erscheint:

- **Überprüfen Sie, ob die URL korrekt und URL-kodiert ist:** Sonderzeichen in der URL (wie Leerzeichen oder Abfrageparameter) müssen ordnungsgemäß kodiert sein. Andernfalls schlägt die Bildanfrage fehl.
- **Prüfen Sie Content-Security-Policies:** Wenn Ihre Organisation eine Content-Security-Policy (CSP) oder interne IT-Sicherheitsregeln hat, kann die Richtlinie die Bild-Domain blockieren. Bestätigen Sie, dass die Domain der Bild-URL von Ihrer CSP zugelassen wird.
- **Verwenden Sie HTTPS:** Bild-URLs sollten `https://` statt `http://` verwenden, um Mixed-Content-Blockierung in Browsern und Apps zu vermeiden.
- **Öffnen Sie die URL direkt in einem Browser:** Wenn das Bild nicht in einem Browser geladen wird, liegt das Problem bei der Bild-URL oder dem Hosting – nicht bei Braze.

### Debug {#debug}

Nachdem Ihre Content Cards gesendet wurden, können Sie alle Probleme über das [Event-Nutzerprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) in der Entwicklungskonsole aufschlüsseln oder debuggen.

Ein häufiger Anwendungsfall ist der Versuch herauszufinden, warum Nutzer:innen eine bestimmte Content-Card nicht sehen können. Dazu können Sie in den **Event-Nutzerprotokollen** nach den Content Cards suchen, die dem SDK bei Sitzungsstart zugestellt wurden, aber vor einer Impression, und diese auf eine bestimmte Campaign zurückverfolgen:

1. Gehen Sie zu **Einstellungen** > **Event-Nutzerprotokoll**.
2. Suchen und erweitern Sie die SDK-Anfrage für Ihre Testnutzer:innen.
3. Klicken Sie auf **Rohdaten**.
4. Suchen Sie die `id` für Ihre Sitzung. Das folgende Beispiel zeigt einen Auszug:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

{: start="5"}
5. Verwenden Sie ein Dekodierungstool wie [Base64 Decode and Encode](https://www.base64decode.org/), um die `id` aus dem Base64-Format zu dekodieren und die zugehörige `campaign_id` zu finden. In unserem Beispiel ergibt dies Folgendes:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Wobei `4861692e-6fce-4215-bd05-3254fb9e9057` die `campaign_id` ist.<br><br>

6. Gehen Sie zur Seite **Campaigns** und suchen Sie nach der `campaign_id`.

![Suche nach campaign_id auf der Campaigns-Seite]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

Von dort aus können Sie Ihre Nachrichteneinstellungen und den Inhalt überprüfen, um herauszufinden, warum Nutzer:innen eine bestimmte Content-Card nicht sehen können.

{% endtab %}
{% tab E-Mail %}

1. Entwerfen Sie Ihre E-Mail-Nachricht.
2. Wählen Sie **Vorschau und Test**.
3. Wählen Sie den Tab **Testversand** und fügen Sie Ihre E-Mail-Adresse oder Nutzer-ID im Feld **Einzelne Nutzer:innen hinzufügen** hinzu.
4. Wählen Sie **Test senden**, um Ihren E-Mail-Entwurf an Ihren Posteingang zu senden.

![Test-E-Mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

Wenn Ihre E-Mail einen Link zu einem [Präferenzcenter]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) enthält, generieren Testversendungen keinen funktionierenden Link und ermöglichen kein Speichern von Präferenzen. Um das Präferenzcenter zu testen, senden Sie die Nachricht stattdessen an Testnutzer:innen oder ein kleines internes Segment. Weitere Informationen finden Sie unter [Präferenzcenter testen]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers).

Wenn Ihre E-Mail-Campaign ein großes Bild enthält und in Outlook nicht wie erwartet angezeigt wird, sollten Sie die tatsächlichen Dateimaße des Bildes mit einem Bildbearbeitungs- oder Größenänderungstool reduzieren, anstatt es nur mit CSS oder HTML zu skalieren.

{% endtab %}
{% tab In-App-Nachricht %}

{% alert warning %}
Um einen Test an [Content-Testgruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) oder einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten vor dem Senden aktiviert sein. Beispielsweise müssen Sie Push auf Ihrem iOS-Gerät aktiviert haben, um auf die Benachrichtigung zu tippen, bevor die Testnachricht angezeigt wird. {% endalert %}

Wenn Sie Push-Benachrichtigungen in Ihrer App und auf Ihrem Testgerät eingerichtet haben, können Sie Test-In-App-Nachrichten an Ihre App senden, um in Echtzeit zu sehen, wie sie aussehen.

1. Entwerfen Sie Ihre In-App-Nachricht.
2. Wählen Sie den Tab **Test** und fügen Sie Ihre E-Mail-Adresse oder Nutzer-ID im Feld **Einzelne Nutzer:innen hinzufügen** hinzu.
3. Wählen Sie **Test senden**, um Ihre Push-Nachricht an Ihr Gerät zu senden.

Eine Test-Push-Nachricht wird oben auf dem Bildschirm Ihres Geräts angezeigt.

![In-App-Nachricht testen]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Testversendungen können dazu führen, dass mehr als eine In-App-Nachricht an jede Empfängerin bzw. jeden Empfänger gesendet wird.
{% endalert %}

Durch direktes Klicken und Öffnen der Push-Nachricht werden Sie zu Ihrer App weitergeleitet, wo Sie Ihren In-App-Nachrichten-Test anzeigen können. Beachten Sie, dass diese In-App-Nachrichten-Testfunktion darauf angewiesen ist, dass Nutzer:innen auf eine Test-Push-Benachrichtigung klicken, um die In-App-Nachricht auszulösen. Daher müssen die Nutzer:innen in der jeweiligen App für den Empfang von Push-Benachrichtigungen berechtigt sein, damit die Test-Push-Benachrichtigung erfolgreich zugestellt werden kann.

### Vorschau

Sie können eine Vorschau Ihrer In-App-Nachricht anzeigen, während Sie sie im Tab **Vorschau** erstellen. Dies sollte Ihnen helfen, sich vorzustellen, wie Ihre endgültige Nachricht aus der Perspektive Ihrer Nutzer:innen aussehen wird. Sie können eine Vorschau anzeigen, wie Ihre Nachricht für zufällige Nutzer:innen, bestimmte Nutzer:innen oder angepasste Nutzer:innen aussehen wird. Sie können auch eine Vorschau von Nachrichten für Mobilgeräte oder Tablets anzeigen.

![Erstellen-Tab beim Erstellen einer In-App-Nachricht, der die Vorschau der Nachricht zeigt. Es sind keine Nutzer:innen ausgewählt, daher wird der im Textbereich hinzugefügte Liquid-Code unverändert angezeigt.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze bietet drei Generationen von In-App Messages an. Sie können genau einstellen, an welche Geräte Ihre Nachrichten gesendet werden sollen, basierend darauf, welche Generation sie unterstützen.

![Wechsel zwischen Generationen bei der Vorschau einer In-App-Nachricht.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
In der **Vorschau** stimmt die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät der Nutzer:innen überein. Wir empfehlen immer, eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und angepassten Attribute korrekt generiert werden.
{% endalert %}

### Test-Checkliste

- Werden die Bilder und Medien wie erwartet angezeigt und verhalten sie sich entsprechend?
- Funktioniert Liquid wie erwartet? Haben Sie einen [Standardattributwert]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) festgelegt, falls Liquid keine Informationen zurückgibt?
- Ist Ihr Text klar, prägnant und korrekt?
- Leiten Ihre Buttons die Nutzer:innen an die richtige Stelle weiter?

### Barrierefreiheitsscanner {#accessibility-scanner}

Um Best Practices für Barrierefreiheit zu unterstützen, scannt Braze automatisch den Inhalt von In-App-Nachrichten, die mit dem traditionellen HTML-Editor erstellt wurden, auf Barrierefreiheitsstandards. Dieser Scanner hilft dabei, Inhalte zu identifizieren, die möglicherweise nicht den Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) entsprechen. WCAG ist ein Satz international anerkannter technischer Standards, die vom World Wide Web Consortium (W3C) entwickelt wurden, um Webinhalte für Menschen mit Behinderungen zugänglicher zu machen.

![Ergebnisse des Barrierefreiheitsscans]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
Der Barrierefreiheitsscanner für In-App-Nachrichten läuft nur bei Nachrichten, die mit benutzerdefiniertem HTML erstellt wurden.
{% endalert %}

#### So funktioniert es {#how-it-works}

Der Scanner läuft automatisch bei benutzerdefinierten HTML-Nachrichten und wertet Ihre gesamte HTML-Nachricht anhand des vollständigen [WCAG 2.1 AA-Regelwerks](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) aus. Für jedes markierte Problem wird Folgendes angezeigt:

- Das spezifische betroffene HTML-Element
- Eine Beschreibung des Barrierefreiheitsproblems
- Ein Link zu zusätzlichem Kontext oder Anleitungen zur Behebung

#### Automatisierte Barrierefreiheitstests verstehen {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Erstellen Sie Ihre LINE-Nachricht.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Testgruppe oder einzelne Nutzer:innen aus, die diese Testnachricht erhalten sollen.
3. Wählen Sie **Test senden**, um Ihre Nachricht zu senden.

![LINE-Testnachricht.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Mobiler Push {#mobile-push}

1. Entwerfen Sie Ihren mobilen Push.
2. Wählen Sie den Tab **Test** und fügen Sie Ihre E-Mail-Adresse oder Nutzer-ID im Feld **Einzelne Nutzer:innen hinzufügen** hinzu.
3. Wählen Sie **Test senden**, um Ihren Nachrichtenentwurf an Ihr Gerät zu senden.

![Push testen]({% image_buster /assets/img_archive/testpush.png %})

Wenn Sie eine Fehlermeldung erhalten, dass keine der ausgewählten Nutzer:innen über passende Push-Token / Textbaustein verfügt, haben die Testnutzer:innen keinen gültigen Push-Token / Textbaustein für die ausgewählte Plattform. Die Nutzer:innen müssen eine Sitzung in der App gestartet und Push für dieses Gerät aktiviert haben. Weitere Informationen finden Sie unter [Push-Aktivierung und Push-Abo]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

#### Web-Push {#web-push}

1. Erstellen Sie Ihren Web-Push.
2. Wählen Sie den Tab **Test**.
3. Wählen Sie **Test an mich senden**.
4. Wählen Sie **Test senden**, um Ihren Web-Push an Ihren Webbrowser zu senden.

![Web-Push testen]({% image_buster /assets/img_archive/testwebpush.png %})

Wenn Sie Push-Nachrichten vom Braze-Dashboard bereits akzeptiert haben, wird die Nachricht in der Ecke Ihres Bildschirms angezeigt. Andernfalls wählen Sie bei Aufforderung **Zulassen**, und die Nachricht wird angezeigt.

Wenn Sie eine Fehlermeldung erhalten, dass keine der ausgewählten Nutzer:innen über passende Push-Token / Textbaustein für Web-Push verfügt, überprüfen Sie, ob die Testnutzer:innen einen gültigen Push-Token / Textbaustein für die ausgewählte Plattform registriert haben. Um einen Push-Token / Textbaustein zu erhalten, müssen die Nutzer:innen so konfiguriert sein, dass sie Push-Benachrichtigungen für die App auf ihrem Gerät empfangen können. Weitere Einzelheiten finden Sie unter [Push-Aktivierung und Push-Abo]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

{% endtab %}
{% tab SMS/MMS und RCS %}

Nachdem Sie Ihre SMS-, MMS- oder RCS-Nachricht erstellt haben, können Sie eine Testnachricht an Ihr Telefon senden, um in Echtzeit zu sehen, wie sie aussehen wird. Die Empfängerin bzw. der Empfänger muss der SMS-Abo-Gruppe angehören, die Sie beim Senden des Tests auswählen, eine gültige Telefonnummer haben und mindestens ein Land unter **Geografische Berechtigungen** ausgewählt haben. Weitere Einzelheiten finden Sie unter [SMS-FAQs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages).

1. Entwerfen Sie Ihre SMS-, MMS- oder RCS-Nachricht.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Testgruppe oder einzelne Nutzer:innen aus, die diese Testnachricht erhalten sollen.
3. Wählen Sie **Test senden**, um Ihre Testnachricht zu senden.

![Test-Content-Card]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Nachdem Sie Ihren Webhook erstellt haben, können Sie einen Testversand durchführen, um die Webhook-Antwort zu überprüfen. Wählen Sie den Tab **Test** und wählen Sie **Test senden**, um einen Testversand an die angegebene Webhook-URL zu senden. Sie können auch einzelne Nutzer:innen auswählen, um die Antwort als bestimmte Nutzer:innen in der Vorschau anzuzeigen.

{% endtab %}
{% tab WhatsApp %}

1. Erstellen Sie Ihre WhatsApp-Nachricht.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Testgruppe oder einzelne Nutzer:innen aus, die diese Testnachricht erhalten sollen.
3. Initiieren Sie ein Konversationsfenster, indem Sie eine WhatsApp-Nachricht an die Telefonnummer senden, die mit der Abo-Gruppe verknüpft ist, die Sie für diese Nachricht verwenden. Die zugehörige Telefonnummer wird im Hinweis auf dem Tab **Test** angezeigt.
4. Wählen Sie **Test senden**, um Ihre Nachricht zu senden.

![WhatsApp-Testnachricht.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Personalisierte Campaigns testen {#test-personalized-campaigns}

Wenn Sie Campaigns testen, die Nutzerdaten befüllen oder angepasste Event-Eigenschaften verwenden, müssen Sie zusätzliche oder andere Schritte ausführen.

### Campaigns mit Nutzerattributen testen {#testing-campaigns-personalized-with-user-attributes}

Wenn Sie [Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) in Ihrer Nachricht verwenden, müssen Sie zusätzliche Schritte ausführen, um Ihre Campaign korrekt in der Vorschau anzuzeigen und sicherzustellen, dass die Nutzerdaten den Content ordnungsgemäß befüllen.

Wenn Sie eine Testnachricht senden, stellen Sie sicher, dass Sie entweder die Option **Select Existing User** auswählen oder die Vorschau als **Custom User** anzeigen.

![Testen einer personalisierten Nachricht]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Bestehende:n Nutzer:in auswählen {#selecting-an-existing-user}

Wenn Sie eine:n bestehende:n Nutzer:in auswählen, geben Sie die spezifische Nutzer-ID oder E-Mail-Adresse in das Suchfeld ein. Verwenden Sie dann die Dashboard-Vorschau, um zu sehen, wie Ihre Nachricht für diese:n Nutzer:in aussehen würde, und senden Sie eine Testnachricht an Ihr Gerät, die widerspiegelt, was diese:r Nutzer:in sehen würde.

![Nutzer:in auswählen]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Angepasste:n Nutzer:in auswählen {#selecting-a-custom-user}

Wenn Sie die Vorschau als angepasste:n Nutzer:in anzeigen, geben Sie Text für die verschiedenen verfügbaren Felder zur Personalisierung ein, wie zum Beispiel den Vornamen und angepasste Attribute. Auch hier können Sie Ihre eigene E-Mail-Adresse eingeben, um einen Test an Ihr Gerät zu senden.

![Angepasste:r Nutzer:in]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Bestehende:n Nutzer:in anpassen {#customizing-an-existing-user}

Sie können einzelne Felder einer/eines zufälligen oder bestehenden Nutzer:in bearbeiten, um dynamischen Content innerhalb Ihrer Nachricht zu testen. Wählen Sie **Edit**, um die/den ausgewählte:n Nutzer:in in eine:n angepasste:n Nutzer:in umzuwandeln, die/den Sie bearbeiten können.

![Der Tab „Preview as a User“ mit einem „Edit“-Button.]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Campaigns mit angepassten Event-Eigenschaften testen {#testing-campaigns-personalized-with-custom-event-properties}

Das Testen von Campaigns, die mit [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) personalisiert sind, unterscheidet sich leicht vom Testen anderer hier beschriebener Campaign-Typen.

{% tabs local %}
{% tab Manuell triggern %}

#### Methode 1: Campaign manuell triggern {#method-1-triggering-campaign-manually}

Sie können die Campaign selbst triggern als robuste Möglichkeit, Campaigns zu testen, die angepasste Event-Eigenschaften verwenden:

1. Verfassen Sie den Text, der die Event-Eigenschaft enthält.

![Testnachricht mit Eigenschaften verfassen]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Verwenden Sie die [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery), um die Campaign zu senden, wenn das Event eintritt.

{% alert note %}
Wenn Sie eine iOS-Push-Campaign testen, müssen Sie die Verzögerung auf eine Minute setzen, um sich genug Zeit zu geben, die App zu verlassen, da iOS keine Push-Benachrichtigungen für die aktuell geöffnete App zustellt. Andere Campaign-Typen können auf sofortige Zustellung eingestellt werden.
{% endalert %}

![Zustellung der Testnachricht]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Erstellen Sie das Targeting der Nutzer:innen wie beim Testen üblich, indem Sie einen Testfilter verwenden oder Ihre eigene E-Mail-Adresse als Ziel angeben, und stellen Sie die Campaign fertig.

![Targeting der Testnachricht]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Öffnen Sie Ihre App und führen Sie das angepasste Event aus.

Die Campaign wird getriggert und zeigt die Nachricht mit der Event-Eigenschaft personalisiert an.

![Beispiel einer Testnachricht]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Testnachricht %}

#### Methode 2: Sich selbst eine Testnachricht senden {#method-2-sending-yourself-a-test-message}

Alternativ können Sie die Campaign auch testen, indem Sie sich selbst eine angepasste Testnachricht senden, sofern Sie angepasste Nutzer-IDs gespeichert haben.

1. Verfassen Sie den Text für Ihre Campaign.
2. Wählen Sie den Tab **Test** und dann **Customized User**.
3. Fügen Sie die angepasste Event-Eigenschaft am unteren Seitenrand hinzu und geben Sie Ihre Nutzer-ID oder E-Mail-Adresse im oberen Feld ein.
4. Wählen Sie **Send Test**, um eine mit der Eigenschaft personalisierte Nachricht zu erhalten.

![Testen mit angepassten Nutzer:innen]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Methode 3: Liquid verwenden {#method-3-using-liquid}

Sie können angepasste Event-Eigenschaften testen, indem Sie Werte manuell mit Liquid eingeben.

1. Geben Sie im Nachrichten-Editor Werte für Ihre angepassten Event-Eigenschaften ein.
2. Wählen Sie den Tab **Preview as a User**, um zu überprüfen, ob die richtige Nachricht angezeigt wird.

{% endtab %}
{% endtabs %}

## Einschränkungen {#limitations}

Es gibt einige Situationen, in denen sich Testnachrichten nicht genauso verhalten wie Campaigns oder Canvases, die an echte Nutzer:innen gesendet werden. Erwägen Sie in diesen Fällen, die Campaign oder das Canvas an eine begrenzte Gruppe von Testnutzer:innen zu senden, um dieses Verhalten zu validieren.

- Wenn Sie das Braze-[Präferenzcenter]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) über Testnachrichten aufrufen, ist der Button **Einstellungen speichern** deaktiviert. Liquid-Tags des Präferenzcenters werden möglicherweise auch nicht zu gültigen Links aufgelöst. Dies ist das erwartete Verhalten. Informationen zum End-to-End-Testen finden Sie unter [Präferenzcenter testen]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers).
- Zum Testen von In-App-Nachrichten und Content Cards muss die Zielnutzer:in über ein Push-Token / Textbaustein für das Zielgerät verfügen.
- Zum Testen von Abmeldelinks in E-Mails stellen Sie sicher, dass sich die E-Mail-Adresse Ihrer Testnutzer:in im entsprechenden Workspace befindet.
- Der `List-Unsubscribe`-Header ist nicht in E-Mails enthalten, die über die Testnachrichtenfunktion gesendet werden.
- E-Mails, die an Nutzer:innen einer Seed-Gruppe gesendet werden, aktualisieren nicht die Liste der empfangenen Campaigns im Kundenprofil und erhöhen auch nicht die Sendungen in den Dashboard-Analytics.

## Fehlerbehebung {#troubleshooting}

### In-App-Nachrichten {#in-app-messages}

Wenn Ihre In-App-Nachrichten-Campaign nicht durch eine Push-Campaign getriggert wird, überprüfen Sie die Segmentierung der In-App-Campaign, um sicherzustellen, dass die Nutzer:innen die Zielgruppe erfüllen, **bevor** sie die Push-Nachricht erhalten.

Bei Testsendungen auf Android und iOS werden In-App-Nachrichten, die das On-Klick, der-Verhalten **Push-Berechtigung anfordern** verwenden, möglicherweise auf einigen Geräten nicht angezeigt. Als Workaround:
- **Android:** Geräte müssen Android 13 und unser Android SDK Version 21.0.0 verwenden. Ein weiterer Grund kann sein, dass das Gerät, auf dem die In-App-Nachricht angezeigt wird, bereits eine Aufforderung auf Systemebene hat. Möglicherweise haben Sie **Nicht erneut fragen** ausgewählt, sodass Sie die App möglicherweise neu installieren müssen, um die Benachrichtigungsberechtigungen vor einem erneuten Test zurückzusetzen.
- **iOS:** Wir empfehlen Ihrem Entwicklerteam, die Implementierung von Push-Benachrichtigungen für Ihre App zu überprüfen und jeglichen Code, der Push-Berechtigungen anfordern würde, manuell zu entfernen. Weitere Informationen finden Sie unter [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices).

Damit eine aktionsbasierte In-App-Nachrichten-Campaign zugestellt wird, müssen Sie angepasste Events über das Braze SDK protokollieren – nicht über REST APIs –, damit Nutzer:innen berechtigte In-App-Nachrichten direkt auf ihrem Gerät erhalten können. Nutzer:innen erhalten die In-App-Nachricht, wenn sie das Event während der Sitzung ausführen.