---
nav_title: IP warming automatisé
article_title: IP warming automatisé
page_order: 1
page_type: reference
description: "Cet article de référence traite de l'IP warming automatisé et explique comment surveiller votre IP warming."
channel: email
---

# IP warming automatisé {#automated-ip-warming}

> Utilisez l'IP warming automatisé pour augmenter progressivement le volume d'e-mails envoyés depuis de nouvelles adresses IP dédiées afin de construire votre réputation d'expéditeur auprès des fournisseurs de boîtes de réception. Pour les questions fréquentes, consultez la [FAQ sur l'IP warming automatisé]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq).

## Fonctionnement {#how-it-works}

Vous pouvez utiliser l'IP warming automatisé pour augmenter progressivement votre volume d'envoi quotidien, permettant ainsi aux fournisseurs de boîtes de réception d'apprendre à reconnaître et à faire confiance à vos habitudes d'envoi. Lorsque vous ajoutez un domaine à votre espace de travail, vous pouvez sélectionner la tuile **Automated IP Warming** dans la section **Pick up where you left off** de votre tableau de bord d'accueil. Cette tuile reste visible pendant 60 jours tant que votre espace de travail se trouve dans la fenêtre d'onboarding des nouveaux expéditeurs, et est masquée une fois que vous avez complété au moins un plan.

Chaque plan d'IP warming automatisé est associé à une adresse d'expéditeur. Cette adresse d'expéditeur correspond à un sous-domaine d'envoi et à un pool d'IP. Si le pool contient plusieurs IP dédiées, Braze les réchauffe ensemble dans un seul plan.

Braze envoie d'abord aux utilisateurs abonnés les plus engagés, ce qui permet au volume quotidien d'augmenter à un rythme conforme aux bonnes pratiques. Ensuite, Braze suit les signaux d'engagement et de livrabilité. Si Braze détecte un problème, le système ajuste automatiquement votre planification.

Une fois que vous avez complété au moins un plan, vous pouvez consulter les plans terminés dans **Paramètres** > **Préférences e-mail** > **Automated IP warming**.

## Prérequis {#prerequisites}

Pour effectuer un IP warming automatisé, vous devez disposer des éléments suivants :

- Un sous-domaine vérifié et des adresses IP actives
- Des autorisations pour consulter et configurer un plan :
    - "View Email Settings" pour consulter les plans d'IP warming et le widget du tableau de bord d'accueil
    - "View Email Templates" pour sélectionner des modèles d'e-mail
    - "View Segments" pour sélectionner des Segments
- Des autorisations pour lancer un plan :
    - "Edit Email Settings"
    - "Edit Campaigns"
    - "Launch Campaigns"
    - "Approve Campaigns"

{% alert note %}
Si le flux de travail d'approbation des campagnes est activé, Braze approuve automatiquement les campagnes créées par l'IP warming automatisé en votre nom.
{% endalert %}

## Configurer un plan automatisé d'IP warming {#set-up-an-automated-ip-warming-plan}

### Étape 1 : Définir une planification {#step-1-set-a-schedule}

1. Saisissez un **nom de plan** unique. Les noms de plan ne peuvent contenir que des lettres, des chiffres, des tirets et des underscores, et doivent être uniques dans votre espace de travail. Un nom de plan est requis avant de pouvoir lancer.
2. Dans la section **Informations d'envoi**, sélectionnez l'**adresse d'expéditeur** pour laquelle effectuer l'IP warming. Braze affiche le **pool d'IP** associé et le nombre d'**adresses IP dans le pool** pour cette adresse d'expéditeur.
3. Saisissez le **volume d'envoi quotidien actuel** et le **volume d'envoi cible**. Braze suggère un volume d'envoi cible allant jusqu'à 2 millions d'envois par IP dans le pool sélectionné. Si votre volume d'envoi quotidien actuel est de 0, le premier jour de votre planification commence avec un maximum de 50 envois par IP, plafonné à 500 au total.
4. Sélectionnez la date de début de l'IP warming automatisé. Cette date doit être au moins un jour après le lancement du plan.
5. Saisissez l'heure d'envoi. Les messages sont envoyés dans le fuseau horaire de l'espace de travail (ou le fuseau horaire de l'entreprise si l'espace de travail n'a pas de remplacement défini).
6. Sélectionnez **Suivant : Segments** pour continuer la configuration.

![Exemple de détails de planification.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Étape 2 : Sélectionner et classer les segments {#step-2-select-and-rank-segments}

1. Ensuite, sélectionnez les segments à cibler. Pendant l'IP warming, Braze commence par envoyer à vos utilisateurs les plus engagés et augmente progressivement le volume d'envoi au fil du temps, en ajoutant lentement des segments avec moins d'engagement.
2. Ensuite, glissez-déposez les segments pour les classer du plus fort au plus faible engagement. Un engagement élevé comprend les destinataires qui ouvrent et cliquent régulièrement sur vos e-mails. Un engagement faible comprend les destinataires dont l'engagement avec vos e-mails est irrégulier ou qui n'ont pas interagi avec vos e-mails depuis très longtemps.
3. Sélectionnez **Suivant : Messages** pour continuer la configuration.

{% alert important %}
Assurez-vous que le nombre total d'utilisateurs pouvant recevoir des e-mails dans l'ensemble des segments sélectionnés est supérieur ou égal à votre **volume d'envoi cible**. Lorsque votre audience est inférieure à votre volume cible, certains utilisateurs reçoivent plus d'un modèle d'e-mail le même jour. Pour plus d'informations, consultez [Taille de l'audience et envois multiples par utilisateur](#audience-size-and-multiple-sends-per-user).
{% endalert %}

![Deux segments sélectionnés à cibler pour l'IP warming automatisé.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Étape 3 : Sélectionner les messages à envoyer {#step-3-select-the-messages-to-send}

1. Sélectionnez **Sélectionner des modèles d'e-mail**.
2. Choisissez les modèles d'e-mail pour les messages à envoyer. Le contenu que vous envoyez pendant l'IP warming doit encourager les ouvertures et les clics. Nous recommandons de choisir du contenu qui a bien fonctionné par le passé. Par exemple, vous pouvez utiliser des offres promotionnelles pour encourager l'engagement immédiat et les achats.
3. Sélectionnez **Sélectionner les modèles**. Braze calcule le nombre de modèles requis avant que vous puissiez lancer. Nous recommandons de fournir plus de modèles que le minimum requis afin de permettre au système de s'adapter aux problèmes de livrabilité sans s'arrêter.
4. Après avoir ajouté le nombre de modèles requis, sélectionnez **Suivant : Résumé**.

{% alert important %}
Les modifications apportées aux Campaigns créées à partir de l'outil d'IP warming (telles que la modification de la date planifiée, du segment ou du volume) ne sont pas reflétées sur la page **Résumé** de l'IP warming.
{% endalert %}

### Étape 4 : Sélectionner les événements de conversion {#step-4-select-conversion-events}

Vous pouvez définir jusqu'à quatre des événements de conversion suivants à suivre. Ces événements de conversion ne peuvent pas être mis à jour après le lancement du plan automatisé d'IP warming.

- Démarrage de session
- Passation de commande
- Exécution d'un événement personnalisé
- Mise à jour de l'application
- Ouverture d'e-mail
- Clic sur un e-mail

Ensuite, sélectionnez la date limite de conversion, qui est le délai maximal pouvant s'écouler entre l'entrée d'un utilisateur dans une Campaign et l'événement de conversion.

![Paramètres de conversion montrant la sélection des événements de conversion et la date limite de conversion.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Étape 5 : Vérifier et lancer {#step-5-review-and-launch}

Vérifiez les détails de votre plan d'IP warming. Ensuite, sélectionnez **Lancer**.

## IP warming multiple {#multiple-ip-warming}

Utilisez plusieurs plans d'IP warming automatisé lorsque vous devez réchauffer plusieurs adresses d'expédition ou pools d'IP.

| Scénario | Recommandation |
| --- | --- |
| Plusieurs IP dédiées dans un seul pool d'IP | Créez un plan et sélectionnez l'adresse d'expédition pour ce pool |
| Plusieurs pools d'IP ou adresses d'expédition | Créez un plan distinct pour chaque adresse d'expédition |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Scénarios d'IP warming multiple" }

### Réchauffer plusieurs IP dans un seul pool {#warm-multiple-ips-in-one-pool}

Lorsque vous sélectionnez une adresse d'expédition à l'[étape 1 : Définir une planification](#step-1-set-a-schedule), Braze affiche le pool d'IP associé et les adresses IP du pool. Braze utilise le nombre d'IP pour construire votre calendrier de montée en puissance et suggérer votre volume d'envoi cible.

Si votre **volume d'envoi quotidien actuel** est de 0, le premier jour planifié commence avec un maximum de 50 envois par IP dans le pool, plafonné à 500 au total. Braze suggère un **volume d'envoi cible** pouvant atteindre 2 millions d'envois par IP dans le pool.

### Réchauffer plusieurs pools d'IP {#warm-multiple-ip-pools}

Pour réchauffer plusieurs adresses d'expédition ou pools d'IP :

1. Accédez à **Paramètres** > **Préférences e-mail** > **IP warming automatisé**.
2. Sélectionnez **Nouveau plan d'IP warming**.
3. Saisissez un **nom de plan** unique.
4. Complétez la configuration pour cette adresse d'expédition.
5. Répétez l'opération pour chaque adresse d'expédition ou pool d'IP supplémentaire à réchauffer.

Suivez chaque plan depuis le tableau **IP warming automatisé**. Chaque plan dispose de sa propre planification, de ses propres Segments, modèles, Campaigns et outil de suivi. Les plans peuvent avoir le statut **Brouillon**, **En cours**, **Terminé** ou **Arrêté**.

{% alert important %}
Évitez d'envoyer des Campaigns volumineuses hors warming depuis la même adresse d'expédition ou le même pool d'IP tant qu'un plan d'IP warming automatisé est actif. Les envois supplémentaires pendant le warming peuvent affecter les signaux de livrabilité et rendre difficile l'isolation des problèmes.
{% endalert %}

## Pendant l'IP warming actif {#during-active-ip-warming}

Les campagnes d'IP warming sont créées à minuit dans le fuseau horaire effectif pour le jour en cours et le jour suivant (0 à 1 jour avant l'envoi). Le lancement d'un plan crée également les campagnes à venir immédiatement. Ces campagnes sont automatiquement nommées selon le format suivant : `IP Warming Day [X] - [Date] - [Template Name]`.

Lorsque l'objectif d'envoi quotidien ciblé est atteint, le système arrête l'envoi pour cette journée afin de protéger votre réputation.

Braze évalue la livrabilité des campagnes envoyées il y a 12 à 20 heures. Si l'un des seuils suivants est dépassé, Braze maintient le volume pour le prochain jour d'envoi au lieu de l'augmenter :

- Taux de livraison inférieur à 90 %
- Taux d'ouverture inférieur à 10 %
- Taux de rebond supérieur à 5 %
- Taux de signalement de courrier indésirable supérieur à 0,04 %

Pour savoir ce qui se passe lorsque le volume est maintenu, consultez [Que se passe-t-il lorsque le volume est maintenu ?]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq#what-happens-when-volume-is-held).

## Taille de l'audience et envois multiples par utilisateur {#audience-size-and-multiple-sends-per-user}

Pour atteindre l'objectif d'envoi de chaque jour, Braze parcourt les modèles d'e-mail que vous avez sélectionnés. Au sein d'un plan, Braze exclut les utilisateurs qui ont déjà reçu un modèle donné, mais ceux qui ont reçu un modèle différent restent éligibles. Lorsque l'audience disponible pour la planification du jour est épuisée, le plan recommence à parcourir vos modèles, de sorte que certains utilisateurs reçoivent un deuxième modèle le même jour.

Si le nombre total d'utilisateurs pouvant recevoir des e-mails dans vos Segments sélectionnés est inférieur à votre **Volume d'envoi cible**, ce résultat est inévitable le dernier jour ou les derniers jours du plan, lorsque le volume quotidien est à son maximum. Par exemple, si vos Segments contiennent 400 000 utilisateurs pouvant recevoir des e-mails et que votre volume d'envoi cible est de 600 000, environ 200 000 utilisateurs reçoivent deux modèles le dernier jour et les 200 000 utilisateurs restants en reçoivent un.

Les utilisateurs peuvent également recevoir différents modèles à différents jours, même lorsque votre audience est plus grande que votre volume d'envoi cible. Étant donné que Braze répartit l'audience de chaque jour entre vos modèles sans tenir compte du modèle qu'un utilisateur a reçu précédemment, un utilisateur ayant reçu un modèle peut être sélectionné pour un modèle différent plus tard dans le plan.

Braze ne vous empêche pas de lancer un plan lorsque votre volume d'envoi cible est supérieur à votre audience disponible. Pour limiter chaque utilisateur à un seul modèle par jour d'envoi, effectuez l'une des actions suivantes avant de lancer :

- Ajoutez des Segments afin que le nombre total d'utilisateurs pouvant recevoir des e-mails soit supérieur ou égal à votre volume d'envoi cible.
- Réduisez votre **Volume d'envoi cible** pour qu'il ne dépasse pas le nombre total d'utilisateurs pouvant recevoir des e-mails.

## Arrêter un plan d'IP warming {#stop-an-ip-warmup-plan}

Vous pouvez arrêter un plan d'IP warming pour empêcher la création de futures Campaigns. L'arrêt d'un plan désactive également toutes les Campaigns associées. Une fois un plan arrêté, vous ne pouvez pas le reprendre. Configurez un nouveau plan pour reprendre là où vous vous étiez arrêté en :

- Téléchargeant les données existantes de votre plan arrêté pour les conserver dans vos dossiers
- Mettant à jour le **volume d'envoi quotidien actuel** avec le volume le plus récent
- Ajoutant un filtre à un Segment si vous prévoyez d'utiliser le même Segment que lors du dernier IP warming, en excluant les utilisateurs qui ont déjà reçu des Campaigns précédentes

## Quand l'IP warming est terminé {#when-an-ip-warming-completes}

L'IP warming est marqué comme terminé lorsque le dernier jour de l'IP warming se termine à minuit dans le fuseau horaire de votre espace de travail (ou le fuseau horaire de l'entreprise si l'espace de travail n'a pas de remplacement). Par exemple, si la dernière campagne du plan est envoyée à 20 h, le plan est marqué comme terminé à minuit, quatre heures plus tard.

Les plans terminés restent disponibles depuis **Paramètres** > **Préférences e-mail** > **IP warming automatisé**. Le suivi reste également sur le tableau de bord d'accueil pendant 90 jours après la fin du plan. Au bout de 90 jours, le suivi du tableau de bord d'accueil est supprimé.

Le téléchargement des données inclut ces indicateurs e-mail standards :

- _Envoyés_
- _Livrés_
- _Rebonds_
- _Signalements de courrier indésirable_
- _Ouvertures totales_
- _Ouvertures uniques_
- _Cliqués_
- _Désabonnements_

Si une journée comporte plusieurs campagnes utilisées pour atteindre les exigences de volume, celles-ci sont agrégées dans la vue quotidienne.

![Suivi de l'IP warming avec le volume d'envoi pour la semaine du 16 janvier.]({% image_buster /assets/img/automated_ip_warming_example.png %})