---
nav_title: Google tag manager
article_title: Google Tag Manager with the Braze SDK
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Learn how to initialize the Braze SDK using methods like runtime initialization, delayed initialization, or Google Tag Manager."

---
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

## Résolution des problèmes

### Sessions du SDK Web attribuées au mauvais utilisateur

Si GTM déclenche les balises d'initialisation ou d'événement de Braze avant que votre application identifie l'utilisateur connecté, les sessions et les événements peuvent être associés au mauvais profil. Initialisez le SDK Web, appelez `changeUser()` avec l'`external_id` de l'utilisateur connecté, puis appelez `openSession()` avant toute balise qui enregistre des événements ou définit des attributs. Utilisez le séquençage des balises GTM ou des déclencheurs de consentement pour que les balises Braze ne s'exécutent qu'après la fin de votre flux d'authentification.

### Journalisation console du SDK Web avec Shopify ou les installations par balise script

L'intégration de l'application Shopify charge le SDK Web avec la journalisation console désactivée. Configurez la journalisation dans votre balise d'initialisation GTM ou dans les options d'`initialize()`. Le tableau de bord de Braze n'inclut pas de contrôle de journalisation pour ces chargeurs.

Si des journaux Braze apparaissent dans la console du navigateur, supprimez `enableLogging: true` de la balise d'initialisation GTM ou du code HTML personnalisé avant de publier en production. Après l'initialisation, utilisez `toggleLogging()` ou le paramètre d'URL `?brazeLogging=true`. Pour l'ensemble des options du SDK Web, consultez la section [Journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

Si Braze ne s'initialise pas ou si les événements n'apparaissent pas comme prévu, vérifiez que votre conteneur GTM est publié, que les déclencheurs et l'ordre de déclenchement des balises correspondent à votre [cycle de vie et stratégie d'initialisation]({{site.baseurl}}/developer_guide/sdk_integration) du SDK, et que les appareils de test ne bloquent pas les endpoints de Braze.

En cas d'échec d'initialisation, vérifiez que la balise Braze ou le fournisseur d'étiquettes personnalisé reçoit le `actionType` et les paramètres attendus (voir les onglets Android, Swift et Web sur cette page). Pour activer la journalisation détaillée lors de la validation des événements déclenchés par GTM, activez la journalisation de débogage du SDK de votre plateforme comme décrit dans les guides d'intégration de plateforme accessibles depuis ces onglets.