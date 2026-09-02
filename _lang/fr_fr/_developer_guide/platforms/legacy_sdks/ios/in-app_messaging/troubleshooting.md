---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de messagerie in-app pour iOS
platform: iOS
page_order: 7
description: "Cet article de référence couvre les sujets potentiels de résolution des problèmes liés aux messages in-app sur iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Résolution des problèmes des messages in-app {#troubleshoot-in-app-messages}

## Impressions {#impressions}

### Les analyses d'impressions ou de clics ne sont pas enregistrées {#impression-or-click-analytics-arent-being-logged}

Si vous avez défini un délégué de message in-app pour gérer manuellement l'affichage du message ou les actions de clic, vous devrez enregistrer manuellement les clics et les impressions sur le message in-app.

#### Les impressions sont inférieures aux attentes {#impressions-are-lower-than-expected}

Les déclencheurs mettent du temps à se synchroniser avec l'appareil au démarrage de la session, ce qui peut entraîner une condition de concurrence si les utilisateurs enregistrent un événement ou un achat juste après le début d'une session. Une solution possible consiste à modifier la campagne pour qu'elle se déclenche au démarrage de la session, puis à segmenter en fonction de l'événement ou de l'achat souhaité. Notez que cela entraînera la distribution du message in-app au prochain démarrage de session après la survenue de l'événement.

## Le message in-app attendu ne s'est pas affiché {#expected-in-app-message-did-not-display}

La plupart des problèmes liés aux messages in-app peuvent être répartis en deux catégories principales : la distribution et l'affichage. Pour résoudre le problème d'un message in-app attendu qui ne s'est pas affiché sur votre appareil, vous devez d'abord vous assurer que le [message in-app a été distribué à l'appareil](#troubleshooting-in-app-message-delivery), puis [résoudre les problèmes d'affichage du message](#troubleshooting-in-app-message-display).

### Distribution des messages in-app {#troubleshooting-in-app-message-delivery}

Le SDK demande les messages in-app aux serveurs Braze au démarrage de la session. Pour vérifier si les messages in-app sont distribués à votre appareil, vous devez vous assurer que les messages in-app sont à la fois demandés par le SDK et renvoyés par les serveurs Braze.

#### Vérifier si les messages sont demandés et renvoyés {#check-if-messages-are-requested-and-returned}

1. Ajoutez-vous en tant qu'[utilisateur test]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) sur le tableau de bord.
2. Configurez une campagne de messages in-app ciblant votre utilisateur.
3. Assurez-vous qu'une nouvelle session se produit dans votre application.
4. Utilisez le [journal des événements utilisateurs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) pour vérifier que votre appareil demande des messages in-app au démarrage de la session. Recherchez la requête SDK associée à l'événement de démarrage de session de votre utilisateur test.
  - Si votre application devait demander des messages in-app déclenchés, vous devriez voir `trigger` dans le champ **Requested Responses** sous **Response Data**.
  - Si votre application devait demander des messages in-app originaux, vous devriez voir `in_app` dans le champ **Requested Responses** sous **Response Data**.
5. Utilisez le [journal des événements utilisateurs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) pour vérifier si les messages in-app corrects sont renvoyés dans les données de réponse.<br>![Entrées du journal des événements utilisateurs pour les requêtes de messages in-app.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Résoudre les problèmes de messages non demandés {#troubleshoot-messages-not-being-requested}

Si vos messages in-app ne sont pas demandés, votre application ne suit peut-être pas correctement les sessions, car les messages in-app sont actualisés au démarrage de la session. Assurez-vous également que votre application démarre effectivement une session en fonction de la sémantique de délai d'expiration de session de votre application :

![La requête SDK trouvée dans le journal des événements utilisateurs affichant un événement de démarrage de session réussi.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### Résoudre les problèmes de messages non renvoyés {#troubleshoot-messages-not-being-returned}

Si vos messages in-app ne sont pas renvoyés, vous rencontrez probablement un problème de ciblage de campagne :

- Votre Segment ne contient pas votre utilisateur.
  - Vérifiez l'onglet [**Engagement**]({{ site.baseurl }}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) de votre utilisateur pour voir si le bon Segment apparaît sous **Segments**.
- Votre utilisateur a déjà reçu le message in-app et n'était pas rééligible pour le recevoir à nouveau.
  - Vérifiez les [paramètres de rééligibilité de la campagne]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) à l'étape **Distribution** du **Campaign Composer** et assurez-vous que les paramètres de rééligibilité correspondent à votre configuration de test.
- Votre utilisateur a atteint la limite de fréquence pour la campagne.
  - Vérifiez les [paramètres de limite de fréquence]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) de la campagne et assurez-vous qu'ils correspondent à votre configuration de test.
- S'il y avait un groupe de contrôle sur la campagne, votre utilisateur est peut-être tombé dans le groupe de contrôle.
  - Vous pouvez vérifier si c'est le cas en créant un Segment avec un filtre de variante de campagne reçue, où la variante de campagne est définie sur **Control**, et en vérifiant si votre utilisateur est tombé dans ce Segment.
  - Lors de la création de Campaigns à des fins de tests d'intégration, assurez-vous de ne pas ajouter de groupe de contrôle.

### Affichage des messages in-app {#troubleshooting-in-app-message-display}

Si votre application demande et reçoit correctement les messages in-app mais qu'ils ne s'affichent pas, une logique côté appareil peut empêcher l'affichage :

- Les messages in-app déclenchés sont limités en débit en fonction de l'[intervalle de temps minimum entre les déclencheurs]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/in-app_message_delivery#minimum-time-interval-between-triggers), qui est par défaut de 30 secondes.
- Si vous avez défini un délégué pour personnaliser la gestion des messages in-app, vérifiez votre délégué pour vous assurer qu'il n'affecte pas l'affichage des messages in-app.
- Les échecs de téléchargement d'images empêcheront les messages in-app contenant des images de s'afficher. Les téléchargements d'images échoueront systématiquement si le framework `SDWebImage` n'est pas correctement intégré. Vérifiez les journaux de votre appareil pour vous assurer que les téléchargements d'images n'échouent pas.
- Si l'orientation de l'appareil ne correspondait pas à l'orientation spécifiée par le message in-app, le message in-app ne s'affichera pas. Assurez-vous que votre appareil est dans la bonne orientation.