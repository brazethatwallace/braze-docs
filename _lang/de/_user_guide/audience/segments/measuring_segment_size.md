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

## Berechnung der Segmentzugehörigkeit {#segment-membership-calculation}

Braze aktualisiert die Segmentzugehörigkeit von Nutzer:innen, sobald Daten an unsere Server zurückgesendet und verarbeitet werden – in der Regel sofort. Die Segmentzugehörigkeit ändert sich erst, wenn die jeweilige Sitzung verarbeitet wurde. Beispielsweise wird ein:e Nutzer:in, der/die zu Beginn einer Sitzung in ein Segment für inaktive Nutzer:innen fällt, nach der Verarbeitung der Sitzung sofort aus diesem Segment entfernt.

### Berechnung der insgesamt erreichbaren Nutzer:innen {#total-reachable-users-calculation}

Jedes Segment zeigt die Gesamtzahl der Nutzer:innen an, die Mitglieder dieses Segments sind. Beim Filtern nach **Nutzer:innen aus allen Apps** werden außerdem einige der am häufigsten genutzten Messaging-Kanäle (wie Web-Push oder E-Mail) sowie die Anzahl der erreichbaren Nutzer:innen für diese spezifischen Kanäle angezeigt.

Es ist möglich, dass die Gesamtzahl der Nutzer:innen von der Anzahl der über die einzelnen Kanäle erreichbaren Nutzer:innen abweicht. Darüber hinaus werden nicht alle Kanäle in der Tabelle der erreichbaren Nutzer:innen aufgeführt. Beispielsweise werden Content Cards, Webhooks und WhatsApp nicht in der Aufschlüsselung angezeigt. Das bedeutet, dass die Gesamtzahl der erreichbaren Nutzer:innen größer sein kann als die Summe der Nutzer:innen für jeden angezeigten Kanal.

![Eine Tabelle, die die insgesamt erreichbaren Nutzer:innen aufgeschlüsselt nach per E-Mail, iOS-Push, Android-Push, Web-Push und Kindle-Push erreichbaren Nutzer:innen zeigt.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Damit ein:e Nutzer:in als über einen bestimmten Kanal erreichbar aufgeführt wird, muss er/sie beides haben:
* Eine gültige E-Mail-Adresse oder ein gültiges Push-Token, das mit dem Profil verknüpft ist, und
* Ein Opt-in oder Abo für Ihre App.

Ein:e einzelne:r Nutzer:in kann verschiedenen Gruppen erreichbarer Nutzer:innen angehören. Beispielsweise könnte ein:e Nutzer:in sowohl eine gültige E-Mail-Adresse als auch ein gültiges Android-Push-Token haben und für beides ein Opt-in erteilt haben, aber kein zugehöriges iOS-Push-Token besitzen. Die Differenz zwischen den insgesamt erreichbaren Nutzer:innen und der Summe der verschiedenen Kanäle ergibt die Anzahl der Nutzer:innen, die sich für das Segment qualifiziert haben, aber über diese Kommunikationskanäle nicht erreichbar sind.

{% alert note %}
**Insgesamt erreichbare Nutzer:innen** umfasst alle, die Ihren Segmentfiltern entsprechen, auch wenn sie einen Kanal nicht mehr abonniert haben. Kanalzeilen wie **iOS** zählen Nutzer:innen, die nur über diesen Kanal erreichbar sind, gemäß den Regeln unter [Erreichbare Nutzer:innen nach Kanal](#reachable-users-by-channel). Um Segmenttotale mit abonnierten Nutzer:innen abzugleichen, fügen Sie Filter wie **Push aktiviert für iOS** ist wahr (oder das Äquivalent für Ihren Kanal) hinzu.
{% endalert %}

## Statistiken zur Segmentgröße {#statistics-for-segment-size}

Geschätzte Statistiken werden durch Stichproben nur eines Teils Ihres Segments ermittelt, sodass Sie damit rechnen sollten, dass die geschätzten Größen über oder unter dem tatsächlichen Wert liegen. Bei größeren Workspaces können die Abweichungen potenziell größer ausfallen. Um eine genaue Anzahl der Nutzer:innen in Ihrem Segment zu erhalten, wählen Sie **Exakte Statistiken berechnen** aus. Die exakte Segmentzugehörigkeit wird immer berechnet, bevor ein Segment von einer Nachricht betroffen ist, die in einer Campaign oder einem Canvas gesendet wird.

Braze stellt die folgenden Statistiken zur Segmentgröße bereit.

### Filterstatistiken {#filter-statistics}

Für jede Filtergruppe können Sie die geschätzte Anzahl erreichbarer Nutzer:innen einsehen. Wählen Sie **Expand extra funnel statistics** aus, um eine Aufschlüsselung nach Kanälen zu sehen.

![Eine Filtergruppe mit einem Filter für Nutzer:innen, die genau eine Sitzung hatten.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Schätzung der erreichbaren Nutzer:innen {#reachable-users-estimate}

Sie können die geschätzte Anzahl erreichbarer Nutzer:innen eines gesamten Segments, einschließlich der geschätzten Nutzer:innenzahlen pro Kanal, im Seitenpanel **Erreichbare Nutzer:innen** einsehen. Diese Schätzung zeigt Ihnen einen ungefähren Bereich für Ihre Segmentgröße sowie eine Schätzung, welcher Prozentsatz Ihrer gesamten Nutzerbasis in dieses Segment fällt. Beachten Sie, dass geschätzte Statistiken 15 Minuten lang zwischengespeichert werden, es sei denn, Sie nehmen Änderungen an Ihrem Segment vor – in diesem Fall werden die geschätzten Statistiken automatisch aktualisiert. Sie können auch eine exakte Anzahl erreichbarer Nutzer:innen (sowohl für das gesamte Segment als auch pro Kanal) anzeigen, indem Sie **Exakte Statistiken berechnen** auswählen.

{% alert note %}
Workspaces mit mehr als 50.000 Nutzer:innen zeigen **Geschätzte Nutzer:innen** an; kleinere Workspaces zeigen **Exakte Nutzer:innen** an.
{% endalert %}

![Das Panel „Erreichbare Nutzer:innen“ mit der Angabe, dass es 2,3 Mio.–2,4 Mio. geschätzte Nutzer:innen gibt.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Hinweise zu geschätzten Zahlen {#considerations-for-estimate-counts}

Braze ermittelt die Anzahl der geschätzten Nutzer:innen, indem eine Teilmenge Ihrer Nutzer:innen abgefragt und die Ergebnisse auf Ihre gesamte Zielgruppe hochgerechnet werden. Da die Teilmenge der Nutzer:innen, die Braze abfragt, bei jeder Berechnung dieser Schätzung unterschiedlich sein kann, kann sich die Schätzung auch in Fällen ändern, in denen die Zugehörigkeit zu Ihrer Zielgruppe technisch gleich geblieben sein sollte. Wenn Sie beispielsweise Ihre Filter neu anordnen oder dasselbe Segment zu einem anderen Zeitpunkt erneut prüfen, ist es möglich, dass sich die geschätzte Anzahl ändert (obwohl **Exakte Statistiken berechnen** dieselben Ergebnisse liefern würde, wenn sich Ihr Segment nicht geändert hat).

Wenn Sie eine große Nutzerpopulation in Ihrem Workspace haben, können Sie größere Abweichungen zwischen Ihren geschätzten und Ihren exakt berechneten Zahlen feststellen, insbesondere wenn Ihr Segment einen sehr kleinen Prozentsatz Ihrer gesamten Workspace-Population ausmacht. Dies liegt daran, dass Braze die Schätzung durch Abfrage einer Teilmenge Ihrer Nutzer:innen ermittelt und die Ergebnisse auf Ihre gesamte Nutzerbasis hochrechnet. Bei größeren Nutzergruppen sind größere Unterschiede zwischen geschätzten und exakten Zahlen zu erwarten.

Sehr kleine Segmente haben einen geschätzten Bereich, der 0 einschließt, was bedeutet, dass der Prozentsatz der Gesamtnutzer:innen auf 0 gerundet werden kann. In diesen Fällen hilft Ihnen **Exakte Statistiken berechnen**, eine genaue Anzahl Ihrer Segmentgröße zu sehen, die tatsächlich nicht 0 sein muss.

![Das Seitenpanel „Erreichbare Nutzer:innen“ mit einer exakten Nutzer:innenzahl von „31“.]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Erreichbare Nutzer:innen nach Kanal {#reachable-users-by-channel}

Um die Anzahl der Nutzer:innen anzuzeigen, die über jeden Messaging-Kanal erreichbar sind, wählen Sie **Aufschlüsselung anzeigen** im Panel **Erreichbare Nutzer:innen**. Dies zeigt einige der am häufigsten verwendeten Messaging-Kanäle (wie Web-Push oder E-Mail) und die Anzahl der erreichbaren Nutzer:innen für diese spezifischen Kanäle an.

Die Kennzahl _Gesamt_ stellt eindeutige Nutzer:innen dar. Wenn beispielsweise eine Nutzerin oder ein Nutzer sowohl Android-Push als auch iOS-Push hat, wird sie oder er in beiden Zeilen gezählt, zählt aber nur als 1 Nutzer:in in der Zeile _Gesamt_.

Es ist jedoch möglich, dass die Gesamtzahl der Nutzer:innen von der Summe der über jeden Kanal erreichbaren Nutzer:innen abweicht, da eine einzelne Nutzerin oder ein einzelner Nutzer zu verschiedenen Gruppen erreichbarer Nutzer:innen gehören kann. Beispielsweise könnte eine Nutzerin oder ein Nutzer sowohl eine gültige E-Mail-Adresse als auch ein gültiges Android-Push-Token haben und für beides angemeldet sein, aber kein zugehöriges iOS-Push-Token besitzen.

Beachten Sie, dass nicht alle Kanäle in der Tabelle **Erreichbare Nutzer:innen** aufgeführt sind (wie Content Cards, Webhooks und WhatsApp). Wenn Sie beispielsweise Nutzer:innen haben, die nur über WhatsApp erreichbar sind, werden diese in _Gesamt_ berücksichtigt, aber nicht in den kanalspezifischen Zeilen. Das bedeutet, dass die Gesamtzahl der erreichbaren Nutzer:innen von der Summe der Nutzer:innen für jeden angezeigten Kanal abweichen kann.

In Fällen, in denen _Gesamt_ höher ist als die Summe der Kanäle, stellt die Differenz die Anzahl der Nutzer:innen dar, die sich für das Segment qualifiziert haben, aber über diese Kommunikationskanäle nicht erreichbar sind.

Damit Nutzer:innen als über einen bestimmten Kanal erreichbar aufgeführt werden, müssen sie:
- Eine gültige E-Mail-Adresse oder ein gültiges Push-Token haben, das mit ihrem Profil verknüpft ist, und
- Sich für Ihre App angemeldet oder ein Abo abgeschlossen haben.

#### Angewendete Filter für kanalspezifisch erreichbare Nutzer:innen {#applied-filters-for-channel-specific-reachable-users}

Die folgenden Filter werden für jeden Kanal bei der Ermittlung erreichbarer Nutzer:innen angewendet.

| Kanal | Filter |
| --- | --- |
| E-Mail | **Email Available** ist wahr. |
| Push | **Foreground Push Enabled** ist wahr. |
| SMS | **Subscription Group** ist eine beliebige SMS-Abo-Gruppe. **Invalid Phone Number** ist falsch. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angewendete Filter für kanalspezifisch erreichbare Nutzer:innen" }

## Exakte Statistiken berechnen {#calculating-exact-statistics}

Um eine genaue Anzahl der Nutzer:innen in Ihrem Segment anzuzeigen, wählen Sie **Exakte Statistiken berechnen** im Bereich **Erreichbare Nutzer:innen** aus.

Um die Statistiken für eine zuvor durchgeführte Berechnung zu aktualisieren, wählen Sie **Exakte Statistiken aktualisieren**. Das Datum der letzten Berechnung wird automatisch aktualisiert.

Beachten Sie, dass die Genauigkeit einer Berechnung nur bei 99,999 % oder höher liegt. Bei großen Segmenten können daher leichte Abweichungen auftreten – auch bei der Berechnung exakter Statistiken –, was ein normales Verhalten ist. Darüber hinaus werden die Ergebnisse exakter Statistiken 24 Stunden lang zwischengespeichert, es sei denn, Sie nehmen Änderungen an Ihrem Segment vor. In diesem Fall können Sie die exakten Statistiken erneut berechnen.

{% alert note %}
Segmente, die gleichmäßig nach [zufälligen Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) aufgeteilt werden, haben nicht dieselbe Größe. Wenn Sie beispielsweise ein Segment mit dem Filter **Zufällige Bucket-Nr. kleiner als 5000** und ein Segment mit dem Filter **Zufällige Bucket-Nr. mindestens 5000** erstellen, ist es möglich und zu erwarten, dass die Segmentgrößen um bis zu einige Prozentpunkte variieren. Dies liegt an Situationen wie dem Löschen inaktiver Nutzer:innen und nicht erreichbaren Nutzer:innen.
{% endalert %}

![Screenshot des Bereichs „Erreichbare Nutzer:innen“ mit exakten Statistiken und einem aufgeklappten Aufschlüsselungsmenü.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Die Statistiken auf Filterebene sind immer geschätzt, auch wenn Sie exakte Statistiken berechnen. **Exakte Statistiken berechnen** berechnet die exakten Statistiken nur auf Segmentebene, nicht auf Filter- oder Filtergruppenebene. Diese Berechnung kann einige Minuten dauern. Insbesondere bei größeren Workspaces kann die Berechnung längere Zeit in Anspruch nehmen. Sie können den Fortschritt über die Fortschrittsanzeige im Bereich **Erreichbare Nutzer:innen** verfolgen. Wenn eine Berechnung voraussichtlich länger als fünf Minuten dauert, sendet Braze Ihnen die Ergebnisse per E-Mail.

Braze priorisiert jeweils eine Berechnung pro Workspace, sodass das gleichzeitige Ausführen mehrerer Berechnungen zu Verzögerungen führt. Sie können **Berechnungswarteschlange anzeigen** auswählen, um zu sehen, welche Segmente vor Ihrem liegen, deren Fortschritt und Initiator:in, und um eine Vorstellung davon zu bekommen, wann Ihre Berechnung priorisiert werden könnte.

![Eine Berechnungswarteschlange mit einer Berechnung.]({% image_buster /assets/img_archive/calculation_queue.png %})

Sie können eine Berechnung exakter Statistiken abbrechen, indem Sie **Abbrechen** auswählen. Dies kann nützlich sein, wenn sich mehrere Berechnungen in der Warteschlange befinden und Sie eine andere Berechnung zuerst priorisieren möchten.

## Historische Segmentmitgliedschaft anzeigen {#viewing-historical-segment-membership-size}

Für alle Segmente können Sie ein historisches Mitgliedschafts-Chart anzeigen, das die geschätzte Segmentmitgliedschaft für jeden Tag zeigt. Dieses Chart zeigt, wie sich die Größe Ihres Segments im Laufe der Zeit verändert hat. Verwenden Sie das Dropdown-Menü, um die Segmentmitgliedschaft nach Datumsbereich zu filtern.

![Verwenden Sie das Dropdown-Menü „Historische Mitgliedschaft“, um die Segmentmitgliedschaft nach Datumsbereich zu filtern.]({% image_buster /assets/img_archive/historical_membership2.png %})

Da dieses Chart Ihnen einen Überblick über die allgemeinen Trends der Segmentmitgliedschaft geben soll, ist die tägliche Anzahl eine Schätzung – ähnlich wie die Segmentgröße eine Schätzung ist, bevor Sie **Exakte Statistiken berechnen** auswählen. Und da dieses Diagramm Schätzungen zeigt, ist es möglich, dass die Größe Ihres Segments in diesem Chart als „0“ angezeigt wird, obwohl die tatsächliche Größe (die nach Auswahl von **Exakte Statistiken berechnen** ermittelt werden kann) nicht „0“ ist. Es ist besonders wahrscheinlich, dass das Chart eine Schätzung von „0“ anzeigt, wenn Ihr Segment im Verhältnis zur Gesamtpopulation Ihres Workspace sehr klein ist.

Nehmen wir zum Beispiel an, Ihr Workspace enthält 100 Millionen Nutzer:innen und Ihr Segment umfasst etwa 700 Nutzer:innen. Es ist möglich, dass an manchen Tagen keine Nutzer:innen im Segment sind und keine Nutzer:innen in den zufälligen Bucket-Bereich fallen, der für die historische Mitgliedschaftsschätzung verwendet wird, was zu einer Tagesmitgliedschaft von 0 führt.

Braze schätzt die Segmentmitgliedschaft, indem eine Teilmenge Ihrer Nutzer:innen abgefragt und die Ergebnisse dann auf Ihre gesamte Zielgruppe hochgerechnet werden. Das bedeutet, dass die Ergebnisse des Charts nur eine Schätzung der möglichen Segmentmitgliedschaft an diesem Tag liefern und dass die Werte von Tag zu Tag schwanken können, da jeden Tag eine andere Stichprobe von Nutzer:innen für diese Schätzung abgefragt werden kann.

{% alert note %}
Alle Schätzungen können um etwa 1 % der Gesamtpopulation Ihres Workspace nach oben oder unten abweichen. Größere Workspaces mit mehr Nutzer:innen haben mit höherer Wahrscheinlichkeit Schätzungen, die numerisch stärker von exakten Berechnungen abweichen können, auch wenn die Differenz weiterhin 1 % der Nutzerpopulation des Workspace beträgt. Das bedeutet, dass größere Abweichungen zwischen Schätzungen und exakten Zahlen bei großen Workspaces zu erwarten sind.
{% endalert %}

### Gründe für signifikante Änderungen {#reasons-for-significant-changes}

Die Mitgliedschaftsanzahl kann sich aus verschiedenen Gründen erheblich ändern, wie in dieser Tabelle dargestellt.

| Grund | Beispiel |
| --- | --- |
| Normales Nutzer:innenverhalten | Nutzer:innen abonnieren nach einer besonders erfolgreichen Campaign. |
| Nutzer:innen werden per CSV importiert | Eine CSV-Datei mit Nutzer:innen wurde importiert, die die Segmentmitgliedschaft erheblich erhöht hat. |
| Segmentzielgruppen-Kriterien werden geändert | Die Zielgruppenregeln eines bestehenden Segments (z. B. Filter) wurden geändert, was zu signifikanten Änderungen der Segmentmitgliedschaft führte. |
| Nutzer:innen werden gelöscht | Eine erhebliche Anzahl von Nutzer:innen wurde gelöscht. |
| Eine Partnerintegration wurde mit Braze synchronisiert | Ein Drittanbieter hat Daten an Braze gesendet, die die Segmentmitgliedschaft erheblich beeinflusst haben. |
| Inaktive Nutzer:innen werden archiviert | Eine erhebliche Anzahl inaktiver Profile wurde archiviert. Zum Beispiel wurde eine große Anzahl per CSV importierter Nutzer:innen, die nie Aktivität verzeichnet haben, gleichzeitig archiviert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gründe für signifikante Änderungen" }