---
nav_title: Benutzerdefinierte Keyword-Verarbeitung
article_title: Benutzerdefinierte Keyword-Verarbeitung
page_order: 2
description: "Dieser Referenzartikel behandelt, wie Braze mit bidirektionalem SMS-, MMS- und RCS-Messaging und automatischen Antworten umgeht. Er enthält Erklärungen zur Funktionsweise von Keyword-Triggern sowie zu benutzerdefinierten Keyword-Kategorien und der Unterstützung mehrerer Sprachen."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Benutzerdefinierte Keyword-Verarbeitung {#custom-keyword-handling}

> Dieser Referenzartikel behandelt, wie Braze mit bidirektionalem SMS-, MMS- und RCS-Messaging und automatischen Antworten umgeht. Er enthält Erklärungen zur Funktionsweise von Keyword-Triggern sowie zu benutzerdefinierten Keyword-Kategorien und der Unterstützung mehrerer Sprachen.

## Bidirektionales Messaging (benutzerdefinierte Keyword-Antworten) {#two-way-messaging-custom-keyword-responses}

Bidirektionales Messaging ermöglicht es Ihnen, Nachrichten zu senden und die Antworten auf diese Nachrichten zu verarbeiten. Endnutzer:innen müssen ein Keyword an Braze senden, woraufhin sie eine automatische Antwort erhalten. Richtig eingesetzt kann bidirektionales Messaging eine einfache, sofortige und dynamische Lösung für Kundenmarketing sein, die Zeit und Ressourcen spart.

## Keywords und automatische Antworten verwalten {#managing-keywords-and-auto-responses}

SMS, MMS und RCS mit Braze bieten Ihnen die Möglichkeit, Keyword-Trigger zu erstellen, benutzerdefinierte Antworten zu definieren, Keyword-Sets für mehrere Sprachen festzulegen und benutzerdefinierte Keyword-Kategorien einzurichten.

{% alert note %}
Braze verwendet Ihren vollständigen Satz an Opt-out-Keywords ([Standard-Keywords]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/) und [benutzerdefinierte Keywords]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/)) für die exakte Opt-out-Verarbeitung und [Fuzzy-Opt-out]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/).
{% endalert %}

{% tabs %}
{% tab Keyword-Trigger hinzufügen %}

#### Keyword-Trigger hinzufügen {#add-keyword-triggers}

Zusätzlich zu den Standard-Keywords für Opt-in und Opt-out können Sie auch eigene Keywords definieren, die Opt-in-, Opt-out- und Hilfe-Antworten triggern.

Um eigene Keywords zu definieren, gehen Sie wie folgt vor:

1. Gehen Sie im Braze-Dashboard zu **Audience** > **Subscription Group Management** und wählen Sie eine **SMS/MMS/RCS**-Abo-Gruppe aus.<br><br>
2. Wählen Sie unter **Global Keywords** das Stiftsymbol neben der Keyword-Kategorie aus, zu der Sie ein Keyword hinzufügen möchten. ![Opt-in-Keywords mit angezeigtem Stiftsymbol.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. Fügen Sie im sich öffnenden Tab ein Keyword hinzu, das diese Keyword-Kategorie triggern soll. Beachten Sie, dass Keywords nicht zwischen Groß- und Kleinschreibung unterscheiden und universelle Keywords wie `START`, `YES` und `UNSTOP` nicht geändert werden können. ![Bearbeitung der Keywords für die Kategorie „Opt-In“. Hinzugefügte Keywords sind „START“, „UNSTOP“ und „YES“. Das Antwort-Nachrichtenfeld lautet: „You have been unsubscribed to messages from this number. Reply HELP for help. Reply STOP to unsubscribe. Message and data rates may apply.“]({% image_buster /assets/img/sms/keyword_edit2.png %})

Die folgenden Regeln gelten für Keywords und Keyword-Antworten:

| Keywords | Keyword-Antworten |
| -------- | ----------------- |
| - Gültige UTF-8-kodierte Zeichen<br>- Maximal 20 Keywords pro Kategorie insgesamt<br>- Maximale Länge von 34 Zeichen<br>- Minimale Länge von 1 Zeichen<br>- Dürfen keine Leerzeichen enthalten<br>- Müssen innerhalb der Abo-Gruppe groß-/kleinschreibungsunabhängig und eindeutig sein | - Dürfen nicht leer sein<br>- Maximale Länge von 300 Zeichen<br>- Gültige UTF-8-Zeichen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Keyword-Trigger hinzufügen" }

{% alert tip %}
Möchten Sie erfahren, wie diese Keywords in Ihren Campaigns und Canvases zum Retargeting und Triggern von Nachrichten verwendet werden können? Besuchen Sie [Nutzer:innen-Retargeting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) für weitere Informationen.
{% endalert %}
{% endtab %}

{% tab Antworten verwalten %}

#### Antworten verwalten {#manage-responses}

Sie können eigene Antworten verwalten, die an Nutzer:innen gesendet werden, nachdem diese ein Keyword an eine bestimmte Keyword-Kategorie gesendet haben.

1. Gehen Sie im Braze-Dashboard zu **Audience** > **Subscription Group Management** und wählen Sie eine **SMS/MMS/RCS**-Abo-Gruppe aus. <br><br>
2. Wählen Sie unter **Global Keywords** eine Keyword-Kategorie aus, für die Sie eine Antwort bearbeiten möchten, indem Sie das Stiftsymbol auswählen. ![Opt-in-Keywords mit angezeigtem Stiftsymbol.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. Bearbeiten Sie im sich öffnenden Tab Ihre Antwort. Beachten Sie unsere [sechs Regeln für korrekte Compliance]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/#the-six-rules-to-get-compliance-right) bei der Erstellung Ihrer Antwort und lesen Sie die folgenden Regeln, die für Keywords und Keyword-Antworten gelten. ![Antworten]({% image_buster /assets/img/sms/keyword_home.png %}){: style="max-width:70%;"}<br><br>
4. Um statische URLs in Ihrer Antwort automatisch zu kürzen, aktivieren Sie den **Link Shortening**-Toggle. Der Zeichenzähler wird aktualisiert und zeigt die erwartete Länge der gekürzten URL an. ![Ein GIF, das zeigt, wie der Zeichenzähler aktualisiert wird, wenn der „Link Shortening“-Toggle aktiviert ist.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

##### Hinweise {#considerations}

| Keywords | Keyword-Antworten |
| -------- | ----------------- |
| - Gültige UTF-8-kodierte Zeichen<br>- Maximal 20 Keywords pro Kategorie insgesamt<br>- Maximale Länge von 34 Zeichen<br>- Minimale Länge von 1 Zeichen<br>- Dürfen keine Leerzeichen enthalten<br>- Müssen innerhalb der Abo-Gruppe groß-/kleinschreibungsunabhängig und eindeutig sein | - Dürfen nicht leer sein<br>- Maximale Länge von 300 Zeichen<br>- Gültige UTF-8-Zeichen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Hinweise" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn ein aktionsbasierter Canvas durch eine eingehende SMS-, MMS- oder RCS-Nachricht getriggert wird, können Sie SMS-, MMS- oder RCS-Eigenschaften im ersten [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) des Canvas referenzieren.
{% endalert %}

## Unterstützung mehrerer Sprachen {#multi-language-support}

Beim Senden in bestimmte Länder kann es erforderlich sein, dass ein Sender eingehende Keywords und ausgehende Antworten in einer lokalen Sprache unterstützt. Um dies zu ermöglichen, erlaubt Braze Ihnen, sprachspezifische Keyword-Einstellungen zu erstellen. Einmal erstellt, gelten sprachspezifische Keyword-Einstellungen für alle Sendenummern innerhalb der Abo-Gruppe.
![Dropdown mit Sprachen, die als Keyword-Einstellung hinzugefügt werden können.]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### Sprachspezifische Keywords erstellen {#creating-language-specific-keywords}

Wählen Sie **Add a Language** und wählen Sie Ihre Zielsprache aus oder suchen Sie im Dropdown nach einer Sprache.

{% alert important %}
Nicht-englische Sprachen werden nicht mit voreingestellten Keywords und Antworten geliefert, sodass Sender mit ihren Marketing- und Rechtsteams zusammenarbeiten müssen, um alle erforderlichen Keywords zu diesem Set hinzuzufügen. Andernfalls verarbeitet Braze keine lokalisierten eingehenden Nachrichten für diese Sprachen.
{% endalert %}

Wenn Sie eine Sprache löschen müssen, wählen Sie den Button **Delete Language** unten rechts.

![Seite „Global Keywords“ mit ausgewähltem Tab „Italian“. Für jede hinzugefügte Sprache existieren zusätzliche Tabs.]({% image_buster /assets/img/sms/multi-language2.png %})

## Benutzerdefinierte Keyword-Kategorien {#custom-keyword-categories}

Zusätzlich zu den drei Standard-Keyword-Kategorien (Opt-in, Opt-out und Hilfe) können Sie auch bis zu 25 eigene Keyword-Kategorien erstellen. So können Sie beliebige Keywords identifizieren und geschäftsspezifische Antworten einrichten. Eine Beispielkategorie könnte „PROMO“ oder „RABATT“ sein, die eine Antwort über aktuelle Aktionen in diesem Monat auslösen könnte.

Diese benutzerdefinierten Keywords funktionieren im „Always-on“-Modus, was bedeutet, dass jede:r Nutzer:in, der/die Ihren Nachrichtendienst abonniert hat, jederzeit Keywords senden und eine Antwort erhalten kann. Zusätzlich zu diesem Verhalten haben Sie auch die Möglichkeit, bestimmte Keywords zu definieren, die nur zu [bestimmten Zeitpunkten](#lifecycle-specific-keywords) im Lebenszyklus Ihrer Nutzer:innen gesendet werden können.

![Keywords für eine „Promo“-Kategorie. Wenn Nutzer:innen „YO“ senden, erhalten sie die Nachricht mit einem Promo-Code.]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### Eine benutzerdefinierte Kategorie erstellen {#creating-a-custom-category}

Um eine benutzerdefinierte Keyword-Kategorie zu erstellen, gehen Sie wie folgt vor:

1. Bearbeiten Sie die entsprechende Abo-Gruppe.
2. Wählen Sie **Add custom keyword**. ![Felder zum Hinzufügen neuer Keywords.]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. Geben Sie einen Namen für die Keyword-Kategorie an und definieren Sie, welche Keywords Nutzer:innen senden können, um die Antwortnachricht zu erhalten.

Nachdem diese Keyword-Kategorie erstellt wurde, steht sie zum [Filtern und Triggern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) in Ihren Campaigns und Canvases zur Verfügung.

Keywords, die in benutzerdefinierten Keyword-Kategorien erstellt werden, unterliegen allen Regeln und Validierungen für die Erstellung neuer Keywords.

### Lebenszyklus-spezifische Keywords {#lifecycle-specific-keywords}

Wenn Sie einen Anwendungsfall haben, bei dem Sie einschränken möchten, wann Kund:innen während ihres Lebenszyklus ein bestimmtes Keyword senden können (z. B. während des ersten Onboardings), um eine Antwort zu erhalten, können Sie den Trigger **Sent inbound SMS to subscription group within keyword category OTHER** in Ihrer Campaign oder Ihrem Canvas verwenden und Keywords definieren, die Ihre Nutzer:innen zu einem bestimmten Zeitpunkt senden können.

Dieser Trigger unterstützt das Filtern nach der spezifischen eingehenden Nachricht mithilfe von „ist“- oder „ist nicht“-Vergleichen der Nachricht sowie „stimmt überein“- oder „stimmt nicht überein“-Regex-Regeln zur Validierung der Eingabe der Nutzer:innen.

#### Canvas

![Aktionsbasierter Canvas-Schritt mit dem Trigger „Send inbound SMS to subscription group „Messaging Service“ within keyword category „Other“", wobei der Nachrichtentext dem regulären Ausdruck „caret symbol skip“ entspricht.]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Campaign

![Aktionsbasierte Campaign mit dem Trigger „Send inbound SMS to subscription group „Marketing Message Service A“ within keyword category „Other“", wobei der Nachrichtentext „Keyword1“ oder „Keyword2“ ist oder nicht „Keyword A“ ist.]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### Umgang mit unbekannten Keywords {#dealing-with-unknown-keywords}

Wir empfehlen dringend, eine automatische Antwort einzurichten, wenn abonnierte Nutzer:innen etwas senden, das keinem Ihrer definierten Keywords entspricht (verarbeitet unter der Keyword-Kategorie **OTHER**).

Um eine Standardantwort zu senden – zum Beispiel „Sorry! Wir konnten dieses Keyword nicht erkennen.“ – gehen Sie wie folgt vor:

1. Erstellen Sie eine [SMS-Campaign]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/).
2. Wählen Sie für **Target audience** die Option **All users** (der Trigger schränkt weiterhin ein, wer die Nachricht erhält).
3. Wählen Sie für **Schedule** die Option **Action-based delivery**.
4. Setzen Sie den Trigger auf **Send inbound SMS** an die entsprechende Abo-Gruppe **within keyword category OTHER**.
5. Geben Sie im **Messaging**-Schritt den Antworttext ein, den Nutzer:innen erhalten sollen.

Informationen dazu, wie Braze eingehende Nachrichten von **unbekannten** Telefonnummern verarbeitet (bevor ein Profil existiert), finden Sie unter [Unbekannte Telefonnummern verarbeiten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/unknown_phone_numbers/).

{% alert tip %}
Möchten Sie erfahren, wie diese Keywords und Keyword-Kategorien in Ihren Campaigns und Canvases zum Retargeting und Triggern von Nachrichten verwendet werden können? Besuchen Sie [Nutzer:innen-Retargeting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) für weitere Informationen.
{% endalert %}