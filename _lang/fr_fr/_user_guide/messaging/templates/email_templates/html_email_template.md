---
nav_title: Télécharger un modèle d'e-mail HTML
article_title: Télécharger un modèle d'e-mail HTML
page_order: 2
description: "Cet article de référence explique comment créer, gérer et résoudre les problèmes d'un modèle d'e-mail HTML à l'aide du tableau de bord de Braze."
tool:
  - Templates
channel:
  - email

---

# Télécharger un modèle d'e-mail HTML {#upload-an-html-email-template}

> Le tableau de bord de Braze vous permet de télécharger vos propres modèles d'e-mail HTML et de les enregistrer pour une utilisation ultérieure dans des campagnes. Vous pouvez également [créer un modèle d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) à l'aide de notre éditeur.

## Conditions requises {#upload-requirements}

Tout d'abord, vous devez créer votre modèle d'e-mail HTML. Il doit s'agir d'un fichier ZIP contenant les éléments suivants :

* Un seul fichier HTML — le corps de votre e-mail
* Un dossier d'images référencées dans le fichier HTML
* Moins de 50 fichiers image
* Une taille inférieure à 5&nbsp;Mo

## Télécharger votre modèle {#uploading-your-template}

### Étape 1 : Accéder à l'éditeur de modèles d'e-mail {#step-1-go-to-the-email-template-editor}

Accédez à **Content** > **Email**. Sélectionnez **Create email template**.

### Étape 2 : Ajouter les détails du modèle {#step-2-add-template-details}

Indiquez un nom de modèle. Vous pouvez éventuellement ajouter une description, des équipes et des tags.

### Étape 3 : Télécharger votre modèle {#step-3-upload-your-template}

Dans la section **Template content**, sélectionnez **Upload file**. Sélectionnez votre modèle depuis votre ordinateur. Consultez la section [Conditions requises](#upload-requirements) pour vous assurer que votre modèle respecte les exigences de téléchargement.

### Étape 4 : Finaliser et enregistrer votre modèle {#step-4-finish-and-save-your-template}

N'oubliez pas d'enregistrer votre modèle en sélectionnant **Save template**. Vous êtes maintenant prêt à utiliser ce modèle dans n'importe quelle campagne ou Canvas de votre choix.

{% alert note %}
Si vous apportez des modifications à un modèle existant, ces changements ne seront pas reflétés dans les campagnes créées à l'aide de versions précédentes de ce modèle.
{% endalert %}

## Utiliser vos modèles dans des campagnes API {#api_for_upload_email_templates}

Pour utiliser votre e-mail dans une campagne API, vous avez besoin de l'`email_template_id`, qui se trouve en bas de tout modèle d'e-mail créé dans Braze.

![Section de l'identifiant API d'un modèle d'e-mail HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Gérer les modèles d'e-mail {#managing-email-templates}

Vous pouvez [dupliquer]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) et [archiver]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) des modèles d'e-mail ! Pour en savoir plus sur la création et la gestion des modèles et du contenu créatif, consultez la page [Modèles]({{site.baseurl}}/user_guide/messaging/templates).

## Résolution des problèmes {#troubleshooting}

Plusieurs messages d'erreur peuvent s'afficher lors du téléchargement d'un fichier de modèle HTML. Si vous recevez une erreur, consultez le tableau suivant pour connaître les problèmes courants et les corrections recommandées :

| Erreur | Correction |
|------|---|
| `.zip over 5&nbsp;MB` | Réduisez la taille de votre fichier et réessayez le téléchargement. |
| `.zip corrupt` | Inspectez votre fichier et réessayez le téléchargement. |
| `Missing HTML` | Ajoutez le fichier HTML à votre fichier ZIP et réessayez le téléchargement. |
| `Multiple HTML` | Supprimez l'un des fichiers HTML et réessayez le téléchargement. |
| `Images over 5&nbsp;MB` | Réduisez le nombre d'images et réessayez le téléchargement. |
| `Extra Images` | Il se peut que des images supplémentaires dans votre fichier ne soient pas référencées dans votre fichier HTML. Cela ne provoque pas d'erreur bloquante, mais les images supplémentaires sont ignorées. Si ces images étaient censées être référencées dans le fichier HTML, vérifiez le contenu, corrigez les erreurs éventuelles et réessayez le téléchargement. |
| `Missing Images` | Si des images sont référencées dans votre fichier HTML mais ne sont pas incluses dans le dossier d'images du fichier ZIP, vous recevez une erreur de fichier. Inspectez votre fichier et corrigez les erreurs éventuelles (comme les fautes de frappe), ou ajoutez les images manquantes à votre fichier ZIP et réessayez le téléchargement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

Notez que lors du téléchargement des fichiers pour des campagnes HTML, des étapes Canvas avec des messages e-mail ou des modèles sur une machine Windows, le caractère `|` (barre verticale) n'est pas pris en charge. Vous devrez peut-être utiliser une autre application pour extraire le contenu téléchargé du fichier ZIP.

## Questions fréquemment posées {#frequently-asked-questions}

Pour obtenir des réponses aux questions fréquemment posées sur les modèles d'e-mail, consultez notre page [FAQ sur les modèles d'e-mail et de liens]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).