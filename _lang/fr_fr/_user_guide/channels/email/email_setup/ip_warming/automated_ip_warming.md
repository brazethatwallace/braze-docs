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

Vous pouvez utiliser le réchauffement automatique d'IP pour augmenter progressivement votre volume d'envoi quotidien, permettant ainsi aux fournisseurs de boîtes de réception d'apprendre et de faire confiance à vos habitudes d'envoi. Lorsque vous ajoutez un domaine à votre espace de travail, vous pouvez sélectionner la tuile **Automated IP Warming** dans la section **Pick up where you left off** de votre tableau de bord d'accueil. Cette tuile reste visible pendant 60 jours tant que votre espace de travail se trouve dans la fenêtre d'onboarding pour les nouveaux expéditeurs. Si votre espace de travail prend en charge plusieurs plans, la tuile est également masquée une fois que vous avez terminé au moins un plan.

Chaque plan de réchauffement automatique d'IP est lié à une adresse d'expéditeur. Cette adresse d'expéditeur correspond à un sous-domaine d'envoi et à un pool d'IP. Si le pool contient plusieurs IP dédiées, Braze les réchauffe ensemble dans un seul plan.

Braze envoie d'abord à vos utilisateurs abonnés les plus engagés, ce qui permet au volume quotidien de croître à un rythme conforme aux bonnes pratiques. Ensuite, Braze suit les signaux d'engagement et de livrabilité. Si Braze détecte un problème, le système ajuste automatiquement votre planification.

Une fois que vous avez terminé au moins un plan, vous pouvez consulter les plans terminés dans **Settings** > **Email Preferences** > **Automated IP warming**.

{% alert note %}
Si vous ne voyez qu'une expérience à plan unique dans votre tableau de bord, votre espace de travail n'a peut-être pas encore accès à plusieurs plans de réchauffement d'IP. Contactez votre équipe de compte Braze pour en savoir plus sur la disponibilité.
{% endalert %}

## Prérequis {#prerequisites}

Pour effectuer un IP warming automatisé, vous devez disposer des éléments suivants :

- Un sous-domaine vérifié et des adresses IP actives
- Des autorisations pour consulter et configurer un plan :
    - « View Email Settings » pour consulter les plans d'IP warming et le widget du tableau de bord d'accueil
    - « View Email Templates » pour sélectionner des modèles d'e-mail
    - « View Segments » pour sélectionner des Segments
- Des autorisations pour lancer un plan :
    - « Edit Email Settings »
    - « Edit Campaigns »
    - « Launch Campaigns »
    - « Approve Campaigns »

{% alert note %}
Si le workflow d'approbation des campagnes est activé, Braze approuve automatiquement les campagnes créées par l'IP warming automatisé en votre nom.
{% endalert %}

{% alert important %}
Cette fonctionnalité peut ne pas être prise en charge selon votre infrastructure d'e-mail.
{% endalert %}

## Configurer un plan automatisé d'IP warming {#set-up-an-automated-ip-warming-plan}

### Étape 1 : Définir une planification {#step-1-set-a-schedule}

1. Si votre espace de travail prend en charge plusieurs plans d'IP warming, saisissez un **Nom de plan** unique. Les noms de plan ne peuvent contenir que des lettres, des chiffres, des tirets et des underscores, et doivent être uniques dans votre espace de travail. Un nom de plan est requis avant de pouvoir lancer le plan.
2. Dans la section **Informations d'envoi**, sélectionnez l'**adresse d'expédition** pour laquelle réchauffer les adresses IP. Braze affiche le **pool d'IP** associé et le nombre d'**adresses IP dans le pool** pour cette adresse d'expédition.
3. Saisissez le **volume d'envoi quotidien actuel** et le **volume d'envoi cible**. Braze suggère un volume d'envoi cible allant jusqu'à 2 millions d'envois par IP dans le pool sélectionné. Si votre volume d'envoi quotidien actuel est de 0, le premier jour de votre planification commence à un maximum de 50 envois par IP, plafonné à 500 au total.
4. Sélectionnez la date de début de l'IP warming automatisé. Cette date doit être au moins un jour après le lancement du plan.
5. Saisissez l'heure d'envoi. Les messages sont envoyés dans le fuseau horaire de l'espace de travail (ou le fuseau horaire de l'entreprise si l'espace de travail n'a pas de remplacement défini).
6. Sélectionnez **Suivant : Segments** pour poursuivre la configuration.

![Exemple de détails de planification.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Étape 2 : Sélectionner et classer les segments {#step-2-select-and-rank-segments}

1. Ensuite, sélectionnez les segments à cibler. Pendant l'IP warming, Braze commence par envoyer à vos utilisateurs les plus engagés, puis augmente progressivement le volume d'envoi au fil du temps en intégrant lentement des segments avec un engagement moindre.
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

Ensuite, sélectionnez la date limite de conversion, qui correspond au délai maximum pouvant s'écouler entre l'entrée d'un utilisateur dans une Campaign et l'événement de conversion.

![Paramètres de conversion montrant la sélection des événements de conversion et la date limite de conversion.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Étape 5 : Vérifier et lancer {#step-5-review-and-launch}

Vérifiez les détails de votre plan d'IP warming. Puis, sélectionnez **Lancer**.

## IP warming multiple {#multiple-ip-warming}

Utilisez plusieurs plans d'IP warming automatisés lorsque vous devez réchauffer plusieurs adresses d'expédition ou pools d'IP.

| Scénario | Recommandation |
| --- | --- |
| Plusieurs IP dédiées dans un seul pool d'IP | Créez un plan et sélectionnez l'adresse d'expédition pour ce pool |
| Plusieurs pools d'IP ou adresses d'expédition | Créez un plan distinct pour chaque adresse d'expédition |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Scénarios d'IP warming multiple" }

### Réchauffer plusieurs IP dans un seul pool {#warm-multiple-ips-in-one-pool}

Lorsque vous sélectionnez une adresse d'expédition à l'[étape 1 : Définir une planification](#step-1-set-a-schedule), Braze affiche le pool d'IP associé et les adresses IP du pool. Braze utilise le nombre d'IP pour construire votre calendrier de montée en charge et suggérer votre volume d'envoi cible.

Si votre **Volume d'envoi quotidien actuel** est de 0, le premier jour planifié commence avec jusqu'à 50 envois par IP dans le pool, plafonné à 500 au total. Braze suggère un **Volume d'envoi cible** pouvant atteindre 2 millions d'envois par IP dans le pool.

### Réchauffer plusieurs pools d'IP {#warm-multiple-ip-pools}

Pour réchauffer plusieurs adresses d'expédition ou pools d'IP :

1. Allez dans **Paramètres** > **Préférences e-mail** > **IP warming automatisé**.
2. Sélectionnez **Nouveau plan d'IP warming**.
3. Saisissez un **Nom de plan** unique.
4. Complétez la configuration pour cette adresse d'expédition.
5. Répétez l'opération pour chaque adresse d'expédition ou pool d'IP supplémentaire à réchauffer.

Suivez chaque plan depuis le tableau **IP warming automatisé**. Chaque plan possède sa propre planification, ses propres Segments, modèles, Campaigns et son propre suivi. Les plans peuvent avoir le statut **Brouillon**, **En cours**, **Terminé** ou **Arrêté**.

{% alert important %}
Évitez d'envoyer des Campaigns volumineuses hors réchauffement depuis la même adresse d'expédition ou le même pool d'IP pendant qu'un plan d'IP warming automatisé est actif. Des envois supplémentaires pendant le réchauffement peuvent affecter les signaux de livrabilité et compliquer l'isolation des problèmes.
{% endalert %}

## Pendant l'IP warming actif {#during-active-ip-warming}

Les campagnes d'IP warming sont créées à minuit dans le fuseau horaire effectif pour le jour en cours et le lendemain (0 à 1 jour avant l'envoi). Le lancement d'un plan crée également immédiatement les campagnes à venir. Ces campagnes sont automatiquement nommées selon le format suivant : `IP Warming Day [X] - [Date] - [Template Name]`.

Lorsque l'objectif d'envoi quotidien ciblé est atteint, le système arrête l'envoi pour cette journée afin de protéger votre réputation.

Braze évalue la livrabilité des campagnes envoyées entre 12 et 20 heures auparavant. Si l'un des seuils suivants est dépassé, Braze maintient le volume pour le prochain jour d'envoi au lieu de l'augmenter :

- Taux de livraison inférieur à 90 %
- Taux d'ouverture inférieur à 10 %
- Taux de rebond supérieur à 5 %
- Taux de signalement de courrier indésirable supérieur à 0,04 %

Pour savoir ce qui se passe lorsque le volume est maintenu, consultez [Que se passe-t-il lorsque le volume est maintenu ?]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq#what-happens-when-volume-is-held).

## Arrêter un plan d'IP warming {#stop-an-ip-warmup-plan}

Vous pouvez arrêter un plan d'IP warming pour empêcher la création de futures Campaigns. L'arrêt d'un plan désactive également toutes les Campaigns associées. Une fois un plan arrêté, vous ne pouvez pas le reprendre. Configurez un nouveau plan pour reprendre là où vous vous êtes arrêté en :

- Téléchargeant les données existantes de votre plan arrêté pour les conserver dans vos archives
- Mettant à jour le **Volume d'envoi quotidien actuel** avec le volume le plus récent
- Ajoutant un filtre à un Segment si vous prévoyez d'utiliser le même Segment que lors du dernier IP warming, en excluant les utilisateurs qui ont déjà reçu des Campaigns précédentes

## Lorsqu'un IP warming se termine {#when-an-ip-warming-completes}

L'IP warming est marqué comme terminé lorsque le dernier jour de l'IP warming se termine à minuit dans le fuseau horaire de votre espace de travail (ou le fuseau horaire de l'entreprise si l'espace de travail n'a pas de remplacement). Par exemple, si la dernière campagne du plan est envoyée à 20 h, le plan est marqué comme terminé à minuit, quatre heures plus tard.

Les plans terminés restent disponibles depuis **Paramètres** > **Préférences e-mail** > **IP warming automatisé**. Si votre espace de travail utilise l'expérience à plan unique, le suivi reste également sur le tableau de bord d'accueil pendant 90 jours après la fin du plan. Après 90 jours, le suivi du tableau de bord d'accueil est supprimé.

Le téléchargement des données inclut ces indicateurs e-mail standard :

- _Envoyés_
- _Livrés_
- _Rebonds_
- _Signalements de courrier indésirable_
- _Ouvertures totales_
- _Ouvertures uniques_
- _Cliqués_
- _Désabonnements_

Si une journée comprend plusieurs campagnes utilisées pour atteindre les exigences de volume, celles-ci sont agrégées dans la vue quotidienne.

![Suivi de l'IP warming avec le volume d'envoi pour la semaine du 16 janvier.]({% image_buster /assets/img/automated_ip_warming_example.png %})