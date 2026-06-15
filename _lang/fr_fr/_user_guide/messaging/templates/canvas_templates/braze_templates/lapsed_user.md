---
nav_title: Utilisateur inactif
article_title: Utilisateur inactif
page_order: 4
page_type: reference
description: "Cet article décrit comment utiliser un modèle Canvas de Braze pour ramener les utilisateurs vers votre application avec des incitations basées sur leurs engagements passés."
tool: Canvas
---

# Utilisateur inactif {#lapsed-user}

> Utilisez le modèle d'utilisateur inactif pour rappeler aux utilisateurs la valeur que votre marque leur apporte, et encouragez leur retour avec des offres attrayantes et des incitations basées sur leurs engagements passés.

Cet article vous guidera à travers un cas d'utilisation du modèle **Lapsed User**, conçu pour l'étape de rétention et de fidélisation du cycle de vie utilisateur. À la fin, vous aurez créé un Canvas qui encourage les utilisateurs à revenir sur votre application avec des promotions qui varient en fonction de leur comportement, par exemple s'ils ont démarré une session dans votre application après avoir reçu un message promotionnel.

## Conditions préalables {#prerequisites}

Pour utiliser avec succès le modèle d'utilisateur inactif, vous devez configurer [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) avec les partenaires et les audiences que vous utilisez.

## Adapter le modèle à vos besoins {#tailoring-the-template-to-your-needs}

Imaginons que nous travaillons pour MovieCanon, un service de streaming proposant du contenu exclusif pour les films et les séries. Nous pouvons utiliser le modèle d'utilisateur inactif pour promouvoir des avantages et du contenu premium auprès des utilisateurs qui n'ont pas visité notre application depuis 30 jours.

Avant de créer le Canvas, nous avons configuré l'intégration [Braze Audience Sync vers Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) afin de pouvoir ajouter des données utilisateur de Braze aux audiences Google pour envoyer des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore.

Pour accéder au modèle d'utilisateur inactif, lors de la création d'un nouveau Canvas, sélectionnez **Use a Canvas template** > **Braze templates**. Ensuite, à côté de **Lapsing User**, sélectionnez **Apply Template**. Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Configurer les détails {#step-1-set-up-the-details}

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Edit** à côté du nom du modèle.

![Le titre et la description actuels du Canvas.]({% image_buster /assets/img/canvas_templates/lapsed_user_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Mettez à jour le nom du Canvas pour préciser que ce Canvas enverra des promotions aux utilisateurs et effectuera une synchronisation d'audience pour ceux qui démarrent une session.
3. Mettez à jour la description pour expliquer que ce Canvas contient des avantages et des promotions.
4. Ajoutez l'étiquette **Lapsing/Retention** afin de pouvoir filtrer ce Canvas sur la page d'accueil Canvas.

![Étape « Set Up Canvas Details » avec le nom du Canvas « Lapsed User - Visit App » et une brève description du Canvas.]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### Étape 2 : Assigner vos événements de conversion {#step-2-assign-your-conversion-events}

Mettez à jour **Primary Conversion Event - A** pour cibler les utilisateurs de notre application (MovieCanon), et laissez **Primary Conversion Event - B** sur la valeur par défaut, à savoir effectuer un achat quelconque.

![Section « Assign Conversion Events » avec un événement de conversion principal correspondant à un utilisateur démarrant une session dans une application spécifique.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### Étape 3 : Adapter la planification d'entrée {#step-3-tailor-the-entry-schedule}

Conservons la planification d'entrée sur **Scheduled** et les options temporelles par défaut, afin que le Canvas vérifie quotidiennement les utilisateurs inactifs.

Nous apporterons deux ajustements à cette étape :

1. Sélectionnez une date et une heure de début.
2. Sélectionnez les paramètres de fin sur **On a specific date** et choisissez une date dans deux mois. Supposons que nous ayons un autre Canvas d'utilisateur inactif que nous souhaitons démarrer après celui-ci.

![Étape « Entry Schedule » pour un Canvas planifié qui fait entrer les utilisateurs à un moment désigné.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### Étape 4 : Sélectionner notre audience cible {#step-4-select-our-target-audience}

Nous conserverons les paramètres par défaut pour l'audience d'entrée, qui est définie sur les utilisateurs n'ayant pas utilisé notre application depuis plus de 30 jours. Nous conserverons également les contrôles d'entrée par défaut afin que les utilisateurs puissent réintégrer le Canvas après quatre semaines. Cela signifie que chaque fois qu'un utilisateur ne visite pas notre application pendant plus de 30 jours consécutifs, il sera inscrit dans le Canvas.

![Étape « Target Audience » ciblant les utilisateurs ayant utilisé les applications pour la dernière fois il y a 30 jours.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### Étape 5 : Sélectionner vos paramètres d'envoi {#step-5-select-your-send-settings}

Nous conserverons la plupart des paramètres d'abonnement par défaut :

- Envoyer uniquement aux utilisateurs qui se sont abonnés ou ont opté pour la réception de messages ou de notifications.
- Appliquer nos [règles de limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping) afin de ne pas submerger notre audience avec le nombre de messages qu'elle reçoit. Dans ce cas, nous avons défini notre limite de fréquence pour limiter le nombre de campagnes ou d'étapes Canvas étiquetées « Lapsing/Retention » qu'un utilisateur peut recevoir à deux par semaine.
- Ne pas envoyer de messages pendant les heures calmes dans le fuseau horaire local de l'utilisateur (de minuit à 8 h).

Le seul paramètre que nous modifierons concerne le comportement lorsqu'un message se déclenche pendant les heures calmes. Au lieu d'annuler le message, sélectionnez **Send at next available time** afin que nos utilisateurs ne manquent aucune promotion.

![Section « Quiet Hours » avec une heure de début à minuit et une heure de fin à 8 h.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### Étape 6 : Personnaliser votre Canvas {#step-6-customize-your-canvas}

Maintenant, nous allons construire notre Canvas en personnalisant les étapes du modèle :

1. Personnalisez le premier e-mail qui sera envoyé à tous les utilisateurs n'ayant pas visité notre application depuis plus de 30 jours. Pour notre cas d'utilisation, nous personnaliserons un e-mail indiquant aux utilisateurs qu'ils débloqueront de nouveaux avantages en visitant notre application aujourd'hui.

![Étape de message Canvas pour un e-mail indiquant aux utilisateurs de débloquer de nouveaux avantages en visitant aujourd'hui.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2. Personnalisez le composant de parcours d'action appelé « Start Session? » en sélectionnant notre application pour le chemin **Started Session**.

![Parcours d'action pour les sessions démarrées dans une application spécifique.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3. Conservez la valeur par défaut pour l'étape de l'arbre décisionnel appelée « Sessions? », qui définit le groupe « >1 Session » comme les utilisateurs ayant utilisé notre application plus d'une fois au cours du dernier jour calendaire.
4. Personnalisez l'étape de message pour les utilisateurs qui appartiennent au groupe « >1 Session ». Dans notre cas d'utilisation, nous remercierons les utilisateurs d'avoir visité notre application et mettrons en avant les avantages qu'ils ont débloqués.
5. Assurez-vous que notre synchronisation Google Audience est configurée dans l'étape Ad Audience Update, afin de mettre à jour et synchroniser les données des utilisateurs ayant eu plusieurs sessions après avoir reçu notre premier e-mail.
6. Conservez la valeur par défaut pour le composant [chemin d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/#experiment-paths) appelé « A/B Test ». Celui-ci enverra aléatoirement l'une des deux promotions (que nous personnaliserons à l'étape suivante) aux utilisateurs ayant eu moins de deux sessions.
7. Personnalisez les deux promotions qui seront envoyées aux utilisateurs dans le cadre du chemin d'expérience. Dans notre cas d'utilisation, nous créerons une promotion de 20 % pour un abonnement de trois mois et une autre de 10 % pour un abonnement d'un mois.

![Étapes Canvas avec des chemins de ramification basés sur le nombre de sessions d'un utilisateur.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### Étape 7 : Tester et lancer le Canvas {#step-7-test-and-launch-the-canvas}

Après avoir testé et vérifié notre Canvas pour nous assurer qu'il fonctionne comme prévu, nous le lancerons en sélectionnant **Launch Canvas**. Désormais, nos utilisateurs qui n'ont pas visité notre application depuis plus de 30 jours et qui se sont abonnés à nos canaux de communication recevront des e-mails les encourageant à revenir !

{% alert tip %}
Consultez notre [liste de vérification pré et post-lancement]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) pour les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}