---
nav_title: Content Optimizer
article_title: Content Optimizer – Agentenschritt
alias: "/content_optimizer_step/"
page_order: 5
description: "Der Content Optimizer-Agentenschritt ermöglicht es Ihnen, mehrere Versionen von Inhaltskomponenten innerhalb eines einzelnen Schritts zu konfigurieren und zu testen. Er hilft Ihnen, mit Inhaltsvarianten zu experimentieren und optimiert im Laufe der Zeit automatisch in Richtung der leistungsstärksten Kombinationen."
page_type: reference

---

# Content Optimizer – Agentenschritt {#content-optimizer-agent-step}

> Der Content Optimizer-Agentenschritt ermöglicht es Ihnen, mehrere Versionen von Inhaltskomponenten innerhalb eines einzelnen Schritts zu konfigurieren und zu testen. Er hilft Ihnen, mit Inhaltsvarianten zu experimentieren und optimiert im Laufe der Zeit automatisch in Richtung der leistungsstärksten Kombinationen. Eine Einführung finden Sie unter [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
Content Optimizer befindet sich derzeit in der Beta-Phase. Wenn Sie Hilfe beim Einstieg benötigen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Einen Content Optimizer-Schritt erstellen {#creating-a-content-optimizer-step}

Für optimale Ergebnisse verwenden Sie den Content Optimizer-Agenten in Canvases, bei denen Nutzer:innen den Schritt nach und nach über einen Zeitraum hinweg betreten. Wenn alle Nutzer:innen den Schritt gleichzeitig betreten, hat der Agent keine Zeit, aus frühen Ergebnissen zu lernen.

### 1. Schritt: Einen Schritt hinzufügen {#step-1-add-a-step}

Ziehen Sie die **Content Optimizer**-Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Content Optimizer**.

### 2. Schritt: Ihre Basisnachricht erstellen {#step-2-create-your-base-message}

Die Basisnachricht ist der Ausgangspunkt für Ihren Schritt. Varianten für jede Inhaltskomponente werden dynamisch basierend auf den im Tab **Content Optimizer Settings** definierten Kombinationen eingefügt.

{% alert note %}
Während der Beta-Phase sind die unterstützten Kanäle E-Mail und Push-Benachrichtigungen.
{% endalert %}

{% tabs local %}
{% tab E-Mail %}

Wählen Sie im Tab **Messaging Channels** die Option **Email** und erstellen Sie Ihre Basis-E-Mail-Nachricht. Weitere Hilfe finden Sie in unserem dedizierten Abschnitt [E-Mail]({{site.baseurl}}/user_guide/channels/email/).

Der Content Optimizer-Agent verwendet die Sendeeinstellungen (wie die E-Mail-Domain und die Antwortadresse), die in dieser Variante angegeben sind, um alle Nachrichten zu senden. Sie können entweder mit einem neuen Design beginnen oder ein vorhandenes Template für diese Nachricht auswählen. Überlegen Sie in diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Diese definieren Sie in [Schritt 4](#step-4).

Unterstützte Komponenten zur Optimierung umfassen:

- Subject
- Body Header
- Body Content
- Primary CTA

{% endtab %}
{% tab Push-Benachrichtigungen %}

Wählen Sie im Tab **Messaging Channels** die Option **Push notifications** und erstellen Sie Ihre Basis-Push-Benachrichtigung. Weitere Hilfe finden Sie in unserem dedizierten Abschnitt [Push]({{site.baseurl}}/user_guide/channels/push/).

Der Content Optimizer-Agent verwendet die in dieser Variante ausgewählten Push-Plattformen, um alle Nachrichten zu senden. Sie können entweder mit einem neuen Design beginnen oder ein vorhandenes Template für diese Nachricht auswählen. Überlegen Sie in diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Diese definieren Sie in [Schritt 4](#step-4).

Unterstützte Komponenten zur Optimierung umfassen:

- Title
- Message

{% endtab %}
{% endtabs %}

### 3. Schritt: Zustellungseinstellungen festlegen {#step-3-specify-delivery-settings}

Im Tab **Delivery Settings** können Sie angeben, ob der Schritt intelligentes Timing oder Zustellungsvalidierungen verwenden soll. Weitere Details finden Sie unter [Zustellungseinstellungen bearbeiten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) im Nachrichtenschritt.

### 4. Schritt: Inhaltskomponenten und Varianten hinzufügen {#step-4}

Inhaltskomponenten sind die einzelnen Elemente Ihrer Nachricht, die Sie testen möchten, wie z. B. verschiedene Betreffzeilen oder Titel. Diese Komponenten ermöglichen es Ihnen, mehrere Versionen einer Nachricht zu generieren und basierend auf der Performance im Laufe der Zeit automatisch zu optimieren.

- **E-Mail:** Sie können bis zu drei Inhaltskomponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, für insgesamt 125 eindeutige Inhaltskombinationen.
- **Push-Benachrichtigungen:** Sie können bis zu zwei Komponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, für insgesamt 25 eindeutige Inhaltskombinationen.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten in der Content Optimizer-Oberfläche. Die Oberfläche zeigt auswählbare Komponenten wie Subject, Body Header, Body Content und Primary CTA, jeweils mit Feldern zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Schritt 4.1: Inhaltskomponenten konfigurieren {#step-41-configure-content-components}

Um Komponenten zu konfigurieren, gehen Sie zum Tab **Content Optimizer Settings**.

{% tabs local %}
{% tab E-Mail %}

Wählen Sie, welche Komponenten Sie für E-Mail-Nachrichten optimieren möchten. Unterstützte Optionen sind:

- Subject
- Body Header
- Body Content
- Primary CTA

Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, unterschiedliche Varianten, die sich in Tonalität, Struktur oder Inhalt unterscheiden. Dies hilft dem Content Optimizer, Top-Performer effektiver zu identifizieren. Sie können:
  - Ihre eigenen Varianten manuell schreiben.
  - KI-generierte Vorschläge nutzen, um schnell neue Optionen zu erkunden.

![Content Optimizer Settings-Oberfläche mit Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die E-Mail-Optimierung. Jede Komponente hat Eingabefelder für verschiedene Varianten. Sichtbarer Text umfasst Komponentennamen und Felder zur Eingabe von Variantentext.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Push-Benachrichtigungen %}

Wählen Sie, welche Komponenten Sie für Push-Benachrichtigungen optimieren möchten. Unterstützte Optionen sind:
- Title
- Message

Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, unterschiedliche Varianten, die sich in Tonalität, Struktur oder Inhalt unterscheiden. Dies hilft dem Content Optimizer, Top-Performer effektiver zu identifizieren. Sie können:
  - Ihre eigenen Varianten manuell schreiben.
  - KI-generierte Vorschläge nutzen, um schnell neue Optionen zu erkunden.

![Content Optimizer-Einstellungen mit Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die Push-Optimierung.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% endtabs %}

#### Schritt 4.2: Liquid zu Ihrer Nachricht hinzufügen {#step-42-add-liquid-to-your-message}

Nachdem Sie mindestens zwei Varianten für jede Komponente definiert haben, kopieren Sie den zugehörigen Liquid-Tag für jede Komponente und fügen Sie ihn an der entsprechenden Stelle in Ihrer Basisnachricht ein.

- Wenn Sie beispielsweise die Betreffzeile optimieren, fügen Sie den Tag {% raw %}`{% message_component "Subject" %}`{% endraw %} in das Betrefffeld des E-Mail-Composers ein.
- Sie können Komponenten-Tags auch innerhalb längerer Texte einfügen, um nur einen Teil der Komponente zu testen. Zum Beispiel: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten wie Subject, Body Header, Body Content und Primary CTA. Jede Komponente hat Felder zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Wenn Sie keinen Liquid-Tag für eine ausgewählte Inhaltskomponente hinzufügen, sehen Sie eine Warnung im Tab **Content Optimizer Settings** und einen Fehler im Tab **Messaging Channels**. Der Canvas kann nicht gestartet werden, bis alle ausgewählten Komponenten ordnungsgemäß zu Ihrer Basisnachricht hinzugefügt wurden.

Während der Canvas läuft, mischt und kombiniert der Agent Varianten über Komponenten hinweg, um verschiedene Inhaltskombinationen zu generieren. Im Laufe der Zeit werden leistungsstärkere Kombinationen bei der Zustellung priorisiert, was Ihnen hilft, die Performance ohne manuelles Eingreifen zu verbessern.

#### Liquid-Referenzen {#liquid-references}

| Kanal | Komponente | Liquid-Snippet |
| --- | --- | --- |
| E-Mail | Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| E-Mail | Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| E-Mail | Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| E-Mail | Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Title | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Message | {% raw %}`{% message_component "Message" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid-Referenzen" }

### 5. Schritt: Optimierungsevent auswählen {#step-5-select-optimization-event}

Das Optimierungsevent bestimmt, wie der Content Optimizer-Agent die Performance bewertet und den Traffic im Laufe der Zeit auf Inhaltskombinationen verteilt.

Ihr ausgewähltes Optimierungsevent gilt für alle Inhaltskomponenten in diesem Schritt.

{% tabs local %}
{% tab E-Mail %}

Für E-Mail können Sie für eines der folgenden Events optimieren. Der Agent verwendet Öffnungen und Klicks, die innerhalb von 7 Tagen nach dem Senden einer Nachricht registriert werden, um die Zustellung in Richtung leistungsstärkerer Inhaltskombinationen zu verschieben.

| Event | Beschreibung | Anwendungsfälle |
| --- | --- | --- |
| Öffnungen | Optimiert für Kombinationen, die Empfänger:innen dazu bringen, die E-Mail zu öffnen. | Testen von Betreffzeilen oder Steigerung der Sichtbarkeit |
| Klicks | Optimiert für Kombinationen, die Engagement mit Links fördern. Beinhaltet keine Bot-Klicks oder von Braze erkannte Abmelde-Klicks. | Steigerung von Traffic, Engagement oder Conversion über Links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Optimierungsevent auswählen" }

{% endtab %}
{% tab Push-Benachrichtigungen %}

Für Push-Benachrichtigungen können Sie für **Öffnungen** optimieren. Dies optimiert Kombinationen, die Empfänger:innen dazu bringen, die Push-Benachrichtigung zu öffnen. Sie können dieses Optimierungsevent verwenden, um Variationen im Titel oder Nachrichtentext zu testen.

{% endtab %}
{% endtabs %}

## Best Practices {#best-practices}

- Generell empfehlen wir, mehr als eine Komponente für den Content Optimizer-Schritt zu testen.
- Wenn Sie für Klicks optimieren, schließen Sie Betreffzeilen in Ihre Tests ein, da stärkere Betreffzeilen zu mehr Öffnungen beitragen und mehr Möglichkeiten für Klicks schaffen können.
- Wenn Sie für Öffnungen optimieren, konzentrieren Sie Ihre Tests auf die Betreffzeile.

## Analytics {#analytics}

Um die Performance zu überprüfen, öffnen Sie das Analytics-Panel auf Schrittebene, um Metriken nach Inhaltsvariante und der Gesamt-Kombinationsperformance zu sehen. Der Content Optimizer-Schritt verwendet die [gleichen Analytics wie der Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#analytics).

![Content Optimizer-Analytics für drei Buttons und den prozentualen Anteil der Sendezuweisungen, die einen Aufwärtstrend zeigen.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Warum sich Schritt-Analytics von allgemeinen Analytics unterscheiden {#why-step-analytics-differ-from-general-analytics}

Gründe, warum sich die Analytics im Content Optimizer-Schritt vom Abschnitt **Analytics** unterscheiden:

- Push-Sends werden für Sends an dieselbe Nutzer:in auf verschiedenen Geräten dedupliziert.
- Generell werden Klicks und Öffnungen dedupliziert, um pro Nutzer:in eindeutig zu sein.
- Nur Klicks und Öffnungen, die innerhalb von sieben Tagen nach dem Senden einer Nachricht stattfinden, werden im Content Optimizer-Schritt gezählt.

## Fehlerbehebung {#troubleshooting}

| Problem | Beschreibung | Lösung |
| --- | --- | --- |
| Fehlende Liquid-Tags | Wenn Sie eine Inhaltskomponente (wie Subject oder CTA) hinzufügen, aber den entsprechenden Liquid-Tag nicht in Ihre Basisnachricht einfügen, sehen Sie: <br>- Eine Warnung im Tab **Content Optimizer Settings** <br>- Einen Fehler im Tab **Messaging Channels** | Kopieren Sie das Liquid-Snippet, das unter jeder Komponente im Tab **Content Optimizer Settings** angezeigt wird, und fügen Sie es in den entsprechenden Teil Ihrer Nachricht ein. |
| Verwaiste Liquid-Tags | Wenn Sie eine Inhaltskomponente löschen, aber ihren Liquid-Tag in der Basisnachricht belassen, wird die Nachricht beim Senden möglicherweise nicht wie erwartet gerendert. | Entfernen Sie alle nicht verwendeten `message_component`-Tags aus Ihrer Basisnachricht, bevor Sie den Canvas starten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehlerbehebung" }