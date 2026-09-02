---
nav_title: Entscheidungsagenten entwerfen
article_title: Entscheidungsagenten entwerfen
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt wichtige Konzepte und Best Practices für das Entwerfen und Konfigurieren Ihres Entscheidungsagenten."
---

# Entscheidungsagenten entwerfen {#design-decisioning-agents}

> Dieser Referenzartikel behandelt wichtige Konzepte und Best Practices für das Entwerfen und Konfigurieren Ihres Entscheidungsagenten.

## Über Entscheidungsagenten {#about-decisioning-agents}

Das Entwerfen Ihres Entscheidungsagenten ist der erste Schritt bei der Einrichtung von Decisioning Studio. Damit der Entscheidungsagent Entscheidungen treffen kann, müssen Sie definieren, welches Ergebnis Sie maximieren möchten und welche Aktionen der Agent dafür ausführen kann.

### Wichtige Konzepte {#key-concepts}

Die folgenden Begriffe werden im gesamten Decisioning-Studio-Leitfaden verwendet.

| Begriff | Definition |
| --- | --- |
| **Entscheidungsagent** | Ein Entscheidungsagent ist eine angepasste Konfiguration für BrazeAI Decisioning Studio™, die speziell auf ein bestimmtes Geschäftsziel zugeschnitten ist. Er wird durch die Erfolgsmetrik, Dimensionen und Optionen definiert, die Sie auswählen. |
| **Erfolgsmetrik** | Die spezifische Geschäftsmetrik, für die Sie optimieren möchten, z. B. Umsatz, Conversions oder durchschnittlicher Umsatz pro Nutzer:in (ARPU). Dies ist die Metrik, die der Entscheidungsagent durch seine Aktionen zu maximieren versucht. |
| **Dimensionen** | Dimensionen können als die *Arten von Hebeln* betrachtet werden, die der Entscheidungsagent nutzen kann, um die Erfolgsmetrik zu maximieren. Typische Dimensionen umfassen Angebot, Betreffzeile, Kreativ, Kanal oder Sendezeit. |
| **Aktionsbank** | Die Aktionsbank definiert die *spezifischen Optionen*, auf die der Entscheidungsagent für jeden Dimensions-„Hebel“ zugreifen kann. Beispielsweise definieren Sie für eine Kanal-Dimension die spezifischen Kanäle, auf die der Entscheidungsagent zugreifen kann. Für eine Angebots-Dimension definieren Sie die spezifischen Angebote, die der Entscheidungsagent testen kann. |
| **Einschränkungen** | Grundsätzlich könnte der Entscheidungsagent jede Kombination von Aktionen ausführen, die Sie in die Aktionsbank aufnehmen. Sie können jedoch auch Einschränkungen definieren, um die Aktionen des Entscheidungsagenten zu begrenzen und wichtige Geschäftsregeln einzuhalten. Dies könnte beispielsweise verhindern, dass ein bestimmtes Angebot für Kund:innen in einer nicht berechtigten Region ausgewählt wird, oder ein maximales Budget festlegen, das der Entscheidungsagent ausgeben darf. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wichtige Konzepte" }

![Ein allgemeiner Überblick über einen Entscheidungsagenten]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
Der Entscheidungsagent kann nur Aktionen ausführen, die *Sie* konfigurieren und zur Aktionsbank hinzufügen. Das bedeutet, dass alle möglichen Aktionen durch die Kombinationen dessen definiert werden, was Sie in die Aktionsbank aufnehmen.
{% endalert %}

## So entwerfen Sie Ihren Entscheidungsagenten {#how-to-design-your-decisioning-agent}

Beim Einrichten eines Entscheidungsagenten müssen Sie vier zentrale Designelemente durchdenken:

### Das „Ziel“: Definieren Sie Ihre Erfolgsmetrik {#the-goal-define-your-success-metric}

*Welches Ergebnis soll der Agent maximieren?*

Ihre Erfolgsmetrik ist das Geschäftsergebnis, für das der Agent optimiert. Dies sollte direkt mit Ihren Geschäftszielen übereinstimmen – nicht Proxy-Metriken wie Klicks oder Öffnungen, sondern echte Geschäftsergebnisse wie Umsatz, Conversions, ARPU oder Kund:innen-LTV or Lifetime-Value or Lifetime-Value.

### Das „Wer“: Wählen Sie Ihre Zielgruppe aus {#the-who-select-your-audience}

*Wen soll der Entscheidungsagent ansprechen?*

Definieren Sie die Zielgruppe, die Ihr Agent bedienen soll. Dies könnten alle Kund:innen sein, ein bestimmtes Segment (wie Mitglieder eines Kundenbindungs-Programms) oder Kund:innen in einer bestimmten Phase ihres Lebenszyklus (wie kürzliche Käufer:innen oder gefährdete Abonnent:innen).

### Das „Was“: Konfigurieren Sie Ihre Aktionsbank {#the-what-configure-your-action-bank}

*Aus welchen Optionen kann der Agent wählen, um das Ergebnis zu erzielen?*

Die Aktionsbank definiert alle Hebel, die der Agent nutzen kann: die Dimensionen (wie Kanal, Angebot, Timing und Häufigkeit) und die spezifischen Optionen innerhalb jeder Dimension. Der Agent experimentiert mit verschiedenen Kombinationen dieser Optionen, um herauszufinden, was für jede:n Kund:in am besten funktioniert.

### Das „Wie“: Konfigurieren Sie Ihre Einschränkungen {#the-how-configure-your-constraints}

*Welche Regeln soll der Agent befolgen?*

Einschränkungen sind die Regeln, die der Agent einhalten muss. Dies könnte verhindern, dass ein bestimmtes Angebot für Kund:innen in einer nicht berechtigten Region ausgewählt wird, oder ein maximales Budget festlegen, das der Entscheidungsagent ausgeben darf.

## Best Practices und Beispiele {#best-practices-and-examples}

Um die Wirkung Ihres Entscheidungsagenten zu maximieren, sollten Sie:

- Eine Erfolgsmetrik wählen, die eng mit Ihren Geschäftszielen übereinstimmt, wie Umsatz, Conversions oder ARPU.
- Sich auf die Dimensionen oder „Hebel“ zum Testen konzentrieren, wie Angebot, Betreffzeile, Kreativ, Kanal oder Sendezeit, die am wahrscheinlichsten einen signifikanten Einfluss auf die Erfolgsmetrik haben.
- Die Optionen für jede Dimension auswählen, wie E-Mail versus Kurzmitteilungsdienst or SMS oder tägliche versus wöchentliche Häufigkeit, die am wahrscheinlichsten einen signifikanten Einfluss auf die Erfolgsmetrik haben.

Einige Beispiele für Entscheidungsagenten, die Sie erstellen könnten:

{% tabs %}
{% tab Wiederholungskauf-Agent %}
Sie könnten einen Wiederholungskauf-Agenten erstellen, um Folge-Conversions nach einem ersten Kauf zu steigern:

- Definieren Sie die Zielgruppe und Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Kombinationen von Produktangeboten, Nachrichtentiming und Häufigkeit für jede:n Kund:in
- Im Laufe der Zeit lernt BrazeAI<sup>TM</sup>, was für jede:n Kund:in am besten funktioniert
- Orchestriert personalisierte Sendungen über Braze, um die Wiederkaufraten zu maximieren
{% endtab %}
{% tab Cross-Sell- oder Upsell-Agent %}
Sie könnten einen Cross-Sell- oder Upsell-Agenten erstellen, um den durchschnittlichen Umsatz pro Nutzer:in (ARPU) aus Internet-Abos zu maximieren:

- Definieren Sie die Zielgruppe und Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Kombinationen von Nachrichten, Sendezeiten, Rabatten und Tarifangeboten für jede:n Kund:in
- BrazeAI<sup>TM</sup> lernt, welche Kund:innen für Leapfrog-Angebote empfänglich sind und welche Rabatte oder andere Anreize zum Upgraden benötigen
- Orchestriert personalisierte Sendungen über Braze, um den ARPU zu maximieren
{% endtab %}
{% tab Verlängerungs- und Bindungs-Agent %}
Sie könnten einen Verlängerungs- und Bindungs-Agenten erstellen, um Vertragsverlängerungen zu sichern und sowohl die Vertragslaufzeit als auch den Nettobarwert (NPV) zu maximieren:

- Definieren Sie die Zielgruppe und Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Verlängerungsangebote für jede:n Kund:in
- BrazeAI<sup>TM</sup> identifiziert Kund:innen, die weniger preissensibel sind und weniger signifikante Rabatte zur Verlängerung benötigen
- Orchestriert personalisierte Sendungen über Braze, um Vertragsverlängerungen und den NPV zu maximieren
{% endtab %}
{% tab Rückgewinnungs-Agent %}
Sie könnten einen Rückgewinnungs-Agenten erstellen, um die Reaktivierung zu steigern, indem ehemalige Abonnent:innen zur erneuten Anmeldung ermutigt werden:

- Definieren Sie die Zielgruppe und Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet Tausende von Variablen gleichzeitig, darunter Kreativ, Nachricht, Kanal und Kadenz
- BrazeAI<sup>TM</sup> ermittelt die beste Kombination für jede:n einzelne:n Kund:in
- Orchestriert personalisierte Sendungen über Braze, um die Reaktivierungsraten zu maximieren
{% endtab %}
{% tab Empfehlungs-Agent %}
Sie könnten einen Empfehlungs-Agenten erstellen, um neue Konten zu maximieren, die durch Geschäftskreditkarten-Empfehlungen von bestehenden Kund:innen eröffnet werden:

- Definieren Sie die Zielgruppe und Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene E-Mails, Kreative, Sendezeiten und Kreditkartenangebote für jede:n Kund:in
- BrazeAI<sup>TM</sup> ermittelt die ideale Kombination für bestimmte Kund:innen
- Orchestriert personalisierte Sendungen über Braze, um Empfehlungs-Conversions zu maximieren
{% endtab %}
{% tab Lead-Nurturing- und Conversion-Agent %}
Sie könnten einen Lead-Nurturing- und Conversion-Agenten erstellen, um inkrementellen Umsatz zu erzielen und den richtigen Betrag für jede:n Kund:in zu zahlen:

- Definieren Sie die Zielgruppe und Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Kundensegmente, Bietmethoden, Gebotshöhen und Kreative
- BrazeAI<sup>TM</sup> nutzt robuste First-Party-Daten, um die Performance bezahlter Anzeigen zu optimieren, während sich Datenschutzrichtlinien ändern
- Orchestriert personalisierte Sendungen über Braze, um den Umsatz zu maximieren und gleichzeitig die Kosten pro Kund:in zu optimieren
{% endtab %}
{% tab Kundenbindungs- und Engagement-Agent %}
Sie könnten einen Kundenbindungs- und Engagement-Agenten erstellen, um Käufe von neuen Teilnehmer:innen eines Kundenbindungs-Programms zu maximieren:

- Definieren Sie die Zielgruppe und Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene E-Mail-Angebote, Sendezeiten und Häufigkeiten für jede:n Kund:in
- BrazeAI<sup>TM</sup> lernt, was für jede:n neue:n Teilnehmer:in im Kundenbindungs-Programm am besten funktioniert
- Orchestriert personalisierte Sendungen über Braze, um Kauf- und Wiederkaufraten zu maximieren
{% endtab %}
{% endtabs %}

## Nächste Schritte {#next-steps}

Bereit, Ihren eigenen Entscheidungsagenten zu erstellen? Unter [Erste Schritte mit Decisioning Studio]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/get_started) finden Sie einen Leitfaden, der Sie durch das Verbinden von Datenquellen, das Einrichten der Orchestrierung, das Entwerfen Ihres Agenten und den Start in die Produktion führt.