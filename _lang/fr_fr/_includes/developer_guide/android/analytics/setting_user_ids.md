# Définir les ID d'utilisateur {#setting-user-ids}

> Cet article de référence explique comment définir des ID utilisateur dans votre application Android ou FireOS, les conventions de dénomination d'ID utilisateur recommandées, ainsi que certaines bonnes pratiques.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Convention de dénomination des ID utilisateurs suggérée {#suggested-user-id-naming-convention}

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### Attribuer un ID utilisateur {#assigning-a-user-id}

Vous devez effectuer l'appel suivant dès que l'utilisateur est identifié (généralement après la connexion) pour définir l'ID utilisateur :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**N'appelez pas `changeUser()` lorsqu'un utilisateur se déconnecte. `changeUser()` ne doit être appelé que lorsque l'utilisateur se connecte à l'application.** Définir `changeUser()` sur une valeur par défaut statique associera TOUTES les activités de l'utilisateur avec cet « utilisateur » par défaut jusqu'à ce qu'il se connecte à nouveau.
{% endalert %}

De plus, nous vous déconseillons de changer l'ID utilisateur lorsqu'un utilisateur se déconnecte, car cela vous empêche de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous anticipez plusieurs utilisateurs sur le même appareil, mais que vous souhaitez uniquement cibler l'un d'entre eux lorsque votre application est à l'état déconnecté, nous vous recommandons de suivre séparément l'ID utilisateur que vous souhaitez cibler durant la déconnexion et de basculer vers cet ID utilisateur dans le cadre du processus de déconnexion de votre application.

Consultez la documentation [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) pour plus d'informations.

### S'abonner aux événements de changement d'utilisateur {#subscribing-to-user-change-events}

Utilisez [`subscribeToChangeUserEvents`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-change-user-events.html) pour exécuter une logique lorsque votre application change d'utilisateur avec `changeUser()`. Cette méthode est disponible à partir de la version 40.0.0 du SDK Android.

Le rappel de l'abonné s'exécute lorsqu'un changement d'utilisateur est effectué via `changeUser()` et reçoit un `BrazeUserChangeEvent`. `BrazeUserChangeEvent` est déclenché lorsque l'utilisateur actuel a changé ou lorsque le SDK vient d'être initialisé. Le SDK peut déclencher plusieurs événements pour le même utilisateur, même lorsqu'aucune transition n'a lieu.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToChangeUserEvents(new IEventSubscriber<BrazeUserChangeEvent>() {
  @Override
  public void trigger(BrazeUserChangeEvent event) {
    // Add your app logic for user changes, such as refreshing user-scoped state.
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToChangeUserEvents { event ->
  // Add your app logic for user changes, such as refreshing user-scoped state.
}
```

{% endtab %}
{% endtabs %}

## Bonnes pratiques et remarques sur l'intégration de l'ID utilisateur {#user-id-integration-best-practices-and-notes}

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Alias d'utilisateurs {#aliasing-users}

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}