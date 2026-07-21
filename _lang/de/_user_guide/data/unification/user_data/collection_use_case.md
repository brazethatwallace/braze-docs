---
nav_title: Anwendungsfall Datenerfassung
article_title: Anwendungsfall Datenerfassung
page_order: 3
page_type: reference
description: "Dieser Referenzartikel behandelt einen Anwendungsfall zur Datenerfassung und zeigt, wie eine Mitfahr-App entscheiden könnte, welche Nutzerdaten sie erfassen soll."

---

# Anwendungsfall Datenerfassung {#collection-use-case}

> Dieser Artikel behandelt einen Anwendungsfall zur Datenerfassung und zeigt, wie eine Mitfahr-App entscheiden könnte, welche Nutzerdaten sie erfassen soll.

Nehmen wir an, eine Taxi- oder Mitfahr-App namens StyleRyde möchte entscheiden, welche Nutzerdaten sie sammeln soll. Die folgenden Fragen und der Brainstorming-Prozess sind ein hervorragendes Modell für ihre Marketing- und Entwicklungsteams. Am Ende dieser Übung sollten beide Teams ein solides Verständnis dafür haben, welche angepassten Events und Attribute sinnvollerweise erfasst werden sollten, um ihr Ziel zu erreichen.

## Fallfrage 1: Was ist das Ziel? {#case-question-1-what-is-the-goal}

Das Ziel von StyleRyde ist ganz einfach: Die Nutzer:innen sollen über die App Taxifahrten anfordern können.

## Fallfrage 2: Was sind die Schritte, um dieses Ziel nach der Installation der App zu erreichen? {#case-question-2-what-are-the-steps-to-reach-that-goal-after-app-installation}

1. StyleRyde benötigt, dass Nutzer:innen den Registrierungsprozess beginnen und ihre persönlichen Daten eingeben.
2. StyleRyde benötigt, dass Nutzer:innen den Registrierungsprozess abschließen und überprüfen, indem sie einen per SMS erhaltenen Code in die App eingeben.
3. StyleRyde benötigt, dass Nutzer:innen versuchen, ein Taxi zu rufen.
4. StyleRyde muss verfügbar sein, wenn Nutzer:innen ein Taxi rufen.

Diese Aktionen könnten dann als die folgenden angepassten Events getaggt werden:

- Registrierung begonnen
- Registrierung abgeschlossen
- Erfolgreiche Taxirufe
- Erfolglose Taxirufe

Nach der Implementierung der Events kann StyleRyde Campaigns wie die folgenden durchführen:

1. Nachrichten an Nutzer:innen senden, die die Registrierung begonnen, aber nicht innerhalb eines bestimmten Zeitraums abgeschlossen haben.
2. Glückwunschnachrichten an Nutzer:innen senden, die die Registrierung abgeschlossen haben.
3. Entschuldigungen und Aktionsguthaben an Nutzer:innen senden, die erfolglose Taxirufe hatten, auf die nicht innerhalb einer bestimmten Zeitspanne ein erfolgreicher Taxiruf folgte.
4. Aktionen an besonders aktive Nutzer:innen mit vielen erfolgreichen Taxirufen senden, um ihnen für ihre Treue zu danken.

## Fallfrage 3: Welche anderen Nutzerinfos könnten wir sammeln und für unser Messaging verwenden? {#case-question-3-what-other-user-information-could-we-collect-and-use-to-inform-our-messaging}

- Haben die Nutzer:innen ein Aktionsguthaben?
- Welche durchschnittliche Bewertung geben Nutzer:innen ihren Fahrer:innen?
- Eindeutige Aktionscodes für Nutzer:innen?

Diese Merkmale könnten dann als die folgenden angepassten Attribute getaggt werden:

- Aktionsguthaben (Dezimaltyp)
- Durchschnittliche Fahrerbewertung (Integer-Typ)
- Eindeutiger Aktionscode (String-Typ)

Diese Attribute ermöglichen es Ihnen, Campaigns an Nutzer:innen zu senden, wie zum Beispiel:

1. Nutzer:innen, die die App sieben Tage lang nicht benutzt haben und über ein Aktionsguthaben verfügen, daran erinnern, zur App zurückzukehren und das Guthaben einzulösen.
2. Unsere Nachrichten-Templates und [Personalisierungs-Features]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) nutzen, um das eindeutige Aktionscode-Attribut in Nachrichten an Nutzer:innen einzufügen.

{% alert important %}
Braze sperrt Nutzer:innen („Dummy-Nutzer:innen“) mit mehr als 5.000.000 Sitzungen und nimmt ihre SDK-Events nicht mehr auf, da sie in der Regel das Ergebnis einer Fehlintegration sind. Wenn Sie feststellen, dass dies bei einer oder einem rechtmäßigen Nutzer:in passiert ist, wenden Sie sich an Ihren Braze Account Manager.
{% endalert %}