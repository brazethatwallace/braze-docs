---
nav_title: Namenskonventionen für Events
article_title: Namenskonventionen für Events
page_order: 4
page_type: reference
description: "Dieser Referenzartikel behandelt korrekte Namenskonventionen für Events und Best Practices."

---

# Namenskonventionen für Events

> Diese Seite behandelt korrekte Namenskonventionen für Events und Best Practices. Indem Sie Konsistenz in Ihrer Event- und Attribut-Taxonomie wahren, halten Sie Ihre Daten sauber und nutzbar – sowohl für neue als auch bestehende Nutzer:innen der Braze-Plattform. So vermeiden Sie spätere Probleme, wie das Triggern einer Kampagne an die falsche Zielgruppe oder das Generieren falscher Ergebnisse durch die Verwendung des falschen Events.

## Best Practices

- Halten Sie Ihre Namenskonvention klar und verständlich.
- Verwenden Sie einheitliche Groß-/Kleinschreibung und Formatierung von Event-Namen.
- Vermeiden Sie es, Events ähnliche Namen zu geben.
- Vermeiden Sie lange Event-Attribut-Strings, da diese im Braze-Dashboard abgeschnitten oder gekürzt werden.

## Namenskonventionen

### Event-Gruppen verwenden

Verwenden Sie Gruppen, um verschiedene Bereiche Ihres Produkts bei der Benennung von Events zu unterscheiden. Durch die Kategorisierung Ihres Produkts in Gruppen kann jede:r Nutzer:in klar nachvollziehen, worauf sich das Event bezieht und was es bewirkt.

### Struktur der Event-Benennung

Die gängigste Benennungsstruktur ist `group_noun_action`. Events sollten durchgehend in Kleinbuchstaben geschrieben werden, um Fehler bei der Instrumentierung durch unterschiedliche Schreibweisen zu vermeiden und Eigenschaften korrekt zu identifizieren.

### Eigenschaften

Taggen Sie ein Event und identifizieren Sie Unterschiede mithilfe von Eigenschaften. Das ist hilfreich bei Events, die im Grunde identisch sind, aber kleine Unterschiede aufweisen – zum Beispiel verschiedene Kanäle für eine Kampagne. So können Sie auch leicht nachvollziehen, wie Nutzer:innen durch Events navigieren. Im [Event-Eigenschaften-Objekt]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) finden Sie ein Beispiel und zusätzlichen Kontext.

## Beispiele

Nehmen wir an, Sie sind Teil eines E-Commerce-Unternehmens und möchten tracken, wann sich Kund:innen für Ihre App registriert haben und wann sie Ihren Newsletter abonniert haben. Hier sind Beispiele für effektive Event-Namen:

- `user_signup`
- `newsletter_subscribed`

Diese beiden Event-Namen geben klar an, welches Event sie tracken. Wenn Sie weitere angepasste Events erstellen, achten Sie darauf, dass Ihre Namenskonventionen verständlich bleiben. Vermeiden Sie beispielsweise Event-Namen wie `signup_event_1`, da dieser Name unklar ist und nicht vermittelt, was das Event trackt – im Gegensatz zu `user_signup`.