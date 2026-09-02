## Das Roku SDK or Software-Development-Kit integrieren {#integrating-the-roku-sdk}

### Schritt 1: Dateien hinzufügen {#step-1-add-files}

Die Braze SDK or Software-Development-Kit-Dateien befinden sich im Verzeichnis `sdk_files` im [Braze Roku SDK or Software-Development-Kit-Repository](https://github.com/braze-inc/braze-roku-sdk).

1. Fügen Sie `BrazeSDK.brs` zu Ihrer App im Verzeichnis `source` hinzu.
2. Fügen Sie `BrazeTask.brs` und `BrazeTask.xml` zu Ihrer App im Verzeichnis `components` hinzu.

### Schritt 2: Referenzen hinzufügen {#step-2-add-references}

Fügen Sie eine Referenz zu `BrazeSDK.brs` in Ihrer Hauptszene hinzu, indem Sie das folgende `script`-Element verwenden:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Schritt 3: Konfigurieren {#step-3-configure}

Setzen Sie in `main.brs` die Braze-Konfiguration auf dem globalen Knoten:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Ihren [SDK or Software-Development-Kit-Endpunkt]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) und API-Schlüssel finden Sie im Braze-Dashboard.

### Schritt 4: Braze initialisieren {#step-4-initialize-braze}

Initialisieren Sie die Braze-Instanz:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Optionale Konfigurationen {#optional-configurations}

### Protokollierung {#logging}

Um Ihre Braze-Integration zu debuggen, können Sie die Roku-Debug-Konsole für Braze-Protokolle einsehen. Weitere Informationen finden Sie unter [Debugging code](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) von Roku Developers.