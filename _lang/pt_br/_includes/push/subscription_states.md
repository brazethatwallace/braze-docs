## Estados de inscrição push {#push-sub-states}

Um "estado de inscrição por push" na Braze identifica a preferência global de um **usuário** quanto ao desejo de receber notificações por push. Como o estado da inscrição é baseado no usuário, ele não é específico de nenhum app individual. Os estados de inscrição tornam-se sinalizadores úteis ao decidir quais usuários devem ser direcionados para notificações por push.

{% alert note %}
O estado da inscrição push de um usuário se aplica a todo o seu perfil de usuário, que inclui todos os dispositivos do usuário.
{% endalert %}

As seguintes opções de estado de inscrição existem: `Subscribed`, `Opted-In` e `Unsubscribed`.

Por padrão, para que seu usuário receba suas mensagens por push, o estado de inscrição por push deve ser `Subscribed` ou `Opted-In`, e ele deve ter o push em primeiro plano ativado. Você pode substituir essa configuração, se necessário, ao criar uma mensagem.

| Estado de aceitação | Descrição |
|---|---|
| `Subscribed` | Estado padrão da inscrição push quando um perfil de usuário é criado na Braze. |
| `Opted-In` | Um usuário expressou explicitamente uma preferência por receber notificações por push. A Braze move automaticamente o estado de aceitação de um usuário para `Opted-In` se o usuário aceitar um prompt de push em nível de sistema operacional.<br><br>Isso não se aplica a usuários do Android 12 ou inferior. |
| `Unsubscribed` | Um usuário cancelou explicitamente a inscrição de push por meio do seu app ou outros métodos fornecidos pela sua marca. Por padrão, as Campaigns de push da Braze visam apenas usuários que estão `Subscribed` ou `Opted-in` para push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de inscrição push" }

{% alert important %}
A Braze não altera automaticamente o estado da inscrição push de um usuário para `Unsubscribed`. Lembre-se de que, se o estado de inscrição por push de um usuário for `Unsubscribed`, então o filtro `Foreground Push Enabled` do usuário na segmentação é `false`.
{% endalert %}

### Registro de push e usuários contatáveis {#push-registration-and-reachable-users}

O estado de inscrição push reflete a preferência de um usuário, mas se ele conta como **contatável** para push no dashboard também depende do [registro de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle) — ou seja, um token de push em primeiro plano válido no perfil. Para saber como a Braze calcula as contagens por canal, consulte [Medir o tamanho do Segment or segmento or segmento]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

- **Campaigns e Canvas de push:** Usuários que não estão registrados para push não são incluídos em **Usuários contatáveis** para Push para Android ou Push para iOS nas estatísticas de público, mesmo quando o estado de inscrição push é `Subscribed` ou `Opted-In`.
- **Outros canais:** Os mesmos usuários ainda podem contar como contatáveis para outros canais para os quais se qualificam (por exemplo, e-mail ou mensagens no app).
- **Segments:** A associação ao Segment or segmento or segmento segue seus filtros. Usuários sem registro de push permanecem no Segment or segmento or segmento, a menos que um filtro os exclua (por exemplo, **Foreground Push Enabled**). A associação total ao Segment or segmento or segmento pode ser maior do que a soma de usuários exibidos nas linhas de **Usuários contatáveis** específicas de push.

Um perfil de usuário pode exibir o estado de inscrição push `Subscribed` sem que nenhum token de push esteja atribuído. Esses usuários ainda não contam para **Usuários contatáveis** para Push para Android ou Push para iOS até que a Braze registre um token válido.

Para definições de filtros, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Atualização dos estados de inscrição push {#update-push-subscription-state}

Veja a seguir as maneiras de atualizar o estado de inscrição por push de um usuário:

#### Aceitação automática (padrão) {#automatic-opt-in-default}

Por padrão, a Braze define o estado da inscrição push de um usuário como `Opted-In` quando ele autoriza pela primeira vez as notificações por push para o seu app. A Braze também faz isso quando um usuário reativa as permissões push nas configurações do sistema após tê-las desativado anteriormente.

{% tabs local %}
{% tab android %}
Para desativar esse comportamento padrão, adicione a seguinte propriedade ao arquivo `braze.xml` do seu projeto do Android Studio:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
No iOS, uma nova instalação normalmente exibe o estado de inscrição push como **`Subscribed`** até que o usuário permita as notificações. Depois que o usuário seleciona **Permitir** no prompt do sistema operacional, a Braze define o estado como **`Opted-In`** quando a aceitação automática está ativada. Se o usuário selecionar **Não permitir** e depois ativar o push nas Configurações do iOS, o estado é atualizado após o usuário registrar uma sessão — não no momento em que ele altera as Configurações.

A partir da [versão 7.5.0 do Braze Swift SDK or kit de desenvolvimento de software](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), você pode desativar ou personalizar ainda mais esse comportamento adicionando a configuração `optInWhenPushAuthorized` ao arquivo `AppDelegate.swift` do seu projeto Xcode:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### Integração SDK or kit de desenvolvimento de software {#sdk-integration}

Você pode atualizar o estado da inscrição de um usuário com o SDK or kit de desenvolvimento de software da Braze usando o método `setPushNotificationSubscriptionType` na [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) ou [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). Por exemplo, você pode usar esse método para criar uma página de configurações no seu app em que os usuários possam ativar ou desativar manualmente as notificações por push.

#### REST or transferir estado representacional API or interface de programação do aplicativo (API)

Você pode atualizar o estado de inscrição de um usuário com a REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze usando o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para atualizar o atributo [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object).

### Diferenças entre ativação de push e estado de inscrição push {#differences-between-push-enablement-and-push-subscription-status}

A ativação de push refere-se a se um usuário concedeu permissão em nível de sistema operacional ou navegador para receber notificações em um dispositivo específico. O estado de inscrição push é uma configuração em nível da Braze que representa a preferência global de um usuário para receber push em todo o seu perfil.

Quando a aceitação automática está ativada (o padrão), a Braze atualiza o estado de inscrição push de um usuário para `Opted-In` quando ele autoriza as notificações por push para o seu app ou reativa as permissões nas configurações do sistema (por exemplo, no iOS, Android 13+ e navegadores web compatíveis). Caso contrário, o estado de inscrição push do usuário permanece `Subscribed` até que você o altere explicitamente usando um método do SDK or kit de desenvolvimento de software ou uma chamada à REST or transferir estado representacional API or interface de programação do aplicativo (API).

A Braze não altera automaticamente o estado de inscrição push de um usuário para `Unsubscribed` quando ele desativa as notificações no nível do sistema operacional, navegador ou app. Para atualizar o estado de inscrição push de um usuário, você deve atualizá-lo na Braze. Por exemplo, se um usuário desativar o push em uma Central de Preferências no app, atualize o estado de inscrição push para `Unsubscribed` na Braze. A Braze não atualiza perfis de usuários com base na sua Central de Preferências. Para alinhar os estados de inscrição com as preferências do usuário no app, chame os métodos apropriados usando o SDK or kit de desenvolvimento de software (iOS ou Android) ou a REST or transferir estado representacional API or interface de programação do aplicativo (API). Para mais informações, consulte [Atualização dos estados de inscrição push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#update-push-subscription-state).

### Tokens de push importados (iOS) {#imported-push-tokens-ios}

Quando você [importa tokens de push do iOS]({{site.baseurl}}/api/objects_filters/user_attributes_object#push-token-import) com `push_token_import`, o estado de inscrição push do usuário normalmente é **`Subscribed`** até que ele registre uma sessão no seu app integrado com a Braze. Após a primeira sessão, a Braze pode atualizar o estado para **`Opted-In`** se a [aceitação automática](#automatic-opt-in-default) se aplicar (por exemplo, quando o usuário autoriza o push no iOS e `optInWhenPushAuthorized` está ativado).

Revise as **Configurações de contato** no perfil do usuário após a importação e novamente após a primeira sessão do usuário no app para confirmar o estado esperado.

### Verificação do estado de inscrição push {#checking-push-subscription-state}

![Perfil de usuário de John Doe com o estado de inscrição push definido como Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Você pode verificar o estado de inscrição por push de um usuário com a Braze de qualquer uma das seguintes maneiras:

* **Perfil do usuário:** Você pode acessar perfis de usuários individuais por meio do dashboard da Braze na página **[Pesquisa de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)**. Depois de encontrar o perfil de um usuário (por meio de endereço de e-mail, número de telefone ou ID de usuário externo), é possível selecionar a guia **Engagement** para visualizar e ajustar manualmente o estado da inscrição de um usuário.
* **Exportação da REST or transferir estado representacional API or interface de programação do aplicativo (API):** Você pode exportar perfis de usuários individuais em formato JSON usando os endpoints de exportação [Usuários por Segment or segmento or segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) ou [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier). A Braze retorna um objeto de tokens de push que contém informações de ativação de push por dispositivo.