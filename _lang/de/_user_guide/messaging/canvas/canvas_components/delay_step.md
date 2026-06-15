---
nav_title: Verzögerung
article_title: Verzögerung
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie eine Verzögerung zu Ihrem Canvas hinzufügen können, ohne eine zugehörige Nachricht hinzufügen zu müssen."
tool: Canvas

---

# Verzögerung

> Verzögerungskomponenten ermöglichen es Ihnen, eine eigenständige Verzögerung zu einem Canvas hinzuzufügen. Sie können eine Verzögerung zu Ihrem Canvas hinzufügen, ohne eine zugehörige Nachricht hinzufügen zu müssen.

Verzögerungen können Ihren Canvas übersichtlicher gestalten. Sie können diese Komponente auch verwenden, um einen anderen Schritt bis zu einem genauen Datum, bis zu einem bestimmten Tag oder bis zu einem bestimmten Wochentag zu verzögern. Eine Verzögerungskomponente kann mit höchstens einem nachfolgenden Schritt verbunden werden. <br> ![Ein Verzögerungsschritt mit einer 1-tägigen Verzögerung als erster Schritt eines Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Eine Verzögerung erstellen

Um eine Verzögerung zu erstellen, fügen Sie einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Verzögerungskomponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und dann **Delay**.

#### Erweiterte Verzögerungen

Sie können Verzögerungsschritte auf bis zu zwei Jahre (730 Tage) verlängern. Wenn Sie beispielsweise neue Nutzer:innen für Ihre App onboarden, können Sie eine erweiterte Verzögerung von zwei Monaten hinzufügen, bevor Sie einen Nachrichtenschritt senden, um die Nutzer:innen anzustoßen, die noch keine Sitzung gestartet haben.

## Arten von Zeitverzögerungen

Sie können die Art der Verzögerung vor der nächsten Nachricht in Ihrem Canvas auswählen. Sie können entweder eine Verzögerung festlegen, die Ihre Nutzer:innen nach einem bestimmten Zeitraum weiterleitet, oder Ihre Nutzer:innen bis zu einem bestimmten Datum und einer bestimmten Uhrzeit verzögern.

Wenn es eine Zeitverzögerung gibt, ist zu erwarten, dass einige Nutzer:innen erst nach der Verzögerung zum nächsten Schritt des Canvas weitergehen. Nutzer:innen, die sich in der Verzögerung befinden, werden nicht zur Metrik _Proceeded to Next Step_ hinzugefügt. Weitere Informationen finden Sie unter [Verzögerungs-Analytics](#delay-analytics).

{% tabs %}
{% tab Duration %}

Die Auswahl von **Duration** ermöglicht es Ihnen, Nutzer:innen für eine festgelegte Anzahl von Sekunden, Minuten, Stunden, Tagen oder Wochen und zu einer bestimmten Uhrzeit zu verzögern. Beispielsweise können Sie Nutzer:innen für vier Stunden oder für einen Tag verzögern.

Beachten Sie den Unterschied, wie „Tage“ und „Kalendertage“ berechnet werden.

- Ein „Tag“ umfasst 24 Stunden und wird ab dem Zeitpunkt berechnet, zu dem die Nutzer:innen den Verzögerungsschritt betreten.
- Ein „Kalendertag“ definiert die Wartezeit bis zur nächsten angegebenen Uhrzeit, die weniger als 24 Stunden betragen kann. Sie können wählen, ob die Verzögerung in Unternehmenszeit oder in der Ortszeit der Nutzer:innen erfolgen soll. Wenn keine Uhrzeit angegeben ist, werden die Nutzer:innen bis Mitternacht des nächsten Tages in Unternehmenszeit verzögert.

Sie können auch **At a specific time** auswählen, um festzulegen, wann die Nutzer:innen im Canvas voranschreiten. Diese Option berücksichtigt den Zeitpunkt, zu dem die Nutzer:innen den Verzögerungsschritt betreten haben. Wenn dieser Zeitpunkt über die in den Einstellungen konfigurierte Zeit hinausgeht, werden zusätzliche Stunden zur Verzögerung hinzugefügt.

Nehmen wir als Beispiel an, heute ist der 11. Dezember, und unser Verzögerungsschritt ist auf eine **Duration** von einer Woche um 8 Uhr UTC eingestellt. Wenn Nutzer:innen den Verzögerungsschritt am 4. Dezember betreten haben, würden sie heute aus dem Verzögerungsschritt entlassen, um ihre Journey fortzusetzen, sofern sie den Verzögerungsschritt ursprünglich vor 8 Uhr UTC betreten haben. Wenn sie den Verzögerungsschritt nach dieser Uhrzeit betreten haben, werden die Nutzer:innen bis zum nächsten Tag (dem nächsten Vorkommen dieser Uhrzeit) verzögert.

{% endtab %}
{% tab Calendar date %}

Die Auswahl von **Calendar date** ermöglicht es Ihnen, Nutzer:innen im Schritt bis zu einem bestimmten Datum und einer bestimmten Uhrzeit zu halten.

#### Hinweise

##### Nutzer:innen erhalten keine Schritte oder Nachrichten mit vergangenem Datum

Wenn das ausgewählte Datum und die Uhrzeit bereits vergangen sind, wenn Nutzer:innen zum Verzögerungsschritt gelangen, verlassen die Nutzer:innen den Canvas. Zwischen dem Start des Canvas und den für „Warten bis zu einem genauen Tag“-Schritte gewählten Daten können bis zu 31 Tage liegen.

{% alert important %}
Wenn Sie am [Canvas Context Early Access]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) teilnehmen, können Sie Verzögerungen von bis zu 2 Jahren festlegen.
{% endalert %}

Beispielsweise erhalten Nutzer:innen in diesen Szenarien keine Schritte oder Nachrichten:

- Eine Nachricht ist für den 3. Mai um 21 Uhr geplant, aber der Verzögerungsschritt läuft am 3. Mai um 9 Uhr ab.
- Ein Canvas-Schritt verzögert bis zu einer bestimmten Uhrzeit in der Ortszeit der Nutzer:innen, aber die Nutzer:innen haben keine Zeitzone in ihrem Nutzerprofil hinterlegt. Die Verzögerung fällt dann für diese Nutzer:innen auf die Unternehmens-Zeitzone zurück, die die angegebene Uhrzeit bereits überschritten hat.

##### Nutzer:innen verlassen den Canvas, wenn ein nachfolgender Verzögerungsschritt innerhalb des Zeitrahmens eines vorherigen Verzögerungsschritts liegt

Wenn der Canvas zwei Verzögerungsschritte hat, aber der erste Verzögerungsschritt länger als der zweite Verzögerungsschritt ist, verlassen die Nutzer:innen ebenfalls den Canvas.

Nehmen wir beispielsweise an, ein Canvas hat diese Schritte:
- Schritt 1: Nachrichtenschritt
- Schritt 2: Verzögerungsschritt bis zum 13. Dezember um 22 Uhr
- Schritt 3: Nachrichtenschritt
- Schritt 4: Verzögerungsschritt bis zum 13. Dezember um 19 Uhr
- Schritt 5: Nachrichtenschritt

Die Nutzer:innen, die Schritt 4 betreten, verlassen den Canvas, bevor sie Schritt 5 erhalten, da die Verzögerung von Schritt 4 Teil des Zeitrahmens von Schritt 2 ist.

{% endtab %}
{% tab Wochentag %}

Die Auswahl von **Day of the week** ermöglicht es Ihnen, Nutzer:innen im Schritt bis zu einem bestimmten Wochentag zu einer bestimmten Uhrzeit zu halten. Beispielsweise können Sie Nutzer:innen bis zum nächsten Donnerstag um 16 Uhr in der Zeitzone des Unternehmens verzögern.

Um dies erfolgreich zu konfigurieren, müssen Sie auch festlegen, was passiert, wenn Nutzer:innen den Canvas am ausgewählten Wochentag (z. B. Donnerstag) betreten, aber nach der angegebenen Uhrzeit. Sie können wählen, ob die Nutzer:innen am selben Tag vorangebracht oder bis zur folgenden Woche gehalten werden sollen.
{% endtab %}
{% endtabs %}

## Verzögerungsschritte verwenden

Nehmen wir an, es ist der 10. Juni. Am 11. Juni möchten Sie, dass Nutzer:innen den Canvas betreten und eine Nachricht über eine bevorstehende Aktion erhalten. Dann möchten Sie die Nutzer:innen im Canvas bis zum 17. Juni um 15 Uhr Ortszeit halten. Um 15 Uhr Ortszeit am 17. Juni möchten Sie den Nutzer:innen eine Erinnerungsnachricht über die Aktion senden.

Die Abfolge der Canvas-Schritte könnte wie folgt aussehen:

1. Beginnen Sie mit einem Nachrichtenschritt, der sofort gesendet wird, nachdem Nutzer:innen den Canvas am 11. Juni betreten.
2. Erstellen Sie einen Verzögerungsschritt, der Nutzer:innen bis 15 Uhr Ortszeit am 17. Juni hält.
3. Verknüpfen Sie den Verzögerungsschritt mit einem weiteren Nachrichtenschritt, der seine Nachricht sofort sendet.

### Verzögerungskomponenten am Ende eines Canvas {#delay-as-last-step}

Wenn Sie eine Verzögerungskomponente zu Ihrem Canvas hinzufügen und es keine nachfolgenden Schritte gibt, werden alle Nutzer:innen, die den letzten Schritt erreichen, automatisch aus dem Canvas weitergeleitet. Dies gilt auch dann, wenn die Zeit des Verzögerungsschritts noch nicht erreicht wurde. Das bedeutet, dass Nutzer:innen, die den Verzögerungsschritt bereits erreicht haben, keine Nachrichten erhalten, die Sie nach diesem Schritt hinzufügen. Wenn Nutzer:innen den Verzögerungsschritt jedoch noch nicht erreicht haben und eine Nachricht hinzugefügt wird, würden sie diese Nachricht erhalten.

### Personalisierte Verzögerungen

{% multi_lang_include early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Wählen Sie den Schalter **Personalize delay**, um eine personalisierte Verzögerung für Ihre Nutzer:innen einzurichten. Sie können dies mit einem [Context-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) verwenden, um die Kontextvariable auszuwählen, nach der verzögert werden soll. Dies überschreibt die im ausgewählten Attribut oder der Eigenschaft festgelegte Tageszeit. Dies ist nützlich, wenn Sie einen Versatz in Tagen oder Wochen anwenden und möchten, dass Nutzer:innen zu einer bestimmten Uhrzeit weitergehen. Die Zeitzone stammt aus dem Attribut oder der Eigenschaft oder verwendet den Fallback, wenn keine verfügbar ist.

#### Zeitzonenverhalten für „zu einer bestimmten Uhrzeit“

Beim Konfigurieren personalisierter Verzögerungen mit der Option **at specific time** hängt das Zeitzonenverhalten vom Datentyp Ihres Attributs oder Ihrer Kontextvariable ab:

- **String-Datentyp mit Zeitzone:** Wenn das Attribut oder die Kontextvariable ein String-Datentyp ist, der Zeitzoneninformationen enthält, wird die in dem String angegebene Zeitzone verwendet. Beispielsweise verwendet `2025-06-10T10:00:00-08:00` UTC-8.
- **String-Datentyp ohne Zeitzone:** Wenn das Attribut oder die Kontextvariable ein String-Datentyp ohne Zeitzoneninformationen ist, wird die Fallback-Zeitzone verwendet. Beispielsweise verwendet `2025-06-10` die Fallback-Zeitzone.
- **Time-Datentyp:** Wenn das Attribut oder die Kontextvariable ein Time-Datentyp ist, wird UTC verwendet. Dies liegt daran, dass der Time-Datentyp beim Speichern in der Datenbank immer in UTC konvertiert wird, sodass „zu einer bestimmten Uhrzeit“ immer auf UTC verweist, wenn die Variable auf den Time-Datentyp gesetzt ist. Beispielsweise verwendet `2025-06-10T10:00:00-08:00` UTC+0.

{% alert note %}
Es ist möglich, dass ein angepasstes Attribut oder eine Kontextvariable weder eine bestimmte Uhrzeit noch eine Zeitzone hat, wenn es sich um einen String-Datentyp handelt. Bei einem Time-Datentyp müssen Sie die Uhrzeit und Zeitzone angeben. Wenn das angepasste Attribut oder die Kontextvariable jedoch ein „irrelevanter“ String ist (wie „product_name“), verlassen die Nutzer:innen den Canvas.
{% endalert %}

#### Anwendungsfall

Nehmen wir an, Sie möchten Ihre Kund:innen daran erinnern, in 30 Tagen Zahnpasta zu kaufen. Mit einer Kombination aus einem Context-Schritt und einem Verzögerungsschritt können Sie diese Kontextvariable auswählen, nach der verzögert werden soll. In diesem Fall hätte Ihr Context-Schritt die folgenden Felder:

- **Context variable name:** product_reminder_interval
- **Data type:** Time
- **Value:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![Die Kontextvariable „product_reminder_interval“ und ihr Wert.]({% image_buster /assets/img/context_step1.png %})

Da Sie Ihre Kund:innen in 30 Tagen erinnern möchten, wählen Sie als Nächstes **Until a specific day** als Verzögerungsoption und wählen **Personalize delay**, um die Informationen aus Ihrem Context-Schritt zu verwenden. Das bedeutet, dass Ihre Nutzer:innen bis zur ausgewählten Kontextvariable verzögert werden.

## Verzögerungs-Analytics {#delay-analytics}

Verzögerungskomponenten verfügen über die folgenden Metriken in der Analytics-Ansicht eines aktiven oder zuvor aktiven Canvas.

| Metrik | Beschreibung |
|---|---|
| _Entered_ | Gibt an, wie oft der Schritt betreten wurde. Wenn Ihr Canvas eine erneute Berechtigung hat und Nutzer:innen einen Verzögerungsschritt zweimal betreten, werden zwei Eintritte erfasst. |
| _Proceeded to Next Step_ | Gibt die Anzahl der Eintritte an, die zum nächsten Schritt im Canvas weitergegangen sind. |
| _Exited Canvas_ | Gibt die Anzahl der Eintritte an, die den Canvas verlassen haben und nicht zum nächsten Schritt weitergegangen sind. |
| _Personalization Failed_ | Gibt an, wie oft eine personalisierte Nachricht oder ein personalisierter Inhalt für Nutzer:innen nicht zugestellt werden konnte, aufgrund folgender Gründe:<br> {::nomarkdown}<ul><li>Der Verzögerungswert liegt in der Vergangenheit</li><li>Der Verzögerungswert liegt mehr als 2 Jahre in der Zukunft</li><li>Der <b>After a duration</b>-Wert ist keine Zahl</li><li>Der <b>Until a specific day</b>-Wert ist kein Datum oder kein datumsformatierter String</li></ul>{:/} <br>Weitere Details finden Sie unter [Fehler bei fehlgeschlagener Personalisierung](#personaliztion-failed-errors). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verzögerungs-Analytics" }

Zeitreihen für diese Analytics sind in der erweiterten Komponentenansicht verfügbar.

## Fehlerbehebung

### Fehler bei fehlgeschlagener Personalisierung {#personaliztion-failed-errors}

Wenn Nutzer:innen keine personalisierte Verzögerung triggern, könnte es daran liegen, dass der Context-Schritt, den Sie eingerichtet haben, um sie für den Verzögerungsschritt zu qualifizieren, nicht wie erwartet funktioniert. Wenn eine [Kontextvariable ungültig ist]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/#troubleshooting), durchlaufen Nutzer:innen Ihren Canvas weiter, ohne dass ihr Kontext durch den Context-Schritt gesetzt wird. Dies kann dazu führen, dass sie sich nicht für spätere Schritte in Ihrem Canvas qualifizieren, wie z. B. personalisierte Verzögerungen.

### Nutzer:innen in einem Verzögerungsschritt, wenn ein Canvas gestoppt wird

Wenn Sie [einen Canvas stoppen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/#stopping-canvases), werden Nutzer:innen, die bereits in einem Verzögerungsschritt warten, nicht sofort entfernt. Braze plant weiterhin den Abschluss der Verzögerung, aber **es werden keine weiteren Nachrichten gesendet**, solange der Canvas gestoppt ist.

Wenn Sie den Canvas erneut aktivieren, bevor die Verzögerung abgelaufen ist, können die Nutzer:innen wie geplant zum nächsten Schritt weitergehen. Wenn das Verzögerungsfenster bereits abgelaufen ist, während der Canvas gestoppt war, verlassen diese Nutzer:innen den Canvas, anstatt den nächsten Schritt zu erhalten. Beispiele finden Sie unter [Was passiert, wenn Sie einen Canvas stoppen?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#what-happens-when-you-stop-a-canvas) und [Canvases stoppen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/#stopping-canvases).