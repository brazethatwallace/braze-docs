---
nav_title: Blocs de contenu
article_title: Blocs de contenu
alias: "/dnd/content_blocks/"
page_order: 4
description: "Découvrez comment créer, utiliser et gérer des blocs de contenu réutilisables dans vos Campaigns et Canvas Braze."
page_type: reference
tool:
  - Templates
  - Media

---

# Blocs de contenu {#content-blocks}

> Les blocs de contenu vous permettent de gérer du contenu réutilisable et cross-canal depuis un emplacement unique et centralisé. Utilisez-les pour créer une apparence cohérente dans vos Campaigns, distribuer les mêmes codes promotionnels sur différents canaux, ou créer des ressources prédéfinies pour un envoi de messages cohérent à grande échelle. Vous pouvez également créer et gérer vos blocs de contenu [via l'API]({{site.baseurl}}/api/endpoints/templates).

## Créer un Content Block {#create-a-content-block}

Il existe deux types de Content Blocks : glisser-déposer et HTML. Chaque type correspond à son éditeur.

{% tabs %}
{% tab Glisser-déposer %}

{% multi_lang_include messaging/create_content_block.md location="dnd" %}

{% alert important %}
Chaque Content Block en glisser-déposer est limité à une seule ligne. Cependant, vous pouvez utiliser les blocs éditeur en glisser-déposer pour créer et personnaliser le Content Block selon vos besoins en matière d'e-mail.
{% endalert %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include messaging/create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Spécifications des Content Blocks {#content-block-specifications}

| Attribut du Content Block | Spécifications |
|---|---|
| Nom | Champ obligatoire avec un maximum de 100 caractères. Les noms de Content Blocks ne peuvent contenir que des lettres (A-Z), des chiffres (0-9), des tirets (`-`) et des underscores (`_`). Les espaces et autres caractères spéciaux ne sont pas autorisés et sont automatiquement convertis (par exemple, les espaces sont remplacés par des underscores). Les noms ne peuvent pas être modifiés après l'enregistrement du Content Block, et vous ne pouvez pas réutiliser le nom d'un Content Block précédent, même s'il est archivé. |
| Description | (facultatif) Maximum de 250 caractères. Décrivez le Content Block afin que les autres utilisateurs de Braze sachent à quoi il sert et où il est utilisé. |
| Taille du contenu | Maximum de 50 Ko. |
| Emplacement | Les Content Blocks ne peuvent pas être utilisés dans un pied de page d'e-mail, mais vous pouvez [créer un Content Block qui inclut un pied de page](#email-footers) pour l'utiliser dans vos e-mails. |
| Création | Éditeur HTML ou éditeur glisser-déposer. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications des Content Blocks" }

{% alert tip %}
Lors de la création de Content Blocks, il peut être utile de visualiser le HTML et le Liquid en ajoutant des sauts de ligne. Si ces sauts de ligne sont laissés lors de l'envoi, vous risquez d'avoir des espaces superflus qui peuvent affecter le rendu du bloc. Pour éviter cela, utilisez l'étiquette **Capture** sur votre bloc avec le filtre **&#124; strip**.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Utiliser les Content Blocks {#use-content-blocks}

Après avoir créé votre Content Block, vous pouvez l'insérer dans vos messages à l'aide de l'éditeur ou de Liquid.

### Utiliser l'éditeur par glisser-déposer {#using-the-editor}

Pour ajouter un Content Block dans l'éditeur par glisser-déposer :

1. Accédez à l'onglet **Lignes** dans l'éditeur et sélectionnez **Content Blocks**.
2. Glissez et déposez votre Content Block dans l'éditeur d'e-mail.
3. (Facultatif) Ajustez la largeur de votre Content Block en sélectionnant le bouton dans le menu de navigation. La largeur par défaut est de 100 % lorsqu'elle n'est pas spécifiée dans les paramètres de style global de votre e-mail ; sinon, les paramètres globaux seront appliqués. <br><br>![Une flèche à double sens avec une option pour modifier la largeur.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

{% alert note %}
Les Content Blocks ajoutés par glisser-déposer ne sont **pas liés** au Content Block d'origine. Pour voir les modifications apportées à l'original, glissez-le à nouveau dans l'éditeur d'e-mail.
{% endalert %}

Un désalignement dans l'éditeur par glisser-déposer peut se produire lorsque plusieurs Content Blocks sont ajoutés à un seul bloc de ligne. Essayez d'utiliser des blocs de ligne séparés pour maintenir l'alignement de votre contenu au niveau de la ligne.

### Utiliser Liquid {#using-liquid}

Pour insérer un Content Block à l'aide de Liquid :

1. Copiez l'**étiquette Liquid du Content Block** depuis la section **Détails du Content Block**.
2. Insérez l'étiquette Liquid du Content Block dans le message. Vous pouvez également commencer à saisir le Liquid et laisser l'étiquette se compléter automatiquement.

Dans l'éditeur par glisser-déposer, vous pouvez également ajouter un Content Block via le panneau **Personnalisation** :

1. Accédez à votre Campaign d'e-mail et sélectionnez **Modifier le corps de l'e-mail**.
2. Cliquez sur <i class="fas fa-plus"></i> **Personnalisation**.
3. Sélectionnez **Content Blocks** dans le menu déroulant **Type de personnalisation**.
4. Sélectionnez le nom de votre Content Block dans le champ **Attribut**.
5. Copiez et collez l'extrait de code Liquid dans un bloc éditeur de texte. <br>![L'onglet Ajouter une personnalisation avec les options disponibles.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

{% alert important %}
Les Content Blocks insérés via Liquid **sont liés** au Content Block d'origine et refléteront toute modification apportée au modèle.
{% endalert %}

## Prévisualiser les Content Blocks {#preview-content-blocks}

Après avoir ajouté un Content Block dans une Campaign ou un Canvas actif, vous pouvez le prévisualiser depuis la bibliothèque de Content Blocks en survolant le Content Block et en sélectionnant l'icône <i class="fa fa-eye preview-icon"></i> **Prévisualiser**.

Cette prévisualisation inclut des informations sur le Content Block, telles que son créateur, les tags, la date de création, la date de dernière modification, la description, le type d'éditeur, le nombre d'inclusions avec des détails (une liste cliquable de messages ou de Content Blocks qui utilisent ce Content Block), ainsi qu'un aperçu réel du Content Block.

{% alert note %}
Lorsque vous vérifiez où un Content Block est utilisé, examinez chaque message ou étape lié(e) individuellement pour confirmer son statut.
{% endalert %}

## Imbriquer des Content Blocks {#nest-content-blocks}

Les Content Blocks peuvent être imbriqués, mais une seule fois. Vous pouvez imbriquer le Content Block A dans le Content Block B, mais vous ne pouvez pas ensuite imbriquer le Content Block B dans le Content Block C.

{% alert warning %}
Rien ne vous empêche d'imbriquer un troisième niveau de Content Block, mais le contenu ne s'affichera pas au-delà du deuxième niveau d'imbrication. Le contenu et l'extrait Liquid sont supprimés du message.
{% endalert %}

Les liens à l'intérieur d'un Content Block imbriqué sont comptabilisés dans le nombre total de liens du message parent. Si vous utilisez un seul Content Block avec de nombreux liens conditionnels, tels que des URL spécifiques à chaque pays pour la localisation, le message parent peut accumuler un grand nombre de liens, ce qui peut ralentir ou empêcher l'enregistrement d'un Canvas. Pour la localisation à grande échelle, les [messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) sont plus adaptés que les liens conditionnels dans un seul Content Block.

## Mettre à jour et copier des Content Blocks {#update-and-copy-content-blocks}

Si vous choisissez de mettre à jour un Content Block, il est mis à jour dans tous les messages où il est inséré via Liquid. Si le Content Block est importé à l'aide du menu déroulant **Content Blocks** sous **Lignes** dans l'éditeur par glisser-déposer, il n'est pas mis à jour dans tous les messages.

Si vous souhaitez mettre à jour un Content Block pour un seul message ou en créer une copie à utiliser dans d'autres messages, vous pouvez soit copier le HTML du message d'origine vers votre nouveau message, soit modifier le Content Block d'origine (il doit déjà avoir été utilisé dans un message) et l'enregistrer. Une invite s'affichera vous permettant de l'enregistrer en tant que nouveau Content Block.

Après avoir apporté des modifications à un Content Block, vous pouvez enregistrer et lancer le Content Block mis à jour en sélectionnant **Lancer le Content Block**. Vous pouvez également sélectionner **Plus** > **Dupliquer** pour créer un duplicata de votre Content Block.

![Un Content Block qui indique « Bienvenue dans notre newsletter ».]({% image_buster /assets/img/copy-content-block.png %})

## Utiliser des pieds de page d'e-mail dans les blocs de contenu {#email-footers}

Les blocs de contenu ne peuvent pas être utilisés dans un pied de page d'e-mail, mais vous pouvez créer un bloc de contenu qui inclut du contenu de pied de page pour l'utiliser dans vos e-mails. Pour ce faire :

1. Accédez à **Paramètres** > **Préférences des e-mails** > **Pied de page personnalisé** et créez le pied de page.
2. Ajoutez le pied de page à un bloc de contenu dans la **Bibliothèque de blocs de contenu**.
3. Ajoutez ce bloc de contenu à vos modèles d'e-mail ou messages.

## Informations importantes {#things-to-know}

- L'utilisation de Content Blocks HTML dans des e-mails par glisser-déposer ou de Content Blocks par glisser-déposer dans des e-mails HTML peut entraîner des problèmes de rendu inattendus. En effet, l'éditeur par glisser-déposer génère du HTML et du CSS qui affichent le contenu de manière dynamique, tandis que l'éditeur HTML est plus statique.
- Si vous insérez un Content Block par glisser-déposer à l'aide de Liquid, Braze n'inclut pas les styles provenant du `<head>` HTML du bloc. Les styles responsifs, tels que le CSS spécifique aux appareils mobiles, peuvent ne pas s'afficher comme prévu. Si le bloc repose sur du CSS responsif, ajoutez ce CSS au message ou au modèle qui inclut le Content Block.
- Les propriétés d'entrée Canvas ne sont prises en charge que dans les Canvas. Si vous faites référence à un Content Block avec des propriétés d'entrée Canvas dans une Campaign, elles ne seront pas renseignées.
- Si un message contenant plusieurs Content Blocks ne s'affiche pas comme prévu, par exemple lorsque des étiquettes Liquid ou du HTML apparaissent sous forme de texte visible au lieu d'être traités, une étiquette non fermée ou une autre erreur dans l'un des Content Blocks en est souvent la cause. Pour identifier la source :
    1. Retirez les Content Blocks du message concerné un par un.
    2. Vérifiez si le message s'affiche correctement après chaque retrait.
    3. Le dernier Content Block que vous retirez avant la disparition du problème est celui qui cause le problème.
- Les balises HTML `<code>` s'affichent en police à chasse fixe dans la plupart des clients de messagerie par défaut, indépendamment de tout style de police défini sur le Content Block. Évitez d'encadrer du texte avec des balises `<code>` sauf si vous souhaitez cet aspect à chasse fixe.
- Lorsque vous insérez un Content Block avec Liquid dans un modèle d'e-mail HTML personnalisé, les règles CSS du modèle parent peuvent remplacer les styles définis à l'intérieur du Content Block. Pour en savoir plus, consultez [Content Blocks dans les modèles HTML personnalisés]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline#content-blocks-in-custom-html-templates).

## Archiver des Content Blocks {#archive-content-blocks}

![Menu déroulant Paramètres développé affichant trois options : Archiver, Dupliquer et Copier vers l'espace de travail.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Une fois que vous avez terminé d'utiliser un Content Block, vous pouvez l'archiver depuis la page **Modèles**. Les Content Blocks archivés sont en lecture seule, vous devez donc désarchiver le Content Block avant de le modifier. Les Content Blocks ne peuvent pas être archivés s'ils sont utilisés dans des messages.

### Bonnes pratiques {#best-practices}

- Lorsque votre bloc n'est utilisé que dans quelques e-mails, nous vous recommandons d'archiver le bloc obsolète et de mettre à jour vos messages en direct avec un bloc plus récent qui n'a pas été archivé.
- Lorsque votre bloc contient uniquement une faute de frappe ou nécessite une modification mineure, nous ne recommandons pas d'archiver le bloc. Mettez plutôt le bloc à jour et lancez vos envois !
- Lorsque votre bloc est utilisé dans plus de messages que vous ne pouvez raisonnablement gérer avec la première suggestion de cette liste, nous vous recommandons de supprimer tout le contenu du bloc. Cela empêche l'inclusion d'informations obsolètes dans les messages.
- Si vous archivez accidentellement un Content Block, vous pouvez le désarchiver.

![Panneau des Content Blocks enregistrés où le menu déroulant des paramètres de « Test_32 » est développé pour afficher trois options : Désarchiver, Dupliquer et Copier vers l'espace de travail]({% image_buster /assets/img/unarchive-content-block.png %})