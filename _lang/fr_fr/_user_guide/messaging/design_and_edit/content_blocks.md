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

## Créer un bloc de contenu {#create-a-content-block}

Il existe deux types de blocs de contenu : glisser-déposer et HTML. Chaque type correspond à son éditeur.

{% tabs %}
{% tab Glisser-déposer %}

{% multi_lang_include messaging/create_content_block.md location="dnd" %}

{% alert important %}
Chaque bloc de contenu glisser-déposer est limité à une seule ligne. Cependant, vous pouvez utiliser les blocs de l'éditeur glisser-déposer pour créer et personnaliser le bloc de contenu selon vos besoins en matière d'e-mails.
{% endalert %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include messaging/create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Spécifications des blocs de contenu {#content-block-specifications}

| Attribut du bloc de contenu | Spécifications |
|---|---|
| Nom | Champ requis avec un maximum de 100 caractères. Les noms de blocs de contenu ne peuvent contenir que des lettres (A-Z), des chiffres (0-9), des tirets (`-`) et des underscores (`_`). Les espaces et autres caractères spéciaux ne sont pas autorisés et sont automatiquement convertis (par exemple, les espaces sont remplacés par des underscores). Les noms ne peuvent pas être modifiés après l'enregistrement du bloc de contenu, et vous ne pouvez pas réutiliser le nom d'un bloc de contenu précédent, même s'il a été archivé. |
| Description | (facultatif) Maximum de 250 caractères. Décrivez le bloc de contenu afin que les autres utilisateurs de Braze sachent à quoi il sert et où il est utilisé. |
| Taille du contenu | Maximum de 50 Ko. |
| Emplacement | Les blocs de contenu ne peuvent pas être utilisés dans un pied de page d'e-mail, mais vous pouvez [créer un bloc de contenu qui inclut un pied de page](#email-footers) pour l'utiliser dans vos e-mails. |
| Création | Éditeur HTML ou éditeur glisser-déposer. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications des blocs de contenu" }

{% alert tip %}
Lors de la création de blocs de contenu, il peut être utile de visualiser le HTML et le Liquid en ajoutant des sauts de ligne. Si ces sauts de ligne sont conservés lors de l'envoi, vous risquez d'avoir des espaces superflus qui peuvent affecter le rendu du bloc. Pour éviter cela, utilisez la balise **Capture** sur votre bloc avec le filtre **&#124; strip**.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Utiliser les blocs de contenu {#use-content-blocks}

Après avoir créé votre bloc de contenu, vous pouvez l'insérer dans vos messages à l'aide de l'éditeur ou de Liquid.

### Utiliser l'éditeur glisser-déposer {#using-the-editor}

Pour ajouter un bloc de contenu dans l'éditeur glisser-déposer :

1. Accédez à l'onglet **Rows** dans l'éditeur et sélectionnez **Content Blocks**.
2. Glissez-déposez votre bloc de contenu dans l'éditeur d'e-mail.
3. (Facultatif) Ajustez la largeur de votre bloc de contenu en sélectionnant le bouton dans le menu de navigation. La largeur par défaut est de 100 % lorsqu'elle n'est pas spécifiée dans les paramètres de style global de votre e-mail ; sinon, les paramètres globaux seront respectés. <br><br>![Une flèche à double sens avec une option pour modifier la largeur.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

{% alert note %}
Les blocs de contenu ajoutés par glisser-déposer ne sont **pas liés** au bloc de contenu d'origine. Pour voir les modifications apportées à l'original, glissez-le à nouveau dans l'éditeur d'e-mail.
{% endalert %}

Un désalignement dans l'éditeur glisser-déposer peut se produire lorsque plusieurs blocs de contenu sont ajoutés à un seul bloc de ligne. Essayez d'utiliser des blocs de ligne séparés pour maintenir l'alignement de votre contenu au niveau de la ligne.

### Utiliser Liquid {#using-liquid}

Pour insérer un bloc de contenu à l'aide de Liquid :

1. Copiez l'**étiquette Liquid du bloc de contenu** depuis la section **Content Block Details**.
2. Insérez l'étiquette Liquid du bloc de contenu dans le message. Vous pouvez également commencer à taper le Liquid et laisser l'étiquette se compléter automatiquement.

Dans l'éditeur glisser-déposer, vous pouvez également ajouter un bloc de contenu via le panneau **Personalization** :

1. Accédez à votre Campaign e-mail et sélectionnez **Edit Email Body**.
2. Cliquez sur <i class="fas fa-plus"></i> **Personalization**.
3. Sélectionnez **Content Blocks** dans le menu déroulant **Personalization Type**.
4. Sélectionnez le nom de votre bloc de contenu dans le champ **Attribute**.
5. Copiez et collez l'extrait de code Liquid dans un bloc éditeur de texte. <br>![L'onglet Add Personalization avec ses options.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

{% alert important %}
Les blocs de contenu insérés via Liquid **sont liés** au bloc de contenu d'origine et refléteront toute modification apportée au modèle.
{% endalert %}

### Bon à savoir {#things-to-know}

- L'utilisation de blocs de contenu HTML dans des e-mails glisser-déposer **ou** de blocs de contenu glisser-déposer dans des e-mails HTML peut entraîner des problèmes de rendu inattendus. En effet, l'éditeur glisser-déposer génère du HTML et du CSS qui rendent le contenu de manière dynamique, tandis que l'éditeur HTML est plus statique.
- Si vous insérez un bloc de contenu glisser-déposer à l'aide de Liquid, Braze n'inclut pas les styles provenant du `<head>` HTML du bloc. Les styles responsifs, tels que le CSS spécifique aux appareils mobiles, peuvent ne pas s'afficher comme prévu. Si le bloc repose sur du CSS responsif, ajoutez ce CSS au message ou au modèle qui inclut le bloc de contenu.
- Les propriétés d'événement Canvas ne sont prises en charge que dans un Canvas. Si vous référencez un bloc de contenu avec des propriétés d'entrée Canvas dans une Campaign, elles ne seront pas renseignées.

## Prévisualiser les blocs de contenu {#preview-content-blocks}

Après avoir ajouté un bloc de contenu dans une Campaign ou un Canvas actif, vous pouvez le prévisualiser depuis la bibliothèque de blocs de contenu en survolant le bloc de contenu et en sélectionnant l'icône <i class="fa fa-eye preview-icon"></i> **Preview**.

Cette prévisualisation inclut des informations sur le bloc de contenu telles que son créateur, les étiquettes, la date de création, la date de dernière modification, la description, le type d'éditeur, le nombre d'inclusions avec les détails (une liste cliquable des messages ou blocs de contenu qui utilisent ce bloc de contenu), ainsi qu'un aperçu réel du bloc de contenu.

## Imbriquer des blocs de contenu {#nest-content-blocks}

Les blocs de contenu peuvent être imbriqués, mais une seule fois. Vous pouvez imbriquer le bloc de contenu A dans le bloc de contenu B, mais vous ne pourrez pas ensuite imbriquer le bloc de contenu B dans le bloc de contenu C.

{% alert warning %}
Rien ne vous empêchera d'imbriquer un troisième niveau de bloc de contenu, mais le contenu ne se développera pas au-delà du deuxième niveau d'imbrication. Le contenu et l'extrait de code Liquid sont supprimés du message.
{% endalert %}

## Mettre à jour et copier des blocs de contenu {#update-and-copy-content-blocks}

Si vous choisissez de mettre à jour un bloc de contenu, il sera mis à jour dans tous les messages où il est inséré via Liquid. Si le bloc de contenu est importé à l'aide du menu déroulant **Content Blocks** sous **Rows** dans l'éditeur glisser-déposer, il ne sera pas mis à jour dans tous les messages.

Si vous souhaitez mettre à jour un bloc de contenu pour un seul message ou en faire une copie pour l'utiliser dans d'autres messages, vous pouvez soit copier le HTML du message d'origine vers votre nouveau message, soit modifier le bloc de contenu d'origine (il doit avoir déjà été utilisé dans un message) et l'enregistrer. Une invite vous permettra alors de l'enregistrer en tant que nouveau bloc de contenu.

Après avoir apporté des modifications à un bloc de contenu, vous pouvez enregistrer et lancer le bloc de contenu mis à jour en sélectionnant **Launch Content Block**. Vous pouvez également sélectionner **More** > **Duplicate** pour créer un duplicata de votre bloc de contenu.

![Un bloc de contenu qui indique « Bienvenue dans notre newsletter ».]({% image_buster /assets/img/copy-content-block.png %})

## Utiliser des pieds de page d'e-mail dans les blocs de contenu {#email-footers}

Les blocs de contenu ne peuvent pas être utilisés dans un pied de page d'e-mail, mais vous pouvez créer un bloc de contenu qui inclut du contenu de pied de page pour l'utiliser dans vos e-mails. Pour ce faire :

1. Accédez à **Paramètres** > **Préférences des e-mails** > **Pied de page personnalisé** et créez le pied de page.
2. Ajoutez le pied de page à un bloc de contenu dans la **Bibliothèque de blocs de contenu**.
3. Ajoutez ce bloc de contenu à vos modèles d'e-mail ou messages.

## Archiver des blocs de contenu {#archive-content-blocks}

![Menu déroulant des paramètres développé affichant trois options : Archiver, Dupliquer et Copier vers l'espace de travail.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Une fois que vous avez terminé d'utiliser un bloc de contenu, vous pouvez l'archiver depuis la page **Modèles**. Les blocs de contenu archivés sont en lecture seule : vous devez donc désarchiver le bloc de contenu avant de le modifier. Les blocs de contenu ne peuvent pas être archivés s'ils sont utilisés dans des messages.

### Bonnes pratiques {#best-practices}

- Lorsque votre bloc n'est utilisé que dans quelques e-mails, nous vous recommandons d'archiver le bloc obsolète et de mettre à jour vos messages en production avec un bloc plus récent qui n'a pas été archivé.
- Lorsque votre bloc ne contient qu'une faute de frappe ou nécessite une modification mineure, nous ne recommandons pas d'archiver le bloc. Mettez plutôt le bloc à jour et continuez vos envois !
- Lorsque votre bloc est utilisé dans plus de messages que vous ne pouvez raisonnablement gérer avec la première suggestion de cette liste, nous vous recommandons de supprimer tout le contenu du bloc. Cela empêche l'inclusion d'informations obsolètes dans les messages.
- Si vous archivez accidentellement un bloc de contenu, vous pouvez le désarchiver.

![Panneau des blocs de contenu enregistrés où le menu déroulant des paramètres de « Test_32 » est développé pour afficher trois options : Désarchiver, Dupliquer et Copier vers l'espace de travail.]({% image_buster /assets/img/unarchive-content-block.png %})