---
nav_title: VideoSmart
article_title: VideoSmart
description: "Cet article de référence décrit le partenariat entre Braze et VideoSmart, une technologie de vidéo personnalisée et interactive qui permet aux marques de diffuser du contenu non linéaire basé sur les données, à grande échelle."
alias: /partners/videosmart/
page_type: partner
search_tag: Partner
---

# VideoSmart

> [VideoSmart](https://www.videosmart.com/) fournit une technologie de vidéo personnalisée et interactive qui vous permet de diffuser du contenu non linéaire basé sur les données, à grande échelle. Chaque vidéo est générée dynamiquement à partir de données au niveau du client, ce qui permet d'adapter les messages et les parcours utilisateur au sein d'une seule expérience vidéo.
>
> L'intégration VideoSmart vous permet d'intégrer du contenu vidéo personnalisé dans vos Campaigns e-mail en utilisant le Contenu connecté de Braze et le templating Liquid pour demander des ressources vidéo à VideoSmart. Cette intégration est généralement mise en œuvre via un modèle de Content Block Braze réutilisable, ce qui permet un déploiement cohérent entre les Campaigns tout en offrant de la flexibilité dans la sélection des Campaigns et la logique de personnalisation.

_Cette intégration est développée et maintenue par VideoSmart._

## À propos de cette intégration {#about-this-integration}

VideoSmart s'intègre à Braze pour générer dynamiquement des ressources vidéo personnalisées au moment de l'envoi, qui sont ensuite intégrées directement dans le contenu e-mail de vos Campaigns et Canvas Braze.

Dans Braze, vous sélectionnez la campagne VideoSmart correspondante et transmettez les attributs client (via le templating Liquid) à VideoSmart lors de l'envoi. Ces attributs sont utilisés pour produire une expérience vidéo unique et personnalisée pour chaque destinataire. Vous pouvez ensuite utiliser le Contenu connecté de Braze pour demander des URL ou des ressources vidéo à l'API de VideoSmart en temps réel, ce qui permet une personnalisation à grande échelle.

Cette intégration est conçue pour les messages e-mail Braze prenant en charge le templating Liquid et le Contenu connecté. Elle peut être configurée pour fonctionner avec les attributs standard du profil utilisateur Braze ou avec des champs de données personnalisés.

## Cas d'utilisation {#use-cases}

Les cas d'utilisation courants incluent les suivants :

- Onboarding client et parcours de bienvenue
- Éducation financière (comme les retraites et les polices d'assurance)
- Relevés annuels et communications réglementaires
- Campagnes de notoriété produit et de vente croisée
- Campagnes de rétention client et de réengagement
- Rappels de panier abandonné : lorsqu'un client ajoute des produits à son panier sans finaliser l'achat, vous envoyez un e-mail avec une vidéo personnalisée mettant en avant les articles laissés de côté
- Suivi post-achat : après un achat, envoyez une vidéo de remerciement personnalisée et recommandez des produits associés

## Conditions préalables {#prerequisites}

Avant de commencer, vérifiez que vous disposez des éléments suivants :

| Condition | Description |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Identifiants de Contenu connecté Braze | Un identifiant d'authentification basique de Contenu connecté nommé **basic_credentials**, configuré avec les valeurs fournies par VideoSmart |
| Modèle de **Content Block VideoSmart** | Le modèle de **Content Block VideoSmart** ajouté à votre tableau de bord de Braze (fourni par VideoSmart) |
| Un message e-mail Braze | Un e-mail de Campaign Braze ou une étape e-mail Canvas dans lequel vous insérerez le **Content Block VideoSmart** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration {#integration}

Suivez ces étapes pour activer le **Content Block VideoSmart** et l'utiliser dans un e-mail.

### Étape 1 : Configurer le modèle de Content Block VideoSmart dans Braze {#step-1-set-up-the-videosmart-content-block-template-in-braze}

Demandez le modèle de **Content Block VideoSmart** à votre conseiller VideoSmart et ajoutez-le à votre tableau de bord de Braze.

VideoSmart fournira les identifiants pour l'authentification du Contenu connecté utilisée par le Content Block.

### Étape 2 : Configurer l'authentification du Contenu connecté {#step-2-set-up-connected-content-authentication}

Créez un identifiant d'authentification basique de Contenu connecté dans Braze nommé « basic_credentials ».

- Suivez les instructions de la section [Utiliser l'authentification basique]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/#using-basic-authentication).
- Utilisez le nom d'utilisateur et le mot de passe fournis par VideoSmart.

### Étape 3 : Ajouter le Content Block à votre e-mail {#step-3-add-the-content-block-to-your-email}

Insérez le **Content Block VideoSmart** dans votre e-mail à l'endroit où vous souhaitez que le contenu vidéo apparaisse.

Dans la plupart des configurations Braze, les Content Blocks sont référencés selon le schéma suivant (remplacez « VideoSmart_Campaign » par le nom du Content Block dans votre compte) :

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
Le nom du Content Block est sensible à la casse et doit correspondre exactement à ce que vous avez configuré dans Braze.
{% endalert %}

### Étape 4 : Remplacer la campagne et les données d'enregistrement (facultatif) {#step-4-override-campaign-and-record-data-optional}

Si votre Content Block prend en charge des valeurs par défaut, vous pouvez l'utiliser sans définir de variables.

Si vous devez choisir une campagne VideoSmart spécifique, transmettre des champs de personnalisation personnalisés, ou les deux, définissez les variables Liquid suivantes avant le rendu du Content Block :

- `vs_campaign_id` : identifiant de la campagne VideoSmart
- `vs_record_data` : une chaîne de caractères JSON contenant les valeurs que vous souhaitez transmettre au modèle VideoSmart

#### Exemple {#example}

Cet exemple utilise les attributs utilisateur Braze pour le prénom et le nom de famille :

{% raw %}
```liquid
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'John' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

{% alert note %}
- Fournissez toujours des valeurs par défaut pour les données utilisées dans `vs_record_data` afin que la prévisualisation de votre e-mail Braze s'affiche correctement.
- `vs_record_data` doit être un JSON valide, encodé sous forme d'une seule chaîne de caractères (l'exemple utilise `strip_newlines`).
{% endalert %}

### Étape 5 : Utiliser les variables générées par le modèle de Content Block VideoSmart {#step-5-use-the-variables-generated-by-videosmarts-content-block-template}

Après l'exécution du Content Block, celui-ci génère des variables que vous pouvez référencer ailleurs dans votre e-mail.

Les variables courantes incluent :

{% raw %}
| Variable | Description |
| --------------------------------- | ----------------------------------------------------- |
| `{{ video_url }}` | URL de la vidéo personnalisée |
| `{{ poster_url }}` | URL de l'image d'aperçu de la vidéo |
| `{{ output_data.VARIABLE_NAME }}` | Champs de sortie supplémentaires exposés par le Content Block |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 5 : Utiliser les variables générées par le modèle de Content Block VideoSmart" }
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 5 : Utiliser les variables générées par le modèle de Content Block VideoSmart" }

## Limites de débit {#rate-limits}

L'API de VideoSmart a une limite de débit de 10 000 requêtes par minute. Si vous dépassez cette limite, vous pourriez recevoir des erreurs ou constater des retards dans la génération des vidéos.

Pour réduire ce risque, configurez la limitation de débit de votre Campaign Braze afin que le rythme d'envoi des messages reste en dessous de la capacité de l'API VideoSmart.

Pour en savoir plus sur la vitesse de distribution et la limitation de débit dans Braze, consultez [Vitesse de distribution et limitation de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting).

## Points à prendre en compte {#considerations}

- Le Contenu connecté est exécuté au moment du rendu du message. Les valeurs peuvent donc différer entre la prévisualisation et l'envoi si vos valeurs par défaut ou vos attributs sont différents.
- Vérifiez que votre e-mail inclut le Content Block avant de référencer des variables comme `video_url`.
- Si vous utilisez des champs personnalisés dans `vs_record_data`, confirmez les noms de champs attendus auprès de VideoSmart.

## Résolution des problèmes {#troubleshooting}

### La prévisualisation ne fonctionne pas {#preview-not-working}

Si la prévisualisation Braze échoue (par exemple, tentatives répétées ou erreurs d'authentification), vérifiez que :

- L'identifiant de Contenu connecté « basic_credentials » existe et est correctement configuré.
- Le modèle de **Content Block VideoSmart** est présent dans votre compte Braze.
- Toutes les variables requises (par exemple, `vs_campaign_id` ou les champs requis dans `vs_record_data`) ont des valeurs par défaut définies pour la prévisualisation.

### Les variables du modèle de Content Block VideoSmart ne produisent pas le résultat attendu {#videosmarts-content-block-template-variables-not-generating-expected-output}

Si les variables générées par le modèle de Content Block VideoSmart ne produisent pas le résultat attendu, vérifiez les points suivants :

- Le modèle de **Content Block VideoSmart** est correctement configuré dans Braze.
- L'authentification du Contenu connecté est correctement configurée avec les identifiants appropriés.
- Affichez les variables dans votre e-mail pour confirmer qu'elles sont bien définies. Par exemple : `{% raw %}{{ video_url }}{% endraw %}`

Si vous utilisez une campagne personnalisée, vérifiez également que :

- `vs_campaign_id` est défini avec un identifiant de campagne valide.
- `vs_record_data` est un JSON valide et contient les champs attendus.