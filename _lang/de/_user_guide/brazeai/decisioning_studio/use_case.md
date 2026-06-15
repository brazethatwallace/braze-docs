---
nav_title: Anwendungsfall
article_title: "Anwendungsfall: Decisioning Studio"
description: "Dieses Beispiel veranschaulicht, wie eine fiktive Marke BrazeAI Decisioning Studio™ und einen Decisioning-Agenten einsetzt, um personalisiertes Messaging für die Rückgewinnung inaktiver Kund:innen bereitzustellen und den Umsatz zu optimieren."
---

# Anwendungsfall: Inaktive Kund:innen mit einem umsatzorientierten Decisioning-Agenten zurückgewinnen {#use-case-win-back-lapsed-customers-with-a-revenue-focused-decisioning-agent}

> Dieses Beispiel veranschaulicht, wie eine fiktive Marke BrazeAI Decisioning Studio™ und einen Decisioning-Agenten einsetzt, um jede:n Kund:in zur optimalen Entscheidung aus der Aktionsbank zu leiten, Messaging für die Rückgewinnung zu personalisieren und den Umsatz zu optimieren. Es verbindet Agentendesign, Zielgruppen und Experimente, Orchestrierung über Braze sowie kontinuierliches Lernen nach dem Start.

Nehmen wir an, Poppy ist CRM-Manager:in bei Kitchenerie, einer fiktiven Online-Handelsmarke, die auf Küchenartikel spezialisiert ist.

Viele Kund:innen durchstöbern saisonale Kollektionen nur ein- oder zweimal, bevor sie die Seite verlassen. Frühere Rückgewinnungsprogramme setzten auf feste Journeys und manuelle A/B-Splits, die zwar hilfreich waren, um Texte zu testen, aber nicht um herauszufinden, welche Kombination aus Angebot, Kanal, Frequenz und Timing den Kaufumsatz für jede:n Kund:in maximiert. Die Priorität der Geschäftsleitung ist klar: So viele inaktive Käufer:innen wie möglich zurückgewinnen und den Umsatz steigern, ohne die Leitplanken für Rabatte oder Häufigkeit zu überschreiten.

Diese Anleitung beschreibt, wie Poppy:

- Inaktive oder gefährdete Kund:innen als Zielgruppe des Agenten definiert und gleichzeitig Experimentgruppen für einen fairen Vergleich strukturiert
- Dem Agenten ermöglicht, die am besten passenden zulässigen Aktionen aus einer umfangreichen Aktionsbank auszuwählen, sodass das Messaging im großen Maßstab personalisiert bleibt
- Die Orchestrierung einrichtet, damit Entscheidungen in Braze als Customer-Engagement-Plattform einfließen
- Den Agenten startet und ihm ermöglicht, autonom zu lernen, was den Rückgewinnungsumsatz steigert

## 1. Schritt: Erfolgsmetriken definieren und festlegen, wen der Agent anspricht {#step-1-define-success-metrics-and-who-the-agent-targets}

Poppy bestätigt die Erfolgsmetrik, die der Agent maximieren soll: Umsatz aus Wiederkäufen bei Kund:innen, die aufgehört haben zu kaufen.

Sie definiert, wer in das Programm aufgenommen wird: ein Braze-Segment inaktiver Käufer:innen oder hochwertiger inaktiver Nutzer:innen. Poppy muss nun lediglich dem AI Decisioning Services-Team mitteilen, welches Segment der Agent ansprechen soll. Die Integration zum Abrufen der Daten dieses Segments erfolgt im Hintergrund, ohne dass Poppy eine Integration einrichten muss.

## 2. Schritt: Aktionsbank und Einschränkungen erstellen {#step-2-build-the-action-bank-and-constraints}

Poppy definiert die Dimensionen, die für Rückgewinnungsstrategien relevant sind:

- Angebot: Kostenloser Versand, prozentualer Rabatt oder Artikelbündel
- Kanal: E-Mail, Push oder SMS
- Sendezeit oder Frequenz
- Kreativ: Kleine Illustrationen oder nutzenorientierte Texte

Für jede Dimension listet sie konkrete Optionen in der Aktionsbank auf – die einzigen Aktionen, die der Agent ausführen darf (alles andere bleibt konstruktionsbedingt ausgeschlossen). Der Agent experimentiert dann mit den zulässigen Kombinationen, um herauszufinden, was für jede:n Kund:in funktioniert, und optimiert dabei die gewählte Erfolgsmetrik.

## 3. Schritt: Daten vorbereiten und Orchestrierung mit Braze verbinden {#step-3-prepare-data-and-connect-orchestration-to-braze}

Gemäß [Daten verbinden]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources/) stellt Poppy sicher, dass umfangreiche First-Party-Signale (einschließlich Kaufhistorie, Kategorie-Affinität, Browsing-Verhalten und Engagement) den Agenten speisen, sodass jede Entscheidung auf echtem Verhalten basiert.

Für die Orchestrierung nutzt sie den nativen Braze-Pfad: Decisioning Studio entscheidet, was gesendet wird und wann; Braze übernimmt die Zustellung. Sie plant Basis-Templates (API-getriggerte Campaigns) pro Kanal mit dynamischen Feldern für Angebote und Kreativinhalte und legt die Wiederberechtigung fest.

## 4. Schritt: Starten, überwachen und für Umsatz optimieren {#step-4-launch-monitor-and-optimize-for-revenue}

Nach einer Konfigurationsüberprüfung mit dem AI Decisioning Services-Team startet Poppy den Agenten. Der Agent beginnt, Aktionen pro Nutzer:in zu empfehlen und Sendungen über Braze zu orchestrieren, um sich im Laufe der Zeit zu verbessern.

Durch die Kombination einer umsatzorientierten Erfolgsmetrik mit einem Decisioning-Agenten, der kontinuierlich zulässige Aktionen testet, entwickelt sich Kitchenerie von statischen Rückgewinnungs-Massensendungen hin zu 1:1-Entscheidungen, die sich pro Kund:in anpassen – mit dem Ziel, mehr Kund:innen zurückzugewinnen und den Umsatz zu steigern, während die von Poppy definierten Geschäftsregeln eingehalten werden.