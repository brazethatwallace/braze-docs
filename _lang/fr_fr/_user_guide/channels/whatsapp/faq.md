---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "Cet article répond aux questions les plus fréquemment posées lors de la configuration de campagnes WhatsApp."
page_type: FAQ
channel:
  - WhatsApp

---

# Questions fréquemment posées {#frequently-asked-questions}

> Sur cette page, nous tenterons de répondre à vos questions les plus pressantes sur WhatsApp !<br><br>Cette FAQ n'a pas vocation à fournir des conseils juridiques et ne saurait être utilisée à cette fin. L'utilisation du canal WhatsApp est soumise à des exigences spécifiques de Meta Platforms, Inc. Pour vous assurer que vous utilisez le canal WhatsApp en conformité avec toutes les exigences applicables et les lois auxquelles vous pourriez être spécifiquement soumis, vous devriez consulter votre conseiller juridique.

## Sujets de la FAQ {#faq-topics}
- [Comptes WhatsApp Business](#whatsapp-business-accounts)
- [Numéros de téléphone du compte WhatsApp Business](#whatsapp-business-account-phone-numbers)
- [Abonnement et gestion des abonnements](#opt-in-and-subscription-management)
- [Limites d'envoi de messages et évaluation de la qualité](#messaging-limits-and-quality-rating)
- [Modèles WhatsApp et compositeur](#whatsapp-templates-and-composer)
- [Livrabilité et facturation](#deliverability-and-billing)
- [Intégrations, données et reporting](#integrations-data-and-reporting)

### Comptes WhatsApp Business {#whatsapp-business-accounts}

#### Comment créer un compte WhatsApp Business ? {#how-do-i-create-a-whatsapp-business-account}
Nous vous recommandons de créer votre compte WhatsApp Business (WABA) via le flux d'inscription intégré dans le tableau de bord de Braze.

#### J'ai déjà un compte Meta Business. Ai-je quand même besoin d'un compte WhatsApp Business ? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
Oui, vous devez tout de même créer un compte WhatsApp Business. Nous vous recommandons de [rattacher votre WABA à votre compte Meta Business principal]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

#### Comment accéder à mon compte WhatsApp Business ? {#how-do-i-access-my-whatsapp-business-account}
Après avoir complété le flux d'inscription intégré, vous pouvez accéder à votre compte sur business.facebook.com en naviguant vers la [section WhatsApp](https://business.facebook.com/wa/manage/home).

#### Puis-je connecter plusieurs WABA à Braze ? {#can-i-connect-multiple-wabas-to-braze}
Oui, vous pouvez ajouter jusqu'à 10 comptes WhatsApp Business par espace de travail, et chaque compte Business peut être rattaché à un Meta Business Manager différent.

![Diagramme de l'écosystème Braze et WhatsApp, montrant comment les espaces de travail et les comptes WhatsApp Business se connectent entre eux : vous pouvez connecter un groupe d'abonnement à un numéro de téléphone, plusieurs comptes WhatsApp Business à un espace de travail, et un espace de travail à plusieurs Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### Puis-je changer la devise de mon compte WhatsApp Business ? {#can-i-change-my-whatsapp-business-account-currency}
Non. Meta contrôle la devise de votre compte WhatsApp Business, et Braze ne peut pas la modifier ni la convertir. Pour utiliser une devise différente, [créez un compte WhatsApp Business distinct]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) avec cette devise, ou contactez le support Meta pour demander s'ils peuvent mettre à jour la devise de votre compte existant.

#### Qu'est-ce que la vérification d'entreprise ? {#what-is-business-verification}
La vérification d'entreprise est un concept WhatsApp utilisé pour s'assurer que la marque est une entreprise légitime. Elle peut être complétée dans le WhatsApp Manager. La vérification d'entreprise est également requise pour augmenter les volumes d'envoi. Sans vérification d'entreprise, les clients ne peuvent envoyer des messages qu'à 250 utilisateurs finaux uniques maximum sur une période glissante de 24 heures.

#### Qu'est-ce qu'un compte professionnel officiel ? {#what-is-an-official-business-account}
L'OBA (Official Business Account) vous donne la coche verte à côté de votre nom d'affichage et est optionnel. Vous pouvez demander un compte professionnel officiel après avoir complété la vérification d'entreprise. Notez que la vérification d'entreprise et le compte professionnel officiel sont des concepts WhatsApp différents.

### Numéros de téléphone du compte WhatsApp Business {#whatsapp-business-account-phone-numbers}
#### Ai-je besoin d'un numéro de téléphone pour mon compte WhatsApp Business ? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
Oui, vous avez besoin d'un numéro auquel vous avez accès. Il vous sera demandé de vérifier votre numéro de téléphone avec l'authentification à deux facteurs lors du flux d'inscription intégré. Le numéro de téléphone ne peut pas être utilisé pour d'autres comptes WhatsApp (professionnels ou personnels).

#### Quels types de numéros de téléphone sont pris en charge par WhatsApp ? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
Consultez les exigences de Meta concernant les [numéros de téléphone](https://developers.facebook.com/docs/whatsapp/phone-numbers) pour plus d'informations.

#### Puis-je utiliser un même numéro de téléphone sur plusieurs WABA ? {#can-i-use-one-phone-number-across-multiple-wabas}
Non. Un numéro de téléphone ne peut pas être partagé entre plusieurs WABA.

#### Ai-je besoin d'un type spécifique de numéro de téléphone pour envoyer des messages vers certains pays ? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
Non. WhatsApp vous permet d'envoyer des messages aux utilisateurs finaux depuis n'importe quel numéro de téléphone pris en charge, dans n'importe quel pays. Consultez les exigences de Meta concernant les [numéros de téléphone](https://developers.facebook.com/docs/whatsapp/phone-numbers) pour plus d'informations.

#### Comment les numéros de téléphone des utilisateurs doivent-ils être stockés dans Braze ? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
Les numéros de téléphone des utilisateurs doivent être stockés au [format E.164]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting).

#### Puis-je importer des numéros de téléphone d'utilisateurs ? {#can-i-import-user-phone-numbers}
Oui. Vous pouvez [importer des numéros de téléphone d'utilisateurs]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers).

### Abonnement et gestion des abonnements {#opt-in-and-subscription-management}

#### Dois-je recueillir le consentement pour envoyer des messages marketing aux utilisateurs finaux sur WhatsApp ? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
Oui, WhatsApp exige que les entreprises [recueillent le consentement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) pour envoyer des messages marketing aux utilisateurs finaux.

#### Puis-je contacter proactivement les utilisateurs finaux sur WhatsApp pour recueillir leur consentement ? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
Si vous choisissez de contacter proactivement les utilisateurs finaux, votre premier message initié par l'entreprise devrait demander à l'utilisateur s'il souhaite recevoir des messages marketing de votre entreprise et devrait être conforme aux exigences de Meta pour [l'obtention du consentement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Gardez à l'esprit que WhatsApp surveille la réputation de votre entreprise sur le canal, et la bonne pratique recommandée est d'être explicite avec les utilisateurs finaux et de n'envoyer que les messages qu'ils ont indiqué vouloir recevoir.

#### Dois-je recueillir le numéro de téléphone de l'utilisateur final lorsque je recueille le consentement ? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
Vous devez disposer du numéro de téléphone de l'utilisateur final sur le profil Braze pour lui envoyer des messages.
- Si vous avez déjà son numéro, vous n'avez pas besoin de le recueillir lors de l'abonnement.
- Si vous n'avez pas le numéro de l'utilisateur final, votre méthode d'abonnement devrait inclure la collecte du numéro de téléphone.

#### Comment mettre à jour le statut d'abonnement des utilisateurs finaux qui s'abonnent ? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
La gestion des abonnements du canal WhatsApp fonctionne de manière similaire aux autres canaux Braze. Consultez [Gérer les abonnements des utilisateurs]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) pour plus d'informations.

#### Si j'ai déjà une liste d'utilisateurs qui ont consenti à recevoir des messages marketing sur WhatsApp, comment mettre à jour leur statut d'abonnement dans Braze ? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
Vous pouvez mettre à jour leur statut d'abonnement via l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#importing-custom-data).

#### Quelles méthodes dois-je utiliser pour recueillir les consentements ? {#what-methods-should-i-use-to-collect-opt-ins}
Braze recommande de consulter les [directives de Meta sur les méthodes de consentement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) pour maintenir la conformité. Consultez la ressource suivante pour des [idées et suggestions de canaux et d'abonnement](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit) de Braze.

#### Le double consentement est-il requis pour WhatsApp ? {#is-double-opt-in-required-for-whatsapp}
Non, le double consentement n'est pas requis.

#### Comment mes utilisateurs se désabonnent-ils des messages WhatsApp ? {#how-do-my-users-opt-out-of-whatsapp-messages}
Vos utilisateurs peuvent se désabonner de deux manières :
1. Configurez un message WhatsApp entrant avec un mot de désabonnement spécifique et utilisez un webhook pour mettre à jour le statut d'abonnement de l'utilisateur.
2. Ajoutez une réponse rapide de désabonnement dans le modèle WhatsApp, avec un webhook correspondant pour la mise à jour.

### Limites d'envoi de messages et évaluation de la qualité {#messaging-limits-and-quality-rating}

#### Que sont les limites d'envoi de messages ? {#what-are-messaging-limits}
Les limites d'envoi de messages sont un concept d'intégrité WhatsApp. Elles déterminent le nombre maximum de conversations initiées par l'entreprise que chaque numéro de téléphone peut démarrer sur une période glissante de 24 heures. Il existe quatre niveaux de limites d'envoi : 1k, 10k, 100k et illimité.

#### Comment augmenter ma limite d'envoi de messages ? {#how-do-i-increase-my-messaging-limit}
WhatsApp augmentera votre limite d'envoi de messages si vous remplissez les conditions suivantes :
1. Le [statut du numéro de téléphone](https://www.facebook.com/business/help/896873687365001) est **Connected**
2. L'[évaluation de la qualité du numéro de téléphone](https://www.facebook.com/business/help/896873687365001) est **Medium** ou **High**
3. Au cours des sept derniers jours, vous avez initié X conversations ou plus avec des utilisateurs uniques, où X correspond à votre limite d'envoi actuelle divisée par 2

Ainsi, pour passer de 100k à illimité, vous devez envoyer au moins 50 000 conversations initiées par l'entreprise sur une période de 7 jours.

#### Combien de temps faut-il pour augmenter mes limites d'envoi de messages ? {#how-long-does-it-take-to-increase-my-messaging-limits}
Si toutes les conditions précédentes sont remplies, vous pouvez augmenter votre limite d'envoi de 1k à illimité en 4 jours.

#### Où puis-je voir ma limite d'envoi actuelle ? {#where-can-i-see-my-current-messaging-limit}
Vous pouvez vérifier vos limites d'envoi actuelles dans l'onglet **WhatsApp Manager > Overview Dashboard > Insights**.

#### Que se passe-t-il si je tente d'envoyer des messages alors que j'ai déjà atteint ma limite d'envoi ? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
Si vous essayez d'envoyer une campagne ou un Canvas à plus d'utilisateurs uniques que votre limite actuelle ne le permet, les messages ne seront pas envoyés. Braze continuera de tenter de renvoyer les messages si/quand votre limite d'envoi augmente, pendant une durée maximale d'un jour.

#### Ma limite d'envoi de messages peut-elle diminuer ? {#can-my-messaging-limit-decrease}
Oui, si l'évaluation de la qualité de votre numéro de téléphone baisse trop, vous risquez que WhatsApp diminue votre limite d'envoi. Braze vous recommande de vous abonner aux notifications de mises à jour liées à la qualité de WhatsApp, y compris les mises à jour du statut de votre numéro de téléphone et du niveau de limite d'envoi. Vous pouvez vous abonner aux notifications directement dans le tableau de bord du WhatsApp Manager.

#### Quels facteurs affectent l'évaluation de la qualité du numéro de téléphone, et que se passe-t-il lorsque mon évaluation de qualité baisse trop ? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
Les facteurs qui affectent l'évaluation de la qualité du numéro de téléphone incluent le blocage de l'entreprise par un utilisateur final (et les raisons qu'il fournit lors du blocage) et le signalement de l'entreprise par un utilisateur final.

Lorsqu'une évaluation de qualité est basse, le statut du numéro de téléphone passe de **Connected** à **Flagged**. Si la qualité ne s'améliore pas en sept jours, le statut revient à **Connected**. Cependant, la limite d'envoi de messages diminuera au niveau inférieur. Par exemple, un numéro de téléphone qui avait une limite d'envoi de 100 000 aura désormais une limite de 10 000.

#### Quelle est la limite de débit de Meta ? {#what-is-the-meta-throughput-limit}
Meta dispose de sa propre limite de débit, distincte de la limite d'envoi du WABA. La limite par défaut prise en charge par l'API cloud est de 80 messages par seconde. Si vous pensez que vos campagnes dépasseront cette limite, vous pouvez [demander](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) une augmentation de votre limite. Meta recommande de soumettre cette demande au moins trois jours avant les envois de campagnes.

### Modèles WhatsApp et compositeur {#whatsapp-templates-and-composer}

#### Qu'est-ce qu'un modèle WhatsApp ? {#what-is-a-whatsapp-template}
WhatsApp exige que tous les messages initiés par l'entreprise commencent par un modèle approuvé. Le modèle inclut le texte du message, ainsi que des médias enrichis optionnels comme des images, des appels à l'action et des boutons de réponse rapide. Une fois les modèles approuvés par WhatsApp, ils peuvent être utilisés pour composer un message WhatsApp dans Braze.

#### Où puis-je créer, modifier et gérer mes modèles WhatsApp ? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Vous créerez, modifierez, gérerez et soumettrez vos modèles pour approbation directement dans le WhatsApp Manager. Une fois votre WABA connecté à Braze, vous verrez tous vos modèles dans le tableau de bord avec un indicateur de statut. Si un modèle est rejeté, vous le soumettrez à nouveau directement via le WhatsApp Manager. **Les modèles ne peuvent pas être créés ou modifiés directement dans Braze.**

#### Combien de temps faut-il à WhatsApp pour examiner une soumission de modèle ? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
Le processus d'approbation peut prendre jusqu'à 24 heures, mais souvent les modèles sont traités en quelques heures ou minutes.

#### Combien de modèles puis-je avoir à un moment donné ? {#how-many-templates-can-i-have-at-a-given-time}
Votre limite de modèles de messages dépend de votre statut de vérification d'entreprise. Vous pouvez vérifier votre limite sur la page **WhatsApp Manager > Message Templates**.

#### Comment personnaliser le texte et les médias enrichis des modèles dans Braze ? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsApp permet d'insérer des paramètres variables dans les modèles de messages. Les messages ne peuvent pas commencer ni se terminer par un paramètre variable. Les paramètres variables peuvent être remplis avec la logique Liquid dans la plateforme Braze. Consultez [Composer un message WhatsApp dans Braze]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) pour en savoir plus sur les paramètres variables.

#### Mon modèle a été rejeté. Braze peut-il m'aider à le faire approuver ? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
L'équipe Braze n'a pas de visibilité sur les rejets de modèles. Vous devez travailler directement avec votre WhatsApp Business Manager pour modifier et soumettre à nouveau le modèle. Assurez-vous de fournir un exemple de modèle si nécessaire. Vérifiez que votre modèle respecte les politiques [commerciales](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) ou de [commerce](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) de Meta.

#### Les médias enrichis peuvent-ils être ciblés ou personnalisés dans Braze ? {#can-the-rich-media-be-targeted-or-personalized-in-braze}
Les images peuvent être téléchargées depuis la bibliothèque multimédia mais ne peuvent pas être ciblées dynamiquement. Pour les URL, la dernière partie du lien peut être [remplie dynamiquement à l'aide de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls).

#### Quels types de médias enrichis sont pris en charge dans les modèles WhatsApp ? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
Vous pouvez ajouter des images, des appels à l'action (URL ou numéro de téléphone) et des boutons de réponse rapide aux modèles WhatsApp. Vous pouvez ajouter ces éléments lorsque vous créez des modèles directement dans WhatsApp.

#### Que faire si mon modèle a été signalé à tort pour violation de la politique commerciale de WhatsApp ? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Si vous pensez que Meta a signalé votre modèle à tort, utilisez le lien de révision dans l'e-mail de WhatsApp pour demander un réexamen. L'équipe WhatsApp Business examine la décision et l'annule si nécessaire.

#### Pourquoi mon modèle WhatsApp importé affiche-t-il « Message Incomplete » dans le compositeur ? {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
L'avertissement « Message Incomplete » apparaît lorsque les emplacements de variables obligatoires du modèle ne sont pas remplis avec des valeurs valides dans le compositeur.

Lorsque vous créez des modèles à l'aide du [générateur de modèles WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), Braze renumérote les variables en marques substitutives séquentielles ({% raw %}`{{1}}`, `{{2}}`, `{{3}}`{% endraw %}, etc.). Les modèles créés en externe dans le WhatsApp Manager de Meta peuvent encore contenir des schémas qui rendent le mappage des variables sujet aux erreurs, tels que :

- Une numérotation non séquentielle (par exemple, {% raw %}`{{1}}`, `{{3}}`, `{{5}}`{% endraw %})
- Des variables manquantes dans la séquence (par exemple, {% raw %}`{{2}}`{% endraw %} est ignoré)
- Des variables qui commencent à un numéro autre que 1

Pour résoudre ce problème, modifiez votre modèle dans le WhatsApp Manager de Meta afin d'utiliser un format de marques substitutives séquentiel, puis réimportez-le dans Braze. Dans Braze, confirmez que chaque champ de variable obligatoire est rempli avec une valeur Liquid valide.

### Livrabilité et facturation {#deliverability-and-billing}

#### Pourquoi un message ne serait-il pas livré ? {#why-would-a-message-not-be-delivered}
Il existe diverses raisons pour lesquelles un message pourrait ne pas être livré, notamment des problèmes de réseau ou un appareil éteint.

#### Si un message n'est pas livré, serai-je facturé ? {#if-a-message-is-not-delivered-will-i-be-billed}
Non. Si un message n'est pas livré, vous ne serez pas facturé.

#### Que se passe-t-il si un utilisateur final bloque mon entreprise ? {#what-happens-if-an-end-user-blocks-my-business}
Si un utilisateur final bloque votre entreprise, les messages suivants que vous tenterez d'envoyer ne seront pas livrés, et vous ne serez pas facturé.

#### Que se passe-t-il si un utilisateur final signale un message ? {#what-happens-if-an-end-user-reports-a-message}
Si un utilisateur final signale un message, vous pouvez toujours envoyer des messages ultérieurs à cet utilisateur. Cependant, le signalement peut affecter votre évaluation de qualité sur le canal.

#### Si un utilisateur final bloque ou signale mon entreprise, son statut d'abonnement sera-t-il mis à jour dans Braze ? {#if-an-end-user-blocks-or-reports-my-business-will-their-subscription-status-be-updated-in-braze}
Non. Son statut d'abonnement Braze ne sera pas mis à jour.

### Intégrations, données et reporting {#integrations-data-and-reporting}

#### Braze prend-il en charge les cas d'usage de support client comme les chatbots et le chat assisté par un humain pour WhatsApp ? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Nous ne prenons pas en charge les chatbots ni le chat assisté par un humain au sein de Braze ou via des intégrations directes.

Si vous utilisez déjà WhatsApp comme canal de support client, nous vous recommandons de conserver votre configuration actuelle et de créer un nouveau WABA via Braze pour l'envoi de messages marketing. Ce WABA nécessitera un nouveau numéro de téléphone.

#### Comment puis-je « faire le lien » entre mes messages de support client et mes messages marketing via Braze ? {#how-can-i-bridge-the-gap-between-my-customer-support-messaging-and-my-marketing-messaging-via-braze}
Vous pouvez utiliser les propriétés Liquid de WhatsApp pour transférer le contenu des messages WhatsApp entrants (y compris le corps du message et les URL des médias) de Braze vers d'autres plateformes, y compris tout outil de support client. Pour plus de détails, consultez nos [balises de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Pour envoyer des informations dans Braze, par exemple pour indiquer qu'un utilisateur est dans une conversation de support active, vous pouvez enregistrer un attribut personnalisé (comme un booléen « conversation de support existante = vrai/faux ») et l'utiliser comme critère de segmentation dans vos campagnes marketing. Vous pouvez également créer des deep links entre deux fils de discussion pour diriger les utilisateurs vers le fil de support depuis le fil marketing et inversement.

#### Braze stocke-t-il les réponses des utilisateurs ? {#does-braze-store-user-responses}
Les messages ne sont stockés que le temps nécessaire à leur traitement. Pour accéder aux messages des utilisateurs, utilisez Currents.

#### Quels indicateurs sont disponibles dans le tableau de bord de Braze ? {#what-metrics-are-available-in-the-braze-dashboard}
Vous pouvez voir les destinataires uniques, les envois, les livraisons, les lectures et les échecs dans le tableau de bord de Braze. Notez que les accusés de lecture des utilisateurs finaux doivent être activés pour que Braze puisse suivre les lectures. Vous pouvez également configurer des événements de conversion pour surveiller les performances des campagnes, de manière similaire aux autres canaux.

#### Qu'est-ce qu'une conversation WhatsApp ? {#what-is-a-whatsapp-conversation}
WhatsApp est un canal axé sur la messagerie bidirectionnelle et s'articule donc autour des conversations (plutôt que du nombre de messages individuels). Une conversation est un fil de 24 heures entre une entreprise et un utilisateur final.

- **Conversation initiée par l'entreprise** : une conversation où l'entreprise commence en envoyant un modèle de message approuvé à l'utilisateur final. Dès que l'entreprise envoie un message, la fenêtre de 24 heures commence.
- **Conversation initiée par l'utilisateur** : une conversation où l'utilisateur final envoie un message à l'entreprise. Lorsque l'entreprise envoie un message en réponse, la fenêtre de 24 heures commence.