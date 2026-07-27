---
nav_title: Outils du tableau de bord
article_title: Outils du tableau de bord pour la personnalisation
page_order: 0
description: "Cet article de référence décrit l'expérience Ajouter une personnalisation dans les éditeurs de messages et de pages d'accueil de Braze, y compris le Liquid pré-formaté, les valeurs par défaut et les améliorations de l'éditeur Liquid telles que les étiquettes de couleur et les suggestions prédictives."
---

# Outils du tableau de bord pour la personnalisation {#dashboard-tools-for-personalization}

> Utilisez les outils du tableau de bord de Braze pour insérer de la personnalisation Liquid sans avoir à écrire chaque balise manuellement. Le flux **Ajouter une personnalisation** génère la syntaxe appropriée pour vous, et l'éditeur Liquid vous aide à lire et à enrichir vos modèles rapidement.

Pour les règles de syntaxe Liquid, les balises prises en charge et les modèles avancés, consultez [Utiliser Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) et [Balises de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Ajouter de la personnalisation dans les éditeurs et les paramètres {#add-personalization-in-composers-and-settings}

L'outil **Add Personalization** apparaît à proximité des champs de texte modélisés dans l'ensemble du tableau de bord, notamment :

- **Les étapes de Campaign et de Canvas** pour les canaux qui prennent en charge Liquid dans le corps ou les en-têtes (par exemple, l'e-mail, les notifications push, les SMS, les messages in-app, les Content Cards et les webhooks).
- **Les éditeurs par glisser-déposer**, où le contrôle se trouve souvent dans la barre d'outils du bloc ou de l'éditeur. Par exemple, dans les messages in-app par glisser-déposer, vous pouvez sélectionner **Add Personalization**, choisir un type de personnalisation, puis placer l'extrait de code généré dans votre contenu avant de prévisualiser sous **Preview & Test**. Pour des notes spécifiques à chaque canal, consultez l'article sur le glisser-déposer ou l'éditeur de votre canal (comme [Paramètres de style des messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#add-liquid) ou [Créer un e-mail par glisser-déposer]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)).
- **Les éditeurs spécialisés** qui proposent un sélecteur de personnalisation — par exemple, les [recommandations d'articles]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations) utilisent des options de **Personalization Type** comme **Item Recommendation** dans le même type de fenêtre.
- **Les pages de destination**, où vous pouvez ajouter de la personnalisation Liquid dans l'éditeur par glisser-déposer ou dans les paramètres de page et de bloc. Pour plus de détails, consultez [Personnaliser les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages).

## Insérer des variables pré-formatées et des valeurs par défaut {#insert-pre-formatted-variables-and-defaults}

L'outil **Ajouter une personnalisation** vous aide à insérer du Liquid avec des valeurs par défaut optionnelles afin que des données de profil vides ne cassent pas votre texte.

![La fenêtre modale Ajouter une personnalisation qui apparaît après avoir sélectionné l'insertion de personnalisation. La fenêtre modale comporte des champs pour le type de personnalisation, l'attribut, une valeur par défaut optionnelle, et affiche un aperçu de la syntaxe Liquid.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

L'outil insère du Liquid avec la valeur par défaut que vous avez spécifiée à l'endroit où se trouvait votre curseur. Le point d'insertion est également indiqué par la zone d'aperçu, qui affiche le texte avant et après. Si un bloc de texte est surligné, le texte surligné sera remplacé.

![Un GIF de la fenêtre modale Ajouter une personnalisation montrant l'utilisateur qui saisit « fellow traveler » comme valeur par défaut, et la fenêtre modale remplaçant le texte surligné « name » dans le compositeur par l'extrait de code Liquid.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

Vous pouvez toujours taper {% raw %}`{{`{% endraw %} dans de nombreux compositeurs pour utiliser l'autocomplétion, ou coller des tags provenant d'ailleurs ; pour plus de détails, consultez [Insérer des tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#inserting-tags) dans **Utiliser Liquid**.

### Assigner des variables {#assign-variables}

{% raw %}
Certaines opérations en Liquid nécessitent de stocker la valeur que vous souhaitez manipuler sous forme de variable. C'est souvent le cas lorsque votre instruction Liquid inclut plusieurs attributs, propriétés d'événement ou filtres.

Par exemple, imaginons que vous souhaitiez additionner deux entiers de données personnalisées.

#### Exemple Liquid incorrect {#incorrect-liquid-example}

Vous ne pouvez pas utiliser :

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Ce code Liquid ne fonctionne pas car vous ne pouvez pas référencer plusieurs attributs sur une seule ligne ; vous devez assigner une variable à au moins une de ces valeurs avant que les fonctions mathématiques ne s'exécutent. Additionner deux attributs personnalisés nécessite deux lignes de Liquid : une pour assigner l'attribut personnalisé à une variable, et une pour effectuer l'addition.

#### Exemple Liquid correct {#correct-liquid-example}

Vous pouvez utiliser :

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### Tutoriel : utiliser des variables pour calculer un solde {#tutorial-using-variables-to-calculate-a-balance}

Calculons le solde actuel d'un utilisateur en additionnant le solde de sa carte cadeau et le solde de ses récompenses :

Tout d'abord, utilisez le tag `assign` pour substituer l'attribut personnalisé `current_rewards_balance` par le terme « balance ». Cela signifie que vous disposez maintenant d'une variable nommée `balance`, que vous pouvez manipuler.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Ensuite, nous utiliserons le filtre `plus` pour combiner le solde de la carte cadeau de chaque utilisateur avec son solde de récompenses, représenté par `{{balance}}`.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
Vous vous retrouvez à assigner les mêmes variables dans chaque message ? Au lieu de réécrire le tag `assign` à chaque fois, vous pouvez enregistrer ce tag en tant que bloc de contenu et le placer en haut de votre message.<br><br>

1. [Créez un bloc de contenu]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block).
2. Donnez un nom à votre bloc de contenu (sans espaces ni caractères spéciaux).
3. Sélectionnez **Modifier** en bas de la page.
4. Saisissez vos tags `assign`.

Tant que le bloc de contenu se trouve en haut de votre message, chaque fois que la variable est insérée dans votre message en tant qu'objet, elle fera référence à l'attribut personnalisé que vous avez choisi !
{% endalert %}

## Améliorations de l'éditeur Liquid {#liquid-editor-enhancements}

Ces comportements du tableau de bord facilitent l'utilisation de Liquid lors de la rédaction de vos messages.

### Étiquettes de couleur {#color-labels}

Chaque élément Liquid correspond à une couleur, ce qui vous permet de différencier vos éléments Liquid d'un coup d'œil dans votre éditeur Liquid.

![Diagramme des différentes étiquettes de couleur pour les éléments Liquid.]({% image_buster /assets/img/liquid_color_code.png %})

### Liquid prédictif {#predictive-liquid}

Vous pouvez également utiliser le Liquid prédictif pour les attributs personnalisés, les noms d'attributs et bien plus encore lors de la création de vos messages personnalisés.

![Braze suggérant différents attributs Liquid à mesure que du texte est saisi dans un champ.]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Étapes suivantes {#next-steps}

- [Utiliser Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) — syntaxe, `assign`, conditions et filtres dans Braze
- [Définir des valeurs par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) — valeurs par défaut dans Liquid au-delà de la fenêtre modale
- [Filtres]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters) — formater les dates, effectuer des calculs, manipuler les chaînes de caractères, et plus encore