---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Cet article de référence présente le partenariat entre Braze et Iterate, qui vous permet d'enrichir les données des clients en utilisant des enquêtes pour ajouter des informations supplémentaires."
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com) fournit des outils d'enquête et de feedback pour vous aider à apprendre de vos clients, en offrant des expériences de recherche conviviales qui correspondent à votre marque.

_Cette intégration est maintenue par Iterate._

## À propos de l'intégration {#about-the-integration}

L'intégration d'Iterate avec Braze vous permet de proposer des enquêtes Iterate de façon fluide au sein de votre produit ou de vos campagnes. Les réponses à l'enquête peuvent être enregistrées en tant qu'attributs personnalisés de l'utilisateur dans Braze, ce qui vous permet de créer une image complète de vos utilisateurs ou de créer de nouvelles audiences et de nouveaux segments puissants.

Avec le SDK de Braze installé dans votre application ou votre site web, vous pouvez utiliser les outils de segmentation et de ciblage disponibles dans Braze pour envoyer des enquêtes via des messages in-app à une partie spécifique de votre audience en fonction de n'importe quel déclencheur ou segment personnalisé. Les enquêtes Iterate peuvent également être intégrées directement dans vos campagnes d'e-mail ou incluses en tant que liens dans vos campagnes push ou autres types de campagnes.

## Conditions préalables {#prerequisites}

| Exigence | Origine |
|---|---|
| Compte Iterate | Un [compte Iterate](https://iteratehq.com) est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track`. Pour envoyer des enquêtes via les messages in-app de Braze, vous aurez également besoin de l'autorisation `kpi.mau.data_series`.<br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

Avec Iterate, vous pouvez collecter presque tous les types de données. Cela va des informations personnelles (nom, âge, e-mail) aux données de performance (Net Promoter Score, satisfaction des clients, classement par étoiles), en passant par les préférences (appareil préféré, fréquence de communication préférée) ou la personnalité (livre préféré, plutôt chien ou chat). Ce que vous demandez dépend entièrement de vous, ainsi que le type de données que vous souhaitez collecter ou les audiences que vous souhaitez créer.

## Intégration {#integration}

### Pour commencer : connecter Braze à Iterate {#getting-started-connect-braze-with-iterate}

Connectez-vous à votre compte Iterate et ajoutez votre endpoint REST de Braze et votre clé API REST sur la page **Company Settings**.

### Envoyer des enquêtes sous forme de message in-app {#deliver-surveys-as-an-in-app-message}

#### Étape 1 : Créez votre enquête {#step-1-create-your-survey}

Avant de créer votre enquête, activez le bouton **Enable in-app message surveys** dans vos paramètres Iterate.

Ensuite, créez une nouvelle enquête dans Iterate et ajoutez des questions pertinentes. Le cas échéant, vous pouvez également inclure un message d'invite qui s'affichera avant l'enquête. Sélectionnez **Send via Braze In-App Message** comme type d'enquête.

Une fois votre enquête terminée, dans l'onglet **Publish**, copiez l'extrait de code sous **Copy and paste your embed code**.

#### Étape 2 : Partagez votre enquête {#step-2-share-your-survey}

Dans Braze, créez une nouvelle campagne de messages in-app, sélectionnez **Custom Code** comme type de message, et collez votre extrait de code dans le message. Ensuite, sélectionnez **Wait for User to Dismiss** comme comportement du message au clic.

Continuez à configurer votre campagne comme vous le feriez pour n'importe quelle autre campagne de messages in-app, en choisissant une méthode de distribution et en ciblant une audience.

### Envoyer des enquêtes par e-mail ou push {#deliver-surveys-through-email-or-push}

#### Étape 1 : Créez votre enquête

Créez une nouvelle enquête par e-mail ou par lien dans Iterate et ajoutez des questions d'enquête pertinentes. Une fois que les questions ont été rédigées et que vous avez personnalisé le design, sélectionnez **Send survey > Integrations > Braze**.

Vous verrez alors les options de configuration pour envoyer des réponses à Braze. Activez l'intégration pour permettre l'envoi des réponses de cette enquête dans Braze.

#### Étape 2 : Partagez votre enquête

Votre enquête peut être partagée de deux manières : en intégrant la première question dans votre message ou en incluant un lien direct vers l'enquête sur la plateforme Iterate.

![Options de liens Iterate]({% image_buster /assets/img/iterate.png %})

- **Intégrer le code**
  - Copiez l'extrait de code sous **Email embed code** dans la section d'intégration de Braze de l'onglet **Send survey**. Insérez le code dans le HTML de votre e-mail Braze à l'endroit où vous souhaitez que le début de l'enquête apparaisse.
  - Si vous avez des difficultés à afficher les questions de l'enquête ou si elles ne sont pas correctement formatées, vous devez aller dans l'onglet **Sending Info** du compositeur de messages et décocher l'option **Inline CSS**.
- **Inclure un lien**
  - Copiez le lien sous **Survey Link** dans la section d'intégration de Braze de l'onglet **Send survey**. Notez que la balise Liquid figurant dans le lien {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} sera automatiquement remplacée pour chaque utilisateur lors de l'envoi.

### Prochaines étapes : créer des campagnes de suivi {#next-steps-build-follow-up-campaigns}

Au fur et à mesure que les utilisateurs répondent, des données en temps réel alimenteront leurs profils. Ces données peuvent être utilisées pour segmenter les utilisateurs et envoyer des campagnes de suivi personnalisées. Par exemple, si vous avez posé la question « Appréciez-vous nos produits ? », vous pouvez créer des segments d'utilisateurs ayant l'attribut utilisateur personnalisé `Do you enjoy our products?` qui ont répondu « Oui » ou « Non » et cibler ces utilisateurs.

## Événements personnalisés de Braze {#braze-custom-events}

Lorsqu'un utilisateur répond à une question de l'enquête, Iterate déclenche un événement personnalisé dans Braze nommé `survey-question-response`. Les événements personnalisés vous permettent de déclencher le nombre et le type de campagnes de suivi que vous souhaitez.

## Personnaliser les noms des attributs utilisateur {#customize-user-attribute-names}

Par défaut, l'attribut utilisateur créé pour une question est le même que l'intitulé de la question.
Dans certains cas, vous souhaiterez peut-être le personnaliser. Pour ce faire, cliquez sur le menu déroulant **Customize user attribute names** dans l'étape **Create your Survey** et saisissez les noms personnalisés de votre choix.