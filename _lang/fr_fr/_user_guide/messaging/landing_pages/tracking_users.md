---
nav_title: Suivre les utilisateurs
article_title: Suivre les utilisateurs via un formulaire
description: "Découvrez comment identifier les utilisateurs qui soumettent un formulaire via votre page d'accueil en ajoutant une étiquette Liquid à vos messages."
page_order: 2
---

# Suivre les utilisateurs via un formulaire {#track-users-through-a-form}

> Découvrez comment suivre les utilisateurs qui soumettent un formulaire via votre page d'accueil en ajoutant une étiquette Liquid de page d'accueil à vos messages. Cette étiquette Liquid est prise en charge sur tous les canaux de communication Braze, y compris les e-mails, les SMS, les messages in-app, et bien plus encore. Pour en savoir plus sur le suivi des données, consultez [À propos des données de suivi des pages d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/about_tracking_data/).

## Conditions préalables {#prerequisites}

Avant de commencer, vous devrez créer une [page d'accueil]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/) et une [campagne]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/).

## Comment ça fonctionne {#how-it-works}

Vous pouvez ajouter une étiquette Liquid {% raw %}`{% landing_page_url %}`{% endraw %} à n'importe lequel de vos messages mono ou multicanaux dans Braze. Lorsqu'un utilisateur visite cette page d'accueil et soumet le formulaire, Braze associera automatiquement ces données à son profil existant, plutôt que de créer un nouveau profil pour cet utilisateur. Dans l'exemple suivant, l'étiquette Liquid de page d'accueil est utilisée pour diriger les clients vers une enquête :

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
Vous pouvez également utiliser les pages d'accueil pour la génération de prospects en intégrant l'URL de la page dans vos canaux externes. Après avoir créé une page d'accueil, accédez à **Landing Page Details** pour obtenir l'URL unique de votre page d'accueil.
{% endalert %}

## Utiliser les étiquettes Liquid de page d'accueil {#using-landing-page-liquid-tags}

### Étape 1 : Vérifier l'URL de la page {#page-url}

Braze utilisera l'URL de votre page d'accueil pour générer son étiquette Liquid unique. Si vous souhaitez modifier l'URL actuelle de la page, accédez à **Messaging** > **Landing Pages**, puis ouvrez votre page d'accueil. Sous **page URL**, vous pouvez saisir une nouvelle URL de page.

{% alert warning %}
Si vous modifiez l'URL de la page après l'envoi de votre message, tout utilisateur qui tente de visiter votre page d'accueil en utilisant l'ancienne URL sera redirigé vers une page `404`.
{% endalert %}

![Un exemple d'URL de page pour une page d'accueil dans Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Étape 2 : Générer l'étiquette Liquid {#step-2-generate-the-liquid-tag}

Accédez à **Messaging** > **Campaigns**, puis choisissez une Campaign. Dans votre éditeur de message, sélectionnez **Personalization**.

![Le bouton « Add personalization » dans l'éditeur par glisser-déposer.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze générera automatiquement une étiquette Liquid en utilisant l'[URL de votre page d'accueil](#page-url). Consultez le tableau suivant pour générer votre étiquette :

| **Type de personnalisation** | Choisissez **Landing Page**. |
| **Page d'accueil** | Choisissez la page d'accueil [que vous avez précédemment créée](#prerequisites). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour ajouter l'étiquette Liquid à votre message, vous pouvez soit sélectionner **Insert**, soit copier l'extrait de code dans votre presse-papiers et l'ajouter manuellement.

![Une étiquette Liquid générée automatiquement pour la page d'accueil sélectionnée.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

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

Lorsque vous êtes prêt, vous pouvez envoyer le message pour commencer à suivre les utilisateurs via votre page d'accueil.