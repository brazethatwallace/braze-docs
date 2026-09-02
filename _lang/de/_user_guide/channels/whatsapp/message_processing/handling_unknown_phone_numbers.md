---
nav_title: "Unbekannte Telefonnummern verarbeiten"
article_title: "Unbekannte Telefonnummern verarbeiten"
description: "Dieser Referenzartikel beschreibt, wie Braze mit unbekannten Telefonnummern von WhatsApp-Nutzer:innen umgeht."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Unbekannte Telefonnummern verarbeiten {#handle-unknown-phone-numbers}

> Es kann vorkommen, dass Sie nach der Einrichtung von WhatsApp mit Braze Nachrichten von unbekannten Nutzer:innen erhalten. Die folgenden Schritte beschreiben, wie nicht identifizierte Nutzer:innen und Nummern verarbeitet werden.

## Opt-in/Opt-out- und angepasster Keyword-Workflow für unbekannte Nummern {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

Braze versucht zunächst, Nutzer:innen mit einer übereinstimmenden Nummer zu finden. Werden keine gefunden, verarbeitet Braze eine unbekannte Nummer automatisch auf eine von zwei Arten:

1. **Wenn ein Trigger or triggern-Wort mit einem [Opt-in-Canvas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) eingerichtet ist:**
- Braze erstellt ein anonymes Profil
- Dem Profil wird ein Nutzer-Alias mit folgenden Details zugewiesen:
  - Ein `alias_name` mit dem Wert der von den Nutzer:innen angegebenen Telefonnummer
  - Ein `alias_label` mit dem Wert `phone`
- Unser System setzt das Telefon-Attribut
- Die Nutzer:innen werden basierend auf der im Canvas eingerichteten Logik der entsprechenden Abo-Gruppe zugeordnet<br><br>
2. **Wenn kein Opt-in-Canvas eingerichtet ist:**
- Braze erstellt ein anonymes Profil
- Dem Profil wird ein Nutzer-Alias mit folgenden Details zugewiesen:
  - Ein `alias_name` mit dem Wert der von den Nutzer:innen angegebenen Telefonnummer
  - Ein `alias_label` mit dem Wert `phone`
- Unser System setzt das Telefon-Attribut
- Der Abo-Status der Nutzer:innen wird für alle WhatsApp-Abo-Gruppen standardmäßig auf `unsubscribed` gesetzt<br><br>