---
nav_title: Datenpunkte
article_title: Datenpunkte
page_order: 3
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, was Datenpunkte bei Braze sind und wie Sie deren Nutzung im Blick behalten können."
search_rank: 6
---

# Datenpunkte {#data-points}

> Bei Braze sind Daten gleichbedeutend mit Aktion: Jede Information, die in Braze eingeht, aktualisiert die Segment-Zugehörigkeit, kann Nachrichten triggern und stornieren, ist sofort für die Personalisierung von Nachrichten verfügbar und vieles mehr. Datenpunkte helfen Ihnen, die wichtigsten Informationen für Ihr Unternehmen zu definieren. Indem Sie sich genau überlegen, welche Daten Sie tracken möchten, stellen Sie sicher, dass Sie das Targeting auf die Daten mit dem höchsten Wirkungsgrad für die Erfahrung Ihrer Nutzer:innen ausrichten.

Die Datenpunkte basieren auf Informationen, die anhand von Nutzerprofilen aufgezeichnet werden. Eine genauere Aufschlüsselung dieser Definition finden Sie in Ihrem Braze-Vertrag. Unser Customer-Success-Team kann Ihnen helfen, die besten Datenpraktiken an Ihre Bedürfnisse anzupassen.

## Definition {#definition}

„Datenpunkte“ bezeichnen eine abrechenbare Nutzungseinheit der Braze-Dienste, gemessen an einem Sitzungsstart, einem Sitzungsende, einem angepassten Event oder einem erfassten Kauf sowie an jedem Attribut, das in einem Endnutzer:innen-Profil festgelegt wird. Zur Klarstellung: Jede der zuvor in diesem Abschnitt genannten Datenarten (wie Sitzungsstart, Sitzungsende, angepasstes Event oder erfasster Kauf sowie jedes Attribut), die zu einem bestimmten Zeitpunkt im Profil einer Endnutzerin oder eines Endnutzers festgelegt wird, zählt jeweils als ein einzelner Datenpunkt.

Daten und Events, die standardmäßig von den Braze-Diensten erfasst werden – darunter beispielsweise Push-Token / Textbaustein, Geräteinformationen und alle Tracking-Events für das Campaign-Engagement, wie E-Mail-Öffnungen und Klicks auf Push-Benachrichtigungen – werden *nicht* als Datenpunkte gezählt.

Im Abschnitt [Verbrauchszählung](#consumption-count) dieses Artikels erfahren Sie, welche Daten auf Ihr Datenpunkt-Kontingent angerechnet werden.

## Datenpunkt-Nutzung anzeigen {#viewing-data-point-usage}

Um Ihre Datenpunkt-Nutzung anzuzeigen, gehen Sie zu **Einstellungen** > **Abrechnung** und wählen Sie den Tab **Gesamte Datenpunkt-Nutzung** aus.

### Aktualisierungszeitplan für Datenpunkte {#data-point-refresh-schedule}

Die Datenpunkt-Nutzung wird alle 24 Stunden etwa um 2:00 Uhr ET zwischengespeichert (nicht in Echtzeit). Bis der Cache aktualisiert wird, sehen verschiedene Dashboard-Nutzer:innen möglicherweise dieselben Gesamtwerte, auch wenn sie den Tab zu unterschiedlichen Zeiten am selben Tag öffnen. Informationen zum gleichen Caching-Verhalten bei anderen Abrechnungsansichten finden Sie unter [Dashboard der Gesamtdatenpunkte]({{site.baseurl}}/user_guide/administer/global/billing#total-data-points-dashboard).

Weitere Informationen zu den Komponenten des Datenpunkt-Dashboards finden Sie unter [Abrechnung]({{site.baseurl}}/user_guide/administer/global/billing).

{% alert tip %}
**Verschwenden Sie keine Datenpunkte. Aktualisieren Sie nur sich ändernde Daten!**<br><br>
Um die Datenpunkt-Nutzung zu minimieren, empfehlen wir, ein Programm einzurichten, das den wiederholten Versand unveränderter Daten verhindert und nur neue und relevante Daten an Braze übergibt. Braze arbeitet mit Ihnen zusammen, um diese Best Practice während des Onboardings zu etablieren.
{% endalert %}

## Verbrauchszählung {#consumption-count}

Zusammenfassend werden Datenpunkte gesammelt, wenn die Profildaten einer Nutzer:in aktualisiert werden oder wenn sie bestimmte Aktionen ausführen. Im Wesentlichen sind Datenpunkte Zählungen für jede `session starts`, `session ends`, `events` und `purchases` Ihrer Nutzer:innen.

In den folgenden Abschnitten finden Sie eine Aufschlüsselung, wie Braze Datenpunkte akkumuliert. Falls Sie jemals Fragen zu den Feinheiten der Braze-Datenpunkte haben, kann Ihr Braze Account Manager:in diese beantworten.

Bei der API-Aufnahme folgt jedes abrechnungsrelevante Update über [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) denselben Regeln wie andere Profil-Updates: Zum Beispiel zählt jedes protokollierte **angepasste Event** als ein Datenpunkt, und **angepasste Attribute** zählen in der Regel pro aktualisiertem Attribut in dieser Anfrage (siehe die abrechnungsrelevanten Tabellen im folgenden Abschnitt und [Besondere Umstände](#special-circumstances)).

Die folgenden Aktionen protokollieren keine Datenpunkte:
- Löschen von Nutzer:innen aus Braze
- Verwendung von Connected-Content in Nachrichten
- Globale Änderungen des Abo-Status und Änderungen rund um Abo-Gruppen
- Umbenennung der externen IDs Ihrer Nutzer:innen über [API-Aufrufe]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)
- Blockieren von Events, Attributen oder Event-Eigenschaften

### Besondere Umstände {#special-circumstances}

#### Arrays {#arrays}

Ein Array ist eine geordnete Sammlung von Elementen, die in einem angepassten Attribut gespeichert werden. Das Aktualisieren eines Arrays kostet einen Datenpunkt pro API-Aufruf, selbst wenn sich das Array tatsächlich nicht ändert. Zum Beispiel verbraucht das Senden einer `remove`-Operation für einen Wert, der im Array nicht existiert, trotzdem einen Datenpunkt. Ebenso verbraucht das Setzen eines angepassten Attributs auf `null`, um es aus dem Profil zu entfernen, einen Datenpunkt. Wenn Sie Werte inkrementell zu einem Array hinzufügen, wird dies als ein Datenpunkt pro Wert gezählt.

{% alert tip %}
Wenn Sie bei einfachen Arrays das gesamte Array auf einmal setzen, wird es als ein einzelner Datenpunkt gezählt. Daher sind Arrays ein hervorragendes Werkzeug, um Nutzerprofile mit relevanten Informationen auf dem neuesten Stand zu halten und Kosten zu senken. <br><br> Arrays von Objekten verbrauchen einen Datenpunkt für jeden Schlüssel, der aktualisiert wird. Reduzieren Sie unnötigen Datenpunkt-Verbrauch, indem Sie nur Updates an Braze übergeben.
{% endalert %}

#### Verschachtelte angepasste Attribute {#nested-custom-attributes}

Verschachtelte angepasste Attribute beziehen sich auf ein Objekt, das eine Reihe von Attributen als Eigenschaft eines anderen Attributs definiert. Jeder Schlüssel im Objekt wird als ein Datenpunkt gezählt.

{% alert note %}
Das Aktualisieren eines angepassten Attribut-Objekts auf `null` verbraucht ebenfalls einen Datenpunkt.
{% endalert %}

#### CSV

Über CSV-Import hochgeladene angepasste Attribute werden auf Ihre Datenpunkte angerechnet. Allerdings protokollieren CSV-Importe zu Segmentierungszwecken (Importe, bei denen `external_id`, `braze_id` oder `user_alias_name` das einzige Feld ist) keine Datenpunkte.

Da Änderungen des Abo-Status keine Datenpunkte protokollieren, fallen außerdem beim Aktualisieren der Felder `email_subscribe`, `push_subscribe`, `subscription_group_id` oder `subscription_state` in Ihrer CSV-Datei keine Kosten an.

## Datenpunkte

{% alert note %}
Die folgenden Tabellen sind zur Veranschaulichung gedacht. Für genaue Namenskonventionen, Groß-/Kleinschreibung und akzeptierte Werte bestimmter Felder lesen Sie die entsprechende Dokumentation für Ihre Ingestion-Methode.
{% endalert %}

{% tabs %}
{% tab Nicht abrechenbar %}

### Nicht abrechenbare Datenpunkte (Standard) {#non-billable-data-points-default}

<div class="small_table"></div>

| Datentyp | Datenpunkt |
| --------- | ---------- |
| Profildaten | Land |
| Profildaten | Sprache |
| Profildaten | Nutzer-ID |
| Profildaten | Nutzer-Alias |
| Neueste Geräte | Anzahl der Geräte |
| Neueste Geräte | Neueste Smartwatch |
| Neueste Geräte | App-Version |
| Neueste Geräte | Gerät |
| Neueste Geräte | Geräte-Betriebssystem |
| Kontakteinstellungen | E-Mail abonniert |
| Kontakteinstellungen | Push abonniert |
| Kontakteinstellungen | Für Push registrierte Apps |
| Kontakteinstellungen | Abo-Gruppe |
| Empfangene Campaigns | E-Mail-Adresse |
| Install-Attribution | Installationsquelle |
| Install-Attribution | Campaign |
| Install-Attribution | Anzeigengruppe |
| Install-Attribution | Anzeige |
| Sonstiges | Zufällige Bucket-Nummer |
| Empfangene Canvas-Nachrichten | Empfangene Canvas-Nachrichten |
| Nachrichten-Engagement | Alle Engagement-Events (z. B. Öffnungen, Klicks, Impressionen und Schließungen) |
| Twitter | Follower |
| Twitter | Following |
| Twitter | Anzahl der Tweets |
| Facebook | Likes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nicht abrechenbare Datenpunkte (Standard)" }

{% endtab %}
{% tab Abrechenbar %}

### Abrechenbare Datenpunkte {#billable-data-points}

{% alert important %}
Das Hinzufügen, Entfernen oder Aktualisieren der folgenden Datentypen verursacht einen abrechenbaren Datenpunkt.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Datentyp | Datenpunkt | Hinweise |
| --------- | ---------- | ----- |
| Profildaten | Vorname | |
| Profildaten | Nachname | |
| Profildaten | E-Mail-Adresse | |
| Profildaten | Geschlecht | |
| Profildaten | Altersgruppe | |
| Profildaten | Land | Bei manueller Erfassung. Wird bei automatischer Erfassung nicht auf den Verbrauch angerechnet. |
| Profildaten | Ort | |
| Profildaten | Sprache | Bei manueller Erfassung. Wird bei automatischer Erfassung nicht auf den Verbrauch angerechnet. |
| Profildaten | Neueste Gerätesprache | |
| Profildaten | Zeitzone | |
| Profildaten | Geburtsdatum | |
| Profildaten | Biografie | |
| Profildaten | Telefonnummer | |
| App-Nutzungsdaten | Sitzungsbeginn | |
| App-Nutzungsdaten | Sitzungsende | |
| Angepasste Attribute | Alle angepassten Attribute | |
| Angepasste Events | Alle angepassten Events | |
| Angepasste Event-Eigenschaften | Alle angepassten Event-Eigenschaften | Angepasste Event-Eigenschaften, die für die Segmentierung mit den Filtern `X Custom Event Property in Y Days` oder `X Purchase Property in Y Days` aktiviert sind, werden jeweils als separate Datenpunkte gezählt – zusätzlich zu dem Datenpunkt, der durch das angepasste Event selbst verursacht wird. |
| Käufe | Alle Käufe | |
| Kauf-Details | Alle Kauf-Details | |
| Amplitude-Kohortenzuweisung | Alle Zuweisungen | |
| Mixpanel-Kohortenzuweisung | Alle Zuweisungen | |
| Hightouch-Kohortenzuweisung | Alle Zuweisungen | |
| Appsflyer-Kohortenzuweisung | Alle Zuweisungen | |
| Letzter Standort | Alle letzten Standorte | Das Betreten oder Verlassen von Geofences protokolliert keine Datenpunkte, da Geofence-Daten nicht im Kundenprofil gespeichert werden. Geofences werden von den Standortdiensten von Apple und Google überwacht; Braze wird nur benachrichtigt, wenn Nutzer:innen einen Geofence auslösen. |
| Twitter | Nutzername | |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abrechenbare Datenpunkte" }

{% endtab %}
{% endtabs %}