# Definir IDs de usuários {#setting-user-ids}

> Este artigo de referência mostra como definir IDs de usuários no seu app para Android ou FireOS, convenções de nomenclatura de IDs de usuários sugeridas e algumas práticas recomendadas.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Sugestão de convenção de nomenclatura de ID de usuário {#suggested-user-id-naming-convention}

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### Atribuindo um ID de usuário {#assigning-a-user-id}

A seguinte chamada deve ser feita assim que o usuário for identificado (geralmente após o login) para definir o ID do usuário:

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
**Não chame `changeUser()` quando um usuário fizer logout. `changeUser()` só deve ser chamado quando o usuário fizer login no aplicativo.** Definir `changeUser()` com um valor padrão estático associará TODAS as atividades do usuário a esse "usuário" padrão até que o usuário faça login novamente.
{% endalert %}

Além disso, recomendamos **não** alterar o ID do usuário quando um usuário faz logout, pois isso impede o direcionamento de campanhas de reengajamento para o usuário que estava conectado anteriormente. Se você espera que vários usuários usem o mesmo dispositivo, mas quer direcionar apenas um deles quando o app estiver em estado de logout, recomendamos manter separadamente o registro do ID de usuário que deseja direcionar enquanto estiver desconectado e voltar para esse ID de usuário como parte do processo de logout do app.

Consulte a documentação de [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) para saber mais.

### Inscrevendo-se em eventos de mudança de usuário {#subscribing-to-user-change-events}

Use [`subscribeToChangeUserEvents`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-change-user-events.html) para executar lógica quando o app muda de usuário com `changeUser()`. Este método está disponível no Android SDK 40.0.0 e versões posteriores.

O retorno de chamada do assinante é executado quando um usuário é alterado por meio de `changeUser()` e recebe um `BrazeUserChangeEvent`. O `BrazeUserChangeEvent` é disparado quando o usuário atual muda ou quando o SDK acabou de ser inicializado. O SDK pode disparar múltiplos eventos para o mesmo usuário, mesmo quando nenhuma transição ocorre.

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

## Práticas recomendadas e notas para integração de ID de usuário {#user-id-integration-best-practices-and-notes}

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Aliasing de usuários {#aliasing-users}

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}