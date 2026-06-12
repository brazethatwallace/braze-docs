---
nav_title: Home
article_title: Home-Dashboard (ehemals Übersicht)
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt Ihr Home-Dashboard und enthält Definitionen für die auf dieser Seite verfügbaren Statistiken."
tool:
  - Reports

---

# Home-Dashboard {#home-dashboard}

> Die **Home**-Seite im Dashboard bietet Ihnen wichtige Metriken, um die Performance Ihrer App oder Website zu verfolgen und zu verstehen, und gibt Ihnen einen schnellen Überblick über Ihre Nutzerbasis.

Die **Home**-Seite besteht aus zwei Hauptbereichen:
- [Dort weitermachen, wo Sie aufgehört haben](#pick-up-where-you-left-off)
- [Performance-Übersicht](#performance-overview)

![Home-Dashboard in Braze.]({% image_buster /assets/img_archive/home_dashboard.png %})

## Dort weitermachen, wo Sie aufgehört haben {#pick-up-where-you-left-off}

Sie können im Braze-Dashboard dort weitermachen, wo Sie aufgehört haben – mit direktem Zugriff auf Dateien, die Sie kürzlich bearbeitet oder erstellt haben. Dieser Abschnitt erscheint oben auf der **Home**-Seite des Braze-Dashboards.

Sie können kürzlich bearbeitete oder erstellte Campaigns, Canvases und Segmente erneut aufrufen. Jede Karte ist mit Tags versehen, die den Inhaltstyp (Campaign, Canvas, Segment) und den Status (aktiv, Entwurf, archiviert, gestoppt) angeben.

{% alert note %}
Der Abschnitt **Dort weitermachen, wo Sie aufgehört haben** erscheint, nachdem Sie eine Campaign, ein Canvas oder ein Segment bearbeitet oder erstellt haben.
{% endalert %}

![Ein Canvas-Entwurf, ein aktives Segment und ein Campaign-Entwurf im Abschnitt „Dort weitermachen, wo Sie aufgehört haben“.]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## Performance-Übersicht {#performance-overview}

Standardmäßig zeigt der Abschnitt **Performance-Übersicht** die Daten der letzten 30 Tage für alle Apps und Websites an. Alle Metriken werden basierend auf dem ausgewählten Zeitraum berechnet.

![Felder für Zeitraum und App im Home-Dashboard.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

Prozentsätze werden auf Basis des aktuellen Zeitraums im Vergleich zum vorherigen Zeitraum berechnet, mit Ausnahme der *monatlich aktiven Nutzer:innen* (MAU), bei denen der letzte Tag des vorherigen Zeitraums anstelle eines Bereichs verwendet wird.

Wenn Sie beispielsweise Ihren Zeitraum auf **Letzte 7 Tage** setzen und Ihre *täglich aktiven Nutzer:innen* einen prozentualen Anstieg von 1,8 % anzeigen, bedeutet das, dass Sie diese Woche 1,8 % mehr täglich aktive Nutzer:innen hatten als in der Vorwoche.

![]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### Aufschlüsselung anzeigen {#show-breakdown}

Wählen Sie **Show Breakdown** für jede Zeile der Performance-Übersicht, um den Wert jeder Statistik pro Tag für den angegebenen Zeitraum anzuzeigen.

![Aufklappen]({% image_buster /assets/img_archive/home_dashboard_breakdown.png %})

### Performance im Zeitverlauf {#performance-over-time}

Der Graph **Performance Over Time** zeigt den Wert jeder Statistik über den angegebenen Zeitraum für die ausgewählten Apps.

![Der Graph „Performance im Zeitverlauf“ mit Statistiken für neue Nutzer:innen über 30 Tage.]({% image_buster /assets/img/dashboards/performance_over_time.png %})

Sie können Statistiken für folgende Bereiche darstellen:
- Banner
- Content Cards
- Täglich aktive Nutzer:innen
  - (Optional) Aufschlüsselung nach Segment
- E-Mail
- In-App-Nachrichten
- KPI-Formeln
  - Wählen Sie **Manage KPI Formulas**, um eine Formel zu erstellen oder eine bestehende Formel zu bearbeiten.
- LINE
- Monatlich aktive Nutzer:innen (MAU)
- Neue Nutzer:innen
- Push
  - (Optional) Aufschlüsselung nach Segment
- Sitzungen
  - (Optional) Aufschlüsselung nach Segment oder App-Version
- Sitzungen pro Stunde
- Sitzungen pro MAU
- SMS
- Stickiness
- Deinstallationen
  - (Optional) Aufschlüsselung nach Segment
- Nutzer:innen
- Webhooks
- WhatsApp

## Verfügbare Statistiken {#available-statistics}

Im Folgenden finden Sie die Definitionen der verfügbaren Statistiken, wie sie berechnet werden und warum sie für Sie wichtig sein sollten.

### Nutzer:innen {#users}

*Nutzer:innen* ist die Gesamtzahl der in diesem Workspace erstellten Nutzer:innen. Dies umfasst alle Nutzer:innen, die Ihre App oder Website zu irgendeinem Zeitpunkt verwendet haben, sowie diejenigen, die möglicherweise keiner bestimmten App oder Website zugeordnet sind. Diese Zahl gibt den Prozentsatz an, wie viele Ihrer Lifetime-Nutzer:innen als *monatlich aktive Nutzer:innen* (MAU) dargestellt werden, was nützlich ist, um die Nutzerbindung über einen langen Zeitraum zu betrachten.

Ein niedriges MAU-zu-Nutzer:innen-Verhältnis kann darauf hindeuten, dass Sie Ihre Messaging-Kanäle diversifizieren oder Ihre Bemühungen verstärken müssen, passive Nutzer:innen zu erreichen. Weitere Informationen finden Sie in unserem Quick Win zum Thema [Passive Nutzer:innen zurückgewinnen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users/#capture-lapsing-users). Im Allgemeinen wird das MAU-zu-Lifetime-Verhältnis aufgrund von Churn im Laufe der Zeit unweigerlich sinken, aber die Tools von Braze können Ihnen helfen, diesen Effekt zu minimieren, indem sie Nutzer:innen länger engagiert halten.

### Lifetime-Sitzungen {#lifetime-sessions}

*Lifetime-Sitzungen* ist die Gesamtzahl der Sitzungen, die Braze seit der Integration aufgezeichnet hat. Eine Sitzung findet jedes Mal statt, wenn ein:e Nutzer:in die App verwendet oder Ihre Website besucht. Eine genauere Definition, wie Sitzungen pro Plattform definiert werden, finden Sie in den entsprechenden Entwicklerartikeln zum Session-Tracking für
[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android) oder [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web).

### Monatlich aktive Nutzer:innen {#monthly-active-users}

*Monatlich aktive Nutzer:innen* (MAU) ist die Anzahl der Nutzer:innen, die in den letzten 30 Tagen eine Sitzung in Ihrer App oder auf Ihrer Website aufgezeichnet haben. MAU werden nächtlich mit einem rollierenden 30-Tage-Fenster berechnet. MAU geben Ihnen ein gutes Verständnis für den Zustand einer App oder Website über einen längeren Zeitraum, da sie die Schwankungen zwischen Tagen mit unterschiedlicher Nutzungsintensität ausgleichen.

Der Prozentsatz neben der MAU-Zahl zeigt die Veränderung der MAU für diesen Zeitraum im Vergleich zum vorherigen Zeitraum.

$$\text{Change in MAU} = \frac{\text{MAU of last date in range} - \text{MAU of day before start date}}{\text{MAU of day before start date}}$$

#### Regeln zur MAU-Berechnung {#mau-calculation-rules}

MAU-Berechnungen folgen bestimmten Regeln, um eine genaue und konsistente Abrechnung sicherzustellen:

- **Berechnungszeitpunkt**: Wird einmal täglich um 12:05 UTC als 30-Tage-Snapshot berechnet; Zahlen ändern sich nie rückwirkend.
- **Anonyme Profile**: Werden **nur** gezählt, wenn mindestens eine Sitzung protokolliert wurde.
- **Identifizierte Profile**: Werden automatisch gezählt, sobald sie existieren.
- **Verwaiste Profile**: Duplikate, die mit einem anderen Profil zusammengeführt wurden, werden **nicht** gezählt.
- **CSV-Uploads**: Per CSV hochgeladene Nutzer:innen werden nur gezählt, wenn `date_of_first_session` oder `date_of_last_session` angegeben ist oder wenn sie später eine Sitzung protokollieren.
- **API-Löschungen**: Das Löschen von Nutzer:innen über die API aktualisiert die MAU nicht sofort; die Zahl korrigiert sich im nächsten monatlichen Zyklus von selbst.

{% alert note %}
Anonyme Nutzer:innen zählen ebenfalls zu Ihren MAU. Bei Mobilgeräten sind anonyme Nutzer:innen geräteabhängig. Bei Web-Nutzer:innen sind anonyme Nutzer:innen vom Browser-Cache abhängig.
{% endalert %}

#### Beispiel zur MAU-Berechnung {#mau-calculation-example}

Das folgende Beispiel zeigt, wie MAU-Berechnungen bei verschiedenen Nutzeraktionen funktionieren:

| Schritt | Aktion | Sofortige MAU-Änderung | Resultierendes Gesamt |
|---------|--------|------------------------|----------------------|
| 1 | **Anonyme:n Nutzer:in 1** erstellen und eine Sitzung protokollieren | +1 | 1 |
| 2 | **Anonyme:n Nutzer:in 1** identifizieren (Profil wird zu identifiziert konvertiert) | 0 | 1 |
| 3 | **Anonyme:n Nutzer:in 2** erstellen und eine Sitzung protokollieren | +1 | 2 |
| 4 | **Anonyme:n Nutzer:in 2** als **dieselbe Person** wie Nutzer:in 1 identifizieren (Nutzer:in 2 wird verwaist) | –1 | 1 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Beispiel zur MAU-Berechnung" }

MAU-Snapshots werden einmal täglich berechnet und ändern sich nie rückwirkend. In diesem Beispiel bleibt die MAU-Zahl für den Tag nach Schritt 3 dauerhaft bei 2, auch wenn Nutzer:in 2 später verwaist wird. Die MAU-Zahl für die folgenden Tage spiegelt jedoch nur die nicht verwaisten Nutzer:innen wider. Innerhalb eines 30-Tage-Fensters verbraucht dieser Ablauf letztlich 1 MAU, da nur ein:e eindeutige:r, nicht verwaiste:r Nutzer:in übrig bleibt.

### Täglich aktive Nutzer:innen {#daily-active-users}

*Täglich aktive Nutzer:innen* (DAU) zeigt die Anzahl der eindeutigen Nutzer:innen an, die an einem bestimmten Tag mindestens eine Sitzung in Ihrer App oder auf Ihrer Website aufzeichnen. DAU kann eine nützliche Statistik sein, um die tägliche Variabilität der Nutzung Ihrer App oder Website zu untersuchen und Ihre Messaging-Kampagnen so effektiv wie möglich zu gestalten. Beispielsweise könnte die Nutzung Ihrer App an Wochenenden deutlich ansteigen – das würde Ihnen zeigen, dass Sie an diesen Tagen mehr Nutzer:innen mit In-App-Nachrichten erreichen könnten als an Wochentagen.

### Neue Nutzer:innen {#new-users}

*Neue Nutzer:innen* gibt an, wie viele Nutzer:innen, die zuvor noch nie eine Sitzung aufgezeichnet haben, begonnen haben, Ihre App oder Website zu nutzen. Diese Zahl ist die Gesamtzahl neuer Nutzer:innen über den angegebenen Zeitraum. Diese Statistik kann sehr wertvoll sein, um die Effektivität Ihrer Werbemaßnahmen zu verfolgen.

{% alert note %}
Wenn Sie Braze erstmals integrieren, werden alle Nutzer:innen als neue Nutzer:innen angezeigt, da Braze zuvor noch nie eine Sitzung für sie aufgezeichnet hat.

Anders als bei MAU kann die Zahl der *neuen Nutzer:innen* rückwirkend sinken, wenn Braze ein anonymes Profil mit einem identifizierten Profil zusammenführt und das anonyme Profil verwaist. Braze entfernt das verwaiste Profil aus den App-Nutzungssummen, was die Zahl der *neuen Nutzer:innen* für bereits angezeigte Daten senken kann. Informationen zum Verhalten bei der Profilverknüpfung finden Sie unter [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/).
{% endalert %}

{% alert important %}
Nutzer:innen, die mit mehr als einer App verknüpft sind, werden für jede App separat gezählt. Das bedeutet, dass ein:e einzelne:r Nutzer:in mehrfach zur Zahl der *neuen Nutzer:innen* beitragen kann, wenn Sitzungen in verschiedenen Apps Ihres Workspace gestartet werden.
{% endalert %}

### Stickiness {#stickiness}

Der *Stickiness*-Wert ist das Verhältnis von DAU zu MAU eines bestimmten Zeitraums. Im Wesentlichen misst Stickiness den Prozentsatz Ihrer MAU, die täglich zurückkehren.

Wenn der Zeitraum beispielsweise auf 30 Tage eingestellt ist, bedeutet ein Verhältnis von 50 %, dass ein:e aktive:r Nutzer:in die App oder Website im Durchschnitt an 15 von 30 Tagen nutzt, oder dass etwa die Hälfte Ihrer aktiven Nutzer:innen täglich zurückkehrt. Stickiness ist eine wichtige Erfolgsmetrik, da die meisten Nutzer:innen eine App nicht aufgeben, weil sie sie aktiv nicht mögen, sondern weil sie nicht Teil ihrer täglichen Routine geworden ist. Daher können Sie Stickiness als Indikator dafür verwenden, wie gut Sie Ihre Nutzer:innen engagieren.

Der Prozentsatz neben dem Stickiness-Verhältnis zeigt die Veränderung der Stickiness für diesen Zeitraum im Vergleich zum vorherigen Zeitraum.

$$\text{Change in stickiness} = \frac{\text{Stickiness of last period} - \text{Stickiness of this period}}{\text{Stickiness of last period}}$$

Die Zeiträume für „letzter Zeitraum“ und „dieser Zeitraum“ werden durch den von Ihnen ausgewählten Zeitraum bestimmt.

{% alert important %}
Der MAU-Wert wird nächtlich berechnet und erst am nächsten Tag aktualisiert.
{% endalert %}

### Tägliche Sitzungen {#daily-sessions}

*Tägliche Sitzungen* ist die Anzahl der an einem bestimmten Tag aufgezeichneten Sitzungen. Ein Vergleich dieses Werts mit Ihrer DAU-Zahl kann Ihnen zeigen, wie oft Ihre Nutzer:innen die App öffnen oder die Website besuchen an Tagen, an denen sie mindestens eine Sitzung aufzeichnen.

### Tägliche Sitzungen pro MAU {#daily-sessions-per-mau}

*Tägliche Sitzungen pro MAU* ist das Verhältnis von *täglichen Sitzungen* zu MAU an einem bestimmten Tag. Diese Statistik zeigt Ihnen, wie viele Sitzungen pro Tag Sie pro MAU erwarten können. Aggregiert und gemittelt kann Ihnen dies eine Vorstellung von der relativen Häufigkeit geben, mit der Ihre Nutzer:innen Ihre App oder Website nutzen. Wenn Ihre *täglichen Sitzungen pro MAU* beispielsweise durchschnittlich 0,5 betragen, könnten Sie erwarten, dass jede:r MAU etwa alle 2 Tage eine Sitzung aufzeichnet.