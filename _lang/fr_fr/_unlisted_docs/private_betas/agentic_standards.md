---
nav_title: Standards agentiques
article_title: Standards agentiques
permalink: /campaign_qa_agent/
description: "Cet article de référence couvre les standards agentiques, y compris le fonctionnement des standards de Campaign et les bonnes pratiques."
hidden: true
---

# Standards agentiques {#agentic-standards}

> Les standards agentiques sont des règles et des ensembles de règles destinés à appliquer les politiques d'entreprise et les garde-fous sur les Campaigns dans Braze. Ils sont suivis par Operator pendant le processus de création et de modification. Ces standards peuvent être évalués de manière agentique avant le lancement d'une Campaign pour servir de dernier rempart de validation par rapport aux directives de marque, aux conventions organisationnelles et aux exigences techniques avant le lancement.

Les standards agentiques réduisent la supervision manuelle afin que chaque message envoyé par Braze soit précis, conforme et prêt à être lancé.

{% alert important %}
Les standards agentiques pour l'Agent Console sont actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cette bêta.
{% endalert %}

## Fonctionnement {#how-it-works}

Lorsque vous créez un standard de Campaign, vous définissez des règles spécifiques, regroupées en « ensembles de règles », qu'Operator suit et évalue avant le lancement d'une Campaign. Vous pouvez choisir parmi des ensembles de règles prédéfinis couvrant les besoins marketing courants ou créer des règles personnalisées propres à votre équipe.

Une fois configuré, vous pouvez tester le standard de Campaign dans le volet **Aperçu de l'évaluation** en le confrontant à n'importe quelle Campaign existante dans votre espace de travail. L'évaluation agentique fournit un rapport détaillé avec des catégories de résultats.

## Créer un standard de Campaign {#create-a-campaign-standard}

### Étape 1 : Choisir le type de standard {#step-1-choose-the-standard-type}

Pour créer votre standard, accédez à **Agent Console** > **Agentic Standards**. Sélectionnez **Create Agentic Standard** et choisissez **Campaign Standards** dans le menu déroulant.

### Étape 2 : Configurer les détails {#step-2-set-up-details}

Ensuite, configurez les détails de votre standard :

1. Saisissez un nom et une description pour aider votre équipe à en comprendre l'objectif.
2. (Facultatif) Ajoutez des tags pour filtrer votre standard.
3. Choisissez le modèle d'évaluation que votre standard utilisera. Celui-ci alimente l'évaluation agentique du standard.

![Un standard de Campaign « Abandoned Cart Campaign Standards » qui définit les règles et les ensembles de règles pour les Campaigns de panier abandonné dans Braze.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### Étape 3 : Configurer les règles de Campaign {#step-3-configure-campaign-rules}

À l'étape **Campaign Rules**, définissez les règles qui doivent être appliquées dans le cadre de ce standard. Vous pouvez ajouter jusqu'à 10 ensembles de règles par standard et jusqu'à 20 règles par ensemble de règles.

Sélectionnez **Add ruleset** pour afficher la liste des catégories suivantes :

- **Configuration de Campaign :** Valide les conventions de nommage, les tags et le suivi des conversions.
- **Audience et ciblage :** Vérifie les Segments, les exclusions et la taille de l'audience.
- **Contenu et rédaction :** Définit les exigences en matière de qualité du texte, de limites de caractères et de complétude du message.
- **Liens et suivi :** Vérifie les URL, les CTA, les deep links et les paramètres UTM.
- **Personnalisation et contenu dynamique :** Définit les vérifications de la logique Liquid et des valeurs de repli.
- **Conformité et livrabilité :** Définit les exigences relatives aux obligations juridiques et aux garde-fous d'envoi.
- **Règles personnalisées :** Sélectionnez **Create custom ruleset** pour définir des exigences uniques qui ne rentrent pas clairement dans les catégories préconfigurées.

Si vous ne savez pas comment formuler une règle, sélectionnez **Generate with Operator** pour qu'Operator vous aide à rédiger une logique spécifique basée sur vos besoins.

![Quatre règles configurées pour la catégorie Audience et ciblage.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### Étape 4 : Tester votre standard {#step-4-test-your-standard}

Avant d'utiliser votre standard pour des Campaigns dans Braze, utilisez le volet **Aperçu de l'évaluation** pour simuler une évaluation agentique.

1. Choisissez une Campaign existante dans le menu déroulant pour l'utiliser comme cas de test.
2. Choisissez de tester tous les ensembles de règles ou un ensemble spécifique.
3. Sélectionnez le bouton **Simulate response**.

Ensuite, examinez les résultats. L'évaluation s'exécute sur la Campaign et affiche les résultats dans les catégories suivantes :

- **Pass :** Ces règles ont été respectées avec succès. Par exemple, l'évaluation peut confirmer que vos conventions de nommage correspondent aux modèles attendus.
- **Warning :** Il s'agit de problèmes non critiques qui peuvent nécessiter une attention particulière. Par exemple, si vous testez un ensemble de règles pour les e-mails sur une Campaign webhook, l'évaluation agentique peut émettre un avertissement indiquant que les noms d'expéditeur ne s'appliquent pas.
- **Fail :** Il s'agit de problèmes critiques qui doivent être corrigés avant le lancement. Par exemple, des dates planifiées dans le passé ou des tags organisationnels obligatoires manquants.

## Utiliser les standards agentiques {#use-agentic-standards}

Après avoir configuré un standard de Campaign, vous pouvez l'utiliser pour évaluer n'importe quelle Campaign lors du processus de révision finale. Cela confirme que votre Campaign respecte toutes les exigences avant d'être envoyée à vos utilisateurs.

### Exécuter une évaluation {#run-an-evaluation}

Pour exécuter une évaluation automatisée, accédez à l'étape **Review Summary** de votre workflow de création de Campaign.

1. Accédez à la section **Agentic Standards** et sélectionnez le standard souhaité dans le menu déroulant.
2. Sélectionnez **Run evaluation**.

Si vous apportez des modifications à votre Campaign après avoir exécuté une première évaluation, sélectionnez **Re-run evaluation** pour actualiser les résultats.

### Examiner les résultats de l'évaluation {#review-evaluation-results}

Une fois l'évaluation terminée, un résumé affiche les résultats dans les catégories suivantes : **Pass**, **Fail** et **Warning**.

L'onglet **Fail** liste les règles qui n'ont pas été respectées. Pour chaque échec, le standard fournit :

- **Rule :** Le critère spécifique vérifié, comme « Spelling & Grammar Check ».
- **Reason :** Une explication de la raison pour laquelle la vérification a échoué. Par exemple, l'évaluation pourrait identifier que « personalized » a été utilisé à la place de l'orthographe en anglais australien « personalised ».

L'onglet **Pass** liste toutes les règles que votre Campaign a respectées avec succès. Cela confirme que des vérifications comme **Offensive Language Detection** ou **Naming Convention Validation** ont été validées.

L'onglet **Warning** liste les problèmes non critiques qui peuvent nécessiter une attention particulière. Par exemple, si vous testez un ensemble de règles pour les e-mails sur une Campaign webhook, l'évaluation du standard peut générer un avertissement indiquant que les noms d'expéditeur ne s'appliquent pas.

### Résoudre ou ignorer les problèmes {#resolve-or-ignore-issues}

Pour chaque échec ou avertissement identifié, vous pouvez décider de la marche à suivre avant le lancement. Sélectionnez **Resolve** à côté d'un problème, puis choisissez parmi les options suivantes :

- **Mark as fixed :** Sélectionnez cette option après avoir mis à jour la configuration ou le contenu de votre Campaign en fonction de la suggestion de l'évaluation.
- **Ignore this issue :** Sélectionnez cette option pour passer outre le problème pour cette exécution uniquement. Cela est utile pour les écarts intentionnels ou les cas particuliers où la suggestion de l'évaluation peut ne pas s'appliquer.
- **Ask BrazeAI Operator :** Sélectionnez cette option pour corriger le problème à l'aide d'Operator.

Une fois que tous les problèmes critiques ont été résolus ou ignorés, vous pouvez procéder au lancement de votre Campaign.

## Bonnes pratiques {#best-practices}

- **Commencez par les modèles :** Utilisez d'abord les ensembles de règles prédéfinis pour la configuration de Campaign et les liens et le suivi, car ils couvrent les erreurs manuelles les plus courantes et fournissent à l'évaluation agentique le bon contexte.
- **Soyez précis :** Lorsque vous rédigez des règles personnalisées, fournissez des exemples clairs de ce à quoi le résultat « correct » ressemble. Par exemple, au lieu d'écrire « Vérifier la convention de nommage », essayez « Le nom de la Campaign commence par l'année en cours (par exemple, 2026_) ».
- **Itérez souvent :** À mesure que vos directives de marque ou vos processus internes évoluent, mettez à jour les ensembles de règles de votre standard de Campaign pour que vos vérifications automatisées restent pertinentes.