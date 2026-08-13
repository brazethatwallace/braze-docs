{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Effacer les données précédemment stockées {#wiping-previously-stored-data}

Le SDK Roku n'inclut pas de méthode `wipeData`. Pour obtenir un état vierge fonctionnellement équivalent à `wipeData()` sur les autres SDK Braze, effacez les quatre sections de registre Braze, puis réinitialisez le SDK.

Le SDK Roku de Braze conserve les données dans les sections de registre suivantes :

| Section | Contenu |
|---------|----------|
| `braze.section.device_id` | L'UUID de l'appareil utilisé pour identifier cet appareil dans Braze. |
| `braze.section.user_id` | L'ID utilisateur externe, s'il a été défini. |
| `braze.section.session` | L'UUID de la session active, l'heure de début et l'heure de fin. |
| `braze.section.config` | La configuration du SDK mise en cache et les données de feature flags. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Effacer les données précédemment stockées" }

### Étape 1 : Effacer les sections de registre {#step-1-clear-the-registry-sections}

Utilisez [`roRegistry.Delete()`](https://developer.roku.com/docs/references/brightscript/components/roregistry.md) pour supprimer chaque section Braze, puis appelez `Flush()` pour persister les modifications :

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

### Étape 2 : Réinitialiser le SDK Braze {#step-2-re-initialize-the-braze-sdk}

Lorsque vous [initialisez à nouveau le SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku), le SDK gère l'absence de données de registre de manière transparente :

- La section de l'ID d'appareil est vide, le SDK génère donc un nouvel UUID et traite l'appareil comme anonyme.
- La section de l'ID utilisateur est vide, le SDK utilise donc par défaut un utilisateur anonyme (une chaîne de caractères vide `""`).
- La section de session est vide, le SDK démarre donc une nouvelle session.
- La section de configuration est vide, le SDK récupère donc la configuration depuis le serveur.

{% alert note %}
Le SDK Roku ne génère aucune requête de suppression côté serveur lorsque vous effacez le registre. Si vous devez également supprimer l'utilisateur de Braze, envoyez une requête à [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) en utilisant l'`external_id` ou le `braze_id` de l'utilisateur.
{% endalert %}

## Déconnexion et désinscription des notifications push {#logout-and-unregister-push}

Cette fonctionnalité n'est pas encore prise en charge par le sdk Roku.