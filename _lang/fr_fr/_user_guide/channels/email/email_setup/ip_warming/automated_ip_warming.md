---
nav_title: IP warming automatisé
article_title: IP warming automatisé
page_order: 1
page_type: reference
description: "Cet article de référence traite du réchauffement d'adresses IP automatisé et explique comment surveiller votre réchauffement d'adresses IP."
channel: email
---

# IP warming automatisé {#automated-ip-warming}

> Utilisez le réchauffement d'adresses IP automatisé pour augmenter progressivement le volume d'e-mails envoyés depuis une nouvelle adresse IP et ainsi construire votre réputation d'expéditeur auprès des fournisseurs de boîtes de réception.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Automated IP warming' %}

## Fonctionnement {#how-it-works}

Vous pouvez utiliser le réchauffement d'adresses IP automatisé pour augmenter progressivement votre volume d'envoi quotidien, afin que les fournisseurs de boîtes de réception apprennent à connaître et à faire confiance à vos habitudes d'envoi. Lorsque vous ajoutez un domaine à votre espace de travail, vous pouvez sélectionner la vignette **Automated IP Warming** dans la section **Pick up where you left off** de votre tableau de bord d'accueil. Cette vignette reste affichée pendant 60 jours.

Braze envoie d'abord vos messages aux utilisateurs abonnés les plus engagés, ce qui permet au volume quotidien d'augmenter à un rythme conforme aux meilleures pratiques. Braze suit ensuite les signaux d'engagement et de livrabilité. Si Braze détecte un problème, le système ajuste automatiquement votre planification.

{% alert note %}
Vous ne pouvez effectuer qu'un seul réchauffement d'adresses IP.
{% endalert %}

## Conditions préalables {#prerequisites}

Pour effectuer un réchauffement d'adresses IP automatisé, vous devez disposer des éléments suivants :

- Un sous-domaine vérifié et des adresses IP actives
- Les autorisations pour consulter et lancer un réchauffement d'adresses IP
    - « View Usage Data » pour consulter la section de réchauffement d'adresses IP
    - « View Email Templates » pour consulter et sélectionner les modèles d'e-mail pour le réchauffement d'adresses IP
    - « Manage Email Settings » pour lancer le réchauffement d'adresses IP
- « Access Campaigns »
- « Approve and Deny Campaigns » si le flux de travail d'approbation pour les campagnes est activé
    - Braze approuve automatiquement les campagnes créées à partir du réchauffement d'adresses IP automatisé en votre nom.

## Configurer un plan de réchauffement d'adresses IP automatisé {#set-up-an-automated-ip-warming-plan}

### Étape 1 : Définir une planification {#step-1-set-a-schedule}

1. Dans la section **Sending information**, sélectionnez l'adresse **From address** pour laquelle réchauffer les adresses IP.
2. Saisissez le volume d'envoi quotidien actuel et le volume d'envoi cible.
3. Sélectionnez la date de début du réchauffement d'adresses IP automatisé. Cette date doit être au moins un jour après le lancement du plan.
4. Saisissez l'heure d'envoi. Les messages sont envoyés dans le fuseau horaire de la société.
5. Sélectionnez **Next: Segments** pour poursuivre la configuration.

![Exemple de détails de planification.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Étape 2 : Sélectionner et classer les segments {#step-2-select-and-rank-segments}

1. Sélectionnez ensuite les segments à cibler. Pendant le réchauffement d'adresses IP, Braze commence par envoyer à vos utilisateurs les plus engagés et augmente progressivement le volume d'envoi au fil du temps, en ajoutant lentement des segments avec un engagement moindre.
2. Glissez-déposez les segments pour les classer de l'engagement le plus élevé au plus faible. Un engagement élevé inclut les destinataires qui ouvrent et cliquent régulièrement sur vos e-mails. Un engagement faible inclut les destinataires qui sont irréguliers dans leur engagement avec vos e-mails ou qui n'ont pas interagi avec vos e-mails depuis très longtemps.
3. Sélectionnez **Next: Messages** pour poursuivre la configuration.

![Deux segments sélectionnés à cibler pour le réchauffement d'adresses IP automatisé.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Étape 3 : Sélectionner les messages à envoyer {#step-3-select-the-messages-to-send}

1. Sélectionnez **Select email templates**.
2. Choisissez les modèles d'e-mail pour les messages à envoyer. Le contenu que vous envoyez pendant le réchauffement d'adresses IP doit encourager les ouvertures et les clics. Nous recommandons de choisir du contenu qui a bien fonctionné par le passé. Par exemple, vous pouvez utiliser des offres promotionnelles pour encourager l'engagement immédiat et les achats.
3. Sélectionnez **Select templates**. Braze calcule le nombre de modèles requis avant que vous puissiez lancer le plan. Nous recommandons de fournir plus de modèles que le minimum requis afin de permettre au système de s'adapter aux problèmes de livrabilité sans s'arrêter.
4. Après avoir ajouté le nombre requis de modèles, sélectionnez **Next: Summary**.

{% alert important %}
Les modifications apportées aux campagnes créées à partir de l'outil de réchauffement d'adresses IP (comme le changement de la date planifiée, du segment ou du volume) ne sont pas reflétées sur la page **Summary** du réchauffement d'adresses IP.
{% endalert %}

### Étape 4 : Sélectionner les événements de conversion {#step-4-select-conversion-events}

Vous pouvez définir jusqu'à quatre des événements de conversion suivants à suivre. Ces événements de conversion ne peuvent pas être mis à jour après le lancement du plan de réchauffement d'adresses IP automatisé.

- Démarre une session
- Passe une commande
- Effectue un événement personnalisé
- Met à jour l'application
- Ouvre un e-mail
- Clique sur un e-mail

Ensuite, sélectionnez la date limite de conversion, qui correspond au temps maximum pouvant s'écouler entre l'entrée d'un utilisateur dans une campagne et l'événement de conversion.

![Paramètres de conversion montrant la sélection des événements de conversion et la date limite de conversion.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Étape 5 : Vérifier et lancer {#step-5-review-and-launch}

Vérifiez les détails de votre plan de réchauffement d'adresses IP. Puis, sélectionnez **Launch**.

## Pendant le réchauffement d'adresses IP actif {#during-active-ip-warming}

Les campagnes de réchauffement d'adresses IP sont créées 1 à 2 jours à l'avance, sauf si vous lancez un réchauffement d'adresses IP le lendemain. Ces campagnes sont automatiquement nommées selon le format suivant : `IP Warming Day [X] - [Date] - [Template Name]`.

Lorsque l'objectif d'envoi quotidien ciblé est atteint, le système arrête les envois pour la journée afin de protéger votre réputation.

Le système surveille la santé de vos envois en se basant sur les références sectorielles suivantes :

- Le taux de distribution chute en dessous ou est égal à 90 %
- Le taux d'ouverture est inférieur à 10 %
- Les rebonds sont supérieurs à 5 %
- Les taux de signalement de courrier indésirable sont supérieurs à 0,04 %

Si les statistiques sont en dessous de nos références, le système maintient le volume le jour suivant au lieu de l'augmenter, afin de limiter les risques pour votre réputation d'expéditeur.

## Arrêter un plan de réchauffement d'adresses IP {#stop-an-ip-warmup-plan}

Braze vous permet d'arrêter le réchauffement d'adresses IP et la création de futures campagnes, mais si une campagne est déjà active ou planifiée dans les prochaines 24 à 48 heures, vous devrez peut-être arrêter manuellement la campagne concernée. L'arrêt d'un plan de réchauffement d'adresses IP arrête également toutes les campagnes associées.

Cependant, une fois arrêté, le réchauffement d'adresses IP ne peut pas être repris. Vous devez configurer un nouveau plan pour reprendre là où vous vous êtes arrêté en :

- Téléchargeant les données existantes de votre plan arrêté pour les conserver dans vos archives, car une fois que vous démarrez un nouveau réchauffement d'adresses IP, le suivi précédent sera supprimé
- Mettant à jour le **Current daily send volume** avec le volume le plus récent
- Ajoutant un filtre à un segment si vous prévoyez d'utiliser le même segment que lors du dernier réchauffement d'adresses IP, en excluant les utilisateurs qui ont déjà reçu les campagnes précédentes

## Lorsqu'un réchauffement d'adresses IP se termine {#when-an-ip-warmup-completes}

Le réchauffement d'adresses IP est marqué comme terminé lorsque le dernier jour de réchauffement se termine à minuit dans le fuseau horaire de votre société. Par exemple, si la dernière campagne envoyée dans le plan de réchauffement d'adresses IP est envoyée à 20 h, alors le plan est marqué comme terminé après quatre heures.

Le suivi reste sur la page d'accueil pendant 90 jours après la fin du plan. Après 90 jours, le suivi est supprimé. Le téléchargement des données inclut ces indicateurs d'e-mail standard :

- _Envoyés_
- _Distribués_
- _Rebonds_
- _Signalements de courrier indésirable_
- _Ouvertures totales_
- _Ouvertures uniques_
- _Cliqués_
- _Désabonnés_

Si une journée inclut plusieurs campagnes utilisées pour atteindre les exigences de volume, celles-ci sont agrégées dans la vue quotidienne.

![Suivi du réchauffement d'adresses IP avec le volume d'envoi pour la semaine du 16 janvier.]({% image_buster /assets/img/automated_ip_warming_example.png %})