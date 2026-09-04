---
nav_title: Copier vers d'autres espaces de travail
article_title: Copier vers d'autres espaces de travail
page_order: 3
alias: "/copying_to_workspaces/"
page_type: reference
description: "Cet article de référence fournit un aperçu de la copie de campagnes, de Canvas et de pages de destination vers différents espaces de travail."
tool:
    - Campaigns
    - Canvas
---

# Copier des campagnes, des Canvas et des pages de destination vers d'autres espaces de travail {#copy-campaigns-canvases-and-landing-pages-across-workspaces}

> La copie de campagnes, de Canvas et de pages de destination vers d'autres espaces de travail vous permet de démarrer rapidement la création de contenu en utilisant du contenu existant d'un autre espace de travail comme point de départ. Cette page explique comment copier des campagnes, des Canvas et des pages de destination vers différents espaces de travail et indique ce qui est copié et ce qui ne l'est pas.

Lorsque vous copiez une campagne, un Canvas ou une page de destination vers un autre espace de travail, la copie reste à l'état de brouillon jusqu'à ce que vous la modifiiez et lanciez la campagne ou le Canvas, ou publiiez la page de destination. Cela vous permet de conserver et de développer vos stratégies de communication efficaces.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
La copie de campagnes vers d'autres espaces de travail est disponible de manière générale. La prise en charge du canal Content Cards n'est pas disponible actuellement.
{% endalert %}

Vous pouvez copier des campagnes vers d'autres espaces de travail pour les canaux pris en charge suivants : SMS, messages in-app, notifications push, e-mail et webhooks. Vous pouvez également copier des modèles d'e-mail, des feature flags et des Content Blocks. Notez que les campagnes multicanal comportant des canaux non pris en charge ne peuvent pas être copiées vers un autre espace de travail.

Pour copier une campagne vers un autre espace de travail :

1. Sélectionnez l'icône d'engrenage <i class="fas fa-cog"></i> à côté de la campagne sélectionnée.
2. Sélectionnez **Copier vers l'espace de travail**.
3. Après la copie, vérifiez et testez votre campagne pour confirmer que tous les champs fonctionnent correctement.

{% endtab %}
{% tab canvas %}

{% alert important %}
La copie de Canvas vers d'autres espaces de travail est disponible de manière générale. Les canaux suivants ne sont pas pris en charge actuellement : LINE, Content Cards et WhatsApp.
{% endalert %}

Vous pouvez copier des Canvas vers d'autres espaces de travail pour les canaux pris en charge suivants : e-mail, messages in-app, notifications push, webhooks et SMS.

Pour copier un Canvas vers un autre espace de travail :

1. Sélectionnez le menu <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;à côté du Canvas sélectionné.
2. Sélectionnez **Copier vers l'espace de travail**.
3. Après la copie, vérifiez et testez votre Canvas pour confirmer que tous les champs fonctionnent correctement.

Lors de la copie d'un Canvas comportant des étapes Audience Sync, les paramètres ne sont pas copiés vers l'espace de travail de destination, mais les étapes du parcours le sont.

{% endtab %}
{% tab pages de destination %}

Vous pouvez copier des pages de destination vers d'autres espaces de travail.

Pour copier une page de destination vers un autre espace de travail :

1. Accédez à **Envoi de messages** > **Pages de destination**.
2. Sélectionnez le menu <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;à côté de la page de destination sélectionnée.
3. Sélectionnez **Copier vers l'espace de travail**.
4. Vérifiez et testez votre page de destination pour confirmer que tous les champs fonctionnent correctement.

{% endtab %}
{% endtabs %}

{% alert note %}
Vous pouvez copier une campagne ou un Canvas vers un autre espace de travail à n'importe quel moment de son cycle de vie, y compris après son lancement. Braze copie la version active.<br><br>Si vous avez [enregistré des modifications en brouillon]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch#campaign-drafts) pour une campagne ou [enregistré un brouillon de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_drafts) que vous n'avez pas encore lancé, Braze n'inclut pas ces modifications en attente. Lancez d'abord le brouillon dans l'espace de travail d'origine, puis effectuez la copie.
{% endalert %}

## Ce qui est copié entre les espaces de travail {#whats-copied-across-workspaces}

Notez que les tableaux suivants couvrent les champs des Campaigns et des Canvas, et ne constituent pas une liste exhaustive de ce qui est copié ou omis entre les espaces de travail. En tant que bonne pratique, vérifiez les détails de la Campaign, du Canvas et de la page de destination, puis testez pour confirmer que votre message fonctionne comme prévu.

Les pages de destination sont copiées en tant que brouillons. Avant de publier une page de destination copiée, vérifiez l'URL de la page, les paramètres de domaine personnalisé, le traitement de la soumission du formulaire, ainsi que toute référence Liquid ou spécifique à l'espace de travail.

{% alert note %}
Les traductions ne sont pas copiées lors de la copie de Campaigns par e-mail, de Canvas ou de modèles entre les espaces de travail. Après la copie, saisissez à nouveau ou rechargez les traductions dans l'espace de travail de destination.
{% endalert %}

### Détails {#details}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Description | Territoires |
| Type | Tags |
| Actions (imbriquées) | Segments et filtres |
| Comportements de conversion (imbriqués) | [Approbations]({{site.baseurl}}/user_guide/messaging/governance/approvals) |
| Configurations du mode silencieux | Planification de déclenchement |
| Configurations de limite de fréquence | Résumés de Campaign |
| État d'abonnement du destinataire |  |
| Planification récurrente |  |
| Est transactionnel |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détails" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Description | Territoires |
| Type | Tags |
| Actions (imbriquées) | Segments et filtres |
| Comportements de conversion (imbriqués) | [Approbations]({{site.baseurl}}/user_guide/messaging/governance/approvals) |
| Configurations du mode silencieux | Planification de déclenchement |
| Configurations de limite de fréquence | Résumés de Canvas |
| État d'abonnement du destinataire |  |
| Planification récurrente | Critères de sortie |
| Est transactionnel |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détails" }

Les critères de filtre des étapes Canvas (par exemple, les étapes [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)) ne sont pas copiés vers l'espace de travail de destination. Reconfigurez ces filtres après la copie.

{% endtab %}
{% endtabs %}

### Comportements de conversion {#conversion-behaviors}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Type de comportement | ID d'espace de travail |
| Interaction de Campaign | ID de Campaign |
| Nom d'événement personnalisé |  |
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportements de conversion" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Type de comportement | ID d'espace de travail |
| Interaction de Canvas | ID de Canvas |
| Nom d'événement personnalisé |  |
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportements de conversion" }

{% endtab %}
{% endtabs %}

### Actions {#actions}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Type de comportement | ID d'espace de travail |
| Interaction de Campaign | ID de Campaign |
| Nom d'événement personnalisé |  |
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Type de comportement | ID d'espace de travail |
| Interaction de Canvas | ID de Canvas |
| Nom d'événement personnalisé |  |
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% endtabs %}

### Variations de message {#message-variations}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Pourcentage d'envoi | ID API |
| Type | ID de groupes initiateurs |
|  | ID de modèles de lien |
|  | ID de groupes d'utilisateurs internes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variations de message" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Pourcentage d'envoi | ID API |
| Type | ID de groupes initiateurs |
|  | ID de modèles de lien |
|  | ID de groupes d'utilisateurs internes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variations de message" }

{% endtab %}
{% endtabs %}


### Variation de message e-mail {#email-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | Adresse d'expéditeur |
| Extras de message | Répondre à |
| Titre | CCI |
| Objet | Modèle de lien |
|  | aliasage de lien |
|  | Traductions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variation de message e-mail" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | Adresse d'expéditeur |
| Extras de message | Répondre à |
| Titre | CCI |
| Objet | Modèle de lien |
|  | aliasage de lien |
|  | Traductions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variation de message e-mail" }

{% endtab %}
{% endtabs %}

### Corps de l'e-mail {#email-body}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Texte brut | aliasage de lien |
| Contenu HTML et glisser-déposer | Traductions |
| Accroche |  |
| CSS en ligne |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Corps de l'e-mail" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Texte brut | aliasage de lien |
| Contenu HTML et glisser-déposer | Traductions |
| Accroche |  |
| CSS en ligne |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Corps de l'e-mail" }

{% endtab %}
{% endtabs %}

### Modèles d'e-mail {#email-templates}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | ID API |
| Description | ID d'images |
| Objet | Territoires |
| En-têtes | Tags |
| | Traductions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modèles d'e-mail" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | ID API |
| Description | ID d'images |
| Objet | Territoires |
| En-têtes | Tags |
| | Traductions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modèles d'e-mail" }

{% endtab %}
{% endtabs %}

### Content Blocks

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Nom | aliasage de lien |
| Description | Clés API |
| Contenu | Territoires |
| Contenu HTML et glisser-déposer | Tags |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Nom | aliasage de lien |
| Description | Clés API |
| Contenu | Territoires |
| Contenu HTML et glisser-déposer | Tags |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% endtabs %}

### Variation de message SMS {#sms-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Corps | Service de messagerie |
| Raccourcissement de lien | Éléments multimédias VCF |
| Suivi des clics |  |
| Éléments multimédias |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variation de message SMS" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps | Service de messagerie |
| Raccourcissement de lien | Éléments multimédias VCF |
| Suivi des clics |  |
| Éléments multimédias |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variation de message SMS" }

{% endtab %}
{% endtabs %}

## Copie de messages contenant du Liquid {#copying-messages-that-contain-liquid}

Les références Liquid dans le corps des messages sont copiées vers l'espace de travail de destination, mais elles peuvent ne pas fonctionner comme prévu. Cela signifie que si un Canvas de l'espace de travail A est copié vers l'espace de travail B, l'espace de travail B ne peut pas référencer les détails de l'espace de travail A, y compris les références Liquid. Par exemple, les champs tels que les actions de déclenchement, les filtres d'audience et les critères de filtre de l'[arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) ne sont pas copiés.

Gardez une trace des références Liquid suivantes avec des dépendances lors de la copie de Campaigns, de Canvas et de pages de destination entre les espaces de travail :

- Tags d'éléments de catalogue
- Tags de contenu connecté
- Content Blocks
- Attributs personnalisés
- Centres de préférences
- Recommandations produit
- Tags d'état d'abonnement
- Tags de bons et de promotions

## Copier des messages avec des feature flags {#copying-messages-with-feature-flags}

Pour copier une campagne de feature flag et un Canvas avec une étape Feature Flag entre les espaces de travail, assurez-vous que l'espace de travail de destination dispose d'une [expérience de feature flag]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurée avec un ID correspondant soit au feature flag référencé dans la campagne d'origine, soit à l'étape Feature Flag référencée dans le Canvas d'origine.

Si vous copiez une campagne ou un Canvas comportant une étape Feature Flag avec un ID de feature flag qui n'existe pas dans l'espace de travail de destination, l'étape Feature Flag sera copiée mais son contenu ne le sera pas.

## Copier des messages avec des Content Blocks {#copying-messages-with-content-blocks}

Lorsque vous copiez une campagne d'un espace de travail à un autre, les Content Blocks ne sont pas copiés. Cependant, un Content Block peut être référencé dans l'espace de travail de destination si un bloc portant le même nom y existe. Vous pouvez également créer le Content Block (ou ces références Liquid) dans l'espace de travail de destination pour éviter les erreurs lors du lancement d'une campagne.

Pour les Canvas qui font référence à un Content Block, celui-ci doit d'abord être copié dans l'espace de travail de destination.