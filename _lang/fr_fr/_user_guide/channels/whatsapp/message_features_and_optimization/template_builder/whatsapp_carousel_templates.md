---
nav_title: Modèles carrousel
article_title: Modèles carrousel WhatsApp
description: "Cet article de référence couvre les modèles carrousel WhatsApp."
tool:
  - WhatsApp
alias: /whatsapp_carousel_templates/
toc_headers: h2
---

# Modèles carrousel WhatsApp {#whatsapp-carousel-templates}

> Les modèles carrousel WhatsApp vous permettent de créer des messages interactifs à plusieurs cartes que les utilisateurs peuvent faire défiler. Chaque carrousel peut contenir jusqu'à 10 cartes avec des images ou des vidéos, ainsi que des boutons personnalisables pour l'engagement. Cette fonctionnalité est idéale pour présenter vos produits et services, ou du contenu en plusieurs étapes dans un format visuellement attrayant.

## Prérequis {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Créer un modèle de carrousel {#create-a-carousel-template}

Vous pouvez créer des modèles de carrousel dans Braze à l'aide du générateur de modèles WhatsApp. Lorsque vous créez des modèles, Braze valide votre contenu pour qu'il respecte les critères de Meta.

Lors de la création d'un modèle dans Braze, vous pouvez utiliser :
- Du Liquid que vous prévoyez d'utiliser lors de l'envoi du message. Braze l'enregistre pour référence ultérieure.
- Des variables génériques comme {% raw %}`{{1}}`{% endraw %}.

{% alert note %}
Les étiquettes Liquid {% raw %}`{% %}`{% endraw %} ne sont pas prises en charge dans le générateur de modèles car elles ne satisfont pas les critères de contenu de Meta.
{% endalert %}

Après la soumission du modèle, il apparaît dans la liste des modèles du WABA et est examiné dans les 24 heures. Cependant, l'examen est souvent effectué en quelques minutes.

### Étape 1 : Accéder au générateur de modèles {#step-1-access-the-template-builder}

1. Dans Braze, accédez à **Modèles**.
2. Sélectionnez **Modèles WhatsApp** parmi les options disponibles.

![Modèles WhatsApp dans le menu de navigation des modèles.]({% image_buster /assets/img/whatsapp/templates/whatsapp_templates.png %}){: style="max-width:70%;"}

{: start="3"}
3. Sélectionnez **Créer un modèle de carrousel**.

![Bouton pour créer un modèle de carrousel.]({% image_buster /assets/img/whatsapp/templates/create_carousel_template.png %})

### Étape 2 : Configurer les paramètres du modèle {#step-2-configure-template-settings}

Remplissez les champs requis.

| Champ | Description |
| --- | --- |
| Compte WhatsApp Business | Sélectionnez le WABA dans lequel ce modèle sera stocké. N'oubliez pas que tous les groupes d'abonnement et numéros de téléphone de ce WABA auront accès au modèle. |
| Langue du modèle | Sélectionnez la langue de votre modèle. Meta limite les modèles à une seule langue, choisissez donc la langue que votre audience verra. |
| Nom du modèle | Saisissez un nom descriptif qui vous aidera à identifier ce modèle ultérieurement. Les noms de modèles ne peuvent pas contenir d'espaces — utilisez des traits de soulignement ou supprimez les espaces entièrement (par exemple `carousel_example` ou `carouselexample`). |
| Catégorie | Automatiquement défini sur **Marketing**. Tous les messages de carrousel sont catégorisés comme messages marketing. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Configurer les paramètres du modèle" }

![Panneau des détails du modèle WhatsApp avec un compte WhatsApp Business sélectionné, l'anglais comme langue du modèle et un nom de modèle « welcome_message ».]({% image_buster /assets/img/whatsapp/templates/whatsapp_template_details.png %}){: style="max-width:70%"}

### Étape 3 : Ajouter le contenu du corps {#step-3-add-body-content}

Chaque message de carrousel doit commencer par un contenu de corps, c'est-à-dire le texte qui apparaît avant les cartes du carrousel.

Vous pouvez inclure des variables Liquid pour la personnalisation, comme {% raw %}`{{first_name}}`{% endraw %}, ce qui crée un emplacement de variable vide pouvant être rempli avec du contenu dynamique ou modifié ultérieurement lors de l'utilisation du modèle dans des Campaigns. Les variables ne peuvent pas être placées tout au début ou à la fin du contenu du corps.

### Étape 4 : Configurer les paramètres du carrousel {#step-4-configure-carousel-settings}

Avant de créer des cartes individuelles, définissez la structure globale du carrousel à l'aide des paramètres du carrousel. Ces paramètres s'appliquent à toutes les cartes et ne peuvent pas être modifiés après la soumission du modèle.

#### Type de média {#media-type}

Choisissez le type de média : **Image** ou **Vidéo**. Ce choix s'applique à toutes les cartes.

![Composeur avec des options pour sélectionner un type de média Image ou Vidéo.]({% image_buster /assets/img/whatsapp/templates/media_types.png %})

#### Configuration des boutons {#button-configuration}

Choisissez le type de bouton : **Réponse rapide**, **Numéro de téléphone** ou **Visiter le site web**. Cette configuration s'applique à toutes les cartes. Ensuite, sélectionnez jusqu'à deux boutons par carte.

### Étape 5 : Créer les cartes du carrousel {#step-5-create-carousel-cards}

Vous pouvez maintenant créer les cartes individuelles du carrousel. Toutes les cartes conservent la même forme et la même structure. Vous pouvez ajouter jusqu'à 10 cartes, mais vous devez en ajouter au moins deux.

{% alert important %}
Vous ne pouvez pas modifier le nombre de cartes après avoir soumis le modèle à Meta pour examen.
{% endalert %}

1. Téléchargez une image ou une vidéo, selon le type de média que vous avez sélectionné.
2. Ajoutez du texte ou une description à la carte.
3. Configurez le texte et les actions des boutons.
4. Ajoutez des variables Liquid si nécessaire. Vous pouvez les ajouter partout où un bouton **+** est présent.

#### Dupliquer une carte {#duplicate-a-card}

Pour copier une carte existante, sélectionnez le menu à trois points sur la carte que vous souhaitez dupliquer et sélectionnez **Dupliquer la carte**. Braze copie le média, le texte et la configuration des boutons de la carte vers une nouvelle carte ajoutée à la fin du carrousel.

Vous pouvez avoir entre 2 et 10 cartes. **Dupliquer la carte** n'est pas disponible lorsque le carrousel compte déjà 10 cartes ou après que vous avez soumis le modèle à Meta (le nombre de cartes est alors fixe).

{% alert tip %}
Utilisez les variables Liquid de manière stratégique pour personnaliser le contenu, comme les pourcentages de réduction, les noms de produits ou les offres spécifiques à l'utilisateur. Des variables peuvent être ajoutées au texte des cartes, au texte des boutons et aux URL.
{% endalert %}

![Composeur avec des exemples de cartes de carrousel promouvant des aliments nutritifs.]({% image_buster /assets/img/whatsapp/templates/example_carousel_cards.png %})

### Étape 6 : Prévisualiser et soumettre {#step-6-preview-and-submit}

1. Utilisez la section **Aperçu** pour visualiser l'apparence de votre carrousel pour les utilisateurs.
2. Sélectionnez **Soumettre à Meta pour examen** pour que Braze envoie le modèle à Meta pour approbation.
3. L'approbation prend généralement quelques minutes, mais peut aller jusqu'à 24 heures.
4. Vérifiez le statut du modèle dans votre liste de **Modèles** sur la page des modèles WhatsApp ou dans le sélecteur de Canvas et de Campaign.

{% alert note %}
L'envoi de test n'est pas disponible tant que Meta n'a pas approuvé le modèle. Le statut du modèle s'affiche comme **Brouillon** lors de la création et passe à **Approuvé** une fois que Meta a terminé l'examen.
{% endalert %}

## Utiliser les modèles de carrousel {#use-carousel-templates}

Une fois votre modèle de carrousel approuvé par Meta, vous pouvez l'utiliser dans des Campaigns et des Canvas. Le processus est similaire pour les deux types de messages.

### Étape 1 : Créer un message WhatsApp {#step-1-create-a-whatsapp-message}

1. Dans Braze, accédez à **Campaigns** ou **Canvas** et créez un message WhatsApp.
2. Sélectionnez le groupe d'abonnement qui correspond au compte WhatsApp Business (WABA) de votre modèle.

{% alert important %}
Si vous disposez de plusieurs comptes WhatsApp Business, sélectionnez un groupe d'abonnement du même WABA où le modèle a été créé. Les modèles ne sont pas partagés entre les WABA, mais ils sont partagés entre tous les groupes d'abonnement et numéros de téléphone au sein du même WABA.
{% endalert %}

### Étape 2 : Sélectionner votre modèle de carrousel {#step-2-select-your-carousel-template}

1. Recherchez votre modèle par nom (par exemple « carousel_example »).
2. Vérifiez que le statut du modèle est **Approved**.
3. Sélectionnez le modèle pour le charger dans le compositeur de messages.

### Étape 3 : Personnaliser le contenu dynamique {#step-3-customize-dynamic-content}

Lorsque votre modèle se charge, il contient du contenu verrouillé et du contenu modifiable.

{% tabs local %}
{% tab Contenu verrouillé %}


- Le texte statique (tout contenu soumis sans variables) est verrouillé et ne peut pas être modifié.
- Le nombre de cartes du carrousel est fixe.
- Le type de média et la configuration des boutons ne peuvent pas être modifiés.

{% endtab %}
{% tab Contenu modifiable %}


{% raw %}
- Tout champ contenant une variable peut être modifié avec un Liquid différent.
- Si vous avez soumis le modèle avec du Liquid (par exemple, `{{first_name}}`), Braze conserve et affiche automatiquement ce Liquid.
- Vous pouvez remplacer le Liquid par d'autres variables (par exemple, passer de `{{first_name}}` à `{{last_name}}`).
- Les images avec des variables peuvent être rendues dynamiques en utilisant des URL avec du Liquid.
- Vous pouvez téléverser de nouvelles images depuis la bibliothèque multimédia de Braze au lieu d'utiliser les médias soumis.
{% endraw %}

#### Exemple {#example}

{% raw %}Par exemple, supposons que votre modèle inclut une variable de pourcentage de réduction : `{{discount_percentage}}`. Dans la Campaign, vous pouvez la conserver ou la remplacer par `{{custom_attributes.vip_discount}}`.{% endraw %} Meta exige uniquement que l'emplacement de la variable soit rempli — le Liquid spécifique utilisé est flexible.

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer votre Campaign ou Canvas {#step-4-launch-your-campaign-or-canvas}

Après la composition, poursuivez avec le workflow de lancement de votre Campaign ou Canvas, y compris les tests. Le modèle de carrousel fonctionne comme tout autre modèle de message WhatsApp.

## Bonnes pratiques {#best-practices}

### Directives de contenu {#content-guidelines}

- **Placement du contenu dans le corps du message :** Les variables ne peuvent pas être placées à la fin du contenu du corps du message. Ajoutez au moins un mot ou un signe de ponctuation après chaque variable.
- **Structure de carte cohérente :** Toutes les cartes doivent avoir la même forme, le même type de média et la même configuration de boutons. Planifiez votre contenu en conséquence.
- **Nombre optimal de cartes :** Bien que vous puissiez créer jusqu'à 10 cartes, pensez à l'expérience utilisateur. Un trop grand nombre de cartes peut être accablant ; 3 à 5 cartes conviennent à la plupart des cas d'usage.
- **Valeurs par défaut :** Lorsque vous utilisez des variables Liquid, fournissez toujours des valeurs par défaut pour un aperçu précis. Cela permet de confirmer que le message s'affiche correctement si certaines données du profil utilisateur sont manquantes.

### Comptes WhatsApp Business et groupes d'abonnement {#whatsapp-business-accounts-and-subscription-groups}

- **Comprendre le partage de modèles :** Les modèles sont partagés entre tous les groupes d'abonnement au sein du même compte WhatsApp Business (WABA), mais pas entre différents WABA. Planifiez en conséquence si vous gérez plusieurs WABA.
- **Organiser par WABA :** Si vous disposez de plusieurs WABA, envisagez d'organiser vos modèles par compte professionnel afin d'éviter toute confusion lors de la sélection de modèles dans les Campaigns.

### Tests et approbation {#testing-and-approval}

- **Prévisualiser avant soumission :** Prévisualisez toujours vos modèles pour détecter d'éventuelles erreurs avant de les soumettre à Meta pour approbation.
- **Prévoir le délai d'approbation :** Bien que l'approbation ne prenne généralement que quelques minutes, intégrez les retards potentiels dans la planification du lancement de vos Campaigns.
- **Tester minutieusement :** Après approbation, testez votre carrousel avec des données utilisateur réelles pour confirmer que toutes les variables se remplissent correctement et que l'expérience utilisateur est fluide.

## Résolution des problèmes {#troubleshooting}

| Problème | Solution |
| --- | --- |
| Le modèle n'apparaît pas dans la campagne | Vérifiez que le groupe d'abonnement sélectionné appartient au même WABA que le modèle. Vérifiez également que le statut du modèle est **Approved** et qu'il n'est pas encore au statut **Draft** ou **Pending**. |
| Impossible de placer une variable à la fin du corps | Déplacez la variable plus tôt dans le texte et ajoutez au moins un caractère ou un signe de ponctuation après celle-ci. Il s'agit d'une exigence Meta pour les modèles WhatsApp. |
| Les variables ne se remplissent pas lors du test | Assurez-vous que votre syntaxe Liquid est correcte et que les attributs existent dans vos profils utilisateur. Vérifiez qu'il n'y a pas de fautes de frappe dans les noms de variables et que les valeurs par défaut sont définies lorsque c'est approprié. |
| Le nom du modèle contient des espaces | Les noms de modèles ne peuvent pas contenir d'espaces. Utilisez des underscores à la place (`template_name`) ou supprimez entièrement les espaces (`templatename`). |
| Impossible de modifier le nombre de cartes | Le nombre de cartes est fixé lors de la création du modèle et ne peut pas être modifié après la soumission. Si vous avez besoin d'un nombre différent de cartes, vous devrez créer un nouveau modèle. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }