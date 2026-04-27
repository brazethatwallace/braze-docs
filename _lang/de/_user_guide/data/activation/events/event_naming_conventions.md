---
nav_title: Konventionen zur Benennung von Ereignissen
article_title: Event-Benennungskonventionen
page_order: 4
page_type: reference
description: "Dieser Artikel referenziert die korrekten Konventionen für die Benennung von Ereignissen und die besten Praktiken."

---

# Konventionen zur Benennung von Ereignissen {#event-naming-conventions}

> Diese Seite behandelt die korrekte Benennung von Ereignissen und bewährte Verfahren. Wenn Sie die Konsistenz Ihrer Ereignis- und Attribut-Taxonomie wahren, bleiben Ihre Daten sauber und für neue und bestehende Nutzer:innen der Braze-Plattform nutzbar. Dies hilft, spätere Probleme zu vermeiden, z.B. das Triggern einer Campaign an die falsche Zielgruppe oder die Generierung falscher Ergebnisse nach Verwendung des falschen Ereignisses.

## Bewährte Praktiken {#best-practices}

- Halten Sie Ihre Namenskonvention klar.
- Verwenden Sie eine einheitliche Schreibweise und Formatierung von Ereignisnamen.
- Vermeiden Sie es, Ereignissen ähnliche Namen zu geben.
- Vermeiden Sie lange Strings für die Attribute von Ereignissen, die im Braze-Dashboard abgeschnitten oder gekürzt werden.

## Konventionen zur Namensgebung {#naming-conventions}

### Ereignisgruppen verwenden {#use-event-groups}

Verwenden Sie Gruppen zur Unterscheidung von Teilen Ihres Produkts, um Ereignisse zu benennen. Indem Sie Ihr Produkt in Gruppen einteilen, kann jeder Nutzer:innen klar verstehen, worauf sich das Ereignis bezieht und was es bewirkt.

### Struktur der Ereignisbenennung {#event-naming-structure}

Die häufigste Namensstruktur ist `group_noun_action`. Ereignisse sollten alle klein geschrieben werden, um Fehler bei der Instrumentierung und der Identifizierung von Eigenschaften zu vermeiden.

### Eigenschaften {#properties}

Markieren Sie ein Ereignis und identifizieren Sie Unterschiede mithilfe von Eigenschaften. Das ist hilfreich bei Ereignissen, die im Grunde identisch sind, aber kleine Unterschiede aufweisen – zum Beispiel verschiedene Kanäle für eine Campaign. So können Sie auch leicht nachvollziehen, wie Nutzer:innen durch Ereignisse navigieren. Im [Event-Eigenschaften-Objekt]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) finden Sie ein Beispiel und zusätzlichen Kontext.

## Beispiele {#examples}

Nehmen wir an, Sie sind Teil eines E-Commerce-Unternehmens und möchten tracken, wann sich Kund:innen für Ihre App registriert haben und wann sie Ihren Newsletter abonniert haben. Hier sind Beispiele für effektive Ereignisnamen:

- `user_signup`
- `newsletter_subscribed`

Diese beiden Ereignisnamen geben klar an, welches Ereignis sie tracken. Wenn Sie weitere angepasste Events erstellen, achten Sie darauf, dass Ihre Namenskonventionen verständlich bleiben. Vermeiden Sie beispielsweise Ereignisnamen wie `signup_event_1`, da dieser Name unklar ist und nicht vermittelt, was das Ereignis trackt – im Gegensatz zu `user_signup`.