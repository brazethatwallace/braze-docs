{% multi_lang_include developer_guide/prerequisites/react_native.md %} Vous devez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Personnalisation des notifications push dans React native {#push-customization-in-react-native}

Le SDK Braze React native n'expose pas la personnalisation des notifications push (boutons d'action, catégories, fabriques de notifications personnalisées) via son API JavaScript. Ces fonctionnalités nécessitent une configuration native dans vos projets iOS et Android.

Le tableau suivant indique les fonctionnalités qui nécessitent une configuration native :

| Fonctionnalité | iOS | Android |
| --- | --- | --- |
| Boutons d'action | Configurer en Swift/Objective-C natif | Configurer en Java/Kotlin natif |
| Catégories push | Configurer en Swift/Objective-C natif | Configurer en Java/Kotlin natif |
| Fabrique de notifications personnalisées | S.O. | Configurer en Java/Kotlin natif |
| Personnalisation des badges | Configurer en Swift/Objective-C natif | S.O. |
| Sons personnalisés | Configurer en Swift/Objective-C natif | Configurer en Java/Kotlin natif |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Personnalisation des notifications push dans React native" }

### Personnalisation iOS {#ios-customization}

Pour ajouter des boutons d'action push, des catégories, des badges ou des sons personnalisés sur iOS, implémentez la configuration native dans votre `AppDelegate` (Swift ou Objective-C). Consultez [Personnaliser les notifications push – Swift]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift) pour obtenir des instructions détaillées.

### Personnalisation Android {#android-customization}

Pour ajouter des boutons d'action push, des catégories ou une fabrique de notifications personnalisées sur Android, implémentez la configuration native dans votre projet Android. Consultez [Personnaliser les notifications push – Android]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android) pour obtenir des instructions détaillées.