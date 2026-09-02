---
nav_title: "Nutzer:innen-Retargeting"
article_title: "Nutzer:innen-Retargeting"
description: "Dieser Referenzartikel beschreibt, wie Nutzer:innen ihre Nachrichten anhand der Kurzmitteilungsdienst or SMS- und RCS-Interaktionen von Nutzer:innen retargeten können."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# Nutzer:innen-Retargeting {#user-retargeting}

> Zusätzlich zur Änderung des Abo-Status von Nutzer:innen und dem Senden automatischer Antworten basierend auf eingehenden Schlüsselwörtern zeichnet Braze auch Interaktionen im Kundenprofil or Nutzerprofil auf, um Nachrichten zu filtern und zu Trigger or triggern or triggern.<br><br>Diese Filter und Trigger or triggern ermöglichen es Ihnen, Aktionen basierend auf Nutzer:innen zu filtern, die Kurzmitteilungsdienst or SMS-, MMS- und RCS-Kampagnen erhalten haben oder darauf geantwortet haben, oder Nutzer:innen weiter anzusprechen, die auf gekürzte URLs geklickt haben.

{% alert tip %}
Um mehr über angepasste Schlüsselwörter zu erfahren und wie Sie Zwei-Wege-Messaging einrichten, um diese Retargeting-Optionen zu nutzen, besuchen Sie unseren Artikel zu [angepassten Schlüsselwörtern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling).
{% endalert %}

## Retargeting-Optionen {#retargeting-options}

{% alert note %}
Beim Aufbau von Zielgruppen mit Nutzer:innen-Retargeting möchten Sie möglicherweise bestimmte Nutzer:innen basierend auf ihren Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, wie z. B. das Recht auf „Nicht verkaufen oder teilen“ gemäß dem CUP. Marketer sollten die relevanten Filter für die Berechtigung von Nutzer:innen in ihren Canvas- und/oder Campaign-Eintrittskriterien implementieren.
{% endalert %}

### Nutzer:innen nach Kurzmitteilungsdienst or SMS, MMS und RCS filtern {#filter-users-by-sms-mms-and-rcs}

Nutzer:innen können danach gefiltert werden, wann sie zuletzt eine Kurzmitteilungsdienst or SMS, MMS oder RCS erhalten haben oder ob sie eine Kurzmitteilungsdienst or SMS, MMS oder RCS von einer bestimmten Campaign erhalten haben. Filter können im Schritt **Zielgruppe** des Campaign-Builders eingestellt werden.

{% alert note %}
Wenn eine Nachricht empfangen, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die dieselbe Telefonnummer wie das Profil teilen, das die Interaktion protokolliert hat. Nutzer:innen, die eine Telefonnummer mit jemandem teilen, der die Nachricht empfangen, geöffnet oder angeklickt hat, können diesem Filter entsprechen, auch wenn sie ursprünglich nicht in der Campaign waren oder die Nachricht nicht direkt erhalten haben.
{% endalert %}

#### Nach zuletzt erhaltener Kurzmitteilungsdienst or SMS/MMS/RCS filtern {#filter-by-last-received-smsmmsrcs}

![Segmentierungsfilter „Zuletzt SMS erhalten“ nach dem 8. Dezember 2020.]({% image_buster /assets/img/sms/filter2.png %})

#### Nach erhaltenen Nachrichten aus einer Kurzmitteilungsdienst or SMS/MMS/RCS-Campaign filtern {#filter-by-received-messages-from-smsmmsrcs-campaign}

Filtert Nutzer:innen, die eine Nachricht von einer bestimmten Campaign erhalten haben. Mit diesem Filter haben Sie auch die Möglichkeit, diejenigen herauszufiltern, die keine Nachrichten von einer Campaign erhalten haben.

![Segmentierungsfilter „Hat Nachricht erhalten von Campaign „SMS retargeting“".]({% image_buster /assets/img/sms/filter1.png %})

### Nachrichten Trigger or triggern or triggern, wenn Nutzer:innen Kurzmitteilungsdienst or SMS, MMS oder RCS erhalten {#trigger-messages}

Um Nachrichten zu Trigger or triggern or triggern, wenn Nutzer:innen Kurzmitteilungsdienst or SMS-, MMS- oder RCS-Nachrichten von einer bestimmten Campaign erhalten, wählen Sie **Interact with Campaign** als Trigger or triggern-Aktion für eine aktionsbasierte Campaign. Wählen Sie dann **Receive Kurzmitteilungsdienst or SMS** und die Kurzmitteilungsdienst or SMS-, MMS- oder RCS-Campaign, die Sie verwenden möchten.

![Um Nachrichten zu triggern, wenn Nutzer:innen SMS-, MMS- oder RCS-Nachrichten von einer bestimmten Campaign erhalten, wählen Sie „Interact with Campaign“ als Trigger-Aktion für eine aktionsbasierte Campaign. Wählen Sie dann „Receive SMS“ und die SMS-, MMS- oder RCS-Campaign, die Sie verwenden möchten.]({% image_buster /assets/img/sms/trigger.png %})

### Nach erweiterten Tracking-Links filtern {#filter-by-advanced-tracking-links}

Retargeten Sie Nutzer:innen, die auf Kampagnen mit [erweiterten Tracking-Links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) geklickt haben.
Nur Kampagnen mit aktiviertem erweitertem Tracking erscheinen in den folgenden Dropdowns:

#### Nutzer:innen retargeten, die auf eine bestimmte Kurzmitteilungsdienst or SMS-, MMS- oder RCS-Campaign geklickt haben {#retarget-users-who-have-clicked-a-specific-sms-mms-or-rcs-campaign}

1. Erstellen Sie ein Segment mit dem Filter **Clicked/Opened Campaign**.
2. Wählen Sie **clicked shortened Kurzmitteilungsdienst or SMS link**.
3. Wählen Sie die gewünschte Campaign.

![Screenshot zum Retargeting von Nutzer:innen, die auf eine bestimmte SMS-, MMS- oder RCS-Campaign geklickt haben.]({% image_buster /assets/img/sms/retargeting5.png %})

#### Nutzer:innen retargeten, die auf einen bestimmten Canvas-Schritt geklickt haben {#retarget-users-who-have-clicked-a-specific-canvas-step}

1. Erstellen Sie ein Segment mit dem Filter **Clicked/Opened Step**.
2. Wählen Sie **clicked shortened Kurzmitteilungsdienst or SMS link**.
3. Wählen Sie den gewünschten Canvas und Canvas-Schritt.

![Screenshot zum Retargeting von Nutzer:innen, die auf einen bestimmten Canvas-Schritt geklickt haben.]({% image_buster /assets/img/keyword_example1.jpg %})

## Schlüsselwortkategorie-spezifisches Retargeting {#keyword-category-specific-retargeting}

Zusätzlich zu den drei Standard-Schlüsselwortkategorien (Opt-in, Opt-out und Hilfe) können Sie auch bis zu 25 eigene Schlüsselwortkategorien erstellen, mit denen Sie beliebige Schlüsselwörter und Antworten identifizieren können. Diese Kategorien können zum Filtern und Retargeting verwendet werden. Um mehr über globale Schlüsselwortkategorien und deren Einrichtung zu erfahren, lesen Sie [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

### Nach Aktualität filtern {#filter-by-recency}

Filtern Sie nach der Aktualität der Antwort von Nutzer:innen auf Ihr Kurzmitteilungsdienst or SMS-, MMS- oder RCS-Programm. Dieser Filter wertet das letzte Datum aus, an dem Nutzer:innen eine eingehende Nachricht gesendet haben, die in eine der Schlüsselwortkategorien fällt.

![Segmentierungsfilter „Zuletzt SMS gesendet an Abo-Gruppe „Marketing SMS“ mit Schlüsselwort „Opt-in“ nach dem 11. August 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Nach Campaign- oder Canvas-Attribution filtern {#filter-by-campaign-or-canvas-attribution}

Filtern Sie nach Nutzer:innen, die auf eine bestimmte Kurzmitteilungsdienst or SMS-, MMS- oder RCS-Campaign oder Canvas-Komponente, Schlüsselwortkategorie oder einen Tag geantwortet haben.

#### Nach Antwort auf eine bestimmte Campaign mit Schlüsselwortkategorie filtern {#filter-by-replied-to-a-specific-campaign-with-keyword-category}

![Campaign mit dem Filter „Hat auf SMS geantwortet“ für Campaign „SMS-283“ „Aktion“. Unter dem Filter wird erwähnt: „Dieser Filter läuft 25 Monate nach dem Senden der letzten Nachricht von „Aktion“ ab, wenn er in keiner aktiven Campaign verwendet wird."]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

#### Nach Antwort auf eine Campaign oder Canvas mit einem bestimmten Tag filtern {#filter-by-replied-to-a-campaign-or-canvas-with-a-specific-tag}

![Campaign mit dem Filter „Hat auf SMS geantwortet“ für Campaign oder Canvas mit Tag „Curbside Messaging Service C“.]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

#### Nach Antwort auf einen bestimmten Schritt filtern {#filter-by-replied-to-a-specific-step}

![Campaign mit dem Filter „Hat auf SMS geantwortet“ für Schritt „SMS Double Opt“ „Step - Help“.]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Nachrichten nach Schlüsselwort Trigger or triggern or triggern {#trigger-messages-by-keyword}

Nachrichten können getriggert werden, wenn Nutzer:innen eingehende Nachrichten basierend auf Schlüsselwortkategorien senden (Nutzer:in hat eines der Schlüsselwörter gesendet) oder auf andere Schlüsselwörter (Nutzer:in hat ein Schlüsselwort gesendet, das nicht in eine der bestehenden Kategorien fällt). Diese Trigger or triggern werden im Zustellungsschritt des Campaign-Builders eingestellt.

Bei der Auswertung, ob eine eingehende Nachricht einem definierten Trigger or triggern-Ereignis entspricht, werden führende und nachfolgende Leerzeichen vor der Auswertung entfernt.

{% alert tip %}
Wenn ein aktionsbasierter Canvas durch eine eingehende Kurzmitteilungsdienst or SMS- oder MMS-Nachricht getriggert wird, können Sie [unterstützte Kurzmitteilungsdienst or SMS-Liquid-Eigenschaften]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) in jedem Canvas-Schritt bis zum nächsten Aktions-Pfad referenzieren.
{% endalert %}

#### Nach eingehender Schlüsselwortkategorie Trigger or triggern or triggern {#trigger-by-inbound-keyword-category}

![Aktionsbasierte SMS-Campaign mit dem Segmentierungsfilter „Schlüsselwort „Opt-in“ an Abo-Gruppe „Marketing SMS“ gesendet".]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

#### Nach beliebigen Schlüsselwörtern Trigger or triggern or triggern {#trigger-by-arbitrary-keywords}

Beachten Sie, dass Sie beim Trigger or triggern or triggern einer Nachricht auf eine „Andere“-Schlüsselwortantwort die Möglichkeit haben, den Schlüsselworttext auf eine exakte Textübereinstimmung zu prüfen. Diese Übereinstimmung folgt denselben Regeln wie beschrieben: Nur die **exakte Einzelwort-Nachricht** wird verarbeitet (Groß-/Kleinschreibung wird _nicht_ berücksichtigt). Ein gesendetes Schlüsselwort `Hello Braze!` würde nicht den im folgenden Beispiel gezeigten Kriterien entsprechen.

![Aktionsbasierte SMS-Campaign mit Schlüsselwortkategorie „Andere“, bei der der Nachrichtentext genau „Hello“ oder „Hey“ ist.]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

#### Schlüsselwörter als Template verwenden {#template-keywords}

Beim Trigger or triggern or triggern einer Campaign oder Canvas-Komponente durch eine eingehende Kurzmitteilungsdienst or SMS oder MMS können Sie optional den Text oder die Medienanhänge, die Nutzer:innen gesendet haben, mit Liquid in den Text Ihrer Campaign oder Ihres Canvas einbinden. Dies ermöglicht Ihnen den Zugriff auf die Antwort der Nutzer:innen, die Sie dann in Ihre Antwort einbeziehen, bedingte Logik anwenden oder alles andere tun können, was mit Liquid möglich ist.

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}