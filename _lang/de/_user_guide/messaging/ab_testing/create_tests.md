---
nav_title: Tests erstellen
article_title: Tests erstellen
page_order: 1
page_type: reference
description: "Dieser Artikel erklärt, wie Sie multivariate und A/B-Tests mit Braze erstellen."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/messaging/ab_testing/optimizations'
---

# Multivariate und A/B-Tests erstellen {#creating-tests}

> Sie können einen multivariaten oder A/B-Test für jede Campaign erstellen, die auf einen einzelnen Kanal ausgerichtet ist. Wenn Sie beispielsweise multivariate oder A/B-Tests für eine Push-Campaign verwenden möchten, können Sie iOS- und Android-Geräte in derselben Campaign ansprechen.

![Das Dropdown-Menü nach Auswahl des Buttons „Campaign erstellen“, um entweder Multichannel oder Einzelkanal auszuwählen.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## Schritt 1: Erstellen Sie Ihre Campaign {#step-1-create-your-campaign}

1. Gehen Sie zu **Messaging** > **Campaigns**.
2. Wählen Sie **Campaign erstellen** und einen Kanal für die Campaign aus dem Bereich, der Multivariate- und A/B-Tests ermöglicht. Eine ausführliche Dokumentation zu jedem Messaging-Kanal finden Sie unter [Campaign erstellen]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign).

## Schritt 2: Varianten erstellen {#step-2-compose-your-variants}

Sie können bis zu acht Varianten Ihrer Nachricht erstellen und dabei zwischen Titeln, Inhalten, Bildern und mehr unterscheiden. Die Anzahl der Unterschiede zwischen den Nachrichten bestimmt, ob es sich um einen multivariaten oder einen A/B-Test handelt. Ein A/B-Test untersucht die Auswirkung der Änderung einer einzigen Variablen, während ein multivariater Test zwei oder mehr Variablen untersucht.

Ideen für den Einstieg in die Differenzierung Ihrer Varianten finden Sie unter [Tipps für verschiedene Kanäle](#tips-different-channels).

![Auswahl von „Variante hinzufügen“ für eine Campaign.]({% image_buster /assets/img/ab_create_2.png %})

## Schritt 3: Planen Sie Ihre Campaign {#step-3-schedule-your-campaign}

Die Planung Ihrer multivariaten Campaign funktioniert genauso wie die Planung jeder anderen Braze Campaign. Alle Standard-[Zustellungstypen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) sind verfügbar.

Nachdem ein multivariater Test begonnen hat, können Sie keine Änderungen mehr an der Campaign vornehmen. Wenn Sie die Parameter ändern, z. B. die Betreffzeile oder den HTML-Body, betrachtet Braze das Experiment als kompromittiert und deaktiviert es sofort.

Um Ihre Varianten automatisch zu optimieren, lesen Sie [A/B-Tests mit BrazeAI optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection). Einmalige und mehrfache Versand-Campaigns verwenden unterschiedliche Optimierungsmethoden und Anforderungen.

## Schritt 4: Segment auswählen und Nutzer:innen auf Varianten verteilen {#step-4-choose-a-segment-and-distribute-your-users-across-variants}

Wählen Sie Segments aus, die Sie ansprechen möchten, und verteilen Sie dann die Mitglieder auf Ihre ausgewählten Varianten und die optionale [Kontrollgruppe](#including-a-control-group). Best Practices zur Auswahl eines Segments für Tests finden Sie unter [Segment auswählen](#choosing-a-segment).

Aktivieren Sie bei unterstützten Campaigns die Option **Mit BrazeAI<sup>TM</sup> optimieren**, um die Verteilung Ihrer Varianten automatisch zu optimieren. Bei einer Campaign mit Einzelversand reserviert Braze einen Teil der Zielgruppe für einen optimierten zweiten Versand. Bei einer Campaign mit Mehrfachversand passt BrazeAI<sup>TM</sup> die Verteilung im Laufe der Zeit an.

### Kontrollgruppe {#including-a-control-group}

Sie können einen Prozentsatz Ihrer Zielgruppe für eine randomisierte Kontrollgruppe reservieren. Nutzer:innen in der Kontrollgruppe erhalten den Test nicht, aber Braze überwacht deren Konversionsrate für die Dauer der Campaign.

Bei der Auswertung Ihrer Ergebnisse können Sie die Konversionsraten Ihrer Varianten mit einer Basis-Konversionsrate vergleichen, die von Ihrer Kontrollgruppe bereitgestellt wird. So können Sie sowohl die Auswirkungen Ihrer Varianten als auch die Auswirkungen Ihrer Varianten im Vergleich zur Konversionsrate beurteilen, die sich ergeben hätte, wenn Sie gar keine Nachricht gesendet hätten.

![A/B-Test-Panel, das die prozentuale Aufschlüsselung der Kontrollgruppe, Variante 1, Variante 2 und Variante 3 mit jeweils 25 % für jede Gruppe zeigt.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
Die Verwendung einer Kontrollgruppe bei der Ermittlung eines Gewinners anhand von _Öffnungen_ oder _Klicks_ wird nicht empfohlen. Da die Kontrollgruppe die Nachricht nicht erhält, können diese Nutzer:innen keine Öffnungen oder Klicks durchführen. Daher liegt die Konversionsrate dieser Gruppe definitionsgemäß bei 0 % und stellt keinen aussagekräftigen Vergleich mit den Varianten dar.
{% endalert %}

#### Kontrollgruppen und A/B-Tests {#control-groups-and-ab-testing}

Bei Verwendung von Rate-Limiting mit einem A/B-Test wird das Rate-Limit nicht in gleicher Weise auf die Kontrollgruppe angewendet wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen darstellt. Verwenden Sie geeignete Konversions-Zeitfenster, um diese Verzerrung zu vermeiden.

#### Kontrollgruppen mit „Mit BrazeAI<sup>TM</sup> optimieren“ {#control-groups-with-optimize-with-brazeai}

Bei einer Campaign mit Mehrfachversand und [Mit BrazeAI<sup>TM</sup> optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) hängt die anfängliche Größe der Kontrollgruppe von der Anzahl der Varianten ab. Wenn jede Variante mehr als 20 % der Nutzer:innen erhält, beginnt die Kontrollgruppe bei 20 %, und die Varianten teilen die verbleibenden 80 % gleichmäßig auf. Bei mehr Varianten startet die Kontrollgruppe kleiner. Während BrazeAI<sup>TM</sup> die Performance analysiert, kann die Kontrollgruppe wachsen oder schrumpfen.

## Schritt 5: Ein Konversions-Event festlegen (optional) {#step-5-designate-a-conversion-event-optional}

Wenn Sie ein Konversions-Event für eine Campaign festlegen, können Sie sehen, wie viele Empfänger:innen dieser Campaign nach dem Erhalt eine bestimmte Aktion ausgeführt haben.

Dies wirkt sich nur auf den Test aus, wenn Sie in den vorherigen Schritten **Primäre Konversionsrate** ausgewählt haben. Weitere Informationen finden Sie unter [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

## Schritt 6: Überprüfen und starten {#step-6-review-and-launch}

Überprüfen Sie auf der Bestätigungsseite die Details Ihrer multivariaten Campaign und starten Sie den Test! Erfahren Sie als Nächstes, wie Sie [Ihre Testergebnisse verstehen]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## Wissenswertes {#things-to-know}

Wenn Ihr Experiment bereits versendet wird und Sie die Nachricht bearbeiten, wird das Experiment ungültig und alle Experimentergebnisse werden entfernt.

- Um Störungen des erwarteten Experimentverhaltens zu vermeiden, empfehlen wir, Nachrichtenänderungen innerhalb einer Stunde vor dem Start der Experiment-Campaign zu vermeiden.
- Wenn Ihr Experiment abgeschlossen ist und Sie die Nachricht nach dem Versand bearbeiten, bleiben die Experimentergebnisse in Ihren Dashboard-Analytics verfügbar. Wenn Sie die Campaign jedoch erneut starten, werden die Experimentergebnisse entfernt.

### Tipps für verschiedene Kanäle {#tips-different-channels}

Je nachdem, welchen Kanal Sie auswählen, können Sie verschiedene Komponenten Ihrer Nachricht testen. Sie können beispielsweise versuchen, Varianten mit einer Idee zu erstellen, was Sie testen möchten und was Sie beweisen möchten. Welche Hebel können Sie nutzen, und welche Effekte sind gewünscht? Obwohl es Millionen von Möglichkeiten gibt, die Sie mithilfe eines multivariaten und A/B-Tests untersuchen können, haben wir einige Vorschläge für den Einstieg:

| Kanal | Aspekte der Nachricht, die Sie ändern können | Erwartete Ergebnisse |
| ---------------------| --------------- | ------------- |
| Push | Text <br> Bild- und Emoji-Verwendung <br> Deeplinks <br> Darstellung von Zahlen (z. B. „verdreifachen“ versus „um 200 % steigern“) <br> Darstellung von Zeit (z. B. „endet um Mitternacht“ versus „endet in 6 Stunden“) | Öffnungen <br> Konversionsrate |
| E-Mail | Betreffzeile <br> Anzeigename <br> Anrede <br> Fließtext <br> Bild- und Emoji-Verwendung <br> Darstellung von Zahlen (z. B. „verdreifachen“ versus „um 200 % steigern“) <br> Darstellung von Zeit (z. B. „endet um Mitternacht“ versus „endet in 6 Stunden“) | Öffnungen <br> Konversionsrate |
| In-App-Nachricht | Für „Push“ aufgeführte Aspekte <br> [Bildspezifikationen für In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#image-specifications) | Klick <br> Konversionsrate |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipps für verschiedene Kanäle" }

{% alert tip %}
Vergessen Sie bei der Durchführung von A/B-Tests nicht, [Funnel-Berichte]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) zu erstellen, mit denen Sie verstehen können, wie jede Variante Ihren Konversions-Funnel beeinflusst hat – insbesondere wenn „Konversion“ für Ihr Unternehmen mehrere Schritte oder Aktionen umfasst.
{% endalert %}

Darüber hinaus kann die ideale Dauer Ihres Tests je nach Kanal variieren. Berücksichtigen Sie die durchschnittliche Zeit, die die meisten Nutzer:innen benötigen, um mit dem jeweiligen Kanal zu interagieren.

Wenn Sie beispielsweise Push testen, erzielen Sie möglicherweise schneller signifikante Ergebnisse als beim Testen von E-Mails, da Nutzer:innen Push-Nachrichten sofort sehen, es aber Tage dauern kann, bis sie eine E-Mail sehen oder öffnen. Wenn Sie In-App-Nachrichten testen, bedenken Sie, dass Nutzer:innen die App öffnen müssen, um die Campaign zu sehen. Daher sollten Sie länger warten, um Ergebnisse sowohl von Ihren aktivsten App-Nutzer:innen als auch von Ihren typischeren Nutzer:innen zu erfassen.

Wenn Sie sich nicht sicher sind, wie lange Ihr Test laufen sollte, kann [Mit BrazeAI<sup>TM</sup> optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) die Optimierung automatisch konfigurieren und durchführen.

### Ein Segment auswählen {#choosing-a-segment}

Da verschiedene Segmente Ihrer Nutzer:innen unterschiedlich auf Nachrichten reagieren können, sagt der Erfolg einer bestimmten Nachricht sowohl etwas über die Nachricht selbst als auch über das Zielsegment aus. Versuchen Sie daher, einen Test mit Blick auf Ihr Zielsegment zu gestalten.

Während beispielsweise aktive Nutzer:innen gleiche Reaktionsraten auf „Dieses Angebot läuft morgen ab!“ und „Dieses Angebot läuft in 24 Stunden ab!“ haben könnten, reagieren Nutzer:innen, die die App seit einer Woche nicht geöffnet haben, möglicherweise stärker auf die letztere Formulierung, da sie ein größeres Gefühl der Dringlichkeit erzeugt.

Stellen Sie außerdem bei der Auswahl des Segments für Ihren Test sicher, dass die Größe dieses Segments für Ihren Test ausreichend ist. Im Allgemeinen benötigen multivariate und A/B-Tests mit mehr Varianten eine größere Testgruppe, um statistisch signifikante Ergebnisse zu erzielen. Dies liegt daran, dass mehr Varianten dazu führen, dass weniger Nutzer:innen jede einzelne Variante sehen.

{% alert tip %}
Als Richtwert benötigen Sie wahrscheinlich etwa 15.000 Nutzer:innen pro Variante (einschließlich der Kontrollgruppe), um eine 95-prozentige Konfidenz in Ihren Testergebnissen zu erreichen. Die genaue Anzahl der benötigten Nutzer:innen kann je nach Ihrem speziellen Fall jedoch höher oder niedriger sein. Für genauere Hinweise zu Varianten-Stichprobengrößen empfiehlt es sich, einen [Stichprobengrößen-Rechner](https://www.calculator.net/sample-size-calculator.html) zu verwenden.
{% endalert %}

### Bias und Randomisierung {#bias-and-randomization}

Eine häufige Frage bei der Zuweisung zu Kontroll- und Testgruppen ist, ob diese einen Bias in Ihre Tests einführen kann. Andere fragen sich manchmal, woher wir wissen, ob diese Zuweisungen wirklich zufällig sind.

Nutzer:innen werden Nachrichtenvarianten, Canvas-Varianten oder ihren jeweiligen Kontrollgruppen zugewiesen, indem ihre (zufällig generierte) Nutzer-ID mit der (zufällig generierten) Campaign- oder Canvas-ID verkettet wird, der Modulus dieses Wertes mit 100 berechnet wird und die Nutzer:innen dann in Abschnitte eingeordnet werden, die den prozentualen Zuweisungen für Varianten und die optionale Kontrollgruppe entsprechen, die im Dashboard ausgewählt wurden. Es gibt also keine praktische Möglichkeit, dass das Verhalten der Nutzer:innen vor der Erstellung einer bestimmten Campaign oder eines Canvas systematisch zwischen Varianten und Kontrollgruppe variieren könnte. Es ist auch nicht praktikabel, zufälliger (oder genauer gesagt pseudo-zufälliger) zu sein als diese Implementierung.

#### Zu vermeidende Fehler {#mistakes-to-avoid}

Es gibt einige häufige Fehler, die den Anschein von Unterschieden basierend auf dem Messaging-Kanal erwecken können, wenn Zielgruppen nicht korrekt gefiltert werden.

Wenn Sie beispielsweise eine Push-Nachricht an eine breite Zielgruppe mit einer Kontrollgruppe senden, sendet die Testgruppe Nachrichten nur an Nutzer:innen mit einem Push-Token. Die Kontrollgruppe umfasst jedoch sowohl Nutzer:innen, die ein Push-Token haben, als auch solche, die keines haben. In diesem Fall muss Ihre anfängliche Zielgruppe für die Campaign oder das Canvas nach dem Vorhandensein eines Push-Tokens filtern (`Foreground Push Enabled` ist `true`). Dasselbe gilt für die Berechtigung zum Empfang von Nachrichten auf anderen Kanälen: Opt-in, Push-Token vorhanden oder abonniert.

Beachten Sie: Wenn eine Kontrollvariante keine Canvas-Schritte enthält, werden für Nutzer:innen in der Kontrollvariante keine Exit-Kriterien-Events protokolliert.

{% alert note %}
Wenn Sie zufällige Bucket-Nummern manuell für Kontrollgruppen verwenden, lesen Sie die [Hinweise]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for) zu Ihren Kontrollgruppen.
{% endalert %}