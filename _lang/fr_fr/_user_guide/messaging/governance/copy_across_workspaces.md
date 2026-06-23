---
nav_title: Copier vers d'autres espaces de travail
article_title: Copier vers d'autres espaces de travail
page_order: 3
alias: "/copying_to_workspaces/"
page_type: reference
description: "Cet article de référence fournit un aperçu de la copie de campagnes, de Canvas et de pages d'accueil vers différents espaces de travail."
tool:
    - Campaigns
    - Canvas
---

# Copier des campagnes, des Canvas et des pages d'accueil vers d'autres espaces de travail {#copy-campaigns-canvases-and-landing-pages-across-workspaces}

> La copie de campagnes, de Canvas et de pages d'accueil vers d'autres espaces de travail vous permet de démarrer rapidement la création de contenu en utilisant du contenu existant d'un autre espace de travail comme point de départ. Cette page explique comment copier des campagnes, des Canvas et des pages d'accueil vers différents espaces de travail et indique ce qui est copié et ce qui ne l'est pas.

Lorsque vous copiez une campagne, un Canvas ou une page d'accueil vers un autre espace de travail, la copie reste à l'état de brouillon jusqu'à ce que vous la modifiiez et lanciez la campagne ou le Canvas, ou publiiez la page d'accueil. Cela vous permet de conserver et de développer vos stratégies d'envoi de messages efficaces.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
La copie de campagnes vers d'autres espaces de travail est disponible de manière générale. La prise en charge du canal Content Cards n'est pas disponible actuellement.
{% endalert %}

Vous pouvez copier des campagnes vers d'autres espaces de travail pour les canaux pris en charge suivants : SMS, messages in-app, notifications push, e-mail et webhooks. Vous pouvez également copier des modèles d'e-mail, des indicateurs de fonctionnalité et des Content Blocks. Notez que les campagnes multicanal comportant des canaux non pris en charge ne peuvent pas être copiées vers un autre espace de travail.

Pour copier une campagne vers un autre espace de travail :

1. Sélectionnez l'icône d'engrenage <i class="fas fa-cog"></i> à côté de la campagne sélectionnée.
2. Sélectionnez **Copier vers l'espace de travail**.
3. Après la copie, vérifiez et testez votre campagne pour confirmer que tous les champs fonctionnent correctement.

{% endtab %}
{% tab canvas %}

{% alert important %}
La copie de Canvas vers d'autres espaces de travail est disponible de manière générale. Les canaux suivants ne sont pas pris en charge actuellement : LINE, Content Cards et WhatsApp.
{% endalert %}

Vous pouvez copier des Canvas vers d'autres espaces de travail pour les canaux pris en charge suivants : e-mail, messages in-app, push, webhooks et SMS.

Pour copier un Canvas vers un autre espace de travail :

1. Sélectionnez le menu <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;à côté du Canvas sélectionné.
2. Sélectionnez **Copier vers l'espace de travail**.
3. Après la copie, vérifiez et testez votre Canvas pour confirmer que tous les champs fonctionnent correctement.

Lors de la copie d'un Canvas comportant des étapes Audience Sync, les paramètres ne sont pas copiés vers l'espace de travail de destination, mais les étapes du parcours le sont.

{% endtab %}
{% tab pages d'accueil %}

Vous pouvez copier des pages d'accueil vers d'autres espaces de travail.

Pour copier une page d'accueil vers un autre espace de travail :

1. Accédez à **Envoi de messages** > **Pages d'accueil**.
2. Sélectionnez le menu <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;à côté de la page d'accueil sélectionnée.
3. Sélectionnez **Copier vers l'espace de travail**.
4. Vérifiez et testez votre page d'accueil pour confirmer que tous les champs fonctionnent correctement.

{% endtab %}
{% endtabs %}

## Ce qui est copié entre les espaces de travail {#whats-copied-across-workspaces}

Notez que les tableaux suivants couvrent les champs des campagnes et des Canvas, et ne constituent pas une liste exhaustive de ce qui est copié entre les espaces de travail et de ce qui est omis. En tant que bonne pratique, vérifiez les détails de la campagne, du Canvas et de la page d'accueil, et testez pour confirmer que votre message fonctionne comme prévu.

Les pages d'accueil sont copiées en tant que brouillons. Avant de publier une page d'accueil copiée, vérifiez l'URL de la page, les paramètres de domaine personnalisé, le traitement de la soumission du formulaire, ainsi que toute référence Liquid ou spécifique à l'espace de travail.

### Détails {#details}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Description | Territoires |
| Type | Étiquettes |
| Actions (imbriquées) | Segments et filtres |
| Comportements de conversion (imbriqués) | [Approbations]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
| Configurations des heures calmes | Planification de déclenchement |
| Configurations de limite de fréquence | Résumés de campagne |
| État d'abonnement du destinataire |  |
| Planification récurrente |  |
| Est transactionnel |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détails" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Description | Territoires |
| Type | Étiquettes |
| Actions (imbriquées) | Segments et filtres |
| Comportements de conversion (imbriqués) | [Approbations]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
| Configurations des heures calmes | Planification de déclenchement |
| Configurations de limite de fréquence | Résumés du Canvas |
| État d'abonnement du destinataire |  |
| Planification récurrente | Critères de sortie |
| Est transactionnel |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détails" }

Les critères de filtre des étapes du Canvas (par exemple, les étapes [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)) ne sont pas copiés vers l'espace de travail de destination. Reconfigurez ces filtres après la copie.

{% endtab %}
{% endtabs %}

### Comportements de conversion {#conversion-behaviors}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Type de comportement | ID d'espace de travail |
| Interaction avec la campagne | ID de campagne |
| Nom d'événement personnalisé |  |
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportements de conversion" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Type de comportement | ID d'espace de travail |
| Interaction avec le Canvas | ID de Canvas |
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
| Interaction avec la campagne | ID de campagne |
| Nom d'événement personnalisé |  |
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Type de comportement | ID d'espace de travail |
| Interaction avec le Canvas | ID de Canvas |
| Nom d'événement personnalisé |  |
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% endtabs %}

### Variantes de message {#message-variations}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Pourcentage d'envoi | ID de l'API |
| Type | ID de groupes initiateurs |
|  | ID de modèles de lien |
|  | ID de groupes d'utilisateurs internes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variantes de message" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Pourcentage d'envoi | ID de l'API |
| Type | ID de groupes initiateurs |
|  | ID de modèles de lien |
|  | ID de groupes d'utilisateurs internes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variantes de message" }

{% endtab %}
{% endtabs %}


### Variante de message e-mail {#email-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | Adresse d'expédition |
| Extras de message | Répondre à |
| Titre | CCI |
| Objet | Modèle de lien |
|  | Aliasage de lien |
|  | Traductions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variante de message e-mail" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | Adresse d'expédition |
| Extras de message | Répondre à |
| Titre | CCI |
| Objet | Modèle de lien |
|  | Aliasage de lien |
|  | Traductions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variante de message e-mail" }

{% endtab %}
{% endtabs %}

### Corps de l'e-mail {#email-body}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Texte brut | Aliasage de lien |
| Contenu HTML et glisser-déposer | Traductions |
| Accroche |  |
| CSS en ligne |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Corps de l'e-mail" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Texte brut | Aliasage de lien |
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
| Corps de l'e-mail | ID de l'API |
| Description | ID d'images |
| Objet | Territoires |
| En-têtes | Étiquettes |
| | Traductions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modèles d'e-mail" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | ID de l'API |
| Description | ID d'images |
| Objet | Territoires |
| En-têtes | Étiquettes |
| | Traductions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modèles d'e-mail" }

{% endtab %}
{% endtabs %}

### Content Blocks

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Nom | Aliasage de lien |
| Description | Clés API |
| Contenu | Territoires |
| Contenu HTML et glisser-déposer | Étiquettes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Nom | Aliasage de lien |
| Description | Clés API |
| Contenu | Territoires |
| Contenu HTML et glisser-déposer | Étiquettes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% endtabs %}

### Variante de message SMS {#sms-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Corps | Service de messagerie |
| Raccourcissement de lien | Éléments multimédias VCF |
| Suivi des clics |  |
| Éléments multimédias |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variante de message SMS" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps | Service de messagerie |
| Raccourcissement de lien | Éléments multimédias VCF |
| Suivi des clics |  |
| Éléments multimédias |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variante de message SMS" }

{% endtab %}
{% endtabs %}

## Copier des messages contenant du Liquid {#copying-messages-that-contain-liquid}

Les références Liquid dans le corps des messages sont copiées vers l'espace de travail de destination, mais elles peuvent ne pas fonctionner comme prévu. Cela signifie que si un Canvas de l'espace de travail A est copié vers l'espace de travail B, l'espace de travail B ne peut pas référencer les détails de l'espace de travail A, y compris les références Liquid. Par exemple, les champs tels que les actions de déclenchement, les filtres d'audience et les critères de filtre de l'[arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) ne sont pas copiés.

Gardez une trace des références Liquid suivantes avec des dépendances lors de la copie de campagnes, de Canvas et de pages d'accueil entre les espaces de travail :

- Étiquettes d'éléments de catalogue
- Balises de contenu connecté
- Content Blocks
- Attributs personnalisés
- Centres de préférences
- Recommandations produit
- Balises d'état d'abonnement
- Balises de bons de réduction et de promotions

## Copier des messages avec des indicateurs de fonctionnalité {#copying-messages-with-feature-flags}

Pour copier une campagne d'indicateur de fonctionnalité et un Canvas comportant une étape d'indicateur de fonctionnalité entre les espaces de travail, assurez-vous que l'espace de travail de destination dispose d'une [expérience d'indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/experiments/) configurée avec un ID correspondant soit à l'indicateur de fonctionnalité référencé dans la campagne d'origine, soit à l'étape d'indicateur de fonctionnalité référencée dans le Canvas d'origine.

Si vous copiez une campagne ou un Canvas comportant une étape d'indicateur de fonctionnalité avec un ID d'indicateur de fonctionnalité qui n'existe pas dans l'espace de travail de destination, l'étape d'indicateur de fonctionnalité sera copiée mais son contenu ne le sera pas.

## Copier des messages avec des Content Blocks {#copying-messages-with-content-blocks}

Lorsque vous copiez une campagne entre les espaces de travail, les Content Blocks ne sont pas copiés. Cependant, un Content Block peut être référencé dans l'espace de travail de destination si un bloc portant le même nom existe. Vous pouvez également créer le Content Block (ou ces références Liquid) dans l'espace de travail de destination pour éviter les erreurs lors du lancement d'une campagne.

Pour les Canvas qui référencent un Content Block, le Content Block doit d'abord être copié vers l'espace de travail de destination.