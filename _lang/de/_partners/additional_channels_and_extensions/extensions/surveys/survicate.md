---
nav_title: Survicate
article_title: Survicate
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Survicate, einer Plattform für Kundenfeedback, die Ihnen hilft, Insights von Kund:innen über mehrere Kanäle und während der gesamten Customer Journey zu sammeln, zu analysieren und zu nutzen."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) ist eine Plattform für Kundenfeedback, die Insights von Kund:innen über mehrere Kanäle und über die gesamte Customer Journey hinweg sammelt, analysiert und auswertet. [Sehen Sie sich eine kurze Demo an](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_Diese Integration wird von Survicate gepflegt._

## Über die Integration {#about-the-integration}

Nutzen Sie die native Integration von Survicate und Braze, um Antworten auf E-Mail-, In-App-, Mobil- oder Web-Umfragen mit Kundenprofilen von Braze zu synchronisieren. Umfrageantworten werden automatisch mit Braze-Nutzerprofilen als angepasste Attribute oder Events synchronisiert. Insights zu Echtzeit-Feedback erleichtern das Tracking und die Analyse von Feedback zusammen mit Kundendaten sowie die Erstellung von Targeting-Follow-ups und hyper-personalisierten Segmenten.

## Anwendungsfälle {#use-cases}

Braze und Survicate arbeiten zusammen, um eine Reihe von Feedback-Anwendungsfällen abzudecken und Ihnen dabei zu helfen, umsetzbare Insights der Nutzer:innen zu sammeln und das Kundenerlebnis zu verbessern:

- Verbessern Sie die Beantwortungsquoten von Umfragen mit eingebetteten Umfragen, die direkt aus dem Posteingang beantwortet werden können.
- Sammeln Sie Insights in kritischen Phasen der Customer Journey über Braze In-App Messages.
- Verwenden Sie in Survicate gespeichertes Feedback, um intelligentere Segmente in Braze zu erstellen.
- Automatisieren Sie Folgekampagnen auf der Grundlage des Feedbacks von Kund:innen.
- Nutzen Sie Insights von Kund:innen, um personalisierte Workflows zu triggern.
- Erreichen Sie eine breitere Zielgruppe mit automatisch übersetzten Umfragen.
- Senden Sie Events an Braze-Kontaktprofile, wenn jemand auf Ihre Umfrage antwortet.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Survicate-Konto | Sie benötigen ein Survicate-Konto, um diese Integration zu aktivieren. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit der Berechtigung `users.track`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** erstellt werden. |
| Braze REST-Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Die wichtigsten Features der Integration {#key-features-of-the-integration}

Die Integration von Survicate und Braze bietet eine Realtime-Datensynchronisation, sodass die aktuellsten Informationen aus Survicate-Umfragen sofort in Braze verfügbar sind. Auf der Grundlage der Umfrageantworten können Sie diese Daten nutzen, um zeitnahe, personalisierte Maßnahmen zu ergreifen.

- **Senden Sie Umfrageantworten als angepasste Attribute an Braze**: Reichern Sie die Nutzerprofile von Braze mit Daten aus Umfrageantworten an.
- **Triggern Sie angepasste Events in Braze**: Nutzen Sie Events, die auf Umfrageantworten basieren, um bestimmte Gruppen zu targeten oder Folgekampagnen zu initiieren.
- **Erstellen Sie detaillierte Segmente**: Erstellen Sie Segmente in Braze anhand von Daten aus Survicate-Umfragen, um Ihre Reichweite weiter zu personalisieren.

## Integration

### Erstellen Sie Ihre Umfragen in Survicate {#creating-your-surveys-in-survicate}

#### Betten Sie Ihre Umfrage in eine E-Mail ein oder erstellen Sie eine Umfrage mit teilbarem Link {#embed-your-survey-in-an-email-or-create-a-shareable-link-survey}

1.  Klicken Sie in Survicate auf **+ Create new survey**, wählen Sie eine beliebige Erstellungsmethode (ein Template, die KI-Umfrageerstellung oder das Hinzufügen eigener Fragen) und den Umfragetyp E-Mail oder Teilbarer Link:
![Braze wird im Umfrage-Ersteller ausgewählt.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2. Wählen Sie auf dem Tab „Konfigurieren“ der Umfrage **Braze** als das Tool aus, mit dem Sie die Befragten identifizieren möchten:
![Braze wird auf dem Tab „Konfigurieren“ der Umfrage ausgewählt.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3. Nachdem Sie Ihre Umfrage eingerichtet haben, gehen Sie auf den Tab „Teilen“ und entscheiden Sie, wie Sie Ihre Umfrage per E-Mail versenden möchten. Es gibt zwei Möglichkeiten: Sie können Ihre **Umfrage als Link** versenden oder **die erste Frage in die E-Mail einbetten**, sodass die Befragten direkt in der E-Mail mit der Beantwortung der Umfrage beginnen.

{% details Survey link option %}

1. Über den Button „Umfragelink kopieren“ können Sie einen Link zu Ihrer Umfrage erstellen:

![Über den Button „Umfragelink kopieren“ können Sie einen Link zu Ihrer Umfrage erstellen.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2. Verbergen Sie den Link zur Umfrage hinter einem CTA-Button oder einem Hyperlink in Ihrer Braze-E-Mail.

![Verbergen Sie den Link zur Umfrage hinter einem CTA-Button oder einem Hyperlink in Ihrer Braze-E-Mail.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

Zeigen Sie die erste Frage direkt im Textkörper der E-Mail an, um die Umfrage aus der E-Mail heraus zu starten. Die Befragten werden dann auf eine Landing-Page weitergeleitet, um den Rest der Umfrage auszufüllen.

1. Klicken Sie auf **Get email code** und dann auf **Copy the HTML code**:

![E-Mail-Code abrufen]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2. Gehen Sie zu der Braze-Kampagne, die Sie für die Umfrage verwenden möchten, klicken Sie auf **Edit email body** und fügen Sie einen HTML-Block zu Ihrem Template hinzu:

![HTML-Block-Code abrufen]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3. Ersetzen Sie den Code durch den Code, den Sie aus Ihrer Survicate-Umfrage kopiert haben. Sie sehen dann die erste Frage der Umfrage im Template:

![Ersetzen Sie den Code durch den Code, den Sie aus Ihrer Survicate-Umfrage kopiert haben]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4. Legen Sie den Zeitplan für die E-Mail fest, wählen Sie Ihre Zielgruppe, und Ihre Kampagne ist versandfertig.

{% enddetails %}

### Braze In-App-Nachrichten-Umfrage {#braze-in-app-message-survey}

1. Klicken Sie auf **+ Create new survey**, wählen Sie eine beliebige Erstellungsmethode (ein Template, die KI-Umfrageerstellung oder das Hinzufügen eigener Fragen) und wählen Sie dann „In-platform surveys“ und den Umfragetyp „Braze In-App Message“:

![Klicken Sie auf + Create new survey und wählen Sie eine beliebige Erstellungsmethode]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2. Starten Sie Ihre Braze In-App-Nachrichten-Umfrage, indem Sie zu Ihrem Braze-Konto navigieren und dann zu **Messaging** > **Campaigns** > **Kampagne erstellen** > **In-App-Nachricht**:
![Starten Sie Ihre Braze In-App-Nachrichten-Umfrage]({% image_buster /assets/img/survicate/survicate_9.gif %})

### Starten Sie Ihre Braze In-App-Messenger-Umfrage über den traditionellen Editor {#launch-your-braze-in-app-messenger-survey-via-the-traditional-editor}

1. Wenn Sie den traditionellen Editor verwenden, wählen Sie unter Nachrichtentyp die Option **Custom Code**:

![Wählen Sie „Custom Code“]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2. Fügen Sie dann den Code aus dem Tab „Launch“ Ihrer Umfrage in das HTML-Feld ein:

![Fügen Sie den Code aus dem Tab „Launch“ Ihrer Umfrage in das HTML-Feld ein]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Braze zeigt In-App-Nachrichten standardmäßig in einem Iframe an, während der Hintergrund der App blockiert ist. Um eine Interaktion mit Ihrer App zuzulassen, während Survicate-Umfragen erscheinen, müssen Sie:<br><br>

- `opts.useBrazeIframeClipper = true` zu Ihrem Survicate-Braze-Snippet hinzufügen.
- Das Paket `@survicate/braze-bridge-npm` ([Paket](https://www.npmjs.com/package/@survicate/braze-bridge-npm)) in der Datei installieren, in der Sie Braze initialisieren, und die Funktion `initBrazeBridge` verwenden.

Ein Beispiel-Snippet und eine React-Implementierung finden Sie [auf der Entwickler-Website von Survicate](https://developers.survicate.com/javascript/installation/#braze).
{% endalert %}

{: start="3"}
3. Richten Sie in Ihrer Braze-Kampagne die Schritte **Target** und **Assign** ein. Wenn Sie fertig sind, ist Ihre Kampagne startbereit. Im Schritt **Review** können Sie sehen, wie die Kampagne aussieht. Die Umfrage erscheint auf Ihrer Website an der Stelle, die im Survicate-Panel angegeben ist, wie oben beschrieben.

### Aktivierung der Braze-Integration {#enabling-the-braze-integration}

1. Um die Braze-Integration zu aktivieren, gehen Sie zu **Integrations**, suchen Sie nach „Braze“ und wählen Sie es aus.

![Braze auswählen]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2. Klicken Sie auf **Connect**, um die Autorisierung einzurichten.

3. Geben Sie den Workspace-API-Schlüssel Ihres Braze-Kontos und die URL der Braze-Instanz ein:

![Geben Sie den Workspace-API-Schlüssel Ihres Braze-Kontos und die URL der Braze-Instanz ein]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Um Survicate mit Braze zu verbinden, muss der Braze-API-Schlüssel über die Berechtigung `users.track` verfügen.
{% endalert %}

### Verbinden Sie Ihre Umfragen mit Braze {#connecting-your-surveys-to-braze}

Jetzt, da die Braze-Integration verbunden ist, können Sie individuelle Einstellungen für jede Umfrage vornehmen. Gehen Sie zu Ihrer Umfrage, wählen Sie den Tab **Connect** und wählen Sie **Braze** aus der Liste der verfügbaren Integrationen.

![Gehen Sie zu Ihrer Umfrage, wählen Sie den Tab „Connect“ und wählen Sie Braze]({% image_buster /assets/img/survicate/survicate_14.png %})

### Senden von Antworten an Braze als angepasste Attribute {#sending-responses-to-braze-as-custom-attributes}

Richten Sie Umfrageantworten so ein, dass sie als angepasste Attribute in Braze einfließen, wodurch Ihre Braze-Nutzerprofile mit gesammelten Daten angereichert werden.

1. Auf dem Tab „Einstellungen“ der Braze-Integration finden Sie den Abschnitt **Update fields**.

![Wählen Sie den Abschnitt „Update fields“]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2. Wählen Sie die Frage aus, deren Felder Sie aktualisieren möchten. Um eine Überflutung Ihrer Braze-Nutzerprofile mit Daten zu vermeiden, können Sie Antworten nur auf ausgewählte Fragen senden.

![Wählen Sie die Frage aus, deren Felder Sie aktualisieren möchten]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
Ranking- und Matrixfragen werden von dieser Braze-Integration nicht unterstützt.
{% endalert %}

{: start="3"}
3. Fügen Sie den Namen des angepassten Attributs, das Sie aktualisieren möchten, unter dem Feld **User** hinzu:

![Fügen Sie den Namen des angepassten Attributs, das Sie aktualisieren möchten, unter dem Feld „User“ hinzu]({% image_buster /assets/img/survicate/survicate_17.png %})

Standardmäßig sendet Survicate den Inhalt einer Umfrageantwort als Attributwert. Sie können die Beschriftung ändern, um sie kürzer zu machen oder an Ihre Datenstruktur anzupassen, indem Sie auf **Edit mapping** klicken, um diese Werte zu ändern:

![Umfrageantwort als Attributwert]({% image_buster /assets/img/survicate/survicate_18.png %})

![Klicken Sie auf „Edit mapping“, um diese Werte zu ändern]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
Für NPS sendet Survicate abgebildete Werte basierend auf der Antwortgruppe der NPS®-Frage. Wenn Sie jedoch numerische Werte empfangen möchten, können Sie die Option „Send Answers as 0-10 values“ aktivieren.
{% endalert %}

![Survicate sendet Werte, die auf der Grundlage der Antwortgruppe abgebildet werden]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4. Verbinden Sie weitere Fragen mit Ihrer Integration, indem Sie auf **+ Add new** klicken und die gleichen Schritte ausführen.

![Verbinden Sie weitere Fragen mit Ihrer Integration]({% image_buster /assets/img/survicate/survicate_21.png %})

### Senden von Events an die Profile von Braze-Kontakten {#sending-events-to-braze-contacts-profiles}

Abgesehen von den vorherigen Einstellungen kann Survicate jedes Mal, wenn ein:e Befragte:r eine Umfragefrage beantwortet, ein angepasstes Event in Braze namens `survicate-question-answered` senden.
Im Survicate-Panel können Sie unter „Antworten als angepasste Attribute senden“ wählen, ob Sie das Event für alle Fragen, für die im Tab „Update fields“ ausgewählten Fragen oder gar nicht senden möchten:

![Sie können wählen, ob Sie das Event für alle Fragen senden möchten]({% image_buster /assets/img/survicate/survicate_22.png %})

Wenn Sie sich für das Senden der Events entscheiden, können Sie in den Profilen der Nutzer:innen sehen, wie oft sie auf Survicate-Umfragen geantwortet haben und wann sie zuletzt geantwortet haben:

![Antworten]({% image_buster /assets/img/survicate/survicate_23.png %})

Das Event enthält Event-Eigenschaften mit der Antwort auf die Frage und Informationen über die Umfrage, die Frage und die befragte Person. Sie können dieses Event verwenden, um Segmente zu erstellen. Erstellen Sie zum Beispiel ein Segment von Nutzer:innen, die nach einem bestimmten Datum oder eine bestimmte Anzahl von Malen geantwortet haben:

![Das Event enthält Event-Eigenschaften mit der Antwort]({% image_buster /assets/img/survicate/survicate_24.png %})

Sie können diese Daten auch verwenden, wenn Sie eine Kampagne in Braze erstellen.

![Sie können diese Daten auch beim Erstellen einer Kampagne in Braze verwenden]({% image_buster /assets/img/survicate/survicate_25.png %})

### Testen Sie die Integration {#test-the-integration}

Wenn Sie Ihre Umfrage fertiggestellt und die Integration eingerichtet haben, können Sie sie testen, ohne Survicate zu verlassen. Klicken Sie dazu auf den Button **Test Integration** neben einem Attribut, Tag oder einer neuen Kontakteinrichtung, die Sie erstellt haben. Survicate erstellt einen Testkontakt (`braze-test@survicate.com`) in Ihrem Braze-Konto. Das Profil des Kontakts enthält aktualisierte Felder gemäß der Einrichtung.

![Klicken Sie auf den Button „Test Integration“]({% image_buster /assets/img/survicate/survicate_26.png %})

In Braze sehen Sie Beispieldaten aus den abgebildeten Feldern im Survicate-Dummy-Kontakt:

![Beispieldaten aus den abgebildeten Feldern im Survicate-Dummy-Kontakt]({% image_buster /assets/img/survicate/survicate_27.png %})

### Analyse der Ergebnisse Ihrer Umfrage {#analyzing-your-survey-results}

Nachdem Sie die Antworten über Ihre Braze-Umfrage gesammelt haben, ist es an der Zeit, das Feedback und die Insights Ihrer Befragten zu analysieren. Mit Survicate können Sie ganz einfach Ergebnisse, Statistiken und Trends überprüfen, um weitere Maßnahmen zu ergreifen.

### Feedback in Survicate

Nachdem Ihre Umfrage mit der Erfassung von Antworten begonnen hat, sehen Sie diese sofort im Tab „Analyze“ der Umfrage.

![Antworten im Tab „Analyze“]({% image_buster /assets/img/survicate/survicate_28.png %})

Der Tab „Analyze“ zeigt Ihnen die Gesamtergebnisse mit Statistiken und Daten im Zeitverlauf sowie die einzelnen Antworten, um jede Umfrageeinreichung im Detail zu betrachten.

### Feedback in Braze

Wenn Sie Nutzerfelder mit Umfrageantworten aktualisieren oder Antworten als angepasste Events senden, können Sie sehen, dass die Umfragedaten in Realtime synchronisiert werden. Gehen Sie in Braze zu einem bestimmten Kontakt, der auf Ihre Umfrage geantwortet hat. In der Hauptansicht des Kontakts sehen Sie sowohl die antwortbasierten Daten als auch die Events.

![Umfragedaten in Realtime synchronisiert]({% image_buster /assets/img/survicate/survicate_29.png %})