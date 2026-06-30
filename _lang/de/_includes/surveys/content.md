{% comment %}
  Gemeinsame Braze-Umfragen-Dokumentation.
  Parameter:
  - channel (erforderlich): "in_app_message" oder "landing_page"
{% endcomment %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Braze surveys' %}

## Voraussetzungen {#prerequisites}

Bevor Sie eine Umfrage erstellen, müssen Sie:

{% if include.channel == 'in_app_message' %}
- Zugriff auf In-App Messages in Ihrem Braze Workspace haben
- Mit dem [Erstellen von In-App-Nachrichten im Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) vertraut sein
{% elsif include.channel == 'landing_page' %}
- Zugriff auf Landing-Pages in Ihrem Braze Workspace haben
- Mit dem [Erstellen von Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) vertraut sein
{% else %}
- Zugriff auf Landing-Pages, In-App Messages oder beides in Ihrem Braze Workspace haben
- Mit dem [Erstellen von Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) und dem [Erstellen von In-App-Nachrichten im Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) vertraut sein
{% endif %}

## Umfrage erstellen {#create-a-survey}

Während des Early Access werden Umfragen innerhalb Ihres bestehenden Nachrichtenkompositions-Flows erstellt.

{% if include.channel == 'in_app_message' %}
1. Erstellen Sie eine [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) in einer Campaign oder einem Canvas.
2. Wählen Sie **Survey** als Ihren Nachrichtentyp aus.
{% elsif include.channel == 'landing_page' %}
1. Gehen Sie zu **Messaging** > **Landing Pages**.
2. Erstellen Sie eine neue Landing-Page.
3. Wählen Sie **Survey** als Ihren Nachrichtentyp aus.
{% else %}
1. Gehen Sie zu **Messaging** > **Landing Pages** oder erstellen Sie eine [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) in einer Campaign oder einem Canvas.
2. Erstellen Sie eine neue Nachricht.
3. Wählen Sie **Survey** als Ihren Nachrichtentyp aus.
{% endif %}

{% if include.channel == 'in_app_message' %}

## In-App-Nachricht-Umfrage verfassen {#compose-an-in-app-message-survey}

In-App-Nachricht-Umfragen enthalten standardmäßig zwei Seiten:

- **Seite 1**, auf der Nutzer:innen Fragen beantworten
- **Bestätigungsseite**, auf der die Umfrage abgesendet wird

Standardmäßig sind Buttons mit **Next page** verknüpft. Um dieses Verhalten zu ändern, aktualisieren Sie jeden Button im **Aktionen**-Panel.

![Seitenfluss und Aktionseinstellungen einer In-App-Nachricht-Umfrage.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Umfrage-Formularblöcke verwenden {#use-survey-form-blocks}

Informationen zu gemeinsamen Stil- und Kompositionssteuerungen finden Sie unter:

{% if include.channel == 'in_app_message' %}
- [Editor-Blöcke des Drag-and-Drop-Editors für In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [Formularblöcke für Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#form-blocks)
{% else %}
- [Editor-Blöcke des Drag-and-Drop-Editors für In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Formularblöcke für Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#form-blocks)
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

### Antwortoptionen randomisieren {#randomize-answer-choices}

Optionsfeld-Gruppen, Kontrollkästchen-Gruppen und Dropdown-Blöcke unterstützen randomisierte Antwortoptionen. Aktivieren Sie **Randomize choice order**, um die Optionen bei jedem Laden der Umfrage zufällig anzuordnen. Verwenden Sie diese Einstellung, um Reihenfolge-Bias zu reduzieren, wenn dieselbe erste Option die Antworten verzerren könnte.

Die Randomisierung ändert nur die Anzeigereihenfolge für jede:n Umfrageteilnehmer:in. Berichtslabels und -werte bleiben den von Ihnen konfigurierten Optionen zugeordnet, sodass Analytics, CSV-Exporte und Segmentierung dieselben Antwortdaten verwenden.

### Langtexterfassung {#long-text-capture}

Die Langtexterfassung eignet sich für qualitatives Feedback.

Sie können Folgendes konfigurieren:

- Minimale und maximale Zeichenanzahl (bis zu 1.000)
- Ob Zeichenlimits während der Komposition angezeigt werden sollen
- Höhe des Textbereichs (Zeilen)
- Platzhaltertext

Während des Early Access sind Langtextantworten in Berichten und Exporten verfügbar, können jedoch nicht als angepasste Attribute im Nutzerprofil protokolliert werden.

![Einstellungen des Langtexterfassungs-Blocks.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Pflichtfelder und Attribute konfigurieren {#configure-required-fields-and-attributes}

Geben Sie für jeden Formularblock im Einstellungs-Panel auf der rechten Seite einen **Identifier for Reporting** ein. Dieser Bezeichner erscheint in Umfrageberichten und CSV-Exporten.

Während des Early Access:

- Sie können die meisten Umfrageantworten als angepasste Attribute im Nutzerprofil protokollieren.
- Langtextantworten können nicht als angepasste Attribute protokolliert werden.
- Wenn Sie eine Antwort nicht als Nutzerattribut protokollieren, können Sie Nutzer:innen nicht nach diesem Antwortwert segmentieren.

![Einstellungen für Berichtsbezeichner und Attributprotokollierung.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Berichte und Analytics anzeigen {#view-reporting-and-analytics}

Überprüfen Sie nach dem Start die Ergebnisse unter:

{% if include.channel == 'in_app_message' %}
- Dem Tab **Responses** für In-App-Nachricht-Umfragen
{% elsif include.channel == 'landing_page' %}
- Der Landing-Page-Analytics-Ansicht für Landing-Page-Umfragen
{% else %}
- Dem Tab **Responses** für In-App-Nachricht-Umfragen
- Der Landing-Page-Analytics-Ansicht für Landing-Page-Umfragen
{% endif %}

Übergeordnete Analytics umfassen:

- **All responses:** Gesamtzahl vollständiger und unvollständiger Antworten
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

Für Optionsfeld-, Dropdown- und Kontrollkästchen-Formularblöcke können Sie in der Umfrage-Analytics-Ansicht zwischen drei Chart-Typen wählen. Dies gibt Ihnen mehr Flexibilität, Insights zu interpretieren und zu teilen, ohne in ein Drittanbieter-Tool exportieren zu müssen.

| Chart-Typ | Geeignet für |
| --- | --- |
| Balkendiagramm | Die standardmäßige horizontale Ansicht von Antwortanzahlen und Prozentsätzen. |
| Säulendiagramm | Eine vertikale Ansicht von Antwortanzahlen und Prozentsätzen. Verwenden Sie dieses Chart, um Antworten nebeneinander zu vergleichen, insbesondere bei Mehrfachauswahl-Fragen oder Fragen mit mehr Antwortoptionen. |
| Kreisdiagramm | Eine proportionale Aufschlüsselung der Antworten. Verwenden Sie dieses Chart für Einzelauswahl-Fragen, wenn Sie sehen möchten, wie sich die Antworten auf die Optionen verteilen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umfrage-Chart-Typen" }

Jedes Chart wird in Echtzeit aktualisiert, sobald Antworten eingehen. Sie können den Chart-Typ jederzeit wechseln, ohne die zugrunde liegenden Daten zu beeinflussen.

![Aufschlüsselung auf Fragenebene einer Umfrage als Balkendiagramm.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Retargeting und Triggern {#retarget-and-trigger}

Während des Early Access können Sie:

- Nutzer:innen nach Umfrageantworten segmentieren, die als Nutzerattribute protokolliert wurden.
- Nutzer:innen nach dem Abschlussstatus der Umfrage segmentieren.

{% if include.channel == 'in_app_message' %}

![Trigger-Einrichtung und Segmentierungsfilter für Umfrage-Follow-up.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage in einer In-App-Nachricht-Campaign abschließen.

![Trigger-Einrichtung und Segmentierungsfilter für Follow-up einer In-App-Nachricht-Campaign-Umfrage.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Trigger-Einrichtung und Segmentierungsfilter für Follow-up einer Landing-Page-Umfrage.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage auf einer Landing-Page abschließen.

{% else %}

![Trigger-Einrichtung und Segmentierungsfilter für Umfrage-Follow-up.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage auf einer Landing-Page oder in einer In-App-Nachricht-Campaign abschließen.

![Trigger-Einrichtung und Segmentierungsfilter für Follow-up einer Landing-Page-Umfrage.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Trigger-Einrichtung und Segmentierungsfilter für Follow-up einer In-App-Nachricht-Campaign-Umfrage.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Einschränkungen {#limitations}

Während des Early Access gelten die folgenden Einschränkungen:

- Sie können Nutzer:innen nicht nach Langtext-Antworten segmentieren.
- Frage-und-Antwort-basiertes Triggern, das nicht auf protokollierten Nutzerattributen basiert, ist nicht verfügbar.