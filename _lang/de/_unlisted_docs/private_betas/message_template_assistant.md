---
nav_title: Template Assistant
article_title: Template Assistant
permalink: "/template_assistant/"
description: "Dieser Referenzartikel beschreibt, wie Sie den Template Assistant für Nachrichten verwenden, um Templates für Ihr E-Mail-Messaging zu generieren."
page_type: reference
---

# Template Assistant für Nachrichten {#message-template-assistant}

> Der Template Assistant für Nachrichten hilft Ihnen, ein bestehendes HTML-E-Mail-Template zu iterieren, indem er GenAI nutzt, um Templates basierend auf Ihren spezifischen Anforderungen zu generieren. Diese Funktionalität kann Ihnen helfen, Ihren Inhalt für einen bestimmten Anwendungsfall, eine bestimmte Zielgruppe oder eine bestimmte Conversion zu optimieren und den Zeit- und Arbeitsaufwand beim Verfassen von E-Mails zu reduzieren.

{% alert important %}
Der Template Assistant für Nachrichten befindet sich im Early Access. Kontaktieren Sie Ihren Customer-Success-Manager, wenn Sie an diesem Early Access teilnehmen möchten. <br><br>Diese Funktionalität wird derzeit nur für den E-Mail-Kanal und nur im HTML-Editor unterstützt, nicht in anderen Editoren (wie Drag-and-Drop oder AMP).
{% endalert %}

## Funktionsweise {#how-it-works}

Der Template Assistant für Nachrichten verwendet Ihre [Markenrichtlinien](https://www.braze.com/docs/user_guide/administrative/app_settings/brand_guidelines) und [globalen Stileinstellungen](https://www.braze.com/docs/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings), um den Nachrichteninhalt und -stil an Ihre Marke anzupassen.

Wenn Sie beispielsweise globale Stileinstellungen eingerichtet haben, wird der Template Assistant für Nachrichten die Farben und Stile Ihrer Marke einbeziehen. Wenn Sie Markenrichtlinien in Braze definiert haben, kann der Assistent diese ebenfalls referenzieren, um Texte im Ton und in der Persönlichkeit Ihrer Marke zu erstellen.

Der Template Assistant für Nachrichten kann sich nur an Ihren Chatverlauf erinnern, solange Sie sich noch im selben Chatfenster befinden. Das bedeutet, dass er möglicherweise auf frühere Prompts zurückgreift, die zur Generierung zukünftiger Prompts verwendet wurden. Der Assistent wird außerdem versuchen, Ihr Template für mobile Responsivität zu iterieren.

Wenn Sie beispielsweise von einem Prompt, der sich speziell auf eine Fitnessmarke bezieht, in Ihren nachfolgenden Prompts zu einer generischen Marke wechseln, kann der Template Assistant für Nachrichten das Template dahingehend informieren, dass es sich um dieselbe Fitnessmarke handelt. Um einen neuen Chat zu starten, wählen Sie **Verlauf löschen** im Chatfenster und öffnen Sie den Template Assistant für Nachrichten erneut.

## Ein Template erstellen {#creating-a-template}

1. Gehen Sie im Dashboard zu **Templates** > **E-Mail-Templates**.
2. Wählen Sie ein bestehendes E-Mail-Template aus.
3. Wählen Sie im Abschnitt **Mit KI erstellen** des HTML-Editors **Template** aus.
4. Von hier aus können Sie verschiedene Prompts eingeben oder Fragen zu Ihrem Inhalt stellen.
5. Der Template Assistant für Nachrichten liefert eine Antwort und bestimmt, welche Änderungen an Ihrem Template erforderlich sind.
6. Wählen Sie **Generieren**, um die Vorschläge anzuwenden.

{% alert important %}
Wir empfehlen dringend, die generierte Ausgabe zu testen, um sicherzustellen, dass sie zu Ihrem Messaging passt.
{% endalert %}

![Ein Beispiel-Prompt zum Erstellen eines Templates mit mehreren Abschnitten, das für mehrere E-Mails verwendet werden soll. Der Template Assistant für Nachrichten erklärt die Änderungen am aktuellen Template.]({% image_buster /assets/unlisted_docs/img/ai_message_template_assistant1.png %}){: style="width:70%;"}

### Beispiel-Prompts {#example-prompts}

Hier sind einige Beispiel-Prompts für den Einstieg:

- Eine Feedback-Umfrage am Ende der E-Mail hinzufügen
- Schriftart auf {% raw %}`{{font name}}` und Schriftgröße des Absatzes auf Größe `{{number}}`{% endraw %} ändern
- Allen Bildern abgerundete Ecken geben
- Einen weiteren Abschnitt mit einem Bild und einem Call-to-Action hinzufügen

{% alert note %}
Abhängig von Ihrem Prompt und der Antwort kann der Template Assistant für Nachrichten beim Generieren des neuen Templates Platzhalterbilder hinzufügen.
{% endalert %}