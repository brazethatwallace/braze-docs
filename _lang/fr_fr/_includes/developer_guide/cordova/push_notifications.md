{% multi_lang_include developer_guide/prerequisites/cordova.md %} Une fois le SDK intégré, la fonctionnalité de notification push de base est activée par défaut. Pour utiliser les [notifications push riches]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) et les [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova), vous devrez les configurer individuellement. Pour utiliser les messages push iOS, vous devez également télécharger un certificat push valide.

{% alert warning %}
Chaque fois que vous ajoutez, supprimez ou mettez à jour vos plugins Cordova, Cordova écrasera le Podfile dans le projet Xcode de votre application iOS. Cela signifie que vous devrez reconfigurer ces fonctionnalités à chaque modification de vos plugins Cordova.
{% endalert %}

## Activation de la création de liens profonds push {#enabling-push-deep-linking}

Par défaut, le SDK Braze Cordova ne gère pas automatiquement les deep links provenant des notifications push. Pour activer la création de liens profonds push, suivez les étapes de configuration décrites dans [Création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova).
Pour plus de détails sur ces options et d'autres options de configuration push, consultez [Configurations facultatives]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

## Désactiver les notifications push de base (iOS uniquement) {#disabling-basic-push-notifications-ios-only}

Une fois le SDK Braze Cordova pour iOS intégré, la fonctionnalité de notification push de base est activée par défaut. Pour désactiver cette fonctionnalité dans votre application iOS, ajoutez ce qui suit à votre fichier `config.xml`. Pour plus d'informations, consultez [Configurations facultatives]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
