---
nav_title: Liquid-Code
article_title: Liquid-Code mit BrazeAI generieren
description: "In diesem Artikel erfahren Sie, wie der KI-Liquid-Assistent funktioniert und wie Sie ihn nutzen können, um Liquid-Snippets für Ihr Messaging zu generieren."
page_type: reference
page_order: 0.0
---

# Liquid-Code mit BrazeAI generieren {#generate-liquid-code-with-brazeai}

> Der BrazeAI<sup>TM</sup> Liquid Assistant ist ein von BrazeAI<sup>TM</sup> betriebener Chat-Assistent, der Ihnen hilft, das Liquid zu generieren, das Sie für die Personalisierung von Nachrichteninhalten benötigen.

## Über den BrazeAI<sup>TM</sup> Liquid-Assistenten {#about-the-brazeaitm-liquid-assistant}

Der BrazeAI<sup>TM</sup> Liquid Assistant wurde entwickelt, um Ihnen beim Schreiben von effektivem Liquid-Code zu helfen, der auf Ihre Marketingbedürfnisse zugeschnitten ist. Unsere KI ist sowohl auf die Liquid-Syntax als auch auf die Art und Weise, wie Marketer Liquid in ihren Nachrichten verwenden, trainiert und versteht die Feinheiten der Erstellung personalisierter Inhalte.

Darüber hinaus stellt unser BrazeAI<sup>TM</sup> Liquid Assistant durch die Bereitstellung Ihrer angepassten Attributnamen (z. B. „favourite_color“) und Datentypen (z. B. Boolescher Wert und String) sicher, dass Ihre Nachrichten präzise ausgerichtet sind und Ihren Zielen entsprechen. Wenn Sie außerdem Markenrichtlinien erstellen, kann der BrazeAI<sup>TM</sup> Liquid Assistant die Markenrichtlinien verwenden, um die generierten Ausgaben besser zu personalisieren und den Inhalt an Ihre eigene Markensprache anzupassen. Die von Ihnen erstellten Markenrichtlinien werden nur zur Personalisierung von Inhalten für Ihren eigenen Gebrauch verwendet.

## Unterstützte Kanäle {#supported-channels}

Sie können den BrazeAI<sup>TM</sup> Liquid Assistant bei der Erstellung folgender Inhalte verwenden:
- SMS-Nachrichten
- Push-Benachrichtigungen
- HTML-E-Mail-Nachrichten
- Canvases

{% alert note %}
Der Assistent arbeitet mit E-Mail-Nachrichten und nicht mit Templates. Er funktioniert am besten mit E-Mail-Nachrichten, die bereits erstellt sind.
{% endalert %}

## Liquid-Code generieren {#generating-liquid-code}

Um den BrazeAI<sup>TM</sup> Liquid Assistant zu starten, wählen Sie das KI-Assistenten-Symbol im Nachrichten-Editor.

![Nachrichten-Editor mit dem KI-Assistenten.]({% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}){: style="max-width:50%;"}

Sie können einen der enthaltenen Prompts auswählen oder Ihren eigenen in das Textfeld eingeben.

{% tabs local %}
{% tab use app activity %}
Der Prompt **Use app activity** generiert Liquid-Code, mit dem Sie verschiedene Nachrichten senden können, je nachdem, wann Ihre App zuletzt verwendet wurde. Möglicherweise werden Ihnen Anschlussfragen gestellt, damit der Assistent ein genaueres Ergebnis generieren kann.

![Beispielausgabe des Prompts „Use app activity“.]({% image_buster /assets/img/ai_liquid/use_app_activity.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab add countdown %}
Dieser Prompt generiert Liquid-Code, der eine Nachricht mit der verbleibenden Zeit bis zu einem Ereignis versendet. Sie werden aufgefordert, Angaben zu Datum und Uhrzeit des Ereignisses zu machen.

![Beispielausgabe des Prompts „Add countdown“.]({% image_buster /assets/img/ai_liquid/add_countdown.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab inspire me %}
Dieser Prompt erscheint, wenn Ihr Nachrichtenfeld Inhalt enthält. Er generiert eine Liste mit Optionen, aus denen Sie wählen können, um Ihre Nachricht mit Liquid zu personalisieren.

![Beispielausgabe des Prompts „Inspire me“.]({% image_buster /assets/img/ai_liquid/inspire_me.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab improve my liquid %}
Dieser Prompt erscheint, wenn Ihr Nachrichten-Editor Inhalt enthält. Wählen Sie ihn, wenn Sie möchten, dass der Assistent Ihren Code effizienter und leichter lesbar macht.

![Beispielausgabe des Prompts „Improve my Liquid“.]({% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}){: style="max-width:45%;"}
{% endtab %}
{% endtabs %}

Um Ihren Liquid-Code zu generieren, wählen Sie **Update composer**.

![KI-Assistenten-Fenster mit bereitgestellten Prompts.]({% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}){: style="max-width:50%;"}

Sie können eine weitere Nachricht mit demselben Prompt generieren, indem Sie **Regenerate** wählen. Um die Nachricht zu entfernen und zur vorherigen zurückzukehren, wählen Sie **Undo update**.

## Liquid-Attribute {#supported-attributes}

Die folgenden Attribute befinden sich derzeit in der Beta-Phase für den BrazeAI<sup>TM</sup> Liquid Assistant:

| Kriterium | Art des Wissens |
| - | - |
| Liquid (einschließlich `for`-Schleifen, `if`-Anweisungen, Mathematik und andere) | Codierung |
| Standard- und Standard-Nutzerattribute | Attribute |
| Angepasste Attribute mit einem der folgenden Datentypen: {::nomarkdown}<ul><li>Boolesche Werte</li><li>Zahlen</li><li>Strings</li><li>Arrays</li><li>Zeit</li></ul>{:/} | Attribute |
| Connected-Content | Codierung |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid attributes" }

## Best Practices {#best-practices}

Wenn Sie Hilfe beim Schreiben effektiver Prompts für den BrazeAI<sup>TM</sup> Liquid Assistant benötigen, lesen Sie unsere Best Practices:

### Natürliche Sprache verwenden {#use-natural-language}

Der BrazeAI<sup>TM</sup> Liquid Assistant ist darauf trainiert, natürliche Sprache zu verstehen. Sprechen Sie mit ihm wie mit einer Kollegin oder einem Kollegen, wenn Sie um Hilfe bitten. Das macht es dem Assistenten leichter, Ihre Bedürfnisse zu verstehen und präzise Hilfe zu leisten.

### Kontext geben {#give-context}

Die Bereitstellung von Kontext hilft dem BrazeAI<sup>TM</sup> Liquid Assistant, das Gesamtbild Ihres Projekts zu verstehen. Es ist hilfreich, Kontext einzubeziehen, z. B.:

- Ihr Unternehmensname und Ihre Branche
- Eine Campaign, an der Sie gerade arbeiten, wie z. B. Black Friday oder Weihnachtsverkauf
- Ihr Ziel, z. B. die Erhöhung Ihrer Click-through-Rate
- Spezifische angepasste Attribute, die Sie in Ihre Nachricht aufnehmen möchten

Wenn Sie den Kontext in Ihren Prompt aufnehmen, kann der Assistent seine Antworten besser auf Ihre Bedürfnisse abstimmen. Sie können auch Details aus Ihrer Campaign, Ihrem Nachrichten-Briefing oder Ihrem Brainstorming-Dokument einfügen, um den Assistenten auf den neuesten Stand zu bringen.

### Konkret sein {#be-specific}

Der BrazeAI<sup>TM</sup> Liquid Assistant kann Anschlussfragen stellen, aber die Angabe von Details im Vorfeld kann schneller zu präziseren Ergebnissen führen. Erwägen Sie, Details wie die folgenden anzugeben:

- Alle bekannten Präferenzen oder Anforderungen an die Nachricht
- Anweisungen für den Umgang mit Situationen, wie z. B. fehlende Antworten der Empfängerin oder des Empfängers oder Fallback-Nachrichtenoptionen
- Wenn Sie nach Liquid fragen, das Connected-Content verwendet, die Dokumentation für den API-Endpunkt, eine Beispiel-API-Antwort oder beides

### Kreativ werden {#get-creative}

Denken Sie bei Ihren Prompts über den Tellerrand hinaus und sehen Sie, wie der BrazeAI<sup>TM</sup> Liquid Assistant Ihr Messaging verbessern kann. Experimentieren Sie mit verschiedenen Prompts und Ideen, denn Kreativität kann zu ansprechenderen Ergebnissen führen.

## Beispiel-Prompts {#example-prompts}

Hier finden Sie einige Beispiele, die Ihnen den Einstieg erleichtern:

{% tabs local %}
{% tab gaining knowledge %}
- Was ist Liquid und wie kann es mir helfen, die Personalisierung meiner Marketing-Campaigns in Braze zu verbessern?
- Welche Arten von Daten kann ich in Liquid verwenden, um meine Marketingnachrichten zu personalisieren, z. B. demografische Informationen oder frühere Käufe?
{% endtab %}

{% tab personalizing dynamic content %}
- Erstellen Sie eine Nachricht, die je nach Treuestatus meiner Kund:innen unterschiedliche Inhalte anzeigt. Wenn wir nichts über den Treuestatus wissen, senden Sie eine Fallback-Nachricht.
- Schreiben Sie eine dynamische Nachricht, die das Lieblingsprodukt einer Nutzerin oder eines Nutzers und das Datum des letzten Kaufs enthält. Wenn es keinen letzten Kauf gibt, brechen Sie die Nachricht ab.
- Schreiben Sie mir Liquid, um jemanden zu ermutigen, auf meine Nachricht zu klicken, die einen Countdown mit der verbleibenden Zeit enthält. Wenn das Angebot abgelaufen ist, brechen Sie die Nachricht ab.
- Helfen Sie mir, eine Nachricht zu verfassen, die Nutzer:innen ermutigt, zurückzukehren und zur Kasse zu gehen, wenn sie noch Artikel in ihrem Warenkorb haben.
- Schreiben Sie Liquid, um eine Nachricht basierend auf dem Land einer Kundin oder eines Kunden zu personalisieren. Ich möchte die Nachricht mit dem Namen des Landes füllen. Wenn wir keines von beiden haben, schlagen Sie vor, auf einen Link zu klicken, um das Profil zu aktualisieren.
- Wie kann ich eine Begrüßungsnachricht mit dem Vornamen einer Nutzerin oder eines Nutzers personalisieren und je nach Geschlecht unterschiedliche Texte verfassen?
- Schreiben Sie Liquid, um verschiedene Nachrichten basierend auf einem angepassten Attribut „CUSTOM_ATTRIBUTE_NAME“ und dessen Wert anzuzeigen. Es gibt sechs verschiedene Optionen, die ich senden könnte. Wenn es keinen Wert für das angepasste Attribut gibt, möchte ich eine Platzhalter-Nachricht senden.
{% endtab %}

{% tab handling outliers %}
- Können Sie mir einige Beispiele dafür nennen, wie Liquid in Marketing-Campaigns eingesetzt wird, um Engagement und Conversion-Raten zu steigern?
- Welche gängigen Anwendungsfälle gibt es für Liquid in SMS-Nachrichten für den Sommerschlussverkauf, z. B. Erinnerungen an einen Warenkorb-Abbruch oder personalisierte Aktionen?
{% endtab %}
{% endtabs %}

{% alert tip %}
Lassen Sie uns wissen, ob Sie interessante Prompts oder Erfahrungen gemacht haben, indem Sie eine [Feedback-Sitzung](https://research.rallyuxr.com/braze/schedule/clxxhw8em0d071ak4b279553s?channel=share) mit uns buchen.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/policy.md %}