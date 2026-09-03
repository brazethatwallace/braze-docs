---
nav_title: Lexer
article_title: Lexer
description: "Cet article de référence présente le partenariat entre Braze et Lexer, une plateforme de données client qui met les données client entre les mains des marketeurs pour inspirer des expériences qui stimulent les ventes."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer](https://lexer.io/), une plateforme de données client créée pour le retail, aide les marques à générer des ventes incrémentales grâce à des expériences client améliorées en combinant un enrichissement robuste des données avec les outils les plus intuitifs et le conseil d'experts.

_Cette intégration est maintenue par Lexer._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Lexer vous permet de synchroniser les données entre les deux plateformes. Utilisez vos données Lexer pour créer de précieux segments Braze ou importez vos segments existants dans Lexer pour obtenir des informations.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte partenaire | Un compte Lexer est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec toutes les autorisations `user` (à l'exception de `user.delete`) et les autorisations `segment.list`. Le jeu d'autorisations peut changer au fur et à mesure que Lexer ajoute la prise en charge de nouveaux objets Braze, de sorte que vous pouvez soit accorder davantage d'autorisations dès maintenant, soit prévoir de les mettre à jour ultérieurement.<br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | Votre [URL d'endpoint REST]({{site.baseurl}}/api/basics#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Compartiment Amazon AWS S3 et identifiants | Avant de commencer l'intégration, vous devez disposer des identifiants d'accès à un compartiment AWS S3 connecté à votre hub Lexer (il peut s'agir d'un compartiment que vous créez ou d'un compartiment que Lexer crée et gère pour vous). Consultez [Lexer](https://learn.lexer.io/docs/amazon-s3) pour obtenir des conseils sur cette exigence. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Dans Lexer, accédez à **Manage > Integration**, sélectionnez la tuile **Braze** et cliquez sur **Integrate Braze**. Fournissez les informations suivantes :
- **Braze REST endpoint**
- **Braze REST API key**
- **AWS Credentials**
  - **AWS S3 bucket name**
  - **AWS S3 [bucket region](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)**
  - **AWS S3 bucket path** : ce chemin doit correspondre à celui que vous avez spécifié lors de la [connexion de votre compartiment S3 à Braze]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3). Ce champ doit être vide si vous n'avez rien spécifié à Braze.
  - **AWS S3 secret access key** : consultez Amazon pour obtenir des informations sur la [création d'une clé d'accès](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/).
- **Braze export segment ID** : l'ID du segment que vous avez créé dans Braze et qui contient tous les utilisateurs que vous souhaitez exporter vers Lexer. S'il y a des utilisateurs que vous ne voulez pas exporter vers Lexer, vous pouvez les exclure du segment que vous avez créé dans Braze. Pour trouver votre identifiant de segment, cliquez sur le segment de votre choix dans Braze et localisez le **Segment API Identifier**.

![Écran de gestion des intégrations Lexer affichant les champs d'intégration Braze pour l'URL de l'API, la clé API, les détails du compartiment AWS S3 et l'ID du segment d'exportation Braze.]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### Choix d'une option AWS S3 (gérée par Lexer ou autogérée) {#choosing-an-aws-s3-option-lexer-managed-or-self-managed}
L'utilisation d'un compartiment géré par Lexer est le moyen privilégié de connecter Braze à votre hub Lexer et réduit le nombre de configurations nécessaires. Lexer vous fournit les détails ponctuels dont vous avez besoin pour configurer Braze.

Si vous avez déjà connecté un compartiment S3 à Braze et que vous l'utilisez à d'autres fins, vous devrez à la place fournir à Lexer un accès à ce compartiment autogéré en suivant les étapes précédentes.

Cette intégration fonctionne en fournissant à Lexer votre jeton API et vos secrets existants, permettant ainsi à Lexer d'effectuer ces exportations en votre nom. Elle importe également vos données Braze dans Lexer en utilisant ces identifiants et votre configuration S3 pour synchroniser automatiquement vos données sur les deux plateformes.

## Envoi de segments à Braze {#sending-segments-to-braze}

### Étape 1 : Créer une activation {#step-1-create-activation}

Lexer Activate mettra automatiquement à jour vos profils Braze, en ajoutant ou en supprimant des attributs au fur et à mesure que les clients entrent et sortent de votre segment.

1. Dans Lexer, dans **Lexer Activations**, cliquez sur **ACTIVATE NEW AUDIENCE**.
2. Sélectionnez l'activation Braze appropriée pour cette campagne.
3. Ajoutez votre segment.
4. Mettez à jour le nom de votre audience ; il deviendra votre valeur d'attribut dans Braze.
5. Il s'agit de l'attribut personnalisé que nous allons mettre à jour dans Braze. Contactez le [service d'assistance de Lexer](mailto:support@lexer.io) pour le mettre à jour.
6. Cochez l'action de liste appropriée — dans la plupart des cas, vous voudrez maintenir votre liste.
7. Passez en revue les conditions générales et cliquez sur **SEND AUDIENCE**.

![Flux de travail Lexer Activate montrant la sélection du canal d'activation, la création de l'audience et les détails de l'activation avant l'envoi d'une audience à Braze.]({% image_buster /assets/img/lexer/lexer.png %})

### Étape 2 : Vérifier l'activation {#step-2-verify-activation}

Une fois que l'envoi de votre activation a été confirmé dans Activate, les enregistrements commenceront à se mettre à jour dans Braze. Vos profils ne seront entièrement mis à jour dans Braze qu'après réception d'un e-mail de confirmation de Lexer.

### Étape 3 : Créer votre segment Braze {#step-3-create-your-braze-segment}

Dans Braze, vous verrez que le nom de votre audience dans Lexer est maintenant une valeur dans votre attribut personnalisé `lexer_audience`. Braze a une limite de 100 valeurs par attribut.

Pour créer votre segment, accédez à **Segment > + Create Segment** et sélectionnez **Custom Attribute** comme filtre. Ensuite, sélectionnez `lexer_audience` comme attribut et le nom de l'audience Lexer souhaitée. Une fois terminé, **enregistrez** votre audience.

Vous pouvez désormais ajouter ce segment nouvellement créé aux futures Campaigns et Canvas Braze pour cibler ces utilisateurs finaux.