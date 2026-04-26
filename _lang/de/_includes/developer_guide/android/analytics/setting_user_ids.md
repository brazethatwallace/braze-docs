# Nutzer-IDs festlegen {#setting-user-ids}

> Dieser Referenzartikel zeigt Ihnen, wie Sie Nutzer-IDs in Ihrer Android- oder FireOS-App festlegen, welche Namenskonventionen für Nutzer-IDs empfohlen werden und einige Best Practices.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Empfohlene Namenskonvention für Nutzer-IDs {#suggested-user-id-naming-convention}

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### Zuweisen einer Nutzer-ID {#assigning-a-user-id}

Sie sollten den folgenden Aufruf tätigen, sobald die Nutzer:in identifiziert wurde (in der Regel nach der Anmeldung), um die Nutzer-ID festzulegen:

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
**Rufen Sie `changeUser()` keinesfalls auf, wenn sich eine Nutzer:in abmeldet. `changeUser()` sollte nur aufgerufen werden, wenn sich die Nutzer:in in die Anwendung einloggt.** Wenn Sie `changeUser()` auf einen statischen Standardwert setzen, werden ALLE Nutzeraktivitäten mit dieser Standard-Nutzer:in verknüpft, bis sich die Nutzer:in erneut anmeldet.
{% endalert %}

Außerdem empfehlen wir, die Nutzer-ID bei der Abmeldung **nicht** zu ändern, da Sie dann die zuvor angemeldete Nutzer:in nicht mit Kampagnen zur erneuten Interaktion ansprechen können. Wenn Sie mit mehreren Nutzer:innen auf demselben Gerät rechnen, aber nur eine davon ansprechen möchten, wenn sich Ihre App im abgemeldeten Zustand befindet, empfehlen wir Ihnen, die Nutzer-ID, die Sie ansprechen möchten, während der Abmeldung separat zu verfolgen und im Rahmen des Abmeldevorgangs Ihrer App wieder zu dieser Nutzer-ID zu wechseln.

Weitere Informationen finden Sie in der [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)-Dokumentation.

### Abonnieren von Nutzerwechsel-Events {#subscribing-to-user-change-events}

Verwenden Sie [`subscribeToChangeUserEvents`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-change-user-events.html), um Logik auszuführen, wenn Ihre App mit `changeUser()` die Nutzer:in wechselt. Diese Methode ist ab Android SDK 40.0.0 verfügbar.

Der Subscriber-Callback wird ausgeführt, wenn eine Nutzer:in über `changeUser()` gewechselt wird, und empfängt ein `BrazeUserChangeEvent`. Das `BrazeUserChangeEvent` wird ausgelöst, wenn die aktuelle Nutzer:in gewechselt wurde oder wenn das SDK gerade initialisiert wurde. Das SDK kann mehrere Events für dieselbe Nutzer:in auslösen, auch wenn kein Wechsel stattfindet.

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

## Best Practices und Hinweise zur Nutzer-ID-Integration {#user-id-integration-best-practices-and-notes}

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Nutzer-Aliasing {#aliasing-users}

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}