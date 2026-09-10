---
nav_title: "Nutzer:innen-Retargeting"
article_title: "Nutzer:innen-Retargeting"
description: "Dieser Referenzartikel beschreibt, wie Nutzer:innen ihre Nachrichten anhand der SMS- und RCS-Interaktionen von Nutzer:innen retargeten können."
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

> Zusätzlich zur Änderung des Abo-Status von Nutzer:innen und dem Senden automatischer Antworten basierend auf eingehenden Schlüsselwörtern zeichnet Braze auch Interaktionen im Kundenprofil auf, um Nachrichten zu filtern und zu triggern.<br><br>Diese Filter und Trigger ermöglichen es Ihnen, Aktionen basierend auf Nutzer:innen zu filtern, die SMS-, MMS- und RCS-Campaigns erhalten haben oder darauf geantwortet haben, oder Nutzer:innen weiter anzusprechen, die auf gekürzte URLs geklickt haben.

{% alert tip %}
Um mehr über angepasste Schlüsselwörter zu erfahren und wie Sie Zwei-Wege-Messaging einrichten, um diese Retargeting-Optionen zu nutzen, besuchen Sie unseren Artikel zu [angepassten Schlüsselwörtern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling).
{% endalert %}

## Retargeting-Optionen {#retargeting-options}

{% alert note %}
Beim Aufbau von Zielgruppen mit Nutzer:innen-Retargeting möchten Sie möglicherweise bestimmte Nutzer:innen basierend auf ihren Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, wie z. B. das „Do Not Sell or Share“-Recht gemäß dem CUP. Marketer sollten die relevanten Filter für die Berechtigung von Nutzer:innen in ihren Canvas- und/oder Campaign-Eintrittskriterien implementieren.
{% endalert %}

### Nutzer:innen nach SMS, MMS und RCS filtern {#filter-users-by-sms-mms-and-rcs}

Nutzer:innen können danach gefiltert werden, wann sie zuletzt eine SMS, MMS oder RCS erhalten haben oder ob sie eine SMS, MMS oder RCS aus einer bestimmten Campaign erhalten haben. Filter können im Schritt **Zielgruppe zusammenstellen** des Campaign-Builders festgelegt werden.

{% alert note %}
Wenn eine Nachricht empfangen, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die dieselbe Telefonnummer wie das Profil mit der protokollierten Interaktion haben. Nutzer:innen, die eine Telefonnummer mit einer Person teilen, die die Nachricht empfangen, geöffnet oder angeklickt hat, können diesem Filter entsprechen, auch wenn sie ursprünglich nicht Teil der Campaign waren oder die Nachricht nicht direkt erhalten haben.
{% endalert %}

#### Nach zuletzt erhaltener SMS/MMS/RCS filtern {#filter-by-last-received-smsmmsrcs}

![Segmentierungsfilter „Letzte erhaltene SMS nach dem 8. Dezember 2020“.]({% image_buster /assets/img/sms/filter2.png %})

#### Nach empfangenen Nachrichten aus einer SMS/MMS/RCS-Campaign filtern {#filter-by-received-messages-from-smsmmsrcs-campaign}

Filtert Nutzer:innen, die eine Nachricht aus einer bestimmten Campaign erhalten haben. Mit diesem Filter haben Sie auch die Möglichkeit, diejenigen herauszufiltern, die keine Nachrichten aus einer Campaign erhalten haben.

![Segmentierungsfilter „Hat Nachricht aus Campaign „SMS retargeting“ erhalten".]({% image_buster /assets/img/sms/filter1.png %})

### Nachrichten triggern, wenn Nutzer:innen SMS, MMS oder RCS erhalten {#trigger-messages}

Um Nachrichten zu triggern, wenn Nutzer:innen SMS-, MMS- oder RCS-Nachrichten aus einer bestimmten Campaign erhalten, wählen Sie **Interact with Campaign** als Aktion triggern für eine aktionsbasierte Campaign aus. Wählen Sie dann **Receive SMS** und die gewünschte Campaign aus.

![Um Nachrichten zu triggern, wenn Nutzer:innen SMS-, MMS- oder RCS-Nachrichten aus einer bestimmten Campaign erhalten, wählen Sie „Interact with Campaign“ als Aktion triggern für eine aktionsbasierte Campaign. Wählen Sie dann „Receive SMS“ und die gewünschte SMS-, MMS- oder RCS-Campaign aus.]({% image_buster /assets/img/sms/trigger.png %})

### Nach erweiterten Tracking-Links filtern {#filter-by-advanced-tracking-links}

Retargeten Sie Nutzer:innen, die auf Campaigns mit [erweiterten Tracking-Links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) geklickt haben.
Nur Campaigns, bei denen erweitertes Tracking aktiviert ist, erscheinen in den folgenden Dropdown-Menüs:

#### Nutzer:innen retargeten, die auf eine bestimmte SMS-, MMS- oder RCS-Campaign geklickt haben {#retarget-users-who-have-clicked-a-specific-sms-mms-or-rcs-campaign}

1. Erstellen Sie ein Segment mit dem Filter **Clicked/Opened Campaign**.
2. Wählen Sie **clicked shortened sms link** aus.
3. Wählen Sie die gewünschte Campaign aus.

![Screenshot zum Retargeting von Nutzer:innen, die auf eine bestimmte SMS-, MMS- oder RCS-Campaign geklickt haben.]({% image_buster /assets/img/sms/retargeting5.png %})

#### Nutzer:innen retargeten, die auf einen bestimmten Canvas-Schritt geklickt haben {#retarget-users-who-have-clicked-a-specific-canvas-step}

1. Erstellen Sie ein Segment mit dem Filter **Clicked/Opened Step**.
2. Wählen Sie **clicked shortened sms link** aus.
3. Wählen Sie den gewünschten Canvas und Canvas-Schritt aus.

![Screenshot zum Retargeting von Nutzer:innen, die auf einen bestimmten Canvas-Schritt geklickt haben.]({% image_buster /assets/img/keyword_example1.jpg %})

## Schlüsselwortkategorie-spezifisches Retargeting {#keyword-category-specific-retargeting}

Zusätzlich zu den drei Standard-Schlüsselwortkategorien (Opt-in, Opt-out und Hilfe) können Sie bis zu 25 eigene Schlüsselwortkategorien erstellen, mit denen Sie beliebige Schlüsselwörter und Antworten identifizieren können. Diese Kategorien können zum Filtern und Retargeting verwendet werden. Weitere Informationen über globale Schlüsselwortkategorien und deren Einrichtung finden Sie unter [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

### Nach Aktualität filtern {#filter-by-recency}

Filtern Sie nach der Aktualität der Antwort einer Nutzer:in auf Ihr SMS-, MMS- oder RCS-Programm. Dieser Filter wertet das letzte Datum aus, an dem eine Nutzer:in eine eingehende Nachricht gesendet hat, die in eine der Schlüsselwortkategorien fällt.

![Segmentierungsfilter „Letzte SMS an Abo-Gruppe „Marketing SMS“ gesendet" mit dem Schlüsselwort „Opt-in“ nach dem 11. August 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Nach Campaign- oder Canvas-Attribution filtern {#filter-by-campaign-or-canvas-attribution}

Filtern Sie nach Nutzer:innen, die auf eine bestimmte SMS-, MMS- oder RCS-Campaign oder Canvas-Komponente, Schlüsselwortkategorie oder einen bestimmten Tag geantwortet haben.

{% alert note %}
Diese Filter verwenden [Messaging-Interaktionsdaten]({{site.baseurl}}/messaging_interaction_data). Bei gestoppten Campaigns und Canvases verfallen diese Daten nach drei Monaten, sofern sie nicht in einem aktiven Retargeting-Filter verwendet werden. Abgelaufene Daten können wiederhergestellt werden. Das Aufbewahrungsfenster Ihres Workspace kann vom Standard abweichen.
{% endalert %}

#### Nach Antwort auf eine bestimmte Campaign mit Schlüsselwortkategorie filtern {#filter-by-replied-to-a-specific-campaign-with-keyword-category}

![Campaign mit dem Filter „Hat auf SMS geantwortet“ für Campaign „SMS-283“ „Aktion“.]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

#### Nach Antwort auf eine Campaign oder ein Canvas mit einem bestimmten Tag filtern {#filter-by-replied-to-a-campaign-or-canvas-with-a-specific-tag}

![Campaign mit dem Filter „Hat auf SMS geantwortet“ für Campaign oder Canvas mit Tag „Curbside Messaging Service C“.]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

#### Nach Antwort auf einen bestimmten Schritt filtern {#filter-by-replied-to-a-specific-step}

![Campaign mit dem Filter „Hat auf SMS geantwortet“ für Schritt „SMS Double Opt“ „Step - Help“.]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Nachrichten per Schlüsselwort triggern {#trigger-messages-by-keyword}

Nachrichten können getriggert werden, wenn Nutzer:innen eingehende Nachrichten basierend auf Schlüsselwortkategorien senden (Nutzer:in hat eines der Schlüsselwörter gesendet) oder auf anderen Schlüsselwörtern basierend (Nutzer:in hat ein Schlüsselwort gesendet, das nicht in eine der bestehenden Kategorien fällt). Diese Trigger werden im Schritt „Zustellung“ des Campaign-Builders festgelegt.

Bei der Auswertung, ob eine eingehende Nachricht ein definiertes Trigger-Ereignis erfüllt, werden führende und nachfolgende Leerzeichen vor der Auswertung entfernt.

{% alert tip %}
Wenn ein aktionsbasiertes Canvas durch eine eingehende SMS- oder MMS-Nachricht getriggert wird, können Sie [unterstützte SMS-Liquid-Eigenschaften]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) in jedem Canvas-Schritt bis zum nächsten Aktionspfad referenzieren.
{% endalert %}

#### Per eingehende Schlüsselwortkategorie triggern {#trigger-by-inbound-keyword-category}

![Aktionsbasierte SMS-Campaign mit dem Segmentierungsfilter „Schlüsselwort „Opt-in“ an Abo-Gruppe „Marketing SMS“ gesendet".]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

#### Per beliebige Schlüsselwörter triggern {#trigger-by-arbitrary-keywords}

Beachten Sie: Wenn Sie eine Nachricht bei einer „Other“-Schlüsselwortantwort triggern, haben Sie die Möglichkeit, den Schlüsselwort-Body auf eine exakte Textübereinstimmung zu prüfen. Diese Übereinstimmung folgt denselben Regeln wie angegeben: Es wird nur die **exakte Einzelwort-Nachricht** verarbeitet (Groß-/Kleinschreibung wird _nicht berücksichtigt_). Ein gesendetes Schlüsselwort wie `Hello Braze!` würde nicht den im folgenden Beispiel gezeigten Kriterien entsprechen.

![Aktionsbasierte SMS-Campaign mit der Schlüsselwortkategorie „Other“, bei der der Nachrichtentext genau „Hello“ oder „Hey“ lautet.]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

#### Schlüsselwörter als Template verwenden {#template-keywords}

Beim Triggern einer Campaign oder Canvas-Komponente durch eine eingehende SMS oder MMS können Sie optional den Text oder die Medienanhänge, die Ihre Nutzer:in gesendet hat, mit Liquid in den Body Ihrer Campaign oder Ihres Canvas einfügen. Dies ermöglicht Ihnen den Zugriff auf die Antwort der Nutzer:in, die Sie dann in Ihre Antwort einbinden, bedingte Logik anwenden oder alles andere tun können, was mit Liquid möglich ist.

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