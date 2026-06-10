---
nav_title: Worthy
article_title: Worthy
description: "Cet article de référence présente le partenariat entre Braze et Worthy, une plateforme de personnalisation des messages qui vous permet de créer des expériences in-app riches et personnalisées et de les diffuser via Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> L'intégration de [Worthy](https://worthy.ai/) et Braze vous permet de créer des expériences in-app personnalisées et riches à l'aide de l'éditeur glisser-déposer de Worthy, puis de les diffuser via Braze. De plus, Worthy effectue automatiquement les opérations suivantes :

_Cette intégration est maintenue par Worthy._

## À propos de l'intégration {#about-the-integration}

- Créer un serveur de contenu connecté et une API sécurisée pour votre envoi de messages.
- Construire vos messages in-app avec des analyses et un suivi des clics qui apparaîtront directement dans Braze.
- Exporter automatiquement du HTML via l'éditeur glisser-déposer de Worthy pour l'utiliser dans des campaigns de messages in-app en **Custom Code** dans Braze, avec les connexions API requises et le contenu dynamique que vous configurez.

## Cas d'utilisation {#use-cases}

- Expériences d'accueil personnalisées basées sur les sélections d'onboarding des utilisateurs
- Expériences in-app pour les événements spéciaux et les promotions
- Recueil des commentaires et des évaluations des clients en fonction du comportement sur l'application
- Test rapide d'idées de produits potentiels pour l'application
- Notifications enrichies, actualités et mises à jour de la communauté

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte [Worthy](https://worthy.ai/) | Un compte Worthy est nécessaire pour bénéficier de ce partenariat. |
| SDK Braze | Vous devrez configurer le SDK Braze dans votre application mobile pour envoyer des messages in-app enrichis. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer un message personnalisé dans Worthy {#step-1-create-personalized-messaging-in-worthy}

Accédez à votre application dans le tableau de bord Worthy, sélectionnez le **Message Creator** et créez un message personnalisé que vous souhaitez utiliser pour engager vos utilisateurs.

### Étape 2 : Créer une campaign Braze {#step-2-create-a-braze-campaign}

Créez une [campaign de messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) dans Braze et définissez le **Type de message** sur **Custom Code**.

### Étape 3 : Copier votre message personnalisé dans Braze {#step-3-copy-your-personalized-message-into-braze}

Dans le créateur de messages Worthy, cliquez sur **Exporter** et sélectionnez **Braze** pour exporter votre message personnalisé afin de l'utiliser dans des campaigns Braze. Copiez le contenu exporté dans la zone de texte HTML sous **HTML + Asset Zip** dans l'éditeur de campaign Braze.

C'est tout ! Vous pouvez immédiatement tester votre message personnalisé à l'aide de l'onglet **Test** dans l'éditeur de campaign Braze.