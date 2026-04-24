---
nav_title: IP warming automatisé
article_title: IP warming automatisé
page_order: 1
page_type: reference
description: "Cet article de référence couvre l'IP warming automatisé et comment surveiller votre IP warming."
channel: email
---

# IP warming automatisé

> Utilisez l'IP warming automatisé pour augmenter progressivement le volume d'e-mails envoyés depuis une nouvelle adresse IP afin de construire la réputation de l'expéditeur auprès des fournisseurs de boîtes de réception.

{% multi_lang_include early_access_beta_alert.md feature='Automated IP warming' %}

## Comment ça fonctionne

Vous pouvez utiliser l'IP warming automatisé pour augmenter progressivement votre volume d'envoi quotidien, permettant aux fournisseurs de boîtes de réception d'apprendre et de faire confiance à vos habitudes d'envoi. Lorsque vous ajoutez un domaine à votre espace de travail, vous pouvez sélectionner la tuile **Automated IP Warming** dans la section **Pick up where you left off** de votre tableau de bord d'accueil, et cette tuile reste visible pendant 60 jours.

Braze envoie d'abord à vos utilisateurs abonnés les plus engagés, ce qui permet au volume quotidien de croître à un rythme conforme aux bonnes pratiques. Ensuite, Braze suit les signaux d'engagement et de livrabilité. Si Braze détecte des problèmes, le système ajuste automatiquement votre planification.

{% alert note %}
Vous ne pouvez effectuer qu'un seul IP warming.
{% endalert %}

## Conditions préalables

Pour effectuer un IP warming automatisé, vous devez disposer des éléments suivants :

- Un sous-domaine vérifié et des adresses IP actives
- Les autorisations pour consulter et lancer un IP warming
    - « View Usage Data » pour consulter la section IP warming
    - « View Email Templates » pour consulter et sélectionner les modèles d'e-mail pour l'IP warming
    - « Manage Email Settings » pour lancer l'IP warming
- « Access Campaigns »
- « Approve and Deny Campaigns » si le flux de travail d'approbation pour les campagnes est activé
    - Braze approuve automatiquement les campagnes créées à partir de l'IP warming automatisé en votre nom.

## Configurer un plan d'IP warming automatisé

### Étape 1 : Définir une planification

1. Dans la section **Sending information**, sélectionnez l'adresse **From address** pour laquelle réchauffer les adresses IP.
2. Saisissez le volume d'envoi quotidien actuel et le volume d'envoi cible.
3. Sélectionnez la date de début de l'IP warming automatisé. Cette date doit être au moins un jour après le lancement du plan.
4. Saisissez l'heure d'envoi. Les messages sont envoyés dans le fuseau horaire de la société.
5. Sélectionnez **Next: Segments** pour poursuivre la configuration.

![Exemple de détails de planification.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Étape 2 : Sélectionner et classer les segments

1. Ensuite, sélectionnez les segments à cibler. Pendant l'IP warming, Braze commence par envoyer à vos utilisateurs les plus engagés et augmente progressivement le volume d'envoi au fil du temps, en ajoutant lentement des segments avec un engagement moindre.
2. Puis, glissez-déposez les segments pour les classer de l'engagement le plus élevé au plus faible. Un engagement élevé inclut les destinataires qui ouvrent et cliquent régulièrement sur vos e-mails. Un engagement faible inclut les destinataires qui sont irréguliers dans leur engagement avec vos e-mails ou qui n'ont pas interagi avec vos e-mails depuis très longtemps.
3. Sélectionnez **Next: Messages** pour poursuivre la configuration.

![Deux segments sélectionnés à cibler pour l'IP warming automatisé.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Étape 3 : Sélectionner les messages à envoyer

1. Sélectionnez **Select email templates**.
2. Choisissez les modèles d'e-mail pour les messages à envoyer. Le contenu que vous envoyez pendant l'IP warming doit encourager les ouvertures et les clics. Nous recommandons de choisir du contenu qui a bien fonctionné par le passé. Par exemple, vous pouvez utiliser des offres promotionnelles pour encourager l'engagement immédiat et les achats.
3. Sélectionnez **Select templates**. Braze calcule le nombre de modèles requis avant que vous puissiez lancer le plan. Nous recommandons de fournir plus de modèles que le minimum requis afin de permettre au système de s'adapter aux problèmes de livrabilité sans s'arrêter.
4. Après avoir ajouté le nombre requis de modèles, sélectionnez **Next: Summary**.

{% alert important %}
Les modifications apportées aux campagnes créées à partir de l'outil d'IP warming (comme le changement de la date planifiée, du segment ou du volume) ne sont pas reflétées sur la page **Summary** de l'IP warming.
{% endalert %}

### Étape 4 : Sélectionner les événements de conversion

Vous pouvez définir jusqu'à quatre des événements de conversion suivants à suivre. Ces événements de conversion ne peuvent pas être mis à jour après le lancement du plan d'IP warming automatisé.

- Démarre une session
- Passe une commande
- Effectue un événement personnalisé
- Met à jour l'application
- Ouvre un e-mail
- Clique sur un e-mail

Ensuite, sélectionnez la date limite de conversion, qui correspond au temps maximum pouvant s'écouler entre l'entrée d'un utilisateur dans une campagne et l'événement de conversion.

![Paramètres de conversion montrant la sélection des événements de conversion et la date limite de conversion.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Étape 5 : Vérifier et lancer

Vérifiez les détails de votre plan d'IP warming. Puis, sélectionnez **Launch**.

## Pendant l'IP warming actif

Les campagnes d'IP warming sont créées 1 à 2 jours à l'avance, sauf si vous lancez un IP warming le lendemain. Ces campagnes sont automatiquement nommées selon le format suivant : `IP Warming Day [X] - [Date] - [Template Name]`.

Lorsque l'objectif d'envoi quotidien ciblé est atteint, le système arrête les envois pour la journée afin de protéger votre réputation.

Le système surveille votre santé d'envoi en se basant sur les références sectorielles suivantes :

- Le taux de distribution chute en dessous ou est égal à 90 %
- Le taux d'ouverture est inférieur à 10 %
- Les rebonds sont supérieurs à 5 %
- Les taux de signalement de courrier indésirable sont supérieurs à 0,04 %

Si les statistiques sont en dessous de nos références, le système maintient le volume le jour suivant au lieu de l'augmenter, afin de limiter les risques pour votre réputation d'expéditeur.

## Arrêter un plan d'IP warming

Braze vous permet d'arrêter l'IP warming et la création de futures campagnes, mais si une campagne est déjà active ou planifiée dans les prochaines 24 à 48 heures, vous devrez peut-être arrêter manuellement la campagne concernée. L'arrêt d'un plan d'IP warming arrête également toutes les campagnes associées.

Cependant, une fois arrêté, l'IP warming ne peut pas être repris. Vous devez configurer un nouveau plan pour reprendre là où vous vous êtes arrêté en :

- Téléchargeant les données existantes de votre plan arrêté pour les conserver dans vos archives, car une fois que vous démarrez un nouvel IP warming, le suivi précédent sera supprimé
- Mettant à jour le **Current daily send volume** avec le volume le plus récent
- Ajoutant un filtre à un segment si vous prévoyez d'utiliser le même segment que lors du dernier IP warming, en excluant les utilisateurs qui ont déjà reçu les campagnes précédentes

## Lorsqu'un IP warming se termine

L'IP warming est marqué comme terminé lorsque le dernier jour d'IP warming se termine à minuit dans le fuseau horaire de votre société. Par exemple, si la dernière campagne envoyée dans le plan d'IP warming est envoyée à 20 h, alors le plan est marqué comme terminé après quatre heures.

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

![Suivi de l'IP warming avec le volume d'envoi pour la semaine du 16 janvier.]({% image_buster /assets/img/automated_ip_warming_example.png %})