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

Utilisez les campagnes pour un envoi de messages simple et unique. Utilisez les Canvas pour des parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Accédez à **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **Email** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et la création de rapports. Par exemple, lorsque vous utilisez le [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), vous pouvez filtrer par étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Pour en savoir plus sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, rédigez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) à l'aide du compositeur de Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le générateur de Canvas. Donnez à votre étape un nom clair et significatif.
3. Choisissez une [planification d'étape]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape, si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
6. Choisissez tout autre canal de communication que vous souhaitez associer à votre message.
{% endtab %}
{% endtabs %}

{% alert tip %}
Si vous prévoyez de créer du HTML personnalisé et que vous souhaitez que les arrière-plans restent cohérents dans l'application mobile Gmail avec le mode sombre activé, consultez [Application mobile Gmail et mode sombre](#gmail-dark-mode).
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Étape 2 : Sélectionner votre expérience d'édition {#step-2-choose-your-template-and-compose-your-email}

Braze propose deux expériences d'édition lors de la création d'une campagne e-mail : notre [éditeur par glisser-déposer]({{site.baseurl}}/dnd/) et notre éditeur HTML standard. Choisissez la tuile correspondant à l'expérience d'édition que vous préférez.

![Choix entre l'éditeur par glisser-déposer, l'éditeur HTML ou les modèles pour votre expérience d'édition d'e-mail.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Ensuite, vous pouvez soit sélectionner un [modèle d'e-mail]({{site.baseurl}}/user_guide/channels/email/html_editor/#creating-an-email-template) existant, [importer un modèle]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template/) depuis un fichier (éditeur HTML uniquement), soit utiliser un modèle vierge.

Si vous utilisez l'éditeur HTML et que vous souhaitez que les couleurs d'arrière-plan restent cohérentes dans l'application mobile Gmail lorsque l'appareil est en mode sombre, consultez [Application mobile Gmail et couleurs d'arrière-plan en mode sombre](#gmail-dark-mode).

{% alert tip %}
Nous recommandons de sélectionner une seule expérience d'édition par campagne e-mail. Par exemple, choisissez soit **HTML Classic** soit **Block editor** dans une même campagne e-mail plutôt que de basculer entre les éditeurs.
{% endalert %}

## Étape 3 : Rédiger votre e-mail {#step-3-compose-your-email}

Après avoir sélectionné votre modèle, vous verrez un aperçu de votre e-mail où vous pouvez accéder directement à l'éditeur en plein écran pour rédiger votre e-mail, modifier vos informations d'envoi et consulter les avertissements relatifs à la livrabilité ou à la conformité légale. Vous pouvez basculer entre les onglets HTML, classique, texte brut et [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email/) pendant la rédaction.

![Le bouton « Régénérer à partir du HTML ».]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Braze met automatiquement à jour la version en texte brut à partir de la version HTML jusqu'à ce qu'une modification du texte brut soit détectée. Dès qu'une modification est détectée, Braze cesse de mettre à jour le texte brut, considérant que vous avez effectué des changements intentionnels. Pour restaurer la synchronisation automatique, accédez à **Plaintext** et sélectionnez **Regenerate from HTML** (visible uniquement lorsque le texte brut n'est pas synchronisé).

{% alert tip %}
Pour ajouter du mouvement dans un e-mail avec un aperçu fidèle, utilisez des GIF plutôt que des éléments nécessitant JavaScript, car la plupart des boîtes de réception ne prennent pas en charge JavaScript.
{% endalert %}


{% alert important %}
Braze supprime automatiquement les gestionnaires d'événements HTML référencés en tant qu'attributs. Cela modifie le HTML, vérifiez donc l'e-mail une fois que vous avez terminé. En savoir plus sur les [gestionnaires HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Besoin d'aide pour rédiger un texte percutant ? Essayez l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy). Saisissez un nom ou une description de produit et l'IA générera un texte marketing de qualité humaine à utiliser dans vos messages.

![Bouton Lancer l'assistant de rédaction IA, situé dans l'onglet Corps du compositeur d'e-mail.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Besoin d'aide pour créer des messages de droite à gauche pour des langues comme l'arabe et l'hébreu ? Consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/) pour les bonnes pratiques.

### Application mobile Gmail et mode sombre {#gmail-dark-mode}

L'application mobile Gmail (Android et iOS) peut inverser les couleurs d'arrière-plan lorsque l'appareil est en mode sombre. Cela peut casser les mises en page où l'arrière-plan de l'e-mail doit correspondre au bord d'une image ou à une couleur de marque spécifique.

Pour éviter cela, dans la cellule du tableau qui nécessite un arrière-plan stable, utilisez un `linear-gradient` CSS monochrome au lieu de `background-color`. Gmail est moins susceptible d'inverser ce traitement qu'une couleur d'arrière-plan unie.

Par exemple, pour conserver un arrière-plan blanc sur une cellule, utilisez ceci :

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

Remplacez `#ffffff` par la couleur souhaitée.

{% alert note %}
Cette approche ne s'applique pas de manière fiable aux éléments `<table>` seuls, définissez donc le dégradé sur la cellule plutôt que sur le tableau uniquement.
{% endalert %}

Pour plus d'informations sur la syntaxe des dégradés, consultez [Les dégradés CSS sur W3Schools](https://www.w3schools.com/css/css3_gradients.asp).

### Étape 3.1 : Ajouter vos informations d'envoi {#step-31-add-your-sending-information}

Après avoir terminé la conception et la création de votre e-mail, ajoutez vos informations d'envoi dans **Sending Settings**.

1. Sous **Sending Info**, sélectionnez un e-mail comme **From Display Name + Address**. Vous pouvez également personnaliser cela en sélectionnant **Customize From Display Name + Address**.
2. Sélectionnez un e-mail comme **Reply-To Address**. Vous pouvez également personnaliser cela en sélectionnant **Customize Reply-To Address**.
3. Ensuite, sélectionnez un e-mail comme **BCC Address** pour rendre votre e-mail visible à cette adresse.
4. Ajoutez une ligne d'objet à votre e-mail. Vous pouvez également ajouter une accroche et un espace blanc après l'accroche.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Un aperçu dans le panneau de droite se remplira avec les informations d'envoi que vous avez ajoutées. Ces informations peuvent également être mises à jour en accédant à **Settings** > **Email Preferences** > **Sending Configuration**.

#### Avancé {#advanced}

Sous **Sending Settings** > **Advanced**, activez l'**insertion CSS** pour la compatibilité la plus large avec les clients de messagerie. Si les messages sont tronqués ou si les images s'étirent à la hauteur de la ligne, essayez de désactiver temporairement l'insertion CSS. Certains modèles fonctionnent mieux sans insertion.

Vous pouvez également ajouter de la personnalisation pour les en-têtes d'e-mail et des extras d'e-mail pour renvoyer des données supplémentaires à d'autres fournisseurs de services d'e-mailing.

##### Pièces jointes d'e-mail {#email-attachments}

Vous pouvez également ajouter des pièces jointes à vos e-mails par les méthodes suivantes :

- **Importer un fichier :** Glissez-déposez ou parcourez pour importer un fichier directement depuis votre ordinateur vers l'e-mail. Braze valide le type et la taille du fichier (jusqu'à 2&nbsp;Mo par défaut) avant l'importation, puis ces fichiers sont importés dans la bibliothèque multimédia. Les fichiers dépassant la limite de 2&nbsp;Mo ne peuvent pas être importés.
- **Utiliser la bibliothèque multimédia :** Parcourez et sélectionnez parmi les ressources déjà stockées dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Les PDF, documents Word, fichiers Excel et présentations PowerPoint sont tous pris en charge.
- **Ajouter depuis une URL :** Saisissez une URL pointant vers le fichier et fournissez un nom de fichier d'affichage. Comme Braze ne peut pas vérifier la taille des fichiers à partir d'URL arbitraires lors de la composition de l'e-mail, la taille du fichier est vérifiée au moment de l'envoi. Notez que Liquid n'est pas pris en charge dans ce champ.

Consultez les [bonnes pratiques pour les e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines/) pour les recommandations spécifiques à prendre en compte.

##### En-têtes d'e-mail {#email-headers}

Pour ajouter des en-têtes d'e-mail, sélectionnez **Add New Header**. Les en-têtes d'e-mail contiennent des informations sur l'e-mail envoyé. Ces [paires clé-valeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) incluent généralement l'expéditeur, le destinataire, le protocole d'authentification et les informations de routage. Braze ajoute automatiquement les informations d'en-tête requises par la RFC pour que les e-mails atteignent les fournisseurs de boîtes de réception.

Braze vous offre la flexibilité d'ajouter des en-têtes d'e-mail supplémentaires selon vos besoins pour des cas d'utilisation avancés. Il existe quelques champs réservés que la plateforme Braze écrasera lors de l'envoi.

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

Les extras d'e-mail vous permettent de renvoyer des données supplémentaires à d'autres fournisseurs de services d'e-mailing. Cela ne s'applique qu'aux cas d'utilisation avancés ; n'utilisez donc les extras d'e-mail que si votre entreprise a déjà mis cela en place.

Pour ajouter des extras d'e-mail, accédez à **Sending Info** et sélectionnez **Add New Extra**.

{% alert warning %}
Le total des paires clé-valeur ajoutées ne doit pas dépasser 1 Ko. Sinon, les messages seront abandonnés.
{% endalert %}

Les valeurs des extras d'e-mail ne sont pas publiées dans Currents ou Snowflake. Si vous souhaitez envoyer des métadonnées supplémentaires ou des valeurs dynamiques à Currents ou Snowflake, utilisez plutôt [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras/).

### Étape 3.2 : Prévisualiser et tester votre message {#step-3b-preview-and-test-your-message}

Après avoir terminé la rédaction de votre e-mail, testez-le avant de l'envoyer. En bas de l'écran d'aperçu, sélectionnez **Preview and Test**.

Ici, vous pouvez prévisualiser l'apparence de votre e-mail dans la boîte de réception d'un client. Avec **Preview as User** sélectionné, vous pouvez prévisualiser votre e-mail en tant qu'utilisateur aléatoire, sélectionner un utilisateur spécifique ou créer un utilisateur personnalisé. Cela vous permet de vérifier que vos appels de contenu connecté et de personnalisation fonctionnent correctement.

Ensuite, vous pouvez utiliser **Copy preview link** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Le lien sera valide pendant sept jours avant de devoir être régénéré.

Vous pouvez également basculer entre les vues ordinateur de bureau, appareil mobile et texte brut pour avoir une idée de l'apparence de votre message dans différents contextes.

{% alert tip %}
Vous souhaitez voir à quoi ressemble votre e-mail pour les utilisateurs en mode sombre ? Activez le bouton **Dark Mode Preview** situé dans la section **Preview and Test** (éditeur par glisser-déposer uniquement). Si vous utilisez l'éditeur HTML, vous pouvez toujours gérer le rendu en mode sombre de Gmail mobile avec [Application mobile Gmail et mode sombre](#gmail-dark-mode).
{% endalert %}

Lorsque vous êtes prêt pour une vérification finale, sélectionnez **Test Send** et envoyez un message de test à vous-même ou à un groupe de testeurs pour confirmer que l'e-mail s'affiche correctement sur tous les appareils et clients.

![Option d'envoi de test et exemple d'aperçu d'e-mail lors de la rédaction de votre e-mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si vous constatez des problèmes avec votre e-mail ou souhaitez apporter des modifications, sélectionnez **Edit Email** pour revenir à l'éditeur.

{% alert tip %}
Les clients de messagerie qui prennent en charge le texte d'aperçu récupèrent toujours suffisamment de caractères pour remplir tout l'espace disponible. Cependant, cela peut vous laisser dans des situations où le texte d'aperçu est incomplet ou non optimisé.
<br><br>Pour éviter cela, vous pouvez créer un espace blanc après le texte d'aperçu souhaité afin que les clients de messagerie ne récupèrent pas d'autres textes ou caractères distrayants dans le contenu de l'enveloppe. Pour ce faire, ajoutez une chaîne de caractères de non-jointure de largeur nulle (‌`&zwnj;`) et d'espaces insécables (`&nbsp;`) après le texte d'aperçu que vous souhaitez afficher. <br><br>Lorsqu'il est ajouté à la fin de votre texte d'aperçu dans la section d'accroche, le code suivant pour l'éditeur HTML ajoutera l'espace blanc recherché :<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

Pour l'éditeur par glisser-déposer, ajoutez uniquement les caractères de non-jointure de largeur nulle (‌`&zwnj;`) sans le formatage `<div>` directement dans l'accroche dans la section **Sending Settings**.
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
  - Visez [moins de 102&nbsp;Ko]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size) pour éviter la troncature.
- Corps ou objet vide
- Lien de désabonnement manquant
- Le domaine d'expéditeur n'est pas dans la liste autorisée (envois fortement limités)

## Étape 4 : Construire le reste de votre campagne ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
Ensuite, construisez le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur l'utilisation des outils Braze pour créer votre campagne e-mail.

### Choisir la planification de distribution ou le déclencheur {#choose-delivery-schedule-or-trigger}

Distribuez les e-mails en fonction d'un horaire planifié, d'une action ou d'un déclencheur API. Pour en savoir plus, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

{% alert note %}
Pour les campagnes déclenchées par API, lorsque l'action de déclenchement est définie sur **Interact With Campaign**, la sélection d'une option **Receive** comme interaction entraînera le déclenchement de votre nouvelle campagne dès que Braze marquera la campagne sélectionnée comme envoyée, même si ce message rebondit ou n'est pas distribué.
{% endalert %}

Vous pouvez également définir la durée de la campagne, spécifier les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) et définir des règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping).

### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, [ciblez les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) en choisissant des segments ou des filtres. Braze affiche un aperçu en temps réel de la population du segment, y compris le nombre d'utilisateurs joignables par e-mail. L'appartenance exacte au segment est calculée juste avant l'envoi.

{% multi_lang_include audience/target_audiences.md %}

Vous pouvez également choisir d'envoyer votre campagne uniquement aux utilisateurs ayant un [statut d'abonnement]({{site.baseurl}}/user_guide/channels/email/subscriptions/) spécifique, comme ceux qui sont abonnés et ont accepté de recevoir des e-mails.

Vous pouvez également limiter la distribution à un nombre spécifié d'utilisateurs au sein du segment, ou permettre aux utilisateurs de recevoir le même message deux fois lors d'une récurrence de la campagne.

{% alert note %}
Lors de la création d'une nouvelle campagne e-mail, le groupe de contrôle est défini par défaut à 20 % et peut être ajusté ou supprimé selon les besoins de votre campagne.
{% endalert %}

#### Campagnes multicanales avec e-mail et push {#multichannel-campaigns-with-email-and-push}

Pour les campagnes multicanales ciblant à la fois les canaux e-mail et push, vous pouvez souhaiter limiter votre campagne afin que seuls les utilisateurs ayant explicitement accepté reçoivent le message (en excluant les utilisateurs abonnés ou désabonnés). Par exemple, supposons que vous ayez trois utilisateurs avec des statuts d'abonnement différents :

- **L'utilisateur A** est abonné aux e-mails et a les notifications push activées. Cet utilisateur ne reçoit pas l'e-mail mais recevra la notification push.
- **L'utilisateur B** a accepté les e-mails mais n'a pas les notifications push activées. Cet utilisateur recevra l'e-mail mais ne recevra pas la notification push.
- **L'utilisateur C** a accepté les e-mails et a les notifications push activées. Cet utilisateur recevra à la fois l'e-mail et la notification push.

Pour ce faire, sous **Audience Summary**, sélectionnez l'envoi de cette campagne aux « utilisateurs ayant accepté uniquement ». Cette option garantira que seuls les utilisateurs ayant accepté recevront votre e-mail, et Braze n'enverra vos notifications push qu'aux utilisateurs ayant les notifications push activées par défaut.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Target Audiences** qui limiterait l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous pouvez spécifier l'une des actions suivantes comme événement de conversion :

- Ouvre l'application
- Effectue un achat (il peut s'agir d'un achat générique ou d'un article spécifique)
- Effectue un événement personnalisé spécifique
- Ouvre l'e-mail

Vous pouvez autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle Braze comptabilise une conversion si l'utilisateur effectue l'action spécifiée. Bien que Braze suive automatiquement les ouvertures et les clics, vous pouvez définir l'événement de conversion sur une ouverture ou un clic pour utiliser la [Sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
Si ce n'est pas déjà fait, complétez les sections restantes de vos composants Canvas. Pour plus de détails sur la façon de construire le reste de votre Canvas, de mettre en œuvre les tests multivariés et la Sélection intelligente, et plus encore, consultez l'étape [Construire votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.
{% endtab %}
{% endtabs %}

## Étape 5 : Vérifier et déployer {#step-5-review-and-deploy}

La dernière section résume la campagne que vous avez conçue. Confirmez tous les détails pertinents et sélectionnez **Launch Campaign**.

Pour savoir comment accéder aux résultats de vos campagnes e-mail, consultez [Rapports e-mail]({{site.baseurl}}/user_guide/channels/email/reporting/).