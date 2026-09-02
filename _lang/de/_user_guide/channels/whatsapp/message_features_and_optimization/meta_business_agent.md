---
nav_title: Meta Business Agent
article_title: Meta Business Agent und Braze WhatsApp
page_order: 8
description: "Dieser Leitfaden erklärt, wie Meta Business Agent mit einer WhatsApp-Business-Telefonnummer interagiert, die mit Braze verbunden ist, und was Sie erwarten können, wenn Sie ihn aktivieren."
page_type: reference
channel:
  - WhatsApp
alias: /meta_business_agent/
hidden: true
noindex: true
---

# Meta Business Agent und Braze WhatsApp {#meta-business-agent-and-braze-whatsapp}

> Meta Business Agent kann auf eingehende WhatsApp-Nachrichten auf einer Nummer antworten, die auch mit Braze verbunden ist. Dieser Artikel behandelt, wie diese beiden Systeme die Nachrichtensichtbarkeit teilen, wie Sie den Agenten in den Tools von Meta aktivieren und wie die Abrechnung aufgeteilt wird. Er spiegelt die Produktfunktionalität und Dokumentation von Metas Business Agent mit Stand August 2026 wider.

Meta entwickelt Meta Business Agent aktiv weiter, daher können sich einige Details ändern. Die neuesten Informationen finden Sie in [Metas Business-Agent-Dokumentation](https://developers.facebook.com/documentation/meta-business-agent/overview).

## Was ist Meta Business Agent? {#what-is-meta-business-agent}

Meta Business Agent ist ein KI or künstliche Intelligenz-gestützter Responder, den Meta direkt auf einer WhatsApp-Business-Telefonnummer betreibt. Wenn er für eine berechtigte Nummer aktiviert ist, kann er im Namen des Unternehmens auf eingehende Nachrichten von Nutzer:innen antworten und dabei Wissen (Unternehmensinformationen, FAQs, Dateien, Website-Inhalte) und Konnektoren nutzen, die in den Tools von Meta konfiguriert wurden.

Die Aktivierung von Meta Business Agent erfolgt vollständig im WhatsApp Manager:in und in der Meta Business Suite und ist von Ihrem Braze-Workspace getrennt. Braze ist für die Einrichtung nicht erforderlich, und es gibt derzeit keine Steuerungsmöglichkeit im Braze-Dashboard dafür.

## Wie er mit Ihrer Braze-verbundenen Nummer interagiert {#how-it-interacts-with-your-braze-connected-number}

Meta Business Agent und Braze können auf derselben WhatsApp-Business-Telefonnummer koexistieren, teilen aber derzeit nicht die Sichtbarkeit jeder Nachricht.

- **Von Braze initiierte ausgehende Nachrichten sind nicht betroffen.** Braze sendet weiterhin WhatsApp-Template-Nachrichten und Antwortnachrichten über Campaigns und Canvase genau wie bisher, unabhängig davon, ob Meta Business Agent aktiviert ist.
- **Eingehende Nachrichten werden von Meta Business Agent geroutet.** Für jede eingehende Nachricht einer Nutzerin oder eines Nutzers entscheidet Meta Business Agent, ob sie an Braze weitergeleitet oder selbst bearbeitet wird.
  - **Wenn Meta die Nachricht an Braze weiterleitet:** Sie wird genauso verarbeitet wie jede eingehende WhatsApp-Nachricht heute. Bestehende aktionsbasierte Trigger or triggern und Aktionspfade in Campaigns und Canvase werden gemäß der von Ihnen erstellten Logik ausgelöst.
  - **Wenn Meta Business Agent die Nachricht selbst bearbeitet:** Braze verarbeitet derzeit nicht den separaten Kanal (Standby-Nachrichten und Nachrichtenechos), der diese Aktivität übertragen würde. Eingehende Nachrichten, die der Agent selbst bearbeitet, und seine eigenen Antworten auf diese Nachrichten sind derzeit in keiner Braze-Oberfläche sichtbar.

| Nachrichtenfluss | Was heute passiert |
| --- | --- |
| WhatsApp-Template-Nachrichten und Antwortnachrichten, die über Campaigns oder Canvas-Schritte gesendet werden | Nicht betroffen; Braze sendet weiterhin wie konfiguriert |
| Eingehende Nachricht, die Meta an Braze weiterleitet | Wird normal verarbeitet; bestehende Trigger or triggern und Aktionspfade gelten |
| Eingehende Nachricht, die Meta Business Agent selbst bearbeitet | Derzeit für Braze nicht sichtbar; bestehende Trigger or triggern und Aktionspfade für eingehende Nachrichten werden nicht ausgelöst |
| Ausgehende Nachricht, die von Meta Business Agent gesendet wird | Derzeit für Braze nicht sichtbar |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nachrichtenfluss" }

## Meta Business Agent aktivieren {#enable-meta-business-agent}

Meta Business Agent wird pro Telefonnummer in den Tools von Meta aktiviert, nicht in Braze:

1. Prüfen Sie die Berechtigung und aktivieren Sie ihn für eine Telefonnummer im [WhatsApp Manager:in](https://business.facebook.com/wa/manage/home/), indem Sie die Nutzungsbedingungen für Meta Business Agent akzeptieren.
2. Konfigurieren Sie das Wissen und die Fähigkeiten des Agenten (Unternehmensinformationen, FAQs, Dateien, Konnektoren) über die [Agenten-Konfigurations-APIs](https://developers.facebook.com/documentation/meta-business-agent/reference/configure/agent-skills) von Meta.
3. Schalten Sie den Agenten über die [Agenteneinstellungen](https://developers.facebook.com/documentation/meta-business-agent/reference/onboard/agent-settings) ein.

## Was Sie vor der Aktivierung abwägen sollten {#things-to-weigh-before-enabling-it}

- **Kein Braze-seitiger Schalter:** Die Aktivierung, Konfiguration und Deaktivierung von Meta Business Agent erfolgt vollständig in den Tools von Meta; es gibt nichts, was in Braze ein- oder ausgeschaltet werden muss.
- **Abrechnung:** Mit der Einführung von Meta Business Agent werden nicht-templatebasierte Nachrichten jetzt in eine von zwei Kategorien eingestuft: Service (bestehende Kategorie) oder Meta Business Agent (neue Kategorie).
  - Nicht-templatebasierte Antworten, die von Braze verarbeitet werden, werden ab dem 1. Oktober 2026 als Service-Nachrichten abgerechnet.
    - Wenn Sie auf eine eingehende Nachricht mit einem Marketing-, Utility- oder Authentifizierungs-Template antworten, wird sie entsprechend abgerechnet.
  - Meta-Business-Agent-Nachrichten werden ab dem 1. August 2026 direkt von Meta abgerechnet. Details entnehmen Sie deren Preisgestaltung.
  - Nachrichten werden nur in eine Kategorie eingestuft, sodass Ihnen dieselbe Nachricht nie doppelt berechnet wird.