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

## 1. Schritt: Testnutzer:innen identifizieren {#step-1-identify-your-test-users}

Bevor Sie Ihre Messaging-Kampagne testen, ist es wichtig, Ihre Testnutzer:innen zu identifizieren. Diese Nutzer:innen können entweder vorhandene Nutzer-IDs oder E-Mail-Adressen sein, oder neue Nutzer:innen, die ausschließlich zum Testen von Messaging-Kampagnen verwendet werden.

### Optional: Content-Testgruppe erstellen {#optional-create-a-content-test-group}

Eine praktische Möglichkeit, Ihre Testnutzer:innen zu organisieren, ist die Erstellung einer [Content-Testgruppe]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/), die eine Gruppe von Nutzer:innen enthält, die Testnachrichten von Campaigns erhalten. Sie können diese Testgruppe zum Feld **Content-Testgruppen hinzufügen** unter **Testempfänger:innen** in Ihrer Campaign hinzufügen und Ihre Tests starten, ohne einzelne Testnutzer:innen erstellen oder hinzufügen zu müssen.

## 2. Schritt: Kanalspezifische Testnachrichten senden {#step-2-send-channel-specific-test-messages}

Informationen zum Senden von Testnachrichten finden Sie im folgenden Abschnitt für Ihren jeweiligen Kanal.

{% tabs local %}
{% tab Banner %}

{% alert important %}
Bevor Sie Banner-Nachrichten in Braze testen können, müssen Sie eine Banner-Campaign in Braze erstellen. Überprüfen Sie außerdem, ob die Platzierung, die Sie testen möchten, bereits [in Ihrer App oder Website platziert]({{site.baseurl}}/developer_guide/banners/placements/) ist.
{% endalert %}

Nachdem Sie Ihre Banner-Nachricht erstellt haben, können Sie Ihr Banner in der Vorschau anzeigen oder eine Testnachricht senden.

1. Entwerfen Sie Ihre Banner-Nachricht.
2. Wählen Sie **Vorschau**, um Ihr Banner in der Vorschau anzuzeigen oder eine Testnachricht zu senden.
3. Um eine Testnachricht zu senden, fügen Sie entweder eine Content-Testgruppe oder eine:n oder mehrere einzelne Nutzer:innen als **Testempfänger:innen** hinzu und wählen Sie dann **Test senden**.

Sie können Ihre Testnachricht bis zu 5 Minuten lang auf dem Gerät anzeigen.

![Vorschau-Tab des Banner-Composers.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Beachten Sie, dass Ihre Vorschau aufgrund von Unterschieden bei der Hardware möglicherweise nicht mit der endgültigen Darstellung auf dem Gerät der Nutzer:innen identisch ist.
{% endalert %}

### Test-Checkliste {#test-checklist}

- Ist Ihre Banner-Campaign einer Platzierung zugewiesen?
- Werden die Bilder und Medien wie erwartet auf Ihren Zielgerätetypen und Bildschirmgrößen angezeigt und verhalten sich wie erwartet?
- Leiten Ihre Links und Buttons die Nutzer:innen dorthin, wo sie hingelangen sollen?
- Funktioniert Liquid wie erwartet? Haben Sie einen Standardattributwert für den Fall berücksichtigt, dass Liquid keine Informationen zurückgibt?
- Ist Ihr Text klar, prägnant und korrekt?

{% endtab %}
{% tab Content Card %}

{% alert important %}
Um einen Test an [Content-Testgruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#content-test-groups) oder einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten aktiviert sein und gültige Push-Token für die Testnutzer:innen registriert sein, bevor Sie senden. Für iOS-Nutzer:innen müssen Sie auf die von Braze gesendete Push-Benachrichtigung tippen, um die Test-Content-Card anzuzeigen. Dieses Verhalten gilt nur für Test-Content-Cards.
{% endalert %}

Test-Content-Cards werden über eine Push-Benachrichtigung zugestellt. Die Card ist in der Push-Payload verpackt, und das SDK extrahiert und speichert sie lokal zwischen, wenn der Push empfangen wird.

Dieser Prozess umgeht das normale Card-Zustellungssystem, weshalb Push aktiviert sein muss, auch wenn Sie eine Content Card testen.

Test-Content-Cards laufen ungefähr fünf Minuten nach dem Senden ab.

Nachdem Sie Ihre Content Card erstellt haben, können Sie eine Test-Content-Card an Ihre App senden, um zu sehen, wie sie in Echtzeit aussieht.

1. Entwerfen Sie Ihre Content Card.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Testgruppe oder eine:n einzelne:n Nutzer:in aus, um diese Testnachricht zu erhalten.
3. Wählen Sie **Test senden**, um Ihre Content Card an Ihre App zu senden.

![Test-Content-Card]({% image_buster /assets/img/contentcard_test.png %})

### Vorschau {#preview}

Sie können Ihre Card während der Erstellung im Tab **Vorschau** in der Vorschau anzeigen. Dies sollte Ihnen helfen, sich vorzustellen, wie Ihre endgültige Nachricht aus der Perspektive Ihrer Nutzer:innen aussehen wird.

{% alert note %}
Im Tab **Vorschau** Ihres Composers stimmt die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät der Nutzer:innen überein. Wir empfehlen, immer eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und angepassten Attribute korrekt generiert werden.
{% endalert %}

### Test-Checkliste

- Haben Ihre Testnutzer:innen Push mit einem gültigen Push-Token aktiviert?
- Werden die Bilder und Medien wie erwartet angezeigt und verhalten sich wie erwartet?
- Funktioniert Liquid wie erwartet? Haben Sie einen [Standardattributwert]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#accounting-for-null-attribute-values) berücksichtigt, falls Liquid keine Informationen zurückgibt?
- Ist Ihr Text klar, prägnant und korrekt?
- Leiten Ihre Links die Nutzer:innen dorthin, wo sie hingelangen sollen?
- Haben Ihre Testnutzer:innen Push mit einem gültigen Push-Token aktiviert?

### Fehlerbehebung bei defekten Bildern {#troubleshooting-broken-images}

Wenn ein Content-Card-Bild nicht gerendert wird oder defekt erscheint:

- **Überprüfen Sie, ob die URL korrekt und URL-kodiert ist:** Sonderzeichen in der URL (wie Leerzeichen oder Abfrageparameter) müssen ordnungsgemäß kodiert sein. Andernfalls schlägt die Bildanfrage fehl.
- **Prüfen Sie Content-Security-Policies:** Wenn Ihre Organisation eine Content-Security-Policy (CSP) oder interne IT-Sicherheitsregeln hat, kann die Policy die Bild-Domain blockieren. Bestätigen Sie, dass die Domain der Bild-URL von Ihrer CSP zugelassen ist.
- **Verwenden Sie HTTPS:** Bild-URLs sollten `https://` anstelle von `http://` verwenden, um Mixed-Content-Blocking in Browsern und Apps zu vermeiden.
- **Öffnen Sie die URL direkt in einem Browser:** Wenn das Bild nicht in einem Browser geladen wird, liegt das Problem bei der Bild-URL oder dem Hosting – nicht bei Braze.

### Debugging {#debug}

Nachdem Ihre Content Cards gesendet wurden, können Sie Probleme über das [Event-Nutzerprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log/) in der Entwicklungskonsole aufschlüsseln oder debuggen.

Ein häufiger Anwendungsfall ist der Versuch zu debuggen, warum Nutzer:innen eine bestimmte Content Card nicht sehen können. Dazu können Sie in den **Event-Nutzerprotokollen** nach den Content Cards suchen, die beim Sitzungsstart an das SDK geliefert wurden, aber vor einer Impression, und diese zu einer bestimmten Campaign zurückverfolgen:

1. Gehen Sie zu **Einstellungen** > **Event-Nutzerprotokoll**.
2. Suchen und erweitern Sie die SDK-Anfrage für Ihre Testnutzer:innen.
3. Klicken Sie auf **Rohdaten**.
4. Suchen Sie die `id` für Ihre Sitzung. Das Folgende zeigt einen Beispielauszug:

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

Von dort aus können Sie Ihre Nachrichteneinstellungen und Inhalte überprüfen, um herauszufinden, warum Nutzer:innen eine bestimmte Content Card nicht sehen können.

{% endtab %}
{% tab E-Mail %}

1. Entwerfen Sie Ihre E-Mail-Nachricht.
2. Wählen Sie **Vorschau und Test**.
3. Wählen Sie den Tab **Testversand** und fügen Sie Ihre E-Mail-Adresse oder Nutzer-ID im Feld **Einzelne Nutzer:innen hinzufügen** hinzu.
4. Wählen Sie **Test senden**, um Ihre entworfene E-Mail an Ihren Posteingang zu senden.

![Test-E-Mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

Wenn Ihre E-Mail-Campaign ein großes Bild enthält und in Outlook nicht wie erwartet angezeigt wird, erwägen Sie, die tatsächlichen Dateiabmessungen des Bildes mit einem Bildbearbeitungs- oder Größenänderungstool zu reduzieren, anstatt es nur mit CSS oder HTML zu skalieren.

{% endtab %}
{% tab In-App-Nachricht %}

{% alert warning %}
Um einen Test an [Content-Testgruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#content-test-groups) oder einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten vor dem Senden aktiviert sein. Beispielsweise müssen Sie Push auf Ihrem iOS-Gerät aktiviert haben, um auf die Benachrichtigung zu tippen, bevor die Testnachricht angezeigt wird. {% endalert %}

Wenn Sie Push-Benachrichtigungen in Ihrer App und auf Ihrem Testgerät eingerichtet haben, können Sie Test-In-App-Nachrichten an Ihre App senden, um zu sehen, wie sie in Echtzeit aussehen.

1. Entwerfen Sie Ihre In-App-Nachricht.
2. Wählen Sie den Tab **Test** und fügen Sie Ihre E-Mail-Adresse oder Nutzer-ID im Feld **Einzelne Nutzer:innen hinzufügen** hinzu.
3. Wählen Sie **Test senden**, um Ihre Push-Nachricht an Ihr Gerät zu senden.

Eine Test-Push-Nachricht wird oben auf Ihrem Gerätebildschirm angezeigt.

![Test-In-App-Nachricht]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Testversendungen können dazu führen, dass mehr als eine In-App-Nachricht an jede:n Empfänger:in gesendet wird.
{% endalert %}

Wenn Sie direkt auf die Push-Nachricht klicken und sie öffnen, gelangen Sie zu Ihrer App, wo Sie Ihren In-App-Nachrichtentest anzeigen können. Beachten Sie, dass diese In-App-Nachrichtentest-Funktion darauf angewiesen ist, dass Nutzer:innen auf eine Test-Push-Benachrichtigung klicken, um die In-App-Nachricht auszulösen. Daher müssen die Nutzer:innen berechtigt sein, Push-Benachrichtigungen in der entsprechenden App zu empfangen, damit die Test-Push-Benachrichtigung erfolgreich zugestellt wird.

### Vorschau

Sie können Ihre In-App-Nachricht während der Erstellung im Tab **Vorschau** in der Vorschau anzeigen. Dies sollte Ihnen helfen, sich vorzustellen, wie Ihre endgültige Nachricht aus der Perspektive Ihrer Nutzer:innen aussehen wird. Sie können eine Vorschau anzeigen, wie Ihre Nachricht für zufällige Nutzer:innen, bestimmte Nutzer:innen oder angepasste Nutzer:innen aussehen wird. Sie können auch Nachrichten für Mobilgeräte oder Tablets in der Vorschau anzeigen.

![Tab „Verfassen“ beim Erstellen einer In-App-Nachricht mit der Vorschau, wie die Nachricht aussehen wird. Es sind keine Nutzer:innen ausgewählt, sodass das im Textbereich hinzugefügte Liquid unverändert angezeigt wird.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze bietet drei Generationen von In-App-Nachrichten an. Sie können genau festlegen, an welche Geräte Ihre Nachrichten gesendet werden sollen, basierend darauf, welche Generation sie unterstützen.

![Wechsel zwischen Generationen bei der Vorschau einer In-App-Nachricht.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
In der **Vorschau** stimmt die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät der Nutzer:innen überein. Wir empfehlen immer, eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und angepassten Attribute korrekt generiert werden.
{% endalert %}

### Test-Checkliste

- Werden die Bilder und Medien wie erwartet angezeigt und verhalten sich wie erwartet?
- Funktioniert Liquid wie erwartet? Haben Sie einen [Standardattributwert]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#accounting-for-null-attribute-values) berücksichtigt, falls Liquid keine Informationen zurückgibt?
- Ist Ihr Text klar, prägnant und korrekt?
- Leiten Ihre Buttons die Nutzer:innen dorthin, wo sie hingelangen sollen?

### Barrierefreiheits-Scanner {#accessibility-scanner}

Um Best Practices für Barrierefreiheit zu unterstützen, scannt Braze automatisch den Inhalt von In-App-Nachrichten, die mit dem traditionellen HTML-Editor erstellt wurden, auf Barrierefreiheitsstandards. Dieser Scanner hilft dabei, Inhalte zu identifizieren, die möglicherweise nicht den Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) entsprechen. WCAG ist ein Satz international anerkannter technischer Standards, die vom World Wide Web Consortium (W3C) entwickelt wurden, um Webinhalte für Menschen mit Behinderungen zugänglicher zu machen.

![Ergebnisse des Barrierefreiheits-Scans]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
Der Barrierefreiheits-Scanner für In-App-Nachrichten wird nur bei Nachrichten ausgeführt, die mit benutzerdefiniertem HTML erstellt wurden.
{% endalert %}

#### Funktionsweise {#how-it-works}

Der Scanner wird automatisch bei benutzerdefinierten HTML-Nachrichten ausgeführt und bewertet Ihre gesamte HTML-Nachricht anhand des vollständigen [WCAG 2.1 AA-Regelwerks](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Für jedes markierte Problem zeigt er:

- Das spezifische betroffene HTML-Element
- Eine Beschreibung des Barrierefreiheitsproblems
- Einen Link zu zusätzlichem Kontext oder Anleitungen zur Behebung

#### Automatisierte Barrierefreiheitstests verstehen {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Erstellen Sie Ihre LINE-Nachricht.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Testgruppe oder eine:n einzelne:n Nutzer:in aus, um diese Testnachricht zu erhalten.
3. Wählen Sie **Test senden**, um Ihre Nachricht zu senden.

![Test-LINE-Nachricht.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Mobiler Push {#mobile-push}

1. Entwerfen Sie Ihren mobilen Push.
2. Wählen Sie den Tab **Test** und fügen Sie Ihre E-Mail-Adresse oder Nutzer-ID im Feld **Einzelne Nutzer:innen hinzufügen** hinzu.
3. Wählen Sie **Test senden**, um Ihre entworfene Nachricht an Ihr Gerät zu senden.

![Test-Push]({% image_buster /assets/img_archive/testpush.png %})

Wenn Sie einen Fehler sehen, dass keine der ausgewählten Nutzer:innen übereinstimmende Push-Token haben, hat die Testnutzer:in kein gültiges Push-Token für die ausgewählte Plattform. Die Nutzer:innen müssen eine Sitzung in der App gestartet und Push für dieses Gerät aktiviert haben. Weitere Informationen finden Sie unter [Push-Aktivierung und Push-Abo-Status]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/).

#### Web-Push {#web-push}

1. Erstellen Sie Ihren Web-Push.
2. Wählen Sie den Tab **Test**.
3. Wählen Sie **Test an mich senden**.
4. Wählen Sie **Test senden**, um Ihren Web-Push an Ihren Webbrowser zu senden.

![Test-Web-Push]({% image_buster /assets/img_archive/testwebpush.png %})

Wenn Sie bereits Push-Nachrichten vom Braze-Dashboard akzeptiert haben, wird die Nachricht in der Ecke Ihres Bildschirms angezeigt. Andernfalls wählen Sie **Zulassen**, wenn Sie dazu aufgefordert werden, und die Nachricht wird angezeigt.

Wenn Sie einen Fehler sehen, dass keine der ausgewählten Nutzer:innen übereinstimmende Push-Token für Web-Push haben, überprüfen Sie, ob die Testnutzer:innen ein gültiges Push-Token für die ausgewählte Plattform registriert haben. Um ein Push-Token zu erhalten, müssen die Nutzer:innen so konfiguriert sein, dass sie Push-Benachrichtigungen für die App auf ihrem Gerät empfangen. Weitere Details finden Sie unter [Push-Aktivierung und Push-Abo-Status]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/).

{% endtab %}
{% tab SMS/MMS und RCS %}

Nachdem Sie Ihre SMS-, MMS- oder RCS-Nachricht erstellt haben, können Sie eine Testnachricht an Ihr Telefon senden, um zu sehen, wie sie in Echtzeit aussieht.

1. Entwerfen Sie Ihre SMS-, MMS- oder RCS-Nachricht.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Testgruppe oder eine:n einzelne:n Nutzer:in aus, um diese Testnachricht zu erhalten.
3. Wählen Sie **Test senden**, um Ihre Testnachricht zu senden.

![Test-SMS-Nachricht]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Nachdem Sie Ihren Webhook erstellt haben, können Sie einen Testversand durchführen, um die Webhook-Antwort zu überprüfen. Wählen Sie den Tab **Test** und wählen Sie **Test senden**, um einen Testversand an die angegebene Webhook-URL zu senden. Sie können auch eine:n einzelne:n Nutzer:in auswählen, um die Antwort als bestimmte:r Nutzer:in in der Vorschau anzuzeigen.

{% endtab %}
{% tab WhatsApp %}

1. Erstellen Sie Ihre WhatsApp-Nachricht.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Testgruppe oder eine:n einzelne:n Nutzer:in aus, um diese Testnachricht zu erhalten.
3. Initiieren Sie ein Konversationsfenster, indem Sie eine WhatsApp-Nachricht an die Telefonnummer senden, die mit der Abo-Gruppe verknüpft ist, die Sie für diese Nachricht verwenden. Die zugehörige Telefonnummer ist im Hinweis auf dem Tab **Test** aufgeführt.
4. Wählen Sie **Test senden**, um Ihre Nachricht zu senden.

![Test-WhatsApp-Nachricht.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Personalisierte Campaigns testen {#test-personalized-campaigns}

Wenn Sie Campaigns testen, die Nutzerdaten verwenden oder angepasste Event-Eigenschaften nutzen, müssen Sie zusätzliche oder andere Schritte unternehmen.

### Campaigns testen, die mit Nutzerattributen personalisiert sind {#testing-campaigns-personalized-with-user-attributes}

Wenn Sie [Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/overview/) in Ihrer Nachricht verwenden, müssen Sie zusätzliche Schritte unternehmen, um Ihre Campaign ordnungsgemäß in der Vorschau anzuzeigen und zu überprüfen, ob die Nutzerdaten den Inhalt korrekt befüllen.

Stellen Sie beim Senden einer Testnachricht sicher, dass Sie entweder die Option **Vorhandene:n Nutzer:in auswählen** wählen oder als **Angepasste:r Nutzer:in** in der Vorschau anzeigen.

![Testen einer personalisierten Nachricht]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Vorhandene:n Nutzer:in auswählen {#selecting-an-existing-user}

Wenn Sie eine:n vorhandene:n Nutzer:in auswählen, geben Sie die spezifische Nutzer-ID oder E-Mail in das Suchfeld ein. Verwenden Sie dann die Dashboard-Vorschau, um zu sehen, wie Ihre Nachricht für diese:n Nutzer:in aussehen würde, und senden Sie eine Testnachricht an Ihr Gerät, die widerspiegelt, was diese:r Nutzer:in sehen würde.

![Nutzer:in auswählen]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Angepasste:n Nutzer:in auswählen {#selecting-a-custom-user}

Wenn Sie als angepasste:r Nutzer:in in der Vorschau anzeigen, geben Sie Text für verschiedene verfügbare Felder zur Personalisierung ein, wie z. B. den Vornamen und angepasste Attribute. Sie können auch Ihre eigene E-Mail-Adresse eingeben, um einen Test an Ihr Gerät zu senden.

![Angepasste:r Nutzer:in]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Vorhandene:n Nutzer:in anpassen {#customizing-an-existing-user}

Sie können einzelne Felder von zufälligen oder vorhandenen Nutzer:innen bearbeiten, um dynamischen Content in Ihrer Nachricht zu testen. Wählen Sie **Bearbeiten**, um die ausgewählten Nutzer:innen in angepasste Nutzer:innen umzuwandeln, die Sie ändern können.

![Der Tab „Vorschau als Nutzer:in“ mit einem Button „Bearbeiten“.]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Campaigns testen, die mit angepassten Event-Eigenschaften personalisiert sind {#testing-campaigns-personalized-with-custom-event-properties}

Das Testen von Campaigns, die mit [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/) personalisiert sind, unterscheidet sich leicht vom Testen anderer Arten von Campaigns, die oben beschrieben wurden.

{% tabs local %}
{% tab Manuell triggern %}

#### Methode 1: Campaign manuell triggern {#method-1-triggering-campaign-manually}

Sie können die Campaign selbst triggern, um Campaigns, die angepasste Event-Eigenschaften verwenden, robust zu testen:

1. Verfassen Sie den Text mit der Event-Eigenschaft.

![Testnachricht mit Eigenschaften verfassen]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Verwenden Sie die [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/), um die Campaign zuzustellen, wenn das Event eintritt.

{% alert note %}
Wenn Sie eine iOS-Push-Campaign testen, müssen Sie die Verzögerung auf eine Minute einstellen, um sich Zeit zu geben, die App zu verlassen, da iOS keine Push-Benachrichtigungen für die aktuell geöffnete App zustellt. Andere Arten von Campaigns können auf sofortige Zustellung eingestellt werden.
{% endalert %}

![Testnachricht-Zustellung]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Richten Sie die Nutzer:innen wie beim Testen ein, indem Sie einen Testfilter verwenden oder Ihre eigene E-Mail-Adresse als Zielgruppe festlegen, und schließen Sie die Erstellung der Campaign ab.

![Testnachricht-Targeting]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Gehen Sie in Ihre App und führen Sie das angepasste Event aus.

Die Campaign wird getriggert und zeigt die mit der Event-Eigenschaft angepasste Nachricht an.

![Testnachricht-Beispiel]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Testnachricht %}

#### Methode 2: Sich selbst eine Testnachricht senden {#method-2-sending-yourself-a-test-message}

Alternativ können Sie, wenn Sie angepasste Nutzer-IDs speichern, die Campaign auch testen, indem Sie sich selbst eine angepasste Testnachricht senden.

1. Verfassen Sie den Text für Ihre Campaign.
2. Wählen Sie den Tab **Test** und wählen Sie **Angepasste:r Nutzer:in**.
3. Fügen Sie die angepasste Event-Eigenschaft am Ende der Seite hinzu und fügen Sie Ihre Nutzer-ID oder E-Mail-Adresse im oberen Feld hinzu.
4. Wählen Sie **Test senden**, um eine mit der Eigenschaft personalisierte Nachricht zu erhalten.

![Testen mit angepassten Nutzer:innen]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Methode 3: Liquid verwenden {#method-3-using-liquid}

Sie können angepasste Event-Eigenschaften testen, indem Sie Werte manuell mit Liquid eingeben.

1. Geben Sie im Nachrichteneditor Werte für Ihre angepassten Event-Eigenschaften ein.
2. Wählen Sie den Tab **Vorschau als Nutzer:in**, um zu überprüfen, ob die richtige Nachricht angezeigt wird.

{% endtab %}
{% endtabs %}

## Einschränkungen {#limitations}

Es gibt einige Situationen, in denen sich Testnachrichten nicht genauso verhalten wie Campaigns oder Canvases, die an echte Nutzer:innen gesendet werden. In diesen Fällen sollten Sie erwägen, die Campaign oder das Canvas an eine begrenzte Gruppe von Testnutzer:innen zu starten, um dieses Verhalten zu validieren.

- Das Anzeigen des Braze-Präferenzzentrums über Testnachrichten führt dazu, dass der Button **Einstellungen speichern** ausgegraut ist.
- Zum Testen von In-App-Nachrichten und Content Cards müssen die Zielnutzer:innen ein Push-Token für das Zielgerät haben.
- Zum Testen von Abmeldelinks in E-Mails stellen Sie sicher, dass die E-Mail-Adresse Ihrer Testnutzer:innen im jeweiligen Workspace vorhanden ist.
- Der `List-Unsubscribe`-Header ist nicht in E-Mails enthalten, die über die Testnachrichtenfunktion gesendet werden.

## Fehlerbehebung {#troubleshooting}

### In-App-Nachrichten {#in-app-messages}

Wenn Ihre In-App-Nachricht-Campaign nicht durch eine Push-Campaign getriggert wird, überprüfen Sie die Segmentierung der In-App-Campaign, um sicherzustellen, dass die Nutzer:innen die Zielgruppe erfüllen, **bevor** sie die Push-Nachricht erhalten.

Bei Testversendungen auf Android und iOS werden In-App-Nachrichten, die das On-Click-Verhalten **Push-Berechtigung anfordern** verwenden, möglicherweise auf einigen Geräten nicht angezeigt. Als Workaround:
- **Android:** Geräte müssen Android 13 und unser Android SDK Version 21.0.0 verwenden. Ein weiterer Grund kann sein, dass das Gerät, auf dem die In-App-Nachricht angezeigt wird, bereits eine Systemaufforderung hat. Möglicherweise haben Sie **Nicht erneut fragen** ausgewählt, sodass Sie die App möglicherweise neu installieren müssen, um die Benachrichtigungsberechtigungen zurückzusetzen, bevor Sie erneut testen.
- **iOS:** Wir empfehlen, dass Ihr Entwicklerteam die Implementierung von Push-Benachrichtigungen für Ihre App überprüft und jeglichen Code manuell entfernt, der Push-Berechtigungen anfordern würde. Weitere Informationen finden Sie unter [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/).

Damit eine aktionsbasierte In-App-Nachricht-Campaign zugestellt wird, müssen Sie angepasste Events über das Braze SDK protokollieren, nicht über REST APIs, damit Nutzer:innen berechtigte In-App-Nachrichten direkt auf ihrem Gerät empfangen können. Nutzer:innen erhalten die In-App-Nachricht, wenn sie das Event während der Sitzung ausführen.