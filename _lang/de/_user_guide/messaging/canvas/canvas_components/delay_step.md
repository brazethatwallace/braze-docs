---
nav_title: Verzögerung
article_title: Verzögerung
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie eine Verzögerung zu Ihrem Canvas hinzufügen können, ohne eine zugehörige Nachricht hinzufügen zu müssen."
tool: Canvas

---

# Verzögerung {#delay}

> Verzögerungskomponenten ermöglichen es Ihnen, eine eigenständige Verzögerung zu einem Canvas hinzuzufügen. Sie können eine Verzögerung zu Ihrem Canvas hinzufügen, ohne eine zugehörige Nachricht hinzufügen zu müssen.

Verzögerungen können Ihren Canvas übersichtlicher gestalten. Sie können diese Komponente auch verwenden, um einen anderen Schritt bis zu einem genauen Datum, bis zu einem bestimmten Tag oder bis zu einem bestimmten Wochentag zu verzögern. Eine Verzögerungskomponente kann mit höchstens einem nachfolgenden Schritt verbunden werden. <br> ![Ein Verzögerungsschritt mit einer 1-tägigen Verzögerung als erster Schritt eines Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Delay erstellen {#create-a-delay}

Um einen Delay zu erstellen, fügen Sie Ihrem Canvas einen Schritt hinzu. Ziehen Sie die Delay-Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und dann **Delay** aus.

### Erweiterte Delays {#extended-delays}

Sie können Delay-Schritte auf bis zu zwei Jahre (730 Tage) verlängern. Wenn Sie beispielsweise neue Nutzer:innen für Ihre App onboarden, können Sie einen erweiterten Delay von zwei Monaten hinzufügen, bevor Sie einen Nachrichten-Schritt senden, um die Nutzer:innen anzustoßen, die noch keine Sitzung gestartet haben.

## Arten von Zeitverzögerungen {#time-delay-types}

Sie können die Art der Verzögerung vor der nächsten Nachricht in Ihrem Canvas auswählen. Sie können entweder eine Verzögerung festlegen, die Ihre Nutzer:innen für einen bestimmten Zeitraum warten lässt, oder Ihre Nutzer:innen bis zu einem bestimmten Datum und einer bestimmten Uhrzeit verzögern.

Wenn eine Zeitverzögerung vorliegt, ist es zu erwarten, dass einige Nutzer:innen erst nach der Verzögerung zum nächsten Canvas-Schritt weitergehen. Nutzer:innen, die sich in der Verzögerung befinden, werden nicht zur Metrik _Zum nächsten Schritt weitergegangen_ hinzugefügt. Weitere Informationen finden Sie unter [Verzögerungs-Analytics](#delay-analytics).

{% tabs %}
{% tab Dauer %}

Wenn Sie **Dauer** auswählen, können Sie Nutzer:innen für eine festgelegte Anzahl von Sekunden, Minuten, Stunden, Tagen oder Wochen und zu einer bestimmten Uhrzeit verzögern. Beispielsweise können Sie Nutzer:innen um vier Stunden oder um einen Tag verzögern.

Beachten Sie den Unterschied zwischen der Berechnung von „Tagen“ und „Kalendertagen“.

- Ein „Tag“ umfasst 24 Stunden und wird ab dem Zeitpunkt berechnet, an dem die Nutzer:innen den Verzögerungsschritt betreten.
- Ein „Kalendertag“ definiert die Wartezeit bis zur nächsten angegebenen Uhrzeit, die weniger als 24 Stunden betragen kann. Sie können wählen, ob die Verzögerung in Unternehmenszeit oder in der Ortszeit der Nutzer:innen erfolgen soll. Wenn keine Uhrzeit angegeben ist, werden die Nutzer:innen bis Mitternacht des nächsten Tages in Unternehmenszeit verzögert.

### Verzögerungsverhalten: „Kalendertage“ zu einer bestimmten Uhrzeit im Vergleich zu „Tagen“ {#delay-behavior-calendar-days-at-a-specific-time-versus-days}

Wenn Sie **Kalendertage** als Einheit auswählen und **Zu einer bestimmten Uhrzeit** aktivieren (z. B. **1 Kalendertag um 9 Uhr**), berechnet Canvas zuerst das Ziel-Kalenderdatum und wendet dann die geplante Uhrzeit an. Wenn beispielsweise ein Canvas-Schritt am Montag um 21 Uhr sendet und der Verzögerungsschritt auf **1 Kalendertag um 9 Uhr** eingestellt ist, wird der nächste Schritt am Dienstag um 9 Uhr gesendet. Canvas berechnet Montag + 1 Kalendertag = Dienstag und wendet dann die Uhrzeit 9 Uhr an.

Im Gegensatz dazu wartet Canvas, wenn Sie **Tage** als Einheit ohne **Zu einer bestimmten Uhrzeit** auswählen (z. B. **Nach 1 Tag**), volle 24 Stunden ab dem Zeitpunkt, an dem die Nutzer:innen den Verzögerungsschritt betreten. Wenn beispielsweise ein Schritt am 13. Oktober um 9:35 Uhr sendet und der Verzögerungsschritt **Nach 1 Tag** beträgt, wird der nächste Schritt am 14. Oktober um 9:35 Uhr gesendet.

Sie können auch **Zu einer bestimmten Uhrzeit** auswählen, um festzulegen, wann die Nutzer:innen im Canvas weitergehen. Diese Option berücksichtigt den Zeitpunkt, zu dem die Nutzer:innen den Verzögerungsschritt betreten haben. Wenn dieser Zeitpunkt nach der in den Einstellungen konfigurierten Uhrzeit liegt, fügt Braze der Verzögerung weitere Stunden hinzu.

Nehmen wir als Beispiel an, heute ist der 11. Dezember und unser Verzögerungsschritt ist auf eine **Dauer** von einer Woche um 8 Uhr UTC eingestellt. Wenn Nutzer:innen den Verzögerungsschritt am 4. Dezember betreten, werden sie heute aus dem Verzögerungsschritt entlassen, um ihre Journey fortzusetzen, sofern sie den Verzögerungsschritt ursprünglich vor 8 Uhr UTC betreten haben. Wenn sie den Verzögerungsschritt nach dieser Uhrzeit betreten haben, werden die Nutzer:innen bis zum nächsten Tag (dem nächsten Vorkommen dieser Uhrzeit) verzögert.

{% endtab %}
{% tab Kalenderdatum %}

Wenn Sie **Kalenderdatum** auswählen, können Sie Nutzer:innen im Schritt bis zu einem bestimmten Datum und einer bestimmten Uhrzeit halten.

### Hinweise {#considerations}

#### Nutzer:innen erhalten keine Schritte oder Nachrichten mit vergangenem Datum {#users-wont-receive-past-dated-steps-or-messages}

Wenn das ausgewählte Datum und die Uhrzeit bereits vergangen sind, wenn Nutzer:innen zum Verzögerungsschritt gelangen, verlassen sie den Canvas. Zwischen dem Start des Canvas und den für „Warten bis zu einem bestimmten Tag“-Schritte gewählten Daten können bis zu 31 Tage liegen.

{% alert important %}
Wenn Sie am [Canvas-Kontext Early Access]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) teilnehmen, können Sie Verzögerungen von bis zu 2 Jahren festlegen.
{% endalert %}

Beispielsweise erhalten Nutzer:innen in diesen Szenarien keine Schritte oder Nachrichten:

- Eine Nachricht ist für den 3. Mai um 21 Uhr geplant, aber der Verzögerungsschritt läuft am 3. Mai um 9 Uhr ab.
- Ein Canvas-Schritt verzögert bis zu einer bestimmten Uhrzeit in der Ortszeit der Nutzer:innen, aber die Nutzer:innen haben keine Zeitzone in ihrem Nutzerprofil hinterlegt. Die Verzögerung verwendet dann standardmäßig die Unternehmens-Zeitzone für diese Nutzer:innen, und die angegebene Uhrzeit ist bereits vergangen.

#### Nutzer:innen verlassen den Canvas, wenn ein nachfolgender Verzögerungsschritt innerhalb des Zeitrahmens eines vorherigen Verzögerungsschritts liegt {#users-exit-if-a-subsequent-delay-step-is-within-a-prior-delay-steps-timeline}

Wenn der Canvas zwei Verzögerungsschritte hat, der erste Verzögerungsschritt aber länger als der zweite ist, verlassen die Nutzer:innen ebenfalls den Canvas.

Nehmen wir beispielsweise an, ein Canvas hat diese Schritte:
- Schritt 1: Nachrichtenschritt
- Schritt 2: Verzögerungsschritt bis zum 13. Dezember um 22 Uhr
- Schritt 3: Nachrichtenschritt
- Schritt 4: Verzögerungsschritt bis zum 13. Dezember um 19 Uhr
- Schritt 5: Nachrichtenschritt

Die Nutzer:innen, die Schritt 4 betreten, verlassen den Canvas, bevor sie Schritt 5 erhalten, da die Verzögerung von Schritt 4 Teil des Zeitrahmens von Schritt 2 ist.

{% endtab %}
{% tab Wochentag %}

Wenn Sie **Wochentag** auswählen, können Sie Nutzer:innen im Schritt bis zu einem bestimmten Wochentag zu einer bestimmten Uhrzeit halten. Beispielsweise können Sie Nutzer:innen bis zum nächsten Donnerstag um 16 Uhr in der Zeitzone des Unternehmens verzögern.

Um dies erfolgreich zu konfigurieren, müssen Sie auch festlegen, was passiert, wenn Nutzer:innen den Canvas am ausgewählten Wochentag (z. B. Donnerstag) betreten, aber nach der angegebenen Uhrzeit. Sie können wählen, ob die Nutzer:innen am selben Tag weitergehen oder bis zur folgenden Woche gehalten werden.
{% endtab %}
{% endtabs %}

### Profilaktualisierungen während Verzögerungen {#profile-updates-during-delays}

Wenn Nutzer:innen einen Canvas betreten und während des Verzögerungsschritts eine gültige E-Mail-Adresse hinzufügen, bevor dieser endet, erhalten sie die E-Mail im nächsten Schritt. Dies gilt auch für andere Profilaktualisierungen. Alle Änderungen an Nutzerattributen oder Kontaktinformationen während der Verzögerung werden berücksichtigt, wenn die Nutzer:innen zu den nachfolgenden Schritten weitergehen.

## Verzögerungsschritte verwenden {#using-delay-steps}

Nehmen wir an, es ist der 10. Juni. Am 11. Juni möchten Sie, dass Nutzer:innen den Canvas betreten und eine Nachricht über eine bevorstehende Aktion erhalten. Dann möchten Sie die Nutzer:innen im Canvas halten, bis zum 17. Juni um 15 Uhr Ortszeit. Um 15 Uhr Ortszeit am 17. Juni möchten Sie den Nutzer:innen eine Erinnerungsnachricht über die Aktion senden.

Die Abfolge der Canvas-Schritte könnte wie folgt aussehen:

1. Beginnen Sie mit einem Nachrichten-Schritt, der sofort gesendet wird, nachdem Nutzer:innen am 11. Juni den Canvas betreten.
2. Erstellen Sie einen Verzögerungsschritt, der Nutzer:innen bis 13 Uhr Ortszeit am 17. Juni hält.
3. Verknüpfen Sie den Verzögerungsschritt mit einem weiteren Nachrichten-Schritt, der seine Nachricht sofort sendet.

### Verzögerungskomponenten am Ende eines Canvas {#delay-as-last-step}

Wenn Sie eine Verzögerungskomponente zu Ihrem Canvas hinzufügen und keine nachfolgenden Schritte vorhanden sind, werden alle Nutzer:innen, die den letzten Schritt erreichen, automatisch aus dem Canvas herausgeführt. Dies gilt auch dann, wenn die Zeit des Verzögerungsschritts noch nicht erreicht wurde. Das bedeutet, dass Nutzer:innen, die den Verzögerungsschritt bereits erreicht haben, keine Nachrichten erhalten, die Sie nach diesem Schritt hinzufügen. Wenn jedoch Nutzer:innen den Verzögerungsschritt noch nicht erreicht haben und eine Nachricht hinzugefügt wird, erhalten sie diese Nachricht.

### Personalisierte Verzögerungen {#personalized-delays}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Wählen Sie den Schalter **Verzögerung personalisieren** aus, um eine personalisierte Verzögerung für Ihre Nutzer:innen einzurichten. Sie können dies mit einem [Kontextschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) verwenden, um die Kontextvariable auszuwählen, nach der verzögert werden soll. Dies überschreibt die im ausgewählten Attribut oder der Eigenschaft festgelegte Tageszeit. Dies ist nützlich, wenn Sie einen Versatz in Tagen oder Wochen anwenden und möchten, dass Nutzer:innen zu einem bestimmten Zeitpunkt weitergehen. Die Zeitzone stammt aus dem Attribut oder der Eigenschaft, oder es wird der Fallback verwendet, wenn keine verfügbar ist.

#### Zeitzonenverhalten für „zu einem bestimmten Zeitpunkt“ {#time-zone-behavior-for-at-specific-time}

Beim Konfigurieren personalisierter Verzögerungen mit der Option **zu einem bestimmten Zeitpunkt** hängt das Zeitzonenverhalten vom Datentyp Ihres Attributs oder Ihrer Kontextvariable ab:

- **String-Datentyp mit Zeitzone:** Wenn das Attribut oder die Kontextvariable ein String-Datentyp ist, der Zeitzoneninformationen enthält, wird die in dem String angegebene Zeitzone verwendet. Zum Beispiel verwendet `2025-06-10T10:00:00-08:00` UTC-8.
- **String-Datentyp ohne Zeitzone:** Wenn das Attribut oder die Kontextvariable ein String-Datentyp ohne Zeitzoneninformationen ist, wird die Fallback-Zeitzone verwendet. Zum Beispiel verwendet `2025-06-10` die Fallback-Zeitzone.
- **Zeit-Datentyp:** Wenn das Attribut oder die Kontextvariable ein Zeit-Datentyp ist, wird UTC verwendet. Dies liegt daran, dass der Zeit-Datentyp beim Speichern in der Datenbank immer in UTC konvertiert wird, sodass „zu einem bestimmten Zeitpunkt“ immer auf UTC verweist, wenn die Variable auf den Zeit-Datentyp gesetzt ist. Zum Beispiel verwendet `2025-06-10T10:00:00-08:00` UTC+0.

{% alert note %}
Es ist möglich, dass ein angepasstes Attribut oder eine Kontextvariable weder eine bestimmte Zeit noch eine Zeitzone hat, wenn es sich um einen String-Datentyp handelt. Bei einem Zeit-Datentyp müssen Sie die Zeit und die Zeitzone angeben. Wenn das angepasste Attribut oder die Kontextvariable jedoch ein „irrelevanter“ String ist (wie „product_name“), verlassen die Nutzer:innen den Canvas.
{% endalert %}

#### Anwendungsfall {#use-case}

Nehmen wir an, Sie möchten Ihre Kund:innen daran erinnern, in 30 Tagen Zahnpasta zu kaufen. Mithilfe einer Kombination aus einem Kontextschritt und einem Verzögerungsschritt können Sie diese Kontextvariable auswählen, nach der verzögert werden soll. In diesem Fall hätte Ihr Kontextschritt die folgenden Felder:

- **Name der Kontextvariable:** product_reminder_interval
- **Datentyp:** Zeit
- **Wert:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![Die Kontextvariable „product_reminder_interval“ und ihr Wert.]({% image_buster /assets/img/context_step1.png %})

Da Sie Ihre Kund:innen in 30 Tagen erinnern möchten, wählen Sie als Nächstes **Bis zu einem bestimmten Tag** als Verzögerungsoption und wählen **Verzögerung personalisieren**, um die Informationen aus Ihrem Kontextschritt zu verwenden. Das bedeutet, dass Ihre Nutzer:innen bis zur ausgewählten Kontextvariable verzögert werden.

## Verzögerungsanalytics {#delay-analytics}

Verzögerungskomponenten verfügen über die folgenden Metriken in der Analytics-Ansicht eines aktiven oder zuvor aktiven Canvas.

| Metrik | Beschreibung |
|---|---|
| *Eingetreten* | Gibt an, wie oft der Schritt betreten wurde. Wenn Ihr Canvas eine erneute Berechtigung hat und ein:e Nutzer:in einen Verzögerungsschritt zweimal betritt, werden zwei Eintritte erfasst. |
| *Zum nächsten Schritt fortgefahren* | Gibt die Anzahl der Eintritte an, die zum nächsten Schritt im Canvas fortgefahren sind. |
| *Canvas verlassen* | Gibt die Anzahl der Eintritte an, die den Canvas verlassen haben und nicht zum nächsten Schritt fortgefahren sind. |
| *Personalisierung fehlgeschlagen* | Gibt an, wie oft eine personalisierte Nachricht oder ein für eine:n Nutzer:in bestimmter Inhalt aus folgenden Gründen nicht zugestellt werden konnte:<br> {::nomarkdown}<ul><li>Der Verzögerungswert liegt in der Vergangenheit</li><li>Der Verzögerungswert liegt mehr als 2 Jahre in der Zukunft</li><li>Der Wert für <b>Nach einer Dauer</b> ist keine Zahl</li><li>Der Wert für <b>Bis zu einem bestimmten Tag</b> ist kein Datum oder kein datumsformatierter String</li></ul>{:/} <br>Weitere Informationen finden Sie unter [Fehler bei fehlgeschlagener Personalisierung](#personaliztion-failed-errors). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verzögerungsanalytics" }

Zeitreihen für diese Analytics sind in der erweiterten Komponentenansicht verfügbar.

## Fehlerbehebung {#troubleshooting}

### Fehler bei der Personalisierung {#personalization-failed-errors}

Wenn Nutzer:innen eine personalisierte Verzögerung nicht triggern, könnte es daran liegen, dass der Kontextschritt, den Sie zur Qualifizierung für den Verzögerungsschritt eingerichtet haben, nicht wie erwartet funktioniert. Wenn eine [Kontextvariable ungültig ist]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#troubleshooting), durchläuft ein:e Nutzer:in Ihren Canvas, ohne dass der Kontext durch den Kontextschritt gesetzt wurde. Dies kann dazu führen, dass sie sich nicht für spätere Schritte in Ihrem Canvas qualifizieren, wie z. B. personalisierte Verzögerungen.

## Fehlerbehebung

### Nutzer:innen in einem Verzögerungsschritt, wenn ein Canvas gestoppt wird {#users-in-a-delay-step-when-a-canvas-is-stopped}

Wenn Sie [einen Canvas stoppen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases), werden Nutzer:innen, die sich bereits in einem Verzögerungsschritt befinden, nicht sofort aus dem Canvas entfernt. Braze plant weiterhin den Abschluss der Verzögerung, aber **es werden keine weiteren Nachrichten gesendet**, solange der Canvas gestoppt ist.

Wenn Sie den Canvas wieder aktivieren, bevor die Verzögerung abgelaufen ist, können die Nutzer:innen planmäßig zum nächsten Schritt voranbringen. Wenn das Verzögerungsfenster bereits abgelaufen ist, während der Canvas gestoppt war, verlassen diese Nutzer:innen den Canvas, anstatt den nächsten Schritt zu erhalten. Beispiele finden Sie unter [Was passiert, wenn Sie einen Canvas stoppen?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) und [Canvases stoppen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).