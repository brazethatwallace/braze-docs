---
nav_title: Intégration
article_title: Aperçu de l'onboarding d'intégration
page_order: 8
page_type: reference
description: "Cet article de référence couvre brièvement les étapes d'intégration dont vos ingénieurs ou développeurs ont besoin."
---

# Intégration {#integration}

> L'intégration avec Braze est un processus qui en vaut la peine. Mais vous êtes malin. Vous êtes **ici**. Il est clair que vous le savez déjà. Mais ce que vous ne savez probablement pas, c'est que vous et vos développeurs êtes sur le point d'entreprendre ensemble un voyage qui nécessite une expertise technique, une planification stratégique et une communication régulière pour bien coordonner vos efforts.

{% alert note %}
Notez que le contenu de cet article ne s'applique pas à l'e-mail. Consultez la section [Configuration de l'e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup).
{% endalert %}

## L'aspect technique du processus d'intégration {#the-technical-side-of-the-integration-process}

Vous vous dites peut-être : « Mes développeurs sont formidables ! Ils peuvent tout faire, alors je les laisse généralement s'en occuper ! » Et c'est probablement vrai ! Mais il n'y a aucune raison de ne pas comprendre ce qu'ils font en coulisses. En fait, cela faciliterait grandement le processus si vous saviez quand intervenir avec les bonnes informations et quoi chercher quand ils vous demandent : « Pouvez-vous m'envoyer la clé API et l'endpoint de l'API ? »

Alors, que font-ils exactement lorsqu'ils intègrent Braze à votre application ou votre site ? Bonne question !

### Étape 1 : Ils déploient le SDK Braze {#step-1-they-implement-the-braze-sdk}

Le SDK Braze (Software Development Kit) est le moyen par lequel nous envoyons et recevons des informations depuis votre application ou votre site. Vos ingénieurs relient, en quelque sorte, nos applications entre elles. Pour ce faire, ils ont besoin de quelques informations clés :

* Vos [clés API]({{site.baseurl}}/api/basics)
* Votre [endpoint du SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)
  * Braze ne fournit plus d'endpoints personnalisés, utilisez donc les endpoints SDK prédéfinis. Si un endpoint personnalisé préexistant vous a été attribué, vous trouverez ici les étapes de configuration pour l'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) et [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#initializing-the-sdk).

Vous pouvez soit leur fournir ces informations directement, soit leur donner accès à Braze en créant un compte pour eux.

{% alert warning %}
Assurez-vous que ni vous ni vos développeurs ne modifiez involontairement les identifiants de l'entreprise dans Braze, car cela pourrait causer des problèmes durant le processus de déploiement ou vous bloquer l'accès à vos comptes.
{% endalert %}

### Étape 2 : Ils déploient les canaux de communication souhaités {#step-2-they-implement-your-desired-messaging-channels}

Braze offre de nombreuses options pour communiquer avec vos utilisateurs, et chacune nécessite sa propre configuration ou ses propres ajustements pour fonctionner comme vous le souhaitez. C'est là que la communication avec vos ingénieurs devient essentielle.

Assurez-vous d'indiquer à vos développeurs quels canaux vous souhaitez utiliser afin que le déploiement soit réalisé efficacement et dans le bon ordre.

| Canal | Détails |
|---|---|
| Messages in-app | Nécessite le déploiement du SDK ainsi que des étapes spécifiques à ce canal. |
| Notifications push | Nécessite le déploiement du SDK pour gérer correctement les identifiants de communication et les jetons push. |
| E-mail | Il s'agit d'un processus entièrement différent. Consultez la section [Configuration de l'e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup) pour plus de détails sur l'intégration. |
| Content Cards | Pour démarrer avec les [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards), contactez votre gestionnaire du succès des clients Braze. |
| SMS et MMS | Consultez la section [Configuration des SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending) pour plus de détails sur l'intégration. |
| Webhooks | Nécessite le déploiement du SDK ainsi que des étapes spécifiques à ce canal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Ils déploient les canaux de communication souhaités" }

{% alert tip %}
Vous pouvez utiliser Braze pour créer des campagnes de communication accessibles sur chaque canal. Collaborez avec vos développeurs pour vous assurer que les normes d'accessibilité sont respectées dans votre déploiement.
{% endalert %}

### Étape 3 : Ils configurent vos données {#step-3-they-set-up-your-data}

Braze ne se limite pas à une seule fonctionnalité. Il ne s'agit pas simplement d'envoyer des e-mails ou des notifications push. Il s'agit de créer des parcours clients personnalisés, uniques pour chaque utilisateur et client. Ces parcours clients reposent sur les actions effectuées au sein de votre application ou de votre site, et c'est vous qui les définissez ! La prochaine tâche de vos développeurs est de s'assurer que les actions réalisées dans votre application ou votre site sont bien captées par Braze.

Alors, que devez-vous faire pour leur fournir ces informations ?

1. Collaborez avec votre équipe marketing pour définir les Campaigns, les objectifs, les attributs et les événements que vous devez suivre. Définissez ces cas d'usage et partagez-les avec vos équipes.
2. Définissez vos exigences en matière de données personnalisées ([attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events), etc.).
3. À partir de là, discutez de la manière dont ces données doivent être suivies (déclenchées via le SDK, etc.).
4. Définissez le nombre d'[espaces de travail]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces) dont vous avez besoin. Vos ingénieurs devront savoir comment [tester et configurer]({{site.baseurl}}/user_guide/get_started/workspaces) ces espaces de travail.

Une fois que vous avez rassemblé toutes ces informations, partagez-les avec votre ingénieur. Il les utilisera pour déployer vos [données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data). Vous pourriez même avoir besoin d'[importer certains utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users). Vous devriez également connaître les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

### Étape 4 : Ils personnalisent en fonction de vos besoins {#step-4-they-customize-based-on-what-you-want}

Si vous souhaitez des fonctionnalités telles que le lancement déclenché par API et le contenu connecté, discutez-en à la fois avec votre contact Braze et vos développeurs pour vous assurer que vous pourrez intégrer dans vos messages des données qui se trouvent en dehors de votre application et de Braze.

### Étape 5 : Vous effectuez ensemble l'assurance qualité de votre déploiement {#step-5-you-both-perform-qa-on-your-implementation}

Collaborez avec votre ingénieur pour vérifier que tout fonctionne correctement. Envoyez des [messages de test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages), utilisez nos [applications de test pour Android]({{site.baseurl}}/developer_guide/references?tab=android) et [applications de test pour iOS]({{site.baseurl}}/developer_guide/references?tab=swift), vérifiez chaque point avant de commencer à envoyer !

Nous proposons même des instructions spécifiques pour [tester votre intégration Android ou FireOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android) et tester les [notifications push pour iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing).

## Après le déploiement {#after-implementation}

Gardez à l'esprit que la fin du déploiement ne signifie pas que vous pouvez envoyer un million de messages d'un coup. Envoyer un million de notifications push pourrait faire planter votre application si tous les clients cliquent sur le même lien en même temps. Nous vous recommandons de discuter de la capacité de votre infrastructure interne à gérer les requêtes provenant de Braze avant de cliquer sur le bouton **Envoyer**. Vous pourrez ensuite définir votre [limitation du débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) en conséquence.

![Logo de la communauté Braze Firebrands]({% image_buster /assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Une fois que vous êtes à l'aise avec Braze, envisagez de devenir un Braze Firebrand ! Avec Braze Firebrands, notre communauté d'engagement client, nous construisons une communauté de pionniers qui utilisent Braze pour moderniser leur expérience client et leur marketing. Vous souhaitez en savoir plus ? [Rejoignez-nous maintenant](https://brazefirebrands.splashthat.com/).