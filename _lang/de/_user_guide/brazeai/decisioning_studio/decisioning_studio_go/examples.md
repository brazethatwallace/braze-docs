---
nav_title: Beispiele
article_title: Beispiele für Decisioning Studio Go
page_order: 5
page_type: reference
description: "Sehen Sie sich gängige E-Mail-Programmtypen an, um festzustellen, ob Decisioning Studio Go gut zu Ihrem Szenario passt."
---

# Beispiele für Decisioning Studio Go {#examples-for-decisioning-studio-go}

> Decisioning Studio Go eignet sich am besten für wiederkehrende E-Mail-Programme, bei denen der Agent Zeit hat, aus dem Engagement zu lernen, und bei denen Ihre Inhalte genügend Varianten-Optionen für eine sinnvolle Personalisierung bieten. Diese Seite gruppiert gängige E-Mail-Anwendungsfälle nach Eignungsstufe, mit Beispielen und Hinweisen für jede Stufe.

Einen Überblick über die Funktionsweise von Decisioning Studio Go finden Sie unter [BrazeAI Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go).

Jedes Beispiel in diesem Leitfaden ist mit einer der folgenden Eignungsstufen gekennzeichnet:

| Eignungsstufe | Beschreibung |
|---|---|
| **Beste Eignung** | Der Agent hat genügend Zeit zum Lernen, Ihre Zielgruppe ist stabil genug, um einen Uplift zu zeigen, und Personalisierung kann das Engagement sinnvoll beeinflussen. Beginnen Sie hier. |
| **Unterstützt** | Das Beispiel kann gut funktionieren, aber der Erfolg hängt von Timing, Zielgruppengröße oder Reihenfolge ab. Prüfen Sie die Hinweise, bevor Sie sich festlegen. |
| **Nicht empfohlen** | Das Beispiel steht im Widerspruch zur Lernweise des Agents. Wählen Sie einen anderen Programmtyp oder sprechen Sie mit Ihrem Customer-Success-Manager oder Solutions Consultant über ein anderes Setup. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eignungsstufen" }

{% alert note %}
Über alle Eignungsstufen hinweg lernt der Agent am besten, wenn Ihre Zielgruppe genügend Engagement-Signale erzeugt, damit der Algorithmus Muster erkennen kann. Als Faustregel sollten Sie Zielgruppen von Zehntausenden von Nutzer:innen oder mehr anvisieren, mit einem konsistenten wöchentlichen Sendevolumen. Der Agent kann auch mit kleineren Zielgruppen arbeiten, aber rechnen Sie mit einer längeren Lernphase und einem weniger zuverlässigen Uplift. Ihr Customer-Success-Manager oder Solutions Consultant kann Ihnen helfen zu bestätigen, ob eine bestimmte Zielgruppe die richtige Größe hat.
{% endalert %}

## Beste Eignung {#best-fit}

### Dauerhafte kalenderbasierte Campaigns {#always-on-calendared-campaigns}

| Thema | Details |
|---|---|
| Wie es aussieht | Ein Marketingkalender, der über mehrere Monate oder länger läuft, wobei Inhalte im Laufe der Zeit ausgetauscht werden – zum Beispiel ein Rewards-Mitglieder-Kalender, ein Content-Drop-Zeitplan oder ein Lifestyle- oder Inspirationskalender. |
| Warum es passt | Langfristige Programme geben dem Agent Zeit zu lernen, was für verschiedene Nutzer:innen funktioniert. Die Zielgruppe ist stabil, Inhalte werden regelmäßig aktualisiert, und Klicks sind in der Regel ein aussagekräftiger Indikator für Engagement. |
| Was Sie mitbringen sollten | Mehrere Basis-Creatives oder Varianten-Sets, die Sie gerne rotieren. Der Agent wählt aus, welche Version für jede:n Nutzer:in funktioniert, benötigt aber genügend Vielfalt in den von Ihnen bereitgestellten Optionen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dauerhafte kalenderbasierte Campaigns" }

### Evergreen-Programme {#evergreen-programs}

| Thema | Details |
|---|---|
| Wie es aussieht | Laufende Campaigns, die nicht an bestimmte Daten oder Ereignisse gebunden sind – Winbacks, Programme zur erneuten Interaktion, Nudges für inaktive Konten oder Meilenstein-Feiern. |
| Warum es passt | Wie bei kalenderbasierten Campaigns ist die Zielgruppe dynamisch, aber das Programm läuft unbegrenzt. Der Agent hat Zeit zum Lernen, die Inhalte sind flexibel, und Klicks sind ein führender Indikator, gegen den der Agent optimieren kann. |
| Was Sie mitbringen sollten | Varianten-Optionen für Betreffzeile und CTA, die die Nachricht für verschiedene Motivationen rahmen. Bild-Varianten helfen, wenn Sie welche haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Evergreen-Programme" }

## Unterstützte Anwendungsfälle {#supported-use-cases}

### Multi-E-Mail-Aktionen {#multi-email-promotions}

| Thema | Details |
|---|---|
| Wie es aussieht | Eine Reihe von E-Mails, die über mehrere Wochen unter demselben Aktionsthema versendet werden – zum Beispiel eine Back-to-School-Serie oder eine mehrwöchige Kategorie-Aktion. |
| Warum es funktioniert | Wenn die Aktion lang genug läuft – mindestens mehrere Wochen – hat der Agent genügend Anlaufzeit, um innerhalb der Aktion zu lernen. Click-through ist in der Regel ein starker führender Indikator für das Engagement bei Aktionen. |
| Hinweise | Bei kürzeren Aktionen hat der Agent möglicherweise nicht genügend Datentage, um vor Programmende zu lernen. Als allgemeine Richtlinie benötigt der Agent mindestens 10 Campaign-Tage, um starke Empfehlungen zu entwickeln. Wenn Ihre Aktion kürzer ist, überlegen Sie, ob ein Evergreen-Programm das Lernen übernehmen könnte, und wenden Sie dann das Gelernte auf die nächste Aktion an. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Multi-E-Mail-Aktionen" }

### Aktions- oder ereignisgesteuerte Journeys {#action-or-event-driven-journeys}

| Thema | Details |
|---|---|
| Wie es aussieht | Eine einzelne E-Mail oder Sequenz, die durch eine Kundenaktion ausgelöst wird – abgebrochener Einkauf, Browse-Abbruch oder Post-Purchase-Follow-up. |
| Warum es funktioniert | Trigger schaffen einen klaren Einstiegspunkt. Wenn die Journey wiederkehrend ist und das Zielgruppenvolumen konsistent ist, kann der Agent lernen, welche Inhalte für welche Nutzer:innen funktionieren. |
| Hinweise | Timing ist entscheidend. Wenn die E-Mail innerhalb von Minuten nach dem Trigger-Ereignis versendet werden muss, klären Sie mit Ihrem Customer-Success-Manager oder Solutions Consultant, ob der Sendezeitplan des Agents kompatibel ist. Wenn Nutzer:innen E-Mails in einer bestimmten Reihenfolge erhalten müssen (E-Mail A vor E-Mail B), müssen Sie die Zielgruppen-Verschiebungen selbst orchestrieren – der Agent sequenziert keine Sendungen für einzelne Nutzer:innen über eine mehrstufige E-Mail-Journey hinweg. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aktions- oder ereignisgesteuerte Journeys" }

## Nicht empfohlen {#not-recommended}

### Drip-Sequenzen {#drip-sequences}

| Thema | Details |
|---|---|
| Wie es aussieht | Eine mehrstufige E-Mail-Sequenz – zum Beispiel ein Onboarding-Tutorial – bei der Nutzer:innen E-Mail A, dann E-Mail B, dann E-Mail C in dieser Reihenfolge erhalten müssen. |
| Warum es nicht passt | Der Agent wählt aus, was er jeder/jedem Nutzer:in sendet, basierend darauf, was wahrscheinlich einen Klick für diese:n Nutzer:in erzeugt. Er modelliert keine Sequenzanforderungen. Wenn Sie eine bestimmte Reihenfolge erzwingen müssen, müssen Sie die Zielgruppe selbst orchestrieren (Nutzer:innen nach jeder E-Mail von Segment zu Segment verschieben), was den größten Teil des Vorteils der Agent-Nutzung reduziert. Der Agent kann auch nicht eigenständig bestätigen, dass E-Mail A erfolgreich war, bevor er E-Mail B sendet. |
| Was Sie stattdessen tun sollten | Verwenden Sie [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), um die Drip-Sequenz zu orchestrieren. Wenn Sie KI-Optimierung innerhalb einer Drip-Sequenz wünschen, sprechen Sie mit Ihrem Customer-Success-Manager oder Solutions Consultant darüber, ob [Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/get_started) besser geeignet ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Drip-Sequenzen" }

### Einmalige E-Mail-Blasts {#one-time-email-blasts}

| Thema | Details |
|---|---|
| Wie es aussieht | Eine einzelne E-Mail, die in einem Blast versendet wird – eine Black-Friday-Ankündigung, ein neuer Produktlaunch oder eine einmalige Unternehmenskommunikation. |
| Warum es nicht passt | Der Agent braucht Zeit zum Lernen. Ein einzelner Versand gibt ihm keine Möglichkeit, Entscheidungen zu verbessern, bevor die Campaign endet. Bis er genügend Engagement-Signale hat, um bessere Entscheidungen zu treffen, ist das Programm vorbei. |
| Was Sie stattdessen tun sollten | Wenn Sie ein Evergreen-Programm mit ähnlichen Inhalten haben – zum Beispiel ein ganzjähriges Produktankündigungs-Programm – verwenden Sie dort Decisioning Studio Go und wenden Sie das Gelernte auf einmalige Sendungen an. Für einen wirklich einmaligen Blast sind [A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing) oder [intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) besser geeignet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Einmalige E-Mail-Blasts" }

## Auf einen Blick {#at-a-glance}

| Szenario | Eignung | Wichtiger Hinweis |
|---|---|---|
| Dauerhafte kalenderbasierte Campaigns | Beste Eignung | Stellen Sie mehrere Basis-Creatives oder Varianten-Sets bereit, die Sie im Laufe der Zeit aktualisieren. |
| Evergreen-Programme (Winbacks, erneute Interaktion) | Beste Eignung | Stellen Sie Varianten-Optionen bereit, die dieselbe Nachricht für verschiedene Motivationen rahmen. |
| Multi-E-Mail-Aktionen | Unterstützt | Planen Sie mindestens 10 Campaign-Tage Anlaufzeit ein; kürzere Aktionen begrenzen das Lernen. |
| Aktions- oder ereignisgesteuerte Journeys | Unterstützt | Klären Sie die Anforderungen an den Sendezeitpunkt; Sie sind für die Durchsetzung der Reihenfolge verantwortlich. |
| Drip-Sequenzen (Onboarding-Tutorials) | Nicht empfohlen | Verwenden Sie Canvas für die Sequenzierung; ziehen Sie Decisioning Studio Pro für die Optimierung innerhalb von Drip-Sequenzen in Betracht. |
| Einmalige E-Mail-Blasts | Nicht empfohlen | Verwenden Sie stattdessen A/B-Tests oder intelligente Auswahl. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zusammenfassungstabelle der Beispiele" }

## Nächste Schritte {#next-steps}

Wenden Sie sich an Ihren Braze Customer-Success-Manager oder Solutions Consultant, wenn Sie unsicher sind, ob Ihr Programm geeignet ist. Starke Signale sind:

- Die Zielgruppe erhält regelmäßig E-Mails – mindestens wöchentlich – über einen Zeitraum von einem Monat oder mehr.
- Die Zielgruppe ist groß genug, um konsistente Engagement-Signale zu erzeugen (Zehntausende von Nutzer:innen sind ein nützlicher Ausgangswert).
- Sie haben mindestens zwei oder drei sinnvolle Varianten-Optionen anzubieten (Betreffzeilen, CTAs oder Bilder, die die Nachricht unterschiedlich rahmen).
- Klicks sind ein führender Indikator für den Geschäftswert dieses Programms, nicht nur eine Eitelkeitsmetrik.
- Das Segment wird nicht aktiv von einem anderen Canvas oder einer anderen Campaign genutzt, die um das Engagement derselben Nutzer:innen konkurrieren würde.