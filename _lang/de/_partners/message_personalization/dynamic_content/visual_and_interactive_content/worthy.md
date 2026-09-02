---
nav_title: Worthy
article_title: Worthy
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Worthy, einer Plattform zur Personalisierung von Nachrichten, die es Ihnen erlaubt, personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zuzustellen."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> Mit der Integration von [Worthy](https://worthy.ai/) und Braze können Sie personalisierte, reichhaltige In-App-Erlebnisse mit dem Drag-and-Drop-Editor von Worthy erstellen und diese über Braze zustellen. Außerdem führt Worthy automatisch die folgenden Aktionen aus:

_Diese Integration wird von Worthy gepflegt._

## Über die Integration {#about-the-integration}

- Erstellen Sie einen Connected-Content-Server und eine gesicherte API für Ihr Messaging.
- Gestalten Sie Ihre In-App-Nachrichten mit Analytics und Klick-Tracking, die direkt in Braze erscheinen.
- Exportieren Sie automatisch HTML über den Drag-and-Drop-Editor von Worthy zur Verwendung in **Custom Code**-In-App-Nachricht-Campaigns in Braze, komplett mit den erforderlichen API-Verbindungen und dynamischen Inhalten, die Sie konfigurieren.

## Anwendungsfälle {#use-cases}

- Angepasste Willkommenserlebnisse basierend auf der Auswahl der Nutzer:innen beim Onboarding
- In-App-Erlebnisse für besondere Ereignisse und Aktionen
- Sammeln von Kundenfeedback und Bewertungen auf der Grundlage des App-Verhaltens
- Schnelles Testen potenzieller Ideen für App-Produkte
- Reichhaltige Mitteilungen, Neuigkeiten und Community-Updates

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| [Worthy](https://worthy.ai/)-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Worthy-Konto. |
| Braze SDK or Software-Development-Kit | Sie müssen das Braze SDK or Software-Development-Kit in Ihrer mobilen Anwendung konfigurieren, um reichhaltige In-App-Nachrichten versenden zu können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Erstellen Sie personalisierte Nachrichten in Worthy {#step-1-create-personalized-messaging-in-worthy}

Navigieren Sie im Worthy-Dashboard zu Ihrer App, wählen Sie den **Message Creator** und erstellen Sie eine personalisierte Nachricht, mit der Sie Ihre Nutzer:innen ansprechen möchten.

### 2. Schritt: Erstellen Sie eine Braze-Campaign {#step-2-create-a-braze-campaign}

Erstellen Sie eine [In-App-Nachricht-Campaign]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) in Braze und stellen Sie den **Nachrichtentyp** auf **Custom Code** ein.

### 3. Schritt: Kopieren Sie Ihre personalisierte Nachricht in Braze {#step-3-copy-your-personalized-message-into-braze}

Klicken Sie im Worthy Message Creator auf **Exportieren** und wählen Sie **Braze**, um Ihre personalisierte Nachricht zur Verwendung in Braze-Campaigns zu exportieren. Kopieren Sie den exportierten Inhalt in das HTML-Textfeld unter **HTML + Asset Zip** im Campaign-Editor von Braze.

Das war's! Sie können Ihre personalisierte Nachricht sofort testen, indem Sie den Tab **Test** im Campaign-Editor von Braze verwenden.