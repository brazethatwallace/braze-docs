---
nav_title: Générateur de modèles WhatsApp
article_title: Générateur de modèles WhatsApp
description: "Découvrez comment créer, configurer et soumettre des modèles de messages WhatsApp directement dans Braze à l'aide du générateur de modèles WhatsApp."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# Générateur de modèles WhatsApp {#whatsapp-template-builder}

> Le générateur de modèles WhatsApp vous permet de créer et de soumettre des modèles de messages WhatsApp directement dans Braze, sans avoir à basculer entre Braze et le Meta Business Manager. Une fois votre modèle approuvé par Meta, utilisez-le dans autant de Campaigns et de Canvas que vous le souhaitez.

## Conditions préalables {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Créer un modèle {#create-a-template}

### Étape 1 : Accéder aux modèles WhatsApp {#step-1-go-to-whatsapp-templates}

Accédez à **Contenu** > **Modèles** > **WhatsApp**, puis sélectionnez **Créer un nouveau modèle**.

![Page des modèles WhatsApp avec un bouton pour créer un nouveau modèle.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### Étape 2 : Configurer les paramètres du modèle {#step-2-configure-template-settings}

Remplissez les champs suivants :

| Champ | Description |
| ----- | ----- |
| **Compte** | Le compte WhatsApp Business (WABA) auquel vous souhaitez soumettre le modèle. Tous les groupes d'abonnement et numéros de téléphone d'un WABA partagent l'accès aux modèles. |
| **Langue** | La langue de ce modèle. WhatsApp exige un modèle distinct pour chaque langue. |
| **Nom du modèle** | Un nom unique pour votre modèle. Les noms de modèles ne peuvent contenir que des lettres minuscules, des chiffres et des underscores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Configurer les paramètres du modèle" }

### Étape 3 : Choisir une mise en page {#step-3-choose-a-layout}

Sous **Mise en page**, sélectionnez le type de modèle :

- **Par défaut :** Un message WhatsApp standard. C'est la mise en page couverte dans cet article.
- **Carrousel :** Un message avec des cartes défilables horizontalement. Pour plus d'informations, consultez [Modèles carrousel]({{site.baseurl}}/whatsapp_carousel_templates).

### Étape 4 : Construire votre modèle {#step-4-build-your-template}

#### En-tête (facultatif) {#header-optional}

Ajoutez un en-tête à afficher avant le corps du message. Vous pouvez choisir :

- **Texte :** Un court en-tête textuel.
- **Média :** Une image, une vidéo ou un document (URL uniquement). Braze stocke la référence du média et soumet un échantillon à Meta pour approbation.
- **Aucun :** Pas d'en-tête

#### Corps {#body}

Saisissez le contenu principal de votre message et personnalisez le corps selon vos besoins en utilisant Liquid ou des variables génériques :

{% raw %}
- Utilisez des étiquettes Liquid (par exemple, `{{${first_name}}}`). Braze enregistre votre Liquid et le met à disposition lorsque vous utilisez le modèle dans un compositeur de Campaign ou de Canvas.
- Utilisez des variables génériques, telles que des marques substitutives numérotées (par exemple, `{{1}}`), si vous préférez ajouter la personnalisation ultérieurement lors de la construction de votre message.
{% endraw %}

Vous pouvez ajouter de la personnalisation partout où le bouton **+** plus apparaît. Tous les champs ne prennent pas en charge la personnalisation.

#### Limites de caractères Liquid {#liquid-character-limits}

Meta impose des limites de caractères sur la structure du modèle que vous soumettez pour approbation (par exemple, 1 024 caractères pour le corps et 60 caractères pour un en-tête textuel). Dans le générateur de modèles, ces limites s'appliquent au modèle envoyé à Meta, et non au message final rendu au moment de l'envoi.

- **Variables {% raw %}`{{ }}`{% endraw %} :** Braze convertit les variables Liquid en marques substitutives numérotées ({% raw %}`{{1}}`, `{{2}}`{% endraw %}) avant de vérifier la longueur. Une expression longue comme {% raw %}`{{${first_name}}}`{% endraw %} compte comme une courte marque substitutive, et non comme la syntaxe Liquid complète.
- **Balises {% raw %}`{% %}`{% endraw %} :** Les balises de logique Liquid comptent comme du texte littéral à leur longueur complète et apparaissent comme du contenu non modifiable dans les messages de modèle.

Pour une personnalisation complexe, utilisez une [étape de contexte]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) pour calculer les valeurs, puis référencez des variables plus courtes dans le modèle. Pour les contraintes liées aux Message Extras et à la logique conditionnelle, consultez [Liquid dans le générateur de modèles WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/template_builder_liquid).

#### Pied de page (facultatif) {#footer-optional}

Ajoutez un court pied de page à afficher après le corps du message.

#### Boutons (facultatif) {#buttons-optional}

Ajoutez jusqu'à 10 boutons à votre modèle. Les types de boutons ont des catégories et des spécifications différentes.

| Type de bouton | Catégorie | Spécifications |
| --- | --- | --- |
| Réponse rapide | Boutons de réponse rapide |{::nomarkdown}<ul><li><b>Nombre maximum :</b> 10</li><li><b>Texte du bouton :</b> Jusqu'à 25 caractères</li></ul> {:/}|
| Numéro de téléphone | Boutons d'appel à l'action | {::nomarkdown}<ul><li><b>Nombre maximum :</b> 1</li><li><b>Texte du bouton :</b> Jusqu'à 25 caractères</li><li><b>Numéro de téléphone :</b> Numéro de téléphone valide avec indicatif pays, sans + (par exemple « 14155552671 »)</li></ul> {:/}|
| Visiter le site web | Boutons d'appel à l'action | {::nomarkdown}<ul><li><b>Nombre maximum :</b> 2</li><li><b>Texte du bouton :</b> Jusqu'à 25 caractères</li><li><b>URL du site web :</b> Jusqu'à 2 000 caractères</li></ul> {:/}|
| Copier le code promotionnel | Boutons d'appel à l'action | {::nomarkdown}<ul><li><b>Nombre maximum :</b> 1</li><li><b>Texte du bouton :</b> « Copy offer code » (non modifiable)</li><li><b>Code promotionnel :</b> Jusqu'à 15 caractères</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Boutons (facultatif)" }

![Compositeur de modèles WhatsApp avec des boutons de réponse rapide et d'appel à l'action.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Étape 5 : Prévisualiser votre modèle {#step-5-preview-your-template}

Avant de soumettre, prévisualisez l'apparence de votre message pour les destinataires :

- **Prévisualiser en tant qu'utilisateur :** Affichez un aperçu générique du message.
- **Prévisualiser en tant qu'utilisateur spécifique :** Sélectionnez un profil utilisateur pour prévisualiser le rendu du modèle avec les données de cet utilisateur.

### Étape 6 : Soumettre pour examen {#step-6-submit-for-review}

Sélectionnez **Soumettre** pour envoyer votre modèle à Meta pour examen, ce qui prend généralement quelques minutes mais peut aller jusqu'à 24 heures. Le modèle apparaît sur votre page **Modèles WhatsApp** une fois soumis, et le statut se met à jour lorsque vous actualisez la page **Modèles WhatsApp**.

## Catégories de modèles prises en charge {#supported-template-categories}

Seuls les modèles Marketing sont actuellement pris en charge dans le générateur de modèles WhatsApp.

## Utiliser un modèle approuvé dans une campagne {#use-an-approved-template-in-a-campaign}

Une fois que Meta a approuvé votre modèle, vous pouvez l'utiliser dans une Campaign WhatsApp ou un Canvas.

1. Accédez à **Campaigns** et sélectionnez **Create Campaign** > **WhatsApp**.
2. Dans le composeur de messages, sélectionnez votre modèle approuvé.
3. Braze renseigne automatiquement le contenu du modèle, y compris les médias et le Liquid que vous avez saisis lors de la création du modèle, afin que vous n'ayez pas à les saisir à nouveau.
4. Mettez à jour le contenu des variables ou la personnalisation selon vos besoins. Les champs verrouillés par Meta (affichés en gris) ne peuvent pas être modifiés. Pour modifier du contenu verrouillé, vous devez modifier et soumettre à nouveau le modèle pour approbation.
5. Utilisez l'onglet **Test** pour prévisualiser le message, mettre à jour les variables du corps et confirmer que le message s'affiche comme prévu avant le lancement.

Pour plus d'informations sur la création de Campaigns WhatsApp, consultez [Créer un message WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

## Questions fréquemment posées {#frequently-asked-questions}

### Combien de temps dure l'examen des modèles par Meta ? {#how-long-does-meta-template-review-take}

Les examens sont généralement terminés en cinq minutes, mais peuvent prendre jusqu'à 24 heures.

### Puis-je modifier un modèle après son approbation ? {#can-i-edit-a-template-after-its-been-approved}

Vous pouvez mettre à jour le contenu variable et la personnalisation lors de la création d'une Campaign ou d'un Canvas. Les modifications du contenu verrouillé (corps du texte, disposition des boutons ou autres champs contrôlés par Meta) nécessitent la création d'un nouveau modèle dans le générateur de modèles ou la modification du modèle dans le WhatsApp Manager de Meta, puis l'attente d'une nouvelle approbation par Meta. Si vous utilisez le [suivi des clics]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking), consultez cet article avant de modifier les modèles créés par Braze dans le WhatsApp Manager de Meta.

### Qu'advient-il des modèles que j'ai soumis avant la disponibilité du générateur de modèles ? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Les modèles créés dans Meta Business Manager sont toujours disponibles dans Braze. Le générateur de modèles est un moyen supplémentaire de créer et de gérer des modèles sans quitter le tableau de bord de Braze.

### Pourquoi ne puis-je pas ajouter de la personnalisation à tous les champs ? {#why-cant-i-add-personalization-to-every-field}

Meta restreint les parties d'un modèle qui peuvent être personnalisées. Le bouton **+** (plus) n'apparaît que dans les champs qui prennent en charge le contenu variable.