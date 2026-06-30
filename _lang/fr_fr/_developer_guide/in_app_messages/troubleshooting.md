---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des messages in-app pour le SDK Braze
page_order: 50
description: "Diagnostiquez pourquoi les messages in-app ne sont pas distribués ou affichés à l'aide d'un index des symptômes, d'un parcours d'investigation standard, de précisions sur les messages in-app Canvas et de vérifications SDK spécifiques à chaque plateforme."
channel:
  - in-app messages

---

# Résolution des problèmes des messages in-app {#troubleshoot-in-app-messages}

> Utilisez cette page pour diagnostiquer pourquoi les messages in-app ne sont pas distribués ou affichés sur un appareil. Pour la configuration côté tableau de bord (priorité, déclencheurs, segments et rééligibilité), consultez la [FAQ sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

Avant de déboguer, ajoutez-vous en tant qu'[utilisateur test]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) et consultez [Envoyer des messages de test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages).

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

| Symptôme | Aller à |
| --- | --- |
| Le message in-app ne s'est pas affiché pour un utilisateur | [Un utilisateur](#in-app-message-not-shown-for-one-user) |
| Le message in-app ne s'est pas affiché sur une plateforme (Android, iOS ou Web) | [Une plateforme](#in-app-message-not-shown-on-one-platform) |
| Le message in-app d'une étape **Canvas** ne s'est pas affiché | [Messages in-app Canvas](#canvas-in-app-messages) |
| Le message in-app s'est affiché en retard ou après un délai | [Timing et affichage différé](#timing-and-delayed-display) |
| Les impressions ou les clics semblent incorrects | [Impressions et analyses](#impressions-and-analytics) |
| `triggers` manquant ou vide dans les journaux des événements utilisateurs | [Résolution des problèmes de distribution](#delivery-troubleshooting) |
| Les déclencheurs sont retournés mais rien ne s'affiche sur l'appareil | [Résolution des problèmes d'affichage par plateforme](#platform-specific-display-troubleshooting) |
| Le chargement des ressources du message in-app échoue (iOS, `NSURLError` -1008) | [Chargement des ressources (onglet Swift)]({{site.baseurl}}/developer_guide/in_app_messages/troubleshooting?sdktab=swift#asset-loading) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme de message in-app" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail pour chaque incident. Commencez à l'étape 1.

1. Confirmez qu'un **démarrage de session** est enregistré pour l'appareil de test. Les messages in-app sont demandés au démarrage de la session.
2. Ouvrez les [journaux des événements utilisateurs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) et trouvez la requête SDK pour ce démarrage de session. Dans **Response Data** :
   - Dans le JSON brut, confirmez que `respond_with` inclut `"triggers": true`.
   - La ligne **Requested Responses** doit inclure **`triggers`**.
   - Les lignes **Trigger In-App Message** listent chaque message in-app retourné pour cette requête.
   - S'il n'y a pas de clé `triggers` ni de lignes **Trigger In-App Message**, consultez [Résoudre les problèmes de messages non demandés](#troubleshoot-messages-not-being-requested).
   - Si `triggers` est présent mais vide (`[]`), consultez [Résoudre les problèmes de messages non retournés](#troubleshoot-messages-not-being-returned).
   - Si des lignes **Trigger In-App Message** sont présentes mais que rien ne s'affiche, consultez [Résolution des problèmes d'affichage par plateforme](#platform-specific-display-troubleshooting).
   - Chaque payload de déclencheur inclut un `type` : `inapp` (standard) ou `templated_iam` (nécessite une requête de modèle avant l'affichage). Voir [Types de messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
3. Pour l'éligibilité côté tableau de bord (segment, rééligibilité, plafonds de fréquence, priorité, groupes de contrôle), consultez [Résolution des problèmes de distribution](#delivery-troubleshooting) et la [FAQ sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
4. Pour les problèmes d'affichage côté appareil (délégués, limites de débit, orientation, délai d'expiration de session), sélectionnez votre onglet SDK sous [Résolution des problèmes d'affichage par plateforme](#platform-specific-display-troubleshooting).

## Messages in-app Canvas {#canvas-in-app-messages}

**Symptôme :** Un utilisateur est entré dans une étape de message in-app Canvas mais n'a pas vu le message au moment attendu.

Trois comportements sont à l'origine de la plupart des tickets liés aux Canvas et aux messages in-app :

1. **Affichage à la session suivante :** Les messages in-app Canvas sont éligibles au *prochain* démarrage de session après le traitement de l'étape, et non immédiatement en cours de session. Voir [Quand les messages in-app dans Canvas sont-ils envoyés ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) dans la FAQ Canvas.
2. **Validations de distribution à l'entrée de l'étape :** Si **Valider l'audience à l'envoi du message** est activé sur l'étape Message, l'appartenance au segment et les plafonds de fréquence sont évalués lorsque l'utilisateur **entre dans l'étape**, et non au moment de l'affichage. Voir [Validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
3. **Délai et expiration de session :** Si un utilisateur entre dans une étape de délai plus longue que le délai d'expiration de session de votre SDK, il peut démarrer une nouvelle session avant l'étape du message in-app. Le message pourrait ne pas être récupéré au démarrage de la session au moment où vous vous attendez à ce qu'il s'affiche.

Pour les fenêtres de disponibilité, l'expiration et les _Envois_ à zéro dans les analyses Canvas, consultez [Messages in-app et distribution]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery) dans la FAQ Canvas.

{% alert important %}
Les messages in-app dans Canvas ne peuvent être déclenchés que par des événements envoyés via le SDK, et non par la REST API.
{% endalert %}

## Le message in-app ne s'est pas affiché pour un utilisateur {#in-app-message-not-shown-for-one-user}

**Symptôme :** Un utilisateur n'a pas reçu un message in-app attendu ; les autres utilisateurs peuvent ne pas être affectés.

Vérifiez les points suivants :

- L'utilisateur était-il dans le segment au **démarrage de la session**, lorsque le SDK demande les nouveaux messages in-app ?
- L'utilisateur était-il éligible ou rééligible selon les règles de ciblage de la campagne ou du Canvas ? Voir [Rééligibilité pour les Campaigns et Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- Un [plafond de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) s'est-il appliqué ?
- L'utilisateur faisait-il partie d'un groupe de contrôle de la campagne ? Vérifiez si la campagne est configurée pour un test A/B.
- Un message in-app de priorité supérieure s'est-il affiché à la place ? Voir [Plusieurs messages in-app peuvent-ils s'afficher dans la même session ?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session) dans la FAQ sur les messages in-app.
- L'appareil était-il dans l'orientation spécifiée par la campagne ?
- Le message a-t-il été supprimé par l'intervalle minimum par défaut de 30 secondes entre les déclencheurs ? Voir [Remplacer la limite de débit par défaut]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#overriding-the-default-rate-limit).

Suivez ensuite le [parcours d'investigation standard](#standard-investigation-path).

## Le message in-app ne s'est pas affiché sur une plateforme {#in-app-message-not-shown-on-one-platform}

**Symptôme :** Les messages in-app ne s'affichent pas sur Android, iOS ou Web, mais peuvent fonctionner sur d'autres plateformes.

| Cause probable | Ce qu'il faut vérifier |
| --- | --- |
| Mauvaise cible **Envoyer à** | Confirmez que la campagne ou l'étape Canvas cible **Applications mobiles** ou **Navigateurs web** selon le cas. Une campagne Web uniquement ne sera pas envoyée aux appareils Android. |
| Une interface personnalisée ou un gestionnaire supprime l'affichage | Vérifiez les délégués (mobile) ou [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) (Web). Voir [Personnalisation]({{site.baseurl}}/developer_guide/in_app_messages/customization) et votre onglet SDK ci-dessous. |
| L'intégration n'a jamais fonctionné sur cette plateforme | Confirmez que cette plateforme et cette version de l'application ont déjà affiché des messages in-app. |
| Le déclencheur ne s'est pas activé sur l'appareil | Le déclencheur doit se produire localement via le SDK. Un appel REST API ne peut pas déclencher un message in-app dans le SDK. Voir [Déclencher des messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages). |
| `triggers` vide dans les journaux des événements utilisateurs | Segment, rééligibilité, plafond de fréquence ou groupe de contrôle. Voir [Résoudre les problèmes de messages non retournés](#troubleshoot-messages-not-being-returned). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cause du symptôme par plateforme" }

## Le message in-app ne s'est affiché pour aucun utilisateur {#in-app-message-not-shown-for-all-users}

**Symptôme :** Aucun utilisateur ou moins d'utilisateurs que prévu n'a reçu le message in-app.

Vérifiez les points suivants :

- L'action de déclenchement est-elle correctement configurée dans le tableau de bord et dans l'intégration de l'application ?
- Un message in-app de priorité supérieure a-t-il intercepté la campagne ? Voir la [FAQ sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).
- Utilisez-vous une version récente du SDK ? Certains types de messages in-app ont des exigences minimales de version SDK.
- Les sessions sont-elles correctement intégrées ? Confirmez que les analyses de session fonctionnent pour cette application.
- Une bibliothèque d'interface personnalisée interfère-t-elle avec l'affichage ? Voir [Personnalisation]({{site.baseurl}}/developer_guide/in_app_messages/customization).

Suivez ensuite le [parcours d'investigation standard](#standard-investigation-path).

## Timing et affichage différé {#timing-and-delayed-display}

**Symptôme :** Le message in-app est apparu plus tard que prévu ou seulement lors d'une nouvelle session.

Causes courantes :

- **Préchargement au démarrage de session :** Les messages in-app sont mis en cache au démarrage de la session et s'affichent lorsque le déclencheur se produit. Un déclencheur qui se produit avant le prochain démarrage de session ne s'affichera pas avant cette session. Voir [Déclencher des messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).
- **Comportement de session suivante dans Canvas :** Voir [Messages in-app Canvas](#canvas-in-app-messages).
- **Délai planifié dans le tableau de bord :** Vérifiez si un délai est configuré sur la campagne ou l'étape.
- **Condition de concurrence des déclencheurs :** Si les utilisateurs enregistrent un événement immédiatement après le démarrage de la session, les déclencheurs peuvent ne pas encore être synchronisés. Envisagez de déclencher sur le démarrage de session et de segmenter sur l'événement visé afin que la distribution se fasse à la session suivante après l'événement.
- **Messages in-app séquentiels :** Si vous différez ou restaurez des messages dans un parcours, voir [Différer les messages in-app déclenchés]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
- **Ressources volumineuses ou CDN lent :** Optimisez les images et les vidéos pour les messages in-app HTML. Sur mobile, les images peuvent être téléchargées avant l'affichage sur les réseaux lents — sélectionnez votre onglet SDK ci-dessous pour les notes spécifiques à la plateforme.

{% alert note %}
Si votre message in-app est déclenché par le démarrage de session et que vous avez défini un délai d'expiration de session prolongé, fermer et rouvrir l'application dans cette fenêtre ne rafraîchira pas la session. Par exemple, avec un délai d'expiration de 300 secondes, un message in-app déclenché au démarrage de session ne s'affichera pas tant que la session ne sera pas réellement rafraîchie. Ajustez le délai d'expiration de session ou le type de déclencheur si cela affecte votre test.
{% endalert %}

## Résolution des problèmes de distribution {#delivery-troubleshooting}

La plupart des problèmes de messages in-app relèvent de la **distribution** (l'appareil n'a pas reçu les déclencheurs) ou de l'**affichage** (les déclencheurs sont arrivés mais ne se sont pas affichés). Confirmez d'abord la [distribution](#troubleshooting-in-app-message-delivery), puis vérifiez l'[affichage](#platform-specific-display-troubleshooting).

### Résoudre les problèmes de distribution {#troubleshooting-in-app-message-delivery}

Le SDK demande les messages in-app aux serveurs Braze au démarrage de la session. Confirmez que le SDK demande les déclencheurs et que Braze les retourne.

#### Vérifier si les messages sont demandés et retournés {#check-if-messages-are-requested-and-returned}

1. Ajoutez-vous en tant qu'[utilisateur test]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users).
2. Configurez une campagne de message in-app ciblant votre utilisateur.
3. Démarrez une nouvelle session dans votre application.
4. Dans les [journaux des événements utilisateurs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log), trouvez la requête SDK pour l'événement de démarrage de session. Dans **Response Data** :
   - Dans le JSON brut, confirmez que `respond_with` inclut `"triggers": true`.
   - La ligne **Requested Responses** liste les clés de premier niveau dans la réponse. Pour les messages in-app, attendez-vous à **`triggers`**.
   - Les lignes **Trigger In-App Message** listent chaque message in-app retourné pour cette requête.

   Puis triez :
   - S'il n'y a pas de clé `triggers` ni de lignes **Trigger In-App Message**, voir [Résoudre les problèmes de messages non demandés](#troubleshoot-messages-not-being-requested).
   - Si `triggers` est présent mais vide (`[]`), voir [Résoudre les problèmes de messages non retournés](#troubleshoot-messages-not-being-returned).
   - Si des lignes **Trigger In-App Message** sont présentes mais que rien ne s'affiche sur l'appareil, voir [Résolution des problèmes d'affichage par plateforme](#platform-specific-display-troubleshooting).
   - Chaque payload de déclencheur inclut un `type` : `inapp` (standard) ou `templated_iam` (nécessite une requête de modèle avant l'affichage). Voir [Types de messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
5. Confirmez que les messages in-app corrects apparaissent dans les données de réponse.

![Journal des événements utilisateurs avec les requêtes SDK et les données de réponse.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Résoudre les problèmes de messages non demandés {#troubleshoot-messages-not-being-requested}

Si les messages in-app ne sont pas demandés, votre application ne suit peut-être pas correctement les sessions — les messages in-app se rafraîchissent au démarrage de la session. Confirmez que l'application démarre une session en fonction de la sémantique de votre délai d'expiration de session :

![La requête SDK trouvée dans les journaux des événements utilisateurs affichant un événement de démarrage de session réussi.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Résoudre les problèmes de messages non retournés {#troubleshoot-messages-not-being-returned}

Si les messages in-app ne sont pas retournés, vous rencontrez probablement un problème de ciblage ou d'éligibilité :

1. Votre segment ne contient pas votre utilisateur.
   - Vérifiez l'onglet [**Engagement**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) de l'utilisateur pour le segment attendu.
2. Votre utilisateur a déjà reçu le message et n'était pas rééligible.
   - Vérifiez les [paramètres de rééligibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) et la [FAQ sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#campaigns).
3. Votre utilisateur a atteint le plafond de fréquence.
   - Vérifiez les [paramètres de plafond de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).
4. Votre utilisateur est tombé dans un groupe de contrôle.
   - Créez un segment avec un filtre **A reçu une variante de campagne** défini sur **Contrôle**, ou désactivez les groupes de contrôle pendant les tests d'intégration.
5. Un message in-app de priorité supérieure a pris le dessus. Voir la [FAQ sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).

Pour les campagnes archivées, la configuration des déclencheurs et les heures calmes, consultez la [FAQ sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Impressions et analyses {#impressions-and-analytics}

**Symptôme :** Le nombre d'impressions ou de clics ne correspond pas aux attentes.

- **_Impressions_ supérieures aux _Impressions uniques_ :** Cela est attendu lorsque les utilisateurs possèdent plusieurs appareils ou lorsqu'un délai planifié fait qu'un même utilisateur se qualifie plus d'une fois. Voir [Rééligibilité pour les Campaigns et Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- **Impressions inférieures aux attentes :** Les utilisateurs peuvent ne pas avoir vu le message (les impressions sont enregistrées à l'affichage), plusieurs messages de haute priorité peuvent s'intercepter mutuellement, ou des conditions de concurrence des déclencheurs peuvent s'appliquer. Pour les messages in-app Canvas, voir [Messages in-app Canvas](#canvas-in-app-messages). Pour les définitions complètes des indicateurs, voir [Rapports sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) et la [FAQ sur les messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
- **Impressions inférieures à avant :** Consultez les journaux de modifications du segment et de la campagne. Confirmez que vous n'avez pas réutilisé le même événement déclencheur dans une campagne de priorité supérieure.

![Lien pour consulter le journal des modifications sur la page Détails de la campagne avec sept modifications depuis la dernière consultation par l'utilisateur.]({% image_buster /assets/img_archive/trouble4.png %})

Si vous utilisez un délégué ou un gestionnaire personnalisé pour afficher les messages in-app manuellement, vous devez enregistrer les impressions et les clics vous-même. Consultez votre onglet SDK sous [Résolution des problèmes d'affichage par plateforme](#platform-specific-display-troubleshooting) pour les détails Swift et Android, ou [Enregistrer les données des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data) pour le Web.

## Résolution des problèmes d'affichage par plateforme {#platform-specific-display-troubleshooting}

Si des lignes **Trigger In-App Message** apparaissent dans les journaux des événements utilisateurs mais que rien ne s'affiche sur l'appareil, sélectionnez votre onglet SDK pour les vérifications d'affichage (délégués, limites de débit, orientation et gestionnaires personnalisés).

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/in_app_messages/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}