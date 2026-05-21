---
nav_title: Messages multilingues
article_title: Messages multilingues
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Cet article décrit les étapes pour utiliser les paramètres régionaux dans vos messages."
---

# Messages multilingues {#multi-language-messages}

> Après avoir ajouté des paramètres régionaux à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues au sein d'une seule notification push, d'un e-mail, d'une bannière, d'un message in-app ou d'un Content Block.

## Conditions préalables {#prerequisites}

Regardez la vidéo suivante pour un aperçu facultatif de la configuration et de l'utilisation des messages multilingues.

{% multi_lang_include video.html id="whfstwrel5" source="wistia" %}

{% tabs %}
{% tab Paramètres régionaux multilingues %}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Types de messages %}

| Fonctionnalité | Autorisations utilisateur requises |
| --- | --- |
| Types&nbsp;de&nbsp;messages | Vous avez besoin de ces autorisations pour ajouter des paramètres régionaux et des traductions aux Campaigns et aux Canvas :<br><br> <ul><li>Modifier les Campaigns</li><li>Modifier les Canvas</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables"}

{% endtab %}
{% tab Modèles %}

| Fonctionnalité | Autorisations utilisateur requises |
| --- | --- |
| Modèles | Vous avez besoin de ces autorisations pour le type de modèle auquel vous souhaitez ajouter des paramètres régionaux et des traductions :<br><br> <ul><li>Modifier les modèles d'e-mail</li><li>Modifier les modèles de messages in-app</li><li>Modifier les modèles de Content Blocks</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

{% endtab %}
{% endtabs %}

## Utiliser les paramètres régionaux {#use-locales}

### Étape 1 : Configurer les paramètres régionaux {#step-1-set-up-locales}

Avant de pouvoir ajouter des traductions à un message, vous devez d'abord [créer les paramètres régionaux que vous souhaitez prendre en charge]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/). Les paramètres régionaux définissent les variantes de langue (et éventuellement de région) disponibles pour l'envoi de messages.

### Étape 2 : Marquer le contenu pour la traduction {#step-2-mark-content-for-translation}

Encadrez le texte que vous souhaitez traduire avec les balises de traduction Liquid {% raw %}`{% translation your_id_here %}` et `{% endtranslation %}`{% endraw %} et attribuez un ID de balise. Les ID de balises de traduction doivent être uniques au sein d'un message. Envisagez d'utiliser des noms d'ID sémantiques qui décrivent clairement le texte, comme {% raw %}`{% translation header %}`{% endraw %}.

Voici un exemple de message marqué pour la traduction : {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Sélectionnez le texte que vous souhaitez traduire et utilisez le raccourci clavier **Cmd + Alt + L** (macOS) ou **Ctrl + Alt + L** (Windows) pour l'encadrer avec des balises de traduction.<br><br> Ce raccourci fonctionne dans tous les canaux prenant en charge les messages multilingues, à l'exception des éditeurs par glisser-déposer pour les e-mails et les Content Blocks. Pour ceux-ci, utilisez le bouton **Ajouter une personnalisation** dans la barre latérale gauche pour ajouter des balises de traduction.
{% endalert %}

#### Localiser les URL {#localize-urls}

Lors de la traduction du contenu, les URL nécessitent un traitement spécial pour éviter les liens brisés.

##### URL standard (statiques) {#standard-static-urls}

Les URL statiques sont saisies manuellement dans l'éditeur (par exemple, `https://example.com`). Nous recommandons également ce qui suit :

| Recommandation | Raison |
| --- | --- |
| Gardez le protocole (`https://`) en dehors des balises de traduction. N'encadrez que le domaine et le chemin (par exemple, `example.com/en`). | Les traducteurs peuvent accidentellement modifier ou supprimer des caractères spéciaux, ce qui entraîne des liens brisés. |
| N'incluez pas les paramètres de requête dans les balises de traduction (par exemple, `?utm_source=promo`). | Les traducteurs peuvent accidentellement modifier ou supprimer des caractères spéciaux, ce qui entraîne des liens brisés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL standard (statiques)" }

Une URL standard qui suit les deux recommandations est :

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### URL générées par Liquid {#liquid-generated-urls}

Si votre URL est générée avec Liquid (par exemple, {% raw %}`{% landing_page_url %}`{% endraw %}), nous recommandons ce qui suit :

| Recommandation | Raison |
| --- | --- |
| N'encadrez l'URL générée par Liquid dans des balises de traduction que si elle doit être localisée. | La syntaxe Liquid doit être soigneusement préservée pour s'afficher correctement. |
| N'incluez pas les paramètres de requête (par exemple, `?utm_source=promo`) dans les balises de traduction. | Les traducteurs peuvent accidentellement modifier ou supprimer des caractères spéciaux, ce qui entraîne des liens brisés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL générées par Liquid" }

Une URL générée par Liquid qui suit les deux recommandations est :

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
Si vous utilisez le [suivi des liens e-mail](#email-link-tracking) (aliasage de lien ou modèles de liens), une configuration supplémentaire est requise lorsque les URL sont encadrées par des balises de traduction.
{% endalert %}

#### Attributs et structure HTML {#html-attributes-and-structure}

N'encadrez que le texte lisible par l'humain dans les balises de traduction. Évitez d'encadrer les attributs HTML (tels que `class`, `style` ou `id`) ou tout autre code structurel. Les attributs HTML contrôlent la mise en page, le style et les fonctionnalités. Les encadrer dans des balises de traduction peut casser le formatage ou les styles dans les versions localisées de votre message.

Ce texte est correctement encadré :

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Texte incorrectement encadré %}

Ce texte est **incorrectement** encadré :

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### Étape 3 : Ajouter des paramètres régionaux à votre message {#step-3-add-locales-to-your-message}

Après avoir ajouté des balises de traduction à votre message, sélectionnez **Gérer les langues** dans l'éditeur (**Langues** dans les éditeurs par glisser-déposer pour les e-mails et les Content Blocks) et sélectionnez au moins un paramètre régional pour lequel vous souhaitez ajouter des traductions.

![Le menu déroulant Ajouter un paramètre régional avec des options pour sélectionner le paramètre régional par défaut ou les attributs personnalisés.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Content Blocks contenant des traductions {#content-blocks-containing-translation}

Si votre message contient des Content Blocks qui ont déjà des traductions enregistrées, vous n'avez pas besoin de les télécharger à nouveau. Les traductions enregistrées sont automatiquement appliquées lorsque le Content Block est ajouté à votre message.

Dans la fenêtre modale **Gérer les langues**, les Content Blocks avec des traductions enregistrées apparaissent dans la liste, aux côtés des paramètres régionaux qu'ils prennent en charge. Cela vous permet de voir quelles parties de votre message sont déjà localisées avant d'ajouter de nouvelles traductions.

![La section Gérer les langues avec une liste de Content Blocks ayant des traductions enregistrées.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Assurez-vous que chaque Content Block inclut des traductions pour chaque paramètre régional ajouté à votre message. Si un Content Block ne dispose pas de traductions pour l'un des paramètres régionaux que vous avez ajoutés, il s'affiche dans sa langue d'origine pour les utilisateurs de ce paramètre régional.
{% endalert %}

### Étape 4 : Ajouter des traductions {#step-4-add-translations}

Après avoir sélectionné les paramètres régionaux, ajoutez des traductions à votre message en utilisant l'une des méthodes suivantes :

![L'onglet Ajouter des traductions avec des options pour télécharger des traductions par CSV ou en se connectant à des partenaires de traduction.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab Télécharger un modèle CSV %}

Sélectionnez **Télécharger le modèle** pour télécharger un CSV contenant une matrice de vos ID de traduction et paramètres régionaux sélectionnés. Saisissez les traductions pour chaque paramètre régional. Téléchargez le fichier complété et les traductions seront appliquées à votre message.

{% alert important %}
Pour éviter les problèmes d'affichage avec les caractères non anglais, évitez d'utiliser Excel pour votre CSV de traduction.
{% endalert %}

![CSV avec des balises de traduction pour un titre, un texte d'offre, un montant d'offre et un CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Utiliser l'API de traduction %}

Utilisez l'API de traduction d'un partenaire pour gérer et mettre à jour les traductions dans vos Campaigns et Canvas. C'est utile si vous utilisez un système externe pour la localisation ou si vous souhaitez vous connecter directement à un partenaire de traduction.

Pour utiliser les endpoints de traduction avec les Canvas, incluez les paramètres suivants :
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
Lorsque vous utilisez l'API de traduction avec des étapes Canvas créées après le lancement du Canvas, le `message_variation_id` que vous transmettez à l'API sera vide ou blanc.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 5 : Prévisualiser les traductions {#step-5-preview-translations}

Pour prévisualiser votre message, sélectionnez l'option **Utilisateur multilingue** dans le menu déroulant **Prévisualiser en tant qu'utilisateur**. Cela vous permet de basculer entre différentes définitions de paramètres régionaux pour prévisualiser toutes les traductions de votre message.

![Prévisualisations des paramètres régionaux]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Gérer les traductions {#manage-translations}

### Dupliquer des étapes Canvas ou des Campaigns, et les traductions {#duplicate-canvas-steps-or-campaigns-and-translations}

Lorsque vous dupliquez une étape Canvas, une Campaign ou une variante, les traductions sont incluses. Cela est également vrai lors de la copie entre espaces de travail, à condition que les paramètres régionaux soient définis dans l'espace de travail de destination. Assurez-vous de vérifier et de mettre à jour les traductions en conséquence lorsque vous apportez des modifications à votre Canvas ou Campaign.

### Enregistrer les traductions dans les Content Blocks {#save-translations-in-content-blocks}

Les Content Blocks prennent en charge le multilingue de la même manière que les messages. Lors de la création ou de la modification de Content Blocks, vous pouvez marquer le contenu pour la traduction, ajouter des paramètres régionaux et télécharger des traductions à l'aide d'un CSV ou de l'[API de traduction]({{site.baseurl}}/api/endpoints/translations/).

Les traductions enregistrées restent associées au Content Block. Lorsque le bloc est ajouté à un message, ses traductions sont automatiquement incluses.

### Messages de droite à gauche {#right-to-left-messages}

Lorsque vous remplissez le fichier de traduction pour les langues écrites de droite à gauche (comme l'arabe), encadrez la traduction avec `span` afin qu'elle soit correctement formatée :

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### Suivi des liens e-mail {#email-link-tracking}

Dans les Campaigns par e-mail, Braze suit les liens en ajoutant des informations de suivi (paramètres de requête) à chaque URL. Ce comportement prend en charge à la fois l'[aliasage de lien]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing/) et les [modèles de liens]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template/).

Lorsqu'une URL est encadrée par des balises de traduction, Braze peut ne pas être en mesure de déterminer où ajouter ces informations de suivi. Pour garantir le bon fonctionnement, vous devez inclure un caractère spécial à la fin de l'URL pour indiquer où le suivi doit être ajouté.

Les URL utilisent deux caractères spéciaux pour contrôler ce fonctionnement :
  - `?` ajoute le suivi à une URL qui n'en possède pas encore.
  - `&` ajoute un suivi supplémentaire si un `?` est déjà présent dans l'URL. Une URL ne peut contenir qu'un seul `?`.

| URL | Contient&nbsp;`?` | Description | Exemple |
| --- | --- | --- | --- |
| URL standard | Non | Ajoutez `?` après la balise de traduction fermante si l'URL n'en contient pas déjà un. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| URL standard | Oui | Utilisez `&` à la fin de l'URL (après la balise de traduction fermante) si elle contient déjà `?`. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Générée par Liquid | Non | Utilisez `?` après les balises de traduction fermantes si l'URL générée n'en contient pas déjà un. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Générée par Liquid | Oui | Utilisez `&` après la balise de traduction fermante si l'URL générée contient déjà un `?`. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Suivi des liens e-mail" }

### Paramètres de langue et accessibilité {#language-settings-and-accessibility}

Commencez par [Langue d'accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/#accessibility-language) dans [Accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/) pour le contexte WCAG, le comportement par canal et éditeur (y compris les pages d'accueil), et les paramètres d'**accessibilité** au niveau du message.

Lorsque vous utilisez des **messages multilingues**, alignez la langue d'accessibilité avec chaque paramètre régional afin que les envois localisés déclarent la langue appropriée.

#### Configurer la langue d'accessibilité {#configuring-the-accessibility-language}

Vous pouvez définir la langue d'accessibilité à deux niveaux :

##### Au niveau du message {#message-level}

Au niveau du message, définissez la langue d'accessibilité dans la section **Accessibilité** des paramètres de votre message. Pour sélectionner une langue, utiliser Liquid et connaître les limitations par canal, consultez [Langue d'accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/#accessibility-language).

##### Au niveau du paramètre régional {#locale-level}

Pour les messages multilingues, définissez la langue d'accessibilité pour chaque paramètre régional dans les **Paramètres de localisation**. Vous pouvez utiliser {% raw %}`{{accessibility_language}}`{% endraw %} dans la section **Accessibilité** afin que la langue du document ou de la carte corresponde aux valeurs de ces paramètres régionaux.

Le fait que ce jeton apparaisse par défaut pour les nouveaux messages dépend du canal et de l'éditeur. Par exemple, les messages in-app et les bannières se comportent différemment des pages d'accueil et des e-mails par glisser-déposer. Consultez [Langue d'accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/#accessibility-language) pour plus de détails.

## Questions fréquemment posées {#frequently-asked-questions}

#### Quelles sont les limites pour les balises de traduction ? {#what-are-the-limits-for-translation-tags}

Lorsque vous utilisez des balises de traduction, les limites suivantes s'appliquent :

- Chaque message peut contenir jusqu'à 200 balises de traduction.
- Chaque texte par défaut (le contenu entre les balises de traduction) peut contenir jusqu'à 2 000 caractères.
- Les traductions par paramètre régional peuvent contenir jusqu'à 409 600 octets (environ 409,6&nbsp;Ko).

#### Puis-je modifier le texte traduit dans l'un de mes paramètres régionaux ? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

Oui. Commencez par effectuer la modification dans le CSV, puis téléchargez à nouveau le fichier pour mettre à jour le texte traduit.

### Braze fournit-il des traductions ? {#does-braze-provide-translations}

Non. Vous devez [fournir vos propres traductions](#step-4-add-translations) soit en téléchargeant un CSV, soit en utilisant l'API de traduction.

### Puis-je imbriquer des balises de traduction ? {#can-i-nest-translation-tags}

Non.

#### Puis-je encadrer des messages HTML entiers dans une balise de traduction ? {#can-i-wrap-entire-html-messages-in-a-translation-tag}

Non. En tant que bonne pratique, vous ne devez encadrer que le texte lisible par l'humain ou le contenu qui doit être localisé. Cela permet d'éviter les problèmes de formatage, de liens ou d'autres éléments non textuels.

De plus, envisagez d'encadrer des morceaux de texte plus petits et sémantiquement liés pour créer des traductions précises et éviter les limitations de performance ou de taille.

#### Puis-je modifier le texte traduit dans l'un de mes paramètres régionaux ?

Oui. Si vous utilisez un CSV, commencez par effectuer la modification dans le fichier, puis téléchargez-le à nouveau pour mettre à jour le texte traduit. Si vous utilisez l'[API de traduction]({{site.baseurl}}/api/endpoints/translations/), utilisez les endpoints de mise à jour pour effectuer des modifications.

#### Quelles validations ou vérifications supplémentaires Braze effectue-t-il ? {#what-validations-or-extra-checks-does-braze-do}

| Scénario | Validation dans Braze |
| --- | --- |
| Un message contient deux ou plusieurs ID de traduction identiques qui correspondent à des textes différents. | Ce fichier de traduction ne sera pas téléchargé. |
| Un fichier de traduction ne contient pas un ou plusieurs ID de balises de traduction. | Ce fichier de traduction ne sera pas importé. |
| Un fichier de traduction contient des paramètres régionaux absents du message. | Ce fichier de traduction ne sera pas importé. |
| Les balises de traduction doivent être ajoutées à un message avant de télécharger le modèle de traduction. | Ce fichier de traduction ne sera pas téléchargé. |
| Des balises de traduction trouvées dans votre fichier importé sont absentes de votre message. | Les traductions supplémentaires ne seront pas enregistrées dans le message. |
| {% raw %}Un message contient une ou plusieurs balises Liquid incorrectes. Pour les balises ouvrantes, utilisez `{% translation your_id_here %}`, fermez les balises de traduction avec `{% endtranslation %}`.{% endraw %} | Ce fichier de traduction ne sera pas téléchargé. |
| Un fichier de traduction contient un texte par défaut qui ne correspond pas à celui du message. | Les traductions sont ajoutées, mais le texte original du message n'est pas mis à jour. |
| Un ou plusieurs paramètres régionaux d'un message ont été supprimés dans les paramètres et n'existent plus. | Les traductions déjà ajoutées continuent d'exister dans le message. Si elles sont supprimées du message, les traductions sont perdues. |
| Les balises de traduction contiennent des URL complètes ou des URL générées par Liquid. | Les balises de traduction contenant des URL sont identifiées au cas où des problèmes de liens brisés ou de suivi des liens surviendraient. |
| Les balises de traduction incluent des paramètres de requête. | Les balises de traduction contenant des paramètres de requête sont identifiées au cas où des problèmes de liens brisés ou de suivi des liens surviendraient. |
| Les balises de traduction contiennent des attributs ou des structures HTML. | Les balises de traduction contenant des attributs ou des structures HTML sont identifiées au cas où des problèmes de styles et de formatage surviendraient. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quelles validations ou vérifications supplémentaires Braze effectue-t-il ?" }