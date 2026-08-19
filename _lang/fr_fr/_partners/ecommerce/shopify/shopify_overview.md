---
nav_title: Aperçu de Shopify
article_title: Aperçu de Shopify
description: "Cet article de référence décrit le partenariat entre Braze et Shopify, une entreprise de commerce mondiale qui vous permet de connecter de façon fluide votre boutique Shopify à Braze pour transmettre certains webhooks Shopify dans Braze. Exploitez les stratégies cross-canal de Braze et Canvas pour inciter les clients à finaliser leurs achats ou recibler les utilisateurs en fonction de leurs achats précédents."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Aperçu de Shopify {#shopify-overview}

> [Shopify](https://www.shopify.com/) est un leader mondial du commerce qui fournit des outils de confiance pour démarrer, développer, commercialiser et gérer une entreprise de toute taille. Shopify améliore le commerce pour tout le monde grâce à une plateforme et des services conçus pour la fiabilité, tout en offrant une meilleure expérience d'achat aux consommateurs partout dans le monde.

L'intégration de Braze à Shopify constitue une solution puissante pour les entreprises de commerce électronique qui cherchent à améliorer l'engagement de leurs clients et à mener des actions marketing personnalisées. Cette intégration connecte de façon fluide les fonctionnalités eCommerce robustes de Shopify avec notre plateforme avancée d'engagement client, ce qui vous permet d'envoyer des messages ciblés, pertinents et opportuns à vos utilisateurs en fonction de leurs comportements d'achat en temps réel et des données transactionnelles.

## Conditions requises {#requirements}

| Condition | Description |
| --- | --- |
| Boutique Shopify | Vous disposez d'une boutique Shopify active. |
| Autorisations de propriétaire ou de membre du personnel de la boutique Shopify | {::nomarkdown}<ul><li>Accès à tous les paramètres généraux et de la boutique en ligne.</li><li> Autorisations d'administration supplémentaires :<ul><li>Commandes : Afficher</li><li>Client : Lecture/Écriture</li><li>Afficher les événements client (Web Pixels)</li><li>Gérer les paramètres</li><li>Afficher les applications développées par le personnel/les collaborateurs</li><li>Gérer/Installer les applications et les canaux</li><li>Gérer/Ajouter des pixels personnalisés</li></ul></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions requises" }

## Comment intégrer {#how-to-integrate}

Braze propose deux options d'intégration pour les marchands Shopify, conçues pour répondre aux besoins variés des entreprises d'eCommerce : **Intégration standard** et **Intégration personnalisée**.

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

## Fonctionnement de l'intégration {#how-the-integration-works}

Si vous avez déjà configuré et activé le [remplissage historique]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) dans vos paramètres de configuration, la synchronisation initiale des données commencera immédiatement.

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

Après la synchronisation initiale des données, Braze continuera de suivre en continu les nouvelles données et mises à jour, directement depuis Shopify et les SDK Braze.

{% alert note %}
Si vous êtes un client Braze existant avec des Campaigns ou des Canvas actifs, consultez le [remplissage historique Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill) pour des informations importantes. Pour voir quelles données client spécifiques sont remplies, consultez les [fonctionnalités Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).
{% endalert %}

### Synchronisation des utilisateurs et des données {#user-and-data-syncing}

Une fois l'intégration en direct, Braze collectera les données utilisateur à partir de deux sources clés via l'intégration Shopify :
- **API Shopify Web Pixel et intégrations d'application :** Cela alimente le SDK Web Braze et le SDK Javascript pour prendre en charge le suivi sur site, la gestion de l'identité, les données comportementales eCommerce et les canaux de communication tels que les messages in-app.
- **Webhooks Shopify :** données comportementales eCommerce, synchronisation des produits et collecte des abonnés

Lors de l'onboarding de l'intégration, vous devrez sélectionner le moment où les SDK Braze s'initialisent et chargent votre site Shopify :
- Lors de la visite du site (par exemple, au début de la session)
    - **Ce que cela fait :** Suit les utilisateurs anonymes, tels que les acheteurs invités, pour accéder à davantage de données et permettre une personnalisation plus approfondie
- Lors de l'inscription au compte (par exemple, à la connexion au compte)
    - **Ce que cela fait :** Empêche le suivi des utilisateurs anonymes pour une approche plus conservatrice et axée sur la confidentialité, de sorte que l'activité de l'utilisateur est suivie *après* que l'utilisateur se connecte à son compte

{% alert note %}
- Les visites du site (sessions) sont comptabilisées dans vos allocations d'utilisateurs actifs mensuels (MAU).
- Les versions du SDK Web Braze et du SDK JavaScript sont automatiquement définies sur la v6.8.0. Vous pouvez mettre à jour la version de votre SDK à tout moment depuis les paramètres de l'intégration.
{% endalert %}

Braze utilise l'intégration Shopify pour prendre en charge plusieurs identifiants qui suivent vos utilisateurs depuis leur expérience d'achat en tant qu'invité jusqu'à ce qu'ils deviennent des utilisateurs identifiés :

| Identifiant Braze | Description |
| --- | --- |
| `device_id` Braze | Un ID généré aléatoirement et stocké dans le navigateur qui suit l'activité des utilisateurs anonymes via les SDK Braze. |
| Alias utilisateur du jeton de panier | Un alias que Braze crée pour suivre les événements de mise à jour du panier. Ce jeton est créé à l'aide du jeton de panier Shopify. |
| Alias utilisateur du jeton de paiement | Un alias que Braze crée lorsque l'utilisateur commence le processus de paiement. Ce jeton est créé à l'aide du jeton de paiement Shopify.<br><br> Si un client utilise Shop Pay comme option de paiement accéléré, Shopify peut contourner certains événements de paiement standard et empêcher Braze de recevoir les données nécessaires pour ajouter l'alias du jeton de paiement. |
| Alias de l'ID client Shopify | L'ID client Shopify est attribué en tant qu'alias lorsque l'ID externe est attribué lors de la connexion au compte ou lorsqu'une commande est passée. |
| `external_id` Braze | Un identifiant unique qui aide à suivre les clients sur différents appareils et plateformes. Cela maintient une expérience utilisateur cohérente et améliore l'analyse en empêchant la création de profils multiples lorsque les utilisateurs changent d'appareil ou réinstallent l'application.<br><br>L'intégration Shopify prend en charge les types d'`external_id` suivants : <br><br>{::nomarkdown}<ul><li>ID client Shopify (par défaut)</li><li>ID externe personnalisé</li><li>E-mail haché (SHA-256)</li><li>E-mail haché (SHA-1)</li><li>E-mail haché (MD5)</li><li>E-mail</li></ul>{:/}Braze attribue un `external_id` à vos utilisateurs en appelant la méthode changeUser au sein des SDK lorsque : <br><br>{::nomarkdown}<ul><li>Un utilisateur se connecte ou crée un compte</li><li>Une commande est passée</li></ul>{:/}<br> Pour plus d'informations sur ce qui se passe lorsque vous attribuez un `external_id` à un profil anonyme, consultez [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>Braze exploitera également l'`external_id` pour attribuer les données comportementales eCommerce en aval provenant des webhooks Shopify.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Synchronisation des utilisateurs et des données" }

L'intégration nécessite que les SDK Braze et les services Shopify fonctionnent ensemble pour suivre et attribuer correctement les données Shopify aux bons utilisateurs en quasi-temps réel. Pour plus de détails sur les données suivies via l'intégration, consultez [Données Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

{% alert note %}
- Si vous testez l'intégration, nous vous conseillons d'utiliser le mode navigation privée ou d'effacer vos cookies pour réinitialiser le `device_id` Braze et simuler le comportement d'un utilisateur anonyme.
- Même si un ID client Shopify est généré lorsqu'un e-mail est saisi dans le pied de page de la newsletter Shopify ou pendant le processus de paiement avant qu'une commande ne soit passée, cet ID client n'est pas accessible via les Shopify Web Pixels. Pour cette raison, Braze ne peut pas utiliser la méthode `changeUser` dans ces deux situations.
{% endalert %}

### Synchronisation des abonnements marketing e-mail et SMS Shopify {#syncing-shopify-email-and-sms-marketing-opt-ins}

Si vous activez la collecte des abonnés dans vos paramètres de configuration, vous devez attribuer un groupe d'abonnement pour chaque boutique que vous connectez à Braze. Cela signifie que vos clients seront catégorisés comme « abonnés » ou « désabonnés » du groupe d'abonnement de votre boutique.

Le statut d'abonnement marketing Shopify pour le marketing par e-mail et SMS peut être mis à jour de la manière suivante :
- **Mise à jour manuelle :** Vous pouvez modifier manuellement le statut d'abonnement marketing e-mail ou SMS d'un utilisateur dans votre interface d'administration Shopify.
- **Pied de page de la newsletter Shopify :** Si un utilisateur saisit son e-mail dans le pied de page par défaut de la newsletter Shopify, son statut d'abonnement est mis à jour.
- **Paiement :** Le consentement de l'utilisateur est capturé lors du paiement lorsque les utilisateurs cochent la case marketing et procèdent au paiement en sélectionnant **Pay now** sur le paiement en une page ou **Continue to shipping** sur le paiement en trois pages.

{% alert note %}
Le statut d'abonnement marketing e-mail de Shopify ne modifiera pas l'[état d'abonnement global aux e-mails]({{site.baseurl}}/user_guide/channels/email/subscriptions) d'un utilisateur dans Braze. L'état d'abonnement par défaut lors de la création d'un profil utilisateur est « subscribed ». N'oubliez pas d'utiliser le groupe d'abonnement dans les critères d'entrée de votre Campaign ou Canvas.
{% endalert %}

Ce tableau montre quels états d'abonnement marketing Shopify correspondent aux statuts au sein de votre groupe d'abonnement Braze.

| État d'abonnement marketing Shopify | État du groupe d'abonnement Braze |
| --- | --- |
| E-mail abonné | Subscribed |
| E-mail désabonné | Unsubscribed |
| E-mail en attente de confirmation | Unsubscribed |
| E-mail invalide | Unsubscribed |
| SMS abonné | Subscribed |
| SMS désabonné | Unsubscribed |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Synchronisation des abonnements marketing e-mail et SMS Shopify" }

### Formulaires d'inscription {#sign-up-forms}

#### Pied de page de la newsletter Shopify {#shopify-newsletter-footer}

Les utilisateurs qui saisissent leur adresse e-mail dans le pied de page de la newsletter Shopify suivront l'un de ces parcours :

##### Utilisateurs qui ne se sont pas connectés à leur compte {#users-who-havent-logged-into-their-account}

1. Braze reçoit un webhook entrant de Shopify chaque fois qu'un client est créé ou mis à jour.
2. Braze crée un profil utilisateur contenant l'adresse e-mail et l'alias de l'ID client Shopify associés à cet utilisateur.
3. Le SDK Braze met à jour le profil anonyme avec l'adresse e-mail.

{% alert note %}
Cela peut entraîner un profil en double jusqu'à ce que l'utilisateur s'identifie en créant son compte, en se connectant à son compte ou en passant une commande. Braze propose des outils de fusion en masse pour vous aider à automatiser la réconciliation des profils en double. Consultez [Utilisateurs en double]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users) pour plus de détails.
{% endalert %}

##### Utilisateurs qui se sont déjà connectés à leur compte {#users-who-have-already-logged-into-their-account}

Braze créera un profil utilisateur contenant l'adresse e-mail et l'alias de l'ID client Shopify associés à cet utilisateur. Braze ne mettra pas à jour l'adresse e-mail de l'utilisateur connecté, car nous supposons que Shopify a déjà fourni cette information.

#### Formulaires d'inscription Braze {#braze-sign-up-forms}

Braze propose deux types de modèles de formulaires d'inscription :
- **[Formulaires d'inscription par e-mail]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/email_capture) :** Créez-les à l'aide de l'éditeur par glisser-déposer.
- **[Formulaire de capture d'e-mail de l'éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form) :** Un formulaire plus simple pour capturer les adresses e-mail.

Lorsque vous utilisez ces modèles de formulaires d'inscription, Braze met automatiquement à jour l'état d'abonnement global aux e-mails sur le profil utilisateur. Pour plus de détails sur la gestion de l'état d'abonnement global aux e-mails, y compris des informations sur la validation des e-mails, consultez la documentation de chaque type de modèle de formulaire.

{% alert note %}
- Assurez-vous d'inclure des critères d'entrée dans votre Campaign ou Canvas qui incluent à la fois l'état d'abonnement global aux e-mails et le groupe d'abonnement connectés à votre boutique Shopify. Cela vous aidera à cibler la bonne audience.
- Braze collecte les informations des visiteurs, telles que les adresses e-mail et les numéros de téléphone, via des messages dans le navigateur. Ces informations sont ensuite envoyées à l'API Shopify Visitor mais ne créent pas de profil client dans Shopify. Pour plus de détails, consultez l'[API Visitor](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Formulaires d'inscription tiers {#third-party-sign-up-forms}

Si vous utilisez une plateforme tierce ou un plugin Shopify pour vos formulaires d'inscription, vous devez travailler avec vos développeurs pour intégrer le code du SDK Braze afin de capturer l'adresse e-mail et l'état d'abonnement global aux e-mails à partir des soumissions de formulaires. Pour en savoir plus, consultez la [configuration de l'intégration standard Shopify]({{site.baseurl}}/shopify_standard_integration) et la [configuration de l'intégration personnalisée Shopify]({{site.baseurl}}/shopify_custom_integration).

### Synchronisation des produits {#product-syncing}

Braze prend en charge la synchronisation des produits de votre boutique Shopify dans un catalogue Braze. Pour plus de détails, consultez [Synchronisation des produits Shopify]({{site.baseurl}}/shopify_catalogs).

## Demandes des personnes concernées {#data-subject-requests}

Dans le cadre de l'intégration Shopify de la plateforme Braze, Braze reçoit automatiquement les [webhooks de conformité de Shopify](https://shopify.dev/docs/apps/build/privacy-law-compliance/). Cependant, étant donné que les clients sont les contrôleurs des données de leurs utilisateurs finaux, les clients doivent effectuer toutes les actions nécessaires pour répondre aux demandes des personnes concernées reçues au sujet des données des utilisateurs finaux dans Braze (y compris les données des utilisateurs finaux reçues via l'intégration Shopify). Consultez notre documentation sur l'[assistance technique en matière de protection des données]({{site.baseurl}}/dp-technical-assistance) pour plus de détails.