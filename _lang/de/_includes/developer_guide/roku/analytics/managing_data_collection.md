{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Zuvor gespeicherte Daten löschen {#wiping-previously-stored-data}

Das Roku SDK enthält keine `wipeData`-Methode. Um einen sauberen Ausgangszustand zu erzeugen, der funktional `wipeData()` in anderen Braze SDKs entspricht, löschen Sie die vier Braze-Registry-Abschnitte und initialisieren Sie das SDK anschließend neu.

Das Braze Roku SDK speichert Daten in den folgenden Registry-Abschnitten:

| Abschnitt | Inhalt |
|---------|----------|
| `braze.section.device_id` | Die Geräte-UUID, die zur Identifizierung dieses Geräts in Braze verwendet wird. |
| `braze.section.user_id` | Die externe Nutzer-ID, sofern eine festgelegt wurde. |
| `braze.section.session` | Die aktive Sitzungs-UUID, Startzeit und Endzeit. |
| `braze.section.config` | Zwischengespeicherte SDK-Konfiguration und Feature-Flag-Daten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wiping previously-stored data" }

### 1. Schritt: Registry-Abschnitte löschen {#step-1-clear-the-registry-sections}

Verwenden Sie [`roRegistry.Delete()`](https://developer.roku.com/docs/references/brightscript/components/roregistry.md), um jeden Braze-Abschnitt zu löschen, und rufen Sie anschließend `Flush()` auf, um die Änderungen zu übernehmen:

```brightscript
sub WipeBrazeData()
    registry = CreateObject("roRegistry")
    registry.Delete("braze.section.device_id")
    registry.Delete("braze.section.user_id")
    registry.Delete("braze.section.session")
    registry.Delete("braze.section.config")
    registry.Flush()
end sub
```

### 2. Schritt: Braze SDK neu initialisieren {#step-2-re-initialize-the-braze-sdk}

Wenn Sie das [Braze SDK erneut initialisieren]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku), geht das SDK mit den fehlenden Registry-Daten problemlos um:

- Der Abschnitt für die Geräte-ID ist leer, sodass das SDK eine neue UUID generiert und das Gerät als anonym behandelt.
- Der Abschnitt für die Nutzer-ID ist leer, sodass das SDK standardmäßig eine:n anonyme:n Nutzer:in verwendet (ein leerer String `""`).
- Der Sitzungsabschnitt ist leer, sodass das SDK eine neue Sitzung startet.
- Der Konfigurationsabschnitt ist leer, sodass das SDK die Konfiguration erneut vom Server abruft.

{% alert note %}
Das Roku SDK erzeugt beim Löschen der Registry keine serverseitige Löschanfrage. Wenn Sie die:den Nutzer:in auch aus Braze entfernen möchten, senden Sie eine Anfrage an [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) unter Verwendung der `external_id` oder `braze_id` der:des Nutzer:in.
{% endalert %}