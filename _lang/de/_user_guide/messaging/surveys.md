---
nav_title: Umfragen
article_title: Umfragen
page_order: 9
page_type: reference
channel:
  - landing pages
  - in-app messages
description: "Erfahren Sie, wie Sie mit Braze-Umfragen First-Party-Feedback über Landing-Pages und In-App-Nachrichten erfassen können, einschließlich Analytics, Formularblöcke und Currents-Export."
---

# Umfragen {#surveys}

> Braze-Umfragen ermöglichen es Ihnen, First-Party-Feedback direkt von Ihren Nutzer:innen zu erfassen und in Folge-Nachrichten darauf zu reagieren – ohne das Braze-Dashboard zu verlassen. Nutzen Sie Umfragen, um die Stimmung Ihrer Nutzer:innen zu verstehen, Präferenzen zu erfassen und Segmente sowie Trigger auf Basis der gesammelten Antworten zu erstellen.


## Kanalverfügbarkeit {#channel-availability}

Umfragen sind auf zwei Kanälen verfügbar. Jede Kanalseite behandelt den kanalspezifischen Erstellungsablauf, die Gestaltung und den Reporting-Standort, während diese Seite die Konzepte und Funktionen abdeckt, die für beide gelten.

| Kanal | Umfragen erstellen in |
| --- | --- |
| Landing-Pages | [Landing-Page-Umfragen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| In-App-Nachrichten | [In-App-Nachricht-Umfragen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbarkeit von Umfragekanälen" }

## Umfragenseite {#surveys-page}

Gehen Sie zu **Messaging** > **Surveys**, um Umfragen über Landing-Pages, Campaigns und Canvases an einem Ort zu finden. Nutzen Sie diese Seite als Einstiegspunkt, um die Performance Ihrer Umfragen kanalübergreifend zu überprüfen.

{% alert note %}
Wenn **Surveys** unter **Messaging** nicht angezeigt wird, wenden Sie sich an Ihren Braze Account Manager.
{% endalert %}

## Analytics {#analytics}

Jeder Umfrage-Fragetyp enthält standardmäßig erweitertes Reporting, sodass Sie Antwortdaten auf einen Blick überprüfen können, ohne zuerst ein Segment zu erstellen oder einen Export in ein separates Tool durchzuführen.

Übergeordnete Analytics umfassen:

- **Alle Antworten:** Gesamtanzahl vollständiger und unvollständiger Antworten
- **Abgeschlossen:** Nutzer:innen, die alle Pflichtfragen beantwortet haben
- **Teilweise abgeschlossen:** Nutzer:innen, die einige Daten übermittelt, aber nicht alle Pflichtfragen beantwortet haben
- **Eindeutige Impressionen:** Gesamtanzahl der Seitenaufrufe

![Seite mit Umfrageantworten, die NPS-Score-Analytics mit Promoter-, Passiv- und Detractor-Prozentsätzen sowie ein horizontales Balkendiagramm der Score-Verteilung zeigt.]({% image_buster /assets/img/surveys/survey_responses.png %})

### Diagrammtypen {#chart-types}

Für Optionsfeld-, Dropdown- und Checkbox-Formularblöcke können Sie in der Umfrage-Analytics-Ansicht zwischen drei Diagrammtypen wählen. Dies gibt Ihnen mehr Flexibilität bei der Interpretation und Weitergabe von Insights, ohne in ein Drittanbieter-Tool exportieren zu müssen.

| Diagrammtyp | Geeignet für |
| --- | --- |
| **Balkendiagramm** | Die standardmäßige horizontale Ansicht von Antwortanzahlen und -prozentsätzen. |
| **Säulendiagramm** | Eine vertikale Ansicht von Antwortanzahlen und -prozentsätzen. Verwenden Sie dieses Diagramm, um Antworten nebeneinander zu vergleichen, insbesondere bei Mehrfachauswahl-Fragen oder Fragen mit mehr Antwortoptionen. |
| **Kreisdiagramm** | Eine proportionale Aufschlüsselung der Antworten. Verwenden Sie dieses Diagramm bei Einzelauswahl-Fragen, wenn Sie sehen möchten, wie die Antworten über die Optionen verteilt sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umfrage-Diagrammtypen" }

Jedes Diagramm zeigt Echtzeitdaten, sobald Antworten eingehen. Sie können den Diagrammtyp jederzeit wechseln, ohne die zugrunde liegenden Daten zu beeinflussen.

![Aufschlüsselung einer Umfragefrage auf Fragenebene als Balkendiagramm.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Mehrstufige Landing-Page-Formulare {#multi-step-landing-page-forms}

Erstellen Sie eine Umfrage als einzelne Landing-Page mit mehreren Schritten, die automatisch miteinander verknüpft werden, anstatt mehrere eigenständige Landing-Pages zu erstellen und manuell zu verlinken. So können Sie beispielsweise separate Schritte für jede Umfragefrage sowie einen Bestätigungsschritt am Ende definieren.

Diese Funktion ist spezifisch für den Landing-Pages-Kanal. In-App-Nachricht-Umfragen unterstützen ebenfalls einen Seitenmanager zum Wechseln zwischen Schritten; Details finden Sie unter [In-App-Nachricht-Umfrage erstellen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey).

![Landing-Page-Editor mit einer mehrstufigen Formularvorschau und dem Formulareigenschaften-Panel, das die Schritte und einen gesperrten Bestätigungsschritt auflistet.]({% image_buster /assets/img/surveys/multi_step.png %})

## Frage- und Formularblöcke {#question-and-form-blocks}

Landing-Pages und In-App-Nachrichten unterstützen alle ihre Standard-Formularblöcke auch in Umfragen, einschließlich Optionsfeldgruppe, Checkbox, Checkbox-Gruppe, Dropdown, Telefonnummernerfassung, E-Mail-Erfassung und Kurztexterfassung. Dieser Abschnitt hebt die drei Formularblöcke hervor, die speziell für Umfragen entwickeltes Reporting bieten: NPS, Zahlenskala und Langtext.

{% tabs local %}
{% tab NPS %}
### Eigenständiger NPS-Block {#standalone-nps-block}

Der **NPS**-Block ist ein separater Formularblock, der sich vom **Bewertungs**-Block (Zahlenskala) unterscheidet und keine Konfigurationsoption innerhalb dieses Blocks ist. Fügen Sie ihn einer Umfrage hinzu, um die standardmäßige Net Promoter Score-Frage (0–10) zu stellen und Reporting zu erhalten, das speziell für diesen Anwendungsfall entwickelt wurde.

Der **NPS**-Block bietet besseres Dashboard-Reporting als eine einfache Bewertungsfrage, die für denselben Zweck verwendet wird. Anstelle einer einfachen Zählung der Antworten pro Zahl gruppiert Braze die Antworten automatisch in Promoter (9–10), Passive (7–8) und Detractors (0–6) und zeigt diese Segmente – und den resultierenden NPS-Score – direkt in der Umfrage-Analytics-Ansicht an.

Currents exportiert den numerischen Score (und, falls hinzugefügt, das Freitext-Feedback-Feld) über das **Survey Response**-Ereignis. Promoter-, Passiv- und Detractor-Segmente sind keine separaten Currents-Felder.

![Eine mobile NPS-Umfrage neben dem Dashboard für Umfrageantworten, das einen NPS-Score mit Promoter-, Passiv- und Detractor-Aufschlüsselungen sowie ein Diagramm zur Antwortverteilung zeigt.]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab Zahlenskala %}
### Zahlenskala-Fragen {#number-scale-questions}

Auf den Kanalseiten auch als Bewertungsskala bezeichnet; beide Begriffe beziehen sich auf denselben **Bewertungs**-Formularblock. Erfassen Sie Zahlenskala-Fragen mit 1–5, 1–10 oder 0–10, um verschiedene Umfrage- und Reporting-Anforderungen abzudecken – von einfachen Zufriedenheitsbewertungen bis hin zu Weiterempfehlungs-Scores. Kanalspezifische Screenshots zur Gestaltung finden Sie im Abschnitt zur Bewertungsskala auf der Seite [Landing-Page-Umfragen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) oder [In-App-Nachricht-Umfragen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale).

Sie können eine Bewertung als Umfrageantwort erfassen, sie als ganzzahliges angepasstes Attribut protokollieren oder beides. Kombinieren Sie eine Zahlenskala-Frage mit einem [Langtext-Erfassungsblock](#long-form-text-capture), um einen numerischen Score zusammen mit qualitativem Feedback in derselben Umfrage zu erfassen.

![Landing-Page-Umfrage-Editor mit einer ausgewählten 1–5-Bewertungsfrage und dem geöffneten Bewertungseigenschaften-Panel auf der rechten Seite.]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab Langtext %}
### Langtext-Erfassung {#long-form-text-capture}

Die Langtext-Erfassung ist nützlich für qualitatives Feedback. Sie können die minimale und maximale Zeichenanzahl (bis zu 1.000 Zeichen) konfigurieren, ob das Zeichenlimit bei der Eingabe angezeigt werden soll, die Höhe des Textbereichs und den Platzhaltertext.

![Einstellungen für den Langtext-Erfassungsblock.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

Langtext-Antworten sind im Reporting und in Exporten verfügbar, können aber nicht als angepasste Attribute im Nutzerprofil protokolliert werden – Sie können Nutzer:innen also nicht direkt nach einem Langtext-Antwortwert segmentieren. Details finden Sie unter [Einschränkungen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations) auf der jeweiligen Kanalseite.

In Currents verwenden Langtext-Antworten `answer_type = 'free_form_text'` mit dem Text in `answer_long_string`.
{% endtab %}
{% endtabs %}

## Zufällige Reihenfolge der Antwortoptionen {#randomized-choice-order}

Optionsfeldgruppen, Checkbox-Gruppen und Dropdown-Blöcke unterstützen eine zufällige Reihenfolge der Antwortoptionen. Aktivieren Sie **Randomize choice order**, um die Auswahlmöglichkeiten bei jedem Laden der Umfrage zu mischen. So wird der Reihenfolge-Bias reduziert, wenn sonst immer dieselbe erste Option die Antworten verzerren könnte.

Die Randomisierung ändert nur die Anzeigereihenfolge für die jeweilige umfrageteilnehmende Person. Reporting-Labels und -Werte bleiben den von Ihnen konfigurierten Auswahlmöglichkeiten zugeordnet, sodass Analytics, CSV-Exporte und Segmentierung unabhängig von der Reihenfolge, die ein:e bestimmte:r Nutzer:in gesehen hat, dieselben Antwortdaten verwenden.

## Umfrage-Templates {#survey-templates}

Speichern Sie eine Umfrage als Template aus der Landing-Page- oder In-App-Nachricht-Template-Bibliothek, damit Ersteller:innen damit starten können, anstatt jedes Mal dieselben Fragen und Formularblöcke neu zu erstellen. Wenn Umfrage-Templates für Ihren Workspace aktiviert sind, filtern Sie die Bibliothek nach **Survey**, um gespeicherte Umfragestrukturen über Campaigns, Canvases und Landing-Pages hinweg zu finden und wiederzuverwenden.

## Survey-Response-Ereignisse {#survey-response-events}

Umfrageantworten fließen in [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), sodass Sie Umfragedaten in Ihr Data Warehouse oder ein BI-Tool eines Drittanbieters exportieren können – für nachgelagerte Analysen, Verknüpfungen mit anderen Engagement-Daten und benutzerdefiniertes Reporting, das über die integrierten Analytics des Dashboards hinausgeht.

Braze exportiert einzelne Umfrageantworten über das **Survey Response**-Ereignis (`users.messages.survey.Response`) an Currents. Jedes Ereignis repräsentiert die Antwort einer umfrageteilnehmenden Person auf eine Umfragefrage. Die vollständige Feldreferenz finden Sie unter [Survey-Response-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) im Currents-Ereignisglossar.

## Landing-Page-Engagement-Funnel {#landing-page-engagement-funnel}

Landing-Page-Umfragen generieren auch **Landing Page Impression**- und **Landing Page Click**-Ereignisse für Seitenaufrufe und getrackte Klicks. Das Abschließen einer Landing-Page-Umfrage schreibt ein **Survey Response**-Ereignis; es löst nicht zusätzlich das generische **Landing Page Form Submission**-Ereignis aus, das für Standard-Landing-Page-Formulare (ohne Umfrage) vorgesehen ist. Die vollständige Feldreferenz für diese Ereignisse finden Sie im [Currents-Ereignisglossar]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Verwandte Artikel {#related-articles}

- [Landing-Page-Umfragen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys): Erstellungsablauf, Gestaltung und Reporting für den Landing-Pages-Kanal
- [In-App-Nachricht-Umfragen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys): Erstellungsablauf, Gestaltung und Reporting für den In-App-Nachrichten-Kanal
- [Drag-and-Drop-Editor-Blöcke]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks): Vollständige Referenz der Formularblöcke, die Sie einer Umfrage hinzufügen können
- [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents): Datenexport in Ihr Warehouse oder BI-Tool einrichten