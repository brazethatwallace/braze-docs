{% multi_lang_include developer_guide/prerequisites/cordova.md %} Após integrar o SDK, a funcionalidade básica de notificação por push é ativada por padrão. Para usar [notificações por push ricas]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) e [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova), você precisará configurá-las individualmente. Para usar mensagens push no iOS, você também precisa fazer upload de um certificado push válido.

{% alert warning %}
Sempre que você adicionar, remover ou atualizar seus plugins Cordova, o Cordova irá sobrescrever o Podfile no projeto Xcode do seu app iOS. Isso significa que você precisará configurar esses recursos novamente sempre que modificar seus plugins Cordova.
{% endalert %}

## Ativando o deep linking por push {#enabling-push-deep-linking}

Por padrão, o SDK da Braze para Cordova não lida automaticamente com deep links de notificações por push. Para ativar o deep linking por push, siga as etapas de configuração em [Deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova).
Para saber mais sobre essas e outras opções de configuração de push, consulte [Configurações opcionais]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

## Desativando notificações por push básicas (apenas iOS) {#disabling-basic-push-notifications-ios-only}

Após integrar o SDK da Braze para Cordova no iOS, a funcionalidade básica de notificação por push é ativada por padrão. Para desativar essa funcionalidade no seu app iOS, adicione o seguinte ao seu arquivo `config.xml`. Para saber mais, consulte [Configurações opcionais]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
