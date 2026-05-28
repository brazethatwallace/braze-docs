## Aufzeichnung des aktuellen Standorts {#logging-the-current-location}

Auch wenn das kontinuierliche Tracking deaktiviert ist, können Sie den aktuellen Standort der Nutzer:innen manuell mit der Methode [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) aufzeichnen.

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

## Kontinuierliches Standort-Tracking {#continuously-tracking-the-location}

{% alert important %}
[Ab Android Marshmallow](https://developer.android.com/training/permissions/index.html) müssen Sie Ihre Nutzer:innen auffordern, dem Standort-Tracking ausdrücklich per Opt-in zuzustimmen. Sobald dies geschehen ist, kann Braze zu Beginn der nächsten Sitzung mit dem Tracking ihres Standorts beginnen. Dies unterscheidet sich von früheren Android-Versionen, bei denen lediglich die Angabe von Standortberechtigungen in Ihrer `AndroidManifest.xml` erforderlich war.
{% endalert %}

Um den Standort von Nutzer:innen kontinuierlich zu tracken, müssen Sie die Absicht Ihrer App, Standortdaten zu erfassen, deklarieren, indem Sie mindestens eine der folgenden Berechtigungen zu Ihrer `AndroidManifest.xml`-Datei hinzufügen.

| Berechtigung | Beschreibung |
|---|---|
| `ACCESS_COARSE_LOCATION` | Verwendet den batterieeffizientesten, nicht-GPS-basierten Anbieter (z. B. ein Heimnetzwerk). In der Regel reicht dies für die meisten Anforderungen an Standortdaten aus. Im Rahmen des Laufzeit-Berechtigungsmodells wird durch die Erteilung der Standortberechtigung implizit auch die Erfassung präziser Standortdaten genehmigt. |
| `ACCESS_FINE_LOCATION`   | Enthält GPS-Daten für eine genauere Standortbestimmung. Im Rahmen des Laufzeit-Berechtigungsmodells umfasst die Erteilung der Standortberechtigung auch den Zugriff auf präzise Standortdaten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Continuously tracking the location" }

Ihre `AndroidManifest.xml` sollte in etwa so aussehen:

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## Deaktivieren des kontinuierlichen Trackings {#disabling-continuous-tracking}

Sie können das kontinuierliche Tracking zur Kompilierungszeit oder zur Laufzeit deaktivieren.

{% tabs local %}
{% tab compile time %}

Um das kontinuierliche Standort-Tracking zur Kompilierungszeit zu deaktivieren, setzen Sie `com_braze_enable_location_collection` in `braze.xml` auf `false`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab runtime %}

Um das kontinuierliche Standort-Tracking zur Laufzeit selektiv zu deaktivieren, verwenden Sie [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

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