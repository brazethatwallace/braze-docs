---
nav_title: Google Tag Manager
article_title: Google Tag Manager avec le SDK Braze
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Découvrez comment initialiser le SDK Braze à l'aide de méthodes telles que l'initialisation au démarrage, l'initialisation différée ou Google Tag Manager."

---

# Google Tag Manager avec le SDK Braze {#google-tag-manager-with-the-braze-sdk}

> Découvrez comment utiliser [Google Tag Manager (GTM)](https://developers.google.com/tag-platform/tag-manager) avec le SDK Braze, afin de contrôler à distance le suivi des événements Braze et les mises à jour des attributs utilisateur sans nécessiter de modifications de code ni de nouvelles versions de l'application.

{% sdktabs %}
{% sdktab web %}
## À propos de Google Tag Manager pour le Web {#google-tag-manager}

Google Tag Manager (GTM) vous permet d'ajouter, de supprimer et de modifier à distance des balises sur votre site web, sans nécessiter de mise en production ni de ressources techniques. Braze propose les modèles suivants pour le SDK Web :

| Type de balise | Cas d'utilisation |
|--------|--------|
| Balise d'initialisation | Cette balise vous permet d'[intégrer le SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sans avoir à modifier le code de votre site. |
| Balise d'action | Cette balise vous permet de [créer des Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), de [définir les attributs utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) et de [gérer la collecte des données]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="À propos de Google Tag Manager pour le Web" }

## Séquençage des balises pour les balises d'action Braze {#tag-sequencing-for-braze-action-tags}

La balise Braze Initialization doit se déclencher avant toute balise qui appelle des méthodes du SDK Braze (telles que `braze.getUser()`, `braze.logCustomEvent()` ou `braze.logPurchase()`). Si ces méthodes se déclenchent avant l'initialisation du SDK, vous pourriez rencontrer des erreurs comme `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')`.

Pour configurer le séquençage des balises dans Google Tag Manager :

1. Ouvrez la balise qui appelle les méthodes du SDK Braze (comme une balise HTML personnalisée ou une balise d'action Braze).
2. Accédez à **Advanced Settings** > **Tag Sequencing**.
3. Sélectionnez **A tag that fires before [this tag] is fired**.
4. Choisissez votre balise **Braze Initialization**.

Cela garantit que le SDK est entièrement chargé avant que d'autres balises ne tentent d'appeler les méthodes Braze.

Pour plus de détails, consultez [Vérifier le séquençage des balises pour les événements personnalisés]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing).

## Enregistrer des achats avec GTM {#log-purchases-with-gtm}

Dans les balises d'action Braze et les balises HTML personnalisées, appelez `braze.logPurchase()` pour enregistrer le chiffre d'affaires. L'ancien espace de noms `appboy.logPurchase()` n'est pas pris en charge dans les intégrations actuelles du SDK Web.

## Journaliser des événements personnalisés avec GTM {#logging-custom-events-with-gtm}

Vous pouvez journaliser des événements personnalisés à l'aide d'une balise **Custom HTML** dans GTM. Cette approche utilise la [couche de données](https://developers.google.com/tag-platform/tag-manager/datalayer) GTM pour transmettre les données d'événement de votre site à une balise GTM qui appelle le SDK Web de Braze.

### Étape 1 : Envoyer l'événement à la couche de données {#step-1-push-the-event-to-the-data-layer}

Dans le code de votre site, envoyez un événement à la couche de données partout où vous souhaitez déclencher l'événement personnalisé. Par exemple, pour journaliser un événement personnalisé lorsqu'un bouton est cliqué :

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Étape 2 : Créer un déclencheur dans GTM {#step-2-create-a-trigger-in-gtm}

1. Dans votre conteneur GTM, accédez à **Triggers** et créez un nouveau déclencheur.
2. Définissez le **Trigger Type** sur **Custom Event**.
3. Définissez le **Event Name** sur la même valeur que celle envoyée à la couche de données (par exemple, `my_custom_event`).
4. Choisissez quand le déclencheur doit se déclencher (par exemple, **All Custom Events**).

### Étape 3 : Créer une balise HTML personnalisée {#step-3-create-a-custom-html-tag}

1. Dans GTM, accédez à **Tags** et créez une nouvelle balise.
2. Définissez le **Tag Type** sur **Custom HTML**.
3. Dans le champ HTML, ajoutez le code suivant :

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. Sous **Triggering**, sélectionnez le déclencheur que vous avez créé à l'étape 2.
5. Enregistrez et publiez votre conteneur.

Pour inclure des propriétés d'événement, transmettez-les en tant que deuxième argument :

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Politique de consentement des utilisateurs de l'UE de Google {#googles-eu-user-consent-policy}

{% alert important %}
Google met à jour sa [politique de consentement des utilisateurs de l'UE](https://www.google.com/about/company/user-consent-policy/) en réponse aux modifications apportées au [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), en vigueur depuis le 6 mars 2024. Ce nouveau changement exige que les annonceurs divulguent certaines informations à leurs utilisateurs finaux de l'EEE et du Royaume-Uni, et qu'ils obtiennent les consentements nécessaires de leur part. Consultez la documentation suivante pour en savoir plus.
{% endalert %}

Dans le cadre de la politique de consentement des utilisateurs de l'UE de Google, les attributs personnalisés booléens suivants doivent être enregistrés dans les profils utilisateur :

- `$google_ad_user_data`
- `$google_ad_personalization`

Si vous définissez ces attributs via l'intégration GTM, les attributs personnalisés nécessitent la création d'une balise HTML personnalisée. Voici un exemple montrant comment journaliser ces valeurs en tant que types de données booléens (et non en tant que chaînes de caractères) :

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Pour plus d'informations, consultez [Audience Sync vers Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync).

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## Résolution des problèmes {#troubleshooting}

Si Braze ne s'initialise pas ou si les événements n'apparaissent pas comme prévu, vérifiez que votre conteneur GTM est publié, que les déclencheurs et l'ordre de déclenchement des balises correspondent à votre [cycle de vie et stratégie d'initialisation]({{site.baseurl}}/developer_guide/sdk_integration) du SDK, et que les appareils de test ne bloquent pas les endpoints de Braze.

En cas d'échec de l'initialisation, vérifiez que la balise Braze ou le fournisseur d'étiquettes personnalisé reçoit le `actionType` et les paramètres attendus (consultez les onglets Android, Swift et Web sur cette page). Pour activer la journalisation détaillée lors de la validation des événements déclenchés par GTM, activez la journalisation de débogage du SDK de votre plateforme comme décrit dans les guides d'intégration de la plateforme accessibles depuis ces onglets.