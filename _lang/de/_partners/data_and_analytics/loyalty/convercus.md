---
nav_title: Convercus
article_title: Convercus
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Convercus, einer Loyalty- und Coupon-Plattform, die Braze mit Echtzeit-Loyalty-Daten anreichert und es Braze-Campaigns ermöglicht, Loyalty-Aktionen in Convercus auszulösen."
page_type: partner
search_tag: Partner
---

# Convercus

> [Convercus](https://www.convercus.com/en) ist eine SaaS-Loyalty- und Coupon-Plattform, die Marken und Händlern hilft, Kundenfrequenz, Warenkorbwert und Wiederkaufsraten durch Omnichannel-Kundenbindungs-Programme und personalisierte Coupon-Kampagnen zu steigern.

_Diese Integration wird von Convercus gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Convercus ist bidirektional: Kundenbindungsdaten fließen in Echtzeit als angepasste Attribute, angepasste Events und Käufe in Braze ein, und Braze-Canvases und Campaigns können über Webhooks Kundenbindungsaktionen in Convercus triggern. Verwenden Sie synchronisierte Mitgliedsstufen, Punktestände, Käufe und Coupon-Aktivitäten in Segments, Liquid und Connected-Content. Aus Braze-Journeys heraus können Sie außerdem Coupons zuweisen, Punktetransaktionen buchen, sammeln und einlösen sowie E-Mail-Abo-Einstellungen in Convercus aktualisieren.

Convercus hostet die Integration, sodass Sie keine zusätzliche Infrastruktur installieren müssen. Während die meisten Kundenbindungs-Konnektoren Daten nur in eine Richtung übertragen, schließt Convercus den Kreislauf: Reagieren Sie in Braze auf ein Kundenbindungs-Event, führen Sie eine Aktion in Convercus aus und messen Sie das Ergebnis direkt in Braze.

## Anwendungsfälle {#use-cases}

* **Stufenaufstiegs-Feier:** Wenn ein Mitglied in Convercus eine Treuestufe aufsteigt, lösen Sie ein personalisiertes Braze-Canvas mit einer Willkommensnachricht, einem stufenexklusiven Vorteil sowie der neuen Stufe und dem Punktestand des Mitglieds aus.
* **Geburtstags- und Meilenstein-Boni:** Buchen Sie aus einer Braze-Journey heraus Bonuspunkte in Convercus zum Geburtstag oder Jubiläum eines Mitglieds und senden Sie anschließend eine Glückwunschnachricht, die den neuen Kontostand bestätigt.
* **Rückgewinnung inaktiver Mitglieder:** Lassen Sie Braze für inaktive Mitglieder über einen Webhook einen personalisierten Coupon in Convercus zuweisen und über E-Mail, Push und In-App Messages zustellen.
* **Live-Punktestand in Nachrichten:** Nutzen Sie Connected-Content, um den Realtime-Punktestand eines Mitglieds per Braze-Liquid abzurufen und so Kommunikationskadenz wie „Ihnen fehlen nur noch X Punkte bis zu Ihrer nächsten Prämie“ zu ermöglichen.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
| --- | --- |
| Ein Convercus-Konto | Ein aktives Convercus-Programm. Kontaktieren Sie Ihren Convercus Account Manager, wenn Sie noch kein:e Kund:in sind. |
| Ein Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit der Berechtigung `users.track`. Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Ein Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

Sie benötigen einen konsistenten Nutzerbezeichner zwischen den Systemen: Der Wert, der in Braze als `external_id` (oder als gewählter Bezeichnertyp) verwendet wird, muss mit dem entsprechenden Mitgliedsbezeichner in Convercus übereinstimmen. Andernfalls werden Events nicht dem richtigen Profil zugeordnet.

## Integration

### Schritt 1: Braze in Convercus Selfservice konfigurieren {#step-1-configure-braze-in-convercus-selfservice}

Öffnen Sie in Convercus Selfservice (der kundenorientierten Admin-Oberfläche – öffnen Sie sie über die URL, die Ihr Convercus Account Manager bereitstellt) das Programm, das Sie mit Braze verbinden möchten, und verwenden Sie die **Braze-Integrationskarte**, um:

1. Die Braze-Verbindung zu konfigurieren, indem Sie das Integrationsformular ausfüllen:

   | Feld | Beschreibung |
   | --- | --- |
   | `apiKey` | Ihr Braze-REST-API-Schlüssel (mit der Berechtigung `users.track`). |
   | `apiEndpoint` | Ihr Braze-REST-Endpunkt, zum Beispiel `https://rest.iad-01.braze.com`. |
   | Bezeichnertyp | Entweder `external_id` oder `user_alias`. Bestimmt, wie Convercus-Mitglieder mit Braze-Nutzerprofilen abgeglichen werden. |
   | `defaultOptins` | Mehrfachauswahl der Opt-in-Kanäle des Programms (aus `membershipOptins`). Wird als Standard für den E-Mail-Abo-Webhook verwendet, wenn die Anfrage `optins` nicht enthält. Die Braze-Konfiguration gilt als unvollständig, bis mindestens einer ausgewählt ist. |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1: Braze in Convercus Selfservice konfigurieren" }

2. Einen API-Schlüssel für eingehende Aufrufe erstellen. Erstellen Sie pro Programm eine `X-Convercus-Key`-Zugangsdaten. Der Rohschlüssel wird bei der Erstellung einmalig angezeigt, mit dem Präfix `cvc_` (Format: `cvc_<base64url>`). Speichern Sie ihn in Braze, wenn Sie die Webhook-Campaigns und Connected-Content-Blöcke in Schritt 2 konfigurieren. Schlüssel können jederzeit über dieselbe Karte widerrufen werden; der Widerruf wird sofort wirksam.

Nachdem Sie die Braze-Verbindung gespeichert haben, beginnt Convercus sofort mit dem Streaming von Loyalty-Events für dieses Programm an Braze. Es ist kein zusätzlicher Infrastrukturaufbau erforderlich.

{% alert note %}
Jedes Convercus-Programm wird unabhängig konfiguriert. Ein einzelner Convercus-Mandant kann verschiedene Programme mit verschiedenen Braze-Workspaces verbinden, jeweils mit eigenem API-Schlüssel.
{% endalert %}

### Schritt 2: Webhooks in Braze konfigurieren {#step-2-configure-webhooks-in-braze}

Um Convercus-Aktionen aus einem Canvas oder einer Campaign auszulösen, erstellen Sie Braze-Webhook-Aktionen, die den Convercus-Integrationsdienst aufrufen. Alle Anfragen müssen die folgenden Header enthalten:

- `X-Convercus-Key: cvc_…` – der in Schritt 1 generierte API-Schlüssel.
- `Content-Type: application/json`

Alle Endpunkte befinden sich unter der Basis-URL `<SERVICE_HOST>/v1/programs/{programId}`. Ersetzen Sie `<SERVICE_HOST>` durch den von Ihrem Convercus Account Manager bereitgestellten Host und `{programId}` durch Ihre Convercus-Programm-ID.

| Aktion | Endpunkt |
| --- | --- |
| Einem Mitglied einen Coupon zuweisen | `POST /campaigns/{couponId}/assign` — gibt `{ "couponCode": "..." }` zurück. |
| Mehreren Mitgliedern einen Coupon zuweisen | `POST /campaigns/{couponId}/assign/batch` — bis zu 500 Mitglieder in einem Aufruf; der Body akzeptiert optionale `valid_from` / `valid_to`. Gibt `{ "batchId": "..." }` zurück. |
| Punkte verdienen / einlösen buchen | `POST /members/{accountId}/bookings` — erstellt ein `EARNBOOKING` oder `BURNBOOKING` auf einem Mitgliedskonto. Gibt `{ "bookingId": "..." }` zurück. |
| E-Mail-Abo-Einstellungen synchronisieren | `POST /subscriptions/email` — setzt die Opt-ins des Mitglieds auf `allowed` oder `declined`. Opt-in-Kanäle werden aufgelöst als Anfrage `optins` > `defaultOptins`. Gibt `200` (alles OK), `207` (teilweise — siehe `succeeded` / `failed`) oder `400` (unbekannte Opt-ins oder keine konfiguriert) zurück. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Webhooks in Braze konfigurieren" }

Beispiel — einem Mitglied einen Coupon zuweisen:

{% raw %}
```text
POST <SERVICE_HOST>/v1/programs/{programId}/campaigns/{couponId}/assign
X-Convercus-Key: cvc_…
Content-Type: application/json

{
  "account_id": "{{custom_attribute.${convercus_account_id}}}",
  "braze_campaign_id": "{{campaign.${api_id}}}"
}
```
{% endraw %}

Die anderen Aktionen folgen demselben Muster und ändern nur den Endpunkt und den Body. Beispielsweise sendet eine Punktebuchung an `/members/{accountId}/bookings` mit `booking_type` (`EARNBOOKING` oder `BURNBOOKING`), `booking_type_code`, `points` und `reason`; der E-Mail-Abo-Webhook sendet an `/subscriptions/email` mit `account_id` und `status` (`allowed` oder `declined`).

#### Fehlerantworten und Wiederholungsversuche {#error-responses-and-retries}

| Status | Bedeutung |
| --- | --- |
| `200` | Erfolg. |
| `207` | Multi-Status — nur für den E-Mail-Abo-Webhook, wenn einige Mitgliedschaften aktualisiert wurden und andere fehlgeschlagen sind. |
| `400` | Validierung des Anfrage-Bodys fehlgeschlagen. |
| `401` | `X-Convercus-Key` fehlt oder ist ungültig. |
| `5xx` | Der vorgelagerte Convercus-Aufruf ist fehlgeschlagen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerantworten und Wiederholungsversuche" }

{% alert warning %}
5xx-Antworten sind nicht sicher für Wiederholungsversuche ohne Erfolgsbestätigung — diese Operationen sind nicht idempotent, und Wiederholungen können Coupons doppelt zuweisen oder Punktebuchungen doppelt gutschreiben. Deaktivieren Sie die automatische Wiederholung von Braze bei 5xx für diese Webhooks oder konfigurieren Sie eine sehr niedrige maximale Anzahl von Wiederholungsversuchen.
{% endalert %}

### Schritt 3: Daten in Braze überprüfen {#step-3-verify-data-in-braze}

1. Lösen Sie ein Loyalty-Event in Convercus aus — zum Beispiel eine Statusstufenänderung, eine Punkte-Transaktion oder eine Coupon-Einlösung.
2. Öffnen Sie die:den entsprechende:n Nutzer:in in Braze und bestätigen Sie, dass das erwartete angepasste Attribut, angepasste Event oder der Kauf im Profil erscheint. Nutzer:innen werden über `external_id` (oder den in Schritt 1 gewählten Bezeichnertyp) abgeglichen.
3. Um die Gegenrichtung zu überprüfen, führen Sie einen Braze-Testversand durch, der einen der Webhooks aus Schritt 2 aufruft, und bestätigen Sie die Aktion in Convercus (Coupon zugewiesen, Punkte gebucht oder Abo aktualisiert).

## Convercus mit Braze verwenden {#use-convercus-with-braze}

### Schritt 1: Nachrichten mit synchronisierten Kundenbindungsdaten personalisieren {#step-1-personalize-messages-with-synced-loyalty-data}

Sobald die Integration aktiv ist, treffen Convercus-Events über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt auf jedem Nutzerprofil in Braze ein und können wie alle anderen nativen Daten verwendet werden:

1. Verwenden Sie angepasste Attribute für Kundenbindung (zum Beispiel `convercus_status_level`, `convercus_balance`) in **Segments**, um Stufeninhaber:innen, Mitglieder mit hohem Punktestand oder kürzlich herabgestufte Nutzer:innen anzusprechen.
2. Verwenden Sie angepasste Events (zum Beispiel `convercus_status_level_changed`, Coupon- und Mitgliedschafts-Events) als **Trigger-Schritte** in Canvas oder als Filter in Campaigns zur erneuten Interaktion.
3. Referenzieren Sie beliebige dieser Felder in **Liquid** für die Personalisierung innerhalb von Nachrichten (Betreffzeilen, Textkörper, Push-Titel).
4. Verwenden Sie `purchase`-Events, die von Convercus gestreamt werden, um produktbezogene Journeys auszulösen (Nachbestellung, Kategorie-Upselling, Bewertungsanfragen nach dem Kauf).

#### Angepasste Attribute {#custom-attributes}

| Attribut | Beschreibung |
| --- | --- |
| `convercus_account_id` | Die Convercus-Konto-ID des Mitglieds – eindeutig innerhalb eines Convercus-Programms / Braze-Workspace. |
| `convercus_user_id` | Die Convercus-Nutzer-ID, die die zugrunde liegende Person über mehrere Convercus-Programme hinweg identifiziert. |
| `convercus_partner_id` | Bezeichner des Convercus-Partners (Händler/Marke), über den sich dieses Mitglied registriert hat. Nützlich für die Segmentierung in Koalitionsprogrammen. |
| `convercus_member_role` | Die Rolle des Mitglieds innerhalb des Kundenbindungs-Programms. |
| `convercus_status_level` | Die aktuelle Stufe oder der Statuslevel des Mitglieds. |
| `convercus_balance` | Objekt mit den aktuellen `points`, `lockedPoints` und `statusPoints` des Mitglieds. |
| `email_subscribe` | E-Mail-Abo-Status, abgeleitet aus Convercus-Opt-ins (`opted_in`, `subscribed` oder `unsubscribed`). |
| `push_subscribe` | Push-Abo-Status, abgeleitet aus Convercus-Push-Token-Events (`opted_in` oder `unsubscribed`). |
| Standard-Profilfelder | `email`, `phone`, `first_name`, `last_name`, `dob`, `gender`, `home_city`, `country`. |
| Angepasste Nutzereigenschaften | Alle angepassten Eigenschaften, die auf dem Convercus-Nutzerobjekt definiert sind, werden als angepasste Braze-Attribute weitergeleitet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angepasste Attribute" }

{% alert note %}
Innerhalb eines Braze-Workspace werden Mitglieder eindeutig durch `convercus_account_id` identifiziert. `convercus_user_id` identifiziert die zugrunde liegende Person über mehrere Convercus-Programme hinweg und wird für programmübergreifende Analytics bereitgestellt. Für die Segmentierung innerhalb von Braze verwenden Sie `convercus_account_id`.
{% endalert %}

**`email_subscribe`-Abbildung**

| Convercus-Status | Braze `email_subscribe` |
| --- | --- |
| `allowedOptins`-Eintrag für `email consent` oder `newsletter` | `opted_in` |
| `declinedOptIns`-Eintrag für diese Kanäle (und kein zulässiger Eintrag) | `unsubscribed` |
| Kein Eintrag in beide Richtungen | `subscribed` (Braze-Standardwert) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="email_subscribe-Abbildung" }

#### Angepasste Events {#custom-events}

| Event | Wird ausgelöst, wenn |
| --- | --- |
| `convercus_account_created` | Ein neues Konto in Convercus erstellt wird. |
| `convercus_membership_added` | Ein bestehendes Konto einem Kundenbindungs-Programm beitritt. |
| `convercus_membership_created` | Eine neue Mitgliedschaft erstellt wird. |
| `convercus_membership_changed` | Sich die Daten einer Mitgliedschaft ändern. |
| `convercus_membership_optins_changed` | Sich die Opt-in-Einstellungen eines Mitglieds ändern. |
| `convercus_membership_terminated` | Eine Mitgliedschaft endet. |
| `convercus_status_level_changed` | Sich die Stufe oder der Statuslevel eines Mitglieds ändert. |
| `convercus_balance_changed` | Sich der Punktestand eines Mitglieds ändert. |
| `convercus_account_transaction` | Eine Kundenbindungs-Transaktion bewertet wird. |
| `convercus_coupon_assigned` | Dem Mitglied ein Coupon zugewiesen wird. |
| `convercus_coupon_redeemed` | Das Mitglied einen Coupon einlöst. |
| `convercus_user_logged_in` | Sich das Mitglied bei einer Convercus-gestützten Oberfläche anmeldet. |
| `convercus_user_logged_out` | Sich das Mitglied abmeldet. |
| `convercus_user_created` | Ein:e neue:r Nutzer:in erstellt wird. |
| `convercus_user_changed` | Sich die Profildaten einer/eines Nutzer:in ändern. |
| `convercus_push_token_created` | Ein Push-Token für das Mitglied registriert wird. |
| `convercus_push_token_deleted` | Ein Push-Token entfernt wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angepasste Events" }

#### Käufe {#purchases}

Convercus-Transaktionen vom Typ `EARNTRANSACTION` (Punkte, die durch Kundenausgaben verdient werden) werden an Braze als [Käufe]({{site.baseurl}}/api/objects_filters/purchase_object) gemeldet und in Braze-Umsatz-Analytics, RFM-Segmentierung und prädiktiven Features berücksichtigt – wobei die Transaktions-ID als Produktbezeichner und der Transaktionsbetrag sowie die Währung als Preis und Währung verwendet werden.

Transaktionen vom Typ `PAYWITHPOINTSTRANSACTION` (Punkteeinlösung) werden **nicht** als Käufe gemeldet – sie fließen als angepasstes Event `convercus_account_transaction` ein, sodass sie für die Segmentierung verfügbar bleiben. Stornierungen und Rückbuchungen von Earn-Transaktionen werden als Käufe mit negativem Preis gemeldet, um den Braze-Umsatz mit Convercus abzugleichen.

### Schritt 2: Live-Kundenbindungsdaten mit Connected Content abrufen {#step-2-fetch-live-loyalty-data-with-connected-content}

Für Werte, die zum Sendezeitpunkt aktuell sein müssen – aktueller Punktestand, aktive Coupons, neueste Stufe – rufen Sie Convercus über [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) aus Braze auf, anstatt sich auf das zuletzt synchronisierte Attribut zu verlassen. Beide Endpunkte befinden sich unter derselben Basis-URL wie die Webhooks und erfordern den `X-Convercus-Key`-Header.

| Daten | Endpunkt | Gibt zurück |
| --- | --- | --- |
| Mitgliedsprofil | `GET /members/{accountId}/profile` | `member_id`, `first_name`, `last_name`, `email`, `tier_name`, `tier_id`, `points_balance`, `enrollment_date`. |
| Mitglieds-Coupons | `GET /members/{accountId}/coupons` | Liste aktiver, einlösbarer Coupons (Status, Wert, Gültigkeitszeitraum, Titel, Beschreibung). Hängen Sie `?lang=<code>` an (zum Beispiel `?lang=de`), um `title`/`description` zu lokalisieren; Standard ist `en`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 2: Live-Kundenbindungsdaten mit Connected Content abrufen" }

Connected-Content-Endpunkte geben bei erwarteten Fehlern immer HTTP 200 zurück, sodass Liquid-Templates anhand des `error`-Felds verzweigen können:

| Antwort | Bedeutung |
| --- | --- |
| `200` + Payload | Erfolg. |
| `200 { "error": "member_not_found" }` | Das Konto existiert in diesem Programm nicht. |
| `200 { "error": "internal_error" }` | Upstream- oder unerwarteter Fehler. |
| `401` | `X-Convercus-Key` fehlt oder ist ungültig (bei der Integration behandeln, nicht in Liquid). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Live-Kundenbindungsdaten mit Connected Content abrufen" }

Beispiel – den Kundenbindungsstatus eines Mitglieds rendern (Stufe, Punkte und aktive Angebote):

{% raw %}
```liquid
{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/profile
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 300
  :retry
  :save member
%}

{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/coupons?lang=en
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 0
  :retry
  :save coupon_data
%}

{% unless member.error %}
  <h2>Your Loyalty Status</h2>
  <p>Hi {{member.first_name}}, you're a <strong>{{member.tier_name}}</strong> member.</p>
  <p>Points balance: <strong>{{member.points_balance}}</strong></p>

  {% if coupon_data.coupons.size > 0 %}
    <h3>Your Active Offers</h3>
    {% for coupon in coupon_data.coupons %}
      <p><strong>{{coupon.title}}</strong> — valid until {{coupon.valid_to}}</p>
    {% endfor %}
  {% endif %}
{% endunless %}
```
{% endraw %}

Umschließen Sie Connected Content immer mit Bedingungen (prüfen Sie `member.error` und leere `coupons`), damit ein vorübergehender Lookup-Fehler niemals eine fehlerhafte Nachricht versendet. Cachen Sie das Profil (`cache_max_age 300`), aber nicht die Coupons (`cache_max_age 0`), da sich der Coupon-Status zwischen den Sendungen ändern kann.

## Überlegungen {#considerations}

- **Latenz:** Convercus-zu-Braze-Events werden über Kafka weitergeleitet und erreichen Braze unter normaler Last innerhalb von Sekunden.
- **Braze-Rate-Limits:** Die Integration wiederholt Anfragen bei `429`-Antworten automatisch und berücksichtigt dabei den `x-ratelimit-retry-after`-Header von Braze mit exponentiellem Backoff.
- **Connected-Content-Caching:** Braze speichert Connected-Content-Antworten standardmäßig für mehrere Minuten im Cache. Für Werte, die zum Sendezeitpunkt exakt sein müssen (z. B. Punktestand), verkürzen oder umgehen Sie das Cache-Fenster im Connected-Content-Aufruf.
- **Eine Konfiguration pro Programm:** Jedes Kundenbindungs-Programm wird einem einzelnen Braze-Workspace zugeordnet. Um einen zweiten Workspace zu verbinden, konfigurieren Sie ihn in einem separaten Programm.
- **Observability:** API-Aufrufstatistiken und Fehlerverlauf pro Programm (in beide Richtungen) werden 90 Tage lang aufbewahrt und sind über die Braze-Integrationskarte im Selfservice verfügbar.

## Fehlerbehebung {#troubleshooting}

- **Events erscheinen nicht in Braze:** Überprüfen Sie, ob der als Bezeichner verwendete Wert (ausgewählt in Schritt 1) mit der `external_id` (oder dem gewählten Bezeichnertyp) der Nutzer:innen in Braze übereinstimmt. Nicht übereinstimmende Bezeichner führen dazu, dass Events dem falschen Profil zugeordnet oder verworfen werden.
- **Webhook gibt `401` zurück:** Der `X-Convercus-Key`-Header fehlt oder der `cvc_…`-API-Schlüssel wurde widerrufen. Generieren Sie den Schlüssel im Selfservice neu und aktualisieren Sie die Webhook-Aktion in Braze.
- **Webhook gibt `400` zurück:** In der Anfrage fehlt `Content-Type: application/json`, oder der Payload entspricht nicht dem dokumentierten Schema. Beim E-Mail-Abo-Webhook bedeutet ein `400` auch, dass die angeforderten Opt-ins dem Programm unbekannt sind oder keine konfiguriert wurden.
- **Weitergehende Fehlersuche:** Überprüfen Sie die API-Aufrufstatistiken und den Fehlerverlauf pro Programm auf der Braze-Integrationskarte im Selfservice oder wenden Sie sich an Ihre Convercus-Vertretung.