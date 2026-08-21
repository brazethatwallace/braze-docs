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
- [Numéro de téléphone du compte WhatsApp Business](#whatsapp-business-account-phone-numbers)
- [Abonnement et gestion des abonnements](#opt-in-and-subscription-management)
- [Limites d'envoi et note de qualité](#messaging-limits-and-quality-rating)
- [Modèles et éditeur WhatsApp](#whatsapp-templates-and-composer)
- [Livrabilité et facturation](#deliverability-and-billing)
- [Intégrations, données et reporting](#integrations-data-and-reporting)
- [Médias et images](#media-and-images)

### Comptes WhatsApp Business {#whatsapp-business-accounts}

#### Comment créer un compte WhatsApp Business ? {#how-do-i-create-a-whatsapp-business-account}
Nous vous recommandons de créer votre compte WhatsApp Business (WABA) via le flux d'inscription intégré dans le tableau de bord de Braze.

#### J'ai déjà un compte Meta Business. Ai-je quand même besoin d'un compte WhatsApp Business ? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
Oui, vous devez quand même créer un compte WhatsApp Business. Nous vous recommandons d'[imbriquer votre WABA sous votre compte Meta Business principal]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

#### Comment accéder à mon compte WhatsApp Business ? {#how-do-i-access-my-whatsapp-business-account}
Après avoir terminé le flux d'inscription intégré, vous pouvez accéder à votre compte sur business.facebook.com en vous rendant dans la [section WhatsApp](https://business.facebook.com/wa/manage/home).

#### Puis-je connecter plusieurs WABA à Braze ? {#can-i-connect-multiple-wabas-to-braze}
Oui, vous pouvez ajouter jusqu'à 10 comptes WhatsApp Business par espace de travail, et chaque compte peut être imbriqué sous un Meta Business Manager différent.

![Schéma de l'écosystème Braze et WhatsApp, montrant comment les espaces de travail et les comptes WhatsApp Business se connectent : vous pouvez relier un groupe d'abonnement à un numéro de téléphone, plusieurs comptes WhatsApp Business à un espace de travail, et un espace de travail à plusieurs Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### Puis-je modifier la devise de mon compte WhatsApp Business ? {#can-i-change-my-whatsapp-business-account-currency}
Non. Meta contrôle la devise de votre compte WhatsApp Business, et Braze ne peut ni la modifier ni la convertir. Pour utiliser une devise différente, [créez un compte WhatsApp Business distinct]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) avec cette devise, ou contactez le support Meta pour demander s'ils peuvent mettre à jour la devise de votre compte existant.

#### Qu'est-ce que la vérification d'entreprise ? {#what-is-business-verification}
La vérification d'entreprise est un concept WhatsApp utilisé pour garantir que la marque est une entreprise légitime. Elle peut être effectuée dans le WhatsApp Manager. La vérification d'entreprise est également requise pour augmenter les volumes d'envoi. Sans vérification d'entreprise, vous ne pouvez envoyer des messages qu'à 250 utilisateurs finaux uniques maximum sur une période glissante de 24 heures.

#### Qu'est-ce qu'un compte professionnel officiel ? {#what-is-an-official-business-account}
L'OBA (Official Business Account) vous donne la coche verte à côté de votre nom d'affichage et est facultatif. Vous pouvez demander un compte professionnel officiel après avoir terminé la vérification d'entreprise. Notez que la vérification d'entreprise et le compte professionnel officiel sont des concepts WhatsApp distincts.

#### Pourquoi mon nom d'affichage WhatsApp Business pourrait-il être rejeté ? {#why-might-my-whatsapp-business-display-name-be-rejected}
Les rejets de noms d'affichage WhatsApp Business sont gérés par Meta. Si votre nom d'affichage est rejeté, consultez les [directives de WhatsApp concernant les noms d'affichage](https://faq.whatsapp.com/793641088597363).

Si votre nom d'affichage respecte les directives et est malgré tout rejeté, Braze ne peut pas voir les raisons spécifiques. Toutefois, la raison la plus courante de rejet est que la présence en ligne de l'entreprise est trop faible, ou que l'entreprise commercialise des [produits réglementés ou restreints](https://business.whatsapp.com/policy#further-guidance).

Pour plus de conseils sur les rejets de noms d'affichage, consultez les [ressources Meta]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources).

### Numéros de téléphone du compte WhatsApp Business {#whatsapp-business-account-phone-numbers}
#### Ai-je besoin d'un numéro de téléphone pour mon compte WhatsApp Business ? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
Oui, vous avez besoin d'un numéro auquel vous avez accès. Il vous sera demandé de vérifier votre numéro de téléphone avec une authentification à deux facteurs lors du flux d'inscription intégré. Le numéro de téléphone ne peut pas être utilisé pour d'autres comptes WhatsApp (professionnels ou personnels).

#### Quels types de numéros de téléphone sont pris en charge par WhatsApp ? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
Consultez les exigences de Meta concernant les [numéros de téléphone](https://developers.facebook.com/docs/whatsapp/phone-numbers) pour plus d'informations.

#### Puis-je utiliser un même numéro de téléphone sur plusieurs WABA ? {#can-i-use-one-phone-number-across-multiple-wabas}
Non. Un numéro de téléphone ne peut pas être partagé entre plusieurs WABA.

#### Ai-je besoin d'un type spécifique de numéro de téléphone pour envoyer des messages vers certains pays ? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
Non. WhatsApp vous permet d'envoyer des messages aux utilisateurs finaux depuis n'importe quel numéro de téléphone pris en charge, dans n'importe quel pays. Consultez les exigences de Meta concernant les [numéros de téléphone](https://developers.facebook.com/docs/whatsapp/phone-numbers) pour plus d'informations.

#### Comment les numéros de téléphone des utilisateurs doivent-ils être stockés dans Braze ? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
Les numéros de téléphone des utilisateurs doivent être stockés au [format E.164]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting).

#### Puis-je importer les numéros de téléphone des utilisateurs ? {#can-i-import-user-phone-numbers}
Oui. Vous pouvez [importer les numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers).

### Abonnement et gestion des abonnements {#opt-in-and-subscription-management}

#### Dois-je recueillir le consentement d'abonnement pour envoyer des messages marketing aux utilisateurs finaux sur WhatsApp ? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
Oui, WhatsApp exige que les entreprises [recueillent le consentement d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) pour envoyer des messages marketing aux utilisateurs finaux.

#### Puis-je contacter proactivement les utilisateurs finaux sur WhatsApp pour recueillir leur consentement d'abonnement ? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
Si vous choisissez de contacter proactivement les utilisateurs finaux, votre premier message initié par l'entreprise devrait demander à l'utilisateur s'il souhaite recevoir des messages marketing de votre entreprise et doit être conforme aux exigences de Meta en matière de [recueil du consentement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Gardez à l'esprit que WhatsApp surveillera la réputation de votre entreprise sur le canal ; la bonne pratique recommandée est donc d'être explicite avec les utilisateurs finaux et de n'envoyer que les messages qu'ils ont indiqué vouloir recevoir.

#### Dois-je collecter le numéro de téléphone de l'utilisateur final lorsque je recueille le consentement d'abonnement ? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
Vous devez disposer du numéro de téléphone de l'utilisateur final sur le profil Braze pour lui envoyer des messages.
- Si vous avez déjà son numéro, vous n'avez pas besoin de le collecter lors de l'abonnement.
- Si vous n'avez pas le numéro de l'utilisateur final, votre méthode d'abonnement doit inclure la collecte du numéro de téléphone.

#### Comment mettre à jour le statut d'abonnement des utilisateurs finaux qui s'abonnent ? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
La gestion des abonnements du canal WhatsApp fonctionne de manière similaire aux autres canaux Braze. Consultez la section [Gestion des abonnements utilisateurs]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) pour plus d'informations.

#### Si j'ai déjà une liste d'utilisateurs ayant consenti à recevoir des messages marketing sur WhatsApp, comment mettre à jour leur statut d'abonnement dans Braze ? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
Vous pouvez mettre à jour leur statut d'abonnement via l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional).

#### Quelles méthodes dois-je utiliser pour recueillir les consentements d'abonnement ? {#what-methods-should-i-use-to-collect-opt-ins}
Braze recommande de consulter les [directives de Meta sur les méthodes d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) pour rester en conformité. Consultez la section [Abonnement et désabonnement]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) pour les méthodes de configuration dans Canvas et les Campaigns.

#### Le double abonnement est-il requis pour WhatsApp ? {#is-double-opt-in-required-for-whatsapp}
Non, le double abonnement n'est pas requis.

#### Comment mes utilisateurs se désabonnent-ils des messages WhatsApp ? {#how-do-my-users-opt-out-of-whatsapp-messages}
Vos utilisateurs peuvent se désabonner de deux manières :
1. Configurer un message WhatsApp entrant avec un mot-clé de désabonnement spécifique et utiliser un webhook pour mettre à jour le statut d'abonnement de l'utilisateur.
2. Ajouter une réponse rapide de désabonnement dans le modèle WhatsApp, avec un webhook correspondant pour effectuer la mise à jour.

#### Puis-je utiliser un groupe d'abonnement WhatsApp de Braze si j'envoie des messages WhatsApp via un tiers ? {#can-i-use-a-braze-whatsapp-subscription-group-if-i-send-whatsapp-messages-through-a-third-party}
Non. Les groupes d'abonnement WhatsApp de Braze s'appliquent aux messages envoyés via le canal WhatsApp de Braze. Si vous envoyez des messages WhatsApp via un fournisseur tiers ou des intégrations personnalisées en dehors des Campaigns et Canvas WhatsApp de Braze, vous pouvez stocker le consentement d'abonnement dans un attribut personnalisé (ou votre propre modèle d'abonnement) et utiliser cet attribut pour la segmentation et l'éligibilité. Pour les cas où Braze possède le numéro WhatsApp, consultez [Comment connecter le support et le marketing WhatsApp dans Braze ?](#how-do-i-connect-whatsapp-support-and-marketing-in-braze).

### Limites d'envoi et note de qualité {#messaging-limits-and-quality-rating}

#### Que sont les limites d'envoi ? {#what-are-messaging-limits}
Les limites d'envoi sont un concept de renforcement de l'intégrité WhatsApp. Elles déterminent le nombre maximum de conversations initiées par l'entreprise que chaque numéro de téléphone peut démarrer sur une période glissante de 24 heures. Il existe quatre niveaux de limites d'envoi : 1k, 10k, 100k et illimité.

#### Comment augmenter ma limite d'envoi ? {#how-do-i-increase-my-messaging-limit}
WhatsApp augmentera votre limite d'envoi si vous remplissez les conditions suivantes :
1. Le [statut du numéro de téléphone](https://www.facebook.com/business/help/896873687365001) est **Connecté**
2. La [note de qualité du numéro de téléphone](https://www.facebook.com/business/help/896873687365001) est **Moyenne** ou **Élevée**
3. Au cours des sept derniers jours, vous avez initié X conversations ou plus avec des utilisateurs uniques, où X correspond à votre limite d'envoi actuelle divisée par 2

Ainsi, pour passer de 100k à illimité, vous devez envoyer au moins 50 000 conversations initiées par l'entreprise sur une période de 7 jours.

#### Combien de temps faut-il pour augmenter mes limites d'envoi ? {#how-long-does-it-take-to-increase-my-messaging-limits}
Si toutes les conditions précédentes sont remplies, vous pouvez augmenter votre limite d'envoi de 1k à illimité en 4 jours.

#### Où puis-je consulter ma limite d'envoi actuelle ? {#where-can-i-see-my-current-messaging-limit}
Vous pouvez vérifier vos limites d'envoi actuelles dans l'onglet **WhatsApp Manager > Overview Dashboard > Insights**.

#### Que se passe-t-il si je tente d'envoyer des messages alors que j'ai déjà atteint ma limite d'envoi ? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
Si vous essayez d'envoyer une Campaign ou un Canvas à plus d'utilisateurs uniques que votre limite actuelle ne le permet, les messages ne seront pas envoyés. Braze continuera de tenter de renvoyer les messages si/quand votre limite d'envoi augmentera, pendant un jour maximum.

#### Ma limite d'envoi peut-elle diminuer ? {#can-my-messaging-limit-decrease}
Oui, si la note de qualité de votre numéro de téléphone baisse trop, vous risquez que WhatsApp diminue votre limite d'envoi. Braze vous recommande de vous abonner aux notifications liées à la qualité de WhatsApp, y compris les mises à jour concernant le statut de votre numéro de téléphone et le niveau de limite d'envoi. Vous pouvez vous abonner aux notifications directement dans le tableau de bord du WhatsApp Manager.

#### Quels facteurs affectent la note de qualité du numéro de téléphone, et que se passe-t-il lorsque ma note de qualité baisse trop ? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
Les facteurs qui affectent la note de qualité du numéro de téléphone incluent le blocage de l'entreprise par un utilisateur final (et les raisons qu'il fournit lors du blocage) et le signalement de l'entreprise par un utilisateur final.

Lorsqu'une note de qualité est basse, le statut du numéro de téléphone passe de **Connecté** à **Signalé**. Si la qualité ne s'améliore pas en sept jours, le statut revient à **Connecté**. Toutefois, la limite d'envoi diminuera au niveau inférieur. Par exemple, un numéro de téléphone qui avait une limite d'envoi de 100 000 aura désormais une limite d'envoi de 10 000.

#### Quelle est la limite de débit Meta ? {#what-is-the-meta-throughput-limit}
Meta dispose de sa propre limite de débit, distincte de la limite d'envoi du WABA. La limite par défaut prise en charge par l'API Cloud est de 80 messages par seconde. Si vous pensez que vos Campaigns dépasseront cette limite, vous pouvez [demander](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) une augmentation de votre limite. Meta recommande de soumettre cette demande au moins trois jours avant les envois de Campaigns.

### Modèles et éditeur WhatsApp {#whatsapp-templates-and-composer}

#### Qu'est-ce qu'un modèle WhatsApp ? {#what-is-a-whatsapp-template}
WhatsApp exige que tous les messages initiés par l'entreprise commencent par un modèle approuvé. Le modèle comprend le texte du message, ainsi que des médias enrichis optionnels comme des images, des appels à l'action et des boutons de réponse rapide. Une fois les modèles approuvés par WhatsApp, ils peuvent être utilisés pour composer un message WhatsApp dans Braze.

#### Où puis-je créer, modifier et gérer mes modèles WhatsApp ? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Vous pouvez créer et soumettre des modèles dans Braze à l'aide du [générateur de modèles WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), ou dans le WhatsApp Manager de Meta. Les modèles créés dans l'un ou l'autre emplacement apparaissent dans le tableau de bord de Braze avec un indicateur de statut. Après soumission, les champs verrouillés nécessitent une nouvelle approbation de Meta ; consultez les [limitations de modification dans la FAQ du générateur de modèles]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder#can-i-edit-a-template-after-its-been-approved) pour plus de détails.

#### Combien de temps WhatsApp met-il pour examiner la soumission d'un modèle ? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
Le processus d'approbation peut prendre jusqu'à 24 heures, mais souvent les modèles sont traités en quelques heures ou minutes.

#### Combien de modèles puis-je avoir à un moment donné ? {#how-many-templates-can-i-have-at-a-given-time}
Votre limite de modèles de messages dépend de votre statut de vérification d'entreprise. Vous pouvez vérifier votre limite sur la page **WhatsApp Manager > Message Templates**.

#### Comment personnaliser le texte et les médias enrichis d'un modèle dans Braze ? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsApp permet d'insérer des paramètres variables dans les modèles de messages. Les messages ne peuvent pas commencer ou finir par un paramètre variable. Les paramètres variables peuvent être remplis avec la logique Liquid dans la plateforme Braze. Consultez la section [Composition d'un message WhatsApp dans Braze]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) pour en savoir plus sur les paramètres variables.

#### Mon modèle a été rejeté. Braze peut-il m'aider à le faire approuver ? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
L'équipe Braze n'a pas de visibilité sur les rejets de modèles. Vous devez travailler directement avec votre WhatsApp Business Manager pour modifier et resoumettre le modèle. Assurez-vous de fournir un exemple de modèle si nécessaire. Vérifiez que votre modèle respecte les politiques [commerciales](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) ou de [commerce](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) de Meta.

#### Les médias enrichis peuvent-ils être ciblés ou personnalisés dans Braze ? {#can-rich-media-be-targeted-or-personalized-in-braze}
Oui. Vous pouvez télécharger des images statiques depuis la bibliothèque multimédia, ou ajouter des images par URL et les personnaliser avec [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Les URL d'images prennent en charge la logique Liquid complète n'importe où dans l'URL. Cela s'applique aux messages de modèle et aux messages de réponse (messages multimédias et mises en page à réponse rapide). Pour plus de détails, consultez la section [Images dynamiques]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#dynamic-images).

#### Quels types de médias enrichis sont pris en charge dans les modèles WhatsApp ? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
Vous pouvez ajouter des images, des appels à l'action (URL ou numéro de téléphone) et des boutons de réponse rapide aux modèles WhatsApp. Vous pouvez ajouter ces éléments lorsque vous créez des modèles directement dans WhatsApp.

#### Que faire si mon modèle a été signalé à tort comme violant la politique commerciale de WhatsApp ? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Si vous pensez que Meta a signalé votre modèle à tort, utilisez le lien de révision dans l'e-mail de WhatsApp pour demander un réexamen. L'équipe WhatsApp Business examine la décision et l'annule si nécessaire.

#### Pourquoi mon modèle WhatsApp importé affiche-t-il « Message Incomplete » dans l'éditeur ? {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
L'avertissement « Message Incomplete » apparaît lorsque les emplacements de variables requis du modèle ne sont pas remplis avec des valeurs valides dans l'éditeur.

Lorsque vous créez des modèles à l'aide du [générateur de modèles WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), Braze renumérote les variables en marques substitutives séquentielles ({% raw %}`{{1}}`, `{{2}}`, `{{3}}`{% endraw %}, etc.). Les modèles créés en externe dans le WhatsApp Manager de Meta peuvent contenir des schémas rendant le mappage des variables sujet aux erreurs, comme :

- Une numérotation non séquentielle (par exemple, {% raw %}`{{1}}`, `{{3}}`, `{{5}}`{% endraw %})
- Des variables manquantes dans la séquence (par exemple, le saut de {% raw %}`{{2}}`{% endraw %})
- Des variables qui commencent par un numéro autre que 1

Pour résoudre ce problème, modifiez votre modèle dans le WhatsApp Manager de Meta pour utiliser un formatage séquentiel des marques substitutives, puis réimportez-le dans Braze. Dans Braze, confirmez que chaque champ de variable requis est rempli avec une valeur Liquid valide.

#### Pourquoi ma Campaign WhatsApp ne s'envoie-t-elle pas alors que le modèle s'affiche correctement en aperçu ? {#why-is-my-whatsapp-campaign-not-sending-despite-template-previewing}
Si votre modèle s'affiche correctement en aperçu mais que le journal de traitement indique **Abort** avec le détail « Param text cannot have new-line/tab characters or more than 4 consecutive spaces », vérifiez les valeurs des paramètres générées par Liquid dans votre message. WhatsApp exige que les valeurs textuelles des paramètres ne contiennent pas :

- De caractères de retour à la ligne
- De caractères de tabulation
- Plus de 4 espaces consécutifs

Confirmez que toute logique Liquid remplissant les paramètres du modèle supprime ces caractères ou formate le texte en conséquence avant l'envoi.

### Livrabilité et facturation {#deliverability-and-billing}

#### Pourquoi un message ne serait-il pas distribué ? {#why-would-a-message-not-be-delivered}
Il existe plusieurs raisons pour lesquelles un message peut ne pas être distribué, notamment des problèmes réseau ou l'appareil éteint.

#### Si un message n'est pas distribué, suis-je facturé ? {#if-a-message-is-not-delivered-will-i-be-billed}
Non. Si un message n'est pas distribué, vous n'êtes pas facturé.

#### Que se passe-t-il si un utilisateur bloque mon entreprise ? {#what-happens-if-a-user-blocks-my-business}
Si un utilisateur bloque votre entreprise, les messages que vous tentez ensuite d'envoyer ne sont pas distribués et vous n'êtes pas facturé. Le statut d'abonnement de l'utilisateur ne sera pas mis à jour.

#### Que se passe-t-il si un utilisateur signale un message ? {#what-happens-if-a-user-reports-a-message}
Si un utilisateur signale un message, vous pouvez toujours lui envoyer des messages ultérieurs. Toutefois, le signalement peut affecter votre note de qualité sur le canal. Le statut d'abonnement de l'utilisateur ne sera pas mis à jour.

#### Comment exclure les utilisateurs qui signalent mon compte WhatsApp des prochains envois ? {#how-can-i-exclude-users-who-report-my-whatsapp-account-from-upcoming-launches}
Braze ne reçoit pas de notifications de WhatsApp lorsque votre compte est signalé, vous ne pouvez donc pas identifier ou exclure automatiquement ces utilisateurs dans Braze. Les utilisateurs qui signalent votre compte peuvent rester dans votre groupe d'abonnement WhatsApp et continuer à être éligibles aux futurs messages.

Vous pouvez toutefois configurer une Campaign qui se déclenche lorsqu'un utilisateur répond avec un mot-clé de désabonnement, ce qui le désabonne automatiquement via l'[endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Pour plus d'informations, consultez la section [Processus d'abonnement et de désabonnement WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process).

#### Braze prend-il en charge un basculement automatique vers le SMS en cas d'échec de distribution WhatsApp ? {#does-braze-support-automatic-sms-fallback-when-whatsapp-delivery-fails}

Non. Braze ne propose pas de chemin de basculement natif WhatsApp vers SMS. Pour réessayer sur un autre canal, segmentez les utilisateurs dont les envois WhatsApp ont échoué (par exemple, via les événements d'échec Currents) et ciblez une Campaign SMS ou e-mail.

#### Les messages de réponse WhatsApp sont-ils gratuits ? {#are-whatsapp-response-messages-free}

Les messages de réponse composés dans l'éditeur de Campaign ou Canvas de Braze (et non les modèles WhatsApp approuvés) sont traités comme des messages de service par Meta. Jusqu'au 30 septembre 2026, les messages de service envoyés via l'intégration native WhatsApp de Braze ne consomment pas de crédits d'action lorsqu'ils sont envoyés en tant que [messages de réponse]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) dans une fenêtre de service client ouverte.

À partir du 1er octobre 2026, les messages de service consommeront des crédits d'action par message distribué. Cette classification dépend du message lui-même : une réponse non modélisée est un message de service, même lorsque la conversation a débuté par un modèle. Si vous répondez avec un modèle marketing, utilitaire ou d'authentification approuvé, le message est facturé selon la catégorie de son modèle.

| Type de message | Crédits d'action | Remarques |
|---|---|---|
| Message de réponse (réponse entrante) | Non consommés jusqu'au 30 septembre 2026 ; consommés à partir du 1er octobre 2026 | Composé dans Braze ; pas un modèle approuvé par Meta. Meta le classe comme message de service. |
| Message de modèle | Consommés | Les modèles marketing, utilitaires, d'authentification et d'offre à durée limitée sont facturés par envoi. |
| Modèle utilitaire dans la fenêtre de service | Non facturé par Meta jusqu'au 30 septembre 2026 ; facturé à partir du 1er octobre 2026 | La consommation de crédits d'action dépend de votre contrat. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Crédits d'action des messages de réponse" }

Pour les flux Canvas où les utilisateurs appuient sur des réponses rapides après la fenêtre initiale de 24 heures, consultez la section [Réponses rapides et messages entrants en dehors de la fenêtre de 24 heures]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Que se passe-t-il si un utilisateur répond ou appuie sur une réponse rapide après la fermeture de la fenêtre de 24 heures ? {#what-happens-if-a-user-replies-or-taps-a-quick-reply-after-the-24-hour-window-closes}
Une nouvelle fenêtre de service client de 24 heures s'ouvre. Consultez la section [Réponses rapides et messages entrants en dehors de la fenêtre de 24 heures]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Dois-je configurer mon parcours d'action Canvas sur 31 jours pour les réponses rapides WhatsApp ? {#do-i-need-to-set-my-canvas-action-path-to-31-days-for-whatsapp-quick-replies}
Non. La durée par défaut du parcours d'action est suffisante. Consultez la section [Réponses rapides et messages entrants en dehors de la fenêtre de 24 heures]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Puis-je voir combien de crédits WhatsApp une Campaign ou un Canvas spécifique a consommés ? {#can-i-see-how-many-whatsapp-credits-a-specific-campaign-or-canvas-consumed}
Pas dans le tableau de bord de Braze aujourd'hui. Les analyses de Campaign et Canvas affichent les envois, les distributions et les échecs, mais pas la consommation de crédits par message. Les nombres d'envois ne correspondent pas exactement à l'utilisation des crédits, car la catégorie de modèle et le type de message affectent la facturation différemment. Pour les détails de facturation, consultez la section [Les messages de réponse WhatsApp sont-ils gratuits ?](#are-whatsapp-response-messages-free).

### Intégrations, données et reporting {#integrations-data-and-reporting}

#### Pourquoi WhatsApp n'apparaît-il pas dans la liste des partenaires technologiques ? {#why-isnt-whatsapp-listed-under-technology-partners}
WhatsApp apparaît sur la page **Partenaires technologiques** lorsque WhatsApp est activé pour votre entreprise. Si vous ne voyez pas WhatsApp sur cette page, contactez votre équipe de compte Braze pour confirmer que WhatsApp est provisionné pour votre tableau de bord.

#### Braze prend-il en charge les cas d'usage de support client comme les chatbots et le chat assisté par un humain pour WhatsApp ? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Nous ne prenons pas en charge les chatbots ni le chat assisté par un humain au sein de Braze ou via des intégrations directes.

Si vous utilisez déjà WhatsApp comme canal de support client, nous vous recommandons de conserver votre configuration actuelle et de créer un nouveau WABA via Braze pour les messages marketing. Ce WABA nécessitera un nouveau numéro de téléphone.

#### Comment connecter le support et le marketing WhatsApp dans Braze ? {#how-do-i-connect-whatsapp-support-and-marketing-in-braze}

Vous pouvez utiliser les propriétés Liquid WhatsApp pour transférer le contenu des messages WhatsApp entrants (y compris le corps du message et les URL des médias) de Braze vers d'autres plateformes, y compris tout outil de support client. Pour plus de détails, consultez nos [Tags de personnalisation pris en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Pour envoyer des informations dans Braze, par exemple pour indiquer qu'un utilisateur est dans une conversation de support active, vous pouvez enregistrer un attribut personnalisé (comme un booléen « has existing support chat = true/false ») et l'utiliser comme critère de segmentation dans vos Campaigns marketing. Vous pouvez également utiliser des deep links entre deux fils de discussion pour diriger les utilisateurs du fil marketing vers le fil de support et inversement.

#### Braze stocke-t-il les réponses des utilisateurs ? {#does-braze-store-user-responses}
Les messages ne sont stockés que le temps nécessaire à leur traitement. Pour accéder aux messages des utilisateurs, utilisez Currents.

#### Quels indicateurs sont disponibles dans le tableau de bord de Braze ? {#what-metrics-are-available-in-the-braze-dashboard}
Vous pouvez consulter les destinataires uniques, les envois, les distributions, les lectures et les échecs dans le tableau de bord de Braze. Notez que les accusés de lecture de l'utilisateur doivent être activés pour que Braze puisse suivre les lectures. Vous pouvez également configurer des événements de conversion pour surveiller la performance des Campaigns, comme pour les autres canaux.

#### Qu'est-ce qu'une conversation WhatsApp ? {#what-is-a-whatsapp-conversation}
WhatsApp est un canal centré sur la communication bidirectionnelle et s'appuie donc sur les conversations (plutôt que sur le nombre de messages individuels). Une conversation est un fil de 24 heures entre une entreprise et un utilisateur final.

- **Conversation initiée par l'entreprise** : une conversation dans laquelle l'entreprise commence par envoyer un message de modèle approuvé à l'utilisateur final. Dès que l'entreprise envoie un message, la fenêtre de 24 heures démarre.
- **Conversation initiée par l'utilisateur** : une conversation dans laquelle l'utilisateur final envoie un message à l'entreprise. Lorsque l'entreprise envoie un message en réponse, la fenêtre de 24 heures démarre.

### Médias et images {#media-and-images}

#### Pourquoi les images ne se chargent-elles pas lorsqu'elles sont envoyées dans un message WhatsApp ? {#why-wont-images-load-when-sent-as-a-whatsapp-message}
Si les utilisateurs signalent que les images dans les messages WhatsApp ne se téléchargent pas ou que l'icône de téléchargement ne réagit pas, cela est probablement dû à un problème connu dans les anciennes versions de l'application WhatsApp. Ce problème peut généralement être résolu en mettant à jour l'appareil vers la version la plus récente de WhatsApp.