## Questionnaire sur la protection de la vie privée dans Google Play {#privacy-questionnaire}

À partir d'avril 2022, les développeurs Android devront remplir le [formulaire de sécurité des données](https://support.google.com/googleplay/android-developer/answer/10787469) de Google Play pour divulguer leurs pratiques en matière de confidentialité et de sécurité. Ce guide fournit des instructions sur la façon de remplir ce nouveau formulaire avec des informations sur la manière dont Braze gère les données de votre application.

En tant que développeur d'applications, vous contrôlez les données que vous envoyez à Braze. Les données reçues par Braze sont traitées conformément à vos instructions. Google classifie ceci en tant que [fournisseur de services](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform).

{% alert important %}
Cet article fournit des informations relatives aux données traitées par le SDK Braze en lien avec la rubrique de sécurité du questionnaire Google. Cet article ne constitue pas un avis juridique ; nous vous recommandons donc de consulter votre équipe juridique avant de soumettre toute information à Google.
{% endalert %}

### Questions

| Questions | Réponses concernant le SDK Braze |
|---|---|
| Votre application collecte-t-elle ou partage-t-elle un des types de données utilisateur requis ? | Oui, le SDK de Braze pour Android recueille des données telles que configurées par le développeur d'applications. |
| Toutes les données utilisateur collectées par votre application sont-elles chiffrées durant leur transit ? | Oui. |
| Fournissez-vous un moyen aux utilisateurs de demander la suppression de leurs données ? | Oui. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Questions" }

Pour plus d'informations sur la gestion des demandes des utilisateurs concernant leurs données et leur suppression, consultez [Informations sur la rétention des données de Braze]({{site.baseurl}}/api/data_retention).

### Collecte de données {#data-collection}

Les données collectées par Braze sont déterminées par votre intégration spécifique et les données utilisateur que vous choisissez de recueillir. Pour en savoir plus sur les données que Braze collecte par défaut et comment désactiver certains attributs, consultez nos [options de collecte de données du SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration).

<table aria-label="Collecte de données" id="datatypes">
    <thead>
        <tr>
            <th width="25%">Catégorie</th>
            <th width="25%">Type de données</th>
            <th width="50%">Utilisation par Braze</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Localisation</td>
            <td>Localisation approximative</td>
            <td rowspan="15">Pas de collecte par défaut.</td>
        </tr>
        <tr>
            <td>Localisation précise</td>
        </tr>
        <tr>
            <td rowspan="9">Informations personnelles</td>
            <td>Nom</td>
        </tr>
        <tr>
            <td>Adresse e-mail</td>
        </tr>
        <tr>
            <td>ID utilisateur</td>
        </tr>
        <tr>
            <td>Adresse</td>
        </tr>
        <tr>
            <td>Numéro de téléphone</td>
        </tr>
        <tr>
            <td>Race et ethnie</td>
        </tr>
        <tr>
            <td>Convictions politiques ou religieuses</td>
        </tr>
        <tr>
            <td>Orientation sexuelle</td>
        </tr>
        <tr>
            <td>Autres informations</td>
        </tr>
        <tr>
            <td rowspan="4">Informations financières</td>
            <td>Informations de paiement de l'utilisateur</td>
        </tr>
        <tr>
            <td>Historique d'achats</td>
        </tr>
        <tr>
            <td>Score de crédit</td>
        </tr>
        <tr>
            <td>Autres informations financières</td>
        </tr>
        <tr>
            <td rowspan="2">Santé et condition physique</td>
            <td>Informations sur la santé</td>
            <td rowspan="2">Pas de collecte par défaut.</td>
        </tr>
        <tr>
            <td>Informations sur la condition physique</td>
        </tr>
        <tr>
            <td rowspan="3">Messages</td>
            <td>E-mails</td>
            <td rowspan="2">Pas de collecte par défaut.</td>
        </tr>
        <tr>
            <td>SMS ou MMS</td>
        </tr>
        <tr>
            <td>Autres messages in-app</td>
            <td>Si vous envoyez des messages in-app ou des notifications push via Braze, nous collectons des informations sur le moment où les utilisateurs ont ouvert ou lu ces messages.</td>
        </tr>
        <tr>
            <td rowspan="2">Photos et vidéos</td>
            <td>Photos</td>
            <td rowspan="8">Pas de collecte.</td>
        </tr>
        <tr>
            <td>Vidéos</td>
        </tr>
        <tr>
            <td rowspan="3">Fichiers audio</td>
            <td>Enregistrements vocaux ou sonores</td>
        </tr>
        <tr>
            <td>Fichiers musicaux</td>
        </tr>
        <tr>
            <td>Autres fichiers audio</td>
        </tr>
        <tr>
            <td>Fichiers et documents</td>
            <td>Fichiers et documents</td>
        </tr>
        <tr>
            <td>Calendrier</td>
            <td>Événements du calendrier</td>
        </tr>
        <tr>
            <td>Contacts</td>
            <td>Contacts</td>
        </tr>
        <tr>
            <td rowspan="5">Activité de l'application</td>
            <td>Interactions avec l'application</td>
            <td>Braze collecte les données d'activité de session par défaut. Toutes les autres interactions et activités sont déterminées par l'intégration personnalisée de votre application.</td>
        </tr>
        <tr>
            <td>Historique de recherche dans l'application</td>
            <td>Pas de collecte.</td>
        </tr>
        <tr>
            <td>Applications installées</td>
            <td>Pas de collecte.</td>
        </tr>
        <tr>
            <td>Autre contenu généré par l'utilisateur</td>
            <td rowspan="2">Pas de collecte par défaut.</td>
        </tr>
        <tr>
            <td>Autres actions</td>
        </tr>
        <tr>
            <td>Navigation web</td>
            <td>Historique de navigation web</td>
            <td>Pas de collecte.</td>
        </tr>
        <tr>
            <td rowspan="3">Informations sur l'application et performances</td>
            <td>Journaux de plantage</td>
            <td>Braze collecte les journaux de plantage pour les erreurs qui se produisent au sein du SDK. Ils contiennent le modèle de téléphone et le niveau d'OS de l'utilisateur, ainsi qu'un ID utilisateur spécifique à Braze.</td>
        </tr>
        <tr>
            <td>Diagnostics</td>
            <td>Pas de collecte.</td>
        </tr>
        <tr>
            <td>Autres données de performance de l'application</td>
            <td>Pas de collecte.</td>
        </tr>
        <tr>
            <td>Appareil ou autres ID</td>
            <td>Appareil ou autres ID</td>
            <td>Braze génère un ID d'appareil pour différencier les appareils des utilisateurs et vérifier que les messages sont envoyés au bon appareil.</td>
        </tr>
    </tbody>
</table>

Pour en savoir plus sur les autres données d'appareils que Braze collecte et qui peuvent ne pas être couvertes par les directives de sécurité des données de Google Play, consultez notre [aperçu du stockage Android]({{site.baseurl}}/developer_guide/storage/?tab=android) et nos [options de collecte de données du SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration).

## Désactivation du suivi des données {#disabling-data-tracking}

Pour désactiver l'activité de suivi des données sur le SDK Android, utilisez la méthode [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Cela entraînera l'annulation de toutes les connexions réseau, ce qui signifie que le SDK Braze ne transmettra plus aucune donnée aux serveurs Braze.

## Effacer les données précédemment stockées {#wiping-previously-stored-data}

Vous pouvez utiliser la méthode [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) pour effacer complètement toutes les données côté client stockées sur l'appareil.

## Reprise du suivi des données {#resuming-data-tracking}

Pour reprendre la collecte de données, vous pouvez utiliser la méthode [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html). Veuillez noter que cela ne restaurera pas les données précédemment effacées.

## Déconnexion et désinscription des notifications push {#logout-and-unregister-push}

Le SDK Braze fournit des méthodes pour cesser de cibler un appareil lorsqu'un utilisateur se désinscrit des notifications push ou se déconnecte. Ces méthodes suppriment les données d'inscription push de l'utilisateur actuel sur le serveur Braze et dans le SDK, de sorte que Braze n'envoie plus de futures Campaigns de notifications push à cet utilisateur.

### Déconnexion {#logout}

Lorsqu'un utilisateur se déconnecte d'une application, appelez la méthode `logout` du SDK pour supprimer l'inscription push de l'appareil de l'utilisateur actuel et effectuer automatiquement des actions de nettoyage sur le SDK. La méthode `logout` effectue les opérations suivantes :

- Désinscrit le jeton push de l'appareil de l'utilisateur actuel sur le serveur Braze.
- Si l'appel de désinscription réussit, le SDK efface les données SDK stockées localement et désactive le SDK.
- En cas d'échec, lève une erreur et un indicateur `isRetriable` pour permettre à l'intégrateur d'agir.

L'exemple de rappel suivant montre la gestion du succès et des erreurs de `logout`. Utilisez-le pour les flux de déconnexion basés sur des rappels, et remplacez la journalisation par votre logique de nouvelle tentative ou de ré-authentification.

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

L'exemple de coroutine suivant montre l'API suspensive `logout`. Utilisez-le dans les flux basés sur des coroutines et personnalisez les branches de succès et d'échec pour votre application.

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

#### Réactiver le suivi et les notifications push après `logout` {#re-enable-tracking-and-push-after-logout}

Après une déconnexion réussie via `logout`, réactivez le SDK avec [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html), puis réinscrivez-vous aux notifications auprès de votre système d'exploitation (OS) ou de votre fournisseur de notifications push en suivant la [configuration push Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

#### Éviter les appels de désinscription immédiats {#avoid-immediate-unregister-calls}

Évitez d'appeler `logout` ou `unregisterPush` directement après l'inscription aux notifications push auprès de l'OS ou du fournisseur de notifications push. En raison du traitement asynchrone côté serveur, cela peut dans de rares cas réajouter le jeton push à l'utilisateur Braze.

### Désinscription des notifications push {#unregister-push}

Pour cesser d'envoyer des notifications push à un appareil sans nettoyage automatique supplémentaire, utilisez la méthode `unregisterPush`. Celle-ci supprime le jeton push de l'appareil de l'utilisateur actuel sur le serveur Braze et efface le jeton stocké localement.

L'exemple de rappel suivant montre comment gérer les résultats de `unregisterPush`. Utilisez-le lorsque votre flux est basé sur des rappels, et remplacez la journalisation par votre propre gestion des nouvelles tentatives.

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

L'exemple de coroutine suivant montre l'API suspensive `unregisterPush`. Utilisez-le dans les flux basés sur des coroutines et personnalisez les branches de succès et d'échec pour votre application.

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

#### Réinscrire les notifications push après `unregisterPush` {#re-register-push-after-unregisterpush}

Après avoir appelé `unregisterPush`, réinscrivez-vous aux notifications auprès de votre OS ou de votre fournisseur de notifications push en suivant la [configuration push Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) avant d'envoyer à nouveau des notifications push Braze.

#### Éviter les appels de désinscription immédiats

Évitez d'appeler `logout` ou `unregisterPush` directement après l'inscription aux notifications push auprès de l'OS ou du fournisseur de notifications push. En raison du traitement asynchrone côté serveur, cela peut dans de rares cas réajouter le jeton push à l'utilisateur Braze.