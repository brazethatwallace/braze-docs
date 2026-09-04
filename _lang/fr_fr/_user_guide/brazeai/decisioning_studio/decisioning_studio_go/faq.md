---
nav_title: FAQ
article_title: FAQ sur Decisioning Studio Go
page_order: 8
page_type: FAQ
description: "Cette page fournit des réponses aux questions fréquemment posées concernant Decisioning Studio Go."
---

# Questions fréquemment posées {#frequently-asked-questions}

## Général {#general}

### Qu'est-ce que Decisioning Studio Go ? {#what-is-decisioning-studio-go}

Decisioning Studio Go est un agent décisionnel basé sur l'IA, intégré au tableau de bord de Braze. Vous composez un menu d'options — variantes créatives, horaires d'envoi, jours de la semaine — et l'agent choisit la bonne combinaison pour chaque utilisateur, en optimisant les clics. Il offre une personnalisation individuelle sans nécessiter de data scientist ni d'intégration personnalisée. La première version prend en charge l'e-mail ; des canaux supplémentaires suivront dans des bêtas distinctes, chaque canal étant géré par son propre agent.

### En quoi est-ce différent du test A/B ? {#how-is-this-different-from-ab-testing}

Le test A/B identifie la variante qui fonctionne le mieux en moyenne sur l'ensemble d'une audience ou au sein d'un segment, puis déploie cette unique variante à tous les membres de ce groupe. Decisioning Studio Go choisit la meilleure variante pour chaque utilisateur, en fonction de ce avec quoi cet utilisateur a interagi auparavant. Différents utilisateurs peuvent recevoir différentes variantes lors du même envoi. Au lieu de déployer une seule variante gagnante à un groupe, Decisioning Studio Go personnalise le contenu au niveau individuel.

### En quoi est-ce différent de Decisioning Studio Pro ? {#how-is-this-different-from-decisioning-studio-pro}

Go est le niveau en libre-service. C'est le point de départ idéal pour les marketeurs qui souhaitent une personnalisation individuelle des e-mails sans un déploiement complexe. Il optimise les clics et fonctionne avec les options que vous configurez directement dans Braze.

Pro est le niveau avec accompagnement complet. Il optimise n'importe quel indicateur métier, se connecte à n'importe quelle source de données first-party, prend en charge plusieurs canaux et inclut un accompagnement dédié de l'équipe Braze AI Decisioning Services.

### Quel type d'IA est utilisé ? Est-ce de l'IA générative ? {#what-kind-of-ai-is-this-is-it-generative}

Non. L'agent qui décide quoi envoyer à chaque utilisateur est un agent décisionnel, pas un agent génératif. Il ne rédige pas de contenu à votre place. Vous fournissez les options, et l'agent apprend quelle option fonctionne le mieux pour chaque utilisateur.

Decisioning Studio Go repose sur l'apprentissage par renforcement. L'agent traite chaque envoi comme une opportunité d'apprentissage : il essaie des combinaisons des options que vous avez approuvées, observe si chaque utilisateur interagit, et met à jour sa compréhension de ce qui fonctionne pour qui. Au fil du temps, il devient de plus en plus précis pour associer chaque utilisateur à l'option de votre menu la plus susceptible de générer un clic.

## Audiences et groupes de contrôle {#audiences-and-control-groups}

### Quelle est la différence entre le groupe Decisioning Studio et le groupe de contrôle aléatoire ? {#whats-the-difference-between-the-decisioning-studio-group-and-the-random-control-group}

Le groupe Decisioning Studio reçoit du contenu e-mail optimisé par l'IA ; l'agent choisit la meilleure variante pour chaque utilisateur. Le groupe de contrôle aléatoire reçoit des combinaisons aléatoires des mêmes options, sans optimisation. Les deux groupes respectent les contraintes que vous avez configurées (par exemple, si vous avez indiqué de ne pas répéter une ligne d'objet dans les 15 jours, cette règle s'applique également au groupe de contrôle aléatoire). La comparaison des deux groupes vous donne une mesure claire du gain apporté par l'agent.

### Le groupe de contrôle aléatoire est-il un groupe d'exclusion d'utilisateurs qui ne reçoivent aucun e-mail ? {#is-the-random-control-a-holdout-group-of-users-who-receive-no-email}

Non. Les utilisateurs du groupe de contrôle aléatoire reçoivent toujours des e-mails. Ils reçoivent des combinaisons sélectionnées aléatoirement parmi les options que vous avez configurées, envoyées à des jours choisis aléatoirement dans votre planification. Cela vous permet de comparer « personnalisé par l'IA » à « le même contenu, envoyé aléatoirement » plutôt qu'à « aucun e-mail du tout ».

### Pourquoi le groupe de contrôle aléatoire est-il obligatoire ? {#why-is-the-random-control-required}

Pour deux raisons. Premièrement, il vous fournit une mesure continue et en temps réel de la performance de l'agent par rapport à une base aléatoire. Deuxièmement, l'agent utilise le comportement du groupe de contrôle aléatoire comme signal d'apprentissage. La taille minimale du groupe de contrôle aléatoire est de 5 % — c'est le seuil nécessaire pour que l'agent apprenne de manière fiable et que la mesure de performance soit significative.

### Puis-je utiliser un segment déjà utilisé dans un autre Canvas ou une autre campagne ? {#can-i-use-a-segment-thats-already-used-in-another-canvas-or-campaign}

Vous le pouvez, mais c'est fortement déconseillé et un avertissement s'affiche. Lorsque les mêmes utilisateurs reçoivent des messages de Decisioning Studio Go et d'autres Canvas ou campagnes en même temps, les autres messages affectent l'engagement d'une manière que l'agent ne peut pas prendre en compte. La configuration la plus propre est un segment dédié à l'agent.

## Configuration {#configuration}

### Que puis-je personnaliser ? {#what-can-i-personalize}

Au sein de chaque création de base, vous pouvez marquer la ligne d'objet, le CTA et une image comme points de personnalisation à l'aide d'étiquettes Liquid. L'agent choisit ensuite parmi les variantes que vous fournissez pour chaque composant, par utilisateur. Vous pouvez également avoir plusieurs créations de base ; l'agent choisit aussi quelle création de base utiliser.

### Puis-je utiliser des Content Blocks pour les composants personnalisés ? {#can-i-use-content-blocks-for-the-personalized-components}

Non. Les Content Blocks ne fonctionnent pas comme points de substitution de composants créatifs pour le moment. Placez votre ligne d'objet, votre CTA et votre image personnalisés directement dans le corps de l'e-mail plutôt que dans un bloc de contenu.

### Puis-je utiliser des modèles basés sur des images sans éléments cliquables ? {#can-i-use-image-based-templates-with-no-clickable-elements}

Les modèles basés sur des images sont pris en charge, mais ils limitent ce que l'agent peut optimiser. Si l'intégralité de l'e-mail est une seule image, l'agent peut toujours décider quelle image envoyer, mais il ne peut pas optimiser la ligne d'objet, le CTA ou la mise en page au sein de l'e-mail. Vous obtenez un meilleur gain avec des modèles HTML comportant plusieurs points de personnalisation.

### Puis-je modifier l'événement de conversion ? {#can-i-change-the-conversion-event}

Pour le niveau en libre-service, l'événement de conversion pris en charge est le clic. Dans Decisioning Studio Pro, vous pouvez optimiser n'importe quel indicateur métier personnalisé.

### Comment fonctionne la fréquence d'envoi ? {#how-does-send-frequency-work}

Vous sélectionnez une fréquence unique, par exemple trois envois par semaine. L'agent ne choisit pas entre différentes fréquences. Dans le cadre de cette fréquence, il choisit quels jours (parmi les jours que vous avez autorisés) et quels horaires (dans vos heures calmes, selon le fuseau horaire local de l'utilisateur) pour envoyer.

### Comment fonctionnent les limites de fréquence ? {#how-do-frequency-caps-work}

Lors de la configuration, vous pouvez appliquer les règles de limite de fréquence de votre espace de travail à l'agent et choisir si les envois de l'agent comptent dans la limite de fréquence globale de chaque utilisateur. Votre gestionnaire du succès des clients ou votre consultant en solutions peut vous aider à déterminer la bonne approche pour votre programme en fonction de la configuration des limites de fréquence dans votre espace de travail.

### L'agent peut-il envoyer sur plusieurs canaux ? {#can-the-agent-send-across-multiple-channels}

Chaque agent est monocanal, et le canal actuellement pris en charge est l'e-mail. Vous pouvez exécuter plusieurs agents en parallèle pour différents programmes, mais chaque agent gère un seul canal.

## Tests et lancement {#testing-and-launch}

### Comment tester avant de passer en production ? {#how-do-i-test-before-going-live}

Utilisez la fonctionnalité native d'envoi test dans le Braze Composer. Les envois test affichent des combinaisons de variantes spécifiques que vous sélectionnez — ils servent à vérifier l'e-mail lui-même, pas à prédire ce que l'agent enverrait réellement à un utilisateur réel. L'aperçu dynamique dans le compositeur vous permet également de voir comment différentes combinaisons de variantes s'affichent.

### Que se passe-t-il juste après le lancement ? {#what-happens-right-after-i-launch}

L'agent entre dans une période d'entraînement. Les e-mails sont envoyés dès le premier jour sans période d'attente, mais les performances peuvent fluctuer pendant que l'agent explore les combinaisons. Les rapports indiquent si l'agent est encore en phase d'entraînement ou s'il est passé en personnalisation active, afin que vous sachiez toujours à quelle étape il se trouve.

### Puis-je modifier l'agent après le lancement ? {#can-i-edit-the-agent-after-launch}

Oui. L'audience, la planification, les créations et les contraintes peuvent toutes être mises à jour après le lancement. Vous devez promouvoir les modifications avant qu'elles ne prennent effet.

### Que se passe-t-il si je mets à jour les options de contenu après le lancement ? {#what-if-i-update-content-options-after-launch}

Vous pouvez ajouter, supprimer ou modifier des variantes de la même manière que lors de la configuration initiale. Les modifications doivent être promues avant de prendre effet. L'ajout d'une nouvelle variante ne réinitialise pas l'entraînement de l'agent sur les variantes existantes.

## Rapports et résultats {#reporting-and-results}

### Les rapports de Decisioning Studio Go correspondent-ils à ce que je vois dans mes analyses e-mail ailleurs dans Braze ? {#does-decisioning-studio-go-reporting-match-what-i-see-in-my-email-analytics-elsewhere-in-braze}

Les chiffres peuvent différer. Decisioning Studio applique un filtrage des clics plus strict que les rapports e-mail standard, de sorte que les totaux peuvent être inférieurs. La comparaison relative entre le groupe Decisioning Studio et le groupe de contrôle aléatoire est cohérente au sein des rapports Decisioning Studio, car le filtrage des clics est appliqué de manière égale à chaque groupe.

### Quels indicateurs l'agent optimise-t-il ? {#what-metrics-does-the-agent-optimize-for}

Les clics uniques quotidiens par utilisateur. L'objectif de l'agent est de maximiser le nombre d'utilisateurs distincts qui cliquent, et non le volume brut de clics.

### Puis-je voir quelles combinaisons fonctionnent le mieux ? {#can-i-see-which-combinations-are-performing-best}

Oui. Les rapports incluent la distribution des éléments individuels — tels que les lignes d'objet, les CTA et les images — que l'agent envoie.

### Qui est responsable du contenu envoyé par l'agent ? {#whos-accountable-for-the-content-the-agent-sends}

Vous l'êtes. L'agent n'envoie que du contenu que vous avez ajouté en tant que variante. L'agent décide de la combinaison pour chaque utilisateur, mais chaque élément individuel provient des variantes que vous avez fournies.

## Assistance {#support}

### Où puis-je obtenir de l'aide pour mon agent ? {#where-do-i-get-help-with-my-agent}

Contactez votre gestionnaire du succès des clients Braze ou votre consultant en solutions pour obtenir de l'aide sur la configuration, l'analyse des performances ou la conception de votre programme.