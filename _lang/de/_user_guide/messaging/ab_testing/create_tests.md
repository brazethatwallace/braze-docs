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

![Das Dropdown-Menü nach Auswahl des Buttons „Kampagne erstellen“, um entweder Multichannel oder Einzelkanal auszuwählen.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## 1. Schritt: Erstellen Sie Ihre Campaign {#step-1-create-your-campaign}

1. Gehen Sie zu **Messaging** > **Campaigns**.
2. Wählen Sie **Kampagne erstellen** und einen Kanal für die Campaign aus dem Bereich, der multivariate und A/B-Tests ermöglicht. Eine ausführliche Dokumentation zu jedem Messaging-Kanal finden Sie unter [Kampagne erstellen]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign).

## 2. Schritt: Verfassen Sie Ihre Varianten {#step-2-compose-your-variants}

Sie können bis zu acht Varianten Ihrer Nachricht erstellen, die sich in Titeln, Inhalten, Bildern und mehr unterscheiden. Die Anzahl der Unterschiede zwischen den Nachrichten bestimmt, ob es sich um einen multivariaten oder einen A/B-Test handelt. Ein A/B-Test untersucht die Wirkung der Änderung einer einzelnen Variable, während ein multivariater Test zwei oder mehr untersucht.

Ideen für den Einstieg in die Differenzierung Ihrer Varianten finden Sie unter [Tipps für verschiedene Kanäle](#tips-different-channels).

![Auswahl von „Variante hinzufügen“ für eine Campaign.]({% image_buster /assets/img/ab_create_2.png %})

## 3. Schritt: Planen Sie Ihre Campaign {#step-3-schedule-your-campaign}

Die Planung Ihrer multivariaten Campaign funktioniert genauso wie die Planung jeder anderen Braze-Campaign. Alle standardmäßigen [Zustellungstypen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) sind verfügbar.

Nachdem ein multivariater Test begonnen hat, können Sie keine Änderungen mehr an der Campaign vornehmen. Wenn Sie Parameter wie die Betreffzeile oder den HTML-Body ändern, betrachtet Braze das Experiment als kompromittiert und deaktiviert es sofort.

{% alert important %}
Um eine [Optimierung]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) zu verwenden (verfügbar für ausgewählte Kanäle), planen Sie Ihre Campaign für einen einmaligen Versand. Optimierungen sind nicht für Campaigns verfügbar, die sich wiederholen oder bei denen die erneute Berechtigung aktiviert ist.
{% endalert %}

## 4. Schritt: Wählen Sie ein Segment und verteilen Sie Ihre Nutzer:innen auf die Varianten {#step-4-choose-a-segment-and-distribute-your-users-across-variants}

Wählen Sie Segmente als Zielgruppe aus und verteilen Sie die Mitglieder auf Ihre ausgewählten Varianten und die optionale [Kontrollgruppe](#including-a-control-group). Best Practices zur Auswahl eines Segments für Tests finden Sie unter [Ein Segment auswählen](#choosing-a-segment).

Für Push-, E-Mail- und Webhook-Campaigns, die für einen einmaligen Versand geplant sind, können Sie auch eine [Optimierung]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) verwenden. Eine Optimierung reserviert einen Teil Ihrer Zielgruppe vom A/B-Test und hält ihn für einen zweiten, optimierten Versand zurück, der auf den Ergebnissen des ersten Tests basiert.

### Kontrollgruppe {#including-a-control-group}

Sie können einen Prozentsatz Ihrer Zielgruppe für eine randomisierte Kontrollgruppe reservieren. Nutzer:innen in der Kontrollgruppe erhalten den Test nicht, aber Braze überwacht ihre Konversionsrate für die Dauer der Campaign.

Bei der Auswertung Ihrer Ergebnisse können Sie die Konversionsraten Ihrer Varianten mit einer Baseline-Konversionsrate vergleichen, die von Ihrer Kontrollgruppe bereitgestellt wird. So können Sie sowohl die Wirkung Ihrer Varianten als auch deren Wirkung im Vergleich zur Konversionsrate beurteilen, die sich ergeben hätte, wenn Sie überhaupt keine Nachricht gesendet hätten.

![A/B-Testing-Panel, das die prozentuale Aufschlüsselung der Kontrollgruppe, Variante 1, Variante 2 und Variante 3 mit jeweils 25 % für jede Gruppe zeigt.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
Die Verwendung einer Kontrollgruppe bei der Bestimmung einer Gewinnervariante anhand von _Öffnungen_ oder _Klicks_ wird nicht empfohlen. Da die Kontrollgruppe die Nachricht nicht erhält, können diese Nutzer:innen keine Öffnungen oder Klicks durchführen. Daher beträgt die Konversionsrate dieser Gruppe per Definition 0 % und stellt keinen aussagekräftigen Vergleich mit den Varianten dar.
{% endalert %}

#### Kontrollgruppen mit A/B-Tests {#control-groups-with-ab-testing}

Bei Verwendung von Rate-Limiting mit einem A/B-Test wird das Rate-Limit nicht auf die gleiche Weise auf die Kontrollgruppe angewendet wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen darstellt. Verwenden Sie geeignete Conversion-Fenster, um diese Verzerrung zu vermeiden.

#### Kontrollgruppen mit Intelligenter Auswahl {#control-groups-with-intelligent-selection}

Die Größe der Kontrollgruppe für eine Campaign mit [Intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) basiert auf der Anzahl der Varianten. Wenn jede Variante an mehr als 20 % der Nutzer:innen gesendet wird, beträgt die Kontrollgruppe 20 %, und die Varianten werden gleichmäßig auf die verbleibenden 80 % aufgeteilt. Wenn Sie jedoch genügend Varianten haben, sodass jede Variante an weniger als 20 % der Nutzer:innen gesendet wird, muss die Kontrollgruppe kleiner werden. Wenn die Intelligente Auswahl beginnt, die Performance Ihres Tests zu analysieren, wächst oder schrumpft die Kontrollgruppe basierend auf den Ergebnissen.

## 5. Schritt: Legen Sie ein Konversions-Event fest (optional) {#step-5-designate-a-conversion-event-optional}

Das Festlegen eines Konversions-Events für eine Campaign ermöglicht es Ihnen zu sehen, wie viele Empfänger:innen dieser Campaign nach dem Erhalt eine bestimmte Aktion durchgeführt haben.

Dies wirkt sich nur auf den Test aus, wenn Sie in den vorherigen Schritten **Primary Conversion Rate** gewählt haben. Weitere Informationen finden Sie unter [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

## 6. Schritt: Überprüfen und starten {#step-6-review-and-launch}

Überprüfen Sie auf der Bestätigungsseite die Details Ihrer multivariaten Campaign und starten Sie den Test! Erfahren Sie als Nächstes, wie Sie [Ihre Testergebnisse verstehen]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## Wissenswertes {#things-to-know}

Wenn Ihr Experiment bereits mit dem Versand begonnen hat und Sie die Nachricht bearbeiten, wird das Experiment ungültig und alle Experimentergebnisse werden entfernt.

- Um Störungen des erwarteten Experimentverhaltens zu vermeiden, empfehlen wir, Nachrichtenbearbeitungen innerhalb einer Stunde nach dem Start der Experiment-Campaign zu vermeiden.
- Wenn Ihr Experiment abgeschlossen ist und Sie die Nachricht nach dem Versand bearbeiten, bleiben die Experimentergebnisse in Ihren Dashboard-Analytics verfügbar. Wenn Sie die Campaign jedoch erneut starten, werden die Experimentergebnisse entfernt.

### Tipps für verschiedene Kanäle {#tips-different-channels}

Je nachdem, welchen Kanal Sie auswählen, können Sie verschiedene Komponenten Ihrer Nachricht testen. Versuchen Sie beispielsweise, Varianten mit einer Idee zu verfassen, was Sie testen möchten und was Sie beweisen wollen. Welche Hebel können Sie betätigen, und welche Effekte sind gewünscht? Obwohl es Millionen von Möglichkeiten gibt, die Sie mit einem multivariaten und A/B-Test untersuchen können, haben wir einige Vorschläge für den Einstieg:

| Kanal | Aspekte der Nachricht, die Sie ändern können | Ergebnisse, auf die Sie achten sollten |
| ---------------------| --------------- | ------------- |
| Push | Text <br> Bild- und Emoji-Verwendung <br> Deeplinks <br> Darstellung von Zahlen (z. B. „verdreifachen“ versus „um 200 % steigern“) <br> Darstellung von Zeit (z. B. „endet um Mitternacht“ versus „endet in 6 Stunden“) | Öffnungen <br> Konversionsrate |
| E-Mail | Betreff <br> Anzeigename <br> Anrede <br> Fließtext <br> Bild- und Emoji-Verwendung <br> Darstellung von Zahlen (z. B. „verdreifachen“ versus „um 200 % steigern“) <br> Darstellung von Zeit (z. B. „endet um Mitternacht“ versus „endet in 6 Stunden“) | Öffnungen <br> Konversionsrate |
| In-App-Nachricht | Aspekte wie bei „Push“ aufgeführt <br> [Bildspezifikationen für In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#in-app-messages) | Klick <br> Konversionsrate |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipps für verschiedene Kanäle" }

{% alert tip %}
Vergessen Sie bei der Durchführung von A/B-Tests nicht, [Funnel-Berichte]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) zu generieren, mit denen Sie verstehen können, wie jede Variante Ihren Konversionstrichter beeinflusst hat – insbesondere wenn „Conversion“ für Ihr Unternehmen mehrere Schritte oder Aktionen umfasst.
{% endalert %}

Darüber hinaus kann die ideale Dauer Ihres Tests je nach Kanal variieren. Bedenken Sie die durchschnittliche Zeit, die die meisten Nutzer:innen benötigen, um mit jedem Kanal zu interagieren.

Wenn Sie beispielsweise einen Push testen, erzielen Sie möglicherweise schneller signifikante Ergebnisse als beim Testen von E-Mails, da Nutzer:innen Push-Nachrichten sofort sehen, es aber Tage dauern kann, bis sie eine E-Mail sehen oder öffnen. Wenn Sie In-App-Nachrichten testen, bedenken Sie, dass Nutzer:innen die App öffnen müssen, um die Campaign zu sehen. Sie sollten daher länger auf Ergebnisse warten, sowohl von Ihren aktivsten App-Nutzer:innen als auch von Ihren typischeren Nutzer:innen.

Wenn Sie unsicher sind, wie lange Ihr Test laufen sollte, kann das Feature [Intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) nützlich sein, um eine Gewinnervariante effizient zu finden.

### Ein Segment auswählen {#choosing-a-segment}

Da verschiedene Segmente Ihrer Nutzer:innen unterschiedlich auf Nachrichten reagieren können, sagt der Erfolg einer bestimmten Nachricht sowohl etwas über die Nachricht selbst als auch über ihr Zielsegment aus. Versuchen Sie daher, einen Test mit Blick auf Ihr Zielsegment zu gestalten.

Während aktive Nutzer:innen beispielsweise gleiche Reaktionsraten auf „Dieses Angebot läuft morgen ab!“ und „Dieses Angebot läuft in 24 Stunden ab!“ haben könnten, reagieren Nutzer:innen, die die App seit einer Woche nicht geöffnet haben, möglicherweise stärker auf die letztere Formulierung, da sie ein größeres Gefühl der Dringlichkeit erzeugt.

Achten Sie außerdem bei der Auswahl des Segments für Ihren Test darauf, dass die Größe dieses Segments groß genug für Ihren Test ist. Im Allgemeinen benötigen multivariate und A/B-Tests mit mehr Varianten eine größere Testgruppe, um statistisch signifikante Ergebnisse zu erzielen. Dies liegt daran, dass mehr Varianten dazu führen, dass weniger Nutzer:innen jede einzelne Variante sehen.

{% alert tip %}
Als Richtwert benötigen Sie wahrscheinlich etwa 15.000 Nutzer:innen pro Variante (einschließlich der Kontrollgruppe), um eine 95%ige Konfidenz in Ihren Testergebnissen zu erreichen. Die genaue Anzahl der benötigten Nutzer:innen kann jedoch je nach Ihrem speziellen Fall höher oder niedriger sein. Für genauere Hinweise zu Stichprobengrößen für Varianten empfiehlt es sich, einen [Stichprobengrößenrechner](https://www.calculator.net/sample-size-calculator.html) zu verwenden.
{% endalert %}

### Verzerrung und Randomisierung {#bias-and-randomization}

Eine häufige Frage bei der Zuweisung von Kontroll- und Testgruppen ist, ob diese Verzerrungen in Ihre Tests einführen können. Andere fragen sich manchmal, wie wir wissen, ob diese Zuweisungen wirklich zufällig sind.

Nutzer:innen werden Nachrichtenvarianten, Canvas-Varianten oder ihren jeweiligen Kontrollgruppen zugewiesen, indem ihre (zufällig generierte) Nutzer-ID mit der (zufällig generierten) Campaign- oder Canvas-ID verkettet wird, der Modulo 100 dieses Werts berechnet wird und die Nutzer:innen dann in Abschnitte eingeordnet werden, die den im Dashboard gewählten prozentualen Zuweisungen für Varianten und optionale Kontrollgruppe entsprechen. Es gibt also keine praktische Möglichkeit, dass das Verhalten von Nutzer:innen vor der Erstellung einer bestimmten Campaign oder eines Canvas systematisch zwischen Varianten und Kontrollgruppe variieren könnte. Es ist auch nicht praktikabel, zufälliger (oder genauer gesagt, pseudo-zufälliger) zu sein als diese Implementierung.

#### Fehler, die Sie vermeiden sollten {#mistakes-to-avoid}

Es gibt einige häufige Fehler, die den Anschein von Unterschieden basierend auf dem Messaging-Kanal erzeugen können, wenn Zielgruppen nicht korrekt gefiltert werden.

Wenn Sie beispielsweise eine Push-Nachricht an eine breite Zielgruppe mit einer Kontrollgruppe senden, sendet die Testgruppe Nachrichten nur an Nutzer:innen mit einem Push-Token. Die Kontrollgruppe umfasst jedoch sowohl Nutzer:innen, die ein Push-Token haben, als auch solche, die keines haben. In diesem Fall muss Ihre anfängliche Zielgruppe für die Campaign oder das Canvas nach dem Vorhandensein eines Push-Tokens filtern (`Foreground Push Enabled` ist `true`). Dasselbe gilt für die Berechtigung zum Empfang von Nachrichten auf anderen Kanälen: Opt-in, Push-Token vorhanden oder abonniert.

Beachten Sie, dass wenn eine Kontrollvariante keine Canvas-Schritte enthält, Exit-Kriterien-Events für Nutzer:innen in der Kontrollvariante nicht protokolliert werden.

{% alert note %}
Wenn Sie manuell zufällige Bucket-Nummern für Kontrollgruppen verwenden, lesen Sie die [Hinweise]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for) zu Ihren Kontrollgruppen.
{% endalert %}