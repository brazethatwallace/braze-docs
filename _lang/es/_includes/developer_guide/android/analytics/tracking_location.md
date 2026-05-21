## Registro de la ubicación actual {#logging-the-current-location}

Aunque el seguimiento continuo esté desactivado, puedes registrar manualmente la ubicación actual del usuario utilizando el método [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html).

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

## Seguimiento continuo de la ubicación {#continuously-tracking-the-location}

{% alert important %}
[A partir de Android Marshmallow](https://developer.android.com/training/permissions/index.html), debes pedir a tus usuarios que acepten explícitamente la adhesión voluntaria al seguimiento de ubicación. Una vez que lo hagan, Braze puede empezar a rastrear su ubicación al inicio de la siguiente sesión. Esto difiere de las versiones anteriores de Android, en las que solo era necesario declarar los permisos de ubicación en tu `AndroidManifest.xml`.
{% endalert %}

Para realizar un seguimiento continuo de la ubicación de un usuario, tendrás que declarar la intención de tu aplicación de recopilar datos de ubicación añadiendo al menos uno de los siguientes permisos a tu archivo `AndroidManifest.xml`.

| Permiso | Descripción |
|---|---|
| `ACCESS_COARSE_LOCATION` | Utiliza el proveedor no GPS que consume menos batería (como una red doméstica). Normalmente, esto es suficiente para la mayoría de las necesidades de datos de ubicación. Según el modelo de permisos en tiempo de ejecución, conceder el permiso de ubicación autoriza implícitamente la recopilación de datos de ubicación precisa. |
| `ACCESS_FINE_LOCATION`   | Incluye datos GPS para una ubicación más precisa. Según el modelo de permisos en tiempo de ejecución, conceder el permiso de ubicación también cubre el acceso a la ubicación precisa. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Continuously tracking the location" }

Tu `AndroidManifest.xml` debe ser similar al siguiente:

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## Desactivar el seguimiento continuo {#disabling-continuous-tracking}

Puedes desactivar el seguimiento continuo en tiempo de compilación o de ejecución.

{% tabs local %}
{% tab compile time %}

Para desactivar el seguimiento de ubicación continuo en tiempo de compilación, configura `com_braze_enable_location_collection` como `false` en `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab runtime %}

Para desactivar selectivamente el seguimiento de ubicación continuo en tiempo de ejecución, utiliza [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

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