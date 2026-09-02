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
Content Optimizer befindet sich derzeit in der Beta-Phase. Wenn Sie Hilfe beim Einstieg benötigen, wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in.
{% endalert %}

## Einen Otimizador de Conteúdo-Schritt erstellen {#create-a-content-optimizer-step}

Für beste Ergebnisse verwenden Sie den Otimizador de Conteúdo in Canvase, in denen Nutzer:innen den Schritt nach und nach über einen Zeitraum betreten. Wenn alle Nutzer:innen den Schritt gleichzeitig betreten, hat der Otimizador de Conteúdo keine Zeit, aus frühen Ergebnissen zu lernen.

### Schritt 1: Einen Schritt hinzufügen {#step-1-add-a-step}

Ziehen Sie die Komponente **Otimizador de Conteúdo** per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Otimizador de Conteúdo**.

### Schritt 2: Ihre Basisnachricht erstellen {#step-2-create-your-base-message}

Die Basisnachricht ist der Ausgangspunkt für Ihren Schritt. Varianten für jede Inhaltskomponente werden dynamisch eingefügt, basierend auf den Kombinationen, die im Tab **Content Optimizer Settings** definiert sind.

{% alert note %}
Während der Beta-Phase sind die unterstützten Kanäle E-Mail, Push-Benachrichtigungen und Kurzmitteilungsdienst or SMS/MMS/RCS.
{% endalert %}

{% tabs local %}
{% tab E-Mail %}

Wählen Sie im Tab **Messaging Channels** die Option **Email** und erstellen Sie Ihre Basis-E-Mail-Nachricht. Weitere Hilfe finden Sie in unserem dedizierten Abschnitt [E-Mail]({{site.baseurl}}/user_guide/channels/email).

Der Otimizador de Conteúdo verwendet die Sendeeinstellungen (wie die E-Mail-Domain und die Antwortadresse), die in dieser Variante angegeben sind, um alle Nachrichten zu senden. Sie können entweder mit einem neuen Design beginnen oder ein bestehendes Template für diese Nachricht auswählen. Überlegen Sie bei diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Diese definieren Sie in [Schritt 4](#step-4).

Unterstützte Komponenten zur Optimierung umfassen:

- Subject
- Body Header
- Body Content
- Primary CTA

{% endtab %}
{% tab Push-Benachrichtigungen %}

Wählen Sie im Tab **Messaging Channels** die Option **Push notifications** und erstellen Sie Ihre Basis-Push-Benachrichtigung. Weitere Hilfe finden Sie in unserem dedizierten Abschnitt [Push]({{site.baseurl}}/user_guide/channels/push).

Der Otimizador de Conteúdo verwendet die in dieser Variante angegebenen ausgewählten Push-Plattformen, um alle Nachrichten zu senden. Sie können entweder mit einem neuen Design beginnen oder ein bestehendes Template für diese Nachricht auswählen. Überlegen Sie bei diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Diese definieren Sie in [Schritt 4](#step-4).

Unterstützte Komponenten zur Optimierung umfassen:

- Title
- Message

{% endtab %}
{% tab Kurzmitteilungsdienst or SMS/MMS/RCS %}

Wählen Sie im Tab **Messaging Channels** die Option **Kurzmitteilungsdienst or SMS/MMS/RCS** und erstellen Sie Ihre Basisnachricht. Weitere Hilfe finden Sie in unserem dedizierten Abschnitt [Kurzmitteilungsdienst or SMS/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs).

Der Otimizador de Conteúdo verwendet die in dieser Variante angegebenen **Content**- und **Message**-Details, um alle Nachrichten zu senden. Sie können entweder mit einem neuen Design beginnen oder ein bestehendes Template für diese Nachricht auswählen. Überlegen Sie bei diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Diese definieren Sie in [Schritt 4](#step-4).

Unterstützte Komponenten zur Optimierung umfassen:

- Hook
- Body
- CTA

{% endtab %}
{% endtabs %}

### Schritt 3: Zustellungseinstellungen festlegen {#step-3-specify-delivery-settings}

Im Tab **Delivery Settings** können Sie festlegen, ob der Schritt intelligentes Timing oder Zustellungsvalidierungen verwenden soll. Weitere Details finden Sie unter [Zustellungseinstellungen bearbeiten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) im Nachrichtenschritt.

### Schritt 4: Inhaltskomponenten und Varianten hinzufügen {#step-4}

Inhaltskomponenten sind die einzelnen Elemente Ihrer Nachricht, die Sie testen möchten, wie verschiedene Betreffzeilen oder Titel. Diese Komponenten ermöglichen es Ihnen, mehrere Versionen einer Nachricht zu generieren und automatisch basierend auf der Performance über einen Zeitraum zu optimieren.

- **E-Mail:** Sie können bis zu drei Inhaltskomponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, für insgesamt 125 einzigartige Inhaltskombinationen.
- **Push-Benachrichtigungen:** Sie können bis zu zwei Komponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, für insgesamt 25 einzigartige Inhaltskombinationen.
- **Kurzmitteilungsdienst or SMS/MMS/RCS:** Sie können bis zu zwei Inhaltskomponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, für insgesamt 25 einzigartige Inhaltskombinationen.

Wenn Sie **Generate KI or künstliche Intelligenz suggestions** verwenden, sendet Braze Inhalte an OpenAI, um Variantenideen zu generieren. Die Zuweisung des Datenverkehrs zur Sendezeit verwendet OpenAI nicht. Details darüber, welche Daten gesendet werden und wie sie verwendet werden, finden Sie unter [OpenAI und Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer#openai-and-content-optimizer).

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten in der Otimizador-de-Conteúdo-Oberfläche. Die Oberfläche zeigt auswählbare Komponenten wie Subject, Body Header, Body Content und Primary CTA, jeweils mit Feldern zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Schritt 4.1: Inhaltskomponenten konfigurieren {#step-41-configure-content-components}

Um Komponenten zu konfigurieren, gehen Sie zum Tab **Content Optimizer Settings**.

{% tabs local %}
{% tab E-Mail %}

Wählen Sie, welche Komponenten Sie für E-Mail-Nachrichten optimieren möchten. Unterstützte Optionen sind:

- Subject
- Body Header
- Body Content
- Primary CTA

Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, unterschiedliche Varianten, die sich in Ton, Struktur oder Inhalt unterscheiden. Dies hilft dem Otimizador de Conteúdo, Top-Performer effektiver zu identifizieren. Sie können:
  - Ihre eigenen Varianten manuell schreiben.
  - KI or künstliche Intelligenz-generierte Vorschläge verwenden, um schnell neue Optionen zu erkunden.

![Content-Optimizer-Settings-Oberfläche mit Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die E-Mail-Optimierung. Jede Komponente verfügt über Eingabefelder für verschiedene Varianten. Sichtbarer Text umfasst Komponentennamen und Felder zur Eingabe von Variantentext.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Push-Benachrichtigungen %}

Wählen Sie, welche Komponenten Sie für Push-Benachrichtigungen optimieren möchten. Unterstützte Optionen sind:
- Title
- Message

Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, unterschiedliche Varianten, die sich in Ton, Struktur oder Inhalt unterscheiden. Dies hilft dem Otimizador de Conteúdo, Top-Performer effektiver zu identifizieren. Sie können:
  - Ihre eigenen Varianten manuell schreiben.
  - KI or künstliche Intelligenz-generierte Vorschläge verwenden, um schnell neue Optionen zu erkunden.

![Content-Optimizer-Einstellungen mit Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die Push-Optimierung.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab Kurzmitteilungsdienst or SMS/MMS/RCS %}

Nachdem Sie Ihre Abo-Gruppe und den Nachrichtentyp (falls zutreffend) ausgewählt haben, wählen Sie, welche Komponenten Sie für Kurzmitteilungsdienst or SMS/MMS/RCS optimieren möchten. Unterstützte Optionen sind:
- Hook
- Body
- CTA
{% alert note %}
Nachdem ein Kurzmitteilungsdienst or SMS/MMS/RCS-Otimizador-de-Conteúdo-Schritt gestartet wurde, können Sie die Abo-Gruppe oder den Nachrichtentyp nicht mehr Update or aktualisieren or aktualisieren.
{% endalert %}
Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, unterschiedliche Varianten, die sich in Ton, Struktur oder Inhalt unterscheiden. Dies hilft dem Otimizador de Conteúdo, Top-Performer effektiver zu identifizieren. Sie können:
  - Ihre eigenen Varianten manuell schreiben.
  - KI or künstliche Intelligenz-generierte Vorschläge verwenden, um schnell neue Optionen zu erkunden.

![Content-Optimizer-Einstellungen mit Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die SMS/MMS/RCS-Optimierung.]({% image_buster /assets/img/content_optimizer/add_content_components_sms_rcs_mms.png %})

{% endtab %}
{% endtabs %}

#### Schritt 4.2: Liquid zu Ihrer Nachricht hinzufügen {#step-42-add-liquid-to-your-message}

Nachdem Sie mindestens zwei Varianten für jede Komponente definiert haben, kopieren Sie den zugehörigen Liquid-Tag für jede Komponente und fügen Sie ihn an der entsprechenden Stelle in Ihrer Basisnachricht ein.

- Wenn Sie beispielsweise die Betreffzeile optimieren, fügen Sie den Tag {% raw %}`{% message_component "Subject" %}`{% endraw %} in das Betrefffeld des E-Mail-Composers ein.
- Sie können Komponenten-Tags auch in längeren Text einfügen, um nur einen Teil der Komponente zu testen. Zum Beispiel: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten wie Subject, Body Header, Body Content und Primary CTA. Jede Komponente verfügt über Felder zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Wenn Sie keinen Liquid-Tag für eine ausgewählte Inhaltskomponente hinzufügen, sehen Sie eine Warnung im Tab **Content Optimizer Settings** und einen Fehler im Tab **Messaging Channels**. Der Canvas kann nicht gestartet werden, bis alle ausgewählten Komponenten ordnungsgemäß zu Ihrer Basisnachricht hinzugefügt wurden.

Während der Canvas läuft, mischt und kombiniert der Otimizador de Conteúdo Varianten über Komponenten hinweg, um verschiedene Inhaltskombinationen zu generieren. Im Laufe der Zeit werden leistungsstärkere Kombinationen für die Zustellung priorisiert, was Ihnen hilft, die Performance ohne manuellen Eingriff zu verbessern.

#### Liquid-Referenzen {#liquid-references}

| Kanal | Komponente | Liquid-Snippet |
| --- | --- | --- |
| E-Mail | Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| E-Mail | Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| E-Mail | Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| E-Mail | Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Title | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Message | {% raw %}`{% message_component "Message" %}`{% endraw %} |
| Kurzmitteilungsdienst or SMS/MMS/RCS | Hook | {% raw %}`{% message_component "Hook" %}`{% endraw %} |
| Kurzmitteilungsdienst or SMS/MMS/RCS | Body | {% raw %}`{% message_component "Body" %}`{% endraw %} |
| Kurzmitteilungsdienst or SMS/MMS/RCS | CTA | {% raw %}`{% message_component "CTA" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid-Referenzen" }

#### Kombinations-Token / Textbaustein {#combination-token}

Verwenden Sie das Kombinations-Token / Textbaustein, um aufzuzeichnen, welche Kombination von Varianten eine Nutzerin oder ein Nutzer erhalten hat. Fügen Sie den Liquid-Tag {% raw %}`{{component_combination_token}}`{% endraw %} zu einem Link in Ihrer Basisnachricht hinzu und verwenden Sie den Wert dann in Ihren eigenen Analytics-Tools, um nachgelagertes Verhalten einer bestimmten Kombination zuzuordnen.

Fügen Sie das Token / Textbaustein beispielsweise als UTM-Parameter zu einem Link hinzu:

{% raw %}
```liquid
https://www.example.com/summer-sale?utm_content={{component_combination_token}}
```
{% endraw %}

Der Tag rendert einen String aus Zahlen, die durch Unterstriche getrennt sind, wie z. B. `3_2_8`:

- Jede Position entspricht einer Inhaltskomponente, in der Reihenfolge, in der die Komponenten im Tab **Content Optimizer Settings** erscheinen.
- Jede Zahl ist der Index der Variante, die die Nutzerin oder der Nutzer für diese Komponente erhalten hat. Indizes beginnen bei 0, wobei `0` die erste für diese Komponente erstellte Variante ist, `1` die zweite usw.

Braze weist einer Variante bei der Erstellung einen Index zu und behält diesen Index für die gesamte Lifetime des Schritts bei. Sie können eine Variante deaktivieren, aber nicht löschen, und Indizes werden niemals wiederverwendet oder neu nummeriert. Ein Index spiegelt nicht die Position der Variante unter den aktuell aktiven Varianten wider.

Aus diesem Grund können Indizes höher klettern, als das Limit von fünf Varianten pro Komponente vermuten lässt. Dieses Limit gilt nur für aktive Varianten. Wenn Sie also mehrere Varianten deaktivieren und neue hinzufügen, können die neuen Varianten Indizes wie 5, 6, 7 und 8 haben.

Beispiel: Ein E-Mail-Schritt optimiert eine Betreffzeile und einen primären CTA. Die Subject-Komponente wurde mit fünf Varianten gestartet. Drei wurden später deaktiviert und drei neue hinzugefügt:

| Subject-Variante | Index | Status |
| --- | --- | --- |
| Your summer sale starts now | 0 | Deaktiviert |
| Summer sale: 20% off | 1 | Deaktiviert |
| 20% off, this week only | 2 | Deaktiviert |
| Save 20% on summer picks | 3 | Aktiv |
| Your 20% off code is inside | 4 | Aktiv |
| Summer picks, 20% off | 5 | Aktiv |
| Don't miss 20% off | 6 | Aktiv |
| Last chance: 20% off summer | 7 | Aktiv |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Subject-Varianten-Indizes" }

Die Primary-CTA-Komponente hat zwei Varianten mit den Indizes 0 und 1. In diesem Schritt bedeutet ein Token / Textbaustein von `6_1`, dass die Nutzerin oder der Nutzer die Subject-Variante mit Index 6 („Don't miss 20% off“) und die Primary-CTA-Variante mit Index 1 erhalten hat.

### Schritt 5: Optimierungsereignis auswählen {#step-5-select-optimization-event}

Das Optimierungsereignis bestimmt, wie der Otimizador de Conteúdo die Performance bewertet und den Datenverkehr im Laufe der Zeit auf Inhaltskombinationen verteilt.

Ihr ausgewähltes Optimierungsereignis gilt für alle Inhaltskomponenten in diesem Schritt.

{% tabs local %}
{% tab E-Mail %}

Für E-Mail können Sie für eines der folgenden Ereignisse optimieren. Der Otimizador de Conteúdo verwendet Öffnungen und Klicks, die innerhalb von 7 Tagen nach dem Senden einer Nachricht registriert werden, um die Zustellung in Richtung leistungsstärkerer Inhaltskombinationen zu verschieben.

| Ereignis | Beschreibung | Anwendungsfälle |
| --- | --- | --- |
| Öffnungen | Optimiert für Kombinationen, die Empfänger:innen dazu bringen, die E-Mail zu öffnen. | Testen von Betreffzeilen oder Steigerung der Sichtbarkeit |
| Klicks | Optimiert für Kombinationen, die Engagement mit Links fördern. Enthält keine Bot-Klicks oder von Braze erkannte Abmelde-Klicks. | Steigerung von Traffic, Engagement oder Konversion über Links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 5: Optimierungsereignis auswählen" }

#### Links von der Optimierung ausschließen {#exclude-links-from-optimization}

Wenn Sie für Klicks optimieren, können Sie einen oder mehrere Links von der Optimierung ausschließen. Verwenden Sie dies für Links, die kein Engagement mit dem getesteten Inhalt signalisieren, wie ein Präferenzcenter oder ein Filialfinder.

Um einen Link auszuschließen, gehen Sie zum Tab **Content Optimizer Settings** und fügen Sie die URL des Links hinzu. Braze gleicht anhand des Präfixes ab, sodass ein Klick auf jede URL in Ihrer Nachricht, die mit der von Ihnen angegebenen URL beginnt, ausgeschlossen wird.

Ausgeschlossene Klicks zählen nicht zum Optimierungsereignis und beeinflussen daher nicht, welche Kombinationen der Otimizador de Conteúdo bevorzugt. Sie werden dennoch in den Gesamt-Analytics des Schritts gezählt und sind nicht in den Tabellen [Performance nach Komponente](#performance-by-component) oder [Performance nach Kombination](#performance-by-combination) enthalten.

{% endtab %}
{% tab Push-Benachrichtigungen %}

Für Push-Benachrichtigungen können Sie für **Öffnungen** optimieren. Dies optimiert Kombinationen, die Empfänger:innen dazu bringen, die Push-Benachrichtigung zu öffnen. Sie können dieses Optimierungsereignis verwenden, um Variationen im Titel oder Nachrichtentext zu testen.

{% endtab %}
{% tab Kurzmitteilungsdienst or SMS/MMS/RCS %}

Für Kurzmitteilungsdienst or SMS- und MMS-Nachrichten können Sie für **Klicks** optimieren. Für RCS-Nachrichten können Sie für **Reads** oder **Klicks** optimieren.

Damit der Schritt ein Ereignis hat, für das er optimiert:
- Kurzmitteilungsdienst or SMS- und MMS-Nachrichten müssen einen Link enthalten.
- RCS-Nachrichten müssen einen Link oder eine vorgeschlagene Antwort enthalten.

{% alert note %}
Derzeit unterstützt RCS-Messaging mit dem Otimizador de Conteúdo keine Kurzmitteilungsdienst or SMS-Fallbacks.
{% endalert %}
{% endtab %}
{% endtabs %}

## Schritt-Status {#step-states}

Wenn ein Content-Optimizer-Schritt ausgeführt wird, bewertet Braze die Performance der Content-Varianten und weist dem Schritt einen von drei Status zu, die im Canvas sichtbar sind.

| Status | Bedeutung |
| --- | --- |
| Learning | Content Optimizer sammelt noch Performance-Daten über Ihre Content-Varianten und hat bisher keinen konsistenten, zuverlässigen Gewinner gefunden. |
| Optimizing | Content Optimizer hat Varianten gefunden, die konstant besser abschneiden als andere, und verlagert die Zustellung in Richtung der Gewinnerkombinationen. |
| Action Recommended | Der Schritt wurde eine Weile ausgeführt, ohne dass ein klarer Gewinner hervorgegangen ist. Überprüfen Sie die Einrichtung Ihres Schritts, um Content Optimizer bei der Ermittlung eines Gewinners zu unterstützen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content-Optimizer-Schritt-Status" }

### Empfohlene Maßnahmen {#actions-to-consider}

Wenn Ihr Schritt in den Status „Action Recommended“ wechselt, sollten Sie Folgendes in Betracht ziehen:

- Erhöhen Sie nach Möglichkeit die Anzahl der Nutzer:innen, die den Canvas betreten. Mehr Sendungen geben Content Optimizer mehr Daten zum Lernen.
- Testen Sie grundsätzlich lieber mehr Kombinationen als weniger (siehe [Best Practices](#best-practices)). So erhält Content Optimizer ein klareres Signal darüber, was gewinnt. Wenn Ihr Zielgruppenvolumen gering ist (durchschnittlich unter etwa 3.000 Sendungen pro Tag), sollten Sie stattdessen die Anzahl der Varianten leicht reduzieren, da zu viele Kombinationen im Verhältnis zu Ihrem Volumen den Lernprozess verlangsamen können.
- Gestalten Sie Ihre Content-Varianten in Ton, Struktur oder Inhalt deutlicher unterschiedlich voneinander.
- Wenn Sie Ihre Zielgruppe nicht vergrößern können und die Anzahl Ihrer Varianten sowie die Content-Vielfalt bereits passend erscheinen, benötigt Ihr Schritt möglicherweise einfach mehr Zeit, um Gewinner zu ermitteln.

## Einen gestarteten Schritt bearbeiten {#edit-a-launched-step}

Nachdem Ihr Canvas gestartet wurde, können Sie einen laufenden Content-Optimizer-Schritt Update or aktualisieren or aktualisieren, indem Sie ihn im Canvas-Editor öffnen. Sie können:

{% multi_lang_include messaging/Canvas/content_optimizer_launched_step_actions.md %}

{% alert note %}
Braze weist jeder Nutzer:in eine Inhaltskombination zu, wenn sie den Content-Optimizer-Schritt betritt. Wenn der Versand durch Zustellungskontrollen wie Rate-Limiting, intelligentes Timing oder Ruhezeiten verzögert wird, kann die Person dennoch eine Variante erhalten, die Sie deaktiviert haben. Um diese Sendungen dringend zu stoppen, befolgen Sie die gleichen Schritte wie bei einem Nachrichten-Schritt. Weitere Informationen finden Sie unter [Canvase stoppen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).
{% endalert %}

Wenn Sie Änderungen veröffentlichen, wird der Optimizer zurückgesetzt und beginnt, den Traffic von Grund auf über alle aktiven Varianten und Kombinationen neu zu verteilen. Vermeiden Sie es, Varianten zu Update or aktualisieren or aktualisieren, während sich der Schritt im Lernzustand befindet. Historische Daten von vor der Bearbeitung werden beibehalten und sind im Tab **Content Analytics** einsehbar.

Die folgenden Einstellungen können nach dem Start nicht mehr geändert werden:

- Der Inhalt bestehender aktiver Varianten
- Welche Komponenten getestet werden
- Das Optimierungsereignis

Für Kurzmitteilungsdienst or SMS/MMS/RCS-Schritte können auch die Abo-Gruppe und der Nachrichtentyp nach dem Start nicht mehr geändert werden.

## Best Practices {#best-practices}

- Testen Sie generell mehr Komponenten statt weniger für den Content-Optimizer-Schritt. Zum Beispiel: Statt zwei Komponenten für E-Mail zu testen, testen Sie drei.
- Das Testen von mindestens 10 Gesamtkombinationen liefert in der Regel bessere Ergebnisse.
- Bei E-Mails übertreffen Schritte, die auf Klicks optimieren, tendenziell solche, die auf Öffnungen optimieren. Wenn Klicks zu Ihrem Anwendungsfall passen, wählen Sie Klicks als Ihr Optimierungsereignis.
- Wenn Sie den Content Optimizer zum ersten Mal verwenden, sollten Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt einsetzen, sodass nur ein Teil Ihrer Zielgruppe den Zweig betritt, der den Content-Optimizer-Schritt enthält. Sie könnten zum Beispiel die Hälfte Ihrer Nutzer:innen über einen Pfad mit dem Content-Optimizer-Schritt leiten und die andere Hälfte über einen Kontrollpfad, der den Nachrichtenschritt mit Ihren aktuellen Standardinhalten sendet. Sammeln Sie dann 2–3 Wochen lang Daten und vergleichen Sie alle KPI or Leistungskennzahl or Leistungskennzahlen or Leistungskennzahl or Leistungskennzahlen (KPIs) oder Gegenmetriken, bevor Sie den Traffic zu den Pfaden mit Content-Optimizer-Schritten erhöhen.
  - Für einen effektiven Eins-zu-eins-Vergleich fügen Sie Ihre Standardinhalte als eine der Varianten für jede Komponente in Ihrem Content-Optimizer-Schritt ein.
- Wenn Sie nach einiger Zeit im Optimierungsstatus Ihres Content-Optimizer-Schritts bereit für eine Aktualisierung sind, deaktivieren Sie leistungsschwache Varianten und fügen Sie neue hinzu, die auf den Merkmalen Ihrer Top-Performer aufbauen.

## Überlegungen {#considerations}

- Mehrsprachige Einstellungen werden in Content-Optimizer-Schritten nicht unterstützt. Verwenden Sie stattdessen einen Content-Optimizer-Schritt pro Sprache und verzweigen Sie die Pfade einzeln.
- Liquid-Tags für Content-Optimizer-Komponenten werden in Nachrichten-Schritten nicht unterstützt, sodass der Liquid-Code in Nachrichten-Schritten abbricht.
- Nachdem ein Content-Optimizer-Schritt gestartet wurde, können Sie nicht mehr ändern, welche Komponenten getestet werden, den Inhalt bestehender aktiver Varianten oder das Optimierungsereignis. Bei Kurzmitteilungsdienst or SMS-/MMS-/RCS-Schritten können auch die Abo-Gruppe und der Nachrichtentyp nicht mehr geändert werden.

## Analytics {#analytics}

Um die Performance zu überprüfen, öffnen Sie das Analytics-Panel auf Schrittebene, um Metriken nach Inhaltsvariante und der gesamten Kombinationsperformance anzuzeigen. Der Content-Optimizer-Schritt verwendet die [gleichen Analytics wie der Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics).

Wenn Sie den Schritt nach dem Start aktualisiert haben, markiert das Sendezuteilungs-Chart, wann jede Inhaltsänderung vorgenommen wurde. Daten deaktivierter Varianten werden beibehalten und bleiben im Analytics-Panel einsehbar, sodass Sie die Performance über die gesamte Lifetime des Schritts vergleichen können.

![Content-Optimizer-Analytics für drei Buttons und den prozentualen Anteil der Sendezuteilung, der einen Aufwärtstrend zeigt.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Performance nach Komponente {#performance-by-component}

Der Bereich **Performance nach Komponente** zeigt die Performance für jede Komponente im Content-Optimizer-Schritt an. Die Spalte **Komponente** entspricht der Inhaltskomponente, die Sie testen (z. B. **Betreffzeile** oder **Primärer CTA**). Die Spalte **Bezeichner** entspricht dem Bezeichner für diese Variante im Tab **Content-Optimizer-Einstellungen**.

Eindeutige Öffnungen und Klicks werden innerhalb von sieben Tagen nach dem Senden einer Nachricht erfasst. Welche Spalten angezeigt werden, hängt von Ihrem Kanal und dem ausgewählten Optimierungsereignis ab.

| Metrik | Beschreibung |
| --- | --- |
| Sendungen | Die Anzahl der Sendungen, die dieser Variante für die betreffende Komponente in diesem Schritt zugeordnet sind, unter Verwendung der gleichen Sendezählung auf Schrittebene wie [*Sendungen*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends) in der Tabelle [Performance nach Kombination](#performance-by-combination). |
| Öffnungen | Wenn diese Spalte für Ihren Kanal angezeigt wird, die Anzahl der **eindeutigen** Öffnungen für diese Variante innerhalb von sieben Tagen nach dem Senden. Siehe [*Eindeutige Öffnungen*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Öffnungsrate | Wenn diese Spalte angezeigt wird, der Prozentsatz der Sendungen für diese Variante, bei denen innerhalb von sieben Tagen mindestens eine qualifizierende eindeutige Öffnung protokolliert wurde. |
| Klicks | Die Anzahl der **eindeutigen** Klicks für diese Variante innerhalb von sieben Tagen nach dem Senden. Siehe [*Gesamtklicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*Eindeutige Klicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks) und [Schritt 5: Optimierungsereignis auswählen](#step-5-select-optimization-event). |
| Klickrate | Der Prozentsatz der Sendungen für diese Variante, bei denen innerhalb von sieben Tagen mindestens ein qualifizierender eindeutiger Klick protokolliert wurde, unter Verwendung des gleichen Schrittfensters wie in der Tabelle [Performance nach Kombination](#performance-by-combination). Weitere Informationen finden Sie unter [Warum sich Schritt-Analytics von allgemeinen Analytics unterscheiden](#why-step-analytics-differ-from-general-analytics). |
| Lesevorgänge | Wenn diese Spalte angezeigt wird (z. B. für RCS bei Optimierung auf Lesevorgänge), wird gezählt, wenn Verbraucher:innen die Nachricht mit aktivierten Lesebestätigungen lesen. Siehe [*Lesevorgänge*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads). |
| Leserate | Der Prozentsatz der Sendungen für diese Variante, die bei Nutzer:innen mit aktivierten Lesebestätigungen zu einem Lesevorgang geführt haben. Siehe [*Leserate*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metriken für Performance nach Komponente" }

![Content-Optimizer-Analytics „Performance nach Komponente“ mit separaten Tabellen pro Komponente, die Sendungen, Klicks und Klickrate für jede Variante auflisten.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### Performance nach Kombination {#performance-by-combination}

Der Bereich **Performance nach Kombination** zeigt die Performance für jede Kombination im Content-Optimizer-Schritt an. Kombinationen sind die Mischung aus Varianten, die diese Zeile definieren – eine ausgewählte Variante aus jeder Inhaltskomponente, die Sie testen (z. B. eine Betreffzeile gepaart mit einem primären CTA).

Eindeutige Öffnungen und Klicks werden innerhalb von sieben Tagen nach dem Senden einer Nachricht erfasst. Welche Spalten angezeigt werden, hängt von Ihrem Kanal und dem ausgewählten Optimierungsereignis ab.

| Metrik | Beschreibung |
| --- | --- |
| Sendungen | Die Gesamtzahl der Nachrichten, die von diesem Schritt mit dieser Kombination gesendet wurden. Die Zählung folgt der gleichen allgemeinen Definition wie [*Sendungen*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends), bezogen auf jede Kombination. |
| Öffnungen | Die Anzahl der eindeutigen Öffnungen für diese Kombination innerhalb von sieben Tagen nach dem Senden. Zur Definition eindeutiger Öffnungen bei E-Mails siehe [*Eindeutige Öffnungen*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Öffnungsrate | Der Prozentsatz der Sendungen für diese Kombination, bei denen innerhalb von sieben Tagen mindestens eine qualifizierende eindeutige Öffnung protokolliert wurde. |
| Klicks | Die Anzahl der eindeutigen Klicks für diese Kombination innerhalb von sieben Tagen nach dem Senden. Zur Definition von Klicks nach Kanal durch Braze siehe [*Gesamtklicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) und [*Eindeutige Klicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks). |
| Klickrate | Der Prozentsatz der Sendungen für diese Kombination, bei denen innerhalb von sieben Tagen mindestens ein qualifizierender eindeutiger Klick protokolliert wurde. Da der Content Optimizer die deduplizierten Sieben-Tage-Werte des Schritts verwendet, stimmt diese Rate möglicherweise nicht mit den Klickraten in allgemeinen Campaign-Analytics überein. Weitere Informationen finden Sie unter [Warum sich Schritt-Analytics von allgemeinen Analytics unterscheiden](#why-step-analytics-differ-from-general-analytics). |
| [Lesevorgänge]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | Wenn diese Spalte angezeigt wird (z. B. für RCS bei Optimierung auf Lesevorgänge), wird gezählt, wenn Verbraucher:innen die Nachricht mit aktivierten Lesebestätigungen lesen. |
| [Leserate]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | Wenn diese Spalte angezeigt wird, der Prozentsatz der Sendungen für diese Kombination, die bei Nutzer:innen mit aktivierten Lesebestätigungen zu einem Lesevorgang geführt haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metriken für Performance nach Kombination" }

![Content-Optimizer-Analytics-Tabelle „Performance nach Kombination“ mit Sendungen, Klicks und Klickrate für jede Inhaltskombination.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

### Warum sich Schritt-Analytics von allgemeinen Analytics unterscheiden {#why-step-analytics-differ-from-general-analytics}

Gründe, warum die Analytics im Content-Optimizer-Schritt von denen im Bereich **Analytics** abweichen:

- Push-Sendungen werden bei Sendungen an dieselbe(n) Nutzer:in auf verschiedenen Geräten dedupliziert.
- Klicks und Öffnungen werden im Allgemeinen dedupliziert, um pro Nutzer:in eindeutig zu sein.
- Im Content-Optimizer-Schritt werden nur Klicks und Öffnungen gezählt, die innerhalb von sieben Tagen nach dem Senden einer Nachricht erfolgen.
- Ausgeschlossene Link-Klicks werden in den Gesamt-Analytics des Schritts gezählt, aber nicht in den Tabellen **Performance nach Komponente** oder **Performance nach Kombination**. Weitere Informationen finden Sie unter [Links von der Optimierung ausschließen](#exclude-links-from-optimization).

### Varianten in einem Kundenprofil or Nutzerprofil anzeigen {#view-variants-on-a-user-profile}

Um zu sehen, welche Varianten einzelne Nutzer:innen erhalten haben, öffnen Sie deren Kundenprofil or Nutzerprofil und navigieren Sie zum Tab **Nachrichtenverlauf**. In der Zeile des Sendeereignisses für einen Content-Optimizer-Schritt zeigt die Tabelle die Komponentenvarianten, die an diese(n) Nutzer:in gesendet wurden. Weitere Informationen finden Sie unter [Tab „Nachrichtenverlauf“]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab).

### Schritte im Berichts-Builder vergleichen {#compare-steps-in-report-builder}

Um die Performance über mehr als einen Content-Optimizer-Schritt hinweg zu vergleichen, erstellen Sie einen Bericht und wählen Sie **Canvas-Schritt mit Canvas Optimizer**. Der Bericht zeigt die Schrittperformance nach Komponente und nach Kombination für die von Ihnen eingeschlossenen Schritte, unabhängig davon, ob sich diese Schritte im selben Canvas oder in verschiedenen Canvase befinden. Weitere Informationen finden Sie unter [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

## Fehlerbehebung {#troubleshooting}

| Problem | Beschreibung | Lösung |
| --- | --- | --- |
| Fehlende Liquid-Tags | Wenn Sie eine Inhaltskomponente (z. B. Betreff oder CTA) hinzufügen, aber den entsprechenden Liquid-Tag nicht in Ihre Basisnachricht einfügen, sehen Sie: <br>- Eine Warnung auf dem Tab **Content Optimizer Settings** <br>- Einen Fehler auf dem Tab **Messaging Channels** | Kopieren Sie das Liquid-Snippet, das unter jeder Komponente im Tab **Content Optimizer Settings** angezeigt wird, und fügen Sie es in den entsprechenden Teil Ihrer Nachricht ein. |
| Verwaiste Liquid-Tags | Wenn Sie eine Inhaltskomponente löschen, aber den zugehörigen Liquid-Tag in der Basisnachricht belassen, wird die Nachricht beim Senden möglicherweise nicht wie erwartet dargestellt. | Entfernen Sie alle nicht verwendeten `message_component`-Tags aus Ihrer Basisnachricht, bevor Sie sie starten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehlerbehebung" }