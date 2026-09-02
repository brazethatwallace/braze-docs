---
nav_title: "A2P 10DLC"
article_title: "A2P 10DLC"
page_order: 2.9
description: "Dieser Artikel behandelt A2P 10DLC, warum die 10DLC-Registrierung für US-Langcode-Kund:innen notwendig ist, hilfreiche Informationen zu Kosten und Durchsatz sowie den Einstieg in die Registrierung."
page_type: reference
channel:
  - SMS

---

# Application-to-Person 10-Digit Long Codes {#application-to-person-10-digit-long-codes}

> A2P 10DLC bezeichnet ein System in den Vereinigten Staaten, das es Unternehmen ermöglicht, Application-to-Person-Nachrichten (A2P) über eine standardmäßige 10-stellige Langcode-Telefonnummer (10DLC) zu senden. Diese registrierten Langcodes erhalten einen höheren Durchsatz, eine bessere Zustellbarkeit und eine verbesserte Compliance im Vergleich zum Standard-Langcode.

{% alert important %}
Alle Kund:innen, die derzeit US-Langcodes besitzen und/oder nutzen, um Nachrichten an US-Kund:innen zu senden, müssen ihre Langcodes für 10DLC Registrierung. Wer dies nicht tut, muss mit einer starken Filterung aller Nachrichten rechnen. Dieser Antragsprozess dauert 4–6 Wochen.
{% endalert %}

## Warum es notwendig ist {#why-its-necessary}

Der 10DLC-Dienst wurde speziell entwickelt, um A2P-Messaging über Langcodes zu ermöglichen. Historisch waren Langcodes für Person-to-Person-Messaging (P2P) gedacht, aber wenn sie für Marketingzwecke verwendet wurden, führte dies zu eingeschränktem Durchsatz und verstärkter Filterung für Unternehmen.

10DLC hilft, diese Probleme zu lösen, indem es Folgendes bietet:
- **Höherer Durchsatz**: 10DLC-Nummern unterstützen ein höheres Nachrichtenvolumen als reguläre Langcodes.
- **Bessere Zustellbarkeit**: 10DLC-Nummern sind für A2P-Verkehr vorgesehen, sodass Nachrichten, die mit diesen Nummern gesendet werden, mit höherer Wahrscheinlichkeit die Empfänger:innen erreichen und weniger wahrscheinlich vom Mobilfunkanbieter gefiltert oder abgelehnt werden als Nachrichten, die über reguläre lokale Langcodes gesendet werden.
- **Verbesserte Compliance**: Die Verwendung eines lokalen Langcodes für kommerzielle Textnachrichten verstößt gegen die [CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)-Richtlinien. 10DLC-Nummern wurden für Massen-Messaging vorgesehen und ermöglichen es Marken, Branchenvorschriften einzuhalten, ohne auf Shortcodes angewiesen zu sein.
- **Budgetfreundlich**: 10DLC ist eine großartige Option für Unternehmen, die mit dem SMS-Versand beginnen oder SMS in kleinen Mengen versenden möchten. Für Marken, die größere Nachrichtenvolumen von über 100.000 Nachrichten pro Tag versenden, empfehlen wir die Verwendung eines Shortcodes.

Seit 2019 haben Mobilfunkanbieter begonnen, 10DLC für kommerzielles Messaging einzuführen, wobei Verizon und AT&T derzeit 10DLC unterstützen, und wir erwarten, dass alle großen Anbieter bald folgen werden. Auch wenn es kurzfristig zu Unannehmlichkeiten kommen kann, werden Kund:innen langfristig von besseren Zustellraten profitieren und gleichzeitig ihre Verbraucher:innen vor unerwünschten Nachrichten schützen.

## Was Sie wissen müssen {#what-you-need-to-know}

### Zugang {#access}

Die Registrierung von Langcodes mit A2P 10DLC dauert 4–6 Wochen.

### Kosten {#costs}

Die Registrierung bei A2P 10DLC kann verschiedene Arten von Gebühren umfassen:

| Gebührenart | Beschreibung |
| -------- | ---------- |
| Registrierungsgebühren | Nominale Gebühren, die bei der Registrierung Ihrer Marke und Ihres Anwendungsfalls in allen großen US-Netzwerken anfallen. |
| Gebühren für sekundäre Überprüfung | Marken können ihren [Vertrauens-Score](#trust-score) anfechten und eine sekundäre Überprüfung beantragen, um ihren Gesamtdurchsatz zu verbessern; für diesen Prozess fällt eine Gebühr an. |
| Anbietergebühren | Gebühren, die von Mobilfunkanbietern für ausgehende SMS- und MMS-Nachrichten erhoben werden, die nach der 10DLC-Registrierung an Nutzer:innen gesendet werden. Ab dem 1. Oktober 2021 sind die Anbietergebühren für nicht registrierten Verkehr (Standard-Langcodes) höher als für registrierten Verkehr (10DLC). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Costs" }

Besuchen Sie den Twilio-10DLC-Artikel, um aktuelle [Gebührenschätzungen](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) einzusehen.

### Durchsatz {#throughput}

Der Nachrichtendurchsatz für Ihr 10DLC hängt von mehreren Faktoren ab, darunter der Vertrauens-Score der Marke, tägliche Nachrichtenlimits und Ihre Messaging-Anwendungsfälle.

#### Vertrauens-Score der Marke {#trust-score}

Die Campaign Registry (TCR) ist eine Drittanbieter-Agentur, die einen Reputationsalgorithmus verwendet, um bestimmte Kriterien in Bezug auf Ihr Unternehmen zu überprüfen und einen Vertrauens-Score zuzuweisen, der den Messaging-Durchsatz für jede Marke bestimmt. Dieser Vertrauens-Score wird zugewiesen, wenn sich Kund:innen für US-10DLC-Messaging Registrierung. Je höher der Vertrauens-Score, desto besser die MPS (MPS), die Sie erleben werden.

|     | Vertrauens-Score | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| Hoch | 75–100 | 75 MPS | 75 MPS | 75 MPS |
| Mittel | 50–74 | 40 MPS | 40 MPS | 40 MPS |
| Niedrig | 1–49 | 4 MPS | 4 MPS | 4 MPS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Brand trust score #trust-score" }

{% alert tip %}
Unternehmen, die im Russell 3000 Index gelistet sind, erhalten nach der 10DLC-Registrierung und -Überprüfung einen hohen Durchsatz und Vertrauens-Score.
{% endalert %}

#### Tägliche Nachrichtenlimits {#daily-message-limits}

Tägliche Limits reichen von 2.000 bis 200.000 Nachrichten, abhängig von Ihrem Vertrauens-Score der Marke, und gelten für alle Langcodes. Obwohl hohe Vertrauens-Scores einen Durchsatz von 60 MPS ermöglichen, gelten die vom Mobilfunkanbieter festgelegten täglichen Nachrichtenlimits weiterhin. Das bedeutet, dass Shortcodes die bessere Option wären, wenn die täglichen Spitzennachrichten einer Marke das auferlegte Tageslimit überschreiten.

#### Messaging-Anwendungsfälle {#messaging-use-cases}

Der Durchsatz wird auch durch die Art des gewählten Messaging-Anwendungsfalls beeinflusst. Die meisten Kund:innen fallen unter den Standard-Marketing- oder gemischten Marketing-Anwendungsfall. Andere weniger verbreitete Anwendungsfälle unterliegen unterschiedlichen Durchsatzwerten.

Abhängig von Ihrem Anwendungsfall variiert der Vertrauens-Score, der benötigt wird, um den maximalen Durchsatz zu erreichen. Die folgenden Tabellen zeigen Standard-Anwendungsfälle und gängige Vertrauens-Score-Bereiche für Anwendungsfälle. Für spezielle Anwendungsfälle wie Notfalldienste oder Wohltätigkeitsorganisationen lesen Sie die [Twilio-Dokumentation](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Standard-Anwendungsfälle | Beschreibung |
| ------------------ | ----------- |
| Marketing | Werbeinhalte wie Verkaufsaktionen und zeitlich begrenzte Angebote. |
| Gemischt | Campaign, die mehrere Anwendungsfälle abdeckt, wie z. B. Kundenbetreuung. |
| Hochschulbildung | Campaigns für Hochschuleinrichtungen. |
| Umfragen und Abstimmungen | Nicht-politische Umfragen und Abstimmungen, wie z. B. Kundenumfragen. |
| Öffentliche Bekanntmachungen | Öffentliche Bekanntmachungen zur Sensibilisierung für ein bestimmtes Thema. |
| Kundenbetreuung | Support, Kontoverwaltung und andere Kundeninteraktionen. |
| Zustellbenachrichtigungen | Status von Zustellnachrichten. |
| Kontobenachrichtigungen | Benachrichtigungen über den Status eines Kontos. |
| 2FA | Jede Authentifizierung oder Kontoverifizierung, wie z. B. OTP. |
| Sicherheitswarnungen | Benachrichtigung über ein kompromittiertes System. |
| Betrugswarnungen | Nachrichten über potenziell betrügerische Aktivitäten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messaging use cases" }

{% tabs %}
{% tab Deklarierter Anwendungsfall %}
Ein deklarierter Anwendungsfall bedeutet, dass Sie einen bestimmten Nicht-Marketing-Anwendungsfall gewählt haben (z. B. 2FA oder Kontobenachrichtigungen).

| Vertrauens-Score | Gesamtdurchsatz zu großen US-Netzwerken | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75–100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50–74	 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1–49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Messaging use cases" }

{% endtab %}
{% tab Gemischter Marketing-Anwendungsfall %}

Gemischte Marketing-Anwendungsfälle können für Kund:innen registriert werden, die Nachrichten für mehrere Anwendungsfälle über denselben Nummernbestand oder für Marketing senden möchten.

| Vertrauens-Score | Gesamtdurchsatz zu großen US-Netzwerken | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75–100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50–74 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1–49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Messaging use cases" }

{% endtab %}
{% endtabs %}

Besuchen Sie den Twilio-10DLC-Artikel, um aktuelle [Durchsatzschätzungen](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) einzusehen.

## Nächste Schritte {#next-steps}

Kund:innen, die sich noch nicht für 10DLC registriert haben, müssen mit ihrem CSM zusammenarbeiten, um ihre Langcodes zu Registrierung. **Wenn Kund:innen ihre Langcodes nicht Registrierung, wird ab dem 1. Oktober 2021 jeder A2P-Sender, der Langcodes verwendet, eine starke Filterung aller Nachrichten erfahren.** Kontaktieren Sie Ihren CSM, um mit Ihrer 10DLC-Registrierung zu beginnen.