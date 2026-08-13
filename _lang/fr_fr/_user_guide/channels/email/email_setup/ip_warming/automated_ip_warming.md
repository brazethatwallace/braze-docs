---
nav_title: IP warming automatisé
article_title: IP warming automatisé
page_order: 1
page_type: reference
description: "Cet article de référence traite de l'IP warming automatisé et explique comment surveiller votre IP warming."
channel: email
---

# IP warming automatisé {#automated-ip-warming}

> Utilisez l'IP warming automatisé pour augmenter progressivement le volume d'e-mails envoyés depuis de nouvelles adresses IP dédiées afin de construire votre réputation d'expéditeur auprès des fournisseurs de boîtes de réception.

## Fonctionnement {#how-it-works}

Vous pouvez utiliser l'IP warming automatisé pour augmenter progressivement votre volume d'envoi quotidien, permettant ainsi aux fournisseurs de boîtes de réception d'apprendre et de faire confiance à vos habitudes d'envoi. Lorsque vous ajoutez un domaine à votre espace de travail, vous pouvez sélectionner la tuile **Automated IP Warming** dans la section **Pick up where you left off** de votre tableau de bord d'accueil. Cette tuile reste visible pendant 60 jours tant que votre espace de travail se trouve dans la fenêtre d'onboarding pour les nouveaux expéditeurs.

Chaque plan d'IP warming automatisé est lié à une adresse d'expédition. Cette adresse d'expédition correspond à un sous-domaine d'envoi et à un pool d'adresses IP. Si le pool contient plusieurs adresses IP dédiées, Braze les réchauffe ensemble dans un seul plan.

Braze envoie d'abord à vos utilisateurs abonnés les plus engagés, ce qui permet au volume quotidien de croître à un rythme conforme aux bonnes pratiques. Ensuite, Braze suit les signaux d'engagement et de livrabilité. Si Braze détecte un problème, le système ajuste automatiquement votre planification.

Une fois que vous avez terminé au moins un plan, vous pouvez consulter les plans terminés dans **Paramètres** > **Préférences e-mail** > **Automated IP warming**.

{% alert note %}
Si vous ne voyez qu'une expérience à plan unique dans votre tableau de bord, votre espace de travail n'a peut-être pas encore accès aux plans d'IP warming multiples. Contactez votre équipe de compte Braze pour en savoir plus sur la disponibilité.
{% endalert %}

## Prérequis {#prerequisites}

Pour effectuer un IP warming automatisé, vous devez disposer des éléments suivants :

- Sous-domaine vérifié et adresses IP actives
- Autorisations pour consulter et lancer un IP warming
    - « View Usage Data » pour consulter la section IP warming
    - « View Email Templates » pour consulter et sélectionner les modèles d'e-mail pour l'IP warming
    - « Manage Email Settings » pour lancer l'IP warming
- « Access Campaigns »
- « Approve and Deny Campaigns » si le workflow d'approbation pour les Campaigns est activé
    - Braze approuve automatiquement les Campaigns créées à partir de l'IP warming automatisé en votre nom.

{% alert important %}
Cette fonctionnalité peut ne pas être prise en charge selon votre infrastructure e-mail.
{% endalert %}

## Configurer un plan automatisé d'IP warming {#set-up-an-automated-ip-warming-plan}

### Étape 1 : Définir une planification {#step-1-set-a-schedule}

1. Si votre espace de travail prend en charge plusieurs plans d'IP warming, saisissez un **Nom de plan** unique. Les noms de plan ne peuvent contenir que des lettres, des chiffres, des tirets et des underscores, et doivent être uniques dans votre espace de travail. Un nom de plan est requis avant de pouvoir lancer le plan.
2. Dans la section **Informations d'envoi**, sélectionnez l'**adresse d'expédition** pour laquelle réchauffer les adresses IP. Braze affiche le **pool d'IP** associé et le nombre d'**adresses IP dans le pool** pour cette adresse d'expédition.
3. Saisissez le **volume d'envoi quotidien actuel** et le **volume d'envoi cible**. Braze suggère un volume d'envoi cible allant jusqu'à 2 millions d'envois par IP dans le pool sélectionné. Si votre volume d'envoi quotidien actuel est de 0, le premier jour de votre planification commence à un maximum de 50 envois par IP, plafonné à 500 au total.
4. Sélectionnez la date de début de l'IP warming automatisé. Cette date doit être au moins un jour après le lancement du plan.
5. Saisissez l'heure d'envoi. Les messages sont envoyés dans le fuseau horaire de l'entreprise.
6. Sélectionnez **Suivant : Segments** pour poursuivre la configuration.

![Exemple de détails de planification.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Étape 2 : Sélectionner et classer les segments {#step-2-select-and-rank-segments}

1. Ensuite, sélectionnez les segments à cibler. Pendant l'IP warming, Braze commence par envoyer à vos utilisateurs les plus engagés, puis augmente progressivement le volume d'envoi au fil du temps en ajoutant lentement des segments avec un engagement moindre.
2. Puis, glissez-déposez les segments pour les classer de l'engagement le plus élevé au plus faible. Un engagement élevé inclut les destinataires qui ouvrent et cliquent régulièrement sur vos e-mails. Un engagement faible inclut les destinataires dont l'interaction avec vos e-mails est irrégulière ou qui n'ont pas interagi avec vos e-mails depuis très longtemps.
3. Sélectionnez **Suivant : Messages** pour poursuivre la configuration.

![Deux segments sélectionnés à cibler pour l'IP warming automatisé.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Étape 3 : Sélectionner les messages à envoyer {#step-3-select-the-messages-to-send}

1. Sélectionnez **Sélectionner des modèles d'e-mail**.
2. Choisissez les modèles d'e-mail pour les messages à envoyer. Le contenu que vous envoyez pendant l'IP warming doit encourager les ouvertures et les clics. Nous recommandons de choisir du contenu qui a été bien reçu par le passé. Par exemple, vous pouvez utiliser des offres promotionnelles pour encourager un engagement et des achats immédiats.
3. Sélectionnez **Sélectionner les modèles**. Braze calcule le nombre de modèles requis avant que vous puissiez lancer le plan. Nous recommandons de fournir plus de modèles que le minimum requis afin de permettre au système de s'adapter aux problèmes de livrabilité sans s'arrêter.
4. Après avoir ajouté le nombre requis de modèles, sélectionnez **Suivant : Résumé**.

{% alert important %}
Les modifications apportées aux Campaigns créées à partir de l'outil d'IP warming (comme le changement de la date planifiée, du segment ou du volume) ne sont pas reflétées sur la page **Résumé** de l'IP warming.
{% endalert %}

### Étape 4 : Sélectionner les événements de conversion {#step-4-select-conversion-events}

Vous pouvez définir jusqu'à quatre des événements de conversion suivants à suivre. Ces événements de conversion ne peuvent pas être mis à jour après le lancement du plan automatisé d'IP warming.

- Démarre une session
- Passe une commande
- Effectue un événement personnalisé
- Met à jour l'application
- Ouvre un e-mail
- Clique sur un e-mail

Ensuite, sélectionnez la date limite de conversion, qui correspond au temps maximum pouvant s'écouler entre l'entrée d'un utilisateur dans une Campaign et l'événement de conversion.

![Paramètres de conversion montrant la sélection des événements de conversion et la date limite de conversion.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Étape 5 : Vérifier et lancer {#step-5-review-and-launch}

Vérifiez les détails de votre plan d'IP warming. Puis, sélectionnez **Lancer**.

## IP warming multiple {#multiple-ip-warming}

Utilisez plusieurs plans d'IP warming automatisés lorsque vous devez réchauffer plusieurs adresses d'expéditeur ou pools d'IP.

| Scénario | Recommandation |
| --- | --- |
| Plusieurs IP dédiées dans un seul pool d'IP | Créez un plan et sélectionnez l'adresse d'expéditeur pour ce pool |
| Plusieurs pools d'IP ou adresses d'expéditeur | Créez un plan distinct pour chaque adresse d'expéditeur |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Scénarios d'IP warming multiple" }

### Réchauffer plusieurs IP dans un seul pool {#warm-multiple-ips-in-one-pool}

Lorsque vous sélectionnez une adresse d'expéditeur à l'[étape 1 : Définir une planification](#step-1-set-a-schedule), Braze affiche le pool d'IP associé et les adresses IP du pool. Braze utilise le nombre d'IP pour construire votre calendrier de montée en charge et suggérer votre volume d'envoi cible.

Si votre **Volume d'envoi quotidien actuel** est de 0, le premier jour planifié commence avec jusqu'à 50 envois par IP dans le pool, plafonné à 500 au total. Braze suggère un **Volume d'envoi cible** allant jusqu'à 2 millions d'envois par IP dans le pool.

### Réchauffer plusieurs pools d'IP {#warm-multiple-ip-pools}

Pour réchauffer plusieurs adresses d'expéditeur ou pools d'IP :

1. Accédez à **Paramètres** > **Préférences e-mail** > **IP warming automatisé**.
2. Sélectionnez **Nouveau plan d'IP warming**.
3. Saisissez un **Nom de plan** unique.
4. Complétez la configuration pour cette adresse d'expéditeur.
5. Répétez l'opération pour chaque adresse d'expéditeur ou pool d'IP supplémentaire à réchauffer.

Suivez chaque plan depuis le tableau **IP warming automatisé**. Chaque plan possède sa propre planification, ses propres Segments, modèles, Campaigns et son propre suivi. Les plans peuvent avoir le statut **Brouillon**, **En cours**, **Terminé** ou **Arrêté**.

{% alert important %}
Évitez d'envoyer des Campaigns volumineuses hors réchauffement depuis la même adresse d'expéditeur ou le même pool d'IP lorsqu'un plan d'IP warming automatisé est actif. Des envois supplémentaires pendant le réchauffement peuvent affecter les signaux de livrabilité et compliquer l'isolation des problèmes.
{% endalert %}

## Pendant le warming IP actif {#during-active-ip-warming}

Les campaigns de warming IP sont créées 1 à 2 jours à l'avance, sauf si vous lancez un warming IP le lendemain. Ces campaigns sont automatiquement nommées selon le format suivant : `IP Warming Day [X] - [Date] - [Template Name]`.

Lorsque l'objectif d'envoi quotidien ciblé est atteint, le système arrête les envois pour la journée afin de protéger votre réputation.

Le système surveille votre santé en fonction des benchmarks suivants du secteur :

- Le taux de distribution chute en dessous ou est égal à 90 %
- Le taux d'ouverture est inférieur à 10 %
- Les rebonds sont supérieurs à 5 %
- Le taux de signalement de courrier indésirable est supérieur à 0,04 %

Si les statistiques sont en dessous de nos benchmarks, le système maintient le volume le jour suivant au lieu de l'augmenter, afin de limiter les risques pour votre réputation d'expéditeur.

## Arrêter un plan d'IP warming {#stop-an-ip-warmup-plan}

Braze vous permet d'arrêter l'IP warming et la création de futures Campaigns, mais si une Campaign est déjà active ou planifiée dans les 24 à 48 prochaines heures, vous devrez peut-être arrêter manuellement la Campaign spécifique. L'arrêt d'un plan d'IP warming arrête également toutes les Campaigns associées.

Cependant, une fois arrêté, l'IP warming ne peut pas être repris. Vous devez plutôt configurer un nouveau plan pour reprendre là où vous vous êtes arrêté en :

- Téléchargeant les données existantes de votre plan arrêté pour les conserver dans vos archives
- Mettant à jour le **Volume d'envoi quotidien actuel** avec le volume le plus récent
- Ajoutant un filtre à un Segment si vous prévoyez d'utiliser le même Segment que lors du dernier IP warming, en excluant les utilisateurs qui ont déjà reçu les Campaigns précédentes

## Lorsqu'un IP warming se termine {#when-an-ip-warmup-completes}

L'IP warming est marqué comme terminé lorsque le dernier jour de l'IP warming se termine à minuit dans le fuseau horaire de votre entreprise. Par exemple, si la dernière Campaign envoyée dans le plan d'IP warming est envoyée à 20 h, le plan est marqué comme terminé après quatre heures.

Les plans terminés restent disponibles depuis **Paramètres** > **Préférences e-mail** > **IP warming automatisé**. Si votre espace de travail utilise l'expérience à plan unique, le suivi reste également sur le tableau de bord d'accueil pendant 90 jours après la fin du plan. Après 90 jours, le suivi du tableau de bord d'accueil est supprimé.

Le téléchargement des données inclut ces indicateurs e-mail standard :

- _Envoyés_
- _Distribués_
- _Rebonds_
- _Signalements de courrier indésirable_
- _Ouvertures totales_
- _Ouvertures uniques_
- _Cliqués_
- _Désabonnements_

Si une journée inclut plusieurs Campaigns utilisées pour atteindre les exigences de volume, celles-ci sont agrégées dans la vue quotidienne.

![Suivi de l'IP warming avec le volume d'envoi pour la semaine du 16 janvier.]({% image_buster /assets/img/automated_ip_warming_example.png %})