## Enregistrement de l'emplacement/localisation actuel {#logging-the-current-location}

Même si le suivi continu est désactivé, vous pouvez enregistrer manuellement l'emplacement/localisation actuel de l'utilisateur à l'aide de la méthode [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html).

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
}
```

{% endtab %}
{% endtabs %}

## Suivi continu de l'emplacement/localisation {#continuously-tracking-the-location}

{% alert important %}
[À partir d'Android Marshmallow](https://developer.android.com/training/permissions/index.html), vous devez demander à vos utilisateurs d'accepter explicitement le suivi de l'emplacement/localisation. Une fois cette autorisation accordée, Braze peut commencer à suivre leur emplacement/localisation au début de la session suivante. Contrairement aux versions antérieures d'Android, il ne suffit plus de déclarer les autorisations d'emplacement/localisation dans votre fichier `AndroidManifest.xml`.
{% endalert %}

Pour suivre en continu l'emplacement/localisation d'un utilisateur, vous devez déclarer l'intention de votre application de collecter des données d'emplacement/localisation en ajoutant au moins l'une des autorisations suivantes à votre fichier `AndroidManifest.xml`.

| Autorisation | Description |
|---|---|
| `ACCESS_COARSE_LOCATION` | Utilise le fournisseur non GPS le plus économe en batterie (comme le réseau domestique). En général, cela suffit pour la plupart des besoins en données d'emplacement/localisation. Avec le modèle d'autorisations d'exécution, accorder l'autorisation d'emplacement/localisation autorise implicitement la collecte de données d'emplacement/localisation précises. |
| `ACCESS_FINE_LOCATION`   | Inclut les données GPS pour un emplacement/localisation plus précis. Avec le modèle d'autorisations d'exécution, accorder l'autorisation d'emplacement/localisation couvre également l'accès à l'emplacement/localisation précis. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Suivi continu de l'emplacement/localisation" }

Votre fichier `AndroidManifest.xml` devrait ressembler à ceci :

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## Désactivation du suivi continu {#disabling-continuous-tracking}

Vous pouvez désactiver le suivi continu au moment de la compilation ou de l'exécution.

{% tabs local %}
{% tab compile time %}

Pour désactiver le suivi continu de l'emplacement/localisation au moment de la compilation, définissez `com_braze_enable_location_collection` sur `false` dans `braze.xml` :

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab runtime %}

Pour désactiver de manière sélective le suivi continu de l'emplacement/localisation au moment de l'exécution, utilisez [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration) :

{% subtabs %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsAutomaticLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsAutomaticLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}