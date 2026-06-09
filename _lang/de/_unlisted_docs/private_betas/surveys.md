---
nav_title: Umfragen
article_title: Braze-Umfragen
description: "Erfahren Sie, wie Sie Umfragen in In-App-Nachrichten und Landing-Pages erstellen, Antworten auswerten und Nutzer:innen während der geschlossenen Beta retargeten."
permalink: /braze_surveys/
hidden: true
---

# Braze-Umfragen {#braze-surveys}

> Braze-Umfragen sammeln Feedback in In-App-Nachrichten und Landing-Pages, das Sie analysieren und für Folgenachrichten nutzen können.

{% alert important %}
Braze-Umfragen befinden sich in der geschlossenen Beta. Senden Sie Ihr Feedback zur Beta an [surveys-feedback@braze.com](mailto:surveys-feedback@braze.com).
{% endalert %}

## Voraussetzungen {#prerequisites}

Bevor Sie eine Umfrage erstellen, müssen Sie:

- Zugang zu Landing-Pages, In-App-Nachrichten oder beidem in Ihrem Braze-Workspace haben
- Mit dem [Erstellen von Landing-Pages](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/) vertraut sein
- Mit dem [Erstellen von Drag-and-Drop-In-App-Nachrichten](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) vertraut sein

## Umfrage erstellen {#create-a-survey}

Während der Beta werden Umfragen innerhalb Ihres bestehenden Nachrichtenkompositions-Flows erstellt.

1. Gehen Sie zu **Messaging** > **Landing-Pages**, oder erstellen Sie eine [In-App-Nachricht](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/) in einer Campaign oder einem Canvas.
2. Erstellen Sie eine neue Nachricht.
3. Wählen Sie **Survey** als Ihren Nachrichtentyp aus.

## In-App-Nachricht-Umfrage verfassen {#compose-an-in-app-message-survey}

In-App-Nachricht-Umfragen enthalten standardmäßig zwei Seiten:

- **Seite 1**, auf der Nutzer:innen Fragen beantworten
- **Bestätigungsseite**, auf der die Umfrage abgesendet wird

Standardmäßig sind Buttons mit **Nächste Seite** verknüpft. Um dieses Verhalten zu ändern, aktualisieren Sie jeden Button im **Aktionen**-Panel.

![Seitenfluss und Aktionseinstellungen einer In-App-Nachricht-Umfrage.]({% image_buster /assets/unlisted_docs/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

## Umfrage-Formularblöcke verwenden {#use-survey-form-blocks}

Informationen zu gemeinsamen Stil- und Kompositionssteuerungen finden Sie unter:

- [Editor-Blöcke des Drag-and-Drop-Editors für In-App-Nachrichten](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)
- [Formularblöcke für Landing-Pages](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)

Sie können die folgenden Formularblöcke zu Umfragen hinzufügen:

- Telefonnummernerfassung
- E-Mail-Erfassung
- Optionsfeldgruppe
- Kurztexterfassung
- Langtexterfassung
- Dropdown
- Einzelnes Kontrollkästchen
- Kontrollkästchengruppe

### Langtexterfassung {#long-text-capture}

Die Langtexterfassung eignet sich für qualitatives Feedback.

Sie können Folgendes konfigurieren:

- Minimale und maximale Zeichenanzahl (bis zu 1.000)
- Ob Zeichenlimits während der Komposition angezeigt werden sollen
- Höhe des Textbereichs (Zeilen)
- Platzhaltertext

Während der Beta sind Langtextantworten in Berichten und Exporten verfügbar, können aber nicht als angepasste Attribute im Nutzerprofil protokolliert werden.

![Einstellungen des Langtexterfassungsblocks.]({% image_buster /assets/unlisted_docs/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Pflichtfelder und Attribute konfigurieren {#configure-required-fields-and-attributes}

Geben Sie für jeden Formularblock im Einstellungspanel auf der rechten Seite einen **Bezeichner für Berichte** ein. Dieser Bezeichner erscheint in Umfrageberichten und CSV-Exporten.

Während der Beta:

- Sie können die meisten Umfrageantworten als angepasste Attribute im Nutzerprofil protokollieren.
- Langtextantworten können nicht als angepasste Attribute protokolliert werden.
- Wenn Sie eine Antwort nicht als Nutzer:innen-Attribut protokollieren, können Sie Nutzer:innen nicht nach diesem Antwortwert segmentieren.

![Einstellungen für Berichtsbezeichner und Attributprotokollierung.]({% image_buster /assets/unlisted_docs/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Berichte und Analytics einsehen {#view-reporting-and-analytics}

Überprüfen Sie nach dem Start die Ergebnisse in:

- Dem Tab **Antworten** für In-App-Nachricht-Umfragen
- Der Analytics-Ansicht der Landing-Page für Landing-Page-Umfragen

![Analytics-Tab der Landing-Page.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-1.png %})

Übergeordnete Analytics umfassen:

- **Alle Antworten:** Gesamtzahl vollständiger und unvollständiger Antworten
- **Abgeschlossen:** Nutzer:innen, die alle Pflichtfragen beantwortet haben
- **Teilweise abgeschlossen:** Nutzer:innen, die einige Daten übermittelt, aber nicht alle Pflichtfragen beantwortet haben
- **Eindeutige Impressionen:** Gesamtzahl der Seitenaufrufe

{% alert note %}
Landing-Page-Umfragen erfassen während der Beta keine teilweise abgeschlossenen Antworten.
{% endalert %}

Sie können auch Aufschlüsselungen der Antworten pro Frage einsehen und Daten als CSV exportieren.

![Übersicht der Umfrage-Analytics und Aufschlüsselung auf Fragenebene.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-text.png %})

![Balkendiagramme der Aufschlüsselung auf Fragenebene.]({% image_buster /assets/unlisted_docs/img/surveys/bar-charts-1.png %})

## Retargeting und Trigger {#retarget-and-trigger}

Während der Beta können Sie:

- Nutzer:innen nach Umfrageantworten segmentieren, die als Nutzer:innen-Attribute protokolliert wurden.
- Nutzer:innen nach dem Abschlussstatus der Umfrage segmentieren. <br><br>![Trigger-Einrichtung und Segmentierungsfilter für Umfrage-Follow-up.]({% image_buster /assets/unlisted_docs/img/surveys/submit-survey-segment.png %})<br><br>
- Campaigns und Canvases triggern, wenn Nutzer:innen eine Umfrage in einer Landing-Page oder einer In-App-Nachricht-Campaign abschließen. <br><br>![Trigger-Einrichtung und Segmentierungsfilter für Landing-Page-Umfrage-Follow-up.]({% image_buster /assets/unlisted_docs/img/surveys/trigger_landing_page_survey.png %}) <br><br>![Trigger-Einrichtung und Segmentierungsfilter für In-App-Nachricht-Campaign-Umfrage-Follow-up.]({% image_buster /assets/unlisted_docs/img/surveys/interact-campaign-step.png %})

### Einschränkungen {#limitations}

Während der Beta gelten die folgenden Einschränkungen:

- Sie können Nutzer:innen nicht nach Langtext-Antworten segmentieren.
- Frage-und-Antwort-Trigger, die nicht auf protokollierten Nutzer:innen-Attributen basieren, sind nicht verfügbar.