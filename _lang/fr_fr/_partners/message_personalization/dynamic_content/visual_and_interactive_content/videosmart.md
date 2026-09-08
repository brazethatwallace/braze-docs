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
> L'intégration VideoSmart vous permet d'intégrer du contenu vidéo personnalisé dans vos Campaigns e-mail en utilisant le contenu connecté de Braze et le templating Liquid pour demander des ressources vidéo à VideoSmart. Cette intégration est généralement mise en œuvre via un modèle de Content Block Braze réutilisable, ce qui permet un déploiement cohérent entre les Campaigns tout en offrant de la flexibilité dans la sélection des Campaigns et la logique de personnalisation.

_Cette intégration est développée et maintenue par VideoSmart._

## À propos de cette intégration {#about-this-integration}

VideoSmart s'intègre à Braze pour générer dynamiquement des ressources vidéo personnalisées au moment de l'envoi, qui sont ensuite intégrées directement dans le contenu de vos e-mails Campaign et Canvas dans Braze.

Dans Braze, vous sélectionnez la Campaign VideoSmart correspondante et transmettez les attributs client (via le templating Liquid) à VideoSmart lors de l'envoi. Ces attributs sont utilisés pour produire une expérience vidéo unique et personnalisée pour chaque destinataire. Vous pouvez ensuite utiliser le contenu connecté de Braze pour demander des URL vidéo ou des ressources à l'API de VideoSmart en temps réel, permettant ainsi une personnalisation à grande échelle.

Cette intégration est conçue pour les e-mails Braze prenant en charge le templating Liquid et le contenu connecté, et peut être configurée pour fonctionner avec les attributs standard du profil utilisateur Braze ou des champs de données personnalisés.

## Cas d'usage {#use-cases}


Les cas d'usage courants incluent les suivants :

- Onboarding et parcours de bienvenue des clients
- Éducation financière (comme les retraites et les polices d'assurance)
- Relevés annuels et communications réglementaires
- Campaigns de visibilité produit et de ventes croisées
- Campaigns de rétention client et de réengagement
- Rappels de panier abandonné : lorsqu'un client ajoute des produits à son panier sans finaliser l'achat, vous envoyez un e-mail avec une vidéo personnalisée mettant en avant les articles qu'il a laissés
- Suivi post-achat : après un achat, envoyez une vidéo de remerciement personnalisée et recommandez des produits associés

## Prérequis {#prerequisites}

Avant de commencer, vérifiez que vous disposez des éléments suivants :

| Exigence                        | Description                                                                                                                 |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Identifiants de contenu connecté Braze | Un identifiant d'authentification basique de contenu connecté nommé **basic_credentials**, configuré avec les valeurs fournies par VideoSmart |
| Modèle **VideoSmart Content Block**   | Le modèle **VideoSmart Content Block** ajouté à votre tableau de bord de Braze (fourni par VideoSmart)                                |
| Un e-mail Braze               | Un e-mail de Campaign Braze ou une étape d'e-mail Canvas dans lequel vous insérerez le **VideoSmart Content Block**                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

Suivez ces étapes pour activer le **bloc de contenu VideoSmart** et l'utiliser dans un e-mail.

### Étape 1 : Configurer le modèle de bloc de contenu VideoSmart dans Braze {#step-1-set-up-the-videosmart-content-block-template-in-braze}

Demandez le modèle de **bloc de contenu VideoSmart** à votre conseiller VideoSmart et ajoutez-le à votre tableau de bord de Braze.

VideoSmart vous fournira les identifiants pour l'authentification du contenu connecté utilisée par le Content Block.

### Étape 2 : Configurer l'authentification du contenu connecté {#step-2-set-up-connected-content-authentication}

Créez un identifiant d'authentification basique pour le contenu connecté dans Braze nommé « basic_credentials ».

- Suivez les instructions dans [Utiliser l'authentification basique]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-basic-authentication).
- Utilisez le nom d'utilisateur et le mot de passe fournis par VideoSmart.

### Étape 3 : Ajouter le Content Block à votre e-mail {#step-3-add-the-content-block-to-your-email}

Insérez le **bloc de contenu VideoSmart** dans votre e-mail à l'endroit où vous souhaitez que le contenu vidéo apparaisse.

Dans la plupart des configurations Braze, les Content Blocks sont référencés selon le modèle suivant (remplacez « VideoSmart_Campaign » par le nom du Content Block dans votre compte) :

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
Le nom du Content Block est sensible à la casse et doit correspondre exactement à ce que vous avez configuré dans Braze.
{% endalert %}

### Étape 4 : Remplacer la campagne et les données d'enregistrement (facultatif) {#step-4-override-campaign-and-record-data-optional}

Si votre Content Block prend en charge des valeurs par défaut, vous pouvez l'utiliser sans définir de variables.

Si vous devez choisir une campagne VideoSmart spécifique, transmettre des champs de personnalisation personnalisés, ou les deux, définissez les variables Liquid suivantes avant le rendu du Content Block :

- `vs_campaign_id` : identifiant de la campagne VideoSmart
- `vs_record_data` : une chaîne JSON contenant les valeurs que vous souhaitez transmettre au modèle VideoSmart

#### Exemple {#example}

Cet exemple utilise les attributs utilisateur Braze pour le prénom et le nom :

{% raw %}
```liquid
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'Alex' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

{% alert note %}
- Fournissez toujours des valeurs par défaut pour les valeurs utilisées dans `vs_record_data` afin que l'aperçu de votre e-mail Braze s'affiche correctement.
- `vs_record_data` doit être du JSON valide, encodé sous forme de chaîne unique (l'exemple utilise `strip_newlines`).
{% endalert %}

### Étape 5 : Utiliser les variables générées par le modèle de Content Block de VideoSmart {#step-5-use-the-variables-generated-by-videosmarts-content-block-template}

Après l'exécution du Content Block, celui-ci génère des variables que vous pouvez référencer ailleurs dans votre e-mail.

Les variables courantes incluent :

{% raw %}
| Variable                          | Description                                                    |
| --------------------------------- | -------------------------------------------------------------- |
| `{{ video_url }}`                 | URL de la vidéo personnalisée                                  |
| `{{ poster_url }}`                | URL de l'image d'affiche de la vidéo                           |
| `{{ output_data.VARIABLE_NAME }}` | Champs de sortie supplémentaires exposés par le Content Block  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 5 : Utiliser les variables générées par le modèle de Content Block de VideoSmart" }
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 5 : Utiliser les variables générées par le modèle de Content Block de VideoSmart" }

## Limites de débit {#rate-limits}

L'API de VideoSmart a une limite de débit de 10 000 requêtes par minute. Si vous dépassez cette limite, vous pouvez recevoir des erreurs ou subir des retards dans la génération des vidéos.

Pour réduire ce risque, configurez la limitation du débit des Campaigns Braze afin que le taux d'envoi des messages reste en dessous de la capacité de l'API VideoSmart.

Pour obtenir des conseils Braze sur la vitesse de distribution et la limitation du débit, consultez [Vitesse de distribution et limitation du débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting).

## Considérations {#considerations}

- Le contenu connecté est exécuté lorsque le message est rendu, les valeurs peuvent donc différer entre l'aperçu et l'envoi si vos valeurs par défaut ou vos attributs diffèrent.
- Confirmez que votre e-mail inclut le Content Block avant de référencer des variables comme `video_url`.
- Si vous utilisez des champs personnalisés dans `vs_record_data`, confirmez les noms de champs attendus auprès de VideoSmart.

## Résolution des problèmes {#troubleshooting}

### L'aperçu ne fonctionne pas {#preview-not-working}

Si l'aperçu Braze échoue (par exemple, tentatives répétées ou erreurs d'authentification), vérifiez que :

- L'identifiant de contenu connecté « basic_credentials » existe et est correctement configuré.
- Le modèle **VideoSmart Content Block** est présent dans votre compte Braze.
- Toutes les variables requises (par exemple, `vs_campaign_id` ou les champs obligatoires dans `vs_record_data`) ont des valeurs par défaut définies pour l'aperçu.

### Les variables du modèle Content Block de VideoSmart ne génèrent pas le résultat attendu {#videosmarts-content-block-template-variables-not-generating-expected-output}

Si les variables générées par le modèle Content Block de VideoSmart ne produisent pas le résultat attendu, vérifiez les points suivants :

- Le modèle **VideoSmart Content Block** est correctement configuré dans Braze.
- L'authentification du contenu connecté est correctement configurée avec les identifiants appropriés.
- Affichez les variables dans votre e-mail pour confirmer qu'elles sont bien définies. Par exemple : `{% raw %}{{ video_url }}{% endraw %}`

Si vous utilisez une Campaign personnalisée, vérifiez également que :

- `vs_campaign_id` est défini sur un identifiant de Campaign valide.
- `vs_record_data` est un JSON valide et contient les champs attendus.