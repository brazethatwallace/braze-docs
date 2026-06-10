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

L'intégration de Braze et de Sendbird permet aux utilisateurs de l'entreprise de :
* Utiliser les fonctionnalités de segmentation et de déclenchement de Braze pour lancer des notifications personnalisées in-app.
* Créer des notifications in-app personnalisées sur la plateforme Sendbird Notifications, qui sont ensuite diffusées dans l'environnement de l'application, améliorant ainsi l'engagement des utilisateurs.

En exploitant les capacités conjointes de Braze et de Sendbird Notifications, les entreprises peuvent renforcer l'engagement client et obtenir des taux de conversion plus élevés grâce à des stratégies de notification in-app efficaces.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Sendbird | Un compte Sendbird est nécessaire pour profiter de ce partenariat. |
| Sendbird UIKit | Vous devez avoir installé le Sendbird UIKit dans votre application [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) ou [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit). |
| Clé REST API de Braze | Une clé REST API de Braze avec les autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

![]({% image_buster /assets/img/sendbird/use-cases.png %})

L'intégration de Braze et de Sendbird Notifications offre un éventail de cas d'utilisation pour stimuler l'engagement client et offrir une expérience utilisateur exceptionnelle :

- **Marketing** : Améliorez les campagnes ciblées avec des promotions et des recommandations personnalisées adaptées aux préférences des utilisateurs, telles que des réductions exclusives basées sur l'historique de navigation ou les achats passés.
- **Transactionnel** : Améliorez la communication avec vos clients grâce à des mises à jour en temps réel sur les commandes, les livraisons, la facturation et les paiements, y compris des notifications concernant le statut de la commande, les détails de l'expédition et les délais de livraison estimés.

## Intégration {#integration}

### Étape 1 : Créer un modèle de notification {#step-1-create-a-notification-template}

Les [modèles Sendbird](https://sendbird.com/docs/notifications/v1/templates) vous permettent d'envoyer des notifications in-app personnalisées en créant et en utilisant plusieurs modèles pour chaque canal. Les modèles peuvent être créés et personnalisés sur le tableau de bord de Sendbird sans avoir à écrire de code.

![]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### Étape 2 : Configurer l'intégration Braze dans le tableau de bord de Sendbird {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

Depuis le **tableau de bord de Sendbird**, sélectionnez votre application, naviguez vers **Notifications > Integrations**, et cliquez sur **Add** sous la section **Braze**. Vous aurez besoin de votre clé REST API de Braze et de votre endpoint REST de Braze.

Une fois que vous avez renseigné tous les champs, cliquez sur **Save** pour terminer l'intégration et accéder aux endpoints d'intégration et au jeton API.

### Étape 3 : Installer le Sendbird Notification Builder {#step-3-install-sendbird-notification-builder}

Ensuite, vous devez installer le [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji). Cette extension Google Chrome vous permet d'envoyer des notifications personnalisées via Sendbird sur le tableau de bord de Braze.

![]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Ajouter les identifiants Sendbird à l'extension {#add-sendbird-credentials-to-the-extension}

Une fois l'extension installée, cliquez sur l'icône Sendbird dans la barre d'outils de votre navigateur et sélectionnez **Settings**. Renseignez votre ID d'application et votre jeton API disponibles dans le **Sendbird Notification Builder**.

### Étape 4 : Mapper l'ID utilisateur Sendbird à l'ID utilisateur Braze {#step-4-map-sendbird-user-id-to-braze-user-id}

Un ID utilisateur Sendbird doit être ajouté au profil utilisateur Braze en tant qu'[attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) pour que l'intégration puisse être utilisée. Vous pouvez télécharger et mettre à jour les profils utilisateurs via des fichiers CSV à partir de la page [Importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv). Vous pouvez également utiliser l'ID utilisateur Braze comme ID utilisateur Sendbird.

### Étape 5 : Configurer votre modèle de webhook {#step-5-set-up-your-webhook-template}

Dans Braze, à partir de **Modèles et médias**, accédez à **Modèles de webhook** et choisissez le **Sendbird Webhook Template**. Notez que ce modèle ne sera disponible que si vous avez installé l'extension Sendbird Notification Builder.

{% raw %}
1. Donnez un nom au modèle et ajoutez des équipes et des étiquettes si nécessaire.
2. Copiez un endpoint en temps réel ou par lot depuis le tableau de bord de Sendbird dans le champ **Webhook URL**.
3. Dans le champ **Receiver**, cliquez sur l'icône <i class="fas fa-plus"></i> et insérez l'attribut utilisateur mappé à l'ID utilisateur Sendbird.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` si vous utilisez un attribut personnalisé `sendbird_id` comme ID utilisateur Sendbird.
    - `{{ '{{' }}${user_id}}}` si vous utilisez l'ID utilisateur Braze comme ID utilisateur Sendbird.
4. Dans l'onglet **Settings**, remplacez `SENDBIRD_API_TOKEN` par le jeton de l'API de notifications provenant du tableau de bord de Sendbird.
5. Enregistrez le modèle.
{% endraw %}

## Utilisation de cette intégration {#using-this-integration}

### Campaigns

1. Dans le tableau de bord de Braze, sur la page **Campaigns**, cliquez sur **Créer une campagne** > **Webhook**.
2. Sélectionnez le modèle de webhook que vous avez créé ci-dessus. Il est fortement recommandé d'utiliser l'endpoint Batch pour les Campaigns.
3. Personnalisez le modèle en modifiant ses variables dans l'onglet **Rédiger**.

### Canvas

1. À partir d'un Canvas nouveau ou existant, ajoutez un composant **Message**.
2. Ouvrez le composant et sélectionnez **Webhook** dans les **Canaux de communication**.
3. Sélectionnez le modèle de webhook que vous avez créé ci-dessus. Il est fortement recommandé d'utiliser l'endpoint en temps réel pour les Canvas.
4. Personnalisez le modèle en modifiant ses variables dans l'onglet **Rédiger**.

## Personnalisation {#customization}

### Suivre la distribution et le statut d'ouverture {#track-delivery-and-open-status}

Pour intégrer les événements de distribution et d'ouverture des notifications à l'indicateur de conversion d'une campagne, ajoutez un événement personnalisé sur le tableau de bord de Braze.

1. Depuis le tableau de bord de Braze, accédez à **Paramètres** > **Gérer les paramètres** > **Événements personnalisés**, puis cliquez sur **+ Add Custom Event**.
2. Après avoir créé un événement personnalisé, cliquez sur **Manage Properties**, ajoutez une propriété nommée « status » et choisissez « String » comme type de propriété.
3. Lorsque vous composez une notification dans les Campaigns ou les Canvas, saisissez le nom de l'événement personnalisé dans le champ **Event Name**.

Cet événement personnalisé sera déclenché deux fois pour chaque notification : lorsqu'un message est envoyé et lorsqu'un utilisateur ouvre le message.
- Lorsqu'un message est envoyé, un événement personnalisé est déclenché avec le statut `SENT`.
- Lorsqu'un message est lu, un événement personnalisé est déclenché avec le statut `READ`.