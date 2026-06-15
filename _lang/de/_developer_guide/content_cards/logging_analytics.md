---
nav_title: Analytics protokollieren
article_title: Analytics protokollieren
page_order: 1
description: "Dieser Artikel beschreibt, wie Sie Impressionen, Klicks und Ausblendungen manuell protokollieren und das On-Click-Verhalten für Ihre angepassten Content Cards handhaben."
toc_headers: "h2"

---

# Analytics protokollieren {#log-analytics}

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Eindeutige Ausblendungen höher als eindeutige Impressionen {#unique-dismissals-higher-than-unique-impressions}

Wenn *Eindeutige Ausblendungen* die *Eindeutigen Impressionen* übersteigen, hat Ihre angepasste Content-Card-Integration Ausblendungen protokolliert, ohne für dieselben Karten Impressionen zu protokollieren. Die Standard-Content-Card-UI von Braze protokolliert beides automatisch, sodass diese Abweichung nur auftritt, wenn Sie eine angepasste UI verwenden.

Protokollieren Sie jedes Mal eine Impression, wenn Sie eine Karte anzeigen, und protokollieren Sie eine Ausblendung, wenn Nutzer:innen sie ausblenden. Methodennamen und Beispiele finden Sie in den nachfolgenden Plattformabschnitten.

## Fehlende Content-Cards-Analytics {#missing-content-cards-analytics}

Wenn Content Cards in Ihrer App korrekt angezeigt werden, Sie aber durchgehend keine Analytics erhalten (eindeutige Empfänger:innen, Impressionen, Klicks usw.), liegt wahrscheinlich ein Problem mit der SDK-Integration vor.

- **Angepasste Content-Card-Ansichten (Android, iOS, Internet):** Die Standard-Braze-UI protokolliert Impressionen und Klicks auf allen Plattformen automatisch. Wenn Sie eine angepasste Content-Card-Ansicht oder -Implementierung verwenden, müssen Sie die entsprechenden Protokollierungsmethoden explizit in Ihrer Anwendung aufrufen. Weitere Informationen finden Sie unter [Analytics protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) für Ihre Plattform. Stellen Sie bei angepassten Internet-Implementierungen insbesondere sicher, dass das Braze Web SDK geladen ist, prüfen Sie die Browser-Konsole auf Fehler und überprüfen Sie, ob Kartendaten empfangen werden.
- **SDK-Initialisierung und Nutzeridentifikation:** Stellen Sie sicher, dass das SDK vollständig initialisiert ist, bevor Karten angezeigt werden. Ereignisse werden stillschweigend verworfen (nicht in die Warteschlange gestellt), wenn das SDK nicht initialisiert ist, sich im verzögerten Initialisierungsmodus befindet oder DSGVO-deaktiviert ist. Das SDK protokolliert zwar Analytics für anonyme Nutzer:innen, aber Dashboard-Metriken wie „Eindeutige Empfänger:innen“ erfordern eine aufgelöste Nutzeridentität. Rufen Sie daher nach Möglichkeit `changeUser` auf, bevor Karten angezeigt werden.

## Content-Card-ID {#content-card-id}

Jeder Campaign-Versand an eine:n Empfänger:in erzeugt eine neue Content-Card-ID. Wenn dieselbe Nutzer:in die Campaign bei einem späteren Versand erneut erhält, weist Braze eine neue ID zu. Referenzieren Sie die Karten-`id`, wenn Sie Impressionen, Klicks und Ausblendungen in angepassten Implementierungen protokollieren.