---
nav_title: Unbekannte Telefonnummern verarbeiten
article_title: Unbekannte Telefonnummern verarbeiten
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Braze unbekannte Telefonnummern von neuen Nutzer:innen verarbeitet."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Unbekannte Telefonnummern verarbeiten – neue Nutzer:innen {#handle-unknown-phone-numbers-new-users}

> Nachdem Sie SMS, MMS und RCS mit Braze eingerichtet haben, kann es vorkommen, dass Sie Nachrichten von unbekannten Nutzer:innen erhalten. Die folgenden Schritte beschreiben, wie eine nicht identifizierte Nutzer:in und Nummer verarbeitet werden.

## Opt-in-/Opt-out- und angepasster Keyword-Workflow für unbekannte Nummern {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

Braze verarbeitet eine unbekannte Nummer automatisch auf eine von drei Arten:

1. Wenn ein Opt-in-Keyword gesendet wird:
  * Braze erstellt ein anonymes Profil
  * Unser System setzt das Telefon-Attribut
  * Die Nutzer:in wird in die entsprechende Abo-Gruppe eingetragen, basierend darauf, welches Opt-in-Keyword von Braze empfangen wurde.<br><br>
2. Wenn ein Opt-out-Keyword gesendet wird:
  * Braze erstellt ein anonymes Profil
  * Unser System setzt das Telefon-Attribut
  * Die Nutzer:in wird aus der entsprechenden Abo-Gruppe abgemeldet, basierend darauf, welches Opt-out-Keyword von Braze empfangen wurde.<br><br>
3. Wenn ein anderes angepasstes Keyword gesendet wird:
  * Braze ignoriert die Textnachricht und unternimmt nichts.