---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Predictive Abwanderung or Abwanderung, Churn or Abwanderung, churnen
description: "Diagnostizieren Sie Trainings- und Zielgruppenfehler bei Predictive Abwanderung or Abwanderung, Churn or Abwanderung, churnen mithilfe eines Symptomindex und der Datenanforderungen."
page_order: 3

---

# Fehlerbehebung für Predictive Abwanderung or Abwanderung, Churn or Abwanderung, churnen {#troubleshoot-predictive-churn}

> Verwenden Sie diese Seite, um Trainings- und Zielgruppenfehler bei Predictive Abwanderung or Abwanderung, Churn or Abwanderung, churnen zu beheben. Informationen zu Analytics und Modellqualität finden Sie unter [Predictive Abwanderung or Abwanderung, Churn or Abwanderung, churnen Analytics]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics).

Predictive Abwanderung or Abwanderung, Churn or Abwanderung, churnen (und jedes Modell des maschinellen Lernens) ist nur so gut wie die Daten, die dem Modell zur Verfügung stehen. Es hängt außerdem davon ab, dass im Workspace ein ausreichendes Nutzer:innenvolumen vorhanden ist.

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

Ordnen Sie die Fehlermeldung, Warnung oder das Ergebnis, das Sie beim Erstellen einer Prognose sehen, dem Abschnitt zu, der erklärt, wie Sie das Problem beheben können.

| Symptom | Gehe zu |
| --- | --- |
| Fehler „Nicht genügend Daten zum Trainieren“ | [Nicht genügend Daten zum Trainieren](#not-enough-data-to-train) |
| Warnung „Nicht genügend vergangene Nicht-Abgewanderte“ | [Prognosezielgruppe zu klein](#problems-with-prediction-audience-size) |
| Prognosezielgruppe überschreitet das Größenlimit | [Prognosezielgruppe zu groß](#prediction-audience-size-is-too-big) |
| Prognosequalität unter 40 % | [Prognose hat eine schlechte Qualität](#prediction-has-poor-quality) |
| Unsicher, ob Ihre Daten zum Modell passen | [Überlegungen zu den Daten](#data-considerations) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptome bei voraussichtlicher Abwanderung" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, wenn das Erstellen einer Prognose fehlschlägt oder Sie durch Daten- oder Zielgruppenanforderungen blockiert werden. Beginnen Sie bei Schritt 1.

1. Bestätigen Sie, dass voraussichtliche Abwanderung für Ihr Unternehmen aktiviert ist und der Workspace über ausreichend monatlich aktive Nutzer:innen (MAU or monatlich aktive:r Nutzer:in) verfügt – in der Regel 300.000 MAU or monatlich aktive:r Nutzer:in in einem einzelnen Workspace.
2. Überprüfen Sie Ihre Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Definition. Zu restriktive Filter reduzieren die Anzahl der abgewanderten Nutzer:innen, die für das Training verfügbar sind.
3. Überprüfen Sie Ihre Definition der Prognosezielgruppe. Zu wenige historische nicht abgewanderte Nutzer:innen blockieren das Modelltraining.
4. Bestätigen Sie, dass angepasste Events (nicht allein angepasste Attribute) die hochwertigen Aktionen erfassen, die auf ein Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Risiko hinweisen.
5. Wenn nach dem Erweitern der Definitionen weiterhin Fehler auftreten, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Nicht genügend Daten zum Trainieren {#not-enough-data-to-train}

**Symptom:** Beim Erstellen einer Prognose wird die Fehlermeldung „Nicht genügend Daten zum Trainieren“ angezeigt.

Dieser Fehler tritt auf, wenn Ihre Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Definition zu einschränkend ist und zu wenige abgewanderte Nutzer:innen zurückgibt.

Um dies zu beheben, ändern Sie entweder die Anzahl der Tage oder die Aktionen, die Abwanderung or Abwanderung, Churn or Abwanderung, churnen definieren, um mehr Nutzer:innen zu erfassen – oder beides. Stellen Sie sicher, dass Sie `AND/OR`-Filter korrekt verwenden, damit Sie keine übermäßig restriktiven Definitionen erstellen.

{% alert important %}
Obwohl voraussichtliche Abwanderung auf Unternehmensebene aktiviert ist, verfügen einige Workspaces möglicherweise nicht über genügend Nutzer:innen, um Prognosen zu erstellen. In der Regel benötigen Sie 300.000 monatlich aktive Nutzer:innen (MAU or monatlich aktive:r Nutzer:in) in einem einzelnen Workspace.
{% endalert %}

## Probleme mit der Größe der Prognose-Zielgruppe {#problems-with-prediction-audience-size}

**Symptom:** Sie sehen die Meldung „Not enough past non-churners to reliably build the Prediction.“

![Datenanforderungen für die Prognose mit 31 früheren Abgewanderten (Anforderung erfüllt) und 0 früheren Nicht-Abgewanderten (unter dem Minimum). Eine Warnmeldung weist darauf hin, dass nicht genügend Nicht-Abgewanderte vorhanden sind, um die Prognose zu erstellen.]({% image_buster /assets/img/churn/audience_size_error.png %})

Wenn Sie Ihre Prognose-Zielgruppe erstellen, um die Art der Nutzung zu verfeinern, gegen die Ihr Modell trainiert werden soll, kann diese Meldung erscheinen, die Sie darauf hinweist, dass Ihre Prognose-Zielgruppe zu wenige Nutzer:innen enthält.

Wenn Ihre Definition der Prognose-Zielgruppe zu streng ist, haben Sie möglicherweise keinen ausreichend großen Pool an historischen und aktiven Nutzer:innen zur Verfügung. Um dies zu beheben, ändern Sie entweder die Anzahl der Tage und die Art der in dieser Definition verwendeten Attribute, passen Sie die Aktionen an, die Abwanderung definieren, oder beides.

Wenn Ihre Prognose-Zielgruppe auch nach Anpassung Ihrer Definitionen weiterhin ein Problem darstellt, haben Sie möglicherweise zu wenige Nutzer:innen, um dieses optionale Feature zu unterstützen. Versuchen Sie stattdessen, eine Prognose ohne die zusätzlichen Ebenen und Filter zu erstellen.

## Die Prognose-Zielgruppe ist zu groß {#prediction-audience-size-is-too-big}

**Symptom:** Ihre Prognose-Zielgruppendefinition überschreitet die maximal zulässige Größe.

Eine Prognose-Zielgruppendefinition darf 100 Millionen Nutzer:innen nicht überschreiten. Wenn eine Meldung angezeigt wird, dass Ihre Zielgruppe zu groß ist, fügen Sie weitere Ebenen zu Ihrer Zielgruppe hinzu oder ändern Sie das zugrunde liegende Zeitfenster.

## Prognose hat schlechte Qualität {#prediction-has-poor-quality}

**Symptom:** Die [Prognosequalität]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics) liegt bei 39 % oder darunter.

![Screenshot zum Thema „Prognose hat schlechte Qualität“.]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Wenn Ihr Modell eine Prognosequalität von 40 % oder mehr aufweist, sind Sie in einer guten Ausgangslage. Wenn die Prognosequalität jedoch auf 39 % oder weniger sinkt, müssen Sie möglicherweise Ihre Definitionen für Abwanderung und Prognosezielgruppe spezifischer gestalten oder andere Zeitfenster verwenden.

Wenn Sie beim Erstellen Ihrer Prognosedefinitionen sowohl die Anforderung an die Zielgruppengröße nicht erfüllen als auch keine Prognosequalität von über 40 % erreichen können, bedeutet dies wahrscheinlich, dass die an Braze gesendeten Daten für diesen Anwendungsfall nicht ideal sind, dass nicht genügend Nutzer:innen vorhanden sind, um ein Modell zu erstellen, oder dass der Lebenszyklus Ihres Produkts länger ist, als unser aktuelles 60-Tage-Rückblickfenster unterstützt.

## Überlegungen zu Daten {#data-considerations}

Die folgenden Fragen sollten Sie sich stellen, wenn Sie Predictive Abwanderung or Abwanderung, Churn or Abwanderung, churnen einrichten. Modelle für maschinelles Lernen sind nur so gut wie die Daten, mit denen sie trainiert werden. Eine gute Datenhygiene und das Verständnis dessen, was in das Modell einfließt, machen also einen großen Unterschied.

- Welche wertvollen Aktionen führen zu Bindung und Treue?
- Haben Sie angepasste Events eingerichtet, die diesen spezifischen Aktionen zugeordnet sind? Predictive Abwanderung or Abwanderung, Churn or Abwanderung, churnen arbeitet mit angepassten Events im Gegensatz zu angepassten Attributen.
- Denken Sie in Zeitfenstern, innerhalb derer Sie Abwanderung or Abwanderung, Churn or Abwanderung, churnen definieren? Sie können Abwanderung or Abwanderung, Churn or Abwanderung, churnen als etwas definieren, das in bis zu 60 Tagen passiert.
- Haben Sie an Jahreszeiten gedacht, die zu untypischem Nutzer:innenverhalten führen, wie z. B. Feiertage? Rasche Veränderungen im Verbraucher:innenverhalten werden Ihre Prognosen beeinflussen.