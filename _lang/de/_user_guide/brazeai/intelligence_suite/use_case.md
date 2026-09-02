---
nav_title: "Anwendungsfall"
article_title: "Anwendungsfall: Intelligence Suite"
page_order: 10
search_rank: 12
description: "Neu bei der Braze Intelligence Suite? Lesen Sie diesen Anwendungsfall darüber, wie intelligentes Timing genutzt werden kann, um personalisierte Aktionen in einem einheitlichen Canvas zu versenden."
tool:
  - Dashboard
---

# Anwendungsfall: Vergangenes App-Verhalten in personalisierte Angebote auf dem richtigen Kanal umwandeln {#use-case-turn-past-app-behavior-into-personalized-offers-on-the-right-channel}

> Dieses Beispiel veranschaulicht, wie eine fiktive Marke intelligentes Timing nutzt, um vergangene App- und Nachrichten-Engagement-Daten für den Versand personalisierter Aktionen in einem einheitlichen Canvas einzusetzen.

Nehmen wir an, Marvin ist Marketing-Manager:in:in bei SandwichEmperor, einem Fast-Food-Restaurant, das häufig zeitlich begrenzte Angebote durchführt. Marvins Team ist dafür verantwortlich, Werbenachrichten in der App zu versenden, um einen neuen zeitlich begrenzten Menüartikel zu bewerben: das Super Sub.

Bisher wurde jede Nachricht für zeitlich begrenzte Artikel als Silo verwaltet: verschiedene Texttests und Ansätze wurden als separate Sendungen zugestellt – das Team probierte unterschiedliche Messaging-Ansätze aus, um ein höheres Engagement zu erzielen, ohne vollständig zu verstehen, wann zeitlich begrenzte Aktionen bei den Nutzer:innen in der App am beliebtesten sind.

Für die neue Super-Sub-Aktion möchte Marvin einen koordinierten Canvas, der im Laufe der Zeit weiterlernt – basierend auf Verhalten, das Braze bereits erfasst (Sitzungen, Öffnungen, Klicks), anstatt Sendezeiten oder eine einzelne Gewinnernachricht zu erraten.

Mit intelligentem Timing kann Marvin Message-Schritte dann zustellen, wenn jede Person mit höherer Wahrscheinlichkeit interagiert, basierend auf einer statistischen Analyse vergangener Interaktionen (zum Beispiel Sitzungsmuster und Kanal-Engagement).

Diese Anleitung beschreibt, wie Marvin:

- Einen Canvas mit Push, E-Mail und SMS in Message-Schritten erstellt
- Intelligentes Timing für diese Schritte verwendet, damit die Zustellung mit den abgeleiteten Engagement-Mustern pro Nutzer:in und Kanal übereinstimmt

## 1. Schritt: Erfolgsmetrik definieren und den Canvas erstellen {#step-1-define-the-success-metric-and-build-the-canvas}

Marvin legt fest, was „Erfolg“ für das Super Sub bedeutet (zum Beispiel Bestellungen oder ein angepasstes Event, das ausgelöst wird, wenn jemand einen Super-Sub-Kauf abschließt oder es in der App hinzufügt).

Anschließend erstellt Marvin einen Canvas, in den neue Nutzer:innen nach einem regelmäßigen Zeitplan eintreten, solange das Angebot läuft.

1. Im Braze-Dashboard navigiert Marvin zu **Messaging** > **Canvas**.
2. Er erstellt einen Canvas und benennt ihn „Limited item - Super Sub“.
3. Dann fügt er ein Konversions-Event und eine weitere Variante im Canvas hinzu.
4. Er vervollständigt die restlichen Canvas-Details und ist nun bereit, die Nutzer-Journey im Canvas-Builder abzubilden.

## 2. Schritt: Zustellungseinstellungen einrichten {#step-2-set-up-delivery-settings}

Im Tab **Delivery Settings** des Message-Schritts plant Marvin, intelligentes Timing zu verwenden, um die vergangenen Interaktionen der Nutzer:innen mit der App und jedem Messaging-Kanal zu analysieren und dann automatisch den besten Zeitpunkt auszuwählen, um das Super Sub bei jeder Nutzer:in zu bewerben. Das bedeutet, dass einige Nutzer:innen die Aktion am Nachmittag erhalten, während andere sie am Abend erhalten.

Er wählt **die beliebteste Zeit zur Nutzung der App unter allen Nutzer:innen** als Fallback für Nutzer:innen, die nicht genügend vergangene Interaktionen zur Analyse aufweisen.

## 3. Schritt: Verzögerungen und intelligentes Timing zu Message-Schritten hinzufügen {#step-3-add-delays-and-intelligent-timing-to-message-steps}

Für Message-Schritte, die intelligentes Timing verwenden, folgt Marvin der Canvas-Anleitung: Er platziert einen Delay-Schritt von mindestens zwei Kalendertagen zwischen dem Eintritt (oder einem vorherigen Schritt) und dem Message-Schritt mit intelligentem Timing. Er bevorzugt Kalendertage für Verzögerungen bei der Verwendung von intelligentem Timing, damit die Zustellung am vorgesehenen Tag zum optimalen Zeitpunkt jeder Nutzer:in erfolgt.

In jedem Push-Benachrichtigungs-, E-Mail- und SMS-Message-Schritt öffnet er **Delivery Settings** und wählt **Using Intelligent Timing**. Er legt eine Fallback-Zeit für Nutzer:innen fest, die nicht genügend Engagement-Verlauf für einen optimalen Zeitpunkt haben. Er merkt an, dass Message-Schritte mit mehreren Kanälen zu unterschiedlichen Zeiten pro Kanal senden oder zu senden versuchen können, was widerspiegelt, wie manche Kund:innen morgens stärker auf E-Mail und abends auf Push reagieren.

## 4. Schritt: Überwachen und optimieren {#step-4-monitor-and-optimize}

Marvin koordiniert die Super-Sub-Werbematerialien über Push, E-Mail und SMS in den Message-Schritten (und allen nachfolgenden Schritten, die seine Varianten verwenden) und startet den Canvas.

Nach dem Start beobachtet er die Canvas-Analytics und Conversion-Zahlen und stellt fest, dass intelligentes Timing kontinuierlich optimiert, wann jeder Kanal für jede Nutzer:in basierend auf laufenden Engagement-Mustern ausgelöst wird. Dadurch hat Marvin SandwichEmperor erfolgreich dabei geholfen, die Performance zeitlich begrenzter Angebote damit zu verknüpfen, wann und welche Journey funktioniert – anstatt nur zu wissen, welche einzelne Werbenachricht beim letzten Mal gewonnen hat.