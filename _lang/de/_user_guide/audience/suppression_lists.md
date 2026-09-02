---
nav_title: Unterdrückungslisten
article_title: Unterdrückungslisten
page_order: 7
page_type: reference
tool: Segments
description: "Diese Seite beschreibt, wie Sie Unterdrückungslisten verwenden, um festzulegen, welche Nutzer:innen Ihre Nachrichten niemals erhalten sollen."

---

# Unterdrückungslisten {#suppression-lists}

> Unterdrückungslisten sind Gruppen von Nutzer:innen, die automatisch keine Campaigns oder Canvases erhalten. Unterdrückungslisten werden durch Segmentfilter definiert, und Nutzer:innen treten in Unterdrückungslisten ein und aus, sobald sie die Filterkriterien erfüllen. Sie können auch Ausnahme-Tags festlegen, damit die Unterdrückungsliste nicht für Campaigns oder Canvases mit diesen Tags gilt. Nachrichten aus Campaigns oder Canvases mit Ausnahme-Tags erreichen weiterhin Nutzer:innen der Unterdrückungsliste, die sich in den Zielsegmenten befinden.

## Warum Unterdrückungslisten verwenden? {#why-use-suppression-lists}

Unterdrückungslisten sind dynamisch und gelten automatisch für alle Formen des Messagings, aber Sie können Ausnahmen für ausgewählte Tags festlegen. Wenn Ihre ausgewählten Ausnahme-Tags in einer Campaign oder einem Canvas verwendet werden, gilt diese Unterdrückungsliste nicht für diese Campaign oder dieses Canvas. Nachrichten aus Campaigns oder Canvases mit Ausnahme-Tags erreichen weiterhin alle Nutzer:innen der Unterdrückungsliste, die Teil Ihrer Zielsegmente sind.

### Nachrichtentypen und Kanäle, die von Unterdrückungslisten betroffen sind {#message-types-and-channels-affected-by-suppression-lists}

Unterdrückungslisten gelten für alle Nachrichtentypen und Kanäle mit Ausnahme von [Feature-Flags]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags). Das bedeutet, dass Unterdrückungslisten standardmäßig für alle Kanäle, Campaigns und Canvases gelten, einschließlich:
- [API-Kampagnen]({{site.baseurl}}/api/api_campaigns)
- API-getriggerte Campaigns und Canvases
- [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)

Der einzige Nachrichtentyp, für den Unterdrückungslisten nicht gelten, sind Feature-Flags. Nutzer:innen in einer Unterdrückungsliste werden nicht von Feature-Flags unterdrückt, aber von allen anderen Kanälen.

Sie können Ausnahme-Tags verwenden, damit Nutzer:innen der Unterdrückungsliste weiterhin von bestimmten Campaigns und Canvases angesprochen werden. Weitere Informationen finden Sie in Schritt 4 unter [Unterdrückungslisten einrichten](#setup). Wenn Sie einer Unterdrückungsliste keine Ausnahme-Tags hinzufügen, werden Nutzer:innen in dieser Unterdrückungsliste mit keinem Messaging außer Feature-Flags angesprochen.

{% alert note %}
Unterdrückungslisten werden auf API-Kampagnen angewendet, die im Braze-Dashboard mit einer `campaign_id` erstellt wurden. Unterdrückungslisten gelten nicht für Nachrichten, die über [Braze-Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) ohne zugehörige `campaign_id` gesendet werden.
{% endalert %}

![Der Abschnitt „Ausnahmeeinstellungen“ mit einem Kontrollkästchen, um die Unterdrückungsliste nicht auf API-getriggerte Campaigns und Canvases anzuwenden.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Unterdrückungslisten einrichten {#setup}

{% alert note %}
Alle Nutzer:innen können Unterdrückungslisten einsehen, aber nur Nutzer:innen mit [Admin-Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions?tab=admin) können Unterdrückungslisten erstellen und verwalten.
{% endalert %}

1. Gehen Sie zu **Audience** > **Suppression Lists**.
2. Wählen Sie **Create Suppression List** und geben Sie einen Namen ein.
3. Verwenden Sie Segmentfilter, um die Nutzer:innen in Ihren Unterdrückungslisten zu identifizieren. Sie müssen mindestens einen auswählen.

{% alert important %}
Obwohl der Einrichtungsprozess der [Segmenterstellung]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) ähnelt, ist eine Unterdrückungsliste eine Gruppe von Nutzer:innen, an die Sie unabhängig von der Segmentzugehörigkeit **keine** Nachrichten senden möchten.
{% endalert %}

![Ein Unterdrückungslisten-Builder mit einem Filter für Nutzer:innen, die eine E-Mail zuletzt vor mehr als 90 Tagen geöffnet haben.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4. Legen Sie fest, ob Ausnahmen basierend auf Tags gelten sollen, indem Sie das Kontrollkästchen unter Ihrem Segmentnamen aktivieren (weitere Informationen finden Sie unter [Warum Unterdrückungslisten verwenden?](#why-use-suppression-lists)), und fügen Sie dann die Tags der Campaigns oder Canvases hinzu, die Nutzer:innen in dieser Unterdrückungsliste weiterhin erhalten sollen. <br><br>Mit anderen Worten: Wenn Sie den Ausnahme-Tag „Versandbestätigung“ hinzufügen, werden Nutzer:innen in Ihrer Unterdrückungsliste von allen Nachrichten ausgeschlossen, außer von solchen, die den Tag „Versandbestätigung“ verwenden.<br><br>![Der Abschnitt „Versandlistendetails“ mit einem angewendeten Ausnahme-Tag namens „Versandbestätigung“.]({% image_buster /assets/img/exception_tags.png %})<br><br>
5. Speichern oder aktivieren Sie Ihre Unterdrückungsliste.
- Wenn Sie speichern, wird Ihre Unterdrückungsliste gespeichert, aber nicht aktiviert, d. h. sie tritt nicht in Kraft. Ihre Unterdrückungsliste bleibt inaktiv, bis Sie sie aktivieren, und inaktive Unterdrückungslisten haben keinen Einfluss auf das Messaging (Nutzer:innen werden nicht von Nachrichten ausgeschlossen).
- Wenn Sie aktivieren, wird Ihre Unterdrückungsliste gespeichert und tritt sofort in Kraft, d. h. Nutzer:innen in Ihrer Unterdrückungsliste werden sofort von Campaigns oder Canvases ausgeschlossen (mit Ausnahme derjenigen, die einen Ausnahme-Tag enthalten).

{% alert note %}
Nur Admins können Unterdrückungslisten speichern oder aktivieren. In der Beta können Sie bis zu fünf aktive Unterdrückungslisten gleichzeitig haben.
{% endalert %}

Sie können Unterdrückungslisten deaktivieren oder archivieren, wenn Sie sie nicht mehr benötigen.
- Zum Deaktivieren wählen Sie eine aktive Unterdrückungsliste aus und wählen Sie **Deactivate**. Deaktivierte Unterdrückungslisten können später wieder aktiviert werden.
- Zum Archivieren tun Sie dies über die Seite **Suppression Lists**.

## Verwendung von Unterdrückungslisten {#suppression-list-usage}

Um zu überprüfen, ob Ihre Unterdrückungsliste Nutzer:innen daran gehindert hat, eine Nachricht zu erhalten, verwenden Sie **User Lookup** im Schritt **Target Audience** innerhalb Ihrer Campaign oder Ihres Canvas. Hier können Sie sehen, zu welcher Unterdrückungsliste sie gehören.

{% alert note %}
Unterdrückungslisten werden vor dem Senden einer Nachricht aktualisiert, nicht nach dem Start einer Campaign. Das bedeutet, dass Nutzer:innen, die nach dem Start der Campaign, aber vor dem Senden der Nachricht zu einer Unterdrückungsliste hinzugefügt werden, die Nachricht möglicherweise trotzdem erhalten können.
{% endalert %}

![Das Fenster „User Lookup“, das zeigt, dass Nutzer:innen in einer Unterdrückungsliste sind.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
Sie können angewendete Unterdrückungslisten auch im Schritt **Summary** finden.
{% endalert %}

Verwenden Sie beim Erstellen einer Campaign oder eines Canvas **User Lookup** im Schritt **Target Audience**, um nach Nutzer:innen zu suchen. Wenn sie nicht in der Zielgruppe sind, können Sie die Unterdrückungsliste sehen, zu der sie gehören.

![Das Fenster „User Lookup“, das zeigt, dass Nutzer:innen in einer Unterdrückungsliste sind.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campaign

Wenn Nutzer:innen in einer Unterdrückungsliste sind, erhalten sie keine Campaign, für die diese Unterdrückungsliste gilt. Informationen zu Fällen, in denen eine Unterdrückungsliste nicht gilt, finden Sie unter [Nachrichtentypen und Kanäle, die von Unterdrückungslisten betroffen sind](#message-types-and-channels-affected-by-suppression-lists).

![Der Abschnitt „Unterdrückungslisten“ mit einer aktiven Unterdrückungsliste namens „Low marketing health scores“.]({% image_buster /assets/img/active_suppression_list.png %})

### Canvas

Ab dem Moment, in dem Nutzer:innen zu einer Unterdrückungsliste hinzugefügt werden, treten sie nicht in Canvases ein. Wenn sie bereits in ein Canvas eingetreten sind, erhalten sie keine Nachrichtenschritte. Das bedeutet, dass Nutzer:innen, die sich bereits in einem Canvas befinden, wenn sie zu einer Unterdrückungsliste hinzugefügt werden, durch das Canvas bis zum nächsten Nachrichtenschritt voranschreiten und an diesem Punkt aussteigen, ohne den Nachrichtenschritt zu erhalten.

Nehmen wir zum Beispiel an, ein Canvas hat einen Nutzeraktualisierungsschritt, gefolgt von einem Nachrichtenschritt. Wenn Nutzer:innen in das Canvas eintreten und dann zu einer Unterdrückungsliste hinzugefügt werden, durchlaufen sie weiterhin den Nutzeraktualisierungsschritt (wo sie möglicherweise aktualisiert werden) und steigen dann beim Nachrichtenschritt aus, wobei sie in den Ausstiegsmetriken berücksichtigt werden.