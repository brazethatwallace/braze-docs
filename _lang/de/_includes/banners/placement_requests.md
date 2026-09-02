Wenn Sie [Platzierungen in Ihrer App oder Website erstellen]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), sendet Ihre App eine Anfrage an Braze, um Banner-Nachrichten für jede Platzierung abzurufen.

- Sie können bis zu **10 Platzierungen pro Aktualisierungsanfrage** anfordern.
- Für jede Platzierung gibt Braze das **Banner mit der höchsten Priorität** zurück, für das die Nutzer:in berechtigt ist.
- Wenn bei einer Aktualisierung mehr als 10 Platzierungen angefragt werden, werden nur die ersten 10 zurückgegeben; die übrigen werden verworfen.

Beispielsweise könnte eine App in einer Aktualisierungsanfrage drei Platzierungen anfordern: `homepage_promo`, `cart_abandonment` und `seasonal_offer`. Jede Anfrage gibt das für diese Platzierung relevanteste Banner zurück.

#### Rate-Limiting für Aktualisierungsanfragen {#rate-limiting-for-refresh-requests}

Wenn Sie ältere SDK or Software-Development-Kit-Versionen verwenden (vor SWIFT 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 und Flutter 15.0.0), ist nur eine Aktualisierungsanfrage pro Sitzung zulässig.

Wenn Sie neuere Mindest-SDK or Software-Development-Kit-Versionen verwenden (SWIFT 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+ und Flutter 15.0.0+), werden Aktualisierungsanfragen durch einen Token / Textbaustein-Bucket-Algorithmus gesteuert, um übermäßiges Polling zu verhindern:

- Jede Sitzung beginnt mit fünf Aktualisierungs-Token / Textbaustein.
- Die Token / Textbaustein werden mit einer Rate von einem Token / Textbaustein alle 180 Sekunden (3 Minuten) aufgefüllt.

Jeder explizite Aufruf von `requestBannersRefresh` verbraucht ein Token / Textbaustein. Die automatische Aktualisierung, die zu Beginn einer neuen Sitzung oder beim Aufruf von `changeUser` erfolgt, verbraucht kein Token / Textbaustein, da bei dieser Aktualisierung das zuletzt zwischengespeicherte Banner für die jeweilige Nutzer:in veröffentlicht wird. Wenn Sie versuchen, eine Aktualisierung durchzuführen, obwohl keine Token / Textbaustein verfügbar sind, sendet das SDK or Software-Development-Kit die Anfrage nicht und protokolliert einen Fehler, bis ein Token / Textbaustein wieder aufgefüllt ist. Dies ist für Updates während der Sitzung und Event-getriggerte Updates von Bedeutung. Um dynamische Updates durchzuführen (beispielsweise nachdem eine Nutzer:in eine Aktion auf derselben Seite abgeschlossen hat), rufen Sie die Aktualisierungsmethode auf, nachdem das angepasste Event protokolliert wurde. Beachten Sie jedoch die erforderliche Verzögerung, die Braze benötigt, um das Event zu erfassen und zu verarbeiten, bevor die Nutzer:in für eine andere Banner-Campaign qualifiziert ist.