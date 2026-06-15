---
nav_title: Modèles de webhook
article_title: Modèles de webhook
page_order: 5
tool:
  - Templates
channel:
  - webhooks
description: "Découvrez comment créer et personnaliser des modèles de webhook pour une utilisation ultérieure au sein de la plateforme Braze."

---

# Créer un modèle de webhook {#create-a-webhook-template}

> Lorsque vous créez et personnalisez vos webhooks, vous pouvez concevoir et exploiter des modèles de webhook pour une utilisation ultérieure au sein de la plateforme Braze. Vous pouvez ainsi créer de manière cohérente une variété de webhooks pour vos différentes campagnes.

## Étape 1 : Accéder à l'éditeur de modèles de webhook {#step-1-go-to-the-webhook-template-editor}

Dans le tableau de bord de Braze, accédez à **Contenu** > **Webhook**.

![La page « Modèles de webhook » avec les modèles de webhook préconçus et enregistrés.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## Étape 2 : Choisir votre modèle {#step-2-choose-your-template}

À partir de là, vous pouvez choisir de créer un nouveau modèle, d'utiliser l'un des modèles de webhook préconçus ou de modifier un modèle existant.

Par exemple, si vous utilisez [LINE]({{site.baseurl}}/user_guide/channels/line/) comme canal de communication, vous pouvez configurer plusieurs webhooks à l'aide des modèles préconçus pour **LINE Carousel** ou **LINE Image**.

## Étape 3 : Renseigner les détails du modèle {#step-3-fill-out-template-details}

1. Donnez un nom unique à votre modèle de webhook.
2. (Facultatif) Ajoutez une description du modèle pour expliquer comment ce modèle est destiné à être utilisé.
3. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) selon vos besoins pour faciliter la recherche et le filtrage de votre modèle.

## Étape 4 : Créer votre modèle {#step-4-build-your-template}

1. Saisissez l'URL du webhook.
2. Sélectionnez la méthode HTTP.
3. Ajoutez un corps de requête. Il peut s'agir de **paires clé/valeur JSON** ou de **texte brut**.
4. (Facultatif) Ajoutez un en-tête de requête. Cela peut être requis par la destination de votre webhook.

![L'onglet « Rédiger » lors de la création d'un modèle de webhook. Les champs disponibles sont l'URL du webhook, la méthode HTTP, le corps de la requête et les en-têtes de requête. Vous pouvez également ajouter des langues.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## Étape 5 : Tester votre modèle {#step-5-test-your-template}

Pour voir à quoi ressemble votre webhook avant de l'envoyer à vos utilisateurs, vous pouvez envoyer un webhook de test à l'aide de l'onglet **Test**. Ici, vous pouvez choisir de prévisualiser le message en tant qu'utilisateur aléatoire, utilisateur existant ou utilisateur personnalisé.

## Étape 6 : Enregistrer votre modèle {#step-6-save-your-template}

Assurez-vous d'enregistrer votre modèle en sélectionnant **Enregistrer le modèle**. Vous êtes maintenant prêt à utiliser ce modèle dans la campagne de votre choix.

{% alert note %}
Les modifications apportées à un modèle existant ne sont pas répercutées dans les campagnes créées à l'aide de versions précédentes de ce modèle.
{% endalert %}

## Gérer vos modèles {#managing-your-templates}

Vous pouvez [dupliquer et archiver]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) des modèles de webhook pour mieux organiser et gérer votre liste de modèles.