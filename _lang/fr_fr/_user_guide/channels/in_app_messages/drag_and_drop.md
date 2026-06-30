---
nav_title: Éditeur par glisser-déposer
article_title: Créer un message in-app dans l'éditeur par glisser-déposer
alias: /iam_drag_and_drop/
page_order: 1
description: "Cet article de référence explique comment créer un message in-app avec l'éditeur par glisser-déposer, les conditions préalables, les détails créatifs, et plus encore."
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-level-styles'
  add-a-custom-font: '/docs/user_guide/channels/in_app_messages/customize/style_settings#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-components'
  creative-details: '/docs/user_guide/channels/in_app_messages/customize/style_settings#creative-details'
---

# Créer un message in-app par glisser-déposer {#create-an-in-app-message-with-drag-and-drop}

> L'éditeur par glisser-déposer vous permet de créer des messages in-app entièrement personnalisés dans des Campaigns ou des Canvas en utilisant l'expérience d'édition par glisser-déposer. Pour en savoir plus sur les blocs de construction disponibles dans l'éditeur, consultez les [Blocs éditeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages).


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

Si vous souhaitez utiliser vos modèles HTML personnalisés existants ou des modèles créés par un tiers, ils doivent être recréés dans l'éditeur par glisser-déposer.

Vous ne savez pas si votre message in-app doit être envoyé via une Campaign ou un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) ? Les Campaigns sont plus adaptées aux campagnes de communication ciblées et ponctuelles, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes. Une fois que vous avez choisi où créer votre message, passons aux étapes de création d'un message in-app par glisser-déposer.

## Conditions préalables {#prerequisites}

### Exigences du SDK {#sdk-requirements}

| Version minimale du SDK                                                       | Version recommandée du SDK                                                    |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exigences du SDK" }

{% details Plus d'informations sur les SDK minimaux %}

Les messages créés avec l'éditeur par glisser-déposer ne peuvent être envoyés qu'aux utilisateurs disposant des versions minimales du SDK (voir le tableau ci-dessus). Si un utilisateur n'a pas mis à jour son application (c'est-à-dire qu'il utilise une version plus ancienne du SDK), il ne recevra pas le message in-app.

Pour profiter de toutes les fonctionnalités disponibles dans l'éditeur par glisser-déposer, mettez à jour vos SDK vers les versions recommandées. Cela vous permet de bénéficier des fonctionnalités supplémentaires suivantes :

- Liens texte qui ne ferment pas le message
- Action de bouton pour demander l'amorce push

Voici les exigences minimales individuelles du SDK pour ces fonctionnalités :

| Liens texte*                                                         | Demande d'amorce push                                                         |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exigences du SDK" }

*Si vous incluez un lien dans votre message in-app qui redirige vers une URL et que l'utilisateur final ne dispose pas des versions minimales du SDK spécifiées, la sélection du lien fermera le message et l'utilisateur ne pourra pas revenir au message pour soumettre le formulaire.

{% enddetails %}

### Conditions préalables supplémentaires {#additional-prerequisites}

- Pour le SDK web, l'option d'initialisation [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) doit être définie sur `true`. L'option `enableHtmlInAppMessages` permet également à ces messages de fonctionner, mais elle est obsolète et doit être remplacée par `allowUserSuppliedJavascript`.
- Si vous utilisez Google Tag Manager, vous devez activer « Allow HTML In-App Messages » dans la configuration GTM.

## Étape 1 : Créer un message in-app {#step-1-create-an-in-app-message}

Créez un nouveau message in-app ou une nouvelle étape Canvas, puis sélectionnez **Drag-And-Drop Editor** comme expérience d'édition.

## Étape 2 : Sélectionner votre modèle {#step-2-select-your-template}

Après avoir sélectionné l'éditeur par glisser-déposer comme expérience d'édition, vous pouvez choisir de :

- Commencer avec un modèle modal vierge
- Utiliser un modèle de message in-app par glisser-déposer de Braze
- Sélectionner un modèle de message in-app par glisser-déposer enregistré

Sélectionnez **Build message** pour commencer à concevoir votre message in-app dans l'éditeur par glisser-déposer.

![La section Braze Templates où vous pouvez choisir un modèle basique, avec image d'arrière-plan, capture de numéro de téléphone ou vierge.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

Vous pouvez également accéder à tous les modèles depuis la section **Templates** du tableau de bord.

## Étape 3 : Ajouter des pages supplémentaires (facultatif) {#multi-page}

L'ajout de pages à votre message in-app vous permet de guider les utilisateurs à travers un flux séquentiel, comme un flux d'onboarding ou un parcours de bienvenue. Vous pouvez gérer les pages depuis la section **Pages** de l'onglet **Build**.

![Un message in-app pour une entreprise de santé composé de trois pages.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Ajouter des pages %}

Les messages in-app commencent avec une page par défaut. Pour ajouter une nouvelle page :

1. Sélectionnez **+ Add page**.
2. Sélectionnez parmi la liste de modèles personnalisés ou fournis par Braze.
3. Donnez un nom significatif à la page. Cela vous aidera lorsque vous relierez les pages entre elles.

{% alert tip %}
Vous pouvez ajouter jusqu'à 10 pages par message in-app.
{% endalert %}

Pour dupliquer une page existante :

1. Survolez la page dans la liste et sélectionnez <i class="fas fa-ellipsis-vertical"></i> **More options**.
2. Sélectionnez **Duplicate**.
3. Donnez un nom significatif à la page. Cela vous aidera lorsque vous relierez les pages entre elles.

{% endtab %}
{% tab Supprimer ou renommer des pages %}

Pour supprimer ou renommer une page :

1. Survolez la page dans la liste et sélectionnez <i class="fas fa-ellipsis-vertical"></i> **More options**.
2. Sélectionnez **Rename** ou **Delete**.

{% endtab %}
{% endtabs %}

### Étape 3a : Relier les pages entre elles {#step-3a-connect-pages-together}

Les messages in-app multi-pages sont séquentiels, ce qui signifie que les utilisateurs interagissent avec le message en appuyant ou en cliquant pour passer à la page suivante du flux.

Pour relier les pages entre elles :

1. Sélectionnez votre page de départ.
2. Sélectionnez un élément bouton ou image dans le canvas.
3. Définissez le **On-click behavior** sur **Go to page**.
4. Sélectionnez la page vers laquelle vous souhaitez créer un lien depuis la page de départ.
5. Continuez jusqu'à ce que toutes les pages soient reliées.

![Un utilisateur modifie le bouton d'action principal pour accéder à la page 2 du message in-app.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Si une page n'est reliée à aucune autre page, le message ne peut pas être lancé.

{% alert note %}
Les utilisateurs peuvent sélectionner le bouton de fermeture X pour quitter le message à tout moment. Ce bouton ne peut pas être supprimé.
{% endalert %}

## Étape 4 : Construire et concevoir votre message in-app {#step-4-build-and-design-your-in-app-message}

C'est ici que votre message prend vie, habillé du style signature de votre marque. En utilisant une combinaison de blocs éditeur et de paramètres de style, vous pouvez personnaliser et concevoir votre message in-app.

- Pour une liste des blocs éditeur disponibles et de leurs propriétés, consultez les [Blocs éditeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages).
- Pour obtenir de l'aide sur la personnalisation de l'apparence de votre message, consultez les [Paramètres de style]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings).
- Pour les bonnes pratiques de création de messages de droite à gauche, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Étape 5 : Tester votre message in-app {#step-5-test-your-in-app-message}

La section **Preview & Test** vous permet de prévisualiser vos messages in-app sur différents appareils et d'envoyer un message de test à votre appareil. Vous pouvez ainsi vous assurer que les détails sont cohérents sur toutes vos plateformes pour votre Campaign de message in-app par glisser-déposer.

Il est important de toujours tester vos messages in-app avant d'envoyer vos Campaigns afin de visualiser à quoi ressemblera votre message final du point de vue de l'utilisateur.

### Prévisualiser le message en tant qu'utilisateur {#preview-message-as-a-user}

{% alert warning %}
Pour envoyer un test à des groupes de test de contenu ou à des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test avant l'envoi.
{% endalert %}

Vous pouvez prévisualiser les messages depuis l'onglet **Preview & Test**, comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé :

- **Random User :** Braze sélectionnera aléatoirement un utilisateur de la base de données et prévisualisera le message in-app en fonction de ses attributs ou informations d'événements.
- **Select User :** Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou de son `external_id`. Le message in-app sera prévisualisé en fonction des attributs et des informations d'événements de cet utilisateur.
- **Custom User :** Vous pouvez personnaliser un utilisateur. Braze proposera des champs de saisie pour tous les attributs et événements disponibles. Saisissez les informations que vous souhaitez voir dans l'e-mail de prévisualisation.

### Liste de vérification pour les tests {#test-checklist}

Tenez compte des questions suivantes lorsque vous testez votre message in-app :

- Avez-vous testé le message sur différents appareils ?
- Les images et les médias s'affichent-ils et fonctionnent-ils comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une valeur d'attribut par défaut au cas où le Liquid ne renverrait aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos boutons dirigent-ils l'utilisateur là où il doit aller ?

## Questions fréquemment posées {#frequently-asked-questions}

### Pourquoi les clics sur le corps n'apparaissent-ils pas sur ma page d'analyse ? {#why-are-body-clicks-not-appearing-on-my-analytics-page}

Les clics sur le corps ne sont pas automatiquement collectés pour les messages in-app créés avec l'éditeur par glisser-déposer. Pour plus de détails, consultez les journaux de modifications du SDK pour [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) et [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

### Puis-je segmenter en fonction des clics sur les boutons ? {#can-i-segment-based-on-button-clicks}

Oui, vous pouvez segmenter en fonction des clics sur les boutons pour un maximum de deux boutons dans votre message. Pour ce faire, définissez l'**Identifier for Reporting** de vos boutons sur « 0 » et « 1 », ce qui correspondra respectivement aux filtres de segmentation « Clicked in-app message button 1 » et « Clicked in-app message button 2 ».

![Le champ « Identifier for Reporting » avec une valeur de « 0 ».]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

### Puis-je personnaliser mon message in-app en utilisant du HTML ou du JavaScript personnalisé, ou transférer des messages HTML existants dans l'éditeur ? {#can-i-customize-my-in-app-message-using-custom-html-or-javascript-or-transfer-existing-html-messages-into-the-editor}

Vous ne pouvez pas transférer directement des messages HTML existants dans l'éditeur, mais vous pouvez insérer du HTML brut, du CSS et du JavaScript dans un bloc de code personnalisé. Vous pouvez utiliser les blocs de code personnalisé pour intégrer des vidéos tierces et du Liquid avancé, comme le Contenu connecté ou les instructions conditionnelles.

### Comment puis-je créer un message in-app contextuel ? {#how-can-i-create-a-slideup-in-app-message}

Actuellement, l'éditeur est limité aux messages modaux et plein écran uniquement. Vous pouvez basculer entre les types d'affichage dans la section **Message container** du panneau **Message styles**.

### Puis-je enregistrer mon message in-app en tant que modèle après l'avoir créé dans ma Campaign ou mon Canvas ? {#can-i-save-my-in-app-message-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Oui. Pour tout message in-app que vous souhaitez réutiliser dans une future Campaign ou étape Canvas, vous pouvez l'enregistrer en tant que modèle personnalisé en utilisant le bouton **Save as template**, disponible après avoir quitté l'éditeur. Avant de pouvoir l'enregistrer en tant que modèle, vous devez d'abord lancer la Campaign OU l'enregistrer en tant que brouillon.

![Une prévisualisation d'un message in-app pour une visite guidée du produit.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

Vous pouvez également créer et enregistrer des modèles de messages in-app en accédant à **Content** > **In-App Message Templates**.