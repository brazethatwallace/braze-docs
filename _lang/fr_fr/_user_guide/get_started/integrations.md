---
nav_title: Intégration
article_title: Aperçu de l'onboarding d'intégration
page_order: 8
page_type: reference
description: "Le présent article de référence couvre brièvement les étapes d'intégration dont vos ingénieurs ou développeurs ont besoin."

---

# Intégration {#integration}

> L'intégration avec Braze est un processus qui en vaut la peine. Mais vous êtes malin. Vous êtes **ici**. Il est clair que vous le savez déjà. Mais ce que vous ne savez probablement pas, c'est que vous et vos développeurs êtes sur le point d'entreprendre ensemble un voyage qui nécessite une expertise technique, une planification stratégique et une communication régulière pour bien coordonner vos efforts.

{% alert note %}
Notez que le contenu de cet article ne s'applique pas à l'e-mail. Consultez la section [Configuration de l'e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/).
{% endalert %}

## Le côté technique du processus d'intégration {#the-technical-side-of-the-integration-process}

Vous pourriez penser « Mes développeurs sont magiques ! Ils peuvent tout faire, donc je les laisse se débrouiller ! » Et c'est probablement vrai ! Mais il n'y a aucune raison de ne pas savoir ce qu'ils font en coulisses. En fait, cela faciliterait l'ensemble du processus si vous saviez quand intervenir avec des informations et ce qu'il faut chercher lorsqu'ils demandent : « Pouvez-vous m'envoyer la clé API et l'endpoint de l'API ? »

Alors, que font-ils lorsqu'ils intègrent Braze avec votre application ou votre site ? Bonne question !

### Étape 1 : Ils mettent en œuvre le SDK Braze {#step-1-they-implement-the-braze-sdk}

Le SDK Braze (Software Development Kit) est le moyen par lequel nous envoyons et recevons des informations depuis et vers votre application ou site. Vos ingénieurs relient essentiellement nos applications entre elles. Pour ce faire, ils ont besoin de quelques informations clés :

* Vos [clés API]({{site.baseurl}}/api/api_key/)
* Votre [endpoint SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)
  * Braze ne fournit plus d'endpoints personnalisés, utilisez donc les endpoints SDK prédéfinis. Si vous avez reçu un endpoint personnalisé préexistant, vous trouverez ici les étapes de configuration nécessaires pour l'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) et [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk).

Vous pouvez leur donner ces informations directement, ou leur donner accès à Braze en créant un compte pour eux.

{% alert warning %}
Assurez-vous que vous et vos développeurs ne modifiez pas sciemment ou involontairement les identifiants de la société dans Braze, car cela pourrait causer des problèmes au cours du processus de mise en œuvre ou verrouiller un ou plusieurs de vos comptes.
{% endalert %}

### Étape 2 : Ils mettent en œuvre les canaux de communication souhaités {#step-2-they-implement-your-desired-messaging-channels}

Braze propose de nombreuses options pour communiquer avec vos utilisateurs, chacune nécessitant sa propre configuration pour fonctionner comme vous le souhaitez. C'est là que la communication avec vos ingénieurs devient essentielle.

Assurez-vous d'indiquer à vos développeurs quels canaux vous souhaitez utiliser afin que la mise en œuvre soit effectuée efficacement et dans le bon ordre.

| Canal | Détails |
|---|---|
| Messages in-app | Nécessite la mise en œuvre du SDK ainsi que des étapes spécifiques à ce canal. |
| Notification push | Nécessite la mise en œuvre du SDK pour assurer une gestion adéquate des identifiants de messagerie et des jetons de notification push. |
| E-mail | Il s'agit d'un processus entièrement différent. Consultez la section [Configuration de l'e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/) pour plus de détails sur l'intégration. |
| Content Cards | Pour commencer à utiliser les [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/), veuillez contacter votre gestionnaire de la satisfaction client Braze. |
| SMS et MMS | Consultez la section [Configuration du SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending/) pour plus de détails sur l'intégration. |
| Webhooks | Nécessite la mise en œuvre du SDK ainsi que des étapes spécifiques à ce canal. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Vous pouvez utiliser Braze pour créer des campagnes de communication accessibles sur chaque canal. Vérifiez avec vos développeurs que vous respectez les normes d'accessibilité lors de la mise en œuvre.
{% endalert %}

### Étape 3 : Ils configurent vos données {#step-3-they-set-up-your-data}

Braze a plus d'un tour dans son sac. Il ne s'agit pas seulement d'envoyer des e-mails ou des notifications push. Il s'agit de créer des parcours client personnalisés, uniques pour chaque utilisateur et chaque client. Ces parcours sont basés sur les actions effectuées au sein de votre application ou de votre site, et c'est à vous de les définir ! La prochaine tâche de vos développeurs est de s'assurer que les actions réalisées dans votre application ou sur votre site sont bien captées par Braze.

Que devez-vous faire pour leur fournir ces informations ?

1. Travaillez avec votre équipe marketing pour définir les campagnes, les objectifs, les attributs et les événements dont vous devez assurer le suivi. Définissez ces cas d'utilisation et partagez-les avec vos équipes.
2. Définissez vos besoins en données personnalisées ([attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/), etc.).
3. À partir de là, discutez de la manière dont ces données doivent être suivies (déclenchées par le SDK, etc.).
4. Définissez le nombre d'[espaces de travail]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/) dont vous avez besoin. Vos ingénieurs devront savoir comment [tester et configurer]({{site.baseurl}}/user_guide/get_started/workspaces/) ces espaces de travail.

Une fois toutes ces informations rassemblées, partagez-les avec votre ingénieur. Il les utilisera pour mettre en œuvre vos [données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/). Vous devrez peut-être même [importer certains utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/). Pensez également à vous familiariser avec les [conventions de dénomination des événements]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions/).

### Étape 4 : Ils personnalisent en fonction de vos besoins {#step-4-they-customize-based-on-what-you-want}

Si vous souhaitez utiliser des fonctionnalités telles que le lancement déclenché par API et le contenu connecté, discutez-en avec votre contact Braze et vos développeurs pour vous assurer de pouvoir intégrer dans vos messages des données provenant de l'extérieur de votre application et de Braze.

### Étape 5 : Vous assurez tous deux l'assurance qualité de votre mise en œuvre {#step-5-you-both-perform-qa-on-your-implementation}

Travaillez avec votre ingénieur pour vous assurer que tout fonctionne. Envoyez des [messages de test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/), utilisez nos [applications de test pour Android]({{site.baseurl}}/developer_guide/references/?tab=android) et nos [applications de test pour iOS]({{site.baseurl}}/developer_guide/references/?tab=swift), vérifiez chaque point avant de commencer l'envoi !

Nous avons même des instructions spécifiques pour [tester votre intégration Android ou FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) et tester les [notifications push pour iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing/).

## Après la mise en œuvre {#after-implementation}

Gardez à l'esprit que la fin de la mise en œuvre ne signifie pas que vous pouvez envoyer un million de messages d'un coup. Envoyer un million de notifications push risque de faire planter votre application si chaque client clique simultanément sur le même lien. Nous vous recommandons de vérifier la capacité de votre infrastructure interne à traiter les requêtes provenant de Braze avant de cliquer sur le bouton **Send**. Vous pouvez ensuite définir votre [limite de débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#rate-limiting) en conséquence.

![]({% image_buster/assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Lorsque vous êtes à l'aise avec Braze, envisagez de devenir Braze Firebrand ! Avec Braze Firebrands, notre communauté d'engagement client, nous construisons une communauté de personnes engagées qui utilisent Braze pour moderniser leur expérience client et leur marketing. Vous souhaitez en savoir plus ? [Rejoignez-nous](https://brazefirebrands.splashthat.com/).