---
nav_title: Lokalise
article_title: Lokalise
description: "Cet article de référence présente le partenariat entre Braze et Lokalise, un service de gestion des traductions pour les équipes agiles."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokalise](https://lokalise.com) est un service de gestion des traductions pour les équipes agiles.

_Cette intégration est maintenue par Lokalise._

## À propos de l'intégration {#about-the-integration}

Lokalise propose deux options d'intégration pour Braze :

- **Intégration multilingue (recommandée)** : utilise l'[API de composition multilingue]({{site.baseurl}}/api/endpoints/translations) de Braze pour fournir une synchronisation bidirectionnelle directe entre Lokalise et Braze. Cette intégration fonctionne avec les variantes de messages localisées pour les Campaigns, les Canvas et les modèles d'e-mail, et prend en charge les workflows de traduction avant et après le lancement pour les notifications push, les e-mails et les In-App Messages.
- **Intégration par contenu connecté (ancienne)** : utilise le contenu connecté de Braze pour insérer du contenu traduit en fonction des paramètres linguistiques de l'utilisateur.

Cet article couvre la configuration des deux intégrations.

## Intégration multilingue (recommandée) {#multi-language-integration-recommended}

L'intégration multilingue utilise l'API de composition multilingue de Braze pour offrir un moyen simplifié et automatisé de gérer le contenu Braze multilingue dans Lokalise.

### Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Lokalise | Un compte Lokalise est nécessaire pour bénéficier de ce partenariat. |
| Projet de traduction Lokalise | Créez un projet Lokalise avec le type **Marketing and support** et choisissez **Braze** comme **Content integration**. |
| Paramètres multilingues Braze | La [prise en charge multilingue]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings) doit être activée dans votre espace de travail Braze. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations de lecture et de mise à jour des Campaigns, des Canvas et des modèles d'e-mail. Vous pouvez en créer une dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
| Région du serveur Braze | Votre [région du serveur Braze]({{site.baseurl}}/api/basics#endpoints) (par exemple, US-01, EU-01). Vous pouvez la trouver dans le tableau de bord de Braze. |
| Balises de traduction dans le contenu Braze | Les messages doivent utiliser des [balises de traduction]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) pour identifier le contenu traduisible. Encadrez chaque bloc traduisible avec des balises {% raw %}`{% translation ID %}...{% endtranslation %}`{% endraw %} dotées d'un ID unique. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

### Configuration et utilisation {#setup-and-usage}

Pour des instructions détaillées sur la connexion de l'intégration multilingue Braze dans Lokalise, l'importation de contenu, la traduction et l'exportation des traductions vers Braze, consultez la [documentation d'intégration Braze de Lokalise](https://docs.lokalise.com/en/articles/13654162-braze).

L'intégration prend en charge :
- La synchronisation bidirectionnelle directe entre Lokalise et Braze (sans manipulation manuelle de fichiers)
- Les variantes de messages localisées pour les Campaigns, les Canvas et les modèles d'e-mail
- Les workflows de traduction avant et après le lancement

{% alert note %}
Seul le contenu configuré pour une utilisation multilingue dans Braze et encadré par des balises de traduction est disponible pour l'importation dans Lokalise. Les codes de langue doivent correspondre exactement dans Braze et Lokalise pour que les traductions se synchronisent correctement.
{% endalert %}

## Intégration par contenu connecté (ancienne) {#connected-content-integration-legacy}

L'intégration ancienne utilise le contenu connecté de Braze pour insérer du contenu traduit en fonction des paramètres linguistiques de l'utilisateur.

### Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Lokalise | Un compte Lokalise est nécessaire pour bénéficier de ce partenariat. |
| Projet de traduction Lokalise | Créez un projet Lokalise avec le type de projet **Software Localization**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

### Créer un nouveau projet Lokalise {#create-a-new-lokalise-project}

Pour créer un nouveau projet de traduction, connectez-vous à Lokalise et sélectionnez **New Project**. Ensuite, nommez votre projet, choisissez une **Base Language** (la langue à partir de laquelle vous allez traduire), ajoutez une ou plusieurs **Target Languages** et choisissez le type de projet **Software Localization**. Lorsque vous êtes prêt, cliquez sur **Proceed**.

### Intégration {#integration}

Dans Lokalise, vous allez créer une clé de traduction pour chacune des variables de contenu connecté que vous définissez dans Braze. Lorsque les traductions sont prêtes, vous pouvez générer un fichier JSON par langue et le publier sur les URL qui serviront votre contenu connecté.

#### Étape 1 : Configurer les langues utilisateur {#step-1-configure-user-languages}

Si vous ne l'avez pas encore fait, ouvrez le tableau de bord de Braze et allez dans **Users > User import**. Ici, vous pouvez importer vos utilisateurs. Lorsque vous préparez un fichier CSV pour l'importation, veillez à inclure une colonne de langues avec les langues des utilisateurs. Ce champ linguistique sera utilisé ultérieurement lors de l'affichage des traductions.

{% alert important %}
Les codes linguistiques utilisés doivent correspondre entre Braze et Lokalise.
{% endalert %}

#### Étape 2 : Préparer vos traductions sur Lokalise {#step-2-prepare-your-translations-on-lokalise}

Ensuite, pour préparer vos traductions sur Lokalise, vous devez créer manuellement les clés de traduction avec le même nom que celui que vous utilisez pour les variables de contenu connecté de Braze.

Par exemple, créons une clé de traduction simple, `description` :
1. Ouvrez votre projet Lokalise, cliquez sur **Add Key**, entrez « description » dans le champ **Key**.
2. Tapez « Demo description » dans le champ **Base Language Value**.
3. Ajoutez « Web » dans la liste déroulante **Platforms**.
4. Lorsque vous êtes prêt, cliquez sur **Save**.

![Fenêtre modale d'ajout de clé dans Lokalise créant la clé de traduction « description ».]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

Votre clé de traduction devrait apparaître dans l'éditeur de projet :

![Éditeur de projet Lokalise affichant la clé de traduction nouvellement ajoutée.]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

##### Problèmes connus {#known-issues}

- Vos clés doivent être attribuées à la plateforme **Web**.
- Évitez d'utiliser des clés contenant des points (`.`) ou la chaîne de caractères `_on`. Par exemple, utilisez `this_is_the_key` au lieu de `this.is.the.key`, et `join_us_instagram` au lieu de `join_us_on_instagram`.

#### Étape 3 : Configurer l'application Braze sur Lokalise {#step-3-configure-the-braze-app-on-lokalise}

Ouvrez votre projet Lokalise et cliquez sur **Apps**. Recherchez et installez l'application Braze. L'écran suivant s'affiche :

![Configuration de Braze sur Lokalise indiquant l'ID du projet et l'URL des fichiers de traduction.]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

Dans le champ **Translation File URL**, Lokalise publie un fichier JSON contenant toutes les traductions de vos clés dans le projet. Vous obtiendrez autant d'URL de fichiers de traduction que de langues cibles dans votre projet. C'est pourquoi les URL des fichiers de traduction comportent deux parties :

1. La première partie du chemin URL est commune à toutes les langues.
2. Le nom du fichier JSON à la fin de l'URL est basé sur le code de la langue.

L'URL du fichier de traduction est celle dont vous aurez besoin pour configurer une Campaign Braze. Vous pouvez actualiser le contenu du fichier JSON en cliquant sur **Refresh**. Notez que l'URL restera la même et que vous n'aurez pas besoin de modifier votre appel au contenu connecté dans Braze.

##### URL de test {#test-url}

Pour tester cette URL, copiez-la et remplacez {% raw %}`{{${language}}}`{% endraw %} par un code de langue (par exemple, `en`) puis ouvrez cette URL dans votre navigateur. Vous obtiendrez un fichier JSON contenant vos clés et vos traductions :

![Aperçu dans le navigateur du fichier JSON de traduction exporté par Lokalise.]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

#### Étape 4 : Utiliser les traductions dans une Campaign Braze {#step-4-use-translations-in-braze-campaign}

##### Insérer un appel de contenu connecté {#insert-connected-content-call}

Lorsque vous êtes prêt, retournez dans Braze et ouvrez une Campaign existante ou créez-en une nouvelle. Nous allons créer une nouvelle Campaign par e-mail avec un exemple de contenu pour cet exemple. Cliquez sur **Edit Email Body**.

Pour insérer vos traductions, vous devez ajouter la requête de contenu connecté dans le code HTML, soit en haut du document, soit juste avant le premier endroit où une traduction est nécessaire. Vous pouvez le faire en insérant la balise suivante :

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Remplacez l'URL `https://exports.live.lokalise.cloud/...` par l'URL du fichier de traduction récupérée à l'étape précédente.

{% raw %}

- `{{${language}}}` signifie « insérer la langue de l'utilisateur à cet emplacement ». Vous pouvez également coder en dur le code de votre langue, par exemple `en.json`.
  - Pour vous assurer que le fichier JSON traduit approprié est récupéré pour chaque utilisateur, vous devez placer l'attribut de profil `{{${language}}}` ou un autre attribut personnalisé similaire contenant la langue de l'utilisateur à la fin de l'URL des fichiers de traduction (par exemple, `/{{${language}}}.json`). Les valeurs contenues dans ces attributs doivent correspondre au préfixe de chacun des fichiers JSON traduits. Cela permet de s'assurer que le fichier de traduction correct est renvoyé pour chaque utilisateur.
- `:save translations` enregistrera le contenu JSON dans la variable translations.

##### Afficher les traductions {#display-translations}

Utilisez maintenant la variable translations pour afficher les traductions souhaitées par leur clé.

Par exemple, pour afficher la clé `description`, utilisez `{{ translations.description }}`.

{% endraw %}
![Exemple dans l'éditeur d'e-mail Braze montrant les traductions par contenu connecté depuis Lokalise.]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

Enfin, enregistrez le modèle d'e-mail et prévisualisez-le. Vous devriez voir votre traduction s'afficher.

## Foire aux questions {#frequently-asked-questions}

### Que se passe-t-il si je supprime accidentellement une clé de Lokalise ? {#what-happens-if-i-accidentally-delete-a-key-from-lokalise}

La chaîne de caractères correspondante dans Braze n'aura plus de traduction.

### Si j'ai une locale `en` mais que je la remplace par `en-US` dans Lokalise, Braze la lira-t-il comme `en-US` ? {#if-i-have-an-en-locale-but-override-it-with-en-us-on-lokalise-will-braze-read-it-as-en-us}

Non, les codes ISO de locale doivent correspondre entre Braze et Lokalise.

### Peut-on utiliser le drapeau `:rerender` lors de la connexion au contenu Lokalise ? {#can-we-use-the-rerender-flag-when-connecting-lokalise-content}

Oui, bien sûr. Vous pouvez consulter la documentation de Braze pour savoir comment ajouter ce drapeau.

### Après avoir actualisé le fichier de traduction sur Lokalise, pourquoi ne vois-je pas de changements dans le contenu traduit sur Braze ? {#after-refreshing-the-translation-file-on-lokalise-why-cant-i-see-any-changes-in-the-translated-content-on-braze}

Braze met en cache le contenu traduit et son actualisation peut prendre quelques minutes. Si vous testez vos Campaigns et avez besoin de voir les résultats des traductions immédiatement, vous pouvez utiliser le paramètre `:cache_max_age` comme expliqué dans cet article de référence.