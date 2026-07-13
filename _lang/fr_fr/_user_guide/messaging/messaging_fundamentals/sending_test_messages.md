---
nav_title: Envoyer des messages de test
article_title: Envoyer des messages de test
page_order: 11.5
tool:
  - Campaigns
  - Canvas
page_type: reference
description: "Cet article de référence explique comment envoyer des messages de test sur les différents canaux de Braze et comment intégrer des propriétés d'événement personnalisées ou des attributs utilisateur."
---

# Envoyer des messages de test {#send-test-messages}

> Avant d'envoyer une campagne de communication à vos utilisateurs, nous vous recommandons, en tant que bonne pratique, de la tester pour vous assurer qu'elle s'affiche correctement et fonctionne comme prévu. Vous pouvez créer et envoyer des messages de test à des appareils ou des membres de votre équipe sélectionnés à l'aide des outils du tableau de bord de Braze.

{% alert important %}
Assurez-vous d'enregistrer le brouillon de votre campagne après les tests pour éviter de supprimer votre campagne. Vous pouvez envoyer des messages de test sans enregistrer le message en tant que brouillon.
{% endalert %}

## Étape 1 : Identifier vos utilisateurs test {#step-1-identify-your-test-users}

Avant de tester votre campagne de communication, il est important d'identifier vos utilisateurs test. Ces utilisateurs peuvent être des ID utilisateur ou des adresses e-mail existants, ou de nouveaux utilisateurs utilisés exclusivement pour tester les campagnes de communication.

### Facultatif : Créer un groupe de test de contenu {#optional-create-a-content-test-group}

Un moyen pratique d'organiser vos utilisateurs test est de créer un [groupe de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), qui comprend un groupe d'utilisateurs qui recevront des messages de test provenant de campagnes. Vous pouvez ajouter ce groupe de test au champ **Add Content Test Groups** sous **Test Recipients** dans votre campagne, et lancer vos tests sans créer ni ajouter d'utilisateurs test individuels.

## Étape 2 : Envoyer des messages de test spécifiques au canal {#step-2-send-channel-specific-test-messages}

Pour les étapes d'envoi de messages de test, consultez la section suivante correspondant à votre canal.

{% tabs local %}
{% tab Bannières %}

{% alert important %}
Avant de pouvoir tester des messages de type bannière dans Braze, vous devez créer une campagne de type bannière dans Braze. De plus, vérifiez que l'emplacement que vous souhaitez tester est déjà [intégré dans votre application ou site web]({{site.baseurl}}/developer_guide/banners/placements).
{% endalert %}

Après avoir créé votre message de type bannière, vous pouvez prévisualiser votre bannière ou envoyer un message de test.

1. Rédigez votre message de type bannière.
2. Sélectionnez **Preview** pour prévisualiser votre bannière ou envoyer un message de test.
3. Pour envoyer un message de test, ajoutez un groupe de test de contenu ou un ou plusieurs utilisateurs individuels en tant que **Test Recipients**, puis sélectionnez **Send Test**.

Vous pourrez visualiser votre message de test sur l'appareil pendant 5 minutes maximum.

![Onglet de prévisualisation du compositeur de bannière.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Gardez à l'esprit que votre prévisualisation peut ne pas être identique au rendu final sur l'appareil d'un utilisateur en raison de différences matérielles.
{% endalert %}

### Liste de vérification du test {#test-checklist}

- Votre campagne de type bannière est-elle assignée à un emplacement ?
- Les images et médias s'affichent-ils et fonctionnent-ils comme prévu sur vos types d'appareils et tailles d'écran ciblés ?
- Vos liens et boutons dirigent-ils l'utilisateur vers la bonne destination ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une valeur d'attribut par défaut au cas où le Liquid ne renverrait aucune information ?
- Votre texte est-il clair, concis et correct ?

{% endtab %}
{% tab Content Card %}

{% alert important %}
Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou à des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test avec des jetons de notification push valides enregistrés pour l'utilisateur test avant l'envoi. Pour les utilisateurs iOS, vous devez appuyer sur la notification push envoyée par Braze pour afficher la Content Card de test. Ce comportement s'applique uniquement aux Content Cards de test.
{% endalert %}

Les Content Cards de test sont envoyées via une notification push. La carte est intégrée dans le payload de la notification push, et le SDK l'extrait et la met en cache localement lorsque la notification push est reçue.

Ce processus contourne le système de distribution normal des cartes, c'est pourquoi les notifications push doivent être activées même si vous testez une Content Card.

Les Content Cards de test expirent environ cinq minutes après leur envoi.

Après avoir créé votre Content Card, vous pouvez envoyer une Content Card de test à votre application pour voir à quoi elle ressemblera en temps réel.

1. Rédigez votre Content Card.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.
3. Sélectionnez **Send Test** pour envoyer votre Content Card à votre application.

![Content Card de test]({% image_buster /assets/img/contentcard_test.png %})

### Prévisualisation {#preview}

Vous pouvez prévisualiser votre carte pendant sa rédaction dans l'onglet **Preview**. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de votre utilisateur.

{% alert note %}
Dans l'onglet **Preview** de votre compositeur, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous recommandons toujours d'envoyer un message de test à un appareil pour vous assurer que vos médias, textes, personnalisations et attributs personnalisés s'affichent correctement.
{% endalert %}

### Liste de vérification du test

- Votre utilisateur test est-il inscrit aux notifications push avec un jeton de notification push valide ?
- Les images et médias s'affichent-ils et fonctionnent-ils comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-attribute-values) si le Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos liens dirigent-ils l'utilisateur vers la bonne destination ?
- Votre utilisateur test est-il inscrit aux notifications push avec un jeton de notification push valide ?

### Résolution des problèmes d'images cassées {#troubleshooting-broken-images}

Si une image de Content Card ne s'affiche pas ou apparaît cassée :

- **Vérifiez que l'URL est correcte et encodée :** Les caractères spéciaux dans l'URL (tels que les espaces ou les paramètres de requête) doivent être correctement encodés. Sinon, la requête d'image échoue.
- **Vérifiez les politiques de sécurité du contenu :** Si votre organisation dispose d'une politique de sécurité du contenu (CSP) ou de règles de sécurité informatique internes, la politique peut bloquer le domaine de l'image. Confirmez que le domaine de l'URL de l'image est autorisé par votre CSP.
- **Utilisez HTTPS :** Les URL d'images doivent utiliser `https://` plutôt que `http://` pour éviter le blocage de contenu mixte dans les navigateurs et les applications.
- **Ouvrez l'URL directement dans un navigateur :** Si l'image ne se charge pas dans un navigateur, le problème vient de l'URL de l'image ou de l'hébergement, pas de Braze.

### Débogage {#debug}

Après l'envoi de vos Content Cards, vous pouvez analyser ou déboguer tout problème depuis le [journal des événements utilisateur]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) dans la console de développement.

Un cas d'usage courant consiste à essayer de déboguer pourquoi un utilisateur ne peut pas voir une Content Card particulière. Pour ce faire, vous pouvez consulter les **journaux des événements utilisateur** pour les Content Cards envoyées au SDK au démarrage de la session, mais avant une impression, et les relier à une campagne spécifique :

1. Allez dans **Settings** > **Event User Log**.
2. Localisez et développez la requête SDK pour votre utilisateur test.
3. Cliquez sur **Raw Data**.
4. Trouvez l'`id` de votre session. Voici un exemple d'extrait :

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

{: start="5"}
5. Utilisez un outil de décodage comme [Base64 Decode and Encode](https://www.base64decode.org/) pour décoder l'`id` au format Base64 et trouver le `campaign_id` associé. Dans notre exemple, cela donne le résultat suivant :

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Où `4861692e-6fce-4215-bd05-3254fb9e9057` est le `campaign_id`.<br><br>

6. Allez sur la page **Campaigns** et recherchez le `campaign_id`.

![Recherche du campaign_id sur la page Campaigns]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

À partir de là, vous pouvez examiner les paramètres et le contenu de votre message pour déterminer pourquoi un utilisateur ne peut pas voir une Content Card particulière.

{% endtab %}
{% tab E-mail %}

1. Rédigez votre e-mail.
2. Sélectionnez **Preview and Test**.
3. Sélectionnez l'onglet **Test Send** et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Add individual users**.
4. Sélectionnez **Send Test** pour envoyer votre e-mail rédigé dans votre boîte de réception.

![E-mail de test]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

Si votre campagne d'e-mail contient une image de grande taille et ne s'affiche pas comme prévu dans Outlook, envisagez de réduire les dimensions réelles du fichier image avec un outil d'édition ou de redimensionnement d'image au lieu de simplement la redimensionner avec du CSS ou du HTML.

{% endtab %}
{% tab Message in-app %}

{% alert warning %}
Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou à des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test avant l'envoi. Par exemple, vous devez avoir les notifications push activées sur votre appareil iOS pour pouvoir appuyer sur la notification avant que le message de test ne s'affiche. {% endalert %}

Si vous avez configuré les notifications push dans votre application et sur votre appareil de test, vous pouvez envoyer des messages in-app de test à votre application pour voir à quoi ils ressemblent en temps réel.

1. Rédigez votre message in-app.
2. Sélectionnez l'onglet **Test** et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Add Individual Users**.
3. Sélectionnez **Send Test** pour envoyer votre notification push à votre appareil.

Une notification push de test apparaîtra en haut de l'écran de votre appareil.

![Message in-app de test]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Les envois de test peuvent entraîner l'envoi de plusieurs messages in-app à chaque destinataire.
{% endalert %}

En cliquant directement sur la notification push et en l'ouvrant, vous serez redirigé vers votre application, où vous pourrez visualiser votre message in-app de test. Notez que cette fonctionnalité de test de message in-app repose sur le fait que l'utilisateur clique sur une notification push de test pour déclencher le message in-app. Par conséquent, l'utilisateur doit être éligible pour recevoir des notifications push dans l'application concernée pour que la notification push de test soit correctement envoyée.

### Prévisualisation

Vous pouvez prévisualiser votre message in-app pendant sa rédaction dans l'onglet **Preview**. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de votre utilisateur. Vous pouvez prévisualiser l'apparence de votre message pour un utilisateur aléatoire, un utilisateur spécifique ou un utilisateur personnalisé. Vous pouvez également prévisualiser les messages pour les appareils mobiles ou les tablettes.

![Onglet de rédaction lors de la création d'un message in-app montrant la prévisualisation de l'apparence du message. Aucun utilisateur n'est sélectionné, donc le Liquid ajouté dans la section du corps s'affiche tel quel.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze propose trois générations de messages in-app. Vous pouvez affiner les appareils auxquels vos messages doivent être envoyés, en fonction de la génération qu'ils prennent en charge.

![Basculement entre les générations lors de la prévisualisation d'un message in-app.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
Dans la **prévisualisation**, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous recommandons toujours d'envoyer un message de test à un appareil pour vous assurer que vos médias, textes, personnalisations et attributs personnalisés s'affichent correctement.
{% endalert %}

### Liste de vérification du test

- Les images et médias s'affichent-ils et fonctionnent-ils comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-attribute-values) si le Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos boutons dirigent-ils l'utilisateur vers la bonne destination ?

### Scanner d'accessibilité {#accessibility-scanner}

Pour soutenir les bonnes pratiques d'accessibilité, Braze analyse automatiquement le contenu des messages in-app créés à l'aide de l'éditeur HTML traditionnel par rapport aux normes d'accessibilité. Ce scanner aide à identifier le contenu qui pourrait ne pas respecter les directives pour l'accessibilité des contenus web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). Les WCAG sont un ensemble de normes techniques internationalement reconnues, développées par le World Wide Web Consortium (W3C), pour rendre le contenu web plus accessible aux personnes en situation de handicap.

![Résultats de l'analyse d'accessibilité]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
Le scanner d'accessibilité des messages in-app ne fonctionne que sur les messages créés avec du HTML personnalisé.
{% endalert %}

#### Fonctionnement {#how-it-works}

Le scanner s'exécute automatiquement sur les messages HTML personnalisés et évalue l'intégralité de votre message HTML par rapport à l'ensemble complet des [règles WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Pour chaque problème signalé, il affiche :

- L'élément HTML spécifique concerné
- Une description du problème d'accessibilité
- Un lien vers des informations complémentaires ou des conseils de remédiation

#### Comprendre les tests d'accessibilité automatisés {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Créez votre message LINE.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.
3. Sélectionnez **Send Test** pour envoyer votre message.

![Message LINE de test.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Push mobile {#mobile-push}

1. Rédigez votre notification push mobile.
2. Sélectionnez l'onglet **Test** et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Add Individual Users**.
3. Sélectionnez **Send Test** pour envoyer votre message rédigé à votre appareil.

![Notification push de test]({% image_buster /assets/img_archive/testpush.png %})

Si vous voyez une erreur indiquant qu'aucun des utilisateurs sélectionnés n'a de jeton de notification push correspondant, l'utilisateur test ne dispose pas d'un jeton de notification push valide pour la plateforme sélectionnée. L'utilisateur doit avoir démarré une session dans l'application et activé les notifications push pour cet appareil. Pour plus d'informations, consultez [Activation des notifications push et états d'abonnement push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

#### Push web {#web-push}

1. Créez votre notification push web.
2. Sélectionnez l'onglet **Test**.
3. Sélectionnez **Send Test to Myself**.
4. Sélectionnez **Send Test** pour envoyer votre notification push web à votre navigateur web.

![Notification push web de test]({% image_buster /assets/img_archive/testwebpush.png %})

Si vous avez déjà accepté les notifications push depuis le tableau de bord de Braze, le message s'affiche dans le coin de votre écran. Sinon, sélectionnez **Allow** lorsque vous y êtes invité, et le message s'affichera.

Si vous voyez une erreur indiquant qu'aucun des utilisateurs sélectionnés n'a de jeton de notification push correspondant pour les notifications push web, vérifiez que l'utilisateur test dispose d'un jeton de notification push valide enregistré pour la plateforme sélectionnée. Pour recevoir un jeton de notification push, l'utilisateur doit être configuré pour recevoir des notifications push pour l'application sur son appareil. Pour plus de détails, consultez [Activation des notifications push et états d'abonnement push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

{% endtab %}
{% tab SMS/MMS et RCS %}

Après avoir créé votre message SMS, MMS ou RCS, vous pouvez envoyer un message de test à votre téléphone pour voir à quoi il ressemblera en temps réel.

1. Rédigez votre message SMS, MMS ou RCS.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.
3. Sélectionnez **Send Test** pour envoyer votre message de test.

![Message SMS de test]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Après avoir créé votre webhook, vous pouvez effectuer un envoi de test pour vérifier la réponse du webhook. Sélectionnez l'onglet **Test** et sélectionnez **Send Test** pour envoyer un test à l'URL du webhook fournie. Vous pouvez également sélectionner un utilisateur individuel pour prévisualiser la réponse en tant qu'utilisateur spécifique.

{% endtab %}
{% tab WhatsApp %}

1. Créez votre message WhatsApp.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.
3. Initiez une fenêtre de conversation en envoyant un message WhatsApp au numéro de téléphone associé au groupe d'abonnement que vous utilisez pour ce message. Le numéro de téléphone associé est indiqué dans l'alerte de l'onglet **Test**.
4. Sélectionnez **Send Test** pour envoyer votre message.

![Message WhatsApp de test.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Tester des campagnes personnalisées {#test-personalized-campaigns}

Si vous testez des campagnes qui utilisent des données utilisateur ou des propriétés d'événement personnalisées, vous devrez suivre des étapes supplémentaires ou différentes.

### Tester des campagnes personnalisées avec des attributs utilisateur {#testing-campaigns-personalized-with-user-attributes}

Si vous utilisez la [personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/overview) dans votre message, vous devrez suivre des étapes supplémentaires pour prévisualiser correctement votre campagne et vérifier que les données utilisateur remplissent correctement le contenu.

Lors de l'envoi d'un message de test, assurez-vous de choisir l'option **Select Existing User** ou de prévisualiser en tant que **Custom User**.

![Test d'un message personnalisé]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Sélectionner un utilisateur existant {#selecting-an-existing-user}

Si vous sélectionnez un utilisateur existant, saisissez l'ID utilisateur ou l'adresse e-mail spécifique dans le champ de recherche. Ensuite, utilisez la prévisualisation du tableau de bord pour voir comment votre message apparaîtrait à cet utilisateur, et envoyez un message de test à votre appareil qui reflète ce que cet utilisateur verrait.

![Sélectionner un utilisateur]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Sélectionner un utilisateur personnalisé {#selecting-a-custom-user}

Si vous prévisualisez en tant qu'utilisateur personnalisé, saisissez du texte pour les différents champs disponibles pour la personnalisation, tels que le prénom de l'utilisateur et les attributs personnalisés. Encore une fois, vous pouvez saisir votre propre adresse e-mail pour envoyer un test à votre appareil.

![Utilisateur personnalisé]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Personnaliser un utilisateur existant {#customizing-an-existing-user}

Vous pouvez modifier des champs individuels d'un utilisateur aléatoire ou existant pour tester le contenu dynamique de votre message. Sélectionnez **Edit** pour convertir l'utilisateur sélectionné en un utilisateur personnalisé que vous pouvez modifier.

![L'onglet « Preview as a User » avec un bouton « Edit ».]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Tester des campagnes personnalisées avec des propriétés d'événement personnalisées {#testing-campaigns-personalized-with-custom-event-properties}

Le test de campagnes personnalisées avec des [propriétés d'événement personnalisées]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) diffère légèrement du test d'autres types de campagnes décrits précédemment.

{% tabs local %}
{% tab Déclenchement manuel %}

#### Méthode 1 : Déclencher la campagne manuellement {#method-1-triggering-campaign-manually}

Vous pouvez déclencher la campagne vous-même comme méthode robuste pour tester les campagnes personnalisées utilisant des propriétés d'événement personnalisées :

1. Rédigez le texte incluant la propriété d'événement.

![Rédaction d'un message de test avec des propriétés]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Utilisez la [livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) pour envoyer la campagne lorsque l'événement se produit.

{% alert note %}
Si vous testez une campagne push iOS, vous devez définir le délai à une minute pour vous laisser le temps de quitter l'application, car iOS n'envoie pas de notifications push pour l'application actuellement ouverte. Les autres types de campagnes peuvent être configurés pour un envoi immédiat.
{% endalert %}

![Envoi du message de test]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Ciblez les utilisateurs comme vous le feriez pour un test en utilisant un filtre de test ou en ciblant votre propre adresse e-mail, et terminez la création de la campagne.

![Ciblage du message de test]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Accédez à votre application et effectuez l'événement personnalisé.

La campagne se déclenchera et affichera le message personnalisé avec la propriété d'événement.

![Exemple de message de test]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Message de test %}

#### Méthode 2 : S'envoyer un message de test {#method-2-sending-yourself-a-test-message}

Alternativement, si vous enregistrez des ID utilisateur personnalisés, vous pouvez également tester la campagne en vous envoyant un message de test personnalisé.

1. Rédigez le texte de votre campagne.
2. Sélectionnez l'onglet **Test** et choisissez **Customized User**.
3. Ajoutez la propriété d'événement personnalisée en bas de la page, et ajoutez votre ID utilisateur ou adresse e-mail dans le champ supérieur.
4. Sélectionnez **Send Test** pour recevoir un message personnalisé avec la propriété.

![Test avec un utilisateur personnalisé]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Méthode 3 : Utiliser Liquid {#method-3-using-liquid}

Vous pouvez tester les propriétés d'événement personnalisées en saisissant manuellement des valeurs avec Liquid.

1. Dans l'éditeur de message, saisissez les valeurs de vos propriétés d'événement personnalisées.
2. Sélectionnez l'onglet **Preview as a User** pour vérifier que le message correct s'affiche.

{% endtab %}
{% endtabs %}

## Limitations {#limitations}

Il existe quelques situations où les messages de test ne se comportent pas de la même manière que les campagnes ou Canvas envoyés à de vrais utilisateurs. Dans ces cas, envisagez de lancer la campagne ou le Canvas à un ensemble limité d'utilisateurs test pour valider ce comportement.

- L'affichage du centre de préférences de Braze à partir de messages de test rendra le bouton **Save Preferences** grisé.
- Pour tester les messages in-app et les Content Cards, l'utilisateur cible doit disposer d'un jeton de notification push pour l'appareil cible.
- Pour tester les liens de désabonnement dans les e-mails, assurez-vous que l'adresse e-mail de votre utilisateur test se trouve dans l'espace de travail correspondant.
- L'en-tête `List-Unsubscribe` n'est pas inclus dans les e-mails envoyés par la fonctionnalité de message de test.
- Les e-mails envoyés aux utilisateurs du groupe initiateur ne mettent pas à jour la liste des campagnes reçues du profil utilisateur et n'incrémentent pas les envois dans l'analytique du tableau de bord.

## Résolution des problèmes {#troubleshooting}

### Messages in-app {#in-app-messages}

Si votre campagne de message in-app n'est pas déclenchée par une campagne push, vérifiez la segmentation de la campagne in-app pour confirmer que l'utilisateur correspond à l'audience cible **avant** de recevoir le message push.

Pour les envois de test sur Android et iOS, les messages in-app qui utilisent le comportement au clic **Request push permission** peuvent ne pas s'afficher sur certains appareils. En guise de solution de contournement :
- **Android :** Les appareils doivent être sous Android 13 et utiliser la version 21.0.0 de notre SDK Android. Une autre raison peut être que l'appareil sur lequel le message in-app est affiché dispose déjà d'une invite au niveau du système. Vous avez peut-être sélectionné **Do not ask again**, vous devrez donc peut-être réinstaller l'application pour réinitialiser les autorisations de notification avant de tester à nouveau.
- **iOS :** Nous recommandons à votre équipe de développement de vérifier l'implémentation des notifications push pour votre application et de supprimer manuellement tout code qui demanderait les autorisations push. Pour plus d'informations, consultez [Messages in-app d'amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices).

Pour qu'une campagne de message in-app basée sur une action soit envoyée, vous devez enregistrer les événements personnalisés via le SDK de Braze, et non via les REST API, afin que les utilisateurs puissent recevoir les messages in-app éligibles directement sur leur appareil. Les utilisateurs reçoivent le message in-app s'ils effectuent l'événement pendant la session.