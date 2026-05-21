---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Predictive Churn
description: "Dieser Referenzartikel behandelt einige Schritte zur Fehlerbehebung und Überlegungen, die Sie bei der Verwendung von Predictive Churn beachten sollten."
page_order: 3

---

# Fehlerbehebung {#troubleshooting}

> Predictive Churn (und jedes Modell des maschinellen Lernens) ist nur so gut wie die Daten, die dem Modell zur Verfügung stehen. Außerdem ist es in hohem Maße davon abhängig, dass bestimmte Datenmengen zur Verfügung stehen.

## Mögliche Fehler {#potential-errors}

### Nicht genügend Daten zum Trainieren {#not-enough-data-to-train}

Diese Fehlermeldung erscheint, wenn Ihre Churn-Definition zu eng gefasst ist und zu wenige abgewanderte Nutzer:innen liefert.

Um dies zu beheben, müssen Sie entweder die Anzahl der Tage und/oder die Aktionen, die Churn definieren, ändern, um mehr Nutzer:innen zu erfassen. Vergewissern Sie sich, dass Sie die `AND/OR`-Filter richtig verwenden, um keine zu restriktiven Definitionen zu erstellen.

{% alert important %}
Auch wenn Predictive Churn auf Unternehmensebene aktiviert ist, haben einige Workspaces möglicherweise nicht genügend Nutzer:innen, um Prognosen zu erstellen. Normalerweise benötigen Sie 300.000 monatlich aktive Nutzer:innen in einem einzigen Workspace.
{% endalert %}

### Probleme mit der Größe der Prognose-Zielgruppe {#problems-with-prediction-audience-size}

Wenn Sie Ihre Prognose-Zielgruppe erstellen, um die Art der Nutzung, für die Sie Ihr Modell trainieren möchten, fein abzustimmen, erhalten Sie möglicherweise diese Meldung, die Sie darüber informiert, dass Ihre Prognose-Zielgruppe zu wenige Nutzer:innen hat:

„Nicht genug nicht abgewanderte Nutzer:innen in der Vergangenheit, um eine zuverlässige Prognose zu erstellen“

![Datenanforderungen für die Prognose mit 31 Abgewanderten in der Vergangenheit (erfüllt die Anforderung) und 0 Nicht-Abgewanderten in der Vergangenheit (unter dem Minimum). Eine Warnung weist darauf hin, dass nicht genügend Nicht-Abgewanderte vorhanden sind, um die Prognose zu erstellen.]({% image_buster /assets/img/churn/audience_size_error.png %})

Wenn Ihre Definition der Prognose-Zielgruppe zu eng gefasst ist, haben Sie möglicherweise keinen ausreichend großen Pool an historischen und aktiven Nutzer:innen, mit dem Sie arbeiten können. Um dies zu beheben, müssen Sie entweder die Anzahl der Tage und die Art der Attribute ändern, die in dieser Definition verwendet werden, die Aktionen ändern, die Churn definieren, oder beides.

Wenn Ihre Prognose-Zielgruppe auch nach der Änderung Ihrer Definitionen weiterhin ein Problem darstellt, haben Sie möglicherweise zu wenige Nutzer:innen, um dieses optionale Feature zu unterstützen. Wir empfehlen, stattdessen eine Prognose ohne die zusätzlichen Ebenen und Filter zu erstellen.

### Prognose-Zielgruppe ist zu groß {#prediction-audience-size-is-too-big}

Die Definition einer Prognose-Zielgruppe darf 100 Millionen Nutzer:innen nicht überschreiten. Wenn Sie die Meldung erhalten, dass Ihre Zielgruppe zu groß ist, empfehlen wir Ihnen, weitere Ebenen zu Ihrer Zielgruppe hinzuzufügen oder das Zeitfenster zu ändern, auf dem sie basiert.

### Prognose hat schlechte Qualität {#prediction-has-poor-quality}

![]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
Wenn Ihr Modell eine [Prognosequalität]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/) von 40 % oder mehr hat, sind Sie auf einem guten Weg! Wenn Ihre Prognosequalität jedoch auf 39 % oder weniger sinkt, müssen Sie Ihre Churn- und Prognose-Zielgruppen-Definitionen möglicherweise so ändern, dass sie spezifischer sind oder andere Zeitfenster haben.

Wenn Sie bei der Erstellung Ihrer Prognose-Definitionen nicht in der Lage sind, sowohl die Anforderungen an die Größe der Zielgruppe zu erfüllen als auch eine Prognosequalität von mehr als 40 % zu erreichen, bedeutet dies wahrscheinlich, dass die an Braze gesendeten Daten für diesen Anwendungsfall nicht ideal sind, dass es nicht genügend Nutzer:innen gibt, anhand derer ein Modell erstellt werden kann, oder dass Ihr Produktlebenszyklus länger ist, als unser aktuelles 60-Tage-Rückblickfenster unterstützt.

## Überlegungen zu Daten {#data-considerations}

Die folgenden Fragen sollten Sie sich stellen, wenn Sie Predictive Churn einrichten. Modelle für maschinelles Lernen sind nur so gut wie die Daten, mit denen sie trainiert werden. Eine gute Datenhygiene und das Verständnis dessen, was in das Modell einfließt, machen also einen großen Unterschied.

- Welche wertvollen Aktionen führen zu Bindung und Treue?
- Haben Sie angepasste Events eingerichtet, die diesen spezifischen Aktionen zugeordnet sind? Predictive Churn arbeitet mit angepassten Events im Gegensatz zu angepassten Attributen.
- Denken Sie in Zeitfenstern, innerhalb derer Sie Churn definieren? Sie können Churn als etwas definieren, das in bis zu 60 Tagen passiert.
- Haben Sie an Jahreszeiten gedacht, die zu untypischem Nutzerverhalten führen, wie z. B. Feiertage? Rasche Veränderungen im Verbraucherverhalten werden Ihre Prognosen beeinflussen.