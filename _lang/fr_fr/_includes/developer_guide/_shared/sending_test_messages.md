# Envoyer des messages de test {#sending-test-messages}

> Avant d'envoyer une campagne de communication à vos utilisateurs, vous pouvez la tester pour vous assurer qu'elle s'affiche correctement et fonctionne de la manière prévue. Vous pouvez utiliser le tableau de bord pour créer et envoyer des messages de test avec des notifications push, des messages in-app (IAM) ou des e-mails.

## Envoi d'un message de test {#sending-a-test-message}

### Étape 1 : Créer un segment d'essai désigné <a class="margin-fix" name="test-segment"></a> {#step-1-create-a-designated-test-segment}

Une fois que vous avez configuré un segment d'essai, vous pouvez l'utiliser pour tester n'importe lequel de vos canaux de communication Braze. Lorsqu'elle est correctement configurée, cette opération ne doit être effectuée qu'une seule fois.

Pour mettre en place un segment d'essai, allez dans **Segments** et créez un nouveau segment. Sélectionnez **Add Filter**, puis choisissez l'un des filtres de test.

![Une campagne de test Braze affichant les filtres disponibles dans l'étape de ciblage.]({% image_buster /assets/img_archive/testmessages1.png %})

Grâce aux filtres de test, vous pouvez vous assurer que seuls les utilisateurs ayant une adresse e-mail ou un [ID utilisateur externe]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) spécifique reçoivent le message de test.

![Un menu déroulant présentant plusieurs filtres répertoriés sous un en-tête indiquant Testing]({% image_buster /assets/img_archive/testmessages2.png %})

Les filtres d'adresses e-mail et d'ID utilisateur externe offrent les options suivantes :

| Opérateur          | Description |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals`      | Recherche une correspondance exacte avec l'e-mail ou l'ID utilisateur que vous avez fourni. Utilisez cette option si vous souhaitez envoyer les campagnes de test uniquement aux appareils associés à un seul e-mail ou ID utilisateur. |
| `does not equal` | Utilisez cette option si vous souhaitez exclure un e-mail ou un ID utilisateur particulier des campagnes de test. |
| `matches`     | Trouve les utilisateurs dont l'adresse e-mail ou l'ID correspond à une partie du terme de recherche que vous avez fourni. Vous pouvez utiliser cette option pour trouver uniquement les utilisateurs qui ont une adresse `@yourcompany.com`, ce qui vous permet d'envoyer des messages à tous les membres de votre équipe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Create a designated test segment a class="margin-fix" name="test-segment"/a" }

Vous pouvez sélectionner plusieurs adresses e-mail spécifiques en utilisant l'option « `matches` » et en séparant les adresses e-mail par un caractère &#124;. Par exemple : « `matches` » « `email1@braze.com` &#124; `email2@braze.com` ». Vous pouvez également combiner plusieurs opérateurs. Par exemple, le segment d'essai pourrait inclure un filtre d'adresses e-mail qui « `matches` » « `@braze.com` » et un autre filtre qui « `does not equal` » « `sales@braze.com` ».

Après avoir ajouté les filtres de test à votre segment d'essai, vous pouvez vérifier qu'il fonctionne en sélectionnant **Preview** ou en sélectionnant **Settings** > **CSV Export All User Data** pour exporter les données utilisateur de ce segment dans un fichier CSV.

![Une rubrique d'une campagne Braze intitulée Segment Details]({% image_buster /assets/img_archive/testmessages3.png %})

{% alert note %}
L'exportation des données utilisateur du segment vers un fichier CSV est la méthode de vérification la plus précise, car l'aperçu ne montrera qu'un échantillon de vos utilisateurs et peut ne pas inclure tous les utilisateurs.
{% endalert %}

### Étape 2 : Envoyer le message {#step-2-send-the-message}

Vous pouvez envoyer un message à l'aide du tableau de bord de Braze ou de la ligne de commande.

{% tabs local %}
{% tab Using the dashboard %}
{% subtabs %}
{% subtab push or in-app message %}
Pour envoyer des notifications push de test ou des messages in-app, vous devez cibler votre segment d'essai précédemment créé. Commencez par créer votre campagne et suivez les étapes habituelles. Lorsque vous arrivez à l'étape **Target Audiences**, sélectionnez votre segment d'essai dans le menu déroulant.

![Une campagne de test Braze affichant les segments disponibles dans l'étape de ciblage.]({% image_buster /assets/img_archive/test_segment.png %})

Confirmez votre campagne et lancez-la pour tester vos notifications push et vos messages in-app.

{% alert note %}
Veillez à sélectionner **Allow users to become re-eligible to receive campaign** dans la partie **Schedule** du compositeur de campagne si vous avez l'intention d'utiliser une seule campagne pour vous envoyer un message de test plus d'une fois.
{% endalert %}
{% endsubtab %}

{% subtab email message %}
Si vous ne testez que des messages e-mail, vous n'avez pas nécessairement besoin de configurer un segment d'essai. Dans la première étape du compositeur de campagne où vous rédigez le message e-mail de votre campagne, cliquez sur **Send Test** et saisissez l'adresse e-mail à laquelle vous souhaitez envoyer un e-mail de test.

![Une campagne Braze avec l'onglet Send Test sélectionné]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
Vous pouvez également activer ou désactiver l'ajout de [TEST (ou SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) à vos messages de test.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Using the command line %}
Vous pouvez également envoyer une seule notification à l'aide de cURL et de l'[API d'envoi de messages de Braze]({{site.baseurl}}/api/endpoints/messaging/). Notez que ces exemples font une requête en utilisant l'instance `US-01`. Pour connaître la vôtre, reportez-vous aux [endpoints de l'API]({{site.baseurl}}/api/basics/#endpoints).

{% subtabs local %}
{% subtab android %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab swift %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": {
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab kindle %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}
{% endsubtabs %}

Remplacez les éléments suivants :

| Marque substitutive         | Description                                               |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY`      | Votre clé API Braze utilisée pour l'authentification. Dans Braze, allez dans **Settings** > **API Keys** pour localiser votre clé. |
| `EXTERNAL_USER_ID` | L'ID utilisateur externe utilisé pour envoyer votre message à un utilisateur spécifique. Dans Braze, allez dans **Audience** > **Search Users**, puis recherchez un utilisateur. |
| `CUSTOM_KEY`         | (Facultatif) Une clé personnalisée pour des données supplémentaires.              |
| `CUSTOM_VALUE`       | (Facultatif) Une valeur personnalisée attribuée à votre clé personnalisée.    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Send the message" }
{% endtab %}
{% endtabs %}

## Limites des tests {#test-limitations}

Dans quelques situations, les messages de test ne disposent pas d'une parité complète de fonctionnalités par rapport au lancement d'une campagne ou d'un Canvas à un ensemble réel d'utilisateurs. Dans ces cas, pour valider ce comportement, vous devez lancer la campagne ou le Canvas à un ensemble limité d'utilisateurs test.

- L'affichage du [centre de préférences]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) de Braze à partir des **messages de test** entraînera le grisement du bouton d'envoi.
- L'en-tête list-unsubscribe n'est pas inclus dans les e-mails envoyés par la fonctionnalité de message de test.
- Pour les messages in-app et les Content Cards, l'utilisateur cible doit disposer d'un jeton de notification push pour l'appareil cible.