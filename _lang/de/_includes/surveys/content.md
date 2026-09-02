{% comment %}
  Gemeinsame Braze-Umfragen-Dokumentation.
  Parameter:
  - channel (erforderlich): "in_app_message" oder "landing_page"
{% endcomment %}

Einen Überblick über Umfragen und die kanalübergreifend verfügbaren Funktionen finden Sie unter [Umfragen]({{site.baseurl}}/user_guide/messaging/surveys).

## Voraussetzungen {#prerequisites}

Bevor Sie eine Umfrage erstellen, müssen Sie:

{% if include.channel == 'in_app_message' %}
- Zugriff auf In-App-Nachrichten in Ihrem Braze-Workspace haben
- Mit dem [Erstellen von In-App-Nachrichten im Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) vertraut sein
{% elsif include.channel == 'landing_page' %}
- Zugriff auf Landing-Pages in Ihrem Braze-Workspace haben
- Mit dem [Erstellen von Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) vertraut sein
{% else %}
- Zugriff auf Landing-Pages, In-App-Nachrichten oder beides in Ihrem Braze-Workspace haben
- Mit dem [Erstellen von Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) und dem [Erstellen von In-App-Nachrichten im Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) vertraut sein
{% endif %}

## Umfrage erstellen {#create-a-survey}

Umfragen werden innerhalb Ihres bestehenden Nachrichtenerstellungs-Flows erstellt.

{% if include.channel == 'in_app_message' %}
1. Erstellen Sie eine [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) in einer Campaign oder einem Canvas.
2. Wählen Sie **Umfrage** als Nachrichtentyp aus.
{% elsif include.channel == 'landing_page' %}
1. Gehen Sie zu **Messaging** > **Landing-Pages**.
2. Erstellen Sie eine neue Landing-Page.
3. Wählen Sie **Umfrage** als Nachrichtentyp aus.
{% else %}
1. Gehen Sie zu **Messaging** > **Landing-Pages** oder erstellen Sie eine [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) in einer Campaign oder einem Canvas.
2. Erstellen Sie eine neue Nachricht.
3. Wählen Sie **Umfrage** als Nachrichtentyp aus.
{% endif %}

{% if include.channel == 'in_app_message' %}

## In-App-Nachrichten-Umfrage erstellen {#compose-an-in-app-message-survey}

In-App-Nachrichten-Umfragen enthalten standardmäßig zwei Seiten:

- **Seite 1**, auf der Nutzer:innen Fragen beantworten
- **Bestätigungsseite**, auf der die Umfrage übermittelt wird

Standardmäßig sind Buttons mit **Nächste Seite** verknüpft. Um dieses Verhalten zu ändern, aktualisieren Sie jeden Button im Panel **Aktionen**.

![Seitenfluss und Aktionseinstellungen einer In-App-Nachrichten-Umfrage.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Umfrage-Formularblöcke verwenden {#use-survey-form-blocks}

Informationen zu gemeinsamen Stil- und Kompositionseinstellungen finden Sie unter:

{% if include.channel == 'in_app_message' %}
- [Drag-and-Drop-Editor-Blöcke für In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [Landing-Page-Formularblöcke]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- [Drag-and-Drop-Editor-Blöcke für In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Landing-Page-Formularblöcke]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% endif %}

Sie können die folgenden Formularblöcke zu Umfragen hinzufügen:

- Telefonnummernerfassung
- E-Mail-Erfassung
- Optionsfeldgruppe
- Kurztexterfassung
- Langtexterfassung
- Dropdown
- Einzelnes Kontrollkästchen
- Kontrollkästchengruppe
- Bewertungsskala
- Net Promoter Score

### Antwortmöglichkeiten randomisieren {#randomize-answer-choices}

Optionsfeldgruppe, Kontrollkästchengruppe und Dropdown-Blöcke unterstützen randomisierte Antwortmöglichkeiten. Aktivieren Sie **Randomize choice order**, um die Auswahlmöglichkeiten bei jedem Laden der Umfrage zufällig anzuordnen. Weitere Informationen finden Sie unter [Randomisierte Reihenfolge der Auswahlmöglichkeiten]({{site.baseurl}}/user_guide/messaging/surveys#randomized-choice-order).

### Langtexterfassung {#long-text-capture}

Die Langtexterfassung eignet sich für qualitatives Feedback mit bis zu 1.000 Zeichen. Weitere Informationen finden Sie unter [Langtexterfassung]({{site.baseurl}}/user_guide/messaging/surveys#long-form-text-capture).

### Bewertungsskala {#rating-scale}

Die Bewertungsskala (auch als Zahlenskala-Frage bezeichnet) eignet sich zur Erfassung von Stimmung, Zufriedenheit oder Weiterempfehlungswahrscheinlichkeit als einzelne Zahl. Weitere Informationen finden Sie unter [Zahlenskala-Fragen]({{site.baseurl}}/user_guide/messaging/surveys#number-scale-questions).

{% if include.channel == 'in_app_message' %}
![Bewertungsskala zur Bewertung Ihres Shop-Erlebnisses von 1 bis 5.]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![Bewertungsskala zur Angabe der Weiterempfehlungswahrscheinlichkeit eines Produkts an Freunde von 1 bis 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![Bewertungsskala zur Angabe der Weiterempfehlungswahrscheinlichkeit eines Produkts an Freunde von 1 bis 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## Pflichtfelder und Attribute konfigurieren {#configure-required-fields-and-attributes}

Geben Sie für jeden Formularblock im Einstellungs-Panel auf der rechten Seite einen **Bezeichner für das Reporting** ein. Dieser Bezeichner wird im Umfrage-Reporting und in CSV-Exporten angezeigt.

Beachten Sie Folgendes:

- Sie können die meisten Umfrageantworten in angepassten Attributen des Nutzerprofils protokollieren.
- Langtextantworten können nicht als angepasste Attribute protokolliert werden.
- Wenn Sie eine Antwort nicht als Nutzerattribut protokollieren, können Sie Nutzer:innen nicht nach diesem Antwortwert segmentieren.

![Einstellungen für den Bezeichner für das Reporting und die Attributprotokollierung.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Berichte und Analytics ansehen {#view-reporting-and-analytics}

Überprüfen Sie nach dem Start die Ergebnisse in:

{% if include.channel == 'in_app_message' %}
- Dem Tab **Responses** für In-App-Nachricht-Umfragen
{% elsif include.channel == 'landing_page' %}
- Der Landing-Page-Analytics-Ansicht für Landing-Page-Umfragen
{% else %}
- Dem Tab **Responses** für In-App-Nachricht-Umfragen
- Der Landing-Page-Analytics-Ansicht für Landing-Page-Umfragen
{% endif %}

Definitionen der übergeordneten Analytics, die für jede Umfrage verfügbar sind (alle Antworten, abgeschlossen, teilweise abgeschlossen und eindeutige Impressionen), finden Sie unter [Analytics]({{site.baseurl}}/user_guide/messaging/surveys#analytics).

{% if include.channel == 'landing_page' %}
{% alert note %}
Landing-Page-Umfragen erfassen teilweise abgeschlossene Antworten, wenn die Umfrage [mehrstufige Formulare]({{site.baseurl}}/user_guide/messaging/surveys#multi-step-landing-page-forms) verwendet.
{% endalert %}
{% endif %}

Sie können auch Aufschlüsselungen der Antworten pro Frage überprüfen, zwischen drei Chart-Typen wählen und Daten als CSV exportieren. Weitere Informationen finden Sie unter [Chart-Typen]({{site.baseurl}}/user_guide/messaging/surveys#chart-types).

## Retarget und Trigger {#retarget-and-trigger}

Sie können:

- Nutzer:innen anhand von Umfrageantworten segmentieren, die als Nutzerattribute protokolliert werden.
- Nutzer:innen anhand des Umfrage-Abschlussstatus segmentieren.

{% if include.channel == 'in_app_message' %}

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung von Umfragen.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage in einer In-App-Nachricht-Campaign abschließen.

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung von In-App-Nachricht-Campaign-Umfragen.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung von Landing-Page-Umfragen.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage auf einer Landing-Page abschließen.

{% else %}

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung von Umfragen.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage auf einer Landing-Page oder in einer In-App-Nachricht-Campaign abschließen.

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung von Landing-Page-Umfragen.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung von In-App-Nachricht-Campaign-Umfragen.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Einschränkungen {#limitations}

Es gelten die folgenden Einschränkungen:

- Sie können Nutzer:innen nicht anhand von Freitext-Antworten segmentieren.
- Eine Frage-und-Antwort-Triggerung, die nicht auf protokollierten Nutzerattributen basiert, ist nicht verfügbar.