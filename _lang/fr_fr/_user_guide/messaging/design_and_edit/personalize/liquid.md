---
nav_title: Référence Liquid
article_title: Référence Liquid
page_order: 3
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Référence Liquid"
guide_top_text: "Liquid est un langage de modèles open source créé par Shopify et utilisé par Braze pour alimenter la personnalisation dynamique. Au lieu d'envoyer un message statique à tout le monde, Liquid vous permet de créer des modèles dont le contenu s'adapte en fonction des données de profil, du comportement ou de la langue de chaque destinataire."
description: "Cette page de destination couvre tout ce qui concerne Liquid : les étiquettes de personnalisation prises en charge, les filtres, la définition de valeurs par défaut, et bien plus encore."

guide_featured_title: "Articles de la section"
guide_featured_list:
- name: Utiliser Liquid
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid
  image: /assets/img/braze_icons/beaker-02.svg
- name: Étiquettes de personnalisation prises en charge
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags
  image: /assets/img/braze_icons/tag-01.svg
- name: Opérateurs
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/operators
  image: /assets/img/braze_icons/code-02.svg
- name: Filtres
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/filters
  image: /assets/img/braze_icons/flag-02.svg
- name: Filtres avancés
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters
  image: /assets/img/braze_icons/settings-01.svg
- name: Définir des valeurs par défaut
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values
  image: /assets/img/braze_icons/table.svg
- name: Logique conditionnelle dans les messages
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic
  image: /assets/img/braze_icons/columns-01.svg
- name: Annuler des messages
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Bibliothèque de cas d'utilisation Liquid
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases
  image: /assets/img/braze_icons/list.svg
- name: Tutoriels
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/tutorials
  image: /assets/img/braze_icons/book-open-01.svg
- name: Questions fréquentes
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/faq
  image: /assets/img/braze_icons/annotation-question.svg

---

## À propos de Liquid {#about-liquid}

Liquid fait le lien entre votre message et les données de vos utilisateurs. Lorsque vous envoyez un message, Braze analyse le texte à la recherche de syntaxe Liquid. Quand il en trouve, il récupère les données pertinentes pour cet utilisateur spécifique et remplace le code par la valeur réelle avant l'envoi du message.

Par exemple, vous pouvez récupérer un attribut personnalisé d'un profil utilisateur correspondant à un type de données entier, puis arrondir cette valeur au nombre entier le plus proche. Pour en savoir plus sur la syntaxe et l'utilisation de Liquid, consultez [**Étiquettes de personnalisation prises en charge**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

Le langage de modèles Liquid prend en charge l'utilisation d'objets, d'étiquettes et de filtres.

- Les [**objets**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) vous permettent d'insérer des attributs personnalisés dans vos messages.
- Les [**étiquettes**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) vous permettent d'insérer des données dans vos messages et d'utiliser une logique conditionnelle pour envoyer des messages si certaines conditions sont remplies. Par exemple, vous pouvez utiliser des étiquettes pour inclure une logique intelligente, comme des instructions « if », dans vos campagnes.
- Les [**filtres**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/) vous permettent de reformater les attributs personnalisés et le contenu dynamique. Par exemple, vous pourriez utiliser le [filtre `date`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#date-filter) pour convertir un horodatage, tel que *2016-09-07 08:43:50 UTC*, en une date, telle que *7 septembre 2016*.

{% alert warning %}
Braze ne prend actuellement pas en charge 100 % du Liquid de Shopify, mais seulement certaines parties que nous avons tenté de décrire dans notre documentation. Nous vous recommandons vivement de tester tous les messages utilisant Liquid avant de les envoyer afin de réduire le risque d'erreurs ou d'utilisation de Liquid non pris en charge.
{% endalert %}

### Prise en charge de Liquid 5 {#liquid-5-support}

Braze prend en charge Liquid jusqu'à **Liquid 5 de Shopify** inclus. L'implémentation de Liquid prend en charge les types d'étiquettes de personnalisation syntaxiques et le contrôle des espaces. Pour plus d'informations sur les étiquettes spécifiques, consultez les [étiquettes de syntaxe]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#syntax-tags).

Les nouveaux filtres de tableaux et filtres mathématiques suivants sont disponibles dans votre Liquid lors de la création de vos messages.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Consultez [Filtres]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/) pour les définitions.

## Termes à connaître {#terms-to-know}

Ces termes sont réinterprétés à partir de la [**documentation de Shopify**](https://shopify.github.io/liquid/basics/introduction/) en fonction de notre niveau de prise en charge.

{% raw %}

| Terme | Définition | Exemple |
|---|---|---|
| Liquid | Un langage de modèles couramment utilisé, orienté client, créé par Shopify et écrit en Ruby, utilisé pour charger et extraire du contenu dynamique. | `{{${first_name}}}` insère le prénom d'un utilisateur dans un message. |
| Objet | Une notation d'une variable et de l'emplacement du nom de variable prévu qui indique à Liquid où afficher le contenu dans le message. | `{{${city}}}` insère la ville d'un utilisateur dans un message. |
| Étiquette de logique conditionnelle | Utilisée pour créer de la logique et contrôler le flux du contenu des messages. Dans Braze, les étiquettes de logique conditionnelle servent à créer des exceptions et des variations dans les messages en fonction de certains critères prédéfinis. | ```{% if ${language} == 'en' %}``` déclenchera votre message d'une manière spécifique si un utilisateur a défini « anglais » comme langue. |
| Filtres | Utilisés pour modifier, affiner ou reformater la sortie de l'objet Liquid. Souvent utilisés pour créer des opérations mathématiques. | ```{{"Big Sale" | upcase}}``` fera apparaître les mots « Big Sale » sous la forme « BIG SALE » dans le message. |
| Opérateurs | Utilisés dans les messages pour créer des dépendances ou des critères pouvant affecter le message que votre utilisateur reçoit. | Si un utilisateur remplit les critères définis dans un message balisé avec `{% custom_attribute.${Total_Revenue} > 0%}`, il recevra le message. Sinon, il recevra un autre message désigné (ou non), selon ce que vous avez configuré. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Termes à connaître" }

{% endraw %}

<br>