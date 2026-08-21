---
nav_title: Suivre les utilisateurs
article_title: Suivre les utilisateurs via un formulaire
description: "Découvrez comment identifier les utilisateurs qui soumettent un formulaire via votre page d'accueil en ajoutant une étiquette Liquid à vos messages."
page_order: 2
---

# Suivre les utilisateurs via un formulaire {#track-users-through-a-form}

> Découvrez comment suivre les utilisateurs qui soumettent un formulaire via votre page d'accueil en ajoutant une étiquette Liquid de page d'accueil à vos messages. Cette étiquette Liquid est prise en charge sur tous les canaux de communication Braze, y compris les e-mails, les SMS, les messages in-app, et bien plus encore. Pour en savoir plus sur le suivi des données, consultez [À propos des données de suivi des pages d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/about_tracking_data).

## Prérequis {#prerequisites}

Avant de commencer, vous devrez créer une [page de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) et une [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign).

## Fonctionnement {#how-it-works}

Vous pouvez ajouter une étiquette Liquid {% raw %}`{% landing_page_url %}`{% endraw %} à n'importe lequel de vos messages mono ou multicanaux dans Braze. Lorsqu'un utilisateur visite cette page de destination et soumet le formulaire, Braze associe automatiquement ces données à son profil existant, au lieu de créer un nouveau profil pour cet utilisateur. Dans l'exemple suivant, l'étiquette Liquid de page de destination est utilisée pour diriger les clients vers une enquête :

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
Vous pouvez également utiliser les pages de destination pour la génération de prospects en intégrant l'URL de la page dans vos canaux externes. Après avoir créé une page de destination, accédez à **Landing Page Details** pour obtenir l'URL unique de votre page de destination.
{% endalert %}

## Utiliser les étiquettes Liquid de page de destination {#using-landing-page-liquid-tags}

### Étape 1 : Vérifier l'URL de la page {#page-url}

Braze utilisera l'URL de votre page de destination pour générer son étiquette Liquid unique. Si vous souhaitez modifier l'URL actuelle de la page, accédez à **Messaging** > **Pages de destination**, puis ouvrez votre page de destination. Sous **URL de la page**, vous pouvez saisir une nouvelle URL de page.

{% alert warning %}
Si vous modifiez l'URL de la page après l'envoi de votre message, tout utilisateur qui tente de visiter votre page de destination en utilisant l'ancienne URL sera redirigé vers une page `404`.
{% endalert %}

![Un exemple d'URL de page pour une page de destination dans Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Étape 2 : Générer l'étiquette Liquid {#step-2-generate-the-liquid-tag}

Accédez à **Messaging** > **Campaigns**, puis choisissez une Campaign. Dans votre éditeur de message, sélectionnez **Personnalisation**.

![Le bouton « Ajouter une personnalisation » dans l'éditeur par glisser-déposer.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze générera automatiquement une étiquette Liquid en utilisant l'[URL de votre page de destination](#page-url). Consultez le tableau suivant pour générer votre étiquette :

| **Type de personnalisation** | Choisissez **Landing Page**. |
| **Page de destination** | Choisissez la page de destination [que vous avez précédemment créée](#prerequisites). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Générer l'étiquette Liquid" }

Pour ajouter l'étiquette Liquid à votre message, vous pouvez soit sélectionner **Insérer**, soit copier l'extrait de code dans votre presse-papiers et l'ajouter manuellement.

![Une étiquette Liquid générée automatiquement pour la page de destination sélectionnée.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Votre extrait de code sera similaire à ce qui suit :

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### Étape 3 : Finaliser et envoyer votre message {#step-3-finalize-and-send-your-message}

Intégrez l'extrait de code Liquid dans votre message, puis finalisez le reste de votre message. Par exemple :

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

Lorsque vous êtes prêt, vous pouvez envoyer le message pour commencer à suivre les utilisateurs via votre page de destination.

### Utiliser les URL de page de destination dans les Content Cards {#use-landing-page-urls-in-content-cards}

Les Content Cards ont une [limite de payload de 2 Ko]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#size-limitations-for-content-cards) qui s'applique à l'ensemble de la carte après le rendu Liquid. Lorsque vous incluez une étiquette Liquid {% raw %}`{% landing_page_url %}`{% endraw %}, Braze comptabilise le jeton de suivi de la page de destination comme un forfait fixe de 32 octets dans cette limite, et non la longueur totale du jeton. Le reste de l'URL ainsi que le titre, le corps et les autres champs de la carte sont toujours comptabilisés normalement dans cette limite.