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

Avant de tester votre campagne de communication, il est important d'identifier vos utilisateurs test. Ces utilisateurs peuvent être des ID utilisateur existants ou des adresses e-mail, ou bien de nouveaux utilisateurs utilisés exclusivement pour tester les campagnes de communication.

### Facultatif : Créer un groupe de test de contenu {#optional-create-a-content-test-group}

Un moyen pratique d'organiser vos utilisateurs test est de créer un [groupe de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), qui comprend un groupe d'utilisateurs qui recevront des messages de test provenant de Campaigns. Vous pouvez ajouter ce groupe de test au champ **Add Content Test Groups** sous **Test Recipients** dans votre campagne, et lancer vos tests sans avoir à créer ou ajouter des utilisateurs test individuels.

## Étape 2 : Envoyer des messages de test spécifiques à chaque canal {#step-2-send-channel-specific-test-messages}

Pour connaître les étapes d'envoi des messages de test, consultez la section ci-dessous correspondant à votre canal.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Avant de pouvoir tester les messages Banner dans Braze, vous devrez créer une campagne Banner dans Braze. De plus, vérifiez que l'emplacement que vous souhaitez tester est déjà [intégré dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements).
{% endalert %}

Après avoir créé votre message Banner, vous pouvez prévisualiser votre Banner ou envoyer un message de test.

1. Rédigez votre message Banner.
2. Sélectionnez **Preview** pour prévisualiser votre Banner ou envoyer un message de test.
3. Pour envoyer un message de test, ajoutez un groupe de test de contenu ou un ou plusieurs utilisateurs individuels en tant que **Test Recipients**, puis sélectionnez **Send Test**.

Vous pourrez consulter votre message de test sur l'appareil pendant 5 minutes maximum.

![Onglet de prévisualisation du composeur de Banner.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Gardez à l'esprit que votre prévisualisation peut ne pas être identique au rendu final sur l'appareil d'un utilisateur en raison des différences matérielles.
{% endalert %}

### Liste de vérification pour les tests {#test-checklist}

- Votre campagne Banner est-elle associée à un emplacement ?
- Les images et médias s'affichent-ils et fonctionnent-ils comme prévu sur vos types d'appareils et tailles d'écran ciblés ?
- Vos liens et boutons dirigent-ils l'utilisateur vers la bonne destination ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une valeur d'attribut par défaut au cas où le Liquid ne renverrait aucune information ?
- Votre texte est-il clair, concis et correct ?

{% endtab %}
{% tab Content Card %}

{% alert important %}
Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou à des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test avec des jetons push valides enregistrés pour l'utilisateur test avant l'envoi. Pour les utilisateurs iOS, vous devez appuyer sur la notification push envoyée par Braze pour afficher la Content Card de test. Ce comportement s'applique uniquement aux Content Cards de test.
{% endalert %}

Les Content Cards de test sont envoyées via une notification push. La carte est intégrée dans le payload push, et le SDK l'extrait et la met en cache localement lorsque la notification push est reçue.

Ce processus contourne le système de distribution normal des cartes, c'est pourquoi les notifications push doivent être activées même si vous testez une Content Card.

Les Content Cards de test expirent environ cinq minutes après leur envoi.

Après avoir créé votre Content Card, vous pouvez envoyer une Content Card de test à votre application pour voir à quoi elle ressemble en temps réel.

1. Rédigez votre Content Card.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.
3. Sélectionnez **Send Test** pour envoyer votre Content Card à votre application.

![Content Card de test]({% image_buster /assets/img/contentcard_test.png %})

### Prévisualisation {#preview}

Vous pouvez prévisualiser votre carte pendant que vous la composez dans l'onglet **Preview**. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de votre utilisateur.

{% alert note %}
Dans l'onglet **Preview** de votre composeur, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous recommandons de toujours envoyer un message de test à un appareil pour vous assurer que vos médias, votre texte, votre personnalisation et vos attributs personnalisés s'affichent correctement.
{% endalert %}

### Liste de vérification pour les tests

- Votre utilisateur test a-t-il activé les notifications push avec un jeton push valide ?
- Les images et médias s'affichent-ils et fonctionnent-ils comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) au cas où le Liquid ne renverrait aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos liens dirigent-ils l'utilisateur vers la bonne destination ?
- Votre utilisateur test a-t-il activé les notifications push avec un jeton push valide ?

### Résolution des problèmes d'images défectueuses {#troubleshooting-broken-images}

Si une image de Content Card ne s'affiche pas ou apparaît cassée :

- **Vérifiez que l'URL est correcte et encodée :** les caractères spéciaux dans l'URL (tels que les espaces ou les paramètres de requête) doivent être correctement encodés. Sinon, la requête d'image échoue.
- **Vérifiez les politiques de sécurité du contenu :** si votre organisation dispose d'une politique de sécurité du contenu (CSP) ou de règles de sécurité informatique internes, la politique peut bloquer le domaine de l'image. Confirmez que le domaine de l'URL de l'image est autorisé par votre CSP.
- **Utilisez HTTPS :** les URL d'images doivent utiliser `https://` plutôt que `http://` pour éviter le blocage de contenu mixte dans les navigateurs et les applications.
- **Ouvrez l'URL directement dans un navigateur :** si l'image ne se charge pas dans un navigateur, le problème vient de l'URL de l'image ou de l'hébergement, et non de Braze.

### Débogage {#debug}

Après l'envoi de vos Content Cards, vous pouvez analyser ou déboguer les problèmes éventuels depuis le [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) dans la console de développement.

Un cas d'usage courant consiste à comprendre pourquoi un utilisateur ne peut pas voir une Content Card particulière. Pour ce faire, vous pouvez consulter les **Event User Logs** pour les Content Cards envoyées au SDK au démarrage de la session, mais avant une impression, et les relier à une campagne spécifique :

1. Accédez à **Settings** > **Event User Log**.
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
5. Utilisez un outil de décodage tel que [Base64 Decode and Encode](https://www.base64decode.org/) pour décoder l'`id` depuis le format Base64 et trouver le `campaign_id` associé. Dans notre exemple, cela donne le résultat suivant :

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Où `4861692e-6fce-4215-bd05-3254fb9e9057` est le `campaign_id`.<br><br>

6. Accédez à la page **Campaigns** et recherchez le `campaign_id`.

![Recherche du campaign_id sur la page Campaigns]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

À partir de là, vous pouvez examiner les paramètres et le contenu de votre message pour déterminer pourquoi un utilisateur ne peut pas voir une Content Card particulière.

{% endtab %}
{% tab E-mail %}

1. Rédigez votre e-mail.
2. Sélectionnez **Preview and Test**.
3. Sélectionnez l'onglet **Test Send** et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Add individual users**.
4. Sélectionnez **Send Test** pour envoyer votre e-mail rédigé à votre boîte de réception.

![E-mail de test]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

Si votre e-mail contient un lien vers un [centre de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center), les envois de test ne génèrent pas de lien fonctionnel et ne permettent pas d'enregistrer des préférences. Pour tester le centre de préférences, lancez le message à un utilisateur test ou à un petit Segment interne. Pour plus de détails, consultez [Tester les centres de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers).

Si votre campagne d'e-mails contient une image volumineuse qui ne s'affiche pas comme prévu dans Outlook, envisagez de réduire les dimensions réelles du fichier image avec un outil d'édition ou de redimensionnement d'image au lieu de simplement la redimensionner avec du CSS ou du HTML.

{% endtab %}
{% tab Message in-app %}

{% alert warning %}
Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou à des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test avant l'envoi. Par exemple, vous devez avoir activé les notifications push sur votre appareil iOS pour pouvoir appuyer sur la notification avant que le message de test ne s'affiche. {% endalert %}

Si vous avez configuré les notifications push dans votre application et sur votre appareil de test, vous pouvez envoyer des messages in-app de test à votre application pour voir à quoi ils ressemblent en temps réel.

1. Rédigez votre message in-app.
2. Sélectionnez l'onglet **Test** et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Add Individual Users**.
3. Sélectionnez **Send Test** pour envoyer votre notification push à votre appareil.

Une notification push de test apparaîtra en haut de l'écran de votre appareil.

![Message in-app de test]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Les envois de test peuvent entraîner l'envoi de plusieurs messages in-app à chaque destinataire.
{% endalert %}

En cliquant directement sur la notification push et en l'ouvrant, vous serez redirigé vers votre application où vous pourrez visualiser votre message in-app de test. Notez que cette fonctionnalité de test de messages in-app repose sur le fait que l'utilisateur clique sur une notification push de test pour déclencher le message in-app. L'utilisateur doit donc être éligible pour recevoir des notifications push dans l'application concernée pour que la notification push de test soit envoyée avec succès.

### Prévisualisation

Vous pouvez prévisualiser votre message in-app pendant que vous le composez dans l'onglet **Preview**. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de votre utilisateur. Vous pouvez prévisualiser ce à quoi votre message ressemblera pour un utilisateur aléatoire, un utilisateur spécifique ou un utilisateur personnalisé. Vous pouvez également prévisualiser les messages pour les appareils mobiles ou les tablettes.

![Onglet de composition lors de la création d'un message in-app montrant la prévisualisation de l'apparence du message. Aucun utilisateur n'est sélectionné, le Liquid ajouté dans le corps s'affiche donc tel quel.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze dispose de trois générations de messages in-app. Vous pouvez affiner les appareils auxquels vos messages doivent être envoyés, en fonction de la génération qu'ils prennent en charge.

![Basculer entre les générations lors de la prévisualisation d'un message in-app.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
Dans **Preview**, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous recommandons de toujours envoyer un message de test à un appareil pour vous assurer que vos médias, votre texte, votre personnalisation et vos attributs personnalisés s'affichent correctement.
{% endalert %}

### Liste de vérification pour les tests

- Les images et médias s'affichent-ils et fonctionnent-ils comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) au cas où le Liquid ne renverrait aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos boutons dirigent-ils l'utilisateur vers la bonne destination ?

### Analyseur d'accessibilité {#accessibility-scanner}

Pour respecter les bonnes pratiques d'accessibilité, Braze analyse automatiquement le contenu des messages in-app créés avec l'éditeur HTML traditionnel par rapport aux normes d'accessibilité. Cet analyseur permet d'identifier le contenu qui pourrait ne pas répondre aux normes des Règles pour l'accessibilité des contenus Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). Les WCAG sont un ensemble de normes techniques internationalement reconnues, développées par le World Wide Web Consortium (W3C), visant à rendre le contenu web plus accessible aux personnes en situation de handicap.

![Résultats de l'analyse d'accessibilité]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
L'analyseur d'accessibilité des messages in-app ne s'exécute que sur les messages créés avec du HTML personnalisé.
{% endalert %}

#### Fonctionnement {#how-it-works}

L'analyseur s'exécute automatiquement sur les messages HTML personnalisés et évalue l'intégralité de votre message HTML par rapport au [jeu de règles WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Pour chaque problème signalé, il affiche :

- L'élément HTML spécifique concerné
- Une description du problème d'accessibilité
- Un lien vers du contexte supplémentaire ou des conseils de remédiation

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

Si vous voyez une erreur indiquant qu'aucun des utilisateurs sélectionnés ne dispose de jetons push correspondants, l'utilisateur test ne possède pas de jeton push valide pour la plateforme sélectionnée. L'utilisateur doit avoir démarré une session dans l'application et activé les notifications push pour cet appareil. Pour plus d'informations, consultez [Activation des notifications push et abonnement push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

#### Push Web {#web-push}

1. Créez votre notification push Web.
2. Sélectionnez l'onglet **Test**.
3. Sélectionnez **Send Test to Myself**.
4. Sélectionnez **Send Test** pour envoyer votre notification push Web à votre navigateur.

![Notification push Web de test]({% image_buster /assets/img_archive/testwebpush.png %})

Si vous avez déjà accepté les notifications push du tableau de bord de Braze, le message s'affiche dans le coin de votre écran. Sinon, sélectionnez **Allow** lorsque vous y êtes invité, et le message s'affiche.

Si vous voyez une erreur indiquant qu'aucun des utilisateurs sélectionnés ne dispose de jetons push correspondants pour le push Web, vérifiez que l'utilisateur test dispose d'un jeton push valide enregistré pour la plateforme sélectionnée. Pour recevoir un jeton push, l'utilisateur doit être configuré pour recevoir des notifications push pour l'application sur son appareil. Pour plus de détails, consultez [Activation des notifications push et abonnement push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

{% endtab %}
{% tab SMS/MMS et RCS %}

Après avoir créé votre message SMS, MMS ou RCS, vous pouvez envoyer un message de test à votre téléphone pour voir à quoi il ressemble en temps réel. Le destinataire doit appartenir au groupe d'abonnement SMS que vous sélectionnez lors de l'envoi du test, disposer d'un numéro de téléphone valide et avoir au moins un pays sélectionné sous **Geographic Permissions**. Pour plus de détails, consultez la [FAQ SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages).

1. Rédigez votre message SMS, MMS ou RCS.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.
3. Sélectionnez **Send Test** pour envoyer votre message de test.

![Content Card de test]({% image_buster /assets/img/sms_test.png %})

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

Si vous testez des campagnes qui remplissent des données utilisateur ou qui utilisent des propriétés d'événement personnalisées, vous devrez suivre des étapes supplémentaires ou différentes.

### Tester des campagnes personnalisées avec des attributs utilisateur {#testing-campaigns-personalized-with-user-attributes}

Si vous utilisez la [personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) dans votre message, vous devrez suivre des étapes supplémentaires pour prévisualiser correctement votre campagne et vérifier que les données utilisateur remplissent correctement le contenu.

Lors de l'envoi d'un message de test, assurez-vous de choisir l'option **Select Existing User** ou de prévisualiser en tant que **Custom User**.

![Test d'un message personnalisé]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Sélectionner un utilisateur existant {#selecting-an-existing-user}

Si vous sélectionnez un utilisateur existant, saisissez l'ID utilisateur spécifique ou l'adresse e-mail dans le champ de recherche. Utilisez ensuite la prévisualisation du tableau de bord pour voir comment votre message apparaîtrait pour cet utilisateur, et envoyez un message de test à votre appareil qui reflète ce que cet utilisateur verrait.

![Sélectionner un utilisateur]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Sélectionner un utilisateur personnalisé {#selecting-a-custom-user}

Si vous prévisualisez en tant qu'utilisateur personnalisé, saisissez du texte pour les différents champs disponibles pour la personnalisation, tels que le prénom de l'utilisateur et les attributs personnalisés. Une fois encore, vous pouvez saisir votre propre adresse e-mail pour envoyer un test à votre appareil.

![Utilisateur personnalisé]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Personnaliser un utilisateur existant {#customizing-an-existing-user}

Vous pouvez modifier des champs individuels à partir d'un utilisateur aléatoire ou existant pour vous aider à tester le contenu dynamique dans votre message. Sélectionnez **Edit** pour convertir l'utilisateur sélectionné en un utilisateur personnalisé que vous pouvez modifier.

![L'onglet « Preview as a User » avec un bouton « Edit ».]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Tester des campagnes personnalisées avec des propriétés d'événement personnalisées {#testing-campaigns-personalized-with-custom-event-properties}

Le test de campagnes personnalisées avec des [propriétés d'événement personnalisées]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) diffère légèrement du test d'autres types de campagnes décrits ci-dessus.

{% tabs local %}
{% tab Déclencher manuellement %}

#### Méthode 1 : déclencher la campagne manuellement {#method-1-triggering-campaign-manually}

Vous pouvez déclencher la campagne vous-même, ce qui constitue un moyen robuste de tester les campagnes personnalisées utilisant des propriétés d'événement personnalisées :

1. Rédigez le contenu incluant la propriété d'événement.

![Rédaction d'un message de test avec des propriétés]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Utilisez la [livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) pour envoyer la campagne lorsque l'événement se produit.

{% alert note %}
Si vous testez une campagne de notification push iOS, vous devez définir le délai à une minute pour vous laisser le temps de quitter l'application, car iOS ne distribue pas les notifications push pour l'application actuellement ouverte. Les autres types de campagnes peuvent être configurés pour une distribution immédiate.
{% endalert %}

![Distribution du message de test]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Ciblez les utilisateurs comme vous le feriez pour un test en utilisant un filtre de test ou en ciblant votre propre adresse e-mail, puis terminez la création de la campagne.

![Ciblage du message de test]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Accédez à votre application et réalisez l'événement personnalisé.

La campagne se déclenchera et affichera le message personnalisé avec la propriété d'événement.

![Exemple de message de test]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Message de test %}

#### Méthode 2 : s'envoyer un message de test {#method-2-sending-yourself-a-test-message}

Sinon, si vous enregistrez des ID utilisateur personnalisés, vous pouvez également tester la campagne en vous envoyant un message de test personnalisé.

1. Rédigez le contenu de votre campagne.
2. Sélectionnez l'onglet **Test** et choisissez **Customized User**.
3. Ajoutez la propriété d'événement personnalisée en bas de la page, et ajoutez votre ID utilisateur ou votre adresse e-mail dans le champ en haut.
4. Sélectionnez **Send Test** pour recevoir un message personnalisé avec la propriété.

![Test en utilisant un utilisateur personnalisé]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Méthode 3 : utiliser Liquid {#method-3-using-liquid}

Vous pouvez tester les propriétés d'événement personnalisées en saisissant manuellement des valeurs avec Liquid.

1. Dans l'éditeur de messages, saisissez des valeurs pour vos propriétés d'événement personnalisées.
2. Sélectionnez l'onglet **Preview as a User** pour vérifier que le message correct s'affiche.

{% endtab %}
{% endtabs %}

## Limitations {#limitations}

Il existe quelques situations où les messages de test ne se comportent pas de la même manière que les Campaigns ou les Canvas envoyés à de vrais utilisateurs. Dans ces cas, envisagez de lancer la Campaign ou le Canvas auprès d'un ensemble limité d'utilisateurs test pour valider ce comportement.

- L'affichage du [centre de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) Braze à partir de messages de test entraîne la désactivation du bouton **Save Preferences**. Les étiquettes Liquid du centre de préférences peuvent également ne pas générer de liens valides. Il s'agit d'un comportement attendu. Pour tester de bout en bout, consultez [Tester les centres de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers).
- Pour tester les messages in-app et les Content Cards, l'utilisateur cible doit disposer d'un jeton de notification push pour l'appareil cible.
- Pour tester les liens de désabonnement dans les e-mails, assurez-vous que l'adresse e-mail de votre utilisateur test se trouve dans l'espace de travail correspondant.
- L'en-tête `List-Unsubscribe` n'est pas inclus dans les e-mails envoyés via la fonctionnalité de message de test.
- Les e-mails envoyés aux utilisateurs du groupe initiateur ne mettent pas à jour la liste des Campaigns reçues sur le profil utilisateur et n'incrémentent pas les envois dans l'analyse du tableau de bord.

## Résolution des problèmes {#troubleshooting}

### Messages in-app {#in-app-messages}

Si votre campagne de messages in-app n'est pas déclenchée par une campagne de notification push, vérifiez la segmentation de la campagne in-app pour confirmer que l'utilisateur correspond à l'audience cible **avant** de recevoir la notification push.

Pour les envois de test sur Android et iOS, les messages in-app qui utilisent le comportement au clic **Demander la permission push** peuvent ne pas s'afficher sur certains appareils. Voici des solutions de contournement :
- **Android :** Les appareils doivent fonctionner sous Android 13 et utiliser la version 21.0.0 de notre SDK Android. Une autre raison possible est que l'appareil sur lequel le message in-app est affiché possède déjà une invite au niveau du système. Vous avez peut-être sélectionné **Ne plus demander**, auquel cas vous devrez réinstaller l'application pour réinitialiser les autorisations de notification avant de tester à nouveau.
- **iOS :** Nous recommandons à votre équipe de développement de vérifier l'implémentation des notifications push pour votre application et de supprimer manuellement tout code qui demanderait les autorisations push. Pour en savoir plus, consultez [Messages in-app d'amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices).

Pour qu'une campagne de messages in-app basée sur une action soit distribuée, vous devez enregistrer les événements personnalisés via le SDK Braze et non via les REST API, afin que les utilisateurs puissent recevoir les messages in-app éligibles directement sur leur appareil. Les utilisateurs reçoivent le message in-app s'ils effectuent l'événement au cours de la session.