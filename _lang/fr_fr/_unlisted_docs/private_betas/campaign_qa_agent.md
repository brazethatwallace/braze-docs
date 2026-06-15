---
nav_title: Agent QA de Campaign
article_title: Agent QA de Campaign
permalink: /campaign_qa_agent/
description: "Cet article de référence couvre les agents QA de Campaign, y compris leur fonctionnement et les bonnes pratiques."
hidden: true
---

# Agent QA de Campaign {#campaign-qa-agent}

> Les agents QA de Campaign sont des assistants alimentés par l'IA qui exécutent des vérifications automatisées sur la configuration de votre Campaign. Ces agents agissent comme un dernier garde-fou, validant votre configuration par rapport aux directives de marque, aux conventions organisationnelles et aux exigences techniques avant le lancement.

En utilisant les agents QA de Campaign, vous pouvez réduire la supervision manuelle et vous assurer que chaque message envoyé depuis la plateforme Braze est précis, conforme et prêt à être lancé.

{% alert important %}
Les agents QA de Campaign pour la Console des agents sont actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cette bêta.
{% endalert %}

## Fonctionnement {#how-it-works}

Lorsque vous créez un agent QA de Campaign, vous définissez des règles spécifiques, regroupées en « ensembles de règles », que l'agent utilise pour évaluer une Campaign. Vous pouvez choisir parmi des ensembles de règles prédéfinis couvrant les besoins marketing courants ou créer des règles personnalisées spécifiques à votre équipe.

Une fois configuré, vous pouvez tester l'agent dans le volet de prévisualisation sur n'importe quelle Campaign existante dans votre espace de travail. L'agent fournit un rapport détaillé, classant ses résultats en Réussi, Avertissement ou Échec.

## Créer un agent QA de Campaign {#create-a-campaign-qa-agent}

### Étape 1 : Choisir le type d'agent {#step-1-choose-the-agent-type}

Pour créer votre agent, accédez à **Console des agents** > **Gestion des agents**. Sélectionnez **Créer un agent** et choisissez **Campaign QA** dans le menu déroulant.

### Étape 2 : Configurer les détails {#step-2-set-up-details}

Ensuite, configurez les détails de votre agent :

1. Saisissez un nom et une description pour aider votre équipe à comprendre son objectif.
2. (facultatif) Ajoutez des étiquettes pour filtrer votre agent.
3. Choisissez le modèle que votre agent utilisera. Celui-ci alimente le raisonnement de l'agent.

![Un agent QA de Campaign « Campaign QA for copy » qui vérifiera la qualité du message de la Campaign, en utilisant le modèle Braze Auto.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### Étape 3 : Configurer les instructions et les règles {#step-3-configure-instructions-and-rules}

Dans l'onglet **Instructions**, définissez les règles que l'agent vérifie. Vous pouvez ajouter jusqu'à 10 ensembles de règles par agent et jusqu'à 20 règles par ensemble de règles.

1. Sélectionnez **Ajouter un ensemble de règles** pour voir une liste des catégories suivantes :

- **Configuration de Campaign :** Valide les conventions de nommage, les étiquettes et le suivi des conversions.
- **Audience et ciblage :** Vérifie les segments, les exclusions et la taille de l'audience.
- **Contenu et texte :** Évalue la qualité du texte, les limites de caractères et la complétude du message.
- **Liens et suivi :** Vérifie les URL, les CTA, les liens profonds et les paramètres UTM.
- **Personnalisation et contenu dynamique :** Vérifie la logique Liquid et les valeurs de repli.
- **Conformité et livrabilité :** S'assure que les exigences légales et les mesures de protection d'envoi sont respectées.
- **Générer avec Operator :** Si vous ne savez pas comment formuler une règle, sélectionnez Générer avec Operator pour que notre assistant IA vous aide à rédiger une logique spécifique basée sur vos exigences.
- **Règles personnalisées :** Sélectionnez Créer un ensemble de règles personnalisé pour définir des vérifications uniques qui ne correspondent pas clairement aux catégories préconfigurées.

![Six règles configurées pour la catégorie Contenu et texte.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### Étape 4 : Tester votre agent {#step-4-test-your-agent}

Avant de déployer votre agent, utilisez le volet **Prévisualisation** pour simuler une réponse et confirmer que la logique fonctionne comme prévu.

1. Choisissez une Campaign existante dans le menu déroulant pour l'utiliser comme cas de test.
2. Choisissez de tester tous les ensembles de règles ou un ensemble spécifique.
3. Sélectionnez le bouton **Simuler la réponse**.

Ensuite, examinez les résultats. L'agent évalue la Campaign et affiche les résultats dans les catégories suivantes :

- **Réussi :** Ces règles ont été respectées avec succès. Par exemple, l'agent peut confirmer que vos conventions de nommage correspondent aux modèles attendus.
- **Avertissement :** Ce sont des problèmes non critiques qui peuvent nécessiter une attention particulière. Par exemple, si vous testez un ensemble de règles d'e-mail sur une Campaign webhook, l'agent peut émettre un avertissement indiquant que les noms d'expéditeur ne s'appliquent pas.
- **Échec :** Ce sont des problèmes critiques qui doivent être corrigés avant le lancement. Par exemple, des dates planifiées dans le passé ou des étiquettes organisationnelles requises manquantes.

## Utiliser les agents QA de Campaign {#use-campaign-qa-agents}

Après avoir configuré un agent QA de Campaign, vous pouvez l'utiliser pour auditer n'importe quelle Campaign lors du processus de vérification finale. Cela garantit que votre Campaign répond à toutes les exigences avant d'être envoyée à vos utilisateurs.

### Exécuter un audit {#run-an-audit}

Pour exécuter une vérification automatisée, accédez à l'étape **Résumé de la vérification** de votre flux de création de Campaign.

1. Accédez à la section **Agent QA** et sélectionnez l'agent souhaité dans le menu déroulant.
3. Sélectionnez **Exécuter l'agent QA**.

Si vous apportez des modifications à votre Campaign après avoir exécuté une vérification initiale, vous pouvez sélectionner **Réexécuter l'agent QA** pour actualiser les résultats.

### Examiner les résultats de l'audit {#review-audit-results}

Une fois l'évaluation terminée, l'agent fournit un résumé de ses résultats classés dans ces onglets : **Réussi**, **Échec** et **Avertissement**.

L'onglet **Échec** liste les règles qui n'ont pas été respectées. Pour chaque échec, l'agent fournit :

- **Règle :** Les critères spécifiques vérifiés, comme « Vérification de l'orthographe et de la grammaire ».
- **Raisonnement :** Une explication détaillée de la raison de l'échec de la vérification. Par exemple, l'agent peut identifier que « personalized » a été utilisé au lieu de l'orthographe en anglais australien « personalised ».
- **Corrections directes :** Des modifications spécifiques de texte ou de configuration suggérées par l'agent pour corriger le problème.

L'onglet **Réussi** liste toutes les règles que votre Campaign a respectées avec succès. Cela confirme que des vérifications comme la **détection de langage offensant** ou la **validation des conventions de nommage** ont été validées.

L'onglet **Avertissement** liste les problèmes non critiques qui peuvent nécessiter une attention particulière. Par exemple, si vous testez un ensemble de règles d'e-mail sur une Campaign webhook, l'agent peut émettre un avertissement indiquant que les noms d'expéditeur ne s'appliquent pas.

### Résoudre ou ignorer les problèmes {#resolve-or-ignore-issues}

Pour chaque échec ou avertissement identifié, vous pouvez décider de la marche à suivre avant le lancement. Sélectionnez **Résoudre** à côté d'un problème, puis choisissez parmi les options suivantes :

- **J'ai corrigé le problème :** Sélectionnez cette option après avoir mis à jour la configuration ou le texte de votre Campaign en fonction des retours de l'agent.
- **Ignorer ce problème :** Sélectionnez cette option pour faire une exception à la règle. Cela est utile pour les déviations intentionnelles ou les cas particuliers où la suggestion de l'agent peut ne pas s'appliquer.

Une fois tous les problèmes critiques résolus ou ignorés, vous pouvez procéder au lancement de votre Campaign.

## Bonnes pratiques {#best-practices}

- **Commencez par les modèles :** Utilisez d'abord les ensembles de règles prédéfinis pour la configuration de Campaign et les liens et le suivi, car ils couvrent les erreurs manuelles les plus courantes et garantissent que l'agent dispose du bon contexte pour effectuer ses vérifications.
- **Soyez précis :** Lorsque vous rédigez des règles personnalisées, fournissez des exemples clairs de ce à quoi le résultat « correct » ressemble. Par exemple, au lieu d'écrire « Vérifier la convention de nommage », essayez « S'assurer que le nom de la Campaign commence par l'année en cours (par exemple, 2026_) ».
- **Itérez souvent :** À mesure que vos directives de marque ou vos processus internes évoluent, mettez à jour les ensembles de règles de votre agent QA de Campaign pour que vos vérifications automatisées restent pertinentes.