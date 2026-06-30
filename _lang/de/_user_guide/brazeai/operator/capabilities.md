---
nav_title: Funktionen
article_title: Was Sie mit Operator tun können
page_order: 1
page_type: reference
toc_headers: h2
description: "Dieser Referenzartikel behandelt die KI-Aufgaben, die über BrazeAI Operator™ verfügbar sind – einschließlich Texterstellung, Liquid, Bildgenerierung, Datentransformationscode und Inhaltsüberprüfung."
---

# Was Sie mit Operator tun können {#operator-capabilities}

> Die KI-Funktionen, die zuvor als eigenständige Assistenten verfügbar waren, sind jetzt über [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) zugänglich. Da Operator in das Dashboard integriert ist und Ihren Workspace versteht (Ihre Markenrichtlinien, Attribute, Connected-Content und die Seite, an der Sie arbeiten), ist die Ausgabe kontextbewusster als das, was die vorherigen Assistenten liefern konnten.

Anstatt für jede Aufgabe ein anderes Tool zu öffnen, beschreiben Sie in natürlicher Sprache, was Sie möchten, und Operator erledigt es im Kontext. Sie können auch das Gespräch fortsetzen – nach einem anderen Ton, einer kürzeren Version oder einer Übersetzung fragen – ohne von vorne zu beginnen. Operator kann auch Änderungen direkt über [Aktionskarten]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) vorschlagen und ausführen, die Sie überprüfen, bevor sie wirksam werden.

## Voraussetzungen {#prerequisites}

Operator hat dieselben Berechtigungen wie Sie, daher erfordern bestimmte Aktionen die entsprechende Berechtigung für die jeweilige Oberfläche – zum Beispiel erfordert die Bildgenerierung *Medienbibliothek-Assets bearbeiten*. Wenn Sie keinen Einstiegspunkt sehen, überprüfen Sie Ihre Berechtigungen bei Ihrem Admin. Weitere Informationen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

## Was über Operator verfügbar ist {#whats-available-through-operator}

Alle bestehenden Einstiegspunkte bleiben erhalten, sodass Ihre Workflows nicht beeinträchtigt werden. Diese Erlebnisse werden jetzt von Operator unterstützt. Die folgende Tabelle ordnet jeden früheren eigenständigen Assistenten seinem neuen Standort zu.

| Früherer Assistent | Was er tat | Wo Sie ihn jetzt finden |
| --- | --- | --- |
| AI Copywriter | Generierte Marketing-Texte aus einem Produktnamen oder einer Beschreibung | Ein neues **Ask Operator**-Symbol in den SMS-, Push-, HTML-E-Mail- und Canvas-Editoren |
| AI Liquid Assistant | Generierte Liquid für die Personalisierung | Ein neues **Ask Operator**-Symbol in den SMS-, Push-, HTML-E-Mail- und Canvas-Editoren |
| AI Image Generator | Generierte Bilder aus einem Text-Prompt für die Medienbibliothek | Ein neuer **Generate with Operator**-Button in der Medienbibliothek |
| Data Transformations AI Copilot | Generierte Transformationscode | Der **Insert Code**-Button auf der Datentransformationsseite |
| Inhaltsüberprüfung | Prüfte Inhalte auf Rechtschreibung, Grammatik, Ton, anstößige Sprache und fehlerhaften Code | **Review with Operator**-Button auf dem **Test**-Tab |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Was über Operator verfügbar ist" }

## Markenrichtlinien anwenden {#apply-brand-guidelines}

Operator verwendet die in Ihrem Workspace konfigurierten Markenrichtlinien, damit generierte Texte, Templates und Bilder zur Stimme, zum Ton und zum Stil Ihrer Marke passen. Um Markenrichtlinien einzurichten, gehen Sie zu **Inhalt** > **Markenrichtlinien**. Weitere Informationen finden Sie unter [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines). Details zur Anwendung von Markenrichtlinien für die Nutzung mit Operator finden Sie unter [Markenrichtlinien anwenden]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines).

## Texte generieren {#generate-copy}

Sie können Operator nutzen, um von überall aus Texte zu brainstormen oder zu generieren, aber das beste Erlebnis erhalten Sie, wenn Sie es direkt im Nachrichten-Editor verwenden, wo es Sie bei der Nachricht, die Sie erstellen, unterstützen kann. Beschreiben Sie Ihr Produkt oder Ihre Campaign, und Operator liefert Texte, die Sie überprüfen und einfügen können.

Operator verbessert den eigenständigen Copywriter auf mehrere Arten:

- Es wendet Ihre [Markenrichtlinien](#apply-brand-guidelines) automatisch an, wenn diese konfiguriert sind.
- Es nutzt [seitenbezogenen Kontext]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context), sodass Sie den Kanal oder die Nachricht, an der Sie arbeiten, nicht erneut beschreiben müssen. Da es seitenbezogen ist, können Sie es auch verwenden, um eine bestehende Nachricht zu bearbeiten oder zu verfeinern, anstatt eine von Grund auf neu zu generieren.
- Es kann Ihre [angepassten Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) und Events nachschlagen, sodass Sie es bitten können, Textempfehlungen mit echtem Liquid zu personalisieren.
- Sie können das Gespräch fortsetzen und iterieren. Fragen Sie zum Beispiel nach einem anderen Ton, einer kürzeren Version oder einer Übersetzung.

### Tonalität {#generate-copy-tones}

Die Tonalität des generierten Textes wird durch Ihren Prompt bestimmt. Beschreiben Sie den gewünschten Stil – zum Beispiel formell, locker, dringend oder auffällig – und Operator passt seine Ausgabe entsprechend an. Sie können die Tonalität auch in Folgeprompts verfeinern, zum Beispiel nach einer entspannteren oder ausgefeilteren Version fragen. Wenn [Markenrichtlinien](#apply-brand-guidelines) konfiguriert sind, wendet Operator diese automatisch an, damit Texte konsistent mit der Stimme Ihrer Marke bleiben.

### Beispiel-Prompts {#generate-copy-example-prompts}

{% include copy_block.html content="Write a short, eye-catching push notification announcing our summer sale." %}

{% include copy_block.html content="Rewrite this subject line in a more casual tone." %}

{% include copy_block.html content="Translate this copy into Spanish." %}

## Liquid generieren {#generate-liquid}

Öffnen Sie in jedem Nachrichten-Editor Operator, um Liquid für die Personalisierung zu generieren und zu verfeinern. Operator versteht die [Liquid-Syntax]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), Ihre Standard- und [angepassten Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) sowie [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) und kann erklären, was der Code tut.

### Wo Sie Liquid generieren können {#generate-liquid-supported-channels}

Wie bei der Texterstellung können Sie Operator von überall aus bitten, Liquid zu generieren, und es funktioniert über alle Kanäle und Nachrichten-Editoren hinweg. Die besten Ergebnisse erzielen Sie innerhalb eines Nachrichten-Editors, wo Operator den vollständigen Kontext der Nachricht hat, die Sie erstellen.

### Liquid-Funktionen {#generate-liquid-attributes}

Operator ist mit Liquid sehr leistungsfähig. Es kann komplexe Liquid-Logik generieren, die auf den Daten in Ihrem Workspace basiert – einschließlich der Suche nach [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs)-Daten, um Beispielwerte zu finden – und es kann das vorhandene Liquid in Ihren Campaigns überprüfen und erklären.

### Best Practices {#generate-liquid-best-practices}

#### Verwenden Sie natürliche Sprache {#generate-liquid-use-natural-language}

Operator ist darauf trainiert, natürliche Sprache zu verstehen. Chatten Sie mit ihm, wie Sie es mit einer Kollegin oder einem Kollegen tun würden, wenn Sie um Hilfe bitten. Das hilft Operator, Ihre Bedürfnisse zu verstehen und präzise Unterstützung zu bieten.

#### Geben Sie Kontext {#generate-liquid-give-context}

Kontext hilft Operator, das Gesamtbild Ihres Projekts zu verstehen. Es ist hilfreich, Kontext wie den folgenden einzubeziehen:

- Ihren Unternehmensnamen und Ihre Branche
- Eine Campaign, an der Sie arbeiten, wie Black Friday oder Feiertagsverkäufe
- Ihr Ziel, wie die Steigerung Ihrer Click-through-Rate
- Bestimmte angepasste Attribute, die Sie in Ihre Nachricht aufnehmen möchten

Das Einbeziehen von Kontext in Ihren Prompt hilft Operator, seine Antworten besser auf Ihre Bedürfnisse abzustimmen. Sie können auch Details aus Ihrer Campaign, Ihrem Nachrichten-Briefing oder Ihrem Brainstorming-Dokument einfügen, um Operator auf den neuesten Stand zu bringen.

#### Seien Sie spezifisch {#generate-liquid-be-specific}

Operator kann Rückfragen stellen, aber die Angabe von Details im Voraus kann schneller zu präziseren Ergebnissen führen. Erwägen Sie, Details wie die folgenden einzubeziehen:

- Bekannte Präferenzen oder Anforderungen für die Nachricht
- Anweisungen zum Umgang mit Situationen, wie fehlende Antworten von Empfänger:innen oder Fallback-Nachrichtenoptionen
- Genaue oder ähnliche Werte für die angepassten Attribute, die Sie verwenden möchten, die Operator helfen, genauere Logik zu generieren und zu testen
- Wenn Sie nach Liquid fragen, das Connected-Content verwendet, die Dokumentation für den API-Endpunkt, eine Beispiel-API-Antwort oder beides

#### Werden Sie kreativ {#generate-liquid-get-creative}

Probieren Sie verschiedene Prompts aus, um zu sehen, wie Operator Ihr Messaging verbessern kann. Experimentieren Sie mit verschiedenen Prompts und Ideen, da Kreativität zu ansprechenderen Ergebnissen führen kann.

### Beispiel-Prompts {#generate-liquid-example-prompts}

{% tabs local %}
{% tab Über Liquid %}

{% include copy_block.html content="What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?" %}

{% include copy_block.html content="What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?" %}

{% include copy_block.html content="Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?" %}

{% include copy_block.html content="What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?" %}

{% endtab %}
{% tab Personalisierung %}

{% include copy_block.html content="Add a countdown to this message that shows the time until the user's flight." %}

{% include copy_block.html content="Personalize this message with the user's first name, with a fallback if it's missing." %}

{% include copy_block.html content="Improve this Liquid so it's easier to read." %}

{% include copy_block.html content="Create a message that shows different content based on my customer's loyalty status. If we don't know about their loyalty status, send a fallback message." %}

{% include copy_block.html content="Write a dynamic message that includes a user's favorite product and their last purchase date. If there's no last purchase, abort the message." %}

{% include copy_block.html content="Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message." %}

{% include copy_block.html content="Help me write a message to encourage users to come back and check out if they have items remaining in their cart." %}

{% include copy_block.html content="Write Liquid to personalize a message based on a customer's country. I want to fill in the message with the country's name. If we don't have either of them, suggest they click on a link to update their profile." %}

{% include copy_block.html content="How can I personalize a welcome message with a user's first name and write different copy based on the user's gender?" %}

{% include copy_block.html content="Write Liquid to display different messages based on a custom attribute, \"CUSTOM_ATTRIBUTE_NAME\" and its value. There are six different options I could send. If there's no value for the custom attribute, I want to send a placeholder message." %}

{% endtab %}
{% endtabs %}

## Bilder generieren {#generate-images}

Operator generiert Bilder mit [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), einem KI-System von OpenAI und einem Drittanbieter von Braze. Damit können Sie realistische Bilder und Kunst aus einer Beschreibung in natürlicher Sprache erstellen.

Wählen Sie in der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) im Panel **Upload Assets** die Option **Generate with Operator** aus. Beschreiben Sie das gewünschte Bild, und Operator generiert es und speichert es direkt in Ihrer Medienbibliothek.

### Prompt-Tipps {#generate-images-prompt-tips}

- Beschreiben Sie das Motiv, den Stil, die Stimmung und die Farben konkret. Je mehr Details Sie angeben, desto besser das Ergebnis.
- Nur Texteingabe; das Hochladen eines Referenzbildes wird nicht unterstützt.
- Wenn Sie [Markenrichtlinien](#apply-brand-guidelines) als Kontext in Ihrem Operator-Prompt anwenden, wendet Operator diese direkt auf das generierte Bild an, sodass das Ergebnis den visuellen Stil Ihrer Marke widerspiegelt.
- Bildgenerierungen werden auf Ihr tägliches Operator-Nutzungslimit angerechnet. Weitere Informationen finden Sie unter [Einschränkungen]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting#limitations).

### Beispiel-Prompts {#generate-images-example-prompts}

{% include copy_block.html content="Generate a bright, summery banner image of a beach scene for an email header." %}

{% include copy_block.html content="Create a minimalist product background in our brand colors." %}

## Datentransformationscode generieren {#generate-data-transformation-code}

Wählen Sie im [Datentransformations]({{site.baseurl}}/user_guide/data/unification/data_transformation)-Editor **Insert Code** aus, um Transformationscode zu generieren, der eine eingehende Webhook-Payload in gültige Braze-API-Anfragen umwandelt.

Schritt-für-Schritt-Anleitungen zum Erstellen einer Transformation finden Sie unter [Transformation erstellen]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

### Beispiel-Prompts {#generate-data-transformation-example-prompts}

{% include copy_block.html content="Write transformation code that maps this survey webhook to a custom event on the user's profile." %}

{% include copy_block.html content="Update this transformation to identify users by email address instead of external ID." %}

## Inhaltsqualität überprüfen {#review-content-quality}

Wählen Sie auf dem **Test**-Tab für SMS, Android-Push, iOS-Push und traditionelle In-App-Nachrichten **Review with Operator** aus, um Ihre Inhalte vor dem Senden zu überprüfen. Standardmäßig prüft Operator Ihre Campaign auf Rechtschreib- und Grammatikfehler, markenfremden oder unangemessenen Ton, anstößige Sprache sowie fehlerhaften Code, Testinhalte oder nicht gerendertes Liquid und empfiehlt, wie gefundene Probleme behoben werden können. Sie können Operator auch direkt in Ihrem Prompt bitten, die Überprüfung Ihrer Inhalte anzupassen.

### Was Sie Operator prüfen lassen können {#review-content-quality-supported-features}

Über die Standardüberprüfung hinaus können Sie Operator auf bestimmte Prüfungen ausrichten. Erwägen Sie, es auf Folgendes prüfen zu lassen:

| Prüfung | Was Sie anfordern können |
| --- | --- |
| Rechtschreibung und Grammatik | Bitten Sie Operator, auf Rechtschreib- und Grammatikfehler zu prüfen und Korrekturen vorzuschlagen, die die Genauigkeit Ihrer Inhalte verbessern. |
| Tonalität | Bitten Sie Operator zu bewerten, ob die Tonalität zu Ihrem beabsichtigten Kommunikationsstil passt, und alles zu markieren, was missverstanden werden könnte. |
| Anstößige Sprache | Bitten Sie Operator, nach potenziell anstößiger oder unangemessener Sprache zu suchen, damit Sie diese überarbeiten und Ihr Messaging respektvoll halten können. |
| Unbeabsichtigte Inhalte | Bitten Sie Operator, fehlerhaften Code, Markup oder Testnachrichten zu erkennen, die Sie unbeabsichtigt hinzugefügt haben, einschließlich Liquid, das für eine:n Testnutzer:in nicht gerendert wurde. |
| Andere Sprachen | Bitten Sie Operator, Inhalte in einer anderen Sprache zu überprüfen. Die Unterstützung für nicht-englische Inhalte kann variieren, daher überprüfen Sie die Ergebnisse sorgfältig. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Was Sie Operator prüfen lassen können" }

### Best Practices {#review-content-quality-best-practices}

Beachten Sie Folgendes, um die Inhaltsüberprüfung optimal zu nutzen:

- **Lesen Sie Ihre Nachricht Korrektur:** Obwohl die Inhaltsüberprüfung helfen kann, Fehler zu identifizieren, ist es weiterhin wichtig, Ihre Inhalte manuell Korrektur zu lesen. Nutzen Sie die KI-generierten Vorschläge als hilfreiche Orientierung, aber verlassen Sie sich auf Ihr eigenes Urteil, um die Genauigkeit sicherzustellen.
- **Verstehen Sie die Tonalitätsanalyse:** Die Ergebnisse der Tonalitätsanalyse sind subjektiv und basieren auf dem Verständnis des KI-Modells. Obwohl sie nützliche Insights liefern können, berücksichtigen Sie Ihre beabsichtigte Tonalität und den Gesprächskontext, um angemessene Anpassungen vorzunehmen.
- **Überprüfen Sie markierte anstößige Sprache:** Die Erkennung anstößiger Sprache ist darauf ausgelegt, robust zu sein, kann aber gelegentlich falsch-positive Ergebnisse liefern. Überprüfen Sie markierte Abschnitte sorgfältig und nehmen Sie bei Bedarf entsprechende Änderungen vor.

### Beispiel-Prompts {#review-content-quality-example-prompts}

{% include copy_block.html content="Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it." %}

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Datenschutz und Sicherheit {#data-privacy-and-security}

Operator integriert sich mit OpenAI, um Ausgaben zu generieren. Weitere Informationen darüber, welche Daten Braze an OpenAI sendet, wie diese Daten verwendet werden und Ihre Rechte an geistigem Eigentum finden Sie unter [Wie Daten mit OpenAI verwendet werden]({{site.baseurl}}/user_guide/brazeai/operator#how-data-is-used-with-openai).

## Nächste Schritte {#next-steps}

- [Erste Schritte mit Operator]({{site.baseurl}}/user_guide/brazeai/operator): Zugriff auf und Nutzung von Operator
- [Aktionen überprüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Vorgeschlagene Änderungen von Operator überprüfen und genehmigen
- [Fehlerbehebung]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Häufige Probleme und Lösungen nachschlagen