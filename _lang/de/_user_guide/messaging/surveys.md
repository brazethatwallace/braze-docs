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

Umfragen sind auf zwei Kanälen verfügbar. Jede Kanalseite behandelt den kanalspezifischen Erstellungsablauf, die Gestaltung und den Standort der Berichte, während diese Seite die Konzepte und Funktionen abdeckt, die für beide gelten.

| Kanal | Umfragen erstellen in |
| --- | --- |
| Landing-Pages | [Landing-Page-Umfragen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| In-App-Nachrichten | [In-App-Nachricht-Umfragen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kanalverfügbarkeit von Umfragen" }

## Umfragen-Seite {#surveys-page}

Gehen Sie zu **Messaging** > **Umfragen**, um Umfragen über Landing-Pages, Campaigns und Canvases an einem Ort zu finden. Nutzen Sie diese Seite als Ausgangspunkt, um die Performance Ihrer Umfragen kanalübergreifend zu überprüfen.

{% alert note %}
Wenn **Umfragen** nicht unter **Messaging** angezeigt wird, wenden Sie sich an Ihren Braze Account Manager.
{% endalert %}

## Analytics {#analytics}

Jeder Umfrage-Fragetyp enthält standardmäßig eine erweiterte Auswertung, sodass Sie die Antwortdaten auf einen Blick überprüfen können, ohne zuerst ein Segment erstellen oder in ein separates Tool exportieren zu müssen.

Die übergeordneten Analytics umfassen:

- **Alle Antworten:** Gesamtzahl der vollständigen und unvollständigen Antworten
- **Abgeschlossen:** Nutzer:innen, die alle Pflichtfragen beantwortet haben
- **Teilweise abgeschlossen:** Nutzer:innen, die einige Daten übermittelt, aber nicht alle Pflichtfragen beantwortet haben
- **Eindeutige Impressionen:** Gesamtzahl der Seitenaufrufe

![Seite mit Umfrageantworten, die NPS-Analyse mit Promoter-, Passiv- und Detractor-Prozentsätzen sowie ein horizontales Balkendiagramm der Bewertungsverteilung zeigt.]({% image_buster /assets/img/surveys/survey_responses.png %})

### Chart-Typen {#chart-types}

Für Radiobutton-, Dropdown- und Checkbox-Formularblöcke können Sie in der Umfrage-Analytics-Ansicht zwischen drei Chart-Typen wählen. So können Sie Insights flexibler interpretieren und teilen, ohne in ein Drittanbieter-Tool exportieren zu müssen.

| Chart-Typ | Geeignet für |
| --- | --- |
| **Balkendiagramm** | Die standardmäßige horizontale Darstellung von Antwortanzahlen und -prozentsätzen. |
| **Säulendiagramm** | Eine vertikale Darstellung von Antwortanzahlen und -prozentsätzen. Verwenden Sie dieses Chart, um Antworten nebeneinander zu vergleichen – besonders bei Mehrfachauswahl-Fragen oder Fragen mit mehr Antwortoptionen. |
| **Kreisdiagramm** | Eine proportionale Aufschlüsselung der Antworten. Verwenden Sie dieses Chart bei Einfachauswahl-Fragen, wenn Sie sehen möchten, wie sich die Antworten auf die Optionen verteilen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umfrage-Chart-Typen" }

Jedes Chart zeigt Echtzeitdaten an, sobald Antworten eingehen. Sie können jederzeit zwischen den Chart-Typen wechseln, ohne die zugrunde liegenden Daten zu beeinflussen.

![Aufschlüsselung auf Frageebene einer Umfrage als Balkendiagramm.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Mehrstufige Landing-Page-Formulare {#multi-step-landing-page-forms}

Erstellen Sie eine Umfrage als einzelne Landing-Page mit mehreren Schritten, die automatisch miteinander verknüpft werden, anstatt mehrere eigenständige Landing-Pages zu erstellen und manuell zu verlinken. Zum Beispiel können Sie für jede Umfragefrage einen eigenen Schritt definieren und am Ende einen Bestätigungsschritt hinzufügen.

Diese Funktion ist spezifisch für den Landing-Page-Kanal. In-App-Nachricht-Umfragen unterstützen ebenfalls einen Seitenmanager zum Wechseln zwischen Schritten; weitere Informationen finden Sie unter [In-App-Nachricht-Umfrage erstellen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey).

![Landing-Page-Editor mit einer mehrstufigen Formularvorschau und dem Formulareigenschaften-Panel, das die Schritte und einen gesperrten Bestätigungsschritt auflistet.]({% image_buster /assets/img/surveys/multi_step.png %})

## Frage- und Formularblöcke {#question-and-form-blocks}

Landing-Pages und In-App-Nachrichten unterstützen in Umfragen alle standardmäßigen Formularblöcke, darunter Optionsfeldgruppen, Kontrollkästchen, Kontrollkästchengruppen, Dropdowns, Telefonnummernerfassung, E-Mail-Erfassung und Kurztexterfassung. Dieser Abschnitt beschreibt die drei Formularblöcke mit speziell für Umfragen entwickeltem Reporting: NPS, Zahlenskala und Langtext.

{% tabs local %}
{% tab NPS %}
### Eigenständiger NPS-Block {#standalone-nps-block}

Der **NPS**-Block ist ein separater Formularblock, der sich vom **Bewertungs**-Block (Zahlenskala) unterscheidet – er ist keine Konfigurationsoption innerhalb dieses Blocks. Fügen Sie ihn einer Umfrage hinzu, um die standardmäßige Net Promoter Score-Frage (0–10) zu stellen und ein speziell für diesen Anwendungsfall konzipiertes Reporting zu erhalten.

Der **NPS**-Block bietet Ihnen ein besseres Dashboard-Reporting als eine einfache Bewertungsfrage, die für denselben Zweck verwendet wird. Anstelle einer reinen Zählung der Antworten pro Zahl gruppiert Braze die Antworten automatisch in Promotoren (9–10), Passive (7–8) und Detraktoren (0–6) und zeigt diese Segmente – sowie den daraus resultierenden NPS-Score – direkt in der Umfrage-Analytics-Ansicht an.

Currents exportiert den numerischen Score (und, falls hinzugefügt, das Freitext-Feedbackfeld) im **Survey Response**-Ereignis. Die Segmente für Promotoren, Passive und Detraktoren sind keine separaten Currents-Felder.

![Eine mobile NPS-Umfrage neben dem Dashboard für Umfrageantworten, das einen NPS-Score mit Aufschlüsselungen nach Promotoren, Passiven und Detraktoren sowie ein Antwortverteilungsdiagramm zeigt.]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab Zahlenskala %}
### Zahlenskalafragen {#number-scale-questions}

Auf den Kanalseiten auch als Bewertungsskala bezeichnet; beide Begriffe beziehen sich auf denselben **Bewertungs**-Formularblock. Erfassen Sie Zahlenskalafragen von 1–5, 1–10 oder 0–10, um verschiedene Umfrage- und Reporting-Anforderungen abzudecken – von einfachen Zufriedenheitsbewertungen bis hin zu Weiterempfehlungswahrscheinlichkeiten. Kanalspezifische Kompositions-Screenshots finden Sie im Abschnitt „Bewertungsskala“ auf der Seite [Landing-Page-Umfragen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) oder [In-App-Nachricht-Umfragen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale).

Sie können eine Bewertung als Umfrageantwort erfassen, als ganzzahliges angepasstes Attribut protokollieren oder beides. Kombinieren Sie eine Zahlenskalafrage mit einem [Langtext-Erfassungsblock](#long-form-text-capture), um in derselben Umfrage einen numerischen Score zusammen mit qualitativem Feedback zu erheben.

![Landing-Page-Umfrageeditor mit einer ausgewählten 1–5-Bewertungsfrage und dem geöffneten Panel „Bewertungseigenschaften“ auf der rechten Seite.]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab Langtext %}
### Langtext-Erfassung {#long-form-text-capture}

Die Langtext-Erfassung eignet sich für qualitatives Feedback. Sie können die minimale und maximale Zeichenanzahl (bis zu 1.000 Zeichen) konfigurieren, ob das Zeichenlimit während der Komposition angezeigt werden soll, die Höhe des Textbereichs und den Platzhaltertext.

![Einstellungen des Langtext-Erfassungsblocks.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

{% alert important %}
Langtextfelder in iOS-In-App-Nachricht-Umfragen sind vorübergehend auf 250 Zeichen begrenzt. Diese Einschränkung wird in einem zukünftigen iOS-SDK-Update behoben. Bis dahin empfiehlt es sich, die maximale Zeichenanzahl für Umfragen, die iOS-Nutzer:innen angezeigt werden, bei 250 oder darunter zu halten.
{% endalert %}

Langtextantworten stehen im Reporting und in Exporten zur Verfügung, können jedoch nicht als angepasste Attribute im Kundenprofil protokolliert werden – Sie können Nutzer:innen also nicht direkt nach einem Langtext-Antwortwert segmentieren. Weitere Informationen finden Sie unter [Einschränkungen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations) auf der jeweiligen Kanalseite.

In Currents verwenden Langtextantworten `answer_type = 'free_form_text'` mit dem Text in `answer_long_string`.
{% endtab %}
{% endtabs %}

## Zufällige Reihenfolge der Auswahlmöglichkeiten {#randomized-choice-order}

Optionsfeld-Gruppen, Checkbox-Gruppen und Dropdown-Blöcke unterstützen eine zufällige Anordnung der Antwortmöglichkeiten. Aktivieren Sie **Randomize choice order**, um die Auswahlmöglichkeiten bei jedem Laden der Umfrage zufällig zu mischen. So wird eine Reihenfolge-Verzerrung vermieden, die entstehen kann, wenn dieselbe erste Option die Antworten systematisch beeinflusst.

Die Randomisierung ändert nur die Anzeigereihenfolge für die jeweilige Person, die an der Umfrage teilnimmt. Reporting-Labels und -Werte bleiben den von Ihnen konfigurierten Auswahlmöglichkeiten zugeordnet, sodass Analytics, CSV-Exporte und Segmentierung dieselben Antwortdaten verwenden – unabhängig davon, in welcher Reihenfolge die Optionen angezeigt wurden.

## Umfrage-Templates {#survey-templates}

Speichern Sie eine Umfrage als Template aus der Landing-Page- oder In-App-Nachricht-Template-Bibliothek, damit andere direkt davon starten können, anstatt jedes Mal dieselben Fragen und Formular-Blöcke neu zu erstellen. Wenn Umfrage-Templates für Ihren Workspace aktiviert sind, filtern Sie die Bibliothek nach **Survey**, um gespeicherte Umfrage-Strukturen für Campaigns, Canvases und Landing-Pages zu finden und wiederzuverwenden.

## Umfrageantwort-Ereignisse {#survey-response-events}

Umfrageantworten fließen in [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ein, sodass Sie Umfragedaten in Ihr Data Warehouse oder ein BI-Tool eines Drittanbieters exportieren können – für weiterführende Analysen, Verknüpfungen mit anderen Engagement-Daten und angepasstes Reporting über die im Dashboard integrierten Analytics hinaus.

Braze exportiert einzelne Umfrageantworten über das **Umfrageantwort**-Ereignis (`users.messages.survey.Response`) an Currents. Jedes Ereignis repräsentiert die Antwort einer/eines Befragten auf eine Umfragefrage. Die vollständige Feldreferenz finden Sie unter [Umfrageantwort-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) im Currents-Ereignis-Glossar.

## Engagement-Funnel für Landing-Pages {#landing-page-engagement-funnel}

Landing-Page-Umfragen erzeugen außerdem **Landing Page Impression**- und **Landing Page Click**-Ereignisse für Seitenaufrufe und getrackte Klicks. Das Abschließen einer Landing-Page-Umfrage schreibt ein **Survey Response**-Ereignis; es wird dabei nicht zusätzlich das generische **Landing Page Form Submission**-Ereignis ausgelöst, das für Standard-Landing-Page-Formulare (ohne Umfrage) vorgesehen ist. Die vollständige Feldreferenz für diese Ereignisse finden Sie im [Currents-Ereignisglossar]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Verwandte Artikel {#related-articles}

- [Landing-Page-Umfragen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys): Erstellungsablauf, Gestaltung und Reporting für den Landing-Page-Kanal
- [In-App-Nachricht-Umfragen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys): Erstellungsablauf, Gestaltung und Reporting für den In-App-Nachrichten-Kanal
- [Drag-and-Drop-Editor-Blöcke]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks): Vollständige Referenz für die Formularblöcke, die Sie einer Umfrage hinzufügen können
- [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents): Richten Sie den Datenexport in Ihr Data Warehouse oder BI-Tool ein