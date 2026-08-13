---
nav_title: Éditeur HTML
article_title: Créer un e-mail avec du HTML personnalisé
page_order: 2
description: "Cet article de référence explique comment créer un e-mail à l'aide de la plateforme Braze. Il inclut les bonnes pratiques pour rédiger vos messages, prévisualiser votre contenu et planifier votre campagne ou Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1
---

# Créer un e-mail avec du HTML personnalisé {#create-an-email-with-custom-html}

> Les e-mails sont un excellent moyen de diffuser du contenu à vos utilisateurs selon leurs préférences. Ils constituent également d'excellents outils pour réengager les utilisateurs qui ont peut-être même désinstallé votre application. L'envoi d'e-mails personnalisés et adaptés améliorera l'expérience de vos utilisateurs et les aidera à tirer le meilleur parti de votre application.

Pour voir des exemples de campagnes e-mail, consultez nos [études de cas](https://www.braze.com/customers).

{% alert tip %}
Si c'est la première fois que vous créez une campagne e-mail, nous vous recommandons vivement de suivre ces cours d'apprentissage Braze :<br><br>
- [Abonnements et autorisations pour les e-mails](https://learning.braze.com/messaging-channels-email)
- [Projet : Créer un programme d'e-mail marketing de base](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

Utilisez les Campaigns pour des communications simples et ponctuelles. Utilisez Canvas pour des parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **Email** ou, pour les Campaigns ciblant plusieurs canaux, sélectionnez **Multichannel**.
3. Donnez à votre Campaign un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) selon vos besoins.
   * Les tags facilitent la recherche de vos Campaigns et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder), vous pouvez filtrer par tags spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre Campaign. Pour en savoir plus sur ce sujet, consultez [Test multivarié et test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si tous les messages de votre Campaign sont similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Si vous prévoyez de créer du HTML personnalisé et souhaitez que les arrière-plans restent cohérents dans l'application mobile Gmail avec le mode sombre de l'appareil activé, consultez [Application mobile Gmail et couleurs d'arrière-plan en mode sombre](#gmail-dark-mode).
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Étape 2 : Sélectionner votre expérience d'édition {#step-2-choose-your-template-and-compose-your-email}

Braze propose deux expériences d'édition lors de la création d'une campagne e-mail : notre [éditeur par glisser-déposer]({{site.baseurl}}/dnd) et notre éditeur HTML standard. Choisissez la tuile correspondant à l'expérience d'édition que vous préférez.

![Choix entre l'éditeur par glisser-déposer, l'éditeur HTML ou les modèles pour votre expérience d'édition d'e-mail.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Ensuite, vous pouvez soit sélectionner un [modèle d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) existant, [importer un modèle]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) depuis un fichier (éditeur HTML uniquement), soit utiliser un modèle vierge.

Si vous utilisez l'éditeur HTML et que vous souhaitez que les couleurs d'arrière-plan restent cohérentes dans l'application mobile Gmail lorsque l'appareil est en mode sombre, consultez [Application mobile Gmail et couleurs d'arrière-plan en mode sombre](#gmail-dark-mode).

{% alert tip %}
Nous recommandons de sélectionner une seule expérience d'édition par campagne e-mail. Par exemple, choisissez soit **HTML Classic** soit **Block editor** dans une même campagne e-mail plutôt que de basculer entre les éditeurs.
{% endalert %}

## Étape 3 : Composer votre e-mail {#step-3-compose-your-email}

Après avoir sélectionné votre modèle, vous verrez un aperçu de votre e-mail où vous pouvez accéder directement à l'éditeur en plein écran pour rédiger votre e-mail, modifier vos informations d'envoi et consulter les avertissements relatifs à la livrabilité ou à la conformité légale. Vous pouvez basculer entre les onglets HTML, classique, texte brut et [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email) pendant la composition.

![Le bouton « Regenerate from HTML ».]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Braze met automatiquement à jour la version en texte brut à partir de la version HTML jusqu'à ce qu'il détecte une modification du texte brut. Après avoir détecté une modification, Braze cesse de mettre à jour le texte brut car il considère que vous avez effectué des changements intentionnels. Pour restaurer la synchronisation automatique, accédez à **Plaintext** et sélectionnez **Regenerate from HTML** (visible uniquement lorsque le texte brut n'est pas synchronisé).

{% alert tip %}
Pour ajouter du mouvement dans un e-mail avec un aperçu fidèle, utilisez des GIF plutôt que des éléments nécessitant JavaScript, car la plupart des boîtes de réception ne prennent pas en charge JavaScript.
{% endalert %}


{% alert important %}
Braze supprime automatiquement les gestionnaires d'événements HTML référencés en tant qu'attributs. Cela modifie le HTML, alors vérifiez à nouveau l'e-mail une fois terminé. En savoir plus sur les [gestionnaires HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Besoin d'aide pour rédiger un texte percutant ? Essayez l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Saisissez un nom ou une description de produit et l'IA générera un texte marketing au style naturel à utiliser dans vos communications.

![Bouton de lancement de l'assistant de rédaction IA, situé dans l'onglet Body du compositeur d'e-mails.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Besoin d'aide pour rédiger des messages de droite à gauche pour des langues comme l'arabe et l'hébreu ? Consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) pour les bonnes pratiques.

### Application mobile Gmail et mode sombre {#gmail-dark-mode}

L'application mobile Gmail (Android et iOS) peut inverser les couleurs d'arrière-plan lorsque l'appareil est en mode sombre. Cela peut casser les mises en page où l'arrière-plan de l'e-mail doit correspondre au bord d'une image ou à une couleur de marque spécifique.

Pour éviter cela, dans la cellule du tableau qui nécessite un arrière-plan stable, utilisez un `linear-gradient` CSS monochrome au lieu de `background-color`. Gmail est moins susceptible d'inverser ce traitement qu'une couleur d'arrière-plan unie.

Par exemple, pour conserver un arrière-plan blanc sur une cellule, utilisez ceci :

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

Remplacez `#ffffff` par la couleur souhaitée.

{% alert note %}
Cette approche ne s'applique pas de manière fiable aux éléments `<table aria-label="Application mobile Gmail et mode sombre #gmail-dark-mode">` seuls, définissez donc le dégradé sur la cellule plutôt que sur le tableau uniquement.
  <caption>Application mobile Gmail et mode sombre</caption>
{% endalert %}

Pour plus d'informations sur la syntaxe des dégradés, consultez [Les dégradés CSS sur W3Schools](https://www.w3schools.com/css/css3_gradients.asp).

### Étape 3.1 : Ajouter vos informations d'envoi {#step-31-add-your-sending-information}

Après avoir terminé la conception et la création de votre e-mail, ajoutez vos informations d'envoi dans **Sending Settings**.

{% multi_lang_include email/sending_info_steps.md %}

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Un aperçu dans le panneau de droite se remplira avec les informations d'envoi que vous avez ajoutées. Ces informations peuvent également être mises à jour en accédant à **Settings** > **Email Preferences** > **Sending Configuration**.

#### Avancé {#advanced}

Sous **Sending Settings** > **Advanced**, activez **inline CSS** pour la compatibilité la plus large avec les clients de messagerie. Si les messages sont tronqués ou si les images s'étirent à la hauteur de la ligne, essayez de désactiver temporairement l'insertion CSS. Certains modèles fonctionnent mieux sans insertion.

Vous pouvez également ajouter de la personnalisation pour les en-têtes d'e-mail et les extras d'e-mail afin de renvoyer des données supplémentaires à d'autres fournisseurs de services d'e-mailing.

##### Pièces jointes d'e-mail {#email-attachments}

Vous pouvez également ajouter des pièces jointes aux e-mails par les méthodes suivantes :

{% multi_lang_include email/attachment_upload_options.md %}

Consultez les [Directives pour les e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines) pour les bonnes pratiques spécifiques à prendre en compte.

##### En-têtes d'e-mail {#email-headers}

Pour ajouter des en-têtes d'e-mail, sélectionnez **Add New Header**. Les en-têtes d'e-mail contiennent des informations sur l'e-mail envoyé. Ces [paires clé-valeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) incluent généralement l'expéditeur, le destinataire, le protocole d'authentification et les informations de routage. Braze ajoute automatiquement les informations d'en-tête requises par la RFC pour que les e-mails atteignent les fournisseurs de boîtes de réception.

Braze vous offre la flexibilité d'ajouter des en-têtes d'e-mail supplémentaires selon vos besoins pour des cas d'usage avancés. Il existe quelques champs réservés que la plateforme Braze écrasera lors de l'envoi.

Évitez d'utiliser les clés suivantes :

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table aria-label="En-têtes d'e-mail" id="reserved-fields">
  <caption>En-têtes d'e-mail</caption>
<thead>
  <tr>
    <th>Champs réservés</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-signature</td>
    <td>Reply-To</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>From</td>
    <td>Subject</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>MIME-Version</td>
    <td>To</td>
  </tr>
  <tr>
    <td>Content-Type</td>
    <td>Received</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>DKIM-Signature</td>
    <td>received</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### Ajouter des extras d'e-mail {#adding-email-extras}

Les extras d'e-mail vous permettent de renvoyer des données supplémentaires à d'autres fournisseurs de services d'e-mailing. Cela ne s'applique qu'aux cas d'usage avancés, vous ne devriez donc utiliser les extras d'e-mail que si votre entreprise a déjà mis cela en place.

Pour ajouter des extras d'e-mail, accédez à **Sending Info** et sélectionnez **Add New Extra**.

{% alert warning %}
Le total des paires clé-valeur ajoutées ne doit pas dépasser 1 Ko. Sinon, les messages seront abandonnés.
{% endalert %}

Les valeurs des extras d'e-mail ne sont pas publiées vers Currents ou Snowflake. Si vous souhaitez envoyer des métadonnées supplémentaires ou des valeurs dynamiques vers Currents ou Snowflake, utilisez plutôt [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras).

### Étape 3.2 : Prévisualiser et tester votre message {#step-3b-preview-and-test-your-message}

Après avoir terminé la composition de votre e-mail, testez-le avant de l'envoyer. En bas de l'écran d'aperçu, sélectionnez **Preview and Test**.

Ici, vous pouvez prévisualiser l'apparence de votre e-mail dans la boîte de réception d'un client. Avec **Preview as User** sélectionné, vous pouvez prévisualiser votre e-mail en tant qu'utilisateur aléatoire, sélectionner un utilisateur spécifique ou créer un utilisateur personnalisé. Cela vous permet de vérifier que vos appels de contenu connecté et de personnalisation fonctionnent comme prévu.

Ensuite, vous pouvez **Copy preview link** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Pour plus d'informations, consultez [Prévisualisation partageable]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

Vous pouvez également basculer entre les vues bureau, mobile et texte brut pour avoir une idée de l'apparence de votre message dans différents contextes.

{% alert tip %}
Curieux de savoir à quoi ressemble votre e-mail pour les utilisateurs en mode sombre ? Sélectionnez la bascule **Dark Mode Preview** située dans la section **Preview and Test** (éditeur par glisser-déposer uniquement). Si vous utilisez l'éditeur HTML, vous pouvez toujours gérer le rendu en mode sombre de l'application mobile Gmail avec [Application mobile Gmail et mode sombre](#gmail-dark-mode).
{% endalert %}

Lorsque vous êtes prêt pour une vérification finale, sélectionnez **Test Send** et envoyez un message de test à vous-même ou à un groupe de testeurs pour confirmer que l'e-mail s'affiche correctement sur tous les appareils et clients.

![Option Test Send et exemple d'aperçu d'e-mail lors de la composition de votre e-mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si vous constatez des problèmes avec votre e-mail ou souhaitez apporter des modifications, sélectionnez **Edit Email** pour revenir à l'éditeur.

{% alert tip %}
Les clients de messagerie qui prennent en charge le texte d'aperçu récupèrent toujours suffisamment de caractères pour remplir tout l'espace disponible pour le texte d'aperçu. Cependant, cela peut vous laisser dans des situations où le texte d'aperçu est incomplet ou non optimisé.
<br><br>Pour éviter cela, vous pouvez créer un espace blanc après le texte d'aperçu souhaité afin que les clients de messagerie ne récupèrent pas d'autres textes ou caractères distrayants dans le contenu de l'enveloppe. Dans la section **Sending Settings**, vous pouvez cocher la case **Add whitespace after preheader** pour ajouter automatiquement un espace blanc. <br><br>Alternativement, si vous avez besoin de plus de contrôle, vous pouvez ajouter manuellement une chaîne de caractères de non-jointure de largeur nulle (`&zwnj;`) et d'espaces insécables (`&nbsp;`) après le texte d'aperçu que vous souhaitez afficher. <br><br>Lorsqu'il est ajouté à la fin de votre texte d'aperçu dans la section d'accroche, le morceau de code suivant pour l'éditeur HTML ajoutera l'espace blanc recherché :<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

Pour l'éditeur par glisser-déposer, ajoutez uniquement les caractères de non-jointure de largeur nulle (`&zwnj;`) sans le formatage `<div>` directement dans l'accroche dans la section **Sending Settings**.
{% endalert %}

{% alert note %}
Dans l'application Apple Mail, les liens d'images dans les e-mails HTML doivent utiliser des URL `https://` pour être cliquables. Utilisez des liens sécurisés pour toute image encapsulée dans une balise d'ancrage lorsque vous attendez des clics de la part de destinataires utilisant Apple Mail.
{% endalert %}

### Étape 3.3 : Vérifier les erreurs d'e-mail {#step-33-check-for-email-errors}

Avant l'envoi, l'éditeur signale les problèmes courants :

- Le nom d'affichage de l'expéditeur et l'en-tête ne sont pas définis ensemble
- Adresses d'expéditeur ou de réponse invalides
- Clés d'en-tête en double
- Erreurs de syntaxe Liquid
- Content Blocks qui incluent un `<!DOCTYPE html>` complet
- Le corps de l'e-mail dépasse 400&nbsp;Ko
  - Visez [moins de 102&nbsp;Ko]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips#email-size) pour éviter la troncature.
- Corps ou objet vide
- Lien de désabonnement manquant
- Le domaine d'expéditeur n'est pas dans la liste d'autorisation (envois fortement limités)

## Étape 4 : Construire le reste de votre campagne ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
Ensuite, construisez le reste de votre campagne. Consultez les sections suivantes pour savoir comment utiliser les outils Braze pour créer votre campagne par e-mail.

### Choisir un calendrier de réception ou un déclencheur {#choose-delivery-schedule-or-trigger}

Envoyez des e-mails en fonction d'un horaire planifié, d'une action ou d'un déclencheur API. Pour en savoir plus, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

{% alert note %}
Pour les Campaigns déclenchées par API, lorsque l'action de déclenchement est définie sur **Interact With Campaign**, la sélection d'une option **Receive** comme interaction entraînera le déclenchement de votre nouvelle campagne dès que Braze marquera la Campaign sélectionnée comme envoyée, même si ce message rebondit ou n'est pas distribué.
{% endalert %}

Vous pouvez également définir la durée de la campagne, spécifier les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) et configurer des règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, [ciblez les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en choisissant des Segments ou des filtres. Braze affiche un aperçu en direct de la population du Segment, y compris le nombre d'utilisateurs joignables par e-mail. L'appartenance exacte au Segment est calculée juste avant l'envoi.

{% multi_lang_include audience/target_audiences.md %}

Vous pouvez également choisir d'envoyer votre campagne uniquement aux utilisateurs ayant un [statut d'abonnement]({{site.baseurl}}/user_guide/channels/email/subscriptions) spécifique, comme ceux qui sont abonnés et ont opté pour recevoir des e-mails.

Vous pouvez aussi limiter la distribution à un nombre spécifié d'utilisateurs au sein du Segment, ou permettre aux utilisateurs de recevoir le même message deux fois lors d'une récurrence de la campagne.

{% alert note %}
Lors de la création d'une nouvelle campagne par e-mail, le groupe de contrôle est défini par défaut à 20 % et peut être ajusté ou supprimé selon les besoins de votre campagne.
{% endalert %}

#### Campaigns multicanales avec e-mail et notification push {#multichannel-campaigns-with-email-and-push}

Pour les Campaigns multicanales ciblant à la fois les canaux e-mail et notification push, vous pouvez souhaiter limiter votre campagne afin que seuls les utilisateurs ayant explicitement opté pour la réception reçoivent le message (en excluant les utilisateurs abonnés ou désabonnés). Par exemple, supposons que vous ayez trois utilisateurs avec des statuts d'abonnement différents :

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Pour ce faire, sous **Audience Summary**, sélectionnez l'envoi de cette campagne aux « utilisateurs ayant opté uniquement ». Cette option garantira que seuls les utilisateurs ayant opté recevront votre e-mail, et Braze n'enverra votre notification push qu'aux utilisateurs pour lesquels les notifications push sont activées par défaut.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Target Audiences** qui limiterait l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), après avoir reçu une campagne. Vous pouvez spécifier l'une des actions suivantes comme événement de conversion :

- Ouvre l'application
- Effectue un achat (il peut s'agir d'un achat générique ou d'un article spécifique)
- Effectue un événement personnalisé spécifique
- Ouvre l'e-mail

Vous pouvez autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle Braze comptabilise une conversion si l'utilisateur effectue l'action spécifiée. Bien que Braze suive automatiquement les ouvertures et les clics, vous pouvez définir l'événement de conversion sur une ouverture ou un clic pour utiliser la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection).
{% endtab %}

{% tab Canvas %}
Si ce n'est pas déjà fait, complétez les sections restantes de vos composants Canvas. Pour plus de détails sur la construction du reste de votre Canvas, la mise en œuvre de tests multivariés et de la sélection intelligente, et bien plus encore, consultez l'étape [Construire votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) de notre documentation Canvas.
{% endtab %}
{% endtabs %}

## Étape 5 : Vérifier et déployer {#step-5-review-and-deploy}

La dernière section résume la campagne que vous avez conçue. Confirmez tous les détails pertinents et sélectionnez **Launch Campaign**.

Pour savoir comment accéder aux résultats de vos campagnes par e-mail, consultez [Rapports sur les e-mails]({{site.baseurl}}/user_guide/channels/email/reporting).