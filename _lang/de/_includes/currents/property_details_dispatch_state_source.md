<ul>
<li><code>dispatch_id</code> ist eine ID für einen bestimmten Nachrichtenversand, beispielsweise den Versand einer Campaign. Alle Push-Ereignisse, die aus demselben Versand stammen, enthalten dieselbe <code>dispatch_id</code>. Verwenden Sie <code>dispatch_id</code>, um Ereignisse zu gruppieren, die zum selben Versand gehören. So können Sie den Lebenszyklus der Push-Nachricht für diesen Versand (z. B. Senden, Bounce und Öffnung) gruppieren und korrelieren.</li>
<li><code>state_change_source</code> gibt einen String mit dem vollständigen Quellennamen zurück. Beispielsweise gibt die Quelle CSV-Import den String <code>CSV import</code> zurück. Die verfügbaren Quellen sind im Folgenden aufgeführt:</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>Quelle</th><th>Beschreibung</th></tr>
</thead>
<tbody>
<tr><td>SDK or Software-Development-Kit</td><td>SDK or Software-Development-Kit-Endpunkte</td></tr>
<tr><td>Dashboard</td><td>Wenn der Abo-Status einer Nutzerin oder eines Nutzers über die Kundenprofil or Nutzerprofil-Seite im Dashboard aktualisiert wird</td></tr>
<tr><td>Abo-Seite</td><td>Wenn sich Nutzer:innen über einen E-Mail-Link abmelden, der nicht das Einstellungscenter ist</td></tr>
<tr><td>Representational State Transfer API</td><td>Representational State Transfer-API-Endpunkte</td></tr>
<tr><td>CSV-Import</td><td>CSV-Nutzerimport</td></tr>
<tr><td>Einstellungscenter</td><td>Wenn Nutzer:innen über das Einstellungscenter aktualisiert werden</td></tr>
<tr><td>Eingehende Nachricht</td><td>Wenn Nutzer:innen durch eingehende Nachrichten von Endnutzer:innen über Kanäle wie Kurzmitteilungsdienst or SMS aktualisiert werden</td></tr>
<tr><td>Migration</td><td>Wenn Nutzer:innen durch interne Migrationen oder Wartungsskripte aktualisiert werden</td></tr>
<tr><td>Nutzerzusammenführung</td><td>Wenn Nutzer:innen durch den Prozess der Nutzerzusammenführung aktualisiert werden</td></tr>
<tr><td>Canvas-Schritt „Nutzeraktualisierung“</td><td>Wenn Nutzer:innen durch den Canvas-Schritt „Nutzeraktualisierung“ aktualisiert werden</td></tr>
</tbody>
</table>