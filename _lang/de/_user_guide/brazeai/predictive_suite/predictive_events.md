---
nav_title: Predictive Events
article_title: Predictive Events
description: "Dieser Artikel befasst sich mit Predictive Events (früher Predictive Purchases), einem Tool der Braze Predictive Suite, mit dem Marketer Nutzer:innen anhand der Wahrscheinlichkeit identifizieren und ansprechen können, dass sie ein bestimmtes Ereignis ausführen."
page_order: 9
alias: /predictive_purchases/
search_rank: 1
---

# Predictive Events {#predictive-events}

> Predictive Events ist ein leistungsstarkes Tool der Braze Predictive Suite, mit dem Nutzer:innen anhand der Wahrscheinlichkeit, dass sie ein bestimmtes Ereignis ausführen, identifiziert und angesprochen werden können. Wenn Sie eine Event-Prognose erstellen, trainiert Braze ein Modell für maschinelles Lernen mithilfe von [Gradient-Boosted-Entscheidungsbäumen](https://en.wikipedia.org/wiki/Gradient_boosting), um aus früheren Aktivitäten zu lernen und zukünftige Aktivitäten vorherzusagen.

## Über Predictive Events {#about-predictive-events}

Nachdem eine Prognose erstellt wurde, wird den Nutzer:innen ein [Wahrscheinlichkeitswert]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#purchase_score) zwischen 0 und 100 zugewiesen, der angibt, wie wahrscheinlich es ist, dass sie das ausgewählte Ereignis ausführen. Je höher der Wert, desto wahrscheinlicher ist es, dass eine Nutzer:in dieses Ereignis ausführt. Nutzer:innen werden außerdem in Kategorien mit niedriger, mittlerer und hoher Wahrscheinlichkeit sortiert.

Der wahre Wert von Predictive Events liegt in der Verwendung der Prognoseergebnisse zur Erstellung eines Segments oder einer Campaign. Marketer können gezielte Campaigns direkt auf der Seite **Prognose** erstellen, um sofortige umsatzsteigernde Ergebnisse zu erzielen, oder ein Segment für eine zukünftige Campaign oder ein Canvas speichern. Sie wissen nicht, wen Sie zuerst ansprechen sollen? Lesen Sie unsere [strategischen Überlegungen]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) zur Benachrichtigung von Nutzer:innen auf der Grundlage ihres Wahrscheinlichkeitswerts.

![Grafik mit dem Titel „Wie Predictive Events funktioniert“, die Nutzerdaten zeigt, die in das Modell für maschinelles Lernen eingespeist werden. Die Beschriftung lautet: „Trainieren Sie mit historischen Daten und vergleichen Sie das Verhalten von Nutzer:innen, die das Ereignis in einem bestimmten Zeitraum ausgeführt haben, mit denen, die es nicht getan haben.“ Außerdem werden die Ergebnisse des maschinellen Lernens dargestellt, bei denen Nutzer:innen von der geringsten bis zur höchsten Wahrscheinlichkeit, das Ereignis auszuführen, eingestuft werden. Die Beschriftung lautet: „Prognostizieren Sie die Wahrscheinlichkeit zukünftiger Ereignisse und weisen Sie Nutzer:innen einen Wahrscheinlichkeitswert für präzises und bequemes Targeting zu.“]({% image_buster /assets/img/how_predictive_events_works.png %})

## Zugriff auf Predictive Events {#accessing-predictive-events}

{% multi_lang_include brazeai/predictions_page_access.md %}

Bevor Sie dieses Feature erwerben, ist es im Vorschaumodus verfügbar. So können Sie eine Demo-Prognose mit synthetischen Daten ansehen und jeweils ein Vorschau-Prognosemodell erstellen. Diese Prognose wird auf der Grundlage Ihrer tatsächlichen Nutzerdaten erstellt, ermöglicht es Ihnen jedoch nicht, Nutzer:innen entsprechend ihres Wahrscheinlichkeitswerts für Nachrichten anzusprechen. Sie wird nach der Erstellung auch nicht regelmäßig aktualisiert.

Mit der Vorschau können Sie diese eine Prognose auch bearbeiten und neu erstellen oder sie archivieren und weitere erstellen, um die erwartete [Prognosequalität]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#prediction_quality) für [verschiedene Zielgruppen]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) zu testen und sich mit den Analytics vertraut zu machen.