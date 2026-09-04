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

## Étape 1 : Segmenter les utilisateurs {#step-1-segment-users}

Tout d'abord, nous allons créer un Segment pour cibler les utilisateurs qui n'ont pas utilisé votre application au cours des deux dernières semaines, en utilisant les filtres suivants :

- **Last Used App** il y a plus de 2 semaines
- **Last Used App** il y a moins de 3 semaines

![Capture d'écran relative à l'étape 1 : segmenter les utilisateurs.]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Donnez au Segment un nom facile à retenir, comme « Lapsed Users – 2 Weeks ». Comme nous configurons la Campaign pour qu'elle se répète chaque semaine, nous voulons nous assurer qu'il y a au moins une semaine d'utilisateurs capturés dans le Segment. C'est pourquoi nous avons sélectionné les utilisateurs qui ont utilisé l'application pour la dernière fois entre deux et trois semaines auparavant.

## Étape 2 : Créer une campagne {#step-2-create-a-campaign}

Ensuite, cliquez sur **Create Campaign** et choisissez le type de Campaign que nous enverrons à ce Segment. Dans cet exemple, nous allons créer une nouvelle [campagne de notifications push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).

![Cliquez ensuite sur Create Campaign et choisissez le type de Campaign à envoyer à ce Segment. Dans cet exemple, nous allons créer une nouvelle campagne de notifications push.]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Nous nommerons la Campaign « Message to Lapsed Users - 2 Weeks », puis nous créerons le contenu de notre message. Dans cet exemple, nous ne ciblerons que les utilisateurs iOS, mais vous pouvez utiliser Braze pour les notifications push Android et iOS.

Plus la dernière visite de l'utilisateur dans l'application est récente, plus il est important d'être pertinent et en phase avec l'actualité. Lorsque vous contactez un utilisateur après deux semaines sans utilisation de l'application, il est essentiel de mettre en avant du contenu pertinent et de souligner les avantages de l'application.

![Capture d'écran liée à l'étape 2 : créer une campagne.]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Ensuite, nous allons créer une planification récurrente pour envoyer notre message hebdomadaire le jeudi à 17 h 45 en utilisant la [distribution selon le fuseau horaire local]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) dans les **Time-Based Scheduling Options**. Nous vous recommandons de consulter votre graphique de sessions pour cibler les utilisateurs juste avant les périodes de forte utilisation. Cela vous permet de tenter de réengager les utilisateurs au moment où ils sont les plus susceptibles d'utiliser l'application. Vous pourrez modifier cela ultérieurement et tester votre hypothèse initiale.

![Nous allons créer une planification récurrente pour envoyer notre message hebdomadaire le jeudi à 17 h 45 en utilisant la distribution selon le fuseau horaire local dans les Time-Based Scheduling Options. Nous vous recommandons de consulter votre graphique de sessions pour cibler les utilisateurs juste avant les périodes de forte utilisation. Cela vous permet de tenter de réengager les utilisateurs au moment où ils sont les plus susceptibles d'utiliser l'application. Vous pourrez modifier cela ultérieurement et tester votre hypothèse initiale.]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Étape 3 : Lancer la campagne {#step-3-launch-the-campaign}

Vous êtes maintenant prêt à envoyer la campagne. Confirmez les paramètres sur la dernière page du composeur et cliquez sur **Launch Campaign** !