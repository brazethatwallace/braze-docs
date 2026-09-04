## Fragebogen zum Datenschutz bei Google Play {#privacy-questionnaire}

Ab April 2022 müssen Android-Entwickler:innen das Google-Play-Formular für [Datensicherheit](https://support.google.com/googleplay/android-developer/answer/10787469) ausfüllen, um Datenschutz- und Sicherheitspraktiken offenzulegen. In diesem Leitfaden finden Sie Anweisungen zum Ausfüllen dieses neuen Formulars sowie Informationen darüber, wie Braze Ihre App-Daten verarbeitet.

Als App-Entwickler:in haben Sie die Kontrolle darüber, welche Daten Sie an Braze senden. Die von Braze empfangenen Daten werden gemäß Ihren Anweisungen verarbeitet. Das ist es, was Google als [Dienstanbieter](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform) klassifiziert.

{% alert important %}
Dieser Artikel enthält Informationen zu den Daten, die das Braze SDK im Zusammenhang mit dem Fragebogen im Abschnitt zur Datensicherheit von Google verarbeitet. Dieser Artikel stellt keine Rechtsberatung dar. Wir empfehlen Ihnen daher, sich mit Ihrer Rechtsabteilung zu beraten, bevor Sie Informationen an Google übermitteln.
{% endalert %}

### Fragen {#questions}

| Fragen | Antworten für Braze SDK |
|---|---|
| Werden die erforderlichen Nutzerdatentypen von Ihrer App erfasst oder geteilt? | Ja, das Braze Android SDK erfasst Daten entsprechend der von der/dem App-Entwickler:in vorgenommenen Konfiguration. |
| Sind alle von Ihrer App gesammelten Nutzerdaten während der Übertragung verschlüsselt? | Ja. |
| Können Nutzer:innen eine Anfrage zur Löschung ihrer Daten stellen? | Ja. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Questions" }

Weitere Informationen über den Umgang mit Nutzeranfragen zu ihren Daten und deren Löschung finden Sie unter [Braze Data Retention Information]({{site.baseurl}}/api/data_retention).

### Datenerfassung {#data-collection}

Die von Braze erfassten Daten sind von der jeweiligen Integration und den Nutzerdaten abhängig, die Sie sammeln möchten. Weitere Informationen darüber, welche Daten standardmäßig von Braze erfasst werden und wie Sie bestimmte Attribute deaktivieren können, finden Sie unter [Optionen für die SDK-Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration).

<table aria-label="Data collection" id="datatypes">
    <thead>
        <tr>
            <th width="25%">Kategorie</th>
            <th width="25%">Datentyp</th>
            <th width="50%">Nutzung durch Braze</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Standort</td>
            <td>Ungefährer Standort</td>
            <td rowspan="15">Wird standardmäßig nicht erfasst.</td>
        </tr>
        <tr>
            <td>Genauer Standort</td>
        </tr>
        <tr>
            <td rowspan="9">Persönliche Infos</td>
            <td>Name</td>
        </tr>
        <tr>
            <td>E-Mail-Adresse</td>
        </tr>
        <tr>
            <td>Nutzer-IDs</td>
        </tr>
        <tr>
            <td>Adresse</td>
        </tr>
        <tr>
            <td>Telefonnummer</td>
        </tr>
        <tr>
            <td>Ethnie und Ethnizität</td>
        </tr>
        <tr>
            <td>Politische oder religiöse Überzeugungen</td>
        </tr>
        <tr>
            <td>Sexuelle Orientierung</td>
        </tr>
        <tr>
            <td>Andere Infos</td>
        </tr>
        <tr>
            <td rowspan="4">Finanzielle Informationen</td>
            <td>Zahlungsinformationen von Nutzer:innen</td>
        </tr>
        <tr>
            <td>Kaufhistorie</td>
        </tr>
        <tr>
            <td>Kreditwürdigkeit</td>
        </tr>
        <tr>
            <td>Andere Finanzinformationen</td>
        </tr>
        <tr>
            <td rowspan="2">Gesundheit und Fitness</td>
            <td>Informationen zur Gesundheit</td>
            <td rowspan="2">Wird standardmäßig nicht erfasst.</td>
        </tr>
        <tr>
            <td>Informationen zur Fitness</td>
        </tr>
        <tr>
            <td rowspan="3">Nachrichten</td>
            <td>E-Mails</td>
            <td rowspan="2">Wird standardmäßig nicht erfasst.</td>
        </tr>
        <tr>
            <td>SMS oder MMS</td>
        </tr>
        <tr>
            <td>Andere In-App-Nachrichten</td>
            <td>Wenn Sie In-App-Nachrichten oder Push-Benachrichtigungen über Braze senden, erfassen wir Informationen darüber, wann Nutzer:innen diese Nachrichten geöffnet oder gelesen haben.</td>
        </tr>
        <tr>
            <td rowspan="2">Fotos und Videos</td>
            <td>Fotos</td>
            <td rowspan="8">Nicht erfasst.</td>
        </tr>
        <tr>
            <td>Videos</td>
        </tr>
        <tr>
            <td rowspan="3">Audio-Dateien</td>
            <td>Sprach- oder Tonaufnahmen</td>
        </tr>
        <tr>
            <td>Musikdateien</td>
        </tr>
        <tr>
            <td>Andere Audio-Dateien</td>
        </tr>
        <tr>
            <td>Dateien und Dokumente</td>
            <td>Dateien und Dokumente</td>
        </tr>
        <tr>
            <td>Kalender</td>
            <td>Kalender-Ereignisse</td>
        </tr>
        <tr>
            <td>Kontakte</td>
            <td>Kontakte</td>
        </tr>
        <tr>
            <td rowspan="5">App-Aktivität</td>
            <td>App-Interaktionen</td>
            <td>Braze erfasst standardmäßig Daten zur Sitzungsaktivität. Alle anderen Interaktionen und Aktivitäten werden von der individuellen Integration Ihrer App bestimmt.</td>
        </tr>
        <tr>
            <td>In-App-Suchverlauf</td>
            <td>Nicht erfasst.</td>
        </tr>
        <tr>
            <td>Installierte Apps</td>
            <td>Nicht erfasst.</td>
        </tr>
        <tr>
            <td>Sonstige von Nutzer:innen generierte Inhalte</td>
            <td rowspan="2">Wird standardmäßig nicht erfasst.</td>
        </tr>
        <tr>
            <td>Andere Aktionen</td>
        </tr>
        <tr>
            <td>Besuchte Internetseiten</td>
            <td>Internetverlauf</td>
            <td>Nicht erfasst.</td>
        </tr>
        <tr>
            <td rowspan="3">Informationen und Performance der App</td>
            <td>Absturzprotokolle</td>
            <td>Braze erfasst Absturzprotokolle für Fehler, die innerhalb des SDK auftreten. Diese enthalten Angaben zum Smartphone-Modell und Betriebssystem der Nutzer:innen sowie eine Braze-spezifische Nutzer-ID.</td>
        </tr>
        <tr>
            <td>Diagnostik</td>
            <td>Nicht erfasst.</td>
        </tr>
        <tr>
            <td>Andere Performance-Daten der App</td>
            <td>Nicht erfasst.</td>
        </tr>
        <tr>
            <td>Gerät oder andere IDs</td>
            <td>Gerät oder andere IDs</td>
            <td>Braze generiert eine Geräte-ID, um die Geräte der Nutzer:innen zu unterscheiden, und überprüft, ob die Nachrichten an das richtige vorgesehene Gerät gesendet werden.</td>
        </tr>
    </tbody>
</table>

Wenn Sie mehr über andere Gerätedaten erfahren möchten, die Braze erfasst und die möglicherweise nicht in den Geltungsbereich der Google-Play-Datensicherheitsrichtlinien fallen, lesen Sie unsere [Übersicht über Android-Speicher]({{site.baseurl}}/developer_guide/storage/?tab=android) und unsere [Optionen für die SDK-Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration).

## Deaktivieren des Trackings von Daten {#disabling-data-tracking}

Um das Tracking von Daten im Android SDK zu deaktivieren, verwenden Sie die Methode [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Dadurch werden alle Netzwerkverbindungen abgebrochen, sodass das Braze SDK keine Daten mehr an die Braze-Server übermittelt.

## Zuvor gespeicherte Daten löschen {#wiping-previously-stored-data}

Sie können die Methode [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) verwenden, um alle clientseitig auf dem Gerät gespeicherten Daten vollständig zu löschen.

## Wiederaufnahme des Trackings von Daten {#resuming-data-tracking}

Um die Datenerfassung wieder aufzunehmen, können Sie die Methode [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) verwenden. Beachten Sie, dass dadurch keine zuvor gelöschten Daten wiederhergestellt werden.

## Abmelden und Push-Registrierung aufheben {#logout-and-unregister-push}

Das Braze SDK stellt Methoden bereit, um ein Gerät nicht mehr anzusprechen, wenn Nutzer:innen sich von Push-Benachrichtigungen abmelden oder sich ausloggen. Diese Methoden entfernen die Push-Registrierungsdaten der/des aktuellen Nutzer:in auf dem Braze-Server und im SDK, sodass Braze keine zukünftigen Push-Benachrichtigungs-Campaigns mehr an diese:n Nutzer:in sendet.

### Abmelden {#logout}

Wenn sich Nutzer:innen aus einer Anwendung abmelden, rufen Sie die `logout`-Methode des SDK auf, um die Push-Registrierung des Geräts von der/dem aktuellen Nutzer:in zu entfernen und automatisch Bereinigungsaktionen im SDK durchzuführen. Die `logout`-Methode führt Folgendes aus:

- Hebt die Registrierung des Push-Tokens des Geräts bei der/dem aktuellen Nutzer:in auf dem Braze-Server auf.
- Wenn der Aufruf zur Aufhebung der Registrierung erfolgreich ist, löscht das SDK lokal gespeicherte SDK-Daten und deaktiviert das SDK.
- Bei einem Fehler wird ein Fehler und ein `isRetriable`-Flag ausgelöst, damit die Integration entsprechende Maßnahmen ergreifen kann.

Das folgende Callback-Beispiel zeigt die Erfolgs- und Fehlerbehandlung von `logout`. Verwenden Sie es für Callback-basierte Abmeldeabläufe und ersetzen Sie das Logging durch Ihre eigene Wiederholungs- oder Re-Authentifizierungslogik.

```kotlin
// Completion callback
Braze.getInstance(context).logout { result ->
  result
    .onSuccess {
      Log.d(TAG, "Logout successful")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
    }
}
```

Das folgende Coroutine-Beispiel zeigt die suspendierende `logout`-API. Verwenden Sie es in Coroutine-basierten Abläufen und passen Sie die Erfolgs- und Fehlerzweige für Ihre App an.

```kotlin
lifecycleScope.launch {
  runCatching { Braze.getInstance(context).logout() }
    .onSuccess {
      Log.d(TAG, "Logout successful")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
    }
}
```

#### Tracking und Push nach `logout` wieder aktivieren {#re-enable-tracking-and-push-after-logout}

Nach einem erfolgreichen `logout` aktivieren Sie das SDK mit [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) erneut und Registrieren Sie sich dann über Ihr Betriebssystem oder Ihren Push-Anbieter erneut für Benachrichtigungen, indem Sie der [Android-Push-Einrichtung]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) folgen.

#### Sofortige Aufrufe zur Aufhebung der Registrierung vermeiden {#avoid-immediate-unregister-calls}

Vermeiden Sie es, `logout` oder `unregisterPush` direkt nach der Registrierung für Push-Benachrichtigungen beim Betriebssystem oder Push-Anbieter aufzurufen. Aufgrund der asynchronen Serververarbeitung kann dies in seltenen Fällen dazu führen, dass das Push-Token erneut der/dem Braze-Nutzer:in hinzugefügt wird.

### Push-Registrierung aufheben {#unregister-push}

Um den Push-Versand an ein Gerät ohne zusätzliche automatische Bereinigung zu stoppen, verwenden Sie die `unregisterPush`-Methode. Diese entfernt das Push-Token des Geräts von der/dem aktuellen Nutzer:in auf dem Braze-Server und löscht das lokal gespeicherte Token.

Das folgende Callback-Beispiel zeigt, wie Sie `unregisterPush`-Ergebnisse behandeln. Verwenden Sie es, wenn Ihr Ablauf Callback-basiert ist, und ersetzen Sie das Logging durch Ihre eigene Wiederholungsbehandlung.

```kotlin
// Completion callback
Braze.getInstance(context).unregisterPush { result ->
  result
    .onSuccess {
      Log.d(TAG, "Push unregistered successfully")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(
        TAG,
        "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
      )
    }
}
```

Das folgende Coroutine-Beispiel zeigt die suspendierende `unregisterPush`-API. Verwenden Sie es in Coroutine-basierten Abläufen und passen Sie die Erfolgs- und Fehlerzweige für Ihre App an.

```kotlin
lifecycleScope.launch {
  runCatching { Braze.getInstance(context).unregisterPush() }
    .onSuccess {
      Log.d(TAG, "Push unregistered successfully")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(
        TAG,
        "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
      )
    }
}
```

#### Push nach `unregisterPush` erneut registrieren {#re-register-push-after-unregisterpush}

Nachdem Sie `unregisterPush` aufgerufen haben, Registrieren Sie sich über Ihr Betriebssystem oder Ihren Push-Anbieter erneut für Benachrichtigungen, indem Sie der [Android-Push-Einrichtung]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) folgen, bevor Sie erneut Braze-Push-Benachrichtigungen senden.

#### Sofortige Aufrufe zur Aufhebung der Registrierung vermeiden

Vermeiden Sie es, `logout` oder `unregisterPush` direkt nach der Registrierung für Push-Benachrichtigungen beim Betriebssystem oder Push-Anbieter aufzurufen. Aufgrund der asynchronen Serververarbeitung kann dies in seltenen Fällen dazu führen, dass das Push-Token erneut der/dem Braze-Nutzer:in hinzugefügt wird.