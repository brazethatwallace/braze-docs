---
nav_title: Analytics
article_title: A/B-Test-Analytics
page_order: 10
page_type: reference
description: "Dieser Artikel erklärt, wie Sie die Ergebnisse einer multivariaten oder A/B-Campaign anzeigen und interpretieren."
---

# Multivariate und A/B-Test-Analytics {#multivariate-and-ab-test-analytics}

> Dieser Artikel erklärt, wie Sie die Ergebnisse eines multivariaten oder A/B-Tests anzeigen. Wenn Sie Ihren Test noch nicht eingerichtet haben, lesen Sie [Multivariate und A/B-Tests erstellen]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) für die einzelnen Schritte.

Nachdem Ihre Campaign gestartet wurde, können Sie die Performance jeder Variante überprüfen, indem Sie Ihre Campaign im Bereich **Campaigns** des Dashboards auswählen.

## Analytics nach Optimierungsoption {#analytics-by-optimization-option}

Ihre Analytics-Ansicht variiert je nachdem, ob Sie während der Ersteinrichtung eine [Optimierung]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) ausgewählt haben.

### Manuelle Variantenverteilung {#manual-variant-distribution}

Wenn **Optimize with BrazeAI<sup>TM</sup>** deaktiviert ist, zeigt die Seite **Kampagnen-Analytics** die Performance Ihrer Varianten im Vergleich zur Kontrollgruppe an, sofern Sie eine einbezogen haben.

![Performance-Bereich der Kampagnen-Analytics für eine E-Mail-Campaign mit mehreren Varianten. Die Tabelle listet verschiedene Performance-Metriken für jede Variante auf, wie Empfänger:innen, Bounces, Klicks und Konversionen.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Weitere Details finden Sie im Artikel [Kampagnen-Analytics]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) für Ihren Messaging-Kanal.

### Optimize with BrazeAI<sup>TM</sup> {#optimize-with-brazeai}

Wenn Sie **Optimize with BrazeAI<sup>TM</sup>** verwenden, zeigt die Campaign-Übersicht jede Steigerung nach dem Experimentfenster für eine Einmalversand-Campaign oder nach der ersten Optimierungsperiode für eine Mehrfachversand-Campaign an. Einmalversand-Campaigns zeigen zusätzlich Details zum initialen Test und zur leistungsstärksten Variante.

Weitere Informationen finden Sie unter [A/B-Tests mit BrazeAI optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

![Kampagnen-Analytics mit Steigerung durch Optimize with BrazeAI<sup>TM</sup>, einschließlich Vergleichsmetriken nach dem Experimentfenster.]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

### Einmalversand-Optimierung {#single-send-optimization}

Bei einer Einmalversand-Campaign mit **Optimize with BrazeAI<sup>TM</sup>** zeigt der Tab **A/B Test Result** die Ergebnisse des initialen Tests und des optimierten Versands.

Das **A/B Test Result** ist in zwei Tabs unterteilt: **Initial Test** und **Winning Variant**.

{% tabs local %}
{% tab Initial Test %}

Der Tab **Initial Test** zeigt die Metriken für jede Variante aus dem initialen A/B-Test, der an einen Teil Ihres Zielsegments gesendet wurde. Sie können eine Zusammenfassung sehen, wie alle Varianten abgeschnitten haben und ob es während des Tests eine Gewinnervariante gab.

Wenn eine Variante alle anderen mit mehr als 95 % [Konfidenz]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence) übertroffen hat, markiert Braze diese Variante mit dem Label „Winner“.

Wenn keine Variante alle anderen mit 95 % Konfidenz übertrifft und Sie sich dennoch entschieden haben, die leistungsstärkste Variante zu senden, wird die leistungsstärkste Variante trotzdem versendet und mit dem Label „Winner“ gekennzeichnet.

![Ergebnisse eines initialen Tests zur Bestimmung der Gewinnervariante, bei dem keine Variante die anderen mit ausreichender Konfidenz übertroffen hat, um die Schwelle von 95 Prozent für statistische Signifikanz zu erreichen.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Wie die Gewinnervariante ausgewählt wird {#how-the-winning-variant-is-selected}

Braze testet alle Varianten gegeneinander mit [Pearsons Chi-Quadrat-Tests](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Damit wird gemessen, ob eine Variante alle anderen statistisch auf einem Signifikanzniveau von p < 0,05 übertrifft, was wir als 95%ige Signifikanz bezeichnen. Wenn ja, wird die Gewinnervariante mit dem Label „Winner“ gekennzeichnet.

Dies ist ein separater Test vom Konfidenzwert, der nur die Performance einer Variante im Vergleich zur Kontrollgruppe mit einem numerischen Wert zwischen 0 und 100 % beschreibt.

Eine Variante kann besser abschneiden als die Kontrollgruppe, aber der Chi-Quadrat-Test prüft, ob eine Variante besser ist als alle anderen. [Folgetests](#recommended-follow-ups) können weitere Details liefern.

{% endtab %}
{% tab Winning Variant %}

Der Tab **Winning Variant** zeigt die Ergebnisse des zweiten Versands, bei dem jede:r verbleibende Nutzer:in die leistungsstärkste Variante aus dem initialen Test erhalten hat. Ihr **Audience %** summiert sich zum Prozentsatz des Zielsegments, das Sie für die Winning-Variant-Gruppe reserviert haben.

![Ergebnisse der Gewinnervariante, die an die Winning-Variant-Gruppe gesendet wurde.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Wenn Sie die Performance der Gewinnervariante über die gesamte Campaign hinweg sehen möchten, einschließlich der A/B-Test-Versendungen, überprüfen Sie die Seite **Kampagnen-Analytics**.

### Bestehende Personalisierte-Variante-Campaigns {#personalized-variant}

Personalisierte Variante ist für neue Campaigns nicht verfügbar. Bei einer bestehenden Campaign, die diese Optimierung verwendet, ist das **A/B Test Result** in zwei Tabs unterteilt: **Initial Test** und **Personalized Variant**.

{% tabs local %}
{% tab Initial Test %}

Der Tab **Initial Test** zeigt die Metriken für jede Variante aus dem initialen A/B-Test, der an einen Teil Ihres Zielsegments gesendet wurde.

![Ergebnisse eines initialen Tests zur Bestimmung der leistungsstärksten Variante für jede:n Nutzer:in. Eine Tabelle zeigt die Performance jeder Variante anhand verschiedener Metriken für den Zielkanal.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Standardmäßig sucht der Test nach Zusammenhängen zwischen den angepassten Events jeder:s Nutzer:in und deren Nachrichtenvarianten-Präferenzen. Diese Analyse erkennt, ob angepasste Events die Wahrscheinlichkeit erhöhen oder verringern, auf eine bestimmte Nachrichtenvariante zu reagieren. Diese Beziehungen werden dann verwendet, um zu bestimmen, welche Nutzer:innen welche Nachrichtenvariante im endgültigen Versand erhalten.

Die Beziehungen zwischen angepassten Events und Nachrichtenpräferenzen werden in der Tabelle auf dem Tab **Initial Send** angezeigt.

![Tabellen mit angepassten Event-Daten für Variante 1 und Variante 2, die Impact-Scores für angepasste Events zeigen und angeben, wie jedes Event die Variantenpräferenz beeinflusst.]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Wenn der Test keine aussagekräftige Beziehung zwischen angepassten Events und Pfadpräferenzen finden kann, greift der Test auf eine sitzungsbasierte Analysemethode zurück, und es werden keine Tabellen mit angepassten Event-Daten angezeigt.

{% details Fallback-Analysemethode %}

**Sitzungsbasierte Analysemethode**<br>
Wenn die Fallback-Methode zur Bestimmung personalisierter Varianten verwendet wird, zeigt der Tab **Initial Test** eine Aufschlüsselung der bevorzugten Varianten der Nutzer:innen basierend auf einer Kombination bestimmter Merkmale.

Diese Merkmale sind:

- **Aktualität:** Wann sie zuletzt eine Sitzung hatten
- **Häufigkeit:** Wie oft sie Sitzungen haben
- **Zugehörigkeitsdauer:** Wie lange sie bereits Nutzer:in sind

Zum Beispiel könnte der Test ergeben, dass die meisten Nutzer:innen Variante A bevorzugen, aber Nutzer:innen, die vor etwa 3–12 Tagen eine Sitzung hatten, zwischen 1–12 Tage zwischen Sitzungen haben und in den letzten 67–577 Tagen erstellt wurden, bevorzugen tendenziell Variante B. Daher erhielten Nutzer:innen in dieser Untergruppe Variante B im zweiten Versand, während die übrigen Variante A erhielten.

![Die Tabelle „User Characteristics“, die zeigt, welche Nutzer:innen voraussichtlich Variante A und Variante B bevorzugen, basierend auf den drei Buckets, in die sie bei Aktualität, Häufigkeit und Zugehörigkeitsdauer fallen.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Wie personalisierte Varianten ausgewählt werden**<br>
Bei dieser Methode ergibt sich die empfohlene Nachricht für eine:n einzelne:n Nutzer:in aus der Summe der Effekte ihrer spezifischen Aktualität, Häufigkeit und Zugehörigkeitsdauer. Aktualität, Häufigkeit und Zugehörigkeitsdauer werden in Buckets aufgeteilt, wie in der Tabelle **User Characteristics** dargestellt. Der Zeitbereich jedes Buckets wird durch die Daten der Nutzer:innen in jeder einzelnen Campaign bestimmt und variiert von Campaign zu Campaign.

Jeder Bucket kann einen unterschiedlichen Beitrag oder „Push“ in Richtung jeder Nachrichtenvariante haben. Die Stärke des Pushs für jeden Bucket wird anhand der Nutzer:innen-Reaktionen im initialen Versand mittels [logistischer Regression](https://en.wikipedia.org/wiki/Logistic_regression) bestimmt. Diese Tabelle fasst die Ergebnisse nur zusammen, indem sie anzeigt, mit welcher Variante Nutzer:innen in jedem Bucket tendenziell interagiert haben. Die tatsächliche personalisierte Variante einer:s einzelnen Nutzer:in hängt von der Summe der Effekte der drei Buckets ab, in denen sie sich befinden – einer für jedes Merkmal.

{% enddetails %}

{% endtab %}
{% tab Personalized Variant %}

Der Tab **Personalized Variant** zeigt die Ergebnisse des zweiten Versands, bei dem jede:r verbleibende Nutzer:in die Variante erhalten hat, mit der sie am wahrscheinlichsten interagieren würden.

Die drei Karten auf dieser Seite zeigen Ihre prognostizierte Steigerung, die Gesamtergebnisse und die projizierten Ergebnisse, wenn Sie stattdessen nur die Gewinnervariante gesendet hätten. Auch wenn es keine Steigerung gibt, was manchmal vorkommen kann, ist das Ergebnis dasselbe wie beim Versand nur der Gewinnervariante (ein traditioneller A/B-Test).

- **Prognostizierte Steigerung:** Die Verbesserung Ihrer ausgewählten Optimierungsmetrik für diesen Versand durch die Verwendung personalisierter Varianten anstelle eines Standard-A/B-Tests (wenn die verbleibenden Nutzer:innen nur die Gewinnervariante erhalten hätten).
- **Gesamtergebnisse:** Die Ergebnisse des zweiten Versands basierend auf Ihrer gewählten Optimierungsmetrik (*Eindeutige Öffnungen*, *Eindeutige Klicks* oder *Primäres Konversions-Event*).
- **Projizierte Ergebnisse:** Die projizierten Ergebnisse des zweiten Versands basierend auf Ihrer gewählten Optimierungsmetrik, wenn Sie stattdessen nur die Gewinnervariante gesendet hätten.

![Tab „Personalized Variant“ für eine Campaign, die für eindeutige Öffnungen optimiert wurde. Die Karten zeigen die prognostizierte Steigerung, die gesamten eindeutigen Öffnungen (mit personalisierter Variante) und die projizierten eindeutigen Öffnungen (mit Gewinnervariante).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

Die Tabelle auf dieser Seite zeigt die Metriken für jede Variante aus dem Versand der personalisierten Variante. Ihr **Audience %** summiert sich zum Prozentsatz des Zielsegments, das Sie für die Personalized-Variant-Gruppe reserviert haben.

![Ergebnistabelle des Versands der personalisierten Variante mit Performance-Metriken für Variante A, Variante B und alle Varianten, einschließlich Zielgruppenprozentsatz, Versendungen, Zustellungen, Öffnungen, Klicks und Konversionen.]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Konfidenz verstehen {#understanding-confidence}

Konfidenz ist das statistische Maß dafür, wie sicher wir sind, dass ein Unterschied in den Daten, wie z. B. Konversionsraten, real ist und nicht nur auf zufällige Schwankungen zurückzuführen ist.

{% alert note %}
Sehen Sie keine Konfidenz in Ihren Ergebnissen? Konfidenz wird nur angezeigt, wenn Sie eine Kontrollgruppe haben.
{% endalert %}

Ein wichtiger Teil Ihrer Ergebnisse ist die Konfidenz. Was wäre zum Beispiel, wenn die Kontrollgruppe eine Konversionsrate von 20 % und Variante A eine Konversionsrate von 25 % hätte? Das scheint darauf hinzudeuten, dass das Senden von Variante A effektiver ist als das Senden keiner Nachricht. Eine Konfidenz von 95 % bedeutet, dass der Unterschied zwischen den beiden Konversionsraten wahrscheinlich auf einen tatsächlichen Unterschied in den Reaktionen der Nutzer:innen zurückzuführen ist und dass es nur eine 5-prozentige Wahrscheinlichkeit gibt, dass der Unterschied zufällig entstanden ist.

Braze vergleicht die Konversionsrate jeder Variante mit der Konversionsrate der Kontrollgruppe mithilfe eines statistischen Verfahrens namens [Z-Test](https://en.wikipedia.org/wiki/Z-test). Ein Ergebnis von 95 % oder höherer Konfidenz, wie im vorherigen Beispiel, zeigt an, dass der Unterschied statistisch bedeutsam ist. Dies gilt überall dort, wo Sie im Braze-Dashboard eine Konfidenzmetrik sehen, die den Unterschied zwischen zwei Nachrichten oder Nutzer:innen-Populationen beschreibt.

Im Allgemeinen ist eine Konfidenz von mindestens 95 % erforderlich, um zu zeigen, dass Ihre Ergebnisse die tatsächlichen Präferenzen der Nutzer:innen widerspiegeln und nicht auf Zufall beruhen. In strengen wissenschaftlichen Tests ist 95 % Konfidenz (oder anders ausgedrückt: ein „p“-Wert von weniger als 0,05) der gängige Maßstab zur Bestimmung statistischer Signifikanz. Wenn Sie wiederholt keine 95 % Konfidenz erreichen, versuchen Sie, Ihre Stichprobengröße zu erhöhen oder die Anzahl der Varianten zu reduzieren.

Konfidenz beschreibt, wie wahrscheinlich es ist, dass ein beobachteter Unterschied zwischen den Konversionsraten von Variante und Kontrollgruppe real ist und nicht auf zufällige Schwankungen zurückzuführen ist. Sie ist eine Funktion der Stichprobengröße und der Größe des Unterschieds zwischen den Konversionsraten. Ob die Gesamtkonversionsraten hoch oder niedrig sind, ist in der Regel weniger wichtig als der beobachtete Unterschied und die Stichprobengröße für die Stärke des Konfidenzmaßes. Es ist möglich, dass eine Variante eine sehr unterschiedliche Konversionsrate im Vergleich zu einer anderen hat und dennoch keine Konfidenz von 95 % oder höher erreicht. Es ist auch möglich, dass zwei Gruppen von Varianten ähnliche Konversions- oder Uplift-Raten haben und dennoch unterschiedliche Konfidenz aufweisen.

Wenn mehr Daten eintreffen, kann die Konfidenz sinken, wenn sich die Konversionsraten von Variante und Kontrollgruppe annähern – der Unterschied, den Sie messen, wird kleiner, was den Effekt einer größeren Stichprobe überwiegen kann.

### Statistisch nicht signifikante Ergebnisse {#statistically-insignificant-results}

Ein Test, der keine Konfidenz von 95 % erreicht, kann dennoch wichtige Erkenntnisse liefern. Hier sind einige Dinge, die Sie aus einem Test mit statistisch nicht signifikanten Ergebnissen lernen können:

- Es ist möglich, dass alle Ihre Varianten ungefähr den gleichen Effekt hatten. Das zu wissen, spart Ihnen die Zeit, die Sie für diese Änderungen aufgewendet hätten. Manchmal stellen Sie fest, dass konventionelle Marketing-Taktiken, wie das Wiederholen Ihres Call-to-Action, nicht unbedingt für Ihre Zielgruppe funktionieren.
- Obwohl Ihre Ergebnisse möglicherweise auf Zufall beruhen, können sie die Hypothese für Ihren nächsten Test informieren. Wenn mehrere Varianten ungefähr die gleichen Ergebnisse zu haben scheinen, führen Sie einige davon erneut zusammen mit neuen Varianten durch, um zu sehen, ob Sie eine effektivere Alternative finden können. Wenn eine Variante besser abschneidet, aber nicht signifikant, können Sie einen weiteren Test durchführen, bei dem der Unterschied dieser Variante stärker ausgeprägt ist.
- Testen Sie weiter! Ein Test mit nicht signifikanten Ergebnissen sollte zu bestimmten Fragen führen. Gab es wirklich keinen Unterschied zwischen Ihren Varianten? Hätten Sie Ihren Test anders strukturieren sollen? Sie können diese Fragen beantworten, indem Sie Folgetests durchführen.
- Obwohl Tests nützlich sind, um herauszufinden, welche Art von Messaging die meiste Resonanz bei Ihrer Zielgruppe erzeugt, ist es auch wichtig zu verstehen, welche Änderungen im Messaging nur einen vernachlässigbaren Effekt haben. So können Sie entweder weiter nach einer effektiveren Alternative testen oder die Zeit sparen, die für die Entscheidung zwischen zwei alternativen Nachrichten aufgewendet worden wäre.

Unabhängig davon, ob Ihr Test einen klaren Gewinner hat, kann es hilfreich sein, einen [Folgetest](#recommended-follow-ups) durchzuführen, um Ihre Ergebnisse zu bestätigen oder Ihre Erkenntnisse auf ein leicht anderes Szenario anzuwenden.

## Diskrepanzen zwischen Kontrollgruppe und Variante {#discrepancies-between-the-control-group-and-variant}

Bei In-App-Nachrichten-Campaigns mit A/B- oder multivariaten Aufteilungen sind die von Ihnen konfigurierten Prozentsätze Zuweisungsziele. Die gemeldeten Impressionen stimmen selten genau mit diesen Prozentsätzen überein, da nur Nutzer:innen, die die Trigger or triggern-Aktion ausführen, Impressionen protokollieren und Kontrollgruppen-Nutzer:innen, die den Trigger or triggern auslösen, eine Impression protokollieren, obwohl sie keine Nachricht sehen.

Nehmen wir zum Beispiel an, eine Campaign hat beim Start eine Zielgruppe von 200 Nutzer:innen, mit 100 Nutzer:innen in der Kontrollgruppe und 100 Nutzer:innen in der Variante.

Die 100 Nutzer:innen in der Variante erhalten die In-App-Nachrichten-Payload, und 50 von ihnen führen die Trigger or triggern-Aktion aus und sehen die In-App-Nachricht. Die 100 Nutzer:innen in der Kontrollgruppe werden nur getrackt, wenn sie die Trigger or triggern-Aktion der Campaign ausführen, und 75 von ihnen führen die Trigger or triggern-Aktion aus und protokollieren eine Impression, sehen aber die In-App-Nachricht nicht.

Trotz der anfänglichen 50/50-Aufteilung sind die protokollierten eindeutigen Impressionen nicht ausgeglichen. Die Variantengruppe hat 50 Impressionen, während die Kontrollgruppe 75 Impressionen hat.

Außerdem können Varianten-Nachrichten, die eine längere Renderzeit erfordern, wie z. B. solche mit großen Bildern oder Connected-Content-Templates, weniger Impressionen als die Kontrollgruppe protokollieren, wenn Nutzer:innen die Nachricht Trigger or triggern or triggern, aber die Seite verlassen, bevor das Rendering abgeschlossen ist.

### Verzögerungen bei In-App-Nachrichten {#in-app-message-delays}

Bei getriggerten In-App-Nachrichten-Campaigns mit verzögerter Anzeige werden Kontrollgruppen-Impressionen zu dem Zeitpunkt erfasst, zu dem die Nutzer:innen die In-App-Nachricht ursprünglich erhalten hätten. Wenn eine Campaign beispielsweise so eingestellt ist, dass die Anzeige um eine Stunde verzögert wird, werden Kontrollgruppen-Impressionen erst nach Ablauf der einstündigen Verzögerung protokolliert. Dies hilft beim genauen Tracking von Impressionen in Bezug auf den beabsichtigten Zeitpunkt der Nachrichtenzustellung.

## Entfernen von Nachrichten-Varianten nach dem Start {#removing-message-variants-after-launch}

Wenn Sie eine Nachrichten-Variante aus einer Campaign oder einem Canvas entfernen, indem Sie im Composer auf das **X** klicken (z. B. wenn Sie eine Nachricht aus einem Template ersetzen), wird die Variante als gelöscht markiert. Analytics sind an die eindeutige ID jeder Variante gebunden, sodass das Entfernen einer Variante das Reporting beeinflusst:

- Bereits vorhandene Analytics für die gelöschte Variante (wie Öffnungen, Klicks und Konversionen) erscheinen nicht mehr in den aktuellen Analytics der Campaign oder des Canvas-Schritts.
- Aufschlüsselungen auf Varianten-Ebene schließen gelöschte Varianten aus. Wenn Sie eine Ersatz-Variante hinzufügen, erhält diese eine neue Varianten-ID und beginnt ohne historische Statistiken, sodass Metriken möglicherweise als 0 angezeigt werden.

Dies gilt nur, wenn Sie Varianten löschen und erneut hinzufügen. Das Bearbeiten des Inhalts einer bestehenden Variante wirkt sich nicht auf historische Analytics aus.

Weitere Details zu gelöschten Varianten im Reporting finden Sie unter [Gelöschte Nachrichten-Varianten]({{site.baseurl}}/user_guide/analytics/reports/report_builder#deleted-message-variants).

## Empfohlene Folgeaktionen {#recommended-follow-ups}

Ein multivariater und A/B-Test kann (und sollte!) Ideen für zukünftige Tests inspirieren und Sie zu Änderungen in Ihrer Messaging-Strategie anleiten. Mögliche Folgeaktionen umfassen:

### Ändern Sie Ihre Messaging-Strategie basierend auf Testergebnissen {#change-your-messaging-strategy-based-on-test-results}

Ihre multivariaten Ergebnisse können Sie dazu veranlassen, die Art und Weise zu ändern, wie Sie Ihre Nachrichten formulieren oder formatieren.

### Ändern Sie die Art, wie Sie Ihre Nutzer:innen verstehen {#change-the-way-you-understand-your-users}

Jeder Test beleuchtet das Verhalten Ihrer Nutzer:innen, wie Nutzer:innen auf verschiedene Messaging-Kanäle reagieren und die Unterschiede (und Gemeinsamkeiten) zwischen Ihren Segmenten.

### Verbessern Sie die Strukturierung zukünftiger Tests {#improve-the-way-you-structure-future-tests}

War Ihre Stichprobengröße zu klein? Waren die Unterschiede zwischen Ihren Varianten zu subtil? Jeder Test bietet die Möglichkeit zu lernen, wie zukünftige Tests verbessert werden können. Wenn Ihre Konfidenz niedrig ist, ist Ihre Stichprobengröße zu klein und sollte für zukünftige Tests vergrößert werden. Wenn Sie keinen klaren Unterschied in der Performance Ihrer Varianten feststellen, ist es möglich, dass die Unterschiede zu subtil waren, um einen erkennbaren Effekt auf die Reaktionen der Nutzer:innen zu haben.

### Führen Sie einen Folgetest mit einer größeren Stichprobengröße durch {#run-a-follow-up-test-with-a-larger-sample-size}

Größere Stichproben erhöhen die Chancen, kleine Unterschiede zwischen Varianten zu erkennen.

### Führen Sie einen Folgetest über einen anderen Messaging-Kanal durch {#run-a-follow-up-test-using-a-different-messaging-channel}

Wenn Sie feststellen, dass eine bestimmte Strategie in einem Kanal sehr effektiv ist, möchten Sie diese Strategie möglicherweise in anderen Kanälen testen. Wenn eine Art von Nachricht in einem Kanal effektiv ist, aber nicht in einem anderen, können Sie möglicherweise schlussfolgern, dass bestimmte Kanäle für bestimmte Arten von Nachrichten besser geeignet sind. Oder vielleicht gibt es einen Unterschied zwischen Nutzer:innen, die eher Push-Benachrichtigungen aktivieren, und solchen, die eher auf In-App-Nachrichten achten. Letztendlich hilft Ihnen die Durchführung dieser Art von Test zu verstehen, wie Ihre Zielgruppe mit Ihren verschiedenen Kommunikationskanälen interagiert.

### Führen Sie einen Folgetest mit einem anderen Segment von Nutzer:innen durch {#run-a-follow-up-test-on-a-different-segment-of-users}

Erstellen Sie dazu einen weiteren Test mit demselben Messaging-Kanal und denselben Varianten, wählen Sie aber ein anderes Segment von Nutzer:innen. Wenn beispielsweise eine Art von Messaging bei engagierten Nutzer:innen äußerst effektiv war, kann es nützlich sein, die Wirkung auf inaktive Nutzer:innen zu untersuchen. Es ist möglich, dass die inaktiven Nutzer:innen ähnlich reagieren, oder sie bevorzugen möglicherweise eine der anderen Varianten. Dieser Test hilft Ihnen, mehr über Ihre verschiedenen Segmente zu erfahren und wie sie auf verschiedene Arten von Nachrichten reagieren. Warum Annahmen über Ihre Segmente treffen, wenn Sie Ihre Strategie auf Daten basieren können?

### Führen Sie einen Folgetest basierend auf Erkenntnissen aus einem früheren Test durch {#run-a-follow-up-test-based-on-insights-from-a-previous-test}

Nutzen Sie die Erkenntnisse, die Sie aus vergangenen Tests gewonnen haben, um Ihre zukünftigen Tests zu leiten. Deutet ein früherer Test darauf hin, dass eine Messaging-Technik effektiver ist? Sind Sie unsicher, welcher spezifische Aspekt einer Variante sie besser gemacht hat? Die Durchführung von Folgetests basierend auf diesen Fragen hilft Ihnen, aufschlussreiche Erkenntnisse über Ihre Nutzer:innen zu gewinnen.

### Vergleichen Sie die langfristige Wirkung verschiedener Varianten {#compare-the-long-term-impact-of-different-variants}

Wenn Sie A/B-Tests für Nachrichten zur erneuten Interaktion durchführen, vergessen Sie nicht, die langfristige Wirkung verschiedener Varianten mithilfe von [Retention Reports]({{site.baseurl}}/user_guide/analytics/reports/retention_reports) zu vergleichen. Sie können Retention Reports verwenden, um zu analysieren, wie jede Variante jedes gewünschte Nutzer:innen-Verhalten Tage, Wochen oder einen Monat nach Nachrichtenempfang beeinflusst hat, und um festzustellen, ob es einen Uplift gibt.