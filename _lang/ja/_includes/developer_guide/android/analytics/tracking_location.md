## 現在地を記録する {#logging-the-current-location}

継続的な追跡が無効になっている場合でも、[`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) メソッドを使用して、ユーザーの現在地を手動で記録できます。

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

`````````kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
}
```

{% endtab %}
{% endtabs %}

## 位置情報の継続的な追跡 {#continuously-tracking-the-location}

{% alert important %}
[Android Marshmallow以降](https://developer.android.com/training/permissions/index.html)では、位置情報の追跡を明示的にオプトインするようユーザーに促す必要があります。ユーザーがオプトインすると、Brazeは次のセッションの開始時に位置情報の追跡を開始できます。これは、`AndroidManifest.xml` で位置情報の権限を宣言するだけで済んだ以前のバージョンのAndroidとは異なります。
{% endalert %}

ユーザーの位置情報を継続的に追跡するには、`AndroidManifest.xml` ファイルに以下の権限の少なくとも1つを追加して、アプリが位置情報データを収集する意図を宣言する必要があります。

| 権限 | 説明 |
|---|---|
| `ACCESS_COARSE_LOCATION` | 最もバッテリー効率の良い非GPSプロバイダー（ホームネットワークなど）を使用します。通常、ほとんどの位置情報のニーズにはこれで十分です。ランタイム権限モデルでは、位置情報の権限を付与すると、暗黙的に詳細な位置情報データの収集も許可されます。 |
| `ACCESS_FINE_LOCATION`   | より正確な位置情報のためのGPSデータを含みます。ランタイム権限モデルでは、位置情報の権限を付与すると、詳細な位置情報へのアクセスもカバーされます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Continuously tracking the location" }

`AndroidManifest.xml` は次のようになります。

`````````xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## 継続的な追跡を無効にする {#disabling-continuous-tracking}

継続的な追跡は、コンパイル時または実行時に無効にできます。

{% tabs local %}
{% tab compile time %}

コンパイル時に位置情報の継続的な追跡を無効にするには、`braze.xml` で `com_braze_enable_location_collection` を `false` に設定します。

`````````xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab runtime %}

実行時に位置情報の継続的な追跡を選択的に無効にするには、[`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration)を使用します。

{% subtabs %}
{% subtab JAVA %}

`````````java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsAutomaticLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

`````````kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsAutomaticLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}