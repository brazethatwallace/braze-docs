## Intégrer le SDK Roku {#integrating-the-roku-sdk}

### Étape 1 : Ajouter les fichiers {#step-1-add-files}

Les fichiers du SDK Braze se trouvent dans le répertoire `sdk_files` du [dépôt GitHub du SDK Roku de Braze](https://github.com/braze-inc/braze-roku-sdk).

1. Ajoutez `BrazeSDK.brs` à votre application dans le répertoire `source`.
2. Ajoutez `BrazeTask.brs` et `BrazeTask.xml` à votre application dans le répertoire `components`.

### Étape 2 : Ajouter les références {#step-2-add-references}

Ajoutez une référence à `BrazeSDK.brs` dans votre scène principale à l'aide de l'élément `script` suivant :

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Étape 3 : Configurer {#step-3-configure}

Dans `main.brs`, définissez la configuration de Braze sur le nœud global :

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

Vous pouvez trouver votre [endpoint du SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) et votre clé API dans le tableau de bord de Braze.

### Étape 4 : Initialiser Braze {#step-4-initialize-braze}

Initialisez l'instance de Braze :

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configurations optionnelles {#optional-configurations}

### Journalisation {#logging}

Pour déboguer votre intégration Braze, vous pouvez consulter la console de débogage Roku pour les journaux Braze. Consultez la section [Debugging code](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) de Roku Developers pour en savoir plus.