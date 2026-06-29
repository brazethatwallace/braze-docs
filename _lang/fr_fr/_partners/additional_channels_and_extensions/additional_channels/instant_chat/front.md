---
nav_title: Front
article_title: Front
description: "Découvrez comment intégrer Front à Braze"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> L'intégration de Front vous permet de tirer parti de la Transformation des données de Braze et des webhooks de chaque plateforme pour mettre en place un pipeline SMS conversationnel bidirectionnel.

Le webhook entrant provenant de Front contiendra un payload comprenant le message envoyé par l'agent. La requête devra être reformatée avant de pouvoir être acceptée par les endpoints de Braze. Le modèle de Transformation des données de Front reformatera le payload et écrira un événement personnalisé dans le profil utilisateur intitulé **Outbound SMS Sent,** le corps du message étant transmis en tant que propriété de l'événement.

Avant de configurer une nouvelle transformation dans Braze, nous vous recommandons de consulter la matrice de prise en charge de chaque niveau dans notre documentation sur la [Transformation des données]({{site.baseurl}}/user_guide/data/unification/data_transformation/). Nos niveaux Free et Pro offrent un nombre différent de transformations actives et de requêtes entrantes par mois. Vérifiez que le plan auquel vous avez souscrit peut prendre en charge votre cas d'utilisation.

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Conditions préalables | Description |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte Front | Un compte Front est nécessaire pour tirer parti de ce partenariat. |
| URL du webhook de Transformation des données Braze | La [Transformation des données de Braze]({{site.baseurl}}/user_guide/data/unification/data_transformation/) sera utilisée pour reformater le webhook entrant de Front afin qu'il puisse être accepté par l'endpoint Braze /users/track. |
| Une clé API REST Front | Une clé API REST de Front sera utilisée pour effectuer une requête webhook sortante de Braze vers Front. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

- Rationalisez votre processus de génération de prospects en utilisant les messages SMS automatisés de Braze pour identifier les préférences des utilisateurs et permettre aux agents commerciaux d'assurer le suivi et de conclure les ventes.
- Réengagez les clients qui ont abandonné leur panier en stimulant les conversions grâce aux réponses SMS automatisées et à l'assistance par chat en direct.

## Intégration de Front {#integrating-front}

### Étape 1 : Créer une transformation de données {#step-1-create-a-data-transformation}

Tout d'abord, vous allez créer une nouvelle transformation de données dans Braze. Les étapes suivantes sont simplifiées ; pour une description complète, consultez [Création d'une transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation/).

1. Dans Braze, accédez à **Paramètres des données** > **Transformations de données**, puis sélectionnez **Créer une transformation**.
2. Sous **Expérience d'édition**, sélectionnez **Recommencer à zéro**.
3. Sous **Sélectionner une destination**, sélectionnez **POST : Suivre les utilisateurs**.
4. Copiez et collez le modèle de transformation suivant, puis enregistrez et activez l'endpoint.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Votre transformation doit refléter l'exemple JavaScript ci-dessus, en adaptant les noms de propriétés et les chemins à la charge utile du webhook Front.

{% alert tip %}
Vous pouvez modifier ce modèle pour répondre à vos besoins spécifiques. Par exemple, vous pouvez personnaliser le nom de l'événement personnalisé prédéfini. Pour plus d'informations, consultez l'[aperçu de la Transformation des données]({{site.baseurl}}/user_guide/data/unification/data_transformation/).
{% endalert %}

### Étape 2 : Créer une campagne SMS sortante {#step-2-create-an-outbound-sms-campaign}

Ensuite, vous allez créer une campagne SMS qui écoutera les webhooks de Front et enverra une réponse SMS personnalisée à vos clients.

#### Étape 2.1 : Rédigez votre message {#step-21-compose-your-message}

Dans la zone de texte **Message**, ajoutez le code Liquid suivant, ainsi que tout texte de désabonnement ou autre contenu statique.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Votre message devrait ressembler à ce qui suit :

![Un exemple de message utilisant du code Liquid.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Planifier la distribution {#22-schedule-the-delivery}

Pour le type de distribution, sélectionnez **Livraison par événement** ; puis pour le déclencheur d'événement personnalisé, sélectionnez **Outbound SMS Sent**.

![La page « Planifier la distribution ».]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
Cet événement personnalisé est la Transformation des données qui écrit dans le profil de l'utilisateur. Les messages de l'agent seront enregistrés en tant que propriété de cet événement.
{% endalert %}

Enfin, sous **Contrôles de l'envoi**, activez la rééligibilité.

![Rééligibilité activée sous « Contrôles de l'envoi ».]({% image_buster /assets/img/front/braze_reeligibility.png %})

### Étape 3 : Créer un canal personnalisé {#step-3-create-a-custom-channel}

Dans le tableau de bord de Front, accédez à **Settings** > **Channels** > **Add Channels**, puis sélectionnez **Custom Channel** et saisissez un nom pour votre nouveau canal Braze.

![Un canal personnalisé pour Braze dans le tableau de bord de Front.]({% image_buster /assets/img/front/front_custom_channel.png %})

### Étape 4 : Configurer les paramètres {#step-4-configure-the-settings}

Dans le champ de l'endpoint API sortant, saisissez l'URL du webhook de Transformation des données [que vous avez créée précédemment](#step-1-set-up-a-data-transformation-in-braze). Tous les messages sortants des agents en direct sur votre nouveau canal Braze seront envoyés ici. Ce canal fournit également une URL d'endpoint vers laquelle Braze pourra transférer les messages SMS dans le champ **Incoming URL**.

Notez bien cette URL&#8212;vous en aurez besoin plus tard.

![Les paramètres du canal Braze nouvellement créé dans Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### Étape 5 : Configurer le transfert des SMS entrants {#step-5-set-up-inbound-sms-forwarding}

Ensuite, vous allez créer deux nouvelles campagnes webhook dans Braze afin de pouvoir transférer les SMS entrants des clients vers la boîte de réception de Front.

| Nombre | Objectif |
|---|---|
| Campagne webhook 1 | Signale à Front qu'une conversation en direct par chat est demandée. |
| Campagne webhook 2 | Transfère toutes les réponses SMS conversationnelles envoyées par le client vers la boîte de réception de Front. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 5 : Configurer le transfert des SMS entrants" }

#### Étape 5.1 : Créer une catégorie de mots-clés SMS {#step-51-create-an-sms-keyword-category}

Dans le tableau de bord de Braze, accédez à **Audience**, choisissez votre **groupe d'abonnement SMS**, puis sélectionnez **Add Custom Keyword**. Pour créer une catégorie de mots-clés SMS exclusive pour Front, remplissez les champs suivants.

| Champ | Description |
|---|---|
| Catégorie de mots-clés | Le nom de votre catégorie de mots-clés, par exemple `FrontSMS1`. |
| Mots-clés | Vos mots-clés personnalisés, tels que `TIMETOMOW`. Évitez les mots courants pour prévenir les déclenchements accidentels. Gardez à l'esprit que les mots-clés ne sont pas sensibles à la casse, de sorte que `lawn` correspondra à `LAWN`. |
| Message de réponse | Le message qui sera envoyé lorsqu'un mot-clé est détecté, par exemple « Un paysagiste vous contactera sous peu. » |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 5.1 : Créer une catégorie de mots-clés SMS" }

![Un exemple de catégorie de mots-clés SMS dans Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Étape 5.2 : Créer votre première campagne webhook {#step-52-create-your-first-webhook-campaign}

Dans le tableau de bord de Braze, créez votre première campagne webhook à l'aide de l'URL [que vous avez créée précédemment](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Un exemple de la première campagne webhook à créer dans Braze.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Ajoutez ce qui suit au corps de votre requête :

{% raw %}
```liquid
{
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

Dans l'onglet Paramètres, configurez vos en-têtes de requête `Authorization`, `content-type` et `accept`.

![Un exemple de requête avec les trois en-têtes requis.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Étape 5.3 : Planifier la première distribution {#step-53-schedule-the-first-delivery}

Pour **Planifier la distribution**, sélectionnez **Livraison par événement**, puis choisissez **Send an SMS Inbound Message** pour votre type de déclencheur. Ajoutez également le groupe d'abonnement SMS et la catégorie de mots-clés que vous avez [définis précédemment](#step-51-create-an-sms-keyword-category).

![La page « Planifier la distribution » pour la première campagne webhook.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

Sous **Contrôles de l'envoi**, activez la rééligibilité.

![Rééligibilité sélectionnée sous « Contrôles de l'envoi » pour la première campagne webhook.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Étape 5.4 : Créer votre deuxième campagne webhook {#step-54-create-your-second-webhook-campaign}

Comme votre deuxième campagne webhook est identique à la première, vous pouvez [dupliquer la première et la renommer]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns).

#### Étape 5.5 : Planifier la seconde distribution {#step-55-schedule-the-second-delivery}

Pour **Planifier la distribution**, définissez le **déclencheur basé sur l'action** et le **groupe d'abonnement SMS** de la même manière que pour [la première distribution](#step-53-schedule-the-first-delivery). Toutefois, pour la **catégorie de mots-clés**, choisissez **Other**.

![La page « Planifier la distribution » pour la deuxième campagne webhook, avec « Other » choisi comme catégorie de mots-clés.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Étape 5.6 : Ajouter un filtre d'audience {#step-56-add-an-audience-filter}

Votre campagne webhook peut désormais transférer les réponses SMS entrantes de vos clients. Pour filtrer les réponses SMS afin que seuls les messages destinés aux chats en direct soient transférés, ajoutez le filtre de segmentation **Last Received Message From Specific Campaign** à l'**étape Audiences cibles**.

![Un filtre d'audience avec « Last Received Message From Specific Campaign » sélectionné.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Configurez ensuite votre filtre :

1. Pour **Campaign**, sélectionnez la campagne SMS [que vous avez créée précédemment](#step-2-create-an-outbound-sms-campaign).
2. Pour **Operator**, sélectionnez **Less Than**.
3. Pour **Time Window**, choisissez la durée pendant laquelle un chat doit rester ouvert sans réponse de la part du client.

![Les paramètres de configuration du filtre d'audience sélectionné.]({% image_buster /assets/img/front/front_target_audience.png %})

## Considérations {#considerations}

### Segments de message facturables {#billable-segments}

- Chez Braze, les messages SMS sont facturés par segment de message. Il est essentiel de comprendre ce qui définit un segment et comment ces messages seront découpés pour savoir comment vous serez facturé. Consultez notre [documentation]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/) pour plus d'informations.
- Les longues réponses des agents consommeront davantage de segments facturables.

### Enregistrement des points de données {#logging-data-points}

Actuellement, cette intégration nécessite l'écriture d'un événement personnalisé dans le profil utilisateur à chaque fois qu'un agent en direct envoie un SMS depuis Front. Cela peut convenir à des échanges rapides qui ne durent que quelques messages, mais au fur et à mesure que les conversations s'allongent, les implications en termes de points de données augmentent également. Si vous avez des questions sur les subtilités des points de données de Braze, votre gestionnaire de compte Braze peut y répondre.

### Inclure des liens dans les messages SMS {#including-links-in-sms-messages}

L'envoi d'un lien depuis le chat en direct de Front ajoutera des balises HTML supplémentaires au rendu.

### Joindre un fichier image depuis Front {#attaching-image-file-from-front}

Les fichiers images de Front ne s'afficheront pas dans les messages SMS envoyés depuis Braze.

### Désabonnements {#opt-outs}

Les messages conversationnels présentent un risque plus élevé de contenir le mot « stop » ou un terme similaire pouvant être interprété comme une demande de désabonnement approximative.