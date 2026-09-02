---
nav_title: Globale Kontrollgruppe
article_title: Globale Kontrollgruppe
alias: /global_control_group/
page_order: 6
page_type: reference
description: "Erfahren Sie, wie Sie die globale Kontrollgruppe einrichten und verwenden, um die Gesamtwirkung Ihrer Messaging-Maßnahmen im Zeitverlauf zu messen."
tool:
  - Reports
search_rank: 1
toc_headers: h2

---

# Globale Kontrollgruppe {#global-control-group}

> Verwenden Sie die globale Kontrollgruppe, um einen Prozentsatz aller Nutzer:innen festzulegen, die keine Campaigns oder Canvases erhalten sollen. So können Sie die Gesamtwirkung Ihrer Messaging-Maßnahmen im Zeitverlauf analysieren.

Indem Sie das Verhalten von Nutzer:innen, die Nachrichten erhalten, mit dem Verhalten derjenigen vergleichen, die keine erhalten, können Sie besser nachvollziehen, wie Ihre Marketing-Kampagnen und Canvases zu einer Steigerung von Sitzungen und angepassten Events beitragen.

## So funktioniert die globale Kontrollgruppe {#how-the-global-control-group-works}

Mit der globalen Kontrollgruppe können Sie einen Prozentsatz aller Nutzer:innen als Kontrollgruppe festlegen. Nach dem Speichern erhalten die Nutzer:innen in der Gruppe keine Campaigns oder Canvases.

{% alert important %}
Ihre globale Kontrollgruppe gilt für alle Kanäle, Campaigns und Canvases, mit Ausnahme von [API-Campaigns]({{site.baseurl}}/api/api_campaigns). Das bedeutet, dass Nutzer:innen in Ihrer Kontrollgruppe weiterhin API-Campaigns erhalten. Diese Ausnahme gilt jedoch nicht für Content Cards. Wenn Sie eine API-getriggerte Content-Card-Kampagne verwenden, erhalten Nutzer:innen in Ihrer Kontrollgruppe diese nicht.
{% endalert %}

### Nutzer:innen zufällig der globalen Kontrollgruppe zuweisen {#assign-users-randomly-to-the-global-control-group}

Braze wählt zufällig mehrere Bereiche von [zufälligen Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers#create-segments-using-random-bucket-numbers) aus und nimmt Nutzer:innen aus diesen ausgewählten Buckets auf. Wenn Sie derzeit zufällige Bucket-Nummern für andere Zwecke verwenden, lesen Sie den Abschnitt [Worauf Sie achten sollten](#things-to-watch-for).

Wenn Ihre globale Kontrollgruppe generiert wird, gehören alle Nutzer:innen mit zufälligen Bucket-Nummern zur Gruppe. Darüber hinaus werden auch neue Nutzer:innen, die nach diesem Zeitpunkt hinzukommen (also nach der Generierung der globalen Kontrollgruppe gewonnen wurden) und diese zufälligen Bucket-Nummern haben, ebenfalls der globalen Kontrollgruppe hinzugefügt. Ebenso können Sie erwarten, dass die Größe Ihrer globalen Kontrollgruppe schrumpft, wenn viele Nutzer:innen gelöscht werden, da ein Prozentsatz dieser gelöschten Nutzer:innen in diese Gruppe gefallen ist. Dadurch bleibt die Größe Ihrer Gruppe als konstanter Prozentsatz relativ zu Ihrer gesamten Nutzerbasis erhalten.

### Nutzer:innen zufällig der Treatment-Gruppe für das Reporting zuweisen {#assign-users-randomly-to-the-treatment-group-for-reporting}

Braze erstellt außerdem eine Treatment-Gruppe für das Reporting zum Uplift. Die Treatment-Gruppe ist eine zufällig ausgewählte Gruppe von Nutzer:innen, die nicht Teil Ihrer globalen Kontrollgruppe ist, und wird mit derselben Methode der zufälligen Bucket-Nummern wie die globale Kontrollgruppe generiert.

Ihre Treatment-Gruppe ist in der Größe ähnlich wie Ihre globale Kontrollgruppe, aber es ist unwahrscheinlich, dass sie exakt die gleiche Größe hat. Für das [Reporting](#reporting) misst Braze das Verhalten der Nutzer:innen in Ihrer Kontrollgruppe und der Nutzer:innen in Ihrer Treatment-Stichprobe. Jeder Workspace hat maximal eine globale Kontrollgruppe und eine Treatment-Stichprobengruppe. Die Treatment-Stichprobengruppe ist dieselbe Gruppe von Nutzer:innen, unabhängig davon, wie Sie Ihr Reporting für die globale Kontrollgruppe konfigurieren.

### Nutzer:innen von Feature-Flags ausschließen {#exclude-users-from-feature-flags}

Sie können [Feature-Flags]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) für Nutzer:innen in Ihrer globalen Kontrollgruppe nicht aktivieren. Das bedeutet, dass Nutzer:innen in Ihrer globalen Kontrollgruppe auch nicht an Feature-Flag-Experimenten teilnehmen können.

### Nutzer:innen aus der globalen Kontrollgruppe ausschließen {#exclude-users-from-the-global-control-group}

Sie können bestimmte Nutzer:innen nicht aus der globalen Kontrollgruppe entfernen, aber Sie können [Ausschlusseinstellungen](#step-3-assign-exclusion-settings) hinzufügen, sodass Campaigns und Canvases mit bestimmten Tags die globale Kontrollgruppe **nicht** verwenden. Sie können Ihre globale Kontrollgruppe auch deaktivieren und erneut aktivieren, um die Mitgliedschaft neu zu mischen. Die ideale Dauer für das Neumischen von Nutzer:innen variiert je nach Art des Tests, den Sie durchführen, aber versuchen Sie, nicht öfter als einmal im Monat neu zu mischen.

## Globale Kontrollgruppe erstellen {#create-a-global-control-group}

### Schritt 1: Zu den Einstellungen der globalen Kontrollgruppe navigieren {#step-1-navigate-to-the-global-control-group-settings}

Gehen Sie im Dashboard zu **Audience** > **Global Control Group**.

### Schritt 2: Einen Prozentsatz aller Nutzer:innen dieser Kontrollgruppe zuweisen {#step-2-assign-a-percentage-of-all-users-to-this-control-group}

Geben Sie einen Prozentsatz für Ihre Kontrollgruppe ein und wählen Sie **Save**. Nach der Eingabe zeigt Braze Ihnen eine Schätzung an, wie viele Nutzer:innen in Ihre globale Kontrollgruppe, die Behandlungsgruppe und die Behandlungsstichprobe fallen. Beachten Sie, dass diese Schätzung umso genauer ist, je mehr Nutzer:innen sich in Ihrem Workspace befinden.

Die Anzahl der Nutzer:innen in Ihrer globalen Kontrollgruppe wird nach der Ersteinrichtung automatisch aktualisiert, um proportional zu diesem Prozentsatz zu bleiben, wenn weitere Nutzer:innen zu Ihrem Workspace hinzugefügt werden. Darüber hinaus werden Nutzer:innen, die nach der Einrichtung der globalen Kontrollgruppe hinzukommen und zufällige Bucket-Nummern haben, ebenfalls der globalen Kontrollgruppe hinzugefügt. Wenn viele Nutzer:innen hinzugefügt werden, wächst die Größe Ihrer globalen Kontrollgruppe, um einen konstanten Prozentsatz im Verhältnis zu Ihrer gesamten Nutzerbasis beizubehalten. Wenn die Größe Ihrer globalen Kontrollgruppe wächst, bleiben die Nutzer:innen, die zuvor in der Gruppe waren, weiterhin in der Gruppe (es sei denn, Sie nehmen Änderungen an Ihrer Gruppe vor, indem Sie sie deaktivieren und eine neue erstellen).

Richtlinien zum Prozentsatz finden Sie unter [Best Practices für Tests](#percentage-guidelines).

![Die Einstellungen der globalen Kontrollgruppe mit der Zielgruppeneinstellung „Assign five percent of all users to the Global Control Group“.]({% image_buster /assets/img/control_group/control_group4.png %})

### Schritt 3: Ausschlusseinstellungen zuweisen {#step-3-assign-exclusion-settings}

Verwenden Sie Tags, um Ausschlusseinstellungen zu Ihrer globalen Kontrollgruppe hinzuzufügen. Campaigns oder Canvases, die die in den Ausschlusseinstellungen enthaltenen Tags verwenden, nutzen Ihre globale Kontrollgruppe nicht. Diese Campaigns und Canvases werden weiterhin an alle Nutzer:innen in der Zielgruppe gesendet, einschließlich derjenigen in Ihrer globalen Kontrollgruppe.

Beachten Sie, dass das Tag-Dropdown nur Tags anzeigt, die derzeit auf mindestens eine aktive Campaign oder ein aktives Canvas angewendet sind. Wenn Sie ein neues Tag erstellen und es in den Ausschlusseinstellungen verwenden möchten, wenden Sie es zuerst auf eine Campaign oder ein Canvas an.

{% alert tip %}
Sie können Ausschlusseinstellungen hinzufügen, wenn Sie transaktionale Nachrichten haben, die an alle Nutzer:innen gesendet werden sollen.
{% endalert %}

![Der Bereich zum Hinzufügen oder Bearbeiten von Ausschlusseinstellungen für Ihre globale Kontrollgruppe.]({% image_buster /assets/img/control_group/control_group5.png %})

### Schritt 4: Kontrollgruppe speichern {#step-4-save-your-control-group}

An diesem Punkt generiert Braze eine zufällig ausgewählte Gruppe von Nutzer:innen, die den ausgewählten Prozentsatz Ihrer gesamten Nutzerbasis umfasst. Nach dem Speichern senden alle derzeit aktiven und zukünftigen Campaigns und Canvases keine Nachrichten mehr an Nutzer:innen in dieser Gruppe, mit Ausnahme von Campaigns oder Canvases, die eines der Tags in Ihren Ausschlusseinstellungen enthalten.

## Änderungen an Ihrer globalen Kontrollgruppe vornehmen {#making-changes-to-your-global-control-group}

Sie können Änderungen an Ihrer globalen Kontrollgruppe nur vornehmen, indem Sie sie deaktivieren und eine neue erstellen. Wenn Sie beispielsweise eine globale Kontrollgruppe eingerichtet haben, die 10 % Ihrer Zielgruppe umfasst, und Sie deren Größe auf 5 % verringern möchten, müssen Sie Ihre aktuelle globale Kontrollgruppe deaktivieren und eine neue globale Kontrollgruppe aktivieren.

Sie können Ihre globale Kontrollgruppe jederzeit über den Tab **Global Control Group Settings** deaktivieren. Beachten Sie jedoch, dass die Nutzer:innen in dieser Gruppe dadurch sofort für Campaigns und Canvases in Frage kommen.

Bevor Sie Ihre Kontrollgruppe deaktivieren, [exportieren](#export-group-members) Sie eine CSV-Datei der Nutzer:innen in dieser Gruppe, falls Sie diese zu einem späteren Zeitpunkt benötigen. Wenn Sie eine Kontrollgruppe deaktivieren, gibt es für Braze keine Möglichkeit, die Gruppe wiederherzustellen oder festzustellen, welche Nutzer:innen sich in dieser Gruppe befanden.

Nach dem Deaktivieren Ihrer Kontrollgruppe können Sie eine neue speichern. Wenn Sie einen Prozentsatz eingeben und speichern, generiert Braze eine neue zufällig ausgewählte Gruppe von Nutzer:innen. Wenn Sie denselben Prozentsatz wie zuvor eingeben, generiert Braze eine neue Gruppe von Nutzer:innen für Ihre Kontroll- und Behandlungsgruppen.

![Ein Dialogfeld mit dem Titel „You are making changes to Global Messaging Settings“ mit einem Warnhinweis, dass Ihre globale Kontrollgruppe nach der Deaktivierung nicht mehr von neuen oder aktiven Campaigns oder Canvases ausgeschlossen wird.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Mitglieder Ihrer Kontrollgruppe exportieren {#export-group-members}

Wenn Sie sehen möchten, welche Nutzer:innen in Ihrer globalen Kontrollgruppe sind, können Sie die Mitglieder Ihrer Gruppe per CSV oder API exportieren.

Um einen CSV-Export durchzuführen, navigieren Sie zum Tab **Global Control Group Settings** und klicken Sie auf <i class="fas fa-download" aria-label="Exportieren"></i>&nbsp;**Export**. Um per API zu exportieren, verwenden Sie den [`/users/export/global_control_group`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group).

{% alert important %}
Historische Kontrollgruppen werden nicht aufbewahrt, sodass Sie nur die Mitglieder Ihrer aktuellen Gruppe exportieren können. Stellen Sie sicher, dass Sie alle erforderlichen Informationen exportieren, bevor Sie eine Kontrollgruppe deaktivieren.
{% endalert %}

## Anzeigen, ob Nutzer:innen in einer globalen Kontrollgruppe sind {#view-whether-a-user-is-in-a-global-control-group}

Sie können die Mitgliedschaft in der globalen Kontrollgruppe einsehen, indem Sie im Kundenprofil auf dem Tab **Engagement** zum Abschnitt **Miscellaneous** navigieren.

![Ein Abschnitt „Miscellaneous“, der anzeigt, dass die Nutzer:in eine zufällige Bucket-Nummer von 6356 hat und nicht in der globalen Kontrollgruppe ist.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Berichterstattung {#reporting}

Der Bericht zur globalen Kontrollgruppe ermöglicht es Ihnen, Ihre Gruppe mit einer Treatment-Stichprobe zu vergleichen. Ihre Treatment-Stichprobe ist eine zufällige Auswahl von Nutzer:innen, die nicht zur Kontrollgruppe gehören, und umfasst ungefähr die gleiche Anzahl von Nutzer:innen wie Ihre Kontrollgruppe. Sie wird mithilfe der Methode der zufälligen Bucket-Nummern generiert.

### Einen Bericht anzeigen {#viewing-a-report}

Um einen Bericht für Ihre globale Kontrollgruppe im Dashboard anzuzeigen, gehen Sie zu **Analytics** > **Global Control Group Report**.

Wählen Sie als Nächstes den Parameter aus, mit dem Sie Ihren Bericht ausführen möchten (Sitzungen oder ein bestimmtes angepasstes Event), und wählen Sie **Bericht ausführen**.

![Wählen Sie als Nächstes den Parameter aus, mit dem Sie Ihren Bericht ausführen möchten (Sitzungen oder ein bestimmtes angepasstes Event), und wählen Sie „Bericht ausführen“.]({% image_buster /assets/img/control_group/control_group6.png %})

### Ihren Bericht konfigurieren {#configuring-your-report}

Wählen Sie beim Erstellen Ihres Berichts ein Event – entweder Sitzungen oder ein beliebiges angepasstes Event – um es über Ihre Treatment- und Kontrollgruppen hinweg zu vergleichen. Wählen Sie dann einen Zeitraum aus, für den Sie Daten anzeigen möchten. Beachten Sie, dass Sie, wenn Sie mehrere Kontrollgruppen-Experimente zu unterschiedlichen Zeiträumen gespeichert haben, vermeiden sollten, Daten aus mehr als einem Experiment in Ihren Bericht aufzunehmen.

Beachten Sie, dass die prozentualen Metriken in Ihrem Bericht gerundet werden. In Fällen, in denen die Anzahl der Konversionen einen sehr geringen Prozentsatz Ihrer gesamten Kontroll- oder Treatment-Gruppe ausmacht, kann die Konversionsrate auf 0 % gerundet werden.

Dieser Bericht zeigt auch einen [Konfidenz]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence)-Prozentsatz für Ihre Metrik „Veränderung gegenüber Kontrollgruppe“ an. In Fällen, in denen die Konversionsrate zwischen Ihrer Kontroll- und Treatment-Gruppe identisch ist, wird eine Konfidenz von 0 % erwartet – dies bedeutet, dass es eine 0%ige Wahrscheinlichkeit für einen Unterschied in der Performance zwischen den beiden Gruppen gibt.

#### Gruppengrößen {#group-sizes}

Vor Mai 2024 war die globale Kontrollgruppe von der Nutzerarchivierung ausgenommen, die Treatment-Stichprobengruppe jedoch nicht. Ab Mai 2024 sind beide Gruppen von der Nutzerarchivierung ausgenommen. Dies könnte dazu führen, dass Ihre Treatment-Stichprobengruppe und Ihre globale Kontrollgruppe deutlich unterschiedliche Größen aufweisen. Wenn Sie Ihre globale Kontrollgruppe das nächste Mal zurücksetzen, wird diese Diskrepanz behoben und Sie werden ähnliche Gruppengrößen sehen.

{% alert note %}
Jeder Workspace hat maximal eine globale Kontrollgruppe und eine Treatment-Stichprobengruppe. Die Treatment-Stichprobengruppe ist dieselbe Gruppe von Nutzer:innen, unabhängig davon, wie Sie Ihre Berichterstattung zur globalen Kontrollgruppe konfigurieren.
{% endalert %}

### Berichtsmetriken {#report-metrics}

| Metrik | Definition | Berechnung |
| -- | -- | -- |
| Veränderung gegenüber Kontrollgruppe | Berechnet den Uplift zwischen der Konversionsrate Ihrer Treatment- und Kontrollgruppe. | ((Konversionsrate Treatment – Konversionsrate Kontrollgruppe) ÷ Konversionsrate Kontrollgruppe) \* 100 |
| Inkrementeller Uplift | Die Differenz der Gesamtereignisse zwischen Ihrer Treatment- und Kontrollgruppe. Diese Metrik versucht die Frage zu beantworten: „Wie viele zusätzliche Konversions-Events hat die Treatment-Gruppe erzielt?“. | Gesamtereignisse Treatment – Gesamtereignisse Kontrollgruppe |
| Inkrementeller Uplift in Prozent | Der Prozentsatz der Gesamtereignisse Ihrer Treatment-Gruppe, der auf Ihr Treatment zurückgeführt werden kann (im Gegensatz zu natürlichem Nutzerverhalten). Wird berechnet, indem der inkrementelle Uplift (Zahl) durch die Gesamtzahl der Ereignisse Ihrer Treatment-Gruppe geteilt wird. | Inkrementeller Uplift (Zahl) ÷ Gesamtereignisse Treatment-Gruppe |
| Konversionsrate | Der geschätzte Prozentsatz der Nutzer:innen in Ihrer Kontroll- oder Treatment-Gruppe, die das ausgewählte Event während des gewählten Zeitraums abschließen. Wird berechnet, indem die Anzahl der Ereignisse aus dem Zeitraum addiert und durch die Summe der Nutzer:innen in der Gruppe pro Tag geteilt wird. Dies kann nur geschätzt werden, da die Gruppengröße regelmäßig schwankt, wenn neue Nutzer:innen Ihrer globalen Kontrollgruppe beitreten, und die Ereignisse Gesamtereignisse – und nicht eindeutige Ereignisse – sind. Wenn die Anzahl der Konversionen sehr gering und Ihre Kontroll- oder Treatment-Gruppe sehr groß ist, kann die Konversionsrate auf 0 % gerundet werden. Wenn die Anzahl der Ereignisse sehr hoch ist – zum Beispiel in Fällen, in denen Nutzer:innen mehr als ein Event pro Tag ausführen können – kann die Konversionsrate über 100 % liegen. | Summe der Anzahl der Ereignisse für diese Nutzer:innen über diesen Zeitraum ÷ Summe der Nutzer:innen in der Gruppe pro Tag |
| Geschätzte Gruppengröße | Die geschätzte Anzahl der Nutzer:innen in Ihrer Kontroll- und Treatment-Gruppe während des ausgewählten Zeitraums. | Die maximale Mitgliedergröße, die Ihre Kontroll- und Treatment-Gruppe während des für den Bericht gewählten Zeitraums erreicht hat. |
| Gesamtzahl der Ereignisse | Die Gesamtzahl, wie oft das ausgewählte Event während des gewählten Zeitraums aufgetreten ist. Dies ist nicht eindeutig (wenn beispielsweise eine Nutzer:in ein Event zweimal während des Zeitraums ausführt, wird das Event zweimal gezählt). | Summe der Anzahl, wie oft ein Event an jedem Tag während des gewählten Zeitraums aufgetreten ist. |
| Ereignisse pro Nutzer:in | Die geschätzte durchschnittliche Anzahl, wie oft Nutzer:innen in jeder Gruppe Ihre Konversions-Events während des ausgewählten Zeitraums abgeschlossen haben. | Gesamtereignisse ÷ geschätzte Gruppengröße. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berichtsmetriken" }

## Fehlerbehebung {#troubleshooting}

Beim Einrichten Ihrer globalen Kontrollgruppen und beim Anzeigen von Berichten können folgende Fehler auftreten:

| Problem | Fehlerbehebung |
| --- | --- |
| Der eingegebene Prozentsatz kann beim Festlegen einer globalen Kontrollgruppe nicht gespeichert werden. | Dieses Problem tritt auf, wenn Sie eine Nicht-Ganzzahl oder eine Ganzzahl eingeben, die nicht zwischen 1 und 15 (einschließlich) liegt. |
| Fehler „Braze is not able to update your Global Control Group“ auf der Einstellungsseite der globalen Kontrollgruppe. | Dies deutet in der Regel darauf hin, dass sich eine Komponente dieser Seite geändert hat, wahrscheinlich aufgrund von Aktionen eines anderen Nutzers bzw. einer anderen Nutzerin in Ihrem Braze-Konto. Aktualisieren Sie in diesem Fall die Seite und versuchen Sie es erneut. |
| Der Bericht der globalen Kontrollgruppe enthält keine Daten. | Wenn Sie auf den Bericht der globalen Kontrollgruppe zugreifen, ohne zuvor eine globale Kontrollgruppe gespeichert zu haben, werden keine Daten im Bericht angezeigt. Erstellen und speichern Sie eine globale Kontrollgruppe und versuchen Sie es erneut. |
| Meine Konversionsrate beträgt 0 % oder die Grafik wird nicht angezeigt, obwohl mehr als null Ereignisse auftreten. | Wenn die Anzahl der Konversionen sehr gering ist und Ihre Kontroll- oder Behandlungsgruppen sehr groß sind, kann die Konversionsrate auf 0 % gerundet werden und wird daher nicht in der Grafik angezeigt. Sie können dies überprüfen, indem Sie die Metrik „Gesamtanzahl der Ereignisse“ prüfen. Sie können die Effektivität Ihrer beiden Gruppen mithilfe der Metrik für den inkrementellen Uplift-Prozentsatz vergleichen. |
| Meine Konversionsrate (oder andere Metriken) ändert sich drastisch je nach dem Zeitraum, für den ich Daten anzeige. | Wenn Sie Daten über kurze Zeiträume betrachten, können Ihre Metriken von Tag zu Tag oder von Woche zu Woche schwanken. Betrachten Sie Metriken über einen Zeitraum von mindestens einem Monat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

### Worauf Sie achten sollten {#things-to-watch-for}

#### Überlappende zufällige Bucket-Nummern {#overlapping-random-bucket-numbers}

Ihre globale Kontrollgruppe wird mithilfe zufälliger Bucket-Nummern gebildet. Wenn Sie also andere Tests mit Segmentfiltern für zufällige Bucket-Nummern durchführen, beachten Sie, dass es eine Überlappung zwischen den von Ihnen erstellten Segmenten und den Nutzer:innen Ihrer globalen Kontrollgruppe geben kann.

#### Doppelte E-Mail-Adressen {#duplicate-email-addresses}

Wenn zwei Nutzer:innen mit unterschiedlichen externen Nutzer-IDs dieselbe E-Mail-Adresse haben und eine dieser Personen in der Kontrollgruppe ist und die andere nicht, wird trotzdem eine E-Mail an diese E-Mail-Adresse gesendet, wenn die Person außerhalb der Kontrollgruppe für eine E-Mail berechtigt ist. In diesem Fall werden beide Nutzerprofile als Empfänger:innen der Campaign oder des Canvas markiert, die bzw. der diese E-Mail enthält.

#### Globale Kontrollgruppe und nachrichtenspezifische Kontrollgruppen {#global-control-group-and-message-specific-control-groups}

Es ist möglich, sowohl eine globale Kontrollgruppe als auch eine Campaign-spezifische oder Canvas-spezifische Kontrollgruppe zu verwenden. Eine Campaign-spezifische oder Canvas-spezifische Kontrollgruppe ermöglicht es Ihnen, die Wirkung einer bestimmten Nachricht zu messen.

Nutzer:innen in Ihrer globalen Kontrollgruppe erhalten keine Nachrichten außer solchen mit Tag-Ausnahmen. Wenn Sie einer Campaign oder einem Canvas eine Kontrollgruppe hinzufügen, hält Braze einen Teil Ihrer globalen Behandlungsgruppe vom Empfang dieser bestimmten Campaign oder dieses Canvas zurück. Das bedeutet: Wenn ein Mitglied der globalen Kontrollgruppe nicht für eine bestimmte Campaign oder ein bestimmtes Canvas berechtigt ist, ist es nicht in der Kontrollgruppe dieser bestimmten Campaign oder dieses Canvas enthalten.

{% alert note %}
Kurz gesagt: Nutzer:innen in der globalen Kontrollgruppe werden vor dem Eintritt aus der Campaign- oder Canvas-Zielgruppe herausgefiltert. Von den Nutzer:innen, die in die Campaign oder das Canvas eintreten, wird ein Prozentsatz der Kontrollvariante zugewiesen.
{% endalert %}

#### Segmente der globalen Kontrollgruppe in der Entwicklungskonsole {#global-control-group-segments-on-the-developer-console}

Möglicherweise sehen Sie mehrere **Global Control**-Segmente im Abschnitt **Additional API Identifiers** auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Dies liegt daran, dass jedes Mal, wenn die globale Kontrollgruppe aktiviert oder deaktiviert wird, eine neue globale Kontrollgruppe gebildet wird. Dies führt zu mehreren Segmenten mit der Bezeichnung „Global Control Group“.

Nur eines dieser Segmente ist aktiv und kann über den [`/users/export/global_control_group`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) abgefragt oder aus dem Dashboard exportiert werden. Der Export aus dem Dashboard gibt ausdrücklich an, welche Untersegmente diese globale Kontrollgruppe bilden.

## Best Practices für Tests {#testing-best-practices}

### Optimale Größe der Kontrollgruppe {#percentage-guidelines}

Zwei wichtige Regeln, die Sie beachten sollten:
1. Ihre Kontrollgruppe sollte nicht kleiner als 1.000 Nutzer:innen sein.
2. Ihre Kontrollgruppe sollte nicht mehr als 10 % Ihrer gesamten Zielgruppe ausmachen.

Wenn Ihre Gesamtzielgruppe kleiner als 10.000 ist, sollten Sie den Prozentsatz erhöhen, um eine Gruppe von über 1.000 Nutzer:innen zu erstellen. In diesem Fall sollten Sie den Prozentsatz jedoch nicht über 15 % hinaus erhöhen. Bedenken Sie, dass es umso schwieriger ist, einen statistisch belastbaren Test durchzuführen, je kleiner Ihr gesamter Workspace ist.

- Einige Abwägungen, die Sie bei der Größe Ihrer Kontrollgruppe berücksichtigen sollten: Sie benötigen eine ausreichend große Anzahl von Kund:innen in Ihrer Kontrollgruppe, damit jede daraus abgeleitete Verhaltensanalyse vertrauenswürdig ist. Je größer Ihre Kontrollgruppe jedoch ist, desto weniger Kund:innen erhalten Ihre Campaigns – ein Nachteil, wenn Sie Ihre Campaigns nutzen, um Engagement und Konversionen zu steigern.
- Der ideale Prozentsatz Ihrer Gesamtzielgruppe hängt davon ab, wie groß Ihre Gesamtzielgruppe ist. Je größer Ihre Gesamtzielgruppe ist, desto kleiner kann Ihr Prozentsatz sein. Bei einer kleinen Zielgruppe benötigen Sie hingegen einen größeren Prozentsatz für Ihre Kontrollgruppe.

### Experimentdauer {#experiment-duration}

#### Eine ideale Dauer wählen {#reshuffle}

Wie lange Sie Ihr Experiment durchführen sollten, bevor Sie die Mitgliedschaft in der Kontrollgruppe neu mischen, hängt davon ab, was Sie testen und wie das Basisverhalten Ihrer Nutzer:innen aussieht. Wenn Sie unsicher sind, ist ein Quartal (drei Monate) ein guter Ausgangspunkt, aber Sie sollten nicht kürzer als einen Monat planen.

Um die angemessene Dauer für Ihr Experiment zu bestimmen, überlegen Sie, welche Fragen Sie beantworten möchten. Möchten Sie beispielsweise herausfinden, ob es einen Unterschied bei den Sitzungen gibt? Wenn ja, denken Sie darüber nach, wie oft Ihre Nutzer:innen organisch Sitzungen haben. Marken, deren Nutzer:innen täglich Sitzungen haben, können kürzere Experimente durchführen als Marken, deren Nutzer:innen nur ein paar Mal im Monat Sitzungen haben.

Oder Sie interessieren sich für ein angepasstes Event – in diesem Fall muss Ihr Experiment möglicherweise länger laufen als ein Experiment, bei dem Sie Sitzungen untersuchen, wenn es wahrscheinlich ist, dass Ihre Nutzer:innen dieses angepasste Event seltener auslösen.

{% alert tip %}
Je länger Sie dieselbe Kontrollgruppe ausschließen, desto stärker weicht sie von der Behandlungsgruppe ab, was zu Verzerrungen führen kann. Das Zurücksetzen der globalen Kontrollgruppe gleicht die Population wieder aus.
{% endalert %}

#### Versuchen Sie, Experimente nicht vorzeitig zu beenden {#try-to-limit-ending-experiments-prematurely}

Legen Sie vor Beginn fest, wie lange Ihr Experiment laufen soll, und beenden Sie es erst dann und erfassen Sie die endgültigen Ergebnisse, wenn Sie diesen vorab festgelegten Zeitpunkt erreicht haben. Ein vorzeitiges Beenden Ihres Experiments – oder ein Abbruch, sobald vielversprechende Daten vorliegen – führt zu Verzerrungen.

#### Denken Sie an aussagekräftige Metriken {#think-about-valuable-metrics}

Berücksichtigen Sie das Basisverhalten für die Metriken, die Sie am meisten interessieren. Interessieren Sie sich für Kaufraten bei Abo-Plänen, die nur jährlich verlängert werden? Oder haben Kund:innen eine wöchentliche Gewohnheit für das Event, das Sie messen möchten? Überlegen Sie, wie lange es dauert, bis Nutzer:innen ihr Verhalten aufgrund Ihres Messagings möglicherweise ändern. Nachdem Sie entschieden haben, wie lange Ihr Experiment laufen soll, beenden Sie es nicht vorzeitig und erfassen Sie die endgültigen Ergebnisse nicht zu früh, da Ihre Erkenntnisse sonst verzerrt sein könnten.