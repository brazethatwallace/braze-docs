---
nav_title: Konventionen zur Benennung von Events
article_title: Konventionen zur Benennung von Events
page_order: 4
page_type: reference
description: "Dieser Referenzartikel behandelt die korrekten Konventionen zur Benennung von Events und bewährte Verfahren."

---

# Konventionen zur Benennung von Events {#event-naming-conventions}

> Diese Seite behandelt die korrekten Konventionen zur Benennung von Events und bewährte Verfahren. Wenn Sie die Konsistenz Ihrer Event- und Attribut-Taxonomie wahren, bleiben Ihre Daten sauber und für neue und bestehende Nutzer:innen der Braze-Plattform nutzbar. Dies hilft, spätere Probleme zu vermeiden, z. B. das Trigger or triggern or triggern einer Campaign an die falsche Zielgruppe oder die Generierung falscher Ergebnisse nach Verwendung des falschen Events.

## Bewährte Verfahren {#best-practices}

- Halten Sie Ihre Namenskonvention klar.
- Verwenden Sie eine einheitliche Schreibweise und Formatierung von Event-Namen.
- Vermeiden Sie es, Events ähnliche Namen zu geben.
- Vermeiden Sie lange Strings für Event-Attribute, die im Braze-Dashboard abgeschnitten oder gekürzt werden.

## Namenskonventionen {#naming-conventions}

### Event-Gruppen verwenden {#use-event-groups}

Verwenden Sie Gruppen zur Unterscheidung von Teilen Ihres Produkts, um Events zu benennen. Indem Sie Ihr Produkt in Gruppen einteilen, können alle Nutzer:innen klar verstehen, worauf sich das Event bezieht und was es bewirkt.

### Struktur der Event-Benennung {#event-naming-structure}

Die häufigste Namensstruktur ist `group_noun_action`. Events sollten alle kleingeschrieben werden, um Fehler bei der Instrumentierung und der Identifizierung von Eigenschaften zu vermeiden.

### Eigenschaften {#properties}

Markieren Sie ein Event und identifizieren Sie Unterschiede mithilfe von Eigenschaften. Das ist hilfreich bei Events, die im Grunde identisch sind, aber kleine Unterschiede aufweisen – zum Beispiel verschiedene Kanäle für eine Campaign. So können Sie auch leicht nachvollziehen, wie Nutzer:innen durch Events navigieren. Im [Event-Eigenschaften-Objekt]({{site.baseurl}}/api/objects_filters/event_object#event-properties-object) finden Sie ein Beispiel und zusätzlichen Kontext.

## Beispiele {#examples}

Nehmen wir an, Sie sind Teil eines E-Commerce-Unternehmens und möchten tracken, wann sich Kund:innen für Ihre App registriert haben und wann sie Ihren Newsletter abonniert haben. Hier sind Beispiele für effektive Event-Namen:

- `user_signup`
- `newsletter_subscribed`

Diese beiden Event-Namen geben klar an, welches Event sie tracken. Wenn Sie weitere angepasste Events erstellen, achten Sie darauf, dass Ihre Namenskonventionen verständlich bleiben. Vermeiden Sie beispielsweise Event-Namen wie `signup_event_1`, da dieser Name unklar ist und nicht vermittelt, was das Event trackt – im Gegensatz zu `user_signup`.