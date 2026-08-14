---
nav_title: Content Optimizer
article_title: Content Optimizer-Schritt
alias: "/content_optimizer_step/"
page_order: 5
description: "Der Content Optimizer-Schritt ermöglicht es Ihnen, mehrere Versionen von Inhaltskomponenten innerhalb eines einzelnen Schritts zu konfigurieren und zu testen. Er hilft Ihnen, mit Inhaltsvarianten zu experimentieren und optimiert im Laufe der Zeit automatisch in Richtung der leistungsstärksten Kombinationen."
page_type: reference

---

# Content Optimizer-Schritt {#content-optimizer-step}

> Der Content Optimizer-Schritt ermöglicht es Ihnen, mehrere Versionen von Inhaltskomponenten innerhalb eines einzelnen Schritts zu konfigurieren und zu testen. Er hilft Ihnen, mit Inhaltsvarianten zu experimentieren und optimiert im Laufe der Zeit automatisch in Richtung der leistungsstärksten Kombinationen. Eine Einführung finden Sie unter [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer).

{% alert important %}
Content Optimizer befindet sich derzeit in der Beta-Phase. Wenn Sie Hilfe beim Einstieg benötigen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Einen Content-Optimizer-Schritt erstellen {#create-a-content-optimizer-step}

Für optimale Ergebnisse verwenden Sie den Content Optimizer in Canvases, bei denen Nutzer:innen den Schritt nach und nach über einen Zeitraum hinweg betreten. Wenn alle Nutzer:innen den Schritt gleichzeitig betreten, hat der Content Optimizer keine Zeit, aus frühen Ergebnissen zu lernen.

### Schritt 1: Einen Schritt hinzufügen {#step-1-add-a-step}

Ziehen Sie die Komponente **Content Optimizer** per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Content Optimizer**.

### Schritt 2: Ihre Basisnachricht erstellen {#step-2-create-your-base-message}

Die Basisnachricht ist der Ausgangspunkt für Ihren Schritt. Varianten für jede Inhaltskomponente werden dynamisch basierend auf den im Tab **Content Optimizer Settings** definierten Kombinationen eingefügt.

{% alert note %}
Während der Beta-Phase sind die unterstützten Kanäle E-Mail, Push-Benachrichtigungen und SMS/MMS/RCS.
{% endalert %}

{% tabs local %}
{% tab E-Mail %}

Wählen Sie im Tab **Messaging Channels** die Option **Email** und erstellen Sie Ihre Basis-E-Mail-Nachricht. Weitere Hilfe finden Sie in unserem dedizierten Abschnitt [E-Mail]({{site.baseurl}}/user_guide/channels/email).

Der Content Optimizer verwendet die in dieser Variante angegebenen Sendeeinstellungen (wie die E-Mail-Domain und die Antwortadresse), um alle Nachrichten zu senden. Sie können entweder mit einem neuen Design beginnen oder ein vorhandenes Template für diese Nachricht auswählen. Überlegen Sie in diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Diese definieren Sie in [Schritt 4](#step-4).

Unterstützte Komponenten zur Optimierung umfassen:

- Subject
- Body Header
- Body Content
- Primary CTA

{% endtab %}
{% tab Push-Benachrichtigungen %}

Wählen Sie im Tab **Messaging Channels** die Option **Push notifications** und erstellen Sie Ihre Basis-Push-Benachrichtigung. Weitere Hilfe finden Sie in unserem dedizierten Abschnitt [Push]({{site.baseurl}}/user_guide/channels/push).

Der Content Optimizer verwendet die in dieser Variante ausgewählten Push-Plattformen, um alle Nachrichten zu senden. Sie können entweder mit einem neuen Design beginnen oder ein vorhandenes Template für diese Nachricht auswählen. Überlegen Sie in diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Diese definieren Sie in [Schritt 4](#step-4).

Unterstützte Komponenten zur Optimierung umfassen:

- Title
- Message

{% endtab %}
{% tab SMS/MMS/RCS %}

Wählen Sie im Tab **Messaging Channels** die Option **SMS/MMS/RCS** und erstellen Sie Ihre Basisnachricht. Weitere Hilfe finden Sie in unserem dedizierten Abschnitt [SMS/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs).

Der Content Optimizer verwendet die in dieser Variante angegebenen Details zu **Content** und **Message**, um alle Nachrichten zu senden. Sie können entweder mit einem neuen Design beginnen oder ein vorhandenes Template für diese Nachricht auswählen. Überlegen Sie in diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Diese definieren Sie in [Schritt 4](#step-4).

Unterstützte Komponenten zur Optimierung umfassen:

- Hook
- Body
- CTA

{% endtab %}
{% endtabs %}

### Schritt 3: Zustellungseinstellungen festlegen {#step-3-specify-delivery-settings}

Im Tab **Delivery Settings** können Sie angeben, ob der Schritt intelligentes Timing oder Zustellungsvalidierungen verwenden soll. Weitere Details finden Sie unter [Zustellungseinstellungen bearbeiten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) im Nachrichtenschritt.

### Schritt 4: Inhaltskomponenten und Varianten hinzufügen {#step-4}

Inhaltskomponenten sind die einzelnen Elemente Ihrer Nachricht, die Sie testen möchten, wie verschiedene Betreffzeilen oder Titel. Diese Komponenten ermöglichen es Ihnen, mehrere Versionen einer Nachricht zu generieren und basierend auf der Performance über die Zeit automatisch zu optimieren.

- **E-Mail:** Sie können bis zu drei Inhaltskomponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, für insgesamt 125 eindeutige Inhaltskombinationen.
- **Push-Benachrichtigungen:** Sie können bis zu zwei Komponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, für insgesamt 25 eindeutige Inhaltskombinationen.
- **SMS/MMS/RCS:** Sie können bis zu zwei Inhaltskomponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, für insgesamt 25 eindeutige Inhaltskombinationen.

Wenn Sie **Generate AI suggestions** verwenden, sendet Braze Inhalte an OpenAI, um Variantenideen zu generieren. Die Verteilung des Sendeverkehrs verwendet kein OpenAI. Details dazu, welche Daten gesendet werden und wie sie verwendet werden, finden Sie unter [OpenAI und Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer#openai-and-content-optimizer).

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten in der Content-Optimizer-Oberfläche. Die Oberfläche zeigt auswählbare Komponenten wie Subject, Body Header, Body Content und Primary CTA, jeweils mit Feldern zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Schritt 4.1: Inhaltskomponenten konfigurieren {#step-41-configure-content-components}

Um Komponenten zu konfigurieren, gehen Sie zum Tab **Content Optimizer Settings**.

{% tabs local %}
{% tab E-Mail %}

Wählen Sie, welche Komponenten Sie für E-Mail-Nachrichten optimieren möchten. Unterstützte Optionen sind:

- Subject
- Body Header
- Body Content
- Primary CTA

Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, unterschiedliche Varianten, die sich in Ton, Struktur oder Inhalt unterscheiden. Dies hilft dem Content Optimizer, die besten Performer effektiver zu identifizieren. Sie können:
  - Ihre eigenen Varianten manuell schreiben.
  - KI-generierte Vorschläge verwenden, um schnell neue Optionen zu erkunden.

![Content-Optimizer-Einstellungsoberfläche mit Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die E-Mail-Optimierung. Jede Komponente hat Eingabefelder für verschiedene Varianten. Sichtbarer Text umfasst Komponentennamen und Felder zur Eingabe von Variantentext.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Push-Benachrichtigungen %}

Wählen Sie, welche Komponenten Sie für Push-Benachrichtigungen optimieren möchten. Unterstützte Optionen sind:
- Title
- Message

Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, unterschiedliche Varianten, die sich in Ton, Struktur oder Inhalt unterscheiden. Dies hilft dem Content Optimizer, die besten Performer effektiver zu identifizieren. Sie können:
  - Ihre eigenen Varianten manuell schreiben.
  - KI-generierte Vorschläge verwenden, um schnell neue Optionen zu erkunden.

![Content-Optimizer-Einstellungen mit Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die Push-Optimierung.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab SMS/MMS/RCS %}

Nachdem Sie Ihre Abo-Gruppe und den Nachrichtentyp (falls zutreffend) ausgewählt haben, wählen Sie, welche Komponenten Sie für SMS/MMS/RCS optimieren möchten. Unterstützte Optionen sind:
- Hook
- Body
- CTA
{% alert note %}
Nachdem ein SMS/MMS/RCS-Content-Optimizer-Schritt gestartet wurde, können Sie die Abo-Gruppe oder den Nachrichtentyp nicht mehr ändern.
{% endalert %}
Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, unterschiedliche Varianten, die sich in Ton, Struktur oder Inhalt unterscheiden. Dies hilft dem Content Optimizer, die besten Performer effektiver zu identifizieren. Sie können:
  - Ihre eigenen Varianten manuell schreiben.
  - KI-generierte Vorschläge verwenden, um schnell neue Optionen zu erkunden.

![Content-Optimizer-Einstellungen mit Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die SMS/RCS/MMS-Optimierung.]({% image_buster /assets/img/content_optimizer/add_content_components_sms_rcs_mms.png %})

{% endtab %}
{% endtabs %}

#### Schritt 4.2: Liquid zu Ihrer Nachricht hinzufügen {#step-42-add-liquid-to-your-message}

Nachdem Sie mindestens zwei Varianten für jede Komponente definiert haben, kopieren Sie den zugehörigen Liquid-Tag für jede Komponente und fügen Sie ihn an der entsprechenden Stelle in Ihrer Basisnachricht ein.

- Wenn Sie beispielsweise die Betreffzeile optimieren, fügen Sie den Tag {% raw %}`{% message_component "Subject" %}`{% endraw %} in das Betrefffeld des E-Mail-Composers ein.
- Sie können Komponenten-Tags auch innerhalb von längerem Text einfügen, um nur einen Teil der Komponente zu testen. Zum Beispiel: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten wie Subject, Body Header, Body Content und Primary CTA. Jede Komponente hat Felder zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Wenn Sie keinen Liquid-Tag für eine ausgewählte Inhaltskomponente hinzufügen, wird eine Warnung im Tab **Content Optimizer Settings** und ein Fehler im Tab **Messaging Channels** angezeigt. Der Canvas kann nicht gestartet werden, bis alle ausgewählten Komponenten ordnungsgemäß zu Ihrer Basisnachricht hinzugefügt wurden.

Während der Canvas läuft, mischt und kombiniert der Content Optimizer Varianten über Komponenten hinweg, um verschiedene Inhaltskombinationen zu generieren. Im Laufe der Zeit werden leistungsstärkere Kombinationen bei der Zustellung priorisiert, was Ihnen hilft, die Performance ohne manuelles Eingreifen zu verbessern.

#### Liquid-Referenzen {#liquid-references}

| Kanal | Komponente | Liquid-Snippet |
| --- | --- | --- |
| E-Mail | Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| E-Mail | Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| E-Mail | Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| E-Mail | Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Title | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Message | {% raw %}`{% message_component "Message" %}`{% endraw %} |
| SMS/MMS/RCS | Hook | {% raw %}`{% message_component "Hook" %}`{% endraw %} |
| SMS/MMS/RCS | Body | {% raw %}`{% message_component "Body" %}`{% endraw %} |
| SMS/MMS/RCS | CTA | {% raw %}`{% message_component "CTA" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid-Referenzen" }

### Schritt 5: Optimierungsereignis auswählen {#step-5-select-optimization-event}

Das Optimierungsereignis bestimmt, wie der Content Optimizer die Performance bewertet und den Verkehr über die Zeit auf Inhaltskombinationen verteilt.

Ihr ausgewähltes Optimierungsereignis gilt für alle Inhaltskomponenten in diesem Schritt.

{% tabs local %}
{% tab E-Mail %}

Für E-Mail können Sie für eines der folgenden Ereignisse optimieren. Der Content Optimizer verwendet Öffnungen und Klicks, die innerhalb von 7 Tagen nach dem Senden einer Nachricht registriert werden, um die Zustellung in Richtung leistungsstärkerer Inhaltskombinationen zu verschieben.

| Ereignis | Beschreibung | Anwendungsfälle |
| --- | --- | --- |
| Öffnungen | Optimiert für Kombinationen, die Empfänger:innen dazu bringen, die E-Mail zu öffnen. | Testen von Betreffzeilen oder Steigerung der Sichtbarkeit |
| Klicks | Optimiert für Kombinationen, die Engagement mit Links fördern. Beinhaltet keine Bot-Klicks oder von Braze erkannte Abmelde-Klicks. | Steigerung von Traffic, Engagement oder Konversion über Links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 5: Optimierungsereignis auswählen" }

{% endtab %}
{% tab Push-Benachrichtigungen %}

Für Push-Benachrichtigungen können Sie für **Öffnungen** optimieren. Dies optimiert Kombinationen, die Empfänger:innen dazu bringen, die Push-Benachrichtigung zu öffnen. Sie können dieses Optimierungsereignis verwenden, um Variationen im Titel oder Nachrichtentext zu testen.

{% endtab %}
{% tab SMS/MMS/RCS %}

Für SMS- und MMS-Nachrichten können Sie für **Klicks** optimieren. Für RCS-Nachrichten können Sie für **Lesevorgänge** oder **Klicks** optimieren.

Damit der Schritt ein Ereignis hat, für das er optimiert:
- SMS- und MMS-Nachrichten müssen einen Link enthalten.
- RCS-Nachrichten müssen einen Link oder eine vorgeschlagene Antwort enthalten.

{% alert note %}
Derzeit unterstützt RCS-Messaging mit dem Content Optimizer keine SMS-Fallbacks.
{% endalert %}
{% endtab %}
{% endtabs %}

## Schrittzustände {#step-states}

Während ein Content-Optimizer-Schritt ausgeführt wird, bewertet Braze die Performance der Inhaltsvarianten und weist dem Schritt einen von drei Zuständen zu, die im Canvas sichtbar sind.

| Zustand | Bedeutung |
| --- | --- |
| Learning | Content Optimizer sammelt noch Performance-Daten über Ihre Inhaltsvarianten und hat noch keine konsistente, zuverlässige Gewinnervariante gefunden. |
| Optimizing | Content Optimizer hat Varianten gefunden, die andere konsistent übertreffen, und verlagert die Zustellung zugunsten der gewinnenden Kombinationen. |
| Action Recommended | Der Schritt läuft bereits seit einiger Zeit, ohne dass eine klare Gewinnervariante hervorgegangen ist. Überprüfen Sie Ihre Schritteinstellungen, um Content Optimizer bei der Ermittlung zu unterstützen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zustände des Content-Optimizer-Schritts" }

### Empfohlene Maßnahmen {#actions-to-consider}

Wenn Ihr Schritt in den Zustand „Action Recommended“ wechselt, sollten Sie Folgendes in Betracht ziehen:

- Erhöhen Sie nach Möglichkeit die Anzahl der Nutzer:innen, die den Canvas betreten. Mehr Sendungen liefern Content Optimizer mehr Daten zum Lernen.
- Testen Sie generell eher mehr Kombinationen als weniger (siehe [Best Practices](#best-practices)). So erhält Content Optimizer ein klareres Signal darüber, was gewinnt. Wenn Ihr Zielgruppenvolumen gering ist (durchschnittlich unter ca. 3.000 Sendungen pro Tag), sollten Sie stattdessen die Anzahl der Varianten leicht reduzieren, da zu viele Kombinationen im Verhältnis zu Ihrem Volumen den Lernprozess verlangsamen können.
- Gestalten Sie Ihre Inhaltsvarianten deutlicher unterschiedlich – in Tonalität, Struktur oder Inhalt.
- Wenn Sie Ihre Zielgruppe nicht vergrößern können und Ihre Variantenanzahl sowie die inhaltliche Vielfalt bereits passend erscheinen, benötigt Ihr Schritt möglicherweise einfach mehr Zeit, um Gewinnervarianten zu finden.

## Einen gestarteten Schritt bearbeiten {#edit-a-launched-step}

Nachdem Ihr Canvas gestartet wurde, können Sie einen laufenden Content-Optimizer-Schritt aktualisieren, indem Sie ihn im Canvas-Editor öffnen. Sie können:

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

Wenn Sie Änderungen veröffentlichen, wird der Optimizer zurückgesetzt und beginnt, den Traffic von Grund auf neu auf alle aktiven Varianten und Kombinationen zu verteilen. Vermeiden Sie es, Varianten zu aktualisieren, während sich der Schritt im Lernzustand befindet. Historische Daten von vor der Bearbeitung werden beibehalten und sind im Tab **Content Analytics** einsehbar.

Die folgenden Einstellungen können nach dem Start nicht mehr geändert werden:

- Der Inhalt bestehender aktiver Varianten
- Welche Komponenten getestet werden
- Das Optimierungsereignis

Bei SMS-/MMS-/RCS-Schritten können die Abo-Gruppe und der Nachrichtentyp nach dem Start ebenfalls nicht mehr geändert werden.

## Best Practices {#best-practices}

- Testen Sie im Allgemeinen mehr Komponenten statt weniger für den Content-Optimizer-Schritt. Testen Sie beispielsweise drei Komponenten für E-Mail statt nur zwei.
- Das Testen von mindestens 10 Gesamtkombinationen liefert in der Regel bessere Ergebnisse.
- Wenn Sie den Content Optimizer zum ersten Mal verwenden, sollten Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt einsetzen, sodass nur ein Teil Ihrer Zielgruppe den Branch betritt, der den Content-Optimizer-Schritt enthält. Sie könnten beispielsweise die Hälfte Ihrer Nutzer:innen über einen Pfad mit dem Content-Optimizer-Schritt senden und die andere Hälfte über einen Kontrollpfad, der den Nachrichtenschritt mit Ihrem aktuellen Standardinhalt sendet. Sammeln Sie dann 2–3 Wochen lang Daten und vergleichen Sie alle Leistungskennzahlen (KPIs) oder Gegenmetriken, bevor Sie den Traffic zu den Pfaden mit Content-Optimizer-Schritten erhöhen.
  - Für einen effektiven Eins-zu-eins-Vergleich fügen Sie Ihren Standardinhalt als eine der Varianten für jede Komponente in Ihrem Content-Optimizer-Schritt hinzu.
- Wenn Sie nach einer gewissen Zeit, in der sich Ihr Content-Optimizer-Schritt im Optimierungsstatus befindet, Aktualisierungen vornehmen möchten, deaktivieren Sie leistungsschwache Varianten und fügen Sie neue hinzu, die auf den Eigenschaften Ihrer Top-Performer aufbauen.

## Überlegungen {#considerations}

- Mehrsprachige Einstellungen werden in Content-Optimizer-Schritten nicht unterstützt. Verwenden Sie stattdessen einen Content-Optimizer-Schritt pro Sprache und verzweigen Sie die Pfade einzeln.
- Liquid-Tags für Content-Optimizer-Komponenten werden in Nachrichtenschritten nicht unterstützt, sodass Liquid in Nachrichtenschritten abbricht.
- Nachdem ein Content-Optimizer-Schritt gestartet wurde, können Sie nicht mehr ändern, welche Komponenten getestet werden, den Inhalt bestehender aktiver Varianten oder das Optimierungsereignis. Bei SMS/MMS/RCS-Schritten können auch die Abo-Gruppe und der Nachrichtentyp nicht mehr geändert werden.

## Analytics {#analytics}

Um die Performance zu überprüfen, öffnen Sie das Analytics-Panel auf Schrittebene, um Metriken nach Inhaltsvariante und der Gesamt-Performance der Kombination einzusehen. Der Content-Optimizer-Schritt verwendet die [gleichen Analytics wie der Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics).

Wenn Sie den Schritt nach dem Start aktualisiert haben, markiert das Diagramm zur Sendezuordnung, wann jede Inhaltsänderung vorgenommen wurde. Daten deaktivierter Varianten werden beibehalten und bleiben im Analytics-Panel einsehbar, sodass Sie die Performance über die gesamte Lifetime des Schritts vergleichen können.

![Content-Optimizer-Analytics für drei Buttons und den prozentualen Anteil der Sendezuordnung, der einen Aufwärtstrend zeigt.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Performance nach Komponente {#performance-by-component}

Der Abschnitt **Performance nach Komponente** zeigt die Performance für jede Komponente im Content-Optimizer-Schritt an. Die Spalte **Komponente** entspricht der Inhaltskomponente, die Sie testen (zum Beispiel **Betreffzeile** oder **Primärer CTA**). Die Spalte **Bezeichner** entspricht dem Bezeichner für diese Variante im Tab **Content Optimizer Settings**.

Die eindeutigen Öffnungen und Klicks werden innerhalb von sieben Tagen nach dem Senden einer Nachricht erfasst. Welche Spalten angezeigt werden, hängt von Ihrem Kanal und dem ausgewählten Optimierungsereignis ab.

| Metrik | Beschreibung |
| --- | --- |
| Sends | Die Anzahl der Sends, die dieser Variante für diese Komponente in diesem Schritt zugeordnet werden, unter Verwendung derselben Zählung auf Schrittebene wie [*Sends*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends) in der Tabelle [Performance nach Kombination](#performance-by-combination). |
| Öffnungen | Wenn diese Spalte für Ihren Kanal angezeigt wird, die Anzahl der **eindeutigen** Öffnungen für diese Variante innerhalb von sieben Tagen nach dem Senden. Siehe [*Eindeutige Öffnungen*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Öffnungsrate | Wenn diese Spalte angezeigt wird, der Prozentsatz der Sends für diese Variante, die mindestens eine qualifizierende eindeutige Öffnung innerhalb von sieben Tagen verzeichnet haben. |
| Klicks | Die Anzahl der **eindeutigen** Klicks für diese Variante innerhalb von sieben Tagen nach dem Senden. Siehe [*Gesamtklicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*Eindeutige Klicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks) und [Schritt 5: Optimierungsereignis auswählen](#step-5-select-optimization-event). |
| Klickrate | Der Prozentsatz der Sends für diese Variante, die mindestens einen qualifizierenden eindeutigen Klick innerhalb von sieben Tagen verzeichnet haben, unter Verwendung desselben Schrittfensters wie die Tabelle [Performance nach Kombination](#performance-by-combination). Weitere Informationen finden Sie unter [Warum sich Schritt-Analytics von allgemeinen Analytics unterscheiden](#why-step-analytics-differ-from-general-analytics). |
| Gelesen | Wenn diese Spalte angezeigt wird (zum Beispiel für RCS, wenn Sie für Lesevorgänge optimieren), wird gezählt, wann eine Verbraucher:in die Nachricht mit aktivierten Lesebestätigungen liest. Siehe [*Reads*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads). |
| Leserate | Der Prozentsatz der Sends für diese Variante, die bei Nutzer:innen mit aktivierten Lesebestätigungen zu einem Lesevorgang geführt haben. Siehe [*Read Rate*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metriken für Performance nach Komponente" }

![Content-Optimizer-Analytics „Performance nach Komponente“ mit separaten Tabellen pro Komponente, die Sends, Klicks und Klickrate für jede Variante auflisten.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### Performance nach Kombination {#performance-by-combination}

Der Abschnitt **Performance nach Kombination** zeigt die Performance für jede Kombination im Content-Optimizer-Schritt an. Kombinationen sind die Mischung aus Varianten, die diese Zeile definieren – eine ausgewählte Variante aus jeder Inhaltskomponente, die Sie testen (zum Beispiel eine Betreffzeile gepaart mit einem primären CTA).

Die eindeutigen Öffnungen und Klicks werden innerhalb von sieben Tagen nach dem Senden einer Nachricht erfasst. Welche Spalten angezeigt werden, hängt von Ihrem Kanal und dem ausgewählten Optimierungsereignis ab.

| Metrik | Beschreibung |
| --- | --- |
| Sends | Die Gesamtzahl der Nachrichten, die aus diesem Schritt mit dieser Kombination gesendet wurden. Die Zählung folgt derselben allgemeinen Bedeutung wie [*Sends*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends), bezogen auf jede Kombination. |
| Öffnungen | Die Anzahl der eindeutigen Öffnungen für diese Kombination innerhalb von sieben Tagen nach dem Senden. Zur Definition eindeutiger Öffnungen für E-Mail siehe [*Eindeutige Öffnungen*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Öffnungsrate | Der Prozentsatz der Sends für diese Kombination, die mindestens eine qualifizierende eindeutige Öffnung innerhalb von sieben Tagen verzeichnet haben. |
| Klicks | Die Anzahl der eindeutigen Klicks für diese Kombination innerhalb von sieben Tagen nach dem Senden. Zur Definition von Klicks nach Kanal durch Braze siehe [*Gesamtklicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) und [*Eindeutige Klicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks). |
| Klickrate | Der Prozentsatz der Sends für diese Kombination, die mindestens einen qualifizierenden eindeutigen Klick innerhalb von sieben Tagen verzeichnet haben. Da der Content Optimizer die deduplizierten Zählungen des Schritts über sieben Tage verwendet, stimmt diese Rate möglicherweise nicht mit den Klickraten in den allgemeinen Campaign-Analytics überein. Weitere Informationen finden Sie unter [Warum sich Schritt-Analytics von allgemeinen Analytics unterscheiden](#why-step-analytics-differ-from-general-analytics). |
| [Reads]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | Wenn diese Spalte angezeigt wird (zum Beispiel für RCS, wenn Sie für Lesevorgänge optimieren), wird gezählt, wann eine Verbraucher:in die Nachricht mit aktivierten Lesebestätigungen liest. |
| [Read Rate]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | Wenn diese Spalte angezeigt wird, der Prozentsatz der Sends für diese Kombination, die bei Nutzer:innen mit aktivierten Lesebestätigungen zu einem Lesevorgang geführt haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metriken für Performance nach Kombination" }

![Content-Optimizer-Analytics-Tabelle „Performance nach Kombination“ mit Sends, Klicks und Klickrate für jede Inhaltskombination.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

### Warum sich Schritt-Analytics von allgemeinen Analytics unterscheiden {#why-step-analytics-differ-from-general-analytics}

Gründe, warum sich die Analytics im Content-Optimizer-Schritt vom Abschnitt **Analytics** unterscheiden, sind unter anderem:

- Push-Sends werden für Sends an dieselbe Nutzer:in auf verschiedenen Geräten dedupliziert.
- Im Allgemeinen werden Klicks und Öffnungen dedupliziert, um pro Nutzer:in eindeutig zu sein.
- Nur Klicks und Öffnungen, die innerhalb von sieben Tagen nach dem Senden einer Nachricht erfolgen, werden im Content-Optimizer-Schritt gezählt.

## Fehlerbehebung {#troubleshooting}

| Problem | Beschreibung | Lösung |
| --- | --- | --- |
| Fehlende Liquid-Tags | Wenn Sie eine Inhaltskomponente (z. B. Betreff oder CTA) hinzufügen, aber den entsprechenden Liquid-Tag nicht in Ihre Basisnachricht einfügen, sehen Sie: <br>- Eine Warnung auf dem Tab **Content Optimizer Settings** <br>- Einen Fehler auf dem Tab **Messaging-Kanäle** | Kopieren Sie das Liquid-Snippet, das unter jeder Komponente im Tab **Content Optimizer Settings** angezeigt wird, und fügen Sie es in den entsprechenden Teil Ihrer Nachricht ein. |
| Verwaiste Liquid-Tags | Wenn Sie eine Inhaltskomponente löschen, aber den zugehörigen Liquid-Tag in der Basisnachricht belassen, wird die Nachricht beim Versand möglicherweise nicht wie erwartet dargestellt. | Entfernen Sie alle nicht verwendeten `message_component`-Tags aus Ihrer Basisnachricht, bevor Sie den Versand starten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehlerbehebung" }