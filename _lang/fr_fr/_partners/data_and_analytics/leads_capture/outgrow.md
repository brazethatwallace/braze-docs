---
nav_title: Outgrow
article_title: Outgrow
alias: /partners/outgrow/
description: "Cet article fournit un guide complet sur la configuration d'une intégration native entre Outgrow et Braze pour une meilleure synchronisation des données utilisateur et des campagnes personnalisées."
page_type: partner
search_tag: Partner
---

# Outgrow

> [Outgrow](https://outgrow.co/) est une plateforme de contenu interactif qui vous permet de créer des quiz, des calculatrices, des enquêtes et d'autres types de contenu attrayant pour recueillir des données et des informations sur les utilisateurs. L'intégration de Braze et Outgrow vous permet de transférer automatiquement les données utilisateur d'Outgrow vers Braze, ce qui permet de réaliser des campagnes hautement personnalisées et ciblées.

Lorsque vous utilisez l'intégration de Braze et Outgrow pour du contenu interactif, vous bénéficiez notamment des avantages suivants :

- **Personnalisation accrue** : collectez des données à partir des quiz, des enquêtes et des calculatrices Outgrow qui peuvent être mappées à des attributs personnalisés dans Braze. Ces données permettent une segmentation précise et des campagnes personnalisées.
- **Synchronisation des données en temps réel** : recevez les données d'Outgrow dans Braze en temps réel, ce qui vous permet d'agir immédiatement sur les informations des utilisateurs. Cela permet d'effectuer des suivis en temps voulu ou d'envoyer des messages personnalisés en fonction des interactions les plus récentes des utilisateurs.
- **Gestion rationalisée des données** : automatisez le transfert de données entre Outgrow et Braze, en éliminant les exportations et importations manuelles de données, en réduisant les divergences de données et en gagnant du temps.
- **Amélioration de l'expérience utilisateur** : exploitez les informations sur les utilisateurs pour créer des expériences plus pertinentes, ce qui se traduit par une plus grande satisfaction, une meilleure fidélisation et une plus grande valeur vie client.
- **Ciblage et segmentation flexibles** : affinez la segmentation dans Braze à l'aide des données d'Outgrow, ce qui vous permet de cibler les utilisateurs en fonction d'interactions spécifiques (telles que les scores de quiz ou les réponses aux enquêtes) afin de créer des campagnes qui trouvent un écho auprès de vos utilisateurs.

## Conditions préalables {#prerequisites}

Avant de configurer l'intégration d'Outgrow et de Braze, confirmez que vous disposez des éléments suivants :

| Condition | Description |
|-------------|-------------|
| **Compte Outgrow** | Un compte Outgrow enregistré pour configurer et gérer le contenu interactif et les paramètres de transfert de données |
| **Compte Braze** | Un compte Braze avec accès aux identifiants de la REST API |
| **Clé API** | Une clé API de Braze avec l'autorisation `users.track` pour permettre le transfert des données utilisateur |
| **Attributs personnalisés dans Braze** | Des attributs personnalisés configurés dans Braze pour capturer les réponses d'Outgrow (tels que les scores de quiz, les segments et autres) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Suivez ces étapes pour configurer l'intégration de Braze et Outgrow :

### Étape 1 : Générer la clé API de Braze {#step-1-generate-braze-api-key}

1. Dans votre compte Braze, accédez à **Console de développement** > **Paramètres API**.
2. Sélectionnez **Créer une nouvelle clé API**.
3. Donnez un nom à votre clé API, activez l'autorisation `users.track` et enregistrez la clé API.

### Étape 2 : Configurer l'intégration de Braze dans Outgrow {#step-2-configure-the-braze-integration-in-outgrow}

1. Connectez-vous à votre compte Outgrow.
2. Dans le tableau de bord, accédez à **Integrations**.
3. Dans la liste des intégrations disponibles, sélectionnez **Braze**.
4. Saisissez votre **clé API Braze** et l'**URL de l'endpoint REST API** :
   - **Clé API** : saisissez la clé API qui a été générée dans Braze.
   - **URL de l'endpoint REST** : saisissez l'endpoint de votre instance Braze (par exemple, `https://rest.iad-01.braze.com`).
5. Sélectionnez **Save** pour activer l'intégration.

### Étape 3 : Mapper les données Outgrow sur les attributs Braze {#step-3-map-outgrow-data-to-braze-attributes}

Dans Outgrow, vous pouvez mapper les réponses du contenu interactif (comme les résultats de quiz, les segments personnalisés ou les scores d'engagement) aux attributs personnalisés de Braze.

1. Dans les **paramètres d'intégration** d'Outgrow pour Braze, définissez les réponses Outgrow à mapper aux attributs de Braze.
2. Assurez-vous que chaque réponse sélectionnée correspond à un attribut personnalisé dans Braze. Par exemple :
   - Le score du quiz est mappé sur `outgrow_quiz_score`.
   - Le segment personnalisé est mappé sur `outgrow_custom_segment`.
3. Enregistrez vos paramètres de mappage.

### Étape 4 : Tester l'intégration {#step-4-test-the-integration}

Après avoir configuré l'intégration, effectuez un test pour confirmer que les données sont correctement transférées d'Outgrow vers Braze.

1. Publiez une expérience Outgrow (comme un quiz ou une calculatrice) et complétez-la en tant qu'utilisateur test.
2. Dans votre compte Braze, accédez à la section **Profil utilisateur** et vérifiez si les attributs ont été mis à jour (tels que `outgrow_quiz_score` ou `outgrow_custom_segment`).
3. Vérifiez que les données sont correctement renseignées sous les attributs personnalisés appropriés.

## Utilisation des données Outgrow dans Braze pour la segmentation et le ciblage {#using-outgrow-data-in-braze-for-segmentation-and-targeting}

### Création de segments dans Braze avec des données Outgrow {#creating-segments-in-braze-with-outgrow-data}

Grâce à cette intégration, vous pouvez créer des segments Braze basés sur des attributs personnalisés renseignés à partir des réponses Outgrow.

1. Dans Braze, accédez à **Engagement** > **Segments** et sélectionnez **Create New Segment**.
2. Nommez votre segment et définissez des filtres basés sur les données Outgrow. Par exemple :
   - Filtrez par `outgrow_quiz_score` pour cibler les utilisateurs dont le score est supérieur à un certain seuil.
   - Filtrez par `outgrow_custom_segment` pour cibler les utilisateurs qui appartiennent à un segment particulier défini par Outgrow.
3. Enregistrez votre segment pour l'utiliser dans des Campaigns et des Canvas.

### Lancer des Campaigns avec des segments définis par Outgrow {#launching-campaigns-with-outgrow-defined-segments}

Vous pouvez utiliser les segments personnalisés créés à partir des données d'Outgrow pour personnaliser vos Campaigns Braze et cibler les utilisateurs en fonction de leurs réponses au contenu interactif. Pour ce faire et créer une expérience utilisateur plus personnalisée, suivez les étapes suivantes :

1. Dans Braze, accédez à **Engagement** > **Campaigns**.
2. Sélectionnez **Create Campaign** et choisissez votre type de campagne (e-mail, push, message in-app ou autres).
3. Dans l'étape de ciblage de l'audience, sélectionnez le segment créé à partir des attributs Outgrow (tels que les utilisateurs ayant des scores de quiz ou des segments spécifiques).
4. Personnalisez le contenu et les paramètres de votre campagne, puis lancez-la.

## Résolution des problèmes courants {#troubleshooting-common-issues}

| Problème | Solution |
|-------|----------|
| **Les données ne sont pas transférées vers Braze** | Vérifiez que la clé API et l'URL de l'endpoint sont correctes dans vos paramètres d'intégration Outgrow. Assurez-vous que la clé API dispose de l'autorisation `users.track` activée. |
| **Mappage incorrect des données** | Assurez-vous que chaque réponse Outgrow mappée correspond à un attribut personnalisé Braze valide et que les noms des attributs correspondent exactement. |
| **Le segment ne filtre pas correctement** | Assurez-vous que les attributs personnalisés dans Braze sont correctement configurés et reçoivent des données. Revérifiez la logique de votre filtre de segment. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes courants" }

## Considérations supplémentaires {#additional-considerations}

- **Confidentialité des données** : respectez les réglementations relatives à la confidentialité des données (telles que le RGPD et le CCPA) lors du transfert des données utilisateur entre les plateformes.
- **Limites de débit** : les données Outgrow sont envoyées à Braze en temps réel, mais des limites de débit de l'API Braze peuvent s'appliquer pour les gros volumes de données. Planifiez en conséquence les expériences à fort trafic.
- **Configuration des attributs personnalisés** : vérifiez que les attributs personnalisés de Braze utilisés dans cette intégration sont correctement configurés pour capturer les données envoyées par Outgrow.

Pour plus d'assistance, reportez-vous à la [documentation Outgrow](https://support.outgrow.co/docs/configuring-native-integration-between-outgrow-braze) ou contactez l'assistance Outgrow.