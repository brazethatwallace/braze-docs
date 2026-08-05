---
nav_title: Groupe de contrôle global
article_title: Groupe de contrôle global
alias: /global_control_group/
page_order: 6
page_type: reference
description: "Découvrez comment configurer et utiliser le groupe de contrôle global pour mesurer l'impact global de vos efforts de communication au fil du temps."
tool:
  - Reports
search_rank: 1
toc_headers: h2

---

# Groupe de contrôle global {#global-control-group}

> Utilisez le groupe de contrôle global pour spécifier un pourcentage de tous les utilisateurs qui ne doivent recevoir aucune campagne ni aucun Canvas, ce qui vous permet d'analyser l'impact global de vos efforts de communication au fil du temps.

En comparant le comportement des utilisateurs qui reçoivent des messages avec ceux qui n'en reçoivent pas, vous pouvez mieux comprendre comment vos campagnes marketing et Canvas contribuent à une augmentation des sessions et des événements personnalisés.

## Fonctionnement du groupe de contrôle global {#how-the-global-control-group-works}

Avec le groupe de contrôle global, vous pouvez définir un pourcentage de l'ensemble de vos utilisateurs comme groupe de contrôle. Une fois enregistrés, les utilisateurs de ce groupe ne reçoivent aucune Campaign ni aucun Canvas.

{% alert important %}
Votre groupe de contrôle global s'applique à tous les canaux, toutes les Campaigns et tous les Canvas, à l'exception des [Campaigns API]({{site.baseurl}}/api/api_campaigns). Cela signifie que les utilisateurs de votre groupe de contrôle reçoivent toujours les Campaigns API. Toutefois, cette exception ne s'applique pas aux Content Cards. Si vous utilisez une Campaign de Content Cards déclenchée par API, les utilisateurs de votre groupe de contrôle ne les recevront pas.
{% endalert %}

### Assigner aléatoirement des utilisateurs au groupe de contrôle global {#assign-users-randomly-to-the-global-control-group}

Braze sélectionne aléatoirement plusieurs plages de [numéros de compartiment aléatoires]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers#create-segments-using-random-bucket-numbers) et inclut les utilisateurs de ces compartiments sélectionnés. Si vous utilisez actuellement des numéros de compartiment aléatoires à d'autres fins, consultez la section [Points de vigilance](#things-to-watch-for).

Lorsque votre groupe de contrôle global est généré, tous les utilisateurs dont les numéros de compartiment aléatoires correspondent font partie du groupe. De plus, les nouveaux utilisateurs qui rejoignent la plateforme après ce moment (ceux acquis après la génération du groupe de contrôle global) et qui possèdent ces numéros de compartiment aléatoires sont également ajoutés au groupe de contrôle global. De même, si de nombreux utilisateurs sont supprimés, vous pouvez vous attendre à ce que la taille de votre groupe de contrôle global diminue, car un pourcentage de ces utilisateurs supprimés faisait partie de ce groupe. Cela permet de maintenir la taille de votre groupe comme un pourcentage constant par rapport à l'ensemble de votre base d'utilisateurs.

### Assigner aléatoirement des utilisateurs au groupe de traitement pour le reporting {#assign-users-randomly-to-the-treatment-group-for-reporting}

Braze crée également un groupe de traitement pour le reporting sur l'uplift. Le groupe de traitement est un groupe d'utilisateurs sélectionnés aléatoirement qui ne font pas partie de votre groupe de contrôle global, et il est généré en utilisant la même méthode de numéros de compartiment aléatoires que le groupe de contrôle global.

Votre groupe de traitement est de taille similaire à votre groupe de contrôle global, mais il est peu probable qu'il soit exactement de la même taille. Pour le [reporting](#reporting), Braze mesure les comportements des utilisateurs de votre groupe de contrôle et des utilisateurs de votre échantillon de traitement. Chaque espace de travail dispose d'un maximum d'un groupe de contrôle global et d'un groupe d'échantillon de traitement. Le groupe d'échantillon de traitement est le même groupe d'utilisateurs, quelle que soit la configuration de votre reporting de contrôle global.

### Exclure des utilisateurs des feature flags {#exclude-users-from-feature-flags}

Vous ne pouvez pas activer les [feature flags]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) pour les utilisateurs de votre groupe de contrôle global. Cela signifie que les utilisateurs de votre groupe de contrôle global ne peuvent pas non plus participer à des expériences de feature flags.

### Exclure des utilisateurs du groupe de contrôle global {#exclude-users-from-the-global-control-group}

Vous ne pouvez pas retirer des utilisateurs spécifiques du groupe de contrôle global, mais vous pouvez ajouter des [paramètres d'exclusion](#step-3-assign-exclusion-settings) afin que les Campaigns et les Canvas portant des étiquettes spécifiques **n'utilisent pas** le groupe de contrôle global. Vous pouvez également désactiver puis réactiver votre groupe de contrôle global pour renouveler la composition du groupe. La durée idéale entre deux renouvellements varie en fonction du type de test que vous effectuez, mais essayez de ne pas renouveler plus d'une fois par mois.

## Créer un groupe de contrôle global {#create-a-global-control-group}

### Étape 1 : Accéder aux paramètres du groupe de contrôle global {#step-1-navigate-to-the-global-control-group-settings}

Depuis le tableau de bord, accédez à **Audience** > **Global Control Group**.

### Étape 2 : Attribuer un pourcentage de tous les utilisateurs à ce groupe de contrôle {#step-2-assign-a-percentage-of-all-users-to-this-control-group}

Saisissez un pourcentage pour votre groupe de contrôle et sélectionnez **Save**. Une fois la valeur saisie, Braze vous affiche une estimation du nombre d'utilisateurs qui font partie de votre groupe de contrôle global, du groupe de traitement et de l'échantillon de traitement. Gardez à l'esprit que plus vous avez d'utilisateurs dans votre espace de travail, plus cette estimation est précise.

Le nombre d'utilisateurs dans votre groupe de contrôle global est automatiquement mis à jour après sa configuration initiale afin de rester proportionnel à ce pourcentage lorsque de nouveaux utilisateurs sont ajoutés à votre espace de travail. De plus, les utilisateurs qui rejoignent l'espace de travail après la mise en place du groupe de contrôle global et qui possèdent des numéros de compartiment aléatoires sont également ajoutés au groupe de contrôle global. Si de nombreux utilisateurs sont ajoutés, la taille de votre groupe de contrôle global augmente pour maintenir un pourcentage constant par rapport à l'ensemble de votre base d'utilisateurs. Lorsque la taille de votre groupe de contrôle global augmente, les utilisateurs qui faisaient déjà partie du groupe y restent (sauf si vous apportez des modifications à votre groupe en le désactivant et en en créant un nouveau).

Pour des recommandations sur les pourcentages, consultez les [bonnes pratiques de test](#percentage-guidelines).

![Les paramètres du groupe de contrôle global avec les paramètres d'audience définis sur « Attribuer cinq pour cent de tous les utilisateurs au groupe de contrôle global ».]({% image_buster /assets/img/control_group/control_group4.png %})

### Étape 3 : Configurer les paramètres d'exclusion {#step-3-assign-exclusion-settings}

Utilisez des tags pour ajouter des paramètres d'exclusion à votre groupe de contrôle global. Les Campaigns ou Canvas qui utilisent les tags inclus dans les paramètres d'exclusion n'utilisent pas votre groupe de contrôle global. Ces Campaigns et Canvas continuent d'être envoyés à chaque utilisateur de l'audience cible, y compris ceux de votre groupe de contrôle global.

Notez que le menu déroulant des tags n'affiche que les tags actuellement appliqués à au moins une Campaign ou un Canvas actif. Si vous créez un nouveau tag et souhaitez l'utiliser dans les paramètres d'exclusion, appliquez-le d'abord à une Campaign ou un Canvas.

{% alert tip %}
Vous pouvez ajouter des paramètres d'exclusion si vous avez des messages transactionnels qui doivent être envoyés à chaque utilisateur.
{% endalert %}

![La section pour ajouter ou modifier les paramètres d'exclusion de votre groupe de contrôle global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Étape 4 : Enregistrer votre groupe de contrôle {#step-4-save-your-control-group}

À ce stade, Braze génère un groupe d'utilisateurs sélectionnés aléatoirement qui représente le pourcentage choisi de votre base totale d'utilisateurs. Une fois enregistré, toutes les Campaigns et Canvas actuellement actifs et futurs ne sont plus envoyés aux utilisateurs de ce groupe, à l'exception des Campaigns ou Canvas qui contiennent l'un des tags de vos paramètres d'exclusion.

## Apporter des modifications à votre groupe de contrôle global {#making-changes-to-your-global-control-group}

Vous ne pouvez apporter des modifications à votre groupe de contrôle global qu'en le désactivant et en en créant un nouveau. Par exemple, si vous avez configuré un groupe de contrôle global représentant 10 % de votre audience et que vous souhaitez réduire sa taille à 5 %, vous devez désactiver votre groupe de contrôle global actuel et en réactiver un nouveau.

Vous pouvez désactiver votre groupe de contrôle global à tout moment depuis l'onglet **Global Control Group Settings**, mais gardez à l'esprit que cela rend immédiatement les utilisateurs de ce groupe éligibles aux Campaigns et aux Canvas.

Avant de désactiver votre groupe de contrôle, [exportez](#export-group-members) un fichier CSV des utilisateurs de ce groupe au cas où vous auriez besoin de le consulter ultérieurement. Lorsque vous désactivez un groupe de contrôle, Braze ne peut en aucun cas restaurer le groupe ni identifier les utilisateurs qui en faisaient partie.

Après avoir désactivé votre groupe de contrôle, vous pouvez en enregistrer un nouveau. Lorsque vous saisissez un pourcentage et que vous l'enregistrez, Braze génère un nouveau groupe d'utilisateurs sélectionnés de manière aléatoire. Si vous saisissez le même pourcentage qu'auparavant, Braze génère un nouveau groupe d'utilisateurs pour vos groupes de contrôle et de traitement.

![Une boîte de dialogue intitulée « You are making changes to Global Messaging Settings » avec un texte avertissant qu'une fois votre groupe de contrôle global désactivé, il n'est plus exclu des Campaigns ou Canvas nouveaux ou actifs.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exporter les membres de votre groupe de contrôle {#export-group-members}

Si vous souhaitez voir quels utilisateurs font partie de votre groupe de contrôle global, vous pouvez exporter les membres de votre groupe par CSV ou API.

Pour effectuer une exportation CSV, accédez à l'onglet **Global Control Group Settings** et cliquez sur <i class="fas fa-download" aria-label="Télécharger"></i>&nbsp;**Export**. Pour exporter par API, utilisez l'[endpoint `/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group).

{% alert important %}
Les groupes de contrôle historiques ne sont pas conservés, vous ne pouvez donc exporter que les membres de votre groupe actuel. Assurez-vous d'exporter toutes les informations nécessaires avant de désactiver un groupe de contrôle.
{% endalert %}

## Vérifier si un utilisateur fait partie d'un groupe de contrôle global {#view-whether-a-user-is-in-a-global-control-group}

Vous pouvez vérifier l'appartenance au groupe de contrôle global en accédant à la section **Miscellaneous** dans l'onglet **Engagement** du profil d'un utilisateur individuel.

![Une section « Miscellaneous » indiquant que l'utilisateur a un numéro de compartiment aléatoire de 6356 et ne fait pas partie du groupe de contrôle global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Rapports {#reporting}

Le rapport du groupe de contrôle global vous permet de comparer votre groupe à un échantillon de traitement. Votre échantillon de traitement est une sélection aléatoire d'utilisateurs hors contrôle, comprenant approximativement le même nombre d'utilisateurs que votre groupe de contrôle, généré à l'aide de la méthode du numéro de compartiment aléatoire.

### Consulter un rapport {#viewing-a-report}

Pour consulter un rapport de votre groupe de contrôle global depuis le tableau de bord, accédez à **Analytics** > **Global Control Group Report**.

Ensuite, sélectionnez le paramètre avec lequel vous souhaitez exécuter votre rapport (sessions ou un événement personnalisé particulier) et sélectionnez **Run Report**.

![Sélectionnez le paramètre avec lequel vous souhaitez exécuter votre rapport (sessions ou un événement personnalisé particulier) et sélectionnez Run Report.]({% image_buster /assets/img/control_group/control_group6.png %})

### Configurer votre rapport {#configuring-your-report}

Lors de la génération de votre rapport, choisissez un événement — sessions ou tout événement personnalisé — à comparer entre vos groupes de traitement et de contrôle. Choisissez ensuite une période pour laquelle afficher les données. Gardez à l'esprit que si vous avez enregistré plusieurs expériences de groupe de contrôle à différentes périodes, vous devriez éviter d'inclure des données provenant de plus d'une expérience dans votre rapport.

Notez que les indicateurs en pourcentage de votre rapport sont arrondis. Par exemple, dans les cas où le nombre de conversions représente un très faible pourcentage de votre groupe de contrôle ou de traitement global, le taux de conversion peut être arrondi à 0 %.

Ce rapport affiche également un pourcentage de [confiance]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence) pour votre indicateur de variation par rapport au contrôle. Dans les cas où le taux de conversion entre votre groupe de contrôle et votre groupe de traitement est identique, une confiance de 0 % est attendue — cela indique qu'il y a 0 % de chance qu'il existe une différence de performance entre les deux groupes.

#### Tailles des groupes {#group-sizes}

Avant mai 2024, le groupe de contrôle global était exclu de l'archivage des utilisateurs, mais le groupe d'échantillon de traitement ne l'était pas. À partir de mai 2024, les deux groupes sont exclus de l'archivage des utilisateurs. Cela pourrait entraîner des tailles significativement différentes entre votre groupe d'échantillon de traitement et votre groupe de contrôle global. La prochaine fois que vous réinitialiserez votre groupe de contrôle global, cet écart se résoudra et vous verrez des tailles de groupes similaires.

{% alert note %}
Chaque espace de travail dispose d'un maximum d'un groupe de contrôle global et d'un groupe d'échantillon de traitement. Le groupe d'échantillon de traitement est le même groupe d'utilisateurs, quelle que soit la manière dont vous configurez vos rapports de contrôle global.
{% endalert %}

### Indicateurs du rapport {#report-metrics}

| Indicateur | Définition | Calcul |
| -- | -- | -- |
| Variation par rapport au contrôle | Calcule l'amélioration entre le taux de conversion de vos groupes de traitement et de contrôle. | ((Taux de conversion du traitement – taux de conversion du contrôle) ÷ taux de conversion du contrôle) \* 100 |
| Amélioration incrémentale | La différence du nombre total d'événements entre vos groupes de traitement et de contrôle. Cet indicateur cherche à répondre à la question : « Combien d'événements de conversion supplémentaires le groupe de traitement a-t-il générés ? ». | Total des événements pour le traitement – total des événements pour le contrôle |
| Pourcentage d'amélioration incrémentale | Le pourcentage du total des événements de votre traitement qui peut être attribué à votre traitement (par opposition au comportement naturel des utilisateurs). Calculé en divisant l'amélioration incrémentale (nombre) par le nombre total d'événements de votre groupe de traitement. | Amélioration incrémentale (nombre) ÷ Total des événements du groupe de traitement |
| Taux de conversion | Le pourcentage estimé d'utilisateurs de votre groupe de contrôle ou de traitement qui réalisent l'événement sélectionné pendant la période choisie. Calculé en additionnant le nombre d'événements de la période et en le divisant par la somme des utilisateurs du groupe chaque jour. Il ne peut s'agir que d'une approximation, car la taille du groupe fluctue régulièrement à mesure que de nouveaux utilisateurs rejoignent votre groupe de contrôle global, et les événements sont des événements totaux — et non uniques. Si le nombre de conversions est très faible et que vos groupes de contrôle ou de traitement sont très grands, le taux de conversion peut être arrondi à 0 %. Si le nombre d'événements est très élevé — par exemple, dans les cas où un utilisateur peut réaliser plus d'un événement par jour — le taux de conversion peut dépasser 100 %. | Somme du nombre d'événements pour ces utilisateurs sur cette période ÷ somme des utilisateurs du groupe chaque jour |
| Taille estimée du groupe | Le nombre estimé d'utilisateurs dans vos groupes de contrôle et de traitement pendant la période sélectionnée. | La taille maximale d'adhésion atteinte par vos groupes de contrôle et de traitement pendant la période choisie pour le rapport. |
| Nombre total d'événements | Le nombre total de fois où l'événement sélectionné s'est produit pendant la période choisie. Ce n'est pas un nombre unique (par exemple, si un utilisateur réalise un événement deux fois pendant la période, l'événement est comptabilisé deux fois). | Somme du nombre de fois où un événement s'est produit chaque jour pendant la période choisie. |
| Événements par utilisateur | Le nombre moyen estimé de fois où les utilisateurs de chaque groupe ont réalisé vos événements de conversion pendant la période sélectionnée. | Total des événements ÷ taille estimée du groupe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Indicateurs du rapport" }

## Résolution des problèmes {#troubleshooting}

Lors de la configuration de vos groupes de contrôle global et de la consultation des rapports, voici les erreurs que vous pourriez rencontrer :

| Problème | Résolution des problèmes |
| --- | --- |
| Impossible d'enregistrer le pourcentage saisi lors de la désignation d'un groupe de contrôle global. | Ce problème survient si vous saisissez un nombre non entier ou un entier qui n'est pas compris entre 1 et 15 (inclus). |
| Erreur « Braze is not able to update your Global Control Group » sur la page de configuration du groupe de contrôle global. | Cela indique généralement qu'un composant de cette page a changé, probablement en raison d'actions effectuées par un autre utilisateur de votre compte Braze. Dans ce cas, actualisez la page et réessayez. |
| Le rapport du groupe de contrôle global ne contient aucune donnée. | Si vous accédez au rapport du groupe de contrôle global sans avoir enregistré de groupe de contrôle global, vous ne verrez aucune donnée dans le rapport. Créez et enregistrez un groupe de contrôle global, puis réessayez. |
| Mon taux de conversion est de 0 % ou le graphique ne s'affiche pas, même si le nombre d'événements est supérieur à zéro. | Si le nombre de conversions est très faible et que vos groupes de contrôle ou de traitement sont très importants, le taux de conversion peut être arrondi à 0 % et ne pas apparaître dans le graphique. Vous pouvez le vérifier en consultant l'indicateur du nombre total d'événements. Vous pouvez comparer l'efficacité de vos deux groupes en utilisant l'indicateur de pourcentage d'augmentation incrémentale. |
| Mon taux de conversion (ou d'autres indicateurs) varie considérablement en fonction de la période pour laquelle je consulte les données. | Si vous consultez les données sur de courtes périodes, il est possible que vos indicateurs fluctuent d'un jour à l'autre ou d'une semaine à l'autre. Consultez les indicateurs sur une période d'au moins un mois. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

### Points d'attention {#things-to-watch-for}

#### Chevauchement des numéros de compartiment aléatoires {#overlapping-random-bucket-numbers}

Votre groupe de contrôle global est formé à l'aide de numéros de compartiment aléatoires. Par conséquent, si vous exécutez d'autres tests utilisant des filtres de Segment basés sur les numéros de compartiment aléatoires, gardez à l'esprit qu'il pourrait y avoir un chevauchement entre les Segments que vous créez et les utilisateurs de votre groupe de contrôle global.

#### Adresses e-mail en double {#duplicate-email-addresses}

Si deux utilisateurs avec des ID utilisateur externes différents ont la même adresse e-mail, et que l'un d'entre eux fait partie du groupe de contrôle tandis que l'autre non, un e-mail sera tout de même envoyé à cette adresse e-mail lorsque l'utilisateur hors du groupe de contrôle est éligible à un e-mail. Dans ce cas, les deux profils utilisateur sont marqués comme ayant reçu la Campaign ou le Canvas contenant cet e-mail.

#### Groupe de contrôle global et groupes de contrôle spécifiques aux messages {#global-control-group-and-message-specific-control-groups}

Il est possible d'avoir à la fois un groupe de contrôle global et d'utiliser un groupe de contrôle spécifique à une Campaign ou à un Canvas. Disposer d'un groupe de contrôle spécifique à une Campaign ou à un Canvas vous permet de mesurer l'impact d'un message particulier.

Les utilisateurs de votre groupe de contrôle global ne reçoivent aucun message, à l'exception de ceux comportant des exceptions d'étiquettes. Si vous ajoutez un contrôle à une Campaign ou un Canvas, Braze exclut une partie de votre groupe de traitement global de la réception de cette Campaign ou de ce Canvas en particulier. Cela signifie que si un membre du groupe de contrôle global n'est pas éligible à une Campaign ou un Canvas donné, il ne sera pas présent dans le groupe de contrôle de cette Campaign ou de ce Canvas.

{% alert note %}
En résumé, les utilisateurs du groupe de contrôle global sont filtrés hors de l'audience de la Campaign ou du Canvas avant l'entrée. Parmi les utilisateurs qui entrent dans la Campaign ou le Canvas, un pourcentage d'entre eux est ensuite assigné à la variante de contrôle.
{% endalert %}

#### Segments du groupe de contrôle global dans la console de développement {#global-control-group-segments-on-the-developer-console}

Vous pouvez voir plusieurs Segments **Contrôle global** dans la section **Identifiants API supplémentaires** de la page [Clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Cela s'explique par le fait qu'à chaque activation ou désactivation du groupe de contrôle global, un nouveau groupe de contrôle global est formé. Cela entraîne la création de plusieurs Segments intitulés « Groupe de contrôle global ».

Un seul de ces Segments est actif et peut être interrogé à l'aide de l'[endpoint `/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group), ou exporté depuis le tableau de bord. L'exportation depuis le tableau de bord indique spécifiquement quels sous-segments composent ce groupe de contrôle global.

## Bonnes pratiques de test {#testing-best-practices}

### Taille optimale du groupe de contrôle {#percentage-guidelines}

Deux règles principales à garder à l'esprit :
1. Votre groupe de contrôle ne doit pas compter moins de 1 000 utilisateurs.
2. Votre groupe de contrôle ne doit pas représenter plus de 10 % de votre audience totale.

Si votre audience totale est inférieure à 10 000, vous devez augmenter votre pourcentage pour créer un groupe de plus de 1 000 utilisateurs ; dans ce cas, vous ne devez pas dépasser 15 %. Gardez à l'esprit que plus la taille globale de votre espace de travail est petite, plus il est difficile de mener un test statistiquement rigoureux.

- Parmi les compromis à prendre en compte lorsque vous réfléchissez à la taille de votre groupe de contrôle, il faut un nombre suffisamment important de clients dans votre groupe de contrôle pour que toute analyse comportementale produite soit fiable. Cependant, plus votre groupe de contrôle est grand, moins de clients reçoivent vos Campaigns, ce qui est un inconvénient si vous utilisez vos Campaigns pour stimuler l'engagement et les conversions.
- Le pourcentage idéal de votre audience totale dépend de la taille de celle-ci. Plus votre audience totale est grande, plus votre pourcentage peut être faible. Si votre audience est petite, en revanche, vous avez besoin d'un pourcentage plus élevé pour votre groupe de contrôle.

### Durée de l'expérience {#experiment-duration}

#### Choisir une durée idéale {#reshuffle}

La durée pendant laquelle vous devez mener votre expérience avant de renouveler la composition du groupe de contrôle dépend de ce que vous testez et des comportements de référence de vos utilisateurs. Si vous n'êtes pas sûr, un bon point de départ est un trimestre (trois mois), mais vous ne devez pas descendre en dessous d'un mois.

Pour déterminer la durée appropriée de votre expérience, réfléchissez aux questions auxquelles vous souhaitez répondre. Par exemple, cherchez-vous à savoir s'il y a une différence dans les sessions ? Si c'est le cas, pensez à la fréquence à laquelle vos utilisateurs ont des sessions de manière organique. Les marques dont les utilisateurs ont des sessions quotidiennes peuvent mener des expériences plus courtes que celles dont les utilisateurs n'ont des sessions que quelques fois par mois.

Ou bien, vous pourriez vous intéresser à un événement personnalisé, auquel cas votre expérience devra peut-être durer plus longtemps qu'une expérience portant sur les sessions, s'il est probable que vos utilisateurs déclenchent cet événement personnalisé moins fréquemment.

{% alert tip %}
Plus vous maintenez le même groupe de contrôle à l'écart longtemps, plus il diverge du groupe de traitement, ce qui peut introduire un biais. Réinitialiser le groupe de contrôle global rééquilibre la population.
{% endalert %}

#### Essayez de ne pas mettre fin aux expériences prématurément {#try-to-limit-ending-experiments-prematurely}

Décidez de la durée de votre expérience avant de la commencer, puis ne mettez fin à votre expérience et ne recueillez les résultats finaux qu'une fois ce point prédéterminé atteint. Mettre fin à votre expérience prématurément, ou dès que vous observez des données prometteuses, introduit un biais.

#### Réfléchissez aux indicateurs pertinents {#think-about-valuable-metrics}

Prenez en compte les comportements de référence pour les indicateurs qui vous intéressent le plus. Vous intéressez-vous aux taux d'achat pour des abonnements renouvelés uniquement sur une base annuelle ? Ou vos clients ont-ils une habitude hebdomadaire pour l'événement que vous souhaitez mesurer ? Réfléchissez au temps qu'il faut aux utilisateurs pour potentiellement modifier leurs comportements en réponse à vos communications. Une fois que vous avez décidé de la durée de votre expérience, veillez à ne pas y mettre fin ou à enregistrer les résultats finaux prématurément, sous peine de biaiser vos conclusions.