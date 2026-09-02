---
nav_title: Messages multilingues
article_title: Messages multilingues
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Cet article décrit les étapes pour utiliser les paramètres régionaux dans vos messages."
---

# Messages multilingues {#multi-language-messages}

> Après avoir ajouté des paramètres régionaux à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues au sein d'une seule notification push, d'un e-mail, d'un webhook, d'une bannière, d'un message in-app ou d'un Content Block.

## Prérequis {#prerequisites}

{% tabs %}
{% tab Paramètres régionaux multilingues %}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Types de messages %}

| Fonctionnalité | Autorisations utilisateur requises |
| --- | --- |
| Types&nbsp;de&nbsp;messages | Vous avez besoin de ces autorisations pour ajouter des paramètres régionaux et des traductions aux Campaigns et aux Canvas :<br><br> {::nomarkdown} <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis"}

{% endtab %}
{% tab Modèles %}

| Fonctionnalité | Autorisations utilisateur requises |
| --- | --- |
| Modèles | Vous avez besoin de ces autorisations pour le type de modèle auquel vous souhaitez ajouter des paramètres régionaux et des traductions :<br><br> {::nomarkdown} <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Webhook Templates</li><li>Edit Content Block Templates</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

{% endtab %}
{% endtabs %}

## Utiliser les locales {#use-locales}

### Étape 1 : Configurer les locales {#step-1-set-up-locales}

Avant de pouvoir ajouter des traductions à un message, vous devez d'abord [créer les locales que vous souhaitez prendre en charge]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings). Les locales définissent les variantes de langue (et éventuellement de région) disponibles pour l'envoi de messages.

### Étape 2 : Marquer le contenu à traduire {#step-2-mark-content-for-translation}

Encadrez le texte que vous souhaitez traduire avec les balises de traduction Liquid {% raw %}`{% translation your_id_here %}` et `{% endtranslation %}`{% endraw %} et attribuez un ID de balise. Les ID de balise de traduction doivent être uniques au sein d'un message. Envisagez d'utiliser des noms d'ID sémantiques qui décrivent clairement le texte, comme {% raw %}`{% translation header %}`{% endraw %}.

Voici un exemple de message marqué pour la traduction : {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Mettez en surbrillance le texte que vous souhaitez traduire et utilisez le raccourci clavier **Cmd + Alt + L** (macOS) ou **Ctrl + Alt + L** (Windows) pour l'encadrer dans des balises de traduction.<br><br> Ce raccourci fonctionne dans tous les canaux prenant en charge la messagerie multilingue, à l'exception des éditeurs par glisser-déposer pour les e-mails et les Content Blocks. Pour ceux-ci, utilisez le bouton **Ajouter de la personnalisation** pour ajouter des balises de traduction.
{% endalert %}

#### Localiser les URL {#localize-urls}

Lors de la traduction de contenu, les URL nécessitent un traitement spécial pour éviter les liens brisés.

##### URL standard (statiques) {#standard-static-urls}

Les URL statiques sont saisies manuellement dans l'éditeur (par exemple, `https://example.com`). Nous recommandons également les pratiques suivantes :

| Recommandation | Justification |
| --- | --- |
| Conservez le protocole (`https://`) en dehors des balises de traduction. Encadrez uniquement le domaine et le chemin (par exemple, `example.com/en`). | Les traducteurs peuvent accidentellement modifier ou supprimer des caractères spéciaux, provoquant des liens brisés. |
| N'incluez pas les paramètres de requête à l'intérieur des balises de traduction (par exemple, `?utm_source=promo`). | Les traducteurs peuvent accidentellement modifier ou supprimer des caractères spéciaux, provoquant des liens brisés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL standard (statiques)" }

Une URL standard suivant les deux recommandations est :

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### URL générées par Liquid {#liquid-generated-urls}

Si votre URL est générée avec Liquid (par exemple, {% raw %}`{% landing_page_url %}`{% endraw %}), nous recommandons les pratiques suivantes :

| Recommandation | Justification |
| --- | --- |
| Encadrez l'URL générée par Liquid dans des balises de traduction uniquement si elle doit être localisée. | La syntaxe Liquid doit être soigneusement préservée pour s'afficher correctement. |
| N'incluez pas les paramètres de requête (par exemple, `?utm_source=promo`) à l'intérieur des balises de traduction. | Les traducteurs peuvent accidentellement modifier ou supprimer des caractères spéciaux, provoquant des liens brisés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL générées par Liquid" }

Une URL générée par Liquid suivant les deux recommandations est :

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
Si vous utilisez le [suivi de liens par e-mail](#email-link-tracking) (aliasage de lien ou modèles de lien), une configuration supplémentaire est nécessaire lorsque les URL sont encadrées dans des balises de traduction.
{% endalert %}

#### Attributs et structure HTML {#html-attributes-and-structure}

Encadrez uniquement le texte lisible par l'utilisateur dans les balises de traduction. Évitez d'encadrer les attributs HTML (tels que `class`, `style` ou `id`) ou tout autre code structurel. Les attributs HTML contrôlent la mise en page, le style et les fonctionnalités. Les encadrer dans des balises de traduction peut casser le formatage ou les styles dans les versions localisées de votre message.

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

### Étape 3 : Ajouter des locales à votre message {#step-3-add-locales-to-your-message}

Après avoir ajouté des balises de traduction à votre message, sélectionnez **Gérer les langues** dans l'éditeur (**Langues** dans les éditeurs par glisser-déposer pour les e-mails et les Content Blocks) et sélectionnez au moins une locale pour laquelle vous souhaitez ajouter des traductions.

![Le menu déroulant d'ajout de locale avec des options pour sélectionner la locale par défaut ou les attributs personnalisés.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Content Blocks contenant des traductions {#content-blocks-containing-translation}

Si votre message contient des Content Blocks ayant déjà des traductions enregistrées, vous n'avez pas besoin de télécharger à nouveau ces traductions. Les traductions enregistrées sont automatiquement appliquées lorsque le Content Block est ajouté à votre message.

Dans la fenêtre modale **Gérer les langues**, les Content Blocks avec des traductions enregistrées apparaissent dans la liste, aux côtés des locales qu'ils prennent en charge. Cela vous permet de voir quelles parties de votre message sont déjà localisées avant d'ajouter de nouvelles traductions.

![La section Gérer les langues avec une liste de Content Blocks ayant des traductions enregistrées.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Assurez-vous que chaque Content Block inclut des traductions pour toutes les locales ajoutées à votre message. Si un Content Block ne possède pas de traductions pour l'une des locales ajoutées, il s'affiche dans sa langue d'origine pour les utilisateurs de cette locale.
{% endalert %}

### Étape 4 : Ajouter des traductions {#step-4-add-translations}

Après avoir sélectionné les locales, ajoutez des traductions à votre message en utilisant l'une des méthodes suivantes :

![L'onglet Ajouter des traductions avec des options pour télécharger les traductions par CSV ou en se connectant à des partenaires de traduction.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab Télécharger un modèle CSV %}

Sélectionnez **Télécharger le modèle** pour télécharger un CSV contenant une matrice de vos ID de traduction sélectionnés et de vos locales.

{% alert important %}
Pour éviter les problèmes d'affichage avec les caractères non anglais, évitez d'utiliser Excel pour votre CSV de traduction.
{% endalert %}

Lorsque vous remplissez le modèle, traduisez uniquement le contenu textuel pour chaque locale. Si des balises HTML sont présentes dans le modèle téléchargé, laissez-les telles quelles et traduisez uniquement le texte à l'intérieur des balises.

Par exemple, si le modèle contient :

```
<p style="margin:0;margin-bottom:0">A charming bakery dedicated to crafting artisanal breads.</p>
```

Traduisez uniquement le texte `A charming bakery dedicated to crafting artisanal breads.` et conservez les balises HTML `<p style="margin:0;margin-bottom:0">` et `</p>` telles quelles.

Ensuite, téléchargez le fichier complété et les traductions seront appliquées à votre message.

![CSV avec des balises de traduction pour un titre, un texte d'offre, un montant d'offre et un CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Utiliser l'API de traduction %}

Utilisez l'API de traduction d'un partenaire pour gérer et mettre à jour les traductions dans vos Campaigns, Canvas, Content Blocks, modèles d'e-mail et modèles de webhook. Cela s'avère utile si vous utilisez un système externe pour la localisation ou si vous souhaitez vous connecter directement à un partenaire de traduction.

Pour utiliser les endpoints de traduction avec les Canvas, incluez les paramètres suivants :
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
Lorsque vous utilisez l'API de traduction avec des étapes de Canvas créées après le lancement du Canvas, le `message_variation_id` que vous transmettez à l'API sera vide ou blanc.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 5 : Prévisualiser les traductions {#step-5-preview-translations}

Pour prévisualiser votre message, sélectionnez l'option **Utilisateur multilingue** dans le menu déroulant **Prévisualiser en tant qu'utilisateur**. Cela vous permet de basculer entre différentes définitions de locale pour prévisualiser toutes les traductions de votre message.

![Aperçu des locales]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Gérer les traductions {#manage-translations}

### Dupliquer des étapes Canvas ou des Campaigns, et les traductions {#duplicate-canvas-steps-or-campaigns-and-translations}

Lorsque vous dupliquez une étape Canvas, une Campaign ou une variante, les traductions sont incluses. Cela vaut également pour la copie entre espaces de travail, à condition que les locales soient définies dans l'espace de travail de destination. Veillez à vérifier et à mettre à jour les traductions en conséquence lorsque vous apportez des modifications à votre Canvas ou Campaign.

### Enregistrer les traductions dans les Content Blocks {#save-translations-in-content-blocks}

Les Content Blocks prennent en charge le multilingue de la même manière que les messages. Lors de la création ou de la modification de Content Blocks, vous pouvez marquer le contenu pour traduction, ajouter des locales et télécharger des traductions à l'aide d'un fichier CSV ou de l'[API de traduction]({{site.baseurl}}/api/endpoints/translations).

Les traductions enregistrées restent associées au Content Block. Lorsque le bloc est ajouté à un message, ses traductions sont automatiquement incluses.

### Messages de droite à gauche {#right-to-left-messages}

Lorsque vous remplissez le fichier de traduction pour des langues écrites de droite à gauche (comme l'arabe), encadrez la traduction avec `span` afin qu'elle soit correctement formatée :

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### Suivi des liens dans les e-mails {#email-link-tracking}

Dans les Campaigns par e-mail, Braze suit les liens en ajoutant des informations de suivi (paramètres de requête) à chaque URL. Ce comportement prend en charge à la fois l'[aliasage de lien]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) et le [templating de lien]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template).

Lorsqu'une URL est encadrée par des balises de traduction, Braze peut ne pas être en mesure de déterminer où ajouter ces informations de suivi. Pour garantir le bon fonctionnement, vous devez inclure un caractère spécial à la fin de l'URL pour indiquer où le suivi doit être ajouté.

Les URL utilisent deux caractères spéciaux pour contrôler ce fonctionnement :
  - `?` ajoute le suivi à une URL qui n'en contient pas encore.
  - `&` ajoute un suivi supplémentaire si un `?` est déjà présent dans l'URL. Une URL ne peut contenir qu'un seul `?`.

| URL | Contient&nbsp;`?` | Description | Exemple |
| --- | --- | --- | --- |
| URL standard | Non | Ajoutez `?` après la balise de fermeture de traduction si l'URL n'en contient pas déjà. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| URL standard | Oui | Utilisez `&` à la fin de l'URL (après la balise de fermeture de traduction) si elle contient déjà `?`. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Générée par Liquid | Non | Utilisez `?` après les balises de fermeture de traduction si l'URL générée n'en contient pas déjà. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Générée par Liquid | Oui | Utilisez `&` après la balise de fermeture de traduction si l'URL générée contient déjà un `?`. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Suivi des liens dans les e-mails" }

### Paramètres de langue et accessibilité {#language-settings-and-accessibility}

Commencez par [Langue d'accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language) dans [Accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility) pour le contexte WCAG, le comportement par canal et éditeur (y compris les pages de destination), et les paramètres d'**accessibilité** au niveau du message.

Lorsque vous utilisez des **messages multilingues**, alignez la langue d'accessibilité avec chaque locale afin que les envois localisés déclarent la langue appropriée.

#### Configurer la langue d'accessibilité {#configuring-the-accessibility-language}

Vous pouvez définir la langue d'accessibilité à deux niveaux :

##### Niveau du message {#message-level}

Au niveau du message, définissez la langue d'accessibilité dans la section **Accessibilité** des paramètres de votre message. Pour le choix d'une langue, l'utilisation de Liquid et les limitations par canal, consultez [Langue d'accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language).

##### Niveau de la locale {#locale-level}

Pour les messages multilingues, définissez la langue d'accessibilité pour chaque locale dans les **paramètres de localisation**. Vous pouvez utiliser {% raw %}`{{accessibility_language}}`{% endraw %} dans la section **Accessibilité** afin que la langue du document ou de la carte corresponde aux valeurs de ces locales.

Le fait que ce jeton apparaisse par défaut pour les nouveaux messages dépend du canal et de l'éditeur. Par exemple, les messages in-app et les Banners se comportent différemment des pages de destination et des e-mails en glisser-déposer. Consultez [Langue d'accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language) pour plus de détails.

## Questions fréquemment posées {#frequently-asked-questions}

### Quelles sont les limites pour les tags de traduction ? {#what-are-the-limits-for-translation-tags}

Lors de l'utilisation des tags de traduction, les limites suivantes s'appliquent :

- Chaque message peut contenir jusqu'à 200 tags de traduction.
- Chaque texte par défaut (le contenu entre les tags de traduction) peut contenir jusqu'à 2 000 caractères.
- Les traductions par locale peuvent contenir jusqu'à 409 600 octets (environ 409,6&nbsp;Ko).

### Pourquoi est-ce que je reçois une erreur lors du téléchargement de modèles d'e-mail multilingues ? {#why-am-i-receiving-an-error-when-downloading-multi-language-email-templates}

Si vous rencontrez des erreurs lors du téléchargement de modèles d'e-mail multilingues, les tags de traduction encapsulent peut-être des attributs HTML ou du style CSS qui entrent en conflit avec la façon dont Braze traite les corps des e-mails.

Braze traite le corps HTML et le corps en texte brut comme des composants distincts du même message. Lorsque les tags de traduction incluent des références `href` et du style CSS, cela peut entraîner des tags conflictuels qui empêchent le téléchargement correct du modèle.

Pour résoudre ce problème :
- Excluez les références `href` et le style CSS des tags de traduction.
- N'encapsulez que le contenu textuel lisible par l'humain dans les tags de traduction, comme décrit dans [Attributs et structure HTML](#html-attributes-and-structure).
- Pour les URL, suivez les recommandations dans [Localiser les URL](#localize-urls).

#### Puis-je modifier le texte traduit dans l'une de mes locales ? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

Oui. Modifiez d'abord le fichier CSV, puis téléchargez-le à nouveau pour appliquer la modification au texte traduit.

### Braze fournit-il des traductions ? {#does-braze-provide-translations}

Non. Vous devez [fournir vos propres traductions](#step-4-add-translations) soit en téléchargeant un CSV, soit en utilisant l'API de traduction.

### Puis-je imbriquer des tags de traduction ? {#can-i-nest-translation-tags}

Non.

#### Puis-je encapsuler l'intégralité d'un message HTML dans un tag de traduction ? {#can-i-wrap-entire-html-messages-in-a-translation-tag}

Non. En tant que bonne pratique, vous ne devez encapsuler que le texte lisible par l'humain ou le contenu qui doit être localisé. Cela permet d'éviter les problèmes de mise en forme, de liens ou d'autres éléments non textuels.

De plus, envisagez d'encapsuler de plus petits morceaux de texte sémantiquement liés pour créer des traductions précises et éviter les limitations de performance ou de taille.

#### Puis-je modifier le texte traduit dans l'une de mes locales ?

Oui. Si vous utilisez un CSV, modifiez d'abord le fichier, puis téléchargez-le à nouveau pour appliquer la modification au texte traduit. Si vous utilisez l'[API de traduction]({{site.baseurl}}/api/endpoints/translations), utilisez les endpoints de mise à jour pour effectuer les modifications.

#### Quelles validations ou vérifications supplémentaires Braze effectue-t-il ? {#what-validations-or-extra-checks-does-braze-do}

| Scénario | Validation dans Braze |
| --- | --- |
| Un message contient deux ou plusieurs ID de traduction identiques correspondant à des textes différents. | Ce fichier de traduction ne sera pas téléchargé. |
| Un fichier de traduction ne contient pas un ou plusieurs ID de tags de traduction. | Ce fichier de traduction ne sera pas téléversé. |
| Un fichier de traduction contient des locales absentes du message. | Ce fichier de traduction ne sera pas téléversé. |
| Les tags de traduction doivent être ajoutés à un message avant de télécharger le modèle de traduction. | Ce fichier de traduction ne sera pas téléchargé. |
| Des tags de traduction trouvés dans votre fichier téléversé sont absents de votre message. | Les traductions supplémentaires ne seront pas enregistrées dans le message. |
| {% raw %}Un message contient une ou plusieurs étiquettes Liquid non valides. Pour les étiquettes d'ouverture, utilisez `{% translation your_id_here %}` ; fermez les tags de traduction avec `{% endtranslation %}`.{% endraw %} | Ce fichier de traduction ne sera pas téléchargé. |
| Un fichier de traduction contient du texte par défaut qui ne correspond pas à celui du message. | Les traductions sont ajoutées, mais le texte original du message n'est pas mis à jour. |
| Une ou plusieurs locales d'un message ont été supprimées dans les paramètres et n'existent plus. | Les traductions déjà ajoutées continuent d'exister dans le message. Si elles sont supprimées du message, les traductions sont perdues. |
| Les tags de traduction contiennent des URL complètes ou des URL générées par Liquid. | Les tags de traduction contenant des URL sont identifiés au cas où des problèmes de liens brisés ou de suivi de liens surviendraient. |
| Les tags de traduction incluent des paramètres de requête. | Les tags de traduction contenant des paramètres de requête sont identifiés au cas où des problèmes de liens brisés ou de suivi de liens surviendraient. |
| Les tags de traduction contiennent des attributs ou des structures HTML. | Les tags de traduction contenant des attributs ou des structures HTML sont identifiés au cas où des problèmes de styles et de mise en forme surviendraient. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quelles validations ou vérifications supplémentaires Braze effectue-t-il ?" }