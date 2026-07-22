{% comment %}
  Gemeinsame Braze-Umfragen-Dokumentation.
  Parameter:
  - channel (erforderlich): "in_app_message" oder "landing_page"
{% endcomment %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Braze surveys' %}

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

Während des Early Access werden Umfragen innerhalb Ihres bestehenden Nachrichtenkompositions-Flows erstellt.

{% if include.channel == 'in_app_message' %}
1. Erstellen Sie eine [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) in einer Campaign oder einem Canvas.
2. Wählen Sie **Umfrage** als Nachrichtentyp aus.
{% elsif include.channel == 'landing_page' %}
1. Gehen Sie zu **Messaging** > **Landing-Pages**.
2. Erstellen Sie eine neue Landing-Page.
3. Wählen Sie **Umfrage** als Nachrichtentyp aus.
{% else %}
1. Gehen Sie zu **Messaging** > **Landing-Pages**, oder erstellen Sie eine [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) in einer Campaign oder einem Canvas.
2. Erstellen Sie eine neue Nachricht.
3. Wählen Sie **Umfrage** als Nachrichtentyp aus.
{% endif %}

{% if include.channel == 'in_app_message' %}

## In-App-Nachrichten-Umfrage erstellen {#compose-an-in-app-message-survey}

In-App-Nachrichten-Umfragen enthalten standardmäßig zwei Seiten:

- **Seite 1**, auf der Nutzer:innen Fragen beantworten
- **Bestätigungsseite**, auf der die Umfrage abgesendet wird

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
- Optionsfeld-Gruppe
- Kurztexterfassung
- Langtexterfassung
- Dropdown
- Einzelnes Kontrollkästchen
- Kontrollkästchen-Gruppe
- Bewertungsskala

### Antwortmöglichkeiten randomisieren {#randomize-answer-choices}

Optionsfeld-Gruppen, Kontrollkästchen-Gruppen und Dropdown-Blöcke unterstützen randomisierte Antwortmöglichkeiten. Aktivieren Sie **Randomize choice order**, um die Auswahlmöglichkeiten bei jedem Laden der Umfrage zufällig anzuordnen. Verwenden Sie diese Einstellung, um Reihenfolge-Bias zu reduzieren, wenn dieselbe erste Option die Antworten verzerren könnte.

Die Randomisierung ändert nur die Anzeigereihenfolge für jede:n Umfrageteilnehmer:in. Reporting-Labels und -Werte bleiben den von Ihnen konfigurierten Auswahlmöglichkeiten zugeordnet, sodass Analytics, CSV-Exporte und Segmentierung dieselben Antwortdaten verwenden.

### Langtexterfassung {#long-text-capture}

Die Langtexterfassung eignet sich für qualitatives Feedback.

Sie können Folgendes konfigurieren:

- Minimale und maximale Zeichenanzahl (bis zu 1.000)
- Ob Zeichenlimits während der Erstellung angezeigt werden sollen
- Höhe des Textbereichs (Zeilen)
- Platzhaltertext

Während des Early Access sind Langtextantworten in Berichten und Exporten verfügbar, können jedoch nicht als angepasste Attribute im Nutzerprofil protokolliert werden.

![Einstellungen für den Langtexterfassungs-Block.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

### Bewertungsskala {#rating-scale}

Die Bewertungsskala eignet sich zur Erfassung von Stimmung, Zufriedenheit oder Weiterempfehlungswahrscheinlichkeit als einzelne Zahl.

Wählen Sie im Einstellungs-Panel eine Skala aus dem Dropdown:

- **1–10**
- **1–5**
- **0–10** (Standard-Net-Promoter-Score-Bereich (NPS))

Sie können eine Bewertung als Umfrageantwort erfassen, als ganzzahliges angepasstes Attribut protokollieren oder beides. Kombinieren Sie einen Bewertungsskala-Block mit einem [Langtexterfassungs](#long-text-capture)-Block, um in derselben Umfrage einen numerischen Wert zusammen mit qualitativem Feedback zu erfassen.

{% if include.channel == 'in_app_message' %}
![Bewertungsskala zur Bewertung Ihres Shop-Erlebnisses von 1 bis 5.]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![Bewertungsskala zur Angabe der Weiterempfehlungswahrscheinlichkeit eines Produkts an Freunde von 1 bis 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![Bewertungsskala zur Angabe der Weiterempfehlungswahrscheinlichkeit eines Produkts an Freunde von 1 bis 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## Pflichtfelder und Attribute konfigurieren {#configure-required-fields-and-attributes}

Geben Sie für jeden Formularblock im Einstellungs-Panel auf der rechten Seite einen **Bezeichner für das Reporting** ein. Dieser Bezeichner erscheint im Umfrage-Reporting und in CSV-Exporten.

Während des Early Access:

- Sie können die meisten Umfrageantworten in angepassten Attributen des Nutzerprofils protokollieren.
- Langtextantworten können nicht als angepasste Attribute protokolliert werden.
- Wenn Sie eine Antwort nicht als Nutzerattribut protokollieren, können Sie Nutzer:innen nicht nach diesem Antwortwert segmentieren.

![Bezeichner für das Reporting und Einstellungen zur Attributprotokollierung.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Berichte und Analytics anzeigen {#view-reporting-and-analytics}

Nach dem Start können Sie die Ergebnisse hier überprüfen:

{% if include.channel == 'in_app_message' %}
- Im Tab **Responses** für In-App-Nachricht-Umfragen
{% elsif include.channel == 'landing_page' %}
- In der Landing-Page-Analytics-Ansicht für Landing-Page-Umfragen
{% else %}
- Im Tab **Responses** für In-App-Nachricht-Umfragen
- In der Landing-Page-Analytics-Ansicht für Landing-Page-Umfragen
{% endif %}

Übergeordnete Analytics umfassen:

- **All responses:** Gesamtzahl der vollständigen und unvollständigen Antworten
- **Completed:** Nutzer:innen, die alle Pflichtfragen beantwortet haben
- **Partially complete:** Nutzer:innen, die einige Daten übermittelt, aber nicht alle Pflichtfragen beantwortet haben
- **Unique impressions:** Gesamtzahl der Seitenaufrufe

{% if include.channel == 'landing_page' %}
{% alert note %}
Landing-Page-Umfragen erfassen während des Early Access keine teilweise abgeschlossenen Antworten.
{% endalert %}
{% endif %}

Sie können auch Aufschlüsselungen der Antworten pro Frage einsehen und Daten als CSV exportieren.

### Chart-Typ auswählen {#choose-a-chart-type}

Für Radiobutton-, Dropdown- und Checkbox-Formularblöcke können Sie in der Umfrage-Analytics-Ansicht zwischen drei Chart-Typen wählen. So erhalten Sie mehr Flexibilität bei der Interpretation und Weitergabe von Insights, ohne in ein Drittanbieter-Tool exportieren zu müssen.

| Chart-Typ | Geeignet für |
| --- | --- |
| Balkendiagramm | Die standardmäßige horizontale Ansicht von Antwortanzahlen und Prozentsätzen. |
| Säulendiagramm | Eine vertikale Ansicht von Antwortanzahlen und Prozentsätzen. Verwenden Sie dieses Chart, um Antworten nebeneinander zu vergleichen, insbesondere bei Mehrfachauswahl-Fragen oder Fragen mit mehr Antwortoptionen. |
| Kreisdiagramm | Eine proportionale Aufschlüsselung der Antworten. Verwenden Sie dieses Chart für Einzelauswahl-Fragen, wenn Sie sehen möchten, wie sich die Antworten auf die Optionen verteilen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chart-Typen für Umfragen" }

Jedes Chart wird in Echtzeit aktualisiert, sobald Antworten eingehen. Sie können den Chart-Typ jederzeit wechseln, ohne die zugrunde liegenden Daten zu beeinflussen.

![Aufschlüsselung der Umfrageergebnisse auf Fragenebene als Balkendiagramm.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Retarget und Trigger {#retarget-and-trigger}

Während des Early Access können Sie:

- Nutzer:innen nach Umfrageantworten segmentieren, die als Nutzerattribute protokolliert werden.
- Nutzer:innen nach dem Abschlussstatus der Umfrage segmentieren.

{% if include.channel == 'in_app_message' %}

![Trigger-Einrichtung und Segmentierungsfilter für die Umfrage-Nachverfolgung.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage in einer In-App-Nachrichten-Campaign abschließen.

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung einer In-App-Nachrichten-Campaign-Umfrage.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung einer Landing-Page-Umfrage.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage auf einer Landing-Page abschließen.

{% else %}

![Trigger-Einrichtung und Segmentierungsfilter für die Umfrage-Nachverfolgung.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage auf einer Landing-Page oder in einer In-App-Nachrichten-Campaign abschließen.

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung einer Landing-Page-Umfrage.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Trigger-Einrichtung und Segmentierungsfilter für die Nachverfolgung einer In-App-Nachrichten-Campaign-Umfrage.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Einschränkungen {#limitations}

Während des Early Access gelten die folgenden Einschränkungen:

- Sie können Nutzer:innen nicht nach Freitext-Antworten segmentieren.
- Frage-und-Antwort-Triggering, das nicht auf protokollierten Nutzerattributen basiert, ist nicht verfügbar.