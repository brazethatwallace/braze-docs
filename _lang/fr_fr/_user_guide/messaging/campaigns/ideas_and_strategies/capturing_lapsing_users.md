---
nav_title: Récupérer les utilisateurs inactifs
article_title: Récupérer les utilisateurs inactifs
page_order: 1
page_type: tutorial
description: "Cet article pratique aborde la problématique des utilisateurs inactifs et explique comment utiliser efficacement les campagnes Braze pour les réengager."
tool:
  - Segments
  - Campaigns

---

# Récupérer les utilisateurs inactifs {#capture-lapsing-users}

> Si votre audience diminue, il est essentiel de chercher à la reconquérir. Avec Braze, vous pouvez mettre en place des campagnes de réengagement automatisées et récurrentes pour récupérer les utilisateurs inactifs. Vous êtes libre de choisir la période de réengagement et la fréquence de récurrence les plus adaptées à votre application. Pour illustrer notre propos, nous allons mettre en place un plan de réengagement sur 14 jours.

Pour en savoir plus sur le ciblage des utilisateurs, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes !

## Étape 1 : Créer un segment d'utilisateurs {#step-1-segment-users}

Commençons par créer un segment ciblant les utilisateurs qui n'ont pas utilisé votre application au cours des deux dernières semaines, à l'aide des filtres suivants :

- **Dernière utilisation de l'application** il y a plus de 2 semaines
- **Dernière utilisation de l'application** il y a moins de 3 semaines

![Capture d'écran relative à l'étape 1 : créer un segment d'utilisateurs.]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Donnez au segment un nom facile à retenir, par exemple « Utilisateurs inactifs – 2 semaines ». Comme nous allons configurer la campagne pour qu'elle se répète chaque semaine, nous voulons nous assurer qu'au moins une semaine d'utilisateurs est capturée dans le segment. C'est pourquoi nous avons sélectionné les utilisateurs ayant utilisé l'application pour la dernière fois entre deux et trois semaines auparavant.

## Étape 2 : Créer une campagne {#step-2-create-a-campaign}

Cliquez ensuite sur **Créer une campagne** et choisissez le type de campagne à envoyer à ce segment. Dans cet exemple, nous allons créer une nouvelle [campagne push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).

![Cliquez ensuite sur Créer une campagne et choisissez le type de campagne à envoyer à ce segment. Dans cet exemple, nous allons créer une nouvelle campagne push.]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Nous nommerons la campagne « Message aux utilisateurs inactifs – 2 semaines », puis nous rédigerons le contenu de notre message. Dans cet exemple, nous ciblons uniquement les utilisateurs iOS, mais vous pouvez utiliser Braze pour les notifications push Android et iOS.

Plus la dernière visite de l'utilisateur dans l'application est récente, plus il est important d'être pertinent et en phase avec l'actualité. Lorsque vous contactez un utilisateur après deux semaines d'inactivité, veillez à mettre en avant du contenu pertinent et à rappeler les avantages de l'application.

![Capture d'écran relative à l'étape 2 : créer une campagne.]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Nous allons ensuite créer une planification récurrente pour envoyer notre message hebdomadaire le jeudi à 17 h 45 en utilisant la [distribution selon le fuseau horaire local]({{site.baseurl}}/help/faqs#what-does-local-time-zone-delivery-offer) dans les **Options de planification basées sur le temps**. Nous vous recommandons de consulter votre graphique de sessions pour cibler les utilisateurs juste avant les périodes de forte utilisation. Cela vous permet de tenter de réengager les utilisateurs au moment où ils sont le plus susceptibles d'utiliser l'application. Vous pourrez modifier ce paramètre ultérieurement et tester votre hypothèse initiale.

![Créer une planification récurrente pour envoyer le message hebdomadaire le jeudi à 17 h 45 en utilisant la distribution selon le fuseau horaire local dans les Options de planification basées sur le temps. Consultez votre graphique de sessions pour cibler les utilisateurs juste avant les périodes de forte utilisation.]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Étape 3 : Lancer la campagne {#step-3-launch-the-campaign}

Vous êtes maintenant prêt à envoyer la campagne. Vérifiez les paramètres sur la dernière page du composeur et cliquez sur **Lancer la campagne** !