---
nav_title: "Boutons d'action push"
article_title: "Boutons d'action push"
page_order: 1
page_type: reference
description: "Cet article de référence explique ce que sont les boutons d'action push et les différences entre les plateformes iOS et Android."
channel:
  - Push

---

# Boutons d'action push {#push-action-buttons}

> Les boutons d'action push vous permettent de définir du contenu et des actions pour les boutons lors de l'utilisation des notifications push iOS et Android de Braze. Grâce aux boutons d'action, vos utilisateurs peuvent interagir directement avec votre application depuis une notification sans avoir à ouvrir l'expérience sur l'application.

![Une notification push iOS avec deux boutons d'action push : Accepter et Refuser.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

## Créer des boutons d'action {#creating-action-buttons}

Chaque bouton interactif peut renvoyer vers une page web, un lien profond ou ouvrir l'application.

- Pour les Campaigns push standard, vous pouvez spécifier vos boutons d'action push dans la section **On-Click Behavior** du compositeur de messages push dans le tableau de bord.
- Pour les [Campaigns push multiplateformes]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push), les boutons d'action peuvent être configurés séparément pour chaque plateforme sous l'onglet **Paramètres**.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Pour utiliser les boutons d'action dans vos messages push iOS, procédez comme suit :

1. Activez les boutons d'action dans l'onglet **Rédiger**.
2. Sélectionnez votre **iOS Notification Category** parmi les combinaisons de boutons disponibles suivantes :
 - Accept / Decline
 - Yes / No
 - Confirm / Cancel
 - More
 - Pre-registered custom iOS Category

![Menu déroulant iOS Notification Category.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
En raison de la gestion des boutons par iOS, vous devez effectuer des étapes d'intégration supplémentaires lors de la configuration des boutons d'action push, qui sont décrites dans notre [documentation développeur]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=swift#swift_customizing-push-categories). En particulier, vous devez soit configurer les catégories iOS, soit sélectionner certaines options de boutons par défaut. Pour les intégrations Android, ces boutons fonctionnent automatiquement.
{% endalert %}

Les paires prédéfinies telles que **Yes** / **No** associent le deuxième bouton à une action de fermeture (**CLOSE**) par défaut, de sorte qu'il n'ouvre pas l'application de la même manière que le premier bouton. Les **_Ouvertures directes_** n'incluent pas ce type d'appui, mais les données **Push Notification Open** dans Currents ou Snowflake peuvent tout de même l'enregistrer avec `button_action_type` et `button_string`. Pour en savoir plus, consultez [Boutons d'action push et reporting]({{site.baseurl}}/user_guide/channels/push/reporting#push-action-buttons-and-reporting).
{% endtab %}
{% tab Android %}
### Android {#android}

Pour utiliser les boutons d'action dans vos messages push Android, procédez comme suit :

1. Activez les boutons d'action dans l'onglet **Rédiger**.
2. Sélectionnez <i class="fas fa-plus-circle"></i> **Add Button** et spécifiez le texte de votre bouton ainsi que le **On-Click Behavior**. Vous pouvez choisir parmi les actions disponibles suivantes :
  - Open App
  - Redirect to Web URL
  - [Lien profond]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) vers l'application

![Sélection de « Open App » comme comportement au clic pour un bouton de notification.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Vous pouvez ajouter jusqu'à trois boutons dans votre notification push.

#### Limites de caractères Android {#android-character-limits}

Contrairement aux boutons iOS, qui sont empilés, les boutons Android sont affichés côte à côte sur une même ligne. Cela signifie que plus vous ajoutez de boutons (jusqu'à trois), moins vous disposez d'espace pour le texte des boutons.

![Boutons d'action push Android avec du texte tronqué.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

Le tableau suivant indique le nombre de caractères que vous pouvez ajouter avant que le texte de votre bouton ne soit tronqué, en fonction du nombre de boutons :

| Nombre de boutons | Nombre maximum de caractères par bouton |
| --- | --- |
| 1 | 46 caractères |
| 2 | 20 caractères |
| 3 | 11 caractères |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de caractères Android" }
{% endtab %}
{% endtabs %}