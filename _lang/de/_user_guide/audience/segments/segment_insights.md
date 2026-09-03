---
nav_title: Segment-Insights
article_title: Segment-Insights
page_order: 6
page_type: tutorial
tool:
  - Segments
  - Reports
description: "Dieser Artikel zeigt Ihnen, wie Sie Segment-Insights verwenden, interpretieren und teilen können."
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Segment-Insights {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordersegment-insights}

> Erfahren Sie, wie Sie Segment-Insights verwenden, interpretieren und teilen können.

Segment-Insights zeigen Ihnen, wie ein Segment im Vergleich zu einem anderen anhand einer Reihe vorausgewählter KPIs abschneidet.

## Segment-Insights anzeigen {#viewing-segment-insights}

Navigieren Sie zur Seite **Segment-Insights** in Ihrem Dashboard unter **Analytics**, um bis zu 10 verschiedene Segmente mit einem Basissegment zu vergleichen.

![Segment-Insights-Dashboard, das drei Segmente „UK Users“, „FR Users“ und „CA Users“ mit einem Basissegment „All Users“ vergleicht.]({% image_buster /assets/img_archive/segment_insights.png %})

{% alert note %}
Die Statistiken auf der Segment-Insights-Seite werden standardmäßig geschätzt. Um exakte Werte zu berechnen, öffnen Sie ein Segment und wählen Sie **Exakte Statistiken berechnen** aus. Schätzungen können höher oder niedriger als die exakten Werte sein, insbesondere in großen Workspaces oder bei kleinen Segmenten.
{% endalert %}

Das Basissegment kann entweder ein bestimmtes Segment sein, das Sie auswählen, oder ein Segment, das alle Ihre Nutzer:innen enthält. Sie können die folgenden Statistiken mithilfe von Segment-Insights vergleichen:

| Messgröße | Beschreibung | Formel |
| --------------------- | ------------- | ------------- |
| Sitzungen pro Tag | Durchschnittliche Anzahl der Sitzungen pro Tag für Nutzer:innen des Segments | (Gesamtanzahl der Sitzungen) / (Anzahl der Tage seit der ersten Sitzung) |
| Tage seit der ersten Sitzung | Durchschnittliche Anzahl der Tage zwischen der ersten Sitzung der Nutzer:innen des Segments und heute | heute – Datum der ersten Sitzung |
| Tage seit der letzten Sitzung | Durchschnittliche Anzahl der Tage zwischen der letzten Sitzung der Nutzer:innen des Segments und heute | heute – Datum der letzten Sitzung |
| Lifetime-Umsatz in Dollar | Durchschnittlicher Lifetime-Umsatz in Dollar für Nutzer:innen des Segments | Lifetime-Ausgaben der Nutzer:innen |
| Tage seit dem ersten Kauf | Durchschnittliche Anzahl der Tage zwischen der ersten Sitzung und dem ersten Kauf der Nutzer:innen des Segments | Datum des ersten Kaufs – Datum der ersten Sitzung |
| Tage seit dem letzten Kauf | Durchschnittliche Anzahl der Tage zwischen dem letzten Kauf der Nutzer:innen des Segments und heute | heute – Datum des letzten Kaufs |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segment-Insights anzeigen" }

Sie können bestimmte Vergleiche ganz einfach über die eindeutige URL der Seite mit Ihren Teammitgliedern teilen. Außerdem können Sie das Augensymbol neben jedem Segment auswählen, um weitere Informationen zu diesem Segment anzuzeigen. Diese Vergleiche werden zurückgesetzt, wenn Sie zwischen Workspaces wechseln.

![Details für das Segment „Premium Users (iOS VideoApp)“ mit einem Diagramm zur historischen Mitgliedschaft und einem Chart, das die geschätzte Größe für verschiedene Messaging-Kanäle aufschlüsselt.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Seite „Segmentdetails“ {#segment-details-page}

Segment-Insights wurden auch direkt in die Ansicht **Segmentdetails** integriert. Wenn Sie ein bestimmtes Segment betrachten, das Sie zuvor eingerichtet haben, finden Sie dieselben sechs Statistiken in der dynamischen, grauen Box „Segmentstatistiken“. Von hier aus können Sie das Segment-Insights-Tool schnell starten, um dieses bestimmte Segment mit beliebigen anderen zuvor eingerichteten Segmenten zu vergleichen. Beachten Sie jedoch, dass dadurch alle Segmente überschrieben werden, die Sie zuvor im Segment-Insights-Tool ausgewählt haben.

{% alert note %}
[Segment-Insights](#viewing-segment-insights) und die Seite **Segmentdetails** berechnen Größenschätzungen separat mit unterschiedlichen Nutzerstichproben und Stichprobengrößen, sodass Abweichungen zwischen den Zahlen zu erwarten sind.
{% endalert %}

![Segment-Insights wurden auch direkt in die Ansicht „Segmentdetails“ integriert. Wenn Sie ein bestimmtes Segment betrachten, das Sie zuvor eingerichtet haben, finden Sie dieselben sechs Statistiken in der dynamischen, grauen Box „Segmentstatistiken“. Von hier aus können Sie das Segment-Insights-Tool schnell starten, um dieses bestimmte Segment mit beliebigen anderen zuvor eingerichteten Segmenten zu vergleichen. Beachten Sie jedoch, dass dadurch alle Segmente überschrieben werden, die Sie zuvor im Segment-Insights-Tool ausgewählt haben.]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Anwendungsfälle {#insights-use-cases}

### Vergleich von demografischer Nutzung und Kaufmustern {#comparing-demographic-usage-and-purchasing-patterns}

Einer der besten Einsatzbereiche von Segment-Insights ist die Beantwortung von Fragen zur Auswirkung der Nutzerdemografie auf die App-Nutzung und die Campaign-Effektivität, wie zum Beispiel:

- Schneiden bestimmte Nutzerdemografien deutlich besser oder schlechter ab als der Durchschnitt?
- Sollte ich die Lokalisierung einer bestimmten Campaign überdenken?
- Spricht eine Campaign eine bestimmte Zielgruppe an?
- Welche Ziele sollte ich für eine Campaign festlegen, die auf eine bestimmte Zielgruppe ausgerichtet ist?

Segment-Insights können helfen, Unterschiede zwischen Nutzerdemografien aufzudecken. Das folgende Beispiel zeigt einen Vergleich der Nutzerbasis einer App nach Sprache und veranschaulicht, wie englischsprachige Nutzer:innen tendenziell einen höheren LTV und höhere Aktivitätslevel aufweisen als Nutzer:innen anderer Sprachen.

![Segment-Insights-Aufschlüsselung für Segmente nach Englisch, Deutsch, Französisch und Spanisch.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

In diesem Beispiel haben sich deutschsprachige Nutzer:innen im Durchschnitt vor längerer Zeit registriert, was erklären könnte, warum sie nicht mehr so aktiv sind. Dies könnte auf eine Vielzahl von Faktoren zurückzuführen sein. Zum Beispiel könnte die App zuerst in Europa gestartet sein, aber mittlerweile in den USA beliebter sein, wo die meisten Menschen Englisch oder Spanisch sprechen. Für belastbarere Ergebnisse ist es bei der Analyse von KPIs über Demografien hinweg sinnvoll, die Erkenntnisse aus einer allgemeinen demografischen Studie (z. B. ob die Sprache den LTV bei allen Nutzer:innen beeinflusst) zu testen, indem man eine kleinere, ähnlichere Population betrachtet und prüft, ob die Ergebnisse bestehen bleiben.

Um die Conversions bei Nutzer:innen anderer Sprachen als Englisch zu verbessern, wäre ein guter erster Schritt, [Campaigns zu lokalisieren]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) und an die Gerätesprache der Nutzer:innen anzupassen. Stellen Sie außerdem sicher, dass der Text dieser Nachrichten die Nutzer:innen anspricht, indem Sie eine [multivariate Campaign]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) verwenden, um verschiedene Versionen des fremdsprachigen Textes zu testen.

### Indikatoren für höheren Umsatz verstehen {#understanding-indicators-of-higher-revenue}

Nutzer:innen zum Kauf zu bewegen, kann schwierig sein, und der Versuch, neue, inaktive oder nicht engagierte Nutzer:innen direkt zum Kauf zu drängen, kann dazu führen, dass sie Ihre App deinstallieren. Segment-Insights können Ihnen helfen, Aktionen zu entdecken, die Nutzer:innen weiter im Kauf-Funnel voranbringen, ohne dass sie sofort kaufen müssen – zum Beispiel das Abonnieren Ihres Newsletters, das Teilen in Social Media oder die Anmeldung für Werbenachrichten. Sie können beispielsweise die Auswirkungen verschiedener Verhaltensweisen innerhalb einer E-Commerce-App auf Käufe darstellen.

![Segment-Insights-Aufschlüsselung für Nutzer:innen, die in Social Media geteilt, sich für Aktionen angemeldet und den Newsletter abonniert haben.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

In diesem Fall sind derzeit relativ wenige Nutzer:innen für Werbenachrichten angemeldet und nicht so aktiv, aber diese Nutzer:innen generieren einen höheren Lifetime-Umsatz. Um den Umsatz zu steigern, könnte es eine gute Idee sein, eine Einladung zur Anmeldung für Werbenachrichten in Onboarding-Campaigns aufzunehmen. Um inaktive Nutzer:innen erneut zu aktivieren, wäre ein guter Plan, eine typische [Campaign für inaktive Nutzer:innen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users) zu versenden und [Nutzer:innen, die konvertiert haben]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#converted-from-campaign), mit einer anschließenden Campaign zur Anmeldung für Werbenachrichten anzusprechen.