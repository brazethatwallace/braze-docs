---
nav_title: Sendbird
article_title: Sendbird
description: "Cet article de référence présente le partenariat entre Braze et Sendbird, une solution de messagerie in-app de premier plan qui permet aux utilisateurs de recevoir des notifications in-app sur la plateforme Sendbird."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird](https://sendbird.com/) Notifications offre aux marketeurs et aux gestionnaires de produits un nouveau canal puissant pour communiquer avec leurs clients in-app avec des messages persistants et interactifs à sens unique. Ces messages peuvent être utilisés pour toute communication et sont le plus souvent utilisés à des fins promotionnelles et transactionnelles.

_Cette intégration est maintenue par Sendbird._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Sendbird permet aux utilisateurs de l'entreprise de :
{% multi_lang_include partners/instant_chat/sendbird_integration_bullets.md %}

En exploitant les capacités combinées de Braze et de Sendbird Notifications, les entreprises peuvent renforcer l'engagement client et générer des taux de conversion plus élevés grâce à des stratégies efficaces de notifications in-app.

## Prérequis {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Sendbird | Un compte Sendbird est nécessaire pour bénéficier de ce partenariat. |
| Sendbird UIKit | Le Sendbird UIKit doit être installé dans votre application [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) ou [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit). |
| Clé API REST Braze | Une clé API REST Braze avec les permissions `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Votre endpoint dépendra de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Cas d'usage {#use-cases}

![Diagramme résumant les cas d'usage de l'intégration Braze et Sendbird Notifications pour la communication marketing et transactionnelle.]({% image_buster /assets/img/sendbird/use-cases.png %})

L'intégration de Braze et Sendbird Notifications offre une gamme de cas d'usage pour renforcer l'engagement client et offrir une expérience utilisateur exceptionnelle :

- **Marketing** : Améliorez les Campaigns ciblées avec des promotions personnalisées et des recommandations adaptées aux préférences des utilisateurs, comme des réductions exclusives basées sur l'historique de navigation ou les achats précédents.
- **Transactionnel** : Optimisez la communication client grâce à des mises à jour en temps réel sur les commandes, les livraisons, la facturation et les paiements, y compris des notifications concernant le statut de la commande, les détails d'expédition et les délais de livraison estimés.

## Intégration {#integration}

### Étape 1 : Créer un modèle de notification {#step-1-create-a-notification-template}

Les [modèles Sendbird](https://sendbird.com/docs/notifications/v1/templates) vous permettent d'envoyer des notifications in-app personnalisées en créant et en utilisant plusieurs modèles pour chaque canal. Les modèles peuvent être créés et personnalisés depuis le tableau de bord Sendbird sans écrire de code.

![Éditeur de modèles du tableau de bord Sendbird pour créer des modèles de notification.]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### Étape 2 : Configurer l'intégration Braze sur le tableau de bord Sendbird {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

Depuis le **tableau de bord Sendbird**, sélectionnez votre application, accédez à **Notifications > Integrations**, puis cliquez sur **Add** dans la section **Braze**. Vous aurez besoin de votre clé API REST Braze et de votre endpoint REST Braze.

Une fois tous les champs renseignés, cliquez sur **Save** pour finaliser l'intégration et accéder aux endpoints d'intégration et au jeton API.

### Étape 3 : Installer Sendbird Notification Builder {#step-3-install-sendbird-notification-builder}

Ensuite, vous devez installer [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji). Cette extension Google Chrome vous permet d'envoyer des notifications personnalisées via Sendbird depuis le tableau de bord de Braze.

![Panneau de l'extension Chrome Sendbird Notification Builder dans le tableau de bord de Braze.]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Ajouter les identifiants Sendbird à l'extension {#add-sendbird-credentials-to-the-extension}

Une fois l'extension installée, cliquez sur l'icône Sendbird dans la barre d'outils de votre navigateur et sélectionnez **Settings**. Renseignez ici votre identifiant d'application et votre jeton API disponibles dans le **Sendbird Notification Builder**.

### Étape 4 : Associer l'identifiant utilisateur Sendbird à l'identifiant utilisateur Braze {#step-4-map-sendbird-user-id-to-braze-user-id}

Un identifiant utilisateur Sendbird doit être ajouté à un profil utilisateur Braze en tant qu'[attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) pour que l'intégration puisse être utilisée. Vous pouvez charger et mettre à jour les profils utilisateur via des fichiers CSV depuis la page [Importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv). Vous pouvez également utiliser l'identifiant utilisateur Braze comme identifiant utilisateur Sendbird.

### Étape 5 : Configurer votre modèle de webhook {#step-5-set-up-your-webhook-template}

Dans Braze, depuis **Modèles et médias**, accédez à **Modèles de webhook** et choisissez le **modèle de webhook Sendbird**. Notez que ce modèle ne sera disponible que si vous avez installé l'extension Sendbird Notification Builder.

{% raw %}
1. Indiquez un nom de modèle et ajoutez des Teams et des tags si nécessaire.
2. Copiez un endpoint temps réel ou par lot depuis le tableau de bord Sendbird dans l'**URL du webhook**.
3. Dans le champ **Receiver**, cliquez sur l'icône <i class="fas fa-plus" aria-label="Ajouter"></i> et insérez l'attribut utilisateur associé à l'identifiant utilisateur Sendbird.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` si vous utilisez un attribut personnalisé `sendbird_id` comme identifiant utilisateur Sendbird.
    - `{{ '{{' }}${user_id}}}` si vous utilisez l'identifiant utilisateur Braze comme identifiant utilisateur Sendbird.
4. Dans l'onglet **Settings**, remplacez `SENDBIRD_API_TOKEN` par le jeton API de notifications du tableau de bord Sendbird.
5. Enregistrez le modèle.
{% endraw %}

## Utilisation de cette intégration {#using-this-integration}

### Campaigns

1. Dans le tableau de bord de Braze, sur la page **Campaigns**, cliquez sur **Create Campaign** > **Webhook**.
2. Sélectionnez le modèle de webhook que vous avez créé dans cette section. Il est fortement recommandé d'utiliser l'endpoint Batch pour les Campaigns.
3. Personnalisez le modèle en modifiant ses variables dans l'onglet **Compose**.

### Canvas

1. À partir d'un Canvas nouveau ou existant, ajoutez un composant **Message**.
2. Ouvrez le composant et sélectionnez **Webhook** dans les **Messaging Channels**.
3. Sélectionnez le modèle de webhook que vous avez créé dans cette section. Il est fortement recommandé d'utiliser l'endpoint en temps réel pour les Canvas.
4. Personnalisez le modèle en modifiant ses variables dans l'onglet **Compose**.

## Personnalisation {#customization}

### Suivre le statut de distribution et d'ouverture {#track-delivery-and-open-status}

Pour intégrer l'événement de statut de distribution et d'ouverture des notifications avec la métrique de conversion d'une campagne, ajoutez un événement personnalisé sur le tableau de bord de Braze.

1. Depuis le tableau de bord de Braze, accédez à **Paramètres > Gérer les paramètres > Événements personnalisés**, puis cliquez sur **+ Ajouter un événement personnalisé**.
2. Après avoir créé un événement personnalisé, cliquez sur **Gérer les propriétés**, ajoutez une propriété nommée « status » et choisissez « String » comme type de propriété.
3. Lorsque vous composez une notification dans des Campaigns ou des Canvas, saisissez le nom de l'événement personnalisé dans le champ **Event Name**.

Cet événement personnalisé sera déclenché deux fois pour chaque notification : lorsqu'un message est envoyé et lorsqu'un utilisateur ouvre le message.
- Lorsqu'un message est envoyé, un événement personnalisé est déclenché avec le statut `SENT`.
- Lorsqu'un message est lu, un événement personnalisé est déclenché avec le statut `READ`.