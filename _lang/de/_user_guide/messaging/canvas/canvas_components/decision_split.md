---
nav_title: Decision-Split
article_title: Decision-Split
alias: /decision_split/
page_order: 7
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Decision-Splits in Ihrem Canvas erstellen und verwenden."
tool: Canvas

---

# Decision-Split {#decision-split}

> Die Decision-Split-Komponente in Canvas ermöglicht es Ihnen, personalisierte Realtime-Erlebnisse für Ihre Nutzer:innen bereitzustellen.

![Ein Decision-Split-Schritt mit dem Namen „Push aktiviert?“ für Nutzer:innen, die nicht Push-aktiviert sind, und Nutzer:innen, die Push-aktiviert sind.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Diese Komponente kann verwendet werden, um Canvas-Verzweigungen basierend darauf zu erstellen, ob Nutzer:innen einer Abfrage entsprechen.

## Einen Decision-Split erstellen {#create-a-decision-split}

Um einen Decision-Split in Ihrem Workflow zu erstellen, fügen Sie einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie dann die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Decision Split**.

### Ihren Split definieren {#define-your-split}

Wie möchten Sie Ihre Nutzer:innen aufteilen? Sie können [Segmente]({{site.baseurl}}/user_guide/audience/segments/) und Filter verwenden, um die Grenze zu ziehen. Im Grunde erstellen Sie eine `true`- oder `false`-Abfrage, die Ihre Nutzer:innen auswertet und sie dann in den einen oder anderen Schritt leitet. Sie müssen mindestens ein Segment oder einen Filter verwenden. Sie müssen nicht sowohl ein Segment als auch einen Filter verwenden.

![Ein Decision-Split-Schritt mit dem ausgewählten Filter „Foreground Push Enabled is true“.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
Standardmäßig werden Segmente und Filter für einen Decision-Split-Schritt direkt nach Erhalt eines vorherigen Schritts geprüft, es sei denn, Sie fügen eine Verzögerung hinzu.
{% endalert %}

## Ihren Split verwenden {#use-your-split}

Die Verwendung eines Decision-Splits kann Ihnen helfen, Pfade für Ihre Nutzer:innen basierend auf ihrem Segment oder ihren Attributen zu unterscheiden – sogar danach, ob sie bestimmte Messaging-Kanäle nutzen, um Ihre Nachrichten zu empfangen!

Nehmen wir an, Sie erstellen einen Onboarding-Flow. Sie könnten mit einer Willkommens-E-Mail bei der Anmeldung beginnen. Zwei Tage später möchten Sie dann eine Push-Nachricht senden, aber nur an Nutzer:innen, die Push aktiviert haben. Danach erhalten alle Nutzer:innen drei Tage nach ihrer Anmeldung eine weitere E-Mail. Sie könnten Ihren Decision-Split auch verwenden, um eine In-App-Nachricht an Nutzer:innen zu senden, die Push nicht aktiviert haben, um sie zu ermutigen, Push zu aktivieren.

Wenn nach einem der Pfade kein Schritt folgt, verlassen Nutzer:innen, die diesen Pfad einschlagen, den Canvas.

![Ein Decision-Split-Schritt mit dem Namen „Push aktiviert?“ für Nutzer:innen, die nicht Push-aktiviert sind, und solche, die es sind. Nutzer:innen ohne Push-Aktivierung erleben eine 3-tägige Verzögerung und erhalten dann eine E-Mail-Nachricht. Nutzer:innen mit Push-Aktivierung erleben eine 1-tägige Verzögerung, erhalten eine Push-Benachrichtigung, gefolgt von einer 2-tägigen Verzögerung, und erhalten dann dieselbe E-Mail-Nachricht wie die Nutzer:innen ohne Push-Aktivierung.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Analytics {#analytics}

In der folgenden Tabelle finden Sie Beschreibungen der Analytics für diesen Schritt:

| Metrik | Beschreibung |
|---|---|
| _Eingetreten_ | Die Gesamtzahl der Eintritte in diesen Schritt. Wenn Ihr Canvas eine erneute Berechtigung hat und Nutzer:innen einen Decision-Split-Schritt zweimal betreten, werden zwei Eintritte erfasst. |
| _Ja_ | Die Anzahl der Eintritte, die die angegebenen Kriterien erfüllt haben und den „Ja“-Pfad eingeschlagen haben. |
| _Nein_ | Die Anzahl der Eintritte, die die angegebenen Kriterien nicht erfüllt haben und den „Nein“-Pfad eingeschlagen haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }