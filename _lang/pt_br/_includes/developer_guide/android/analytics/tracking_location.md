## Registro do local atual {#logging-the-current-location}

Mesmo que o rastreamento contínuo esteja desativado, você pode registrar manualmente o local atual do usuário usando o método [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html).

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

## Monitoramento contínuo da localização {#continuously-tracking-the-location}

{% alert important %}
[A partir do Android Marshmallow](https://developer.android.com/training/permissions/index.html), você precisa solicitar que os usuários façam opt-in explícito no monitoramento de localização. Assim que aceitarem, a Braze poderá começar a rastrear a localização deles no início da próxima sessão. Isso é diferente das versões anteriores do Android, em que bastava declarar as permissões de local no `AndroidManifest.xml`.
{% endalert %}

Para rastrear continuamente a localização de um usuário, você precisa declarar a intenção do app de coletar dados de localização adicionando pelo menos uma das seguintes permissões ao arquivo `AndroidManifest.xml`.

| Permissão | Descrição |
|---|---|
| `ACCESS_COARSE_LOCATION` | Usa o provedor não GPS mais eficiente em termos de bateria (como uma rede doméstica). Normalmente, isso é suficiente para a maioria das necessidades de dados de localização. No modelo de permissões em tempo de execução, conceder a permissão de local autoriza implicitamente a coleta de dados de localização precisa. |
| `ACCESS_FINE_LOCATION`   | Inclui dados de GPS para uma localização mais precisa. No modelo de permissões em tempo de execução, conceder a permissão de local também abrange o acesso à localização precisa. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Continuously tracking the location" }

Seu `AndroidManifest.xml` deve ser semelhante ao seguinte:

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## Desativar o rastreamento contínuo {#disabling-continuous-tracking}

Você pode desativar o rastreamento contínuo em tempo de compilação ou em tempo de execução.

{% tabs local %}
{% tab compile time %}

Para desativar o monitoramento contínuo de localização em tempo de compilação, defina `com_braze_enable_location_collection` como `false` em `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab runtime %}

Para desativar seletivamente o monitoramento contínuo de localização em tempo de execução, use [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

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