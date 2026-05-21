---
nav_title: Inhalt QA
article_title: Qualitätssicherung von Inhalten mit KI
page_order: 4
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit KI direkt aus dem Nachrichten-Editor eine Qualitätssicherung für Ihre Nachrichteninhalte durchführen können."
---

# Qualitätssicherung von Inhalten mit BrazeAI {#content-qa-with-brazeai}

> Erfahren Sie, wie Sie Ihre Inhalte mit BrazeAI<sup>TM</sup> überprüfen können, damit Sie Rechtschreib- und Grammatikfehler, einen unangemessenen Tonfall oder beleidigende Sprache erkennen&#8212;bevor Sie auf „Senden“ drücken.

## Unterstützte Features {#supported-features}

Die folgenden Features werden unterstützt, um die Qualität Ihrer Inhalte zu verbessern:

| Feature | Beschreibung |
|----------------------------|-------------|
| Rechtschreib- und Grammatikprüfung | Prüft automatisch auf Rechtschreib- und Grammatikfehler in Ihrer Nachricht. Es schlägt Korrekturen vor und gibt Empfehlungen zur Verbesserung der Gesamtgenauigkeit des Inhalts. |
| Tonanalyse | Bewertet den Ton der Nachricht, um mögliche Probleme zu erkennen. So können Sie sicherstellen, dass der beabsichtigte Ton mit dem gewünschten Kommunikationsstil übereinstimmt und Missverständnisse oder unbeabsichtigte Beleidigungen vermieden werden. |
| Erkennung anstößiger Sprache | Scannt Ihre Nachricht auf potenziell beleidigende oder unangemessene Sprache. So können Sie Ihren Inhalt überarbeiten und eine respektvolle Kommunikation aufrechterhalten. |
| Versehentliche Inhaltsprüfung | Erkennt alle Einfügungen von Code, Markup-Sprache oder Testnachrichten, die möglicherweise unbeabsichtigt hinzugefügt wurden, einschließlich Liquid-Code, der für eine:n Testnutzer:in nicht gerendert wurde. |
| Unterstützung mehrerer Sprachen | Obwohl nicht offiziell von OpenAI unterstützt, kann GPT [mehrere Sprachen](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages) verstehen. Beachten Sie, dass Braze keine Informationen über die Sprache oder das Gebietsschema Ihres Textes weitergibt, wenn dieser an OpenAI gesendet wird. Daher können Ihre Ergebnisse je nach Sprache, in der Sie schreiben, variieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unterstützte Features" }

## Verwendung von BrazeAI<sup>TM</sup> zur Qualitätssicherung von Inhalten {#using-brazeaitm-to-qa-content}

{% alert note %}
Dieses Feature ist derzeit nur für SMS, Android-Push, iOS-Push und herkömmliche In-App-Nachrichten verfügbar.
{% endalert %}

1. Nachdem Sie eine mobile Push-Nachricht, eine SMS oder eine herkömmliche In-App-Nachricht verfasst haben, navigieren Sie zum Tab **Test**.
2. Suchen Sie den Abschnitt **Content QA with AI**.
3. Klicken Sie auf **Test Content**.

![Abschnitt „Content QA with AI“ im Tab „Test“.]({% image_buster /assets/img/content_qa_ai.png %})

## Best Practices {#best-practices}

Beachten Sie die folgenden Punkte, damit Sie das Beste aus der Qualitätssicherung von Inhalten mit KI herausholen können:

- **Lesen Sie Ihre Nachricht Korrektur:** Obwohl die Inhaltsprüfung bei der Identifizierung von Fehlern helfen kann, ist es dennoch unerlässlich, Ihre Inhalte manuell zu korrigieren. Verlassen Sie sich auf die von der KI generierten Vorschläge als hilfreiche Orientierungshilfe, aber nutzen Sie Ihr Urteilsvermögen, um die Genauigkeit sicherzustellen.
- **Verstehen Sie die Tonanalyse:** Die Ergebnisse der Tonanalyse sind subjektiv und basieren auf dem Verständnis des KI-Modells. Sie können zwar nützliche Insights liefern, aber Sie sollten Ihren beabsichtigten Tonfall und den Kontext des Gesprächs berücksichtigen, um entsprechende Anpassungen vorzunehmen.
- **Überprüfen Sie die markierte anstößige Sprache:** Die Erkennung anstößiger Sprache ist so konzipiert, dass sie robust ist, aber es kann gelegentlich zu falsch positiven Ergebnissen kommen. Überprüfen Sie die markierten Abschnitte sorgfältig und nehmen Sie bei Bedarf entsprechende Änderungen vor.

{% multi_lang_include brazeai/generative_ai/policy.md %}