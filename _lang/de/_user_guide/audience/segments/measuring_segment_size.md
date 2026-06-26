---
nav_title: Segmentgröße messen
article_title: Segmentgröße messen
page_order: 5
page_type: reference
tool:
- Segments
description: "Diese Seite beschreibt, wie Sie die Mitgliedschaft und Größe Ihres Segments überwachen können."
---

# Segmentgröße messen {#measure-segment-size}

> Diese Seite beschreibt, wie Sie die Mitgliedschaft und Größe Ihres Segments überwachen können.

## Berechnung der Segmentmitgliedschaft {#segment-membership-calculation}

Braze aktualisiert die Segmentmitgliedschaft von Nutzer:innen, sobald Daten an unsere Server zurückgesendet und verarbeitet werden – in der Regel sofort. Die Segmentmitgliedschaft einer/eines Nutzer:in ändert sich erst, wenn die jeweilige Sitzung verarbeitet wurde. Beispielsweise wird eine/ein Nutzer:in, die/der zu Beginn einer Sitzung in ein Segment für inaktive Nutzer:innen fällt, sofort aus diesem Segment entfernt, sobald die Sitzung verarbeitet ist.

### Berechnung der insgesamt erreichbaren Nutzer:innen {#total-reachable-users-calculation}

Jedes Segment zeigt die Gesamtzahl der Nutzer:innen an, die Mitglieder dieses Segments sind. Wenn Sie nach **Nutzer:innen aus allen Apps** filtern, werden zusätzlich einige der am häufigsten genutzten Messaging-Kanäle (wie Web-Push oder E-Mail) sowie die Anzahl der erreichbaren Nutzer:innen für diese spezifischen Kanäle angezeigt.

Es ist möglich, dass die Gesamtzahl der Nutzer:innen von der Anzahl der über jeden einzelnen Kanal erreichbaren Nutzer:innen abweicht. Außerdem werden nicht alle Kanäle in der Tabelle der erreichbaren Nutzer:innen aufgeführt. Beispielsweise werden Content Cards, Webhooks und WhatsApp nicht in der Aufschlüsselung angezeigt. Das bedeutet, dass die Gesamtzahl der erreichbaren Nutzer:innen größer sein kann als die Summe der Nutzer:innen für jeden angezeigten Kanal.

![Eine Tabelle, die die insgesamt erreichbaren Nutzer:innen aufgeschlüsselt nach E-Mail, iOS-Push, Android-Push, Web-Push und Kindle-Push zeigt.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Damit Nutzer:innen als über einen bestimmten Kanal erreichbar aufgeführt werden, müssen sie beides haben:
* Eine gültige E-Mail-Adresse oder ein gültiges Push-Token, das mit ihrem Profil verknüpft ist, und
* Ein Opt-in oder Abo für Ihre App.

Einzelne Nutzer:innen können zu verschiedenen Gruppen erreichbarer Nutzer:innen gehören. Beispielsweise könnte eine/ein Nutzer:in sowohl eine gültige E-Mail-Adresse als auch ein gültiges Android-Push-Token haben und für beides ein Opt-in erteilt haben, aber kein zugehöriges iOS-Push-Token besitzen. Die Differenz zwischen den insgesamt erreichbaren Nutzer:innen und der Summe der verschiedenen Kanäle entspricht der Anzahl der Nutzer:innen, die sich für das Segment qualifiziert haben, aber über diese Kommunikationskanäle nicht erreichbar sind.

{% alert note %}
**Insgesamt erreichbare Nutzer:innen** umfasst alle, die Ihren Segmentfiltern entsprechen, auch wenn sie einen Kanal nicht mehr abonniert haben. Kanalzeilen wie **iOS** zählen Nutzer:innen, die nur über diesen Kanal erreichbar sind, gemäß den Regeln unter [Erreichbare Nutzer:innen nach Kanal](#reachable-users-by-channel). Um die Segmenttotale mit abonnierten Nutzer:innen abzugleichen, fügen Sie Filter wie **Push enabled for iOS** ist wahr (oder das Äquivalent für Ihren Kanal) hinzu.
{% endalert %}

## Statistiken zur Segmentgröße {#statistics-for-segment-size}

Geschätzte Statistiken werden durch Stichproben nur eines Teils Ihres Segments approximiert. Sie sollten daher damit rechnen, dass geschätzte Größen größer oder kleiner als der tatsächliche Wert ausfallen, wobei größere Workspaces potenziell größere Fehlerspannen aufweisen können. Um eine genaue Anzahl der Nutzer:innen in Ihrem Segment zu erhalten, wählen Sie **Calculate Exact Statistics**. Die exakte Segmentmitgliedschaft wird immer berechnet, bevor ein Segment von einer Nachricht betroffen ist, die in einer Kampagne oder einem Canvas gesendet wird.

Braze stellt die folgenden Statistiken zur Segmentgröße bereit.

### Filterstatistiken {#filter-statistics}

Für jede Filtergruppe können Sie die geschätzten erreichbaren Nutzer:innen einsehen. Wählen Sie **Expand extra funnel statistics**, um eine Aufschlüsselung nach Kanälen zu sehen.

![Eine Filtergruppe mit einem Filter für Nutzer:innen, die genau eine Sitzung hatten.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Schätzung der erreichbaren Nutzer:innen {#reachable-users-estimate}

Sie können die geschätzten erreichbaren Nutzer:innen eines gesamten Segments, einschließlich geschätzter Nutzer:innenzahlen pro Kanal, im Seitenpanel **Reachable users** einsehen. Diese **Schätzung** zeigt Ihnen einen ungefähren Bereich für Ihre Segmentgröße sowie eine Schätzung, welcher Prozentsatz Ihrer gesamten Nutzerbasis in dieses Segment fällt. Beachten Sie, dass geschätzte Statistiken 15 Minuten lang zwischengespeichert werden, es sei denn, Sie nehmen Änderungen an Ihrem Segment vor – in diesem Fall werden die geschätzten Statistiken automatisch aktualisiert. Sie können auch eine exakte Anzahl der erreichbaren Nutzer:innen (sowohl für das gesamte Segment als auch pro Kanal) einsehen, indem Sie **Calculate exact statistics** auswählen.

![Das Panel „Reachable users“ mit der Angabe, dass es 2,3 Mio.–2,4 Mio. geschätzte Nutzer:innen gibt.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Hinweise zu geschätzten Zahlen {#considerations-for-estimate-counts}

Braze ermittelt die Anzahl der geschätzten Nutzer:innen, indem eine Teilmenge Ihrer Nutzer:innen abgefragt und die Ergebnisse auf Ihre gesamte Zielgruppe hochgerechnet werden. Da die Teilmenge der Nutzer:innen, die Braze abfragt, bei jeder Berechnung dieser Schätzung unterschiedlich sein kann, kann sich die Schätzung auch in Fällen ändern, in denen sich Ihre Zielgruppenmitgliedschaft technisch nicht geändert haben sollte. Wenn Sie beispielsweise Ihre Filter neu anordnen oder dasselbe Segment zu einem anderen Zeitpunkt erneut prüfen, ist es möglich, dass sich die geschätzte Anzahl ändert (obwohl **Calculate exact stats** dieselben Ergebnisse liefern würde, wenn sich Ihr Segment nicht geändert hat).

Wenn Sie eine große Nutzerpopulation in Ihrem Workspace haben, können Sie größere Abweichungen zwischen Ihren geschätzten und exakten Berechnungswerten feststellen, insbesondere wenn Ihr Segment einen sehr kleinen Prozentsatz Ihrer gesamten Workspace-Population ausmacht. Dies liegt daran, dass Braze die Schätzung durch Abfrage einer Teilmenge Ihrer Nutzer:innen und Hochrechnung der Ergebnisse auf Ihre gesamte Nutzerbasis ermittelt. Bei größeren Nutzergruppen sind größere Unterschiede zwischen geschätzten und exakten Zahlen zu erwarten.

Sehr kleine Segmente haben einen geschätzten Bereich, der 0 einschließt, was bedeutet, dass der Prozentsatz der Gesamtnutzer:innen auf 0 gerundet werden kann. In diesen Fällen hilft Ihnen **Calculate exact stats**, eine genaue Anzahl Ihrer Segmentgröße zu sehen, die tatsächlich nicht 0 sein muss.

![Das Seitenpanel „Reachable users“ mit einer exakten Nutzer:innenzahl von „31“.]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Erreichbare Nutzer:innen nach Kanal {#reachable-users-by-channel}

Um die Anzahl der Nutzer:innen einzusehen, die über jeden Messaging-Kanal erreichbar sind, wählen Sie **Show breakdown** im Panel **Reachable users**. Dies zeigt einige der am häufigsten genutzten Messaging-Kanäle (wie Web-Push oder E-Mail) sowie die Anzahl der erreichbaren Nutzer:innen für diese spezifischen Kanäle an.

Die Metrik _Gesamt_ stellt eindeutige Nutzer:innen dar. Wenn beispielsweise eine/ein Nutzer:in sowohl Android-Push als auch iOS-Push hat, wird sie/er für beide Zeilen gezählt, aber nur als 1 Nutzer:in in der Zeile _Gesamt_.

Es ist jedoch möglich, dass die Gesamtzahl der Nutzer:innen von der Summe der über jeden Kanal erreichbaren Nutzer:innen abweicht, da einzelne Nutzer:innen zu verschiedenen Gruppen erreichbarer Nutzer:innen gehören können. Beispielsweise könnte eine/ein Nutzer:in sowohl eine gültige E-Mail-Adresse als auch ein gültiges Android-Push-Token haben und für beides ein Opt-in erteilt haben, aber kein zugehöriges iOS-Push-Token besitzen.

Beachten Sie, dass nicht alle Kanäle in der Tabelle **Reachable users** aufgeführt sind (wie Content Cards, Webhooks und WhatsApp). Wenn Sie beispielsweise Nutzer:innen haben, die nur über WhatsApp erreichbar sind, werden sie in der Zeile _Gesamt_ berücksichtigt, aber nicht in den kanalspezifischen Zeilen. Das bedeutet, dass die Gesamtzahl der erreichbaren Nutzer:innen von der Summe der Nutzer:innen für jeden angezeigten Kanal abweichen kann.

In Fällen, in denen die Zeile _Gesamt_ höher ist als die Summe der Kanäle, stellt die Differenz die Anzahl der Nutzer:innen dar, die sich für das Segment qualifiziert haben, aber über diese Kommunikationskanäle nicht erreichbar sind.

Damit Nutzer:innen als über einen bestimmten Kanal erreichbar aufgeführt werden, müssen sie Folgendes haben:
- Eine gültige E-Mail-Adresse oder ein gültiges Push-Token, das mit ihrem Profil verknüpft ist, und
- Ein Opt-in oder Abo für Ihre App.

#### Angewendete Filter für kanalspezifische erreichbare Nutzer:innen {#applied-filters-for-channel-specific-reachable-users}

Die folgenden Filter werden für jeden Kanal bei der Ermittlung der erreichbaren Nutzer:innen angewendet.

| Kanal | Filter |
| --- | --- |
| E-Mail | **Email Available** ist wahr. |
| Push | **Foreground Push Enabled** ist wahr. |
| SMS | **Subscription Group** ist eine beliebige SMS-Abo-Gruppe. **Invalid Phone Number** ist falsch. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angewendete Filter für kanalspezifische erreichbare Nutzer:innen" }

## Exakte Statistiken berechnen {#calculating-exact-statistics}

Um eine genaue Anzahl der Nutzer:innen in Ihrem Segment einzusehen, wählen Sie **Calculate exact stats** im Panel **Reachable users**.

Um die Statistiken einer zuvor durchgeführten Berechnung zu aktualisieren, wählen Sie **Refresh exact statistics**. Das Datum der letzten Berechnung wird automatisch aktualisiert.

Beachten Sie, dass die Genauigkeit einer Berechnung nur 99,999 % oder höher beträgt. Bei großen Segmenten können Sie daher leichte Abweichungen feststellen&#8212;auch bei der Berechnung exakter Statistiken&#8212;, was ein normales Verhalten ist. Darüber hinaus werden Ergebnisse exakter Statistiken 24 Stunden lang zwischengespeichert, es sei denn, Sie nehmen Änderungen an Ihrem Segment vor – in diesem Fall können Sie die exakten Statistiken erneut berechnen.

{% alert note %}
Segmente, die gleichmäßig durch [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) aufgeteilt werden, haben nicht dieselbe Größe. Wenn Sie beispielsweise ein Segment mit dem Filter **Random Bucket # less than 5000** und ein Segment mit dem Filter **Random Bucket # at least 5000** erstellen, ist es möglich und zu erwarten, dass die Segmentgrößen um bis zu einige Prozentpunkte variieren. Dies liegt an Situationen wie dem Löschen inaktiver Nutzer:innen und der Nichterreichbarkeit von Nutzer:innen.
{% endalert %}

![Screenshot des Panels „Reachable users“ mit exakten Statistiken und einem erweiterten Aufschlüsselungsmenü.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Die Statistiken auf Filterebene sind immer geschätzt, auch wenn Sie exakte Statistiken berechnen. **Calculate exact stats** berechnet die exakten Statistiken nur auf Segmentebene, nicht auf Filter- oder Filtergruppenebene. Diese Berechnung kann einige Minuten dauern. Insbesondere größere Workspaces können längere Zeiträume für die Berechnung benötigen. Sie können Ihren Fortschritt über den Fortschrittsbalken im Panel **Reachable users** verfolgen. Wenn eine Berechnung voraussichtlich mehr als fünf Minuten dauert, sendet Braze Ihnen die Ergebnisse per E-Mail.

Braze priorisiert jeweils eine Berechnung pro Workspace, sodass das gleichzeitige Ausführen mehrerer Berechnungen zu Verzögerungen führt. Sie können **View calculation queue** auswählen, um zu sehen, welche Segmente vor Ihrem stehen, deren Fortschritt und Initiator:in, und eine Vorstellung davon zu bekommen, wann Ihre Berechnung priorisiert werden könnte.

![Eine Berechnungswarteschlange mit einer Berechnung.]({% image_buster /assets/img_archive/calculation_queue.png %})

Sie können eine Berechnung exakter Statistiken abbrechen, indem Sie **Cancel** auswählen. Dies kann vorteilhaft sein, wenn sich mehrere Berechnungen in der Warteschlange befinden und Sie eine andere Berechnung zuerst priorisieren möchten.


## Historische Segmentmitgliedschaftsgröße anzeigen {#viewing-historical-segment-membership-size}

Für alle Segmente können Sie ein historisches Mitgliedschaftsdiagramm einsehen, das die geschätzte Segmentmitgliedschaft für jeden Tag zeigt. Dieses Diagramm zeigt, wie sich die Größe Ihres Segments im Laufe der Zeit verändert hat. Verwenden Sie das Dropdown-Menü, um die Segmentmitgliedschaft nach Datumsbereich zu filtern.

![Verwenden Sie das Dropdown-Menü „Historical Membership“, um die Segmentmitgliedschaft nach Datumsbereich zu filtern.]({% image_buster /assets/img_archive/historical_membership2.png %})

Da das Ziel dieses Diagramms darin besteht, Ihnen einen Überblick über die allgemeinen Trends der Segmentmitgliedschaft zu geben, ist die tägliche Anzahl eine Schätzung – ähnlich wie die Segmentgröße eine Schätzung ist, bevor Sie **Calculate Exact Statistics** auswählen. Und da dieses Diagramm Schätzungen zeigt, ist es möglich, dass die Größe Ihres Segments in diesem Diagramm als „0“ erscheint, obwohl die tatsächliche Größe (die nach Auswahl von **Calculate Exact Stats** ermittelt werden kann) nicht „0“ ist. Es ist besonders wahrscheinlich, dass das Diagramm eine Schätzung von „0“ zeigt, wenn Ihr Segment im Verhältnis zur Größe Ihrer Workspace-Population sehr klein ist.

Nehmen wir beispielsweise an, Ihr Workspace enthält 100 Millionen Nutzer:innen und Ihr Segment hat etwa 700 Nutzer:innen. Es ist möglich, dass an manchen Tagen keine Nutzer:innen im Segment sind und keine Nutzer:innen in den zufälligen Bucket-Bereich fallen, der für die historische Mitgliedschaftsschätzung verwendet wird, was zu einer Tagesmitgliedschaftszahl von 0 führt.

Braze schätzt die Segmentmitgliedschaftszahl, indem eine Teilmenge Ihrer Nutzer:innen abgefragt und die Ergebnisse auf Ihre gesamte Zielgruppe hochgerechnet werden. Das bedeutet, dass die Ergebnisse des Diagramms nur eine Schätzung dessen liefern, wie die Segmentmitgliedschaft an diesem Tag aussehen könnte, und es ist zu erwarten, dass sie von Tag zu Tag schwanken, da täglich eine andere Stichprobe von Nutzer:innen für diese Schätzung abgefragt werden kann.

{% alert note %}
Alle Schätzungen können um etwa 1 % der gesamten Populationsgröße Ihres Workspaces höher oder niedriger als der angezeigte Wert sein. Größere Workspaces mit mehr Nutzer:innen haben mit höherer Wahrscheinlichkeit Schätzungen, die von exakten Berechnungen um einen höheren numerischen Betrag abweichen können, auch wenn die Differenz weiterhin 1 % der Nutzerpopulation des Workspaces beträgt. Das bedeutet, dass größere Unterschiede zwischen Schätzungen und exakten Zahlen bei großen Workspaces zu erwarten sind.
{% endalert %}

### Gründe für signifikante Änderungen {#reasons-for-significant-changes}

Die Mitgliedschaftszahl kann sich aus verschiedenen Gründen signifikant ändern, wie in dieser Tabelle aufgeführt.

| Grund | Beispiel |
| --- | --- |
| Normales Nutzer:innenverhalten | Nutzer:innen abonnieren nach einer besonders erfolgreichen Kampagne. |
| Nutzer:innen werden per CSV importiert | Eine CSV-Datei mit Nutzer:innen wurde importiert, die die Segmentmitgliedschaft erheblich erhöht hat. |
| Segmentzielgruppenkriterien werden geändert | Die Zielgruppenregeln eines bestehenden Segments (wie Filter) wurden geändert, was zu signifikanten Änderungen der Segmentmitgliedschaft führt. |
| Nutzer:innen werden gelöscht | Eine erhebliche Anzahl von Nutzer:innen wurde gelöscht. |
| Eine Partnerintegration hat sich mit Braze synchronisiert | Ein Drittanbieter hat Daten an Braze gesendet, die die Segmentmitgliedschaft erheblich beeinflusst haben. |
| Inaktive Nutzer:innen werden archiviert | Eine erhebliche Anzahl inaktiver Profile wurde archiviert. Beispielsweise wird eine große Anzahl per CSV importierter Nutzer:innen, die nie Aktivität protokollieren, gleichzeitig archiviert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gründe für signifikante Änderungen" }