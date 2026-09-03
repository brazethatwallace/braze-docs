{% if include.section == "SDK requirements" %}

## Voraussetzungen {#prerequisites}

### Minimale SDK-Versionen {#minimum-sdk-versions}

Nachrichten, die mit dem Drag-and-Drop-Editor erstellt wurden, können nur an Nutzer:innen mit den folgenden SDK-Mindestversionen gesendet werden. Weitere Informationen finden Sie unter [Erstellen einer In-App-Nachricht per Drag-and-Drop: Voraussetzungen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#prerequisites).

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### SDK-Versionen für Textlinks {#sdk-versions-for-text-links}

Um Textlinks einzubinden, die die Nachricht nicht schließen, sind die folgenden SDK-Mindestversionen erforderlich:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Wenn Sie in Ihrer In-App-Nachricht einen Link einfügen, der zu einer URL weiterleitet, und die Nutzer:innen nicht über die angegebenen SDK-Mindestversionen verfügen, wird die Nachricht durch einen Klick auf den Link geschlossen, und die Nutzer:innen können nicht zur Nachricht zurückkehren, um das Formular abzuschicken.
{% endalert %}

{% endif %}

{% if include.section == "message style" %}

Bevor Sie mit dem Anpassen Ihres Templates beginnen, können Sie über das Seitenmenü Stile auf Nachrichtenebene für die gesamte Nachricht festlegen. Vielleicht möchten Sie zum Beispiel die Schriftart des gesamten Textes oder die Farbe aller Links in Ihrer Nachricht anpassen. Sie können die Nachricht auch als Modal oder im Vollbildmodus anzeigen lassen.

{% endif %}


<!-- Add this after the disclaimers are added to all email sign-up templates: "We have provided a placeholder disclaimer in the template solely as an example, but this should not be relied upon for compliance purposes."-->

{% if include.section == "email disclaimer" %}

Wir empfehlen Ihnen, in Ihre Nachricht eine Opt-in-Formulierung und Links zu den Datenschutzrichtlinien und Geschäftsbedingungen Ihrer Marke aufzunehmen. Arbeiten Sie unbedingt mit Ihrer Rechtsabteilung zusammen, um eine Formulierung zu entwickeln, die auf Ihre spezifische Marke zugeschnitten ist.

{% alert note %}
Best Practices für die Zustellbarkeit gehen oft über die gesetzlichen Anforderungen hinaus. Unsere Empfehlung lautet, immer die ausdrückliche Zustimmung zum Versand von E-Mails einzuholen und den Nutzer:innen die Möglichkeit zu geben, den Empfang einfach abzulehnen.
{% endalert %}

{% endif %}

{% if include.section == "email validation" %}

Wenn Nutzer:innen eine E-Mail-Adresse eingeben, die nicht akzeptierte Sonderzeichen enthält, wird eine allgemeine Fehleranzeige angezeigt und das Formular kann nicht abgeschickt werden. Diese Fehlermeldung ist nicht anpassbar. Sie können das Fehlerverhalten im Tab **Preview & Test** und auf Ihrem Testgerät ansehen. Erfahren Sie mehr darüber, wie Braze E-Mail-Adressen formatiert, unter [E-Mail-Validierung]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation).

{% endif %}

{% if include.section == "email double opt-in" %}

### Doppelte Opt-in-Verifizierung {#double-opt-in-verification}

Um sicherzustellen, dass sich alle, die sich in Ihre Liste eingetragen haben, auch wirklich eintragen wollten und die richtige E-Mail-Adresse angegeben haben, empfehlen wir, von allen, die sich über Ihr E-Mail-Anmeldeformular registriert haben, eine zweite Bestätigung einzuholen, indem Sie einen [Double-Opt-in](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in)-Flow versenden.

Eine der Möglichkeiten, dies einzurichten, ist über Canvas:

1. Erstellen Sie ein aktionsbasiertes Canvas und richten Sie es so ein, dass es ausgelöst wird, wenn Nutzer:innen eine E-Mail-Adresse zu Braze hinzufügen. Stellen Sie sicher, dass Sie auch Nutzer:innen ansprechen können, die neu auf der Plattform sind (z. B. indem Sie ein Segment ohne Filter im Canvas verwenden).
2. Erstellen Sie einen E-Mail-Nachrichtenschritt mit einem CTA, der einen Hyperlink zum {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} Liquid-Tag enthält. Dadurch wird der E-Mail-Abo-Status der Nutzer:innen in `opted_in` geändert, wenn sie auf den Button klicken.
3. Fügen Sie einen [Aktionspfade-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths) hinzu.
4. Lösen Sie für den ersten Pfad eine E-Mail aus, wenn Nutzer:innen ihren E-Mail-Abo-Status in `opted_in` ändern. Diese E-Mail sollte die Nutzer:innen darüber informieren, dass ihre E-Mail-Adresse bestätigt wurde.
5. Richten Sie den anderen Pfad so ein, dass das Canvas verlassen wird, nachdem das Zeitfenster abgelaufen ist.

{% endif %}

{% if include.section == "reporting" %}

Nachdem Ihre Campaign gestartet ist, können Sie die Ergebnisse in Echtzeit analysieren, um zu sehen, wie viele Nutzer:innen mit Ihrer Campaign interagiert haben. Um zu sehen, wie viele Nutzer:innen sich für die Abo-Gruppe angemeldet haben, können Sie [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment), das Nutzer:innen enthält, die die Abo-Gruppe abonniert haben, indem Sie nach Nutzer:innen filtern, die die In-App-Nachricht erhalten und das Formular abgeschickt haben.

{% endif %}