---
nav_title: Centre de préférences des e-mails via API
article_title: Centre de préférences des e-mails via API
page_order: 1
description: "Cet article décrit le centre de préférences des e-mails via API et comment le personnaliser."
channel:
  - email
---

# Centre de préférences des e-mails via API {#api-email-preference-center}

> La mise en place d'un centre de préférences offre à vos utilisateurs un point d'accès unique pour modifier et gérer leurs préférences de notification pour votre [envoi de messages par e-mail]({{site.baseurl}}/user_guide/channels/email). Cet article décrit les étapes pour créer un centre de préférences généré par API, mais vous pouvez également créer un centre de préférences à l'aide de l'[éditeur par glisser-déposer]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center).

Dans le tableau de bord de Braze, accédez à **Audience** > **Email Preference Centers**.

C'est ici que vous pouvez gérer et consulter chaque groupe d'abonnement. Chaque groupe d'abonnement que vous créez est ajouté à cette liste de centres de préférences. Vous pouvez créer plusieurs centres de préférences.

{% alert important %}
Le centre de préférences est conçu pour être utilisé dans le canal e-mail de Braze. Les liens du centre de préférences sont dynamiques et basés sur chaque utilisateur ; ils ne peuvent pas être hébergés en externe.
{% endalert %}

## Créer un centre de préférences avec l'API {#create-a-preference-center-with-api}

En utilisant les [endpoints Braze du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center), vous pouvez créer un centre de préférences, un site web hébergé par Braze, qui peut afficher l'état d'abonnement et les statuts des groupes d'abonnement de vos utilisateurs. En utilisant HTML et CSS, votre équipe de développement peut créer le centre de préférences afin que le style de la page corresponde à vos directives de marque.

L'utilisation de Liquid vous permet de récupérer les noms de vos groupes d'abonnement ainsi que le statut de chaque utilisateur. De cette façon, Braze stocke et récupère ces données lorsque la page est chargée.

### Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Centre de préférences activé | Votre tableau de bord de Braze dispose des autorisations nécessaires pour utiliser la fonctionnalité de centre de préférences. |
| Espace de travail valide avec un groupe d'abonnement e-mail, SMS ou WhatsApp | Un espace de travail fonctionnel avec des utilisateurs valides et un groupe d'abonnement e-mail, SMS ou WhatsApp. |
| Utilisateur valide | Un utilisateur avec une adresse e-mail et un ID externe. |
| Clé API générée avec les autorisations du centre de préférences | Dans le tableau de bord de Braze, accédez à **Paramètres** > **Clés API** pour confirmer que vous avez accès à une clé API avec les autorisations du centre de préférences. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

### Étape 1 : Utiliser l'endpoint de création du centre de préférences {#step-1-use-the-create-preference-center-endpoint}

Commençons par créer un centre de préférences à l'aide de l'[endpoint de création du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center). Pour personnaliser votre centre de préférences, vous pouvez inclure du HTML conforme à votre image de marque dans le champ `preference_center_page_html` et le champ `confirmation_page_html`.

L'[endpoint de génération d'URL du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) vous permet de récupérer l'URL du centre de préférences pour un utilisateur spécifique en dehors d'un e-mail envoyé via Braze.

{% alert note %}
Braze affiche `confirmation_page_html` dans une iframe qui utilise une URL `data:`. Les navigateurs traitent les URL `data:` comme des origines opaques. Par conséquent, les scripts dans cette iframe ne peuvent pas charger de ressources externes supplémentaires, et la navigation dans la fenêtre parente ou la communication entre les cadres depuis cette page échouera.<br><br>À la place, vous pouvez créer un lien vers du contenu externe, comme une URL de sondage hébergée, au lieu d'intégrer des scripts. Si vous devez intégrer un outil tiers et que le fournisseur le permet, utilisez un `<iframe title="Description du contenu intégré" src="https://example.com/...">` pointant vers l'URL HTTPS hébergée de l'outil.
{% endalert %}

### Étape 2 : Inclure dans votre campagne e-mail {#step-2-include-in-your-email-campaign}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Pour placer un lien vers le centre de préférences dans vos e-mails, utilisez l'étiquette Liquid suivante à l'endroit souhaité dans votre e-mail, de la même manière que vous inséreriez des URL de désabonnement.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Vous pouvez également utiliser une combinaison de HTML incluant du Liquid. Par exemple, vous pouvez coller ce qui suit comme URL dans l'éditeur HTML ou l'éditeur par glisser-déposer. Cela affiche la disposition de base du centre de préférences qui répertorie automatiquement tous les groupes d'abonnement e-mail. Si vous utilisez l'[aliasing de lien]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing), ajoutez un point d'interrogation final (`?`) après l'étiquette Liquid afin que Braze puisse ajouter les paramètres de suivi.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

Le centre de préférences dispose d'une case à cocher permettant à vos utilisateurs de se désabonner de tous les e-mails.

{% multi_lang_include preference_center/testing.md section="api" %}

#### Modifier un centre de préférences {#edit-a-preference-center}

Vous pouvez modifier et mettre à jour votre centre de préférences en utilisant l'[endpoint de mise à jour du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center).

#### Identifier les centres de préférences et leurs détails {#identify-preference-centers-and-details}

Pour identifier vos centres de préférences, utilisez l'[endpoint d'affichage des détails du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) pour renvoyer des informations associées telles que l'horodatage de la dernière mise à jour, l'ID du centre de préférences, et plus encore.

## Personnaliser un centre de préférences {#customize-a-preference-center}

Braze gère les mises à jour de l'état d'abonnement depuis le centre de préférences, ce qui maintient le centre de préférences synchronisé. Cependant, vous pouvez également créer et héberger votre propre centre de préférences en utilisant les [API des groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) avec les options suivantes.

### Option 1 : Lien avec des paramètres de chaîne de requête {#option-1-link-with-string-query-parameters}

Utilisez des paires champ-valeur de chaîne de requête dans le corps de l'URL pour transmettre l'ID utilisateur et la catégorie d'e-mail à la page afin que les utilisateurs n'aient qu'à confirmer leur choix de désabonnement. Cette option convient à ceux qui stockent un identifiant utilisateur sous forme hachée et qui ne disposent pas déjà d'un centre d'abonnement.

Pour cette option, chaque catégorie d'e-mail nécessite son propre lien de désabonnement spécifique :<br>
`http://mycompany.com/query-string-form-fill?field_id=Alex&field_category=offers`

{% alert tip %}
Il est également possible de hacher l'ID externe de l'utilisateur au moment de l'envoi à l'aide d'un filtre Liquid. Cela convertira le `user_id` en une valeur de hachage MD5, par exemple :
{% raw %}
```liquid
{% assign my_string = ${user_id} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Option 2 : Authentifier avec un jeton web JSON {#option-2-authenticate-with-json-web-token}

Utilisez un [jeton web JSON](https://auth0.com/learn/json-web-tokens/) pour authentifier les utilisateurs sur une partie de votre serveur web (par exemple, les préférences de compte) qui se trouve normalement derrière une couche d'authentification telle qu'un identifiant et un mot de passe.

Cette approche ne nécessite pas de paires de valeurs de chaîne de requête intégrées dans l'URL, car celles-ci peuvent être transmises dans le payload du jeton web JSON, par exemple :

```json
{
    "user_id": "1234567890",
    "name": "Alex Smith",
    "category": "offers"
}
```

## Foire aux questions {#frequently-asked-questions}

### Pourquoi mon centre de préférences ne fonctionne-t-il pas dans un envoi de test ? {#why-doesnt-my-preference-center-work-in-a-test-send}

Les liens du centre de préférences nécessitent un contexte d'envoi réel. Les envois de test ne génèrent pas d'URL de centre de préférences valides, et le bouton **Enregistrer les préférences** est désactivé si la page se charge. Il s'agit du comportement attendu. Pour tester de bout en bout, lancez une campagne ou une étape Canvas vers un utilisateur test ou un petit segment interne, ou utilisez l'[endpoint de génération d'URL du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center). Pour plus de détails, consultez [Tester les centres de préférences](#testing-preference-centers).

### Je n'ai pas créé de centre de préférences. Pourquoi est-ce que je vois « PreferenceCenterBrazeDefault » sur mon tableau de bord ? {#i-havent-created-a-preference-center-why-am-i-seeing-preferencecenterbrazedefault-on-my-dashboard}

Cela est utilisé pour afficher le centre de préférences lorsque le Liquid hérité {%raw%}`${preference_center_url}`{%endraw%} est utilisé, ce qui signifie que les étapes Canvas ou les modèles qui font référence à {%raw%}`${preference_center_url}` ou `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} ne fonctionneront pas. Cela s'applique également aux messages précédemment envoyés qui incluaient le Liquid hérité ou « PreferenceCenterBrazeDefault » dans le message.

Si vous faites référence à {%raw%}`${preference_center_url}`{%endraw%} dans un nouveau message, un centre de préférences nommé « PreferenceCenterBrazeDefault » sera créé à nouveau.

### Les centres de préférences prennent-ils en charge plusieurs langues ? {#do-preference-centers-support-multiple-languages}

Non. Cependant, vous pouvez tirer parti de Liquid lors de la rédaction du HTML pour les pages personnalisées d'abonnement et de désabonnement. Si vous utilisez des liens dynamiques pour gérer les désabonnements, il s'agit d'un lien unique.

Par exemple, si vous suivez le taux de désabonnement des utilisateurs hispanophones, vous devrez soit utiliser des campagnes distinctes, soit exploiter les analyses autour de Currents (comme vérifier quand un utilisateur se désabonne et consulter la langue préférée de cet utilisateur).

Autre exemple : pour suivre les taux de désabonnement des utilisateurs hispanophones, vous pourriez ajouter une chaîne de paramètre de requête comme `?Spanish=true` à l'URL de désabonnement si la langue de l'utilisateur est l'espagnol, et utiliser un lien de désabonnement classique dans le cas contraire :

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Ensuite, via Currents, vous pourriez identifier quels utilisateurs parlent espagnol et combien d'événements de clic il y a eu pour ce lien de désabonnement.

### Les liens de désabonnement et les centres de préférences des e-mails sont-ils tous deux requis pour l'envoi ? {#are-both-unsubscribe-links-and-email-preference-centers-required-for-sending}

Non. Si vous voyez le message « Your Email Body does not include an unsubscribe link » lors de la composition d'une campagne e-mail, cet avertissement est attendu si votre lien de désabonnement se trouve dans un bloc de contenu.

### Comment mettre à jour l'icône par défaut du navigateur ? {#how-do-i-update-the-default-browser-icon}

Par défaut, l'icône à côté du nom de l'onglet du navigateur (favicon) utilise le logo Braze. Pour ajouter un favicon personnalisé, vous le définissez via l'attribut `links-tags` dans votre appel API de création ou de mise à jour du [centre de préférences]({{site.baseurl}}/api/endpoints/preference_center). Braze injecte ensuite la balise {% raw %}`<link rel="icon" ...>`{% endraw %} dans la page hébergée pour vous.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}