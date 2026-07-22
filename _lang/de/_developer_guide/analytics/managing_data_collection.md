---
nav_title: Datenerfassung verwalten
article_title: Datenerfassung für das Braze SDK verwalten
page_order: 8
description: "Erfahren Sie, wie Sie die Datenerfassung für das Braze SDK verwalten können."

---

# Datenerfassung verwalten {#manage-data-collection}

> Erfahren Sie, wie Sie die Datenerfassung für das Braze SDK verwalten, damit Sie bei Bedarf alle Datenschutzbestimmungen einhalten können.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/analytics/managing_data_collection.md %}
{% endsdktab %}

{% sdktab android %}
## Fragebogen zum Datenschutz bei Google Play {#privacy-questionnaire}

Ab April 2022 müssen Android-Entwickler:innen das Google-Play-Formular für [Datensicherheit](https://support.google.com/googleplay/android-developer/answer/10787469) ausfüllen, um Datenschutz- und Sicherheitspraktiken offenzulegen. In diesem Leitfaden finden Sie Anweisungen zum Ausfüllen dieses neuen Formulars sowie Informationen darüber, wie Braze Ihre App-Daten verarbeitet.

Als App-Entwickler:in haben Sie die Kontrolle darüber, welche Daten Sie an Braze senden. Die von Braze empfangenen Daten werden gemäß Ihren Anweisungen verarbeitet. Das ist es, was Google als [Dienstanbieter](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform) klassifiziert.

{% alert important %}
Dieser Artikel enthält Informationen zu den Daten, die das Braze SDK im Zusammenhang mit dem Fragebogen im Abschnitt zur Datensicherheit von Google verarbeitet. Dieser Artikel stellt keine Rechtsberatung dar. Wir empfehlen Ihnen daher, sich mit Ihrer Rechtsabteilung zu beraten, bevor Sie Informationen an Google übermitteln.
{% endalert %}

### Fragen {#questions}

| Fragen | Antworten für Braze SDK |
|---|---|
| Werden die erforderlichen Nutzerdatentypen von Ihrer App erfasst oder geteilt? | Ja, das Braze Android SDK erfasst Daten entsprechend der von der App-Entwickler:in vorgenommenen Konfiguration. |
| Werden alle von Ihrer App erfassten Nutzerdaten bei der Übertragung verschlüsselt? | Ja. |
| Bieten Sie Nutzer:innen eine Möglichkeit, die Löschung ihrer Daten zu beantragen? | Ja. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fragen" }

Weitere Informationen zum Umgang mit Nutzeranfragen zu ihren Daten und deren Löschung finden Sie unter [Braze-Informationen zur Datenaufbewahrung]({{site.baseurl}}/api/data_retention).

### Datenerfassung {#data-collection}

Die von Braze erfassten Daten werden durch Ihre spezifische Integration und die von Ihnen gewählten Nutzerdaten bestimmt. Weitere Informationen darüber, welche Daten Braze standardmäßig erfasst und wie Sie bestimmte Attribute deaktivieren können, finden Sie in unseren [SDK-Optionen zur Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection#minimum-integration).

<table aria-label="Datenerfassung" id="datatypes">
    <thead>
        <tr>
            <th width="25%">Kategorie</th>
            <th width="25%">Datentyp</th>
            <th width="50%">Verwendung durch Braze</th>
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
            <td rowspan="9">Persönliche Informationen</td>
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
            <td>Ethnie und Herkunft</td>
        </tr>
        <tr>
            <td>Politische oder religiöse Überzeugungen</td>
        </tr>
        <tr>
            <td>Sexuelle Orientierung</td>
        </tr>
        <tr>
            <td>Sonstige Informationen</td>
        </tr>
        <tr>
            <td rowspan="4">Finanzinformationen</td>
            <td>Zahlungsinformationen der Nutzer:innen</td>
        </tr>
        <tr>
            <td>Kaufhistorie</td>
        </tr>
        <tr>
            <td>Kreditwürdigkeit</td>
        </tr>
        <tr>
            <td>Sonstige Finanzinformationen</td>
        </tr>
        <tr>
            <td rowspan="2">Gesundheit und Fitness</td>
            <td>Gesundheitsinformationen</td>
            <td rowspan="2">Wird standardmäßig nicht erfasst.</td>
        </tr>
        <tr>
            <td>Fitnessinformationen</td>
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
            <td>Sonstige In-App-Nachrichten</td>
            <td>Wenn Sie In-App-Nachrichten oder Push-Benachrichtigungen über Braze senden, erfassen wir Informationen darüber, wann Nutzer:innen diese Nachrichten geöffnet oder gelesen haben.</td>
        </tr>
        <tr>
            <td rowspan="2">Fotos und Videos</td>
            <td>Fotos</td>
            <td rowspan="8">Wird nicht erfasst.</td>
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
            <td>Sonstige Audio-Dateien</td>
        </tr>
        <tr>
            <td>Dateien und Dokumente</td>
            <td>Dateien und Dokumente</td>
        </tr>
        <tr>
            <td>Kalender</td>
            <td>Kalendereinträge</td>
        </tr>
        <tr>
            <td>Kontakte</td>
            <td>Kontakte</td>
        </tr>
        <tr>
            <td rowspan="5">App-Aktivität</td>
            <td>App-Interaktionen</td>
            <td>Braze erfasst standardmäßig Sitzungsaktivitätsdaten. Alle anderen Interaktionen und Aktivitäten werden durch die angepasste Integration Ihrer App bestimmt.</td>
        </tr>
        <tr>
            <td>In-App-Suchverlauf</td>
            <td>Wird nicht erfasst.</td>
        </tr>
        <tr>
            <td>Installierte Apps</td>
            <td>Wird nicht erfasst.</td>
        </tr>
        <tr>
            <td>Sonstige nutzergenerierte Inhalte</td>
            <td rowspan="2">Wird standardmäßig nicht erfasst.</td>
        </tr>
        <tr>
            <td>Sonstige Aktionen</td>
        </tr>
        <tr>
            <td>Surfen im Internet</td>
            <td>Browserverlauf</td>
            <td>Wird nicht erfasst.</td>
        </tr>
        <tr>
            <td rowspan="3">App-Informationen und Performance</td>
            <td>Absturzprotokolle</td>
            <td>Braze erfasst Absturzprotokolle für Fehler, die innerhalb des SDK auftreten. Diese enthalten das Telefonmodell und die Betriebssystemversion der Nutzer:innen sowie eine Braze-spezifische Nutzer-ID.</td>
        </tr>
        <tr>
            <td>Diagnose</td>
            <td>Wird nicht erfasst.</td>
        </tr>
        <tr>
            <td>Sonstige App-Performance-Daten</td>
            <td>Wird nicht erfasst.</td>
        </tr>
        <tr>
            <td>Geräte- oder sonstige IDs</td>
            <td>Geräte- oder sonstige IDs</td>
            <td>Braze generiert eine Geräte-ID, um die Geräte der Nutzer:innen zu unterscheiden, und prüft, ob Nachrichten an das richtige vorgesehene Gerät gesendet werden.</td>
        </tr>
    </tbody>
</table>

Weitere Informationen zu anderen Gerätedaten, die Braze erfasst und die möglicherweise nicht in den Geltungsbereich der Datensicherheitsrichtlinien von Google Play fallen, finden Sie in unserer [Übersicht zum Android-Speicher]({{site.baseurl}}/developer_guide/storage/?tab=android) und in unseren [SDK-Optionen zur Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection#minimum-integration).

## Deaktivieren des Trackings von Daten {#disabling-data-tracking}

Um das Tracking von Daten im Android SDK zu deaktivieren, verwenden Sie die Methode [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Dadurch werden alle Netzwerkverbindungen abgebrochen, sodass das Braze SDK keine Daten mehr an die Braze-Server übermittelt.

## Zuvor gespeicherte Daten löschen {#wiping-previously-stored-data}

Sie können die Methode [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) verwenden, um alle clientseitig auf dem Gerät gespeicherten Daten vollständig zu löschen.

## Wiederaufnahme des Trackings von Daten {#resuming-data-tracking}

Um die Datenerfassung wieder aufzunehmen, können Sie die Methode [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) verwenden. Beachten Sie, dass dadurch keine zuvor gelöschten Daten wiederhergestellt werden.

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/managing_data_collection.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/analytics/managing_data_collection.md %}
{% endsdktab %}

{% sdktab roku %}
{% multi_lang_include developer_guide/roku/analytics/managing_data_collection.md %}
{% endsdktab %}

{% endsdktabs %}