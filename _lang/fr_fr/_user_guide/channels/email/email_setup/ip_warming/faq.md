---
nav_title: FAQ
article_title: FAQ sur l'IP warming automatisé
channel: email
page_order: 3
description: "Réponses aux questions fréquemment posées sur l'IP warming automatisé dans Braze."
---

# FAQ sur l'IP warming automatisé {#automated-ip-warming-faq}

> Réponses aux questions courantes sur l'[IP warming automatisé]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming). Pour les concepts d'IP warming et les planifications manuelles, consultez [IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming).

## Quand utiliser l'IP warming automatisé ? {#when-should-i-use-automated-ip-warming}

Utilisez l'IP warming automatisé lorsque vous devez :

- Préchauffer de nouvelles adresses IP pour la première fois
- Préchauffer de nouvelles unités commerciales ou marques avec de nouveaux sous-domaines
- Repréchauffer des IP existantes pour améliorer la livrabilité
- Repréchauffer pour des fournisseurs de messagerie spécifiques afin d'améliorer la livrabilité

Pour les étapes de configuration et les prérequis, consultez [IP warming automatisé]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming).

## Jusqu'à combien de temps à l'avance la date de début doit-elle être définie ? {#how-far-in-advance-must-the-start-date-be}

La date de début doit être fixée au lendemain ou à une date ultérieure dans le fuseau horaire de votre espace de travail (ou le fuseau horaire de l'entreprise si l'espace de travail n'a pas de paramètre personnalisé).

Braze crée les Campaigns à minuit dans ce fuseau horaire pour le jour en cours et le jour suivant (0 à 1 jour avant l'envoi). Le lancement d'un plan crée également immédiatement les Campaigns à venir.

## Combien de modèles sont nécessaires ? {#how-many-templates-are-required}

Braze calcule le minimum à partir de vos volumes d'envoi planifiés et des utilisateurs contactables par e-mail dans les Segments sélectionnés (et non la taille totale du Segment). Fournissez plus de modèles que le minimum afin que le système puisse s'adapter aux problèmes de livrabilité sans s'arrêter. Pour plus de détails, consultez l'[Étape 3 : Sélectionner les messages à envoyer]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Puis-je utiliser le même Segment pour plusieurs tentatives de mise en chauffe ? {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

Au sein d'un même plan actif, Braze exclut automatiquement les utilisateurs qui ont déjà reçu des envois d'IP warming antérieurs pour le même modèle. Si vous arrêtez un plan et en démarrez un nouveau qui réutilise les mêmes Segments, ajoutez un filtre pour exclure les utilisateurs qui ont reçu des Campaigns du plan précédent.

## Un utilisateur peut-il recevoir plus d'un modèle d'e-mail le même jour ? {#can-a-user-receive-more-than-one-email-template-on-the-same-day}

Oui. Braze exclut les utilisateurs qui ont déjà reçu un modèle donné dans le cadre du plan, mais les utilisateurs ayant reçu un modèle différent restent éligibles. Lorsque l'audience disponible pour la planification d'un jour est épuisée, le plan recommence à parcourir vos modèles et certains utilisateurs reçoivent un deuxième modèle ce jour-là.

Cela se produit lorsque le nombre total d'utilisateurs pouvant recevoir des e-mails dans vos Segments sélectionnés est inférieur à votre **volume d'envoi cible**, le plus souvent le dernier jour ou les derniers jours du plan. Par exemple, avec 400 000 utilisateurs pouvant recevoir des e-mails et un volume d'envoi cible de 600 000, environ 200 000 utilisateurs reçoivent deux modèles le dernier jour. Pour éviter cela, maintenez votre nombre total d'utilisateurs pouvant recevoir des e-mails supérieur ou égal à votre volume d'envoi cible. Pour en savoir plus, consultez [Taille de l'audience et envois multiples par utilisateur]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#audience-size-and-multiple-sends-per-user).

## Puis-je commencer l'IP warming en cours de planification ? {#can-i-start-ip-warming-mid-schedule}

L'IP warming automatisé construit toujours la planification depuis le début de la montée en charge. Pour simuler un démarrage en cours de planification, définissez le **Current daily send volume** sur une valeur supérieure à 0 correspondant à votre volume actuel. Lorsque le volume actuel est supérieur à 0, Braze n'applique pas la mise à l'échelle par nombre d'IP au jour 1.

## Quel fuseau horaire est utilisé pour l'envoi ? {#what-time-zone-is-used-for-sending}

Les envois utilisent le fuseau horaire de l'espace de travail lorsqu'il est défini ; sinon, ils utilisent le fuseau horaire de l'entreprise. Les Campaigns ne sont pas créées dans le fuseau horaire local de chaque utilisateur. Pour envoyer en heure locale, mettez à jour manuellement les Campaigns créées par le plan.

## Combien de plans d'IP warming peuvent être exécutés en même temps ? {#how-many-ip-warming-plans-can-run-at-the-same-time}

Plusieurs plans peuvent être exécutés simultanément. Pour plus de détails, consultez [IP warming multiple]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming).

## Comment le volume évolue-t-il pour les pools d'IP avec plusieurs IP ? {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

Lorsque le **volume d'envoi quotidien actuel** est 0, le jour 1 commence au minimum entre 50 envois par IP et 500 au total. Le volume augmente ensuite d'environ 1,75 fois par jour d'envoi, sous réserve des garde-fous de montée en puissance. Par exemple, avec 10 IP : 500 → 875 → 1 532 → 2 681.

Si vous définissez un volume actuel personnalisé supérieur à 0, la mise à l'échelle par nombre d'IP ne s'applique pas au jour 1. Pour en savoir plus sur les plans multi-IP, consultez [Préchauffer plusieurs IP dans un même pool]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool).

## Le réchauffement IP automatisé prend-il en charge la limitation du débit par Campaign ? {#does-automated-ip-warming-support-rate-limiting-per-campaign}

Non. Chaque Campaign est envoyée à l'heure configurée sans limitation du débit par Campaign.

## Quand Braze retient-il le volume pendant l'IP warming ? {#when-does-braze-hold-volume-during-ip-warming}

Braze évalue la livrabilité des Campaigns envoyées entre 12 et 20 heures auparavant. Si les taux de livraison, d'ouverture, de rebond ou de signalement de courrier indésirable dépassent les seuils de référence indiqués dans [Pendant l'IP warming actif]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming), Braze retient le volume pour le jour d'envoi suivant au lieu de l'augmenter.

## Que se passe-t-il lorsque le volume est maintenu ? {#what-happens-when-volume-is-held}

Le maintien du volume est l'ajustement automatique que Braze applique lorsque ces seuils sont dépassés. L'envoi planifié suivant conserve le même volume au lieu de progresser. Braze réorganise les entrées de planification futures, archive les Campaigns futures existantes du plan et crée immédiatement de nouvelles Campaigns pour le calendrier mis à jour. Le plan peut nécessiter plus de temps pour atteindre le volume cible.

## Pourquoi les modifications de Campaign n'apparaissent-elles pas dans le suivi de l'IP warming ? {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

Les modifications que vous apportez aux Campaigns créées par l'IP warming automatisé (telles que la planification, le Segment ou le volume) ne sont pas resynchronisées avec le suivi de l'IP warming. Pour les notes de configuration associées, consultez l'[Étape 3 : Sélectionner les messages à envoyer]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Puis-je arrêter un plan d'IP warming ? {#can-i-stop-an-ip-warming-plan}

Oui. L'arrêt met définitivement fin au plan : Braze désactive les Campaigns associées et n'en crée pas de nouvelles. Il n'est pas possible de reprendre un plan arrêté — créez un nouveau plan pour continuer. Pour connaître les étapes à suivre après un arrêt, consultez la section [Arrêter un plan d'IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan).

## Quand un plan d'IP warming est-il marqué comme terminé ? {#when-is-an-ip-warming-plan-marked-as-complete}

Le plan est marqué comme terminé après la fin du dernier jour d'envoi planifié, à minuit dans le fuseau horaire effectif (espace de travail ou entreprise). Par exemple, si la dernière Campaign est envoyée à 20 h, le plan est marqué comme terminé à minuit, quatre heures plus tard.

## Quelles données puis-je télécharger ? {#what-data-can-i-download}

L'export CSV comprend des lignes par Campaign avec des indicateurs quotidiens : *Envoyés*, *Distribués*, *Rebonds*, *Signalements de courrier indésirable*, *Ouvertures totales*, *Ouvertures uniques*, *Cliqués* et *Désabonnés*. Le tableau de suivi agrège plusieurs Campaigns du même jour dans une vue quotidienne. Pour en savoir plus, consultez [Lorsqu'un IP warming est terminé]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes).