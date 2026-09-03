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

## Fallbeispiel 1: Was ist das Ziel? {#case-question-1-what-is-the-goal}

Das Ziel von StyleRyde ist einfach: Sie möchten, dass Nutzer:innen über ihre App Taxifahrten buchen.

## Fallbeispiel 2: Welche Schritte sind nötig, um dieses Ziel nach der App-Installation zu erreichen? {#case-question-2-what-are-the-steps-to-reach-that-goal-after-app-installation}

1. StyleRyde benötigt, dass Nutzer:innen den Registrierungsprozess starten und ihre persönlichen Daten eingeben.
2. StyleRyde benötigt, dass Nutzer:innen die Registrierung abschließen und überprüfen, indem sie einen per SMS erhaltenen Code in die App eingeben.
3. StyleRyde benötigt, dass Nutzer:innen versuchen, ein Taxi zu rufen.
4. StyleRyde muss verfügbar sein, wenn Nutzer:innen ein Taxi rufen.

Diese Aktionen könnten dann als folgende angepasste Events getaggt werden:

- Began Registration
- Completed Registration
- Successful Taxi Hails
- Unsuccessful Taxi Hails

Nach der Implementierung der Events kann StyleRyde Campaigns durchführen, darunter:

1. Nutzer:innen kontaktieren, die „Began Registration“ ausgelöst, aber „Completed Registration“ nicht innerhalb eines bestimmten Zeitraums abgeschlossen haben.
2. Glückwunschnachrichten an Nutzer:innen senden, die „Completed Registration“ abgeschlossen haben.
3. Entschuldigungen und Aktionsguthaben an Nutzer:innen senden, die „Unsuccessful Taxi Hails“ hatten, auf die nicht innerhalb eines bestimmten Zeitraums ein „Successful Taxi Hail“ folgte.
4. Aktionen an Power-Nutzer:innen mit vielen „Successful Taxi Hails“ senden, um ihnen für ihre Treue zu danken.

## Fallbeispiel 3: Welche weiteren Nutzerinfos könnten wir erfassen und für unser Messaging nutzen? {#case-question-3-what-other-user-information-could-we-collect-and-use-to-inform-our-messaging}

- Ob Nutzer:innen Aktionsguthaben haben?
- Die durchschnittliche Bewertung, die Nutzer:innen ihren Fahrer:innen geben?
- Eindeutige Aktionscodes für Nutzer:innen?

Diese Merkmale könnten dann als folgende angepasste Attribute getaggt werden:

- Aktionsguthaben (Dezimaltyp)
- Durchschnittliche Fahrerbewertung (Ganzzahltyp)
- Eindeutiger Aktionscode (String-Typ)

Diese Attribute ermöglichen es Ihnen, Campaigns an Nutzer:innen zu senden, wie zum Beispiel:

1. Nutzer:innen, die die App seit sieben Tagen nicht genutzt haben und Aktionsguthaben auf ihrem Konto haben, daran erinnern, zur App zurückzukehren und das Guthaben einzulösen.
2. Unsere Nachrichten-Templates und [Personalisierungs-Features]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) nutzen, um das Attribut für den eindeutigen Aktionscode in Nachrichten einzufügen, die an Nutzer:innen gerichtet sind.

{% alert important %}
Braze blockiert Nutzerprofile („Dummy-Nutzer:innen“) mit mehr als 5.000.000 Sitzungen, mehr als 20.000 verschiedenen angepassten Event-Namen oder mehr als 20.000 verschiedenen Produktnamen in Käufen, da diese in der Regel das Ergebnis einer fehlerhaften Integration sind. Nachdem ein Profil blockiert wurde, stoppt Braze die Aufnahme aller eingehenden Daten für dieses Profil – sowohl von den SDKs als auch von der REST API. Wenn Sie feststellen, dass dies bei einem/einer legitimen Nutzer:in passiert ist, wenden Sie sich an Ihren Braze Account Manager:in.
{% endalert %}