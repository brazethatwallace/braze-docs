---
nav_title: Créer un modèle d'e-mail
article_title: Créer un modèle d'e-mail
page_order: 0
description: "Cet article de référence explique comment créer, personnaliser et gérer des modèles d'e-mail."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Créer un modèle d'e-mail {#create-an-email-template}

> Le tableau de bord de Braze dispose d'un éditeur de modèles d'e-mail qui vous permet de créer des e-mails personnalisés et attrayants, puis de les enregistrer pour une utilisation ultérieure dans des Campaigns. Vous pouvez également charger votre propre [modèle d'e-mail HTML]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template).

## Étape 1 : Accéder à l'éditeur de modèles d'e-mail {#step-1-navigate-to-the-email-template-editor}

Dans le tableau de bord de Braze, allez dans **Contenu** > **E-mail**.

## Étape 2 : Sélectionner votre expérience d'édition {#step-2-select-your-editing-experience}

Choisissez entre l'**éditeur par glisser-déposer** ou l'**éditeur de code HTML** pour votre expérience d'édition.

Vous pouvez également choisir parmi les modèles Braze préconçus, créer un nouveau modèle ou modifier un modèle existant (simple ou [responsive mobile]({{site.baseurl}}/releases/2018/may#mobile-responsive-email-templates)).

![Un modèle d'e-mail pour les soldes de printemps d'une entreprise avec des options pour sélectionner l'éditeur par glisser-déposer ou l'éditeur HTML, ou pour choisir parmi les modèles Braze.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Tout modèle HTML personnalisé existant doit être recréé à l'aide de l'éditeur par glisser-déposer.
{% endalert %}

## Étape 3 : Personnaliser votre modèle {#step-3-customize-your-template}

Après avoir sélectionné votre expérience d'éditeur, c'est l'occasion de faire preuve de créativité en personnalisant votre modèle d'e-mail. Vous pouvez utiliser le HTML pour créer et reproduire votre image de marque dans l'éditeur HTML, ou inclure une variété de [détails créatifs]({{site.baseurl}}/user_guide/channels/email/drag_and_drop) dans l'éditeur par glisser-déposer.

### Inclure un lien de désinscription {#include-an-unsubscribe-link}

Lors de la conception de votre modèle d'e-mail, si vous n'incluez pas de lien de désinscription, Braze vous invitera à en ajouter un dans votre e-mail, car il est exigé par la loi pour tous les e-mails marketing. Vous pouvez ajouter ce lien de désinscription en tant que pied de page en bas de vos e-mails en utilisant l'étiquette Liquid {% raw %}``${email_footer}``{% endraw %}, ou en [personnalisant le pied de page]({{site.baseurl}}/user_guide/channels/email/subscriptions#custom-footer) dans votre modèle.

## Étape 4 : Vérifier les erreurs d'e-mail {#step-4-check-for-email-errors}

Les erreurs d'e-mail sont présentées dans l'onglet **Compose** du flux de travail du message. Les erreurs vous empêchent de poursuivre. Les « avertissements » sont des rappels qui vous aident à suivre les bonnes pratiques. Selon votre activité, vous pouvez choisir de les ignorer.

![Liste des erreurs et avertissements d'un exemple d'e-mail.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Voici la liste des erreurs prises en compte dans notre éditeur :

- Syntaxe Liquid incorrecte
- [Corps d'e-mail de plus de 400 Ko ; il est fortement recommandé que les corps fassent moins de 102 Ko]({{site.baseurl}}/user_guide/channels/email/best_practices)
- Modèles sans lien de désabonnement
- E-mails avec un champ **Body** ou **Subject** vide
- E-mails sans lien de désabonnement

## Étape 5 : Prévisualiser et tester votre message {#step-5-preview-and-test-your-message}

Après avoir terminé la composition de votre modèle, vous pouvez le tester avant de l'envoyer.

En bas de l'écran d'aperçu, sélectionnez **Preview and Test**. Vous pouvez y prévisualiser l'apparence de votre e-mail dans la boîte de réception d'un client. Avec l'option **Preview as User** sélectionnée, vous pouvez prévisualiser votre e-mail en tant qu'utilisateur aléatoire, sélectionner un utilisateur spécifique ou créer un utilisateur personnalisé. Cela vous permet de vérifier que vos appels de contenu connecté et de personnalisation fonctionnent correctement.

Ensuite, vous pouvez utiliser **Copy preview link** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemble l'e-mail pour un utilisateur aléatoire. Pour plus d'informations, consultez [Prévisualisation partageable]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

Vous pouvez également basculer entre les vues bureau, mobile et texte brut pour avoir une idée de l'apparence de votre message dans différents contextes.

{% alert tip %}
Vous êtes curieux de savoir à quoi ressemble votre e-mail pour les utilisateurs en mode sombre ? Activez le bouton bascule **Dark Mode Preview** situé dans la section **Preview and Test** (éditeur par glisser-déposer uniquement).
{% endalert %}

Lorsque vous êtes prêt pour une vérification finale, sélectionnez **Test Send** et envoyez un message test à vous-même ou à un groupe de testeurs de contenu pour vous assurer que votre e-mail s'affiche correctement sur différents appareils et clients de messagerie.

![Exemple de prévisualisation d'e-mail à envoyer pour test.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si vous constatez des problèmes avec votre modèle ou souhaitez apporter des modifications, sélectionnez **Edit Email** pour retourner à l'éditeur. Notez que les modifications effectuées dans l'éditeur **Classic** peuvent ne pas être reflétées dans l'éditeur HTML ou dans la prévisualisation de l'e-mail.

## Étape 6 : Enregistrer votre modèle {#step-6-save-your-template}

Assurez-vous d'enregistrer votre modèle en sélectionnant **Enregistrer le modèle**. Vous êtes maintenant prêt à utiliser ce modèle dans n'importe quelle Campaign ou composant Canvas de votre choix. Pour accéder à votre modèle, sélectionnez l'expérience d'édition avec laquelle vous l'avez créé, puis sélectionnez-le dans la liste des modèles disponibles.

{% alert note %}
Si vous apportez des modifications à un modèle existant, ces changements ne seront pas reflétés dans les Campaigns créées à partir de versions précédentes de ce modèle.
{% endalert %}

### Gérer vos modèles {#manage-your-templates}

Vous pouvez consulter les modèles d'e-mail dans **Modèles** > **Modèles d'e-mail**, en filtrant par statut, type, tags, l'utilisateur qui l'a créé, ou en recherchant par nom de modèle. Vous devez disposer des autorisations utilisateur appropriées, telles que **Voir les modèles d'e-mail**, pour consulter ces modèles. Pour plus de détails, consultez [Autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

Au fur et à mesure que vous créez des modèles d'e-mail, vous pouvez [dupliquer]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicating-templates) et [archiver]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archiving-templates) des modèles d'e-mail. Apprenez-en plus sur la création et la gestion de votre bibliothèque de modèles et de contenu créatif dans [Modèles et médias]({{site.baseurl}}/user_guide/messaging/templates).

### Utiliser vos modèles dans les Campaigns API {#use-your-templates-in-api-campaigns}

Pour utiliser votre e-mail dans une Campaign API, vous avez besoin d'un `email_template_id`, que vous pouvez trouver en bas de tout modèle d'e-mail créé dans Braze.

![Identifiant API situé en bas d'un modèle d'e-mail.]({% image_buster /assets/img/email_templates/template5.png %})

### Commenter les modèles d'e-mail {#comment-on-email-templates}

Vous pouvez collaborer et commenter les modèles d'e-mail dans l'éditeur par glisser-déposer.

1. Sélectionnez le bloc de contenu ou la ligne dans le corps de l'e-mail que vous souhaitez commenter.
2. Sélectionnez l'icône de commentaire <i class="fas fa-comment" aria-label="Commenter"></i>.
3. Saisissez votre commentaire dans la barre latérale, puis sélectionnez **Soumettre**.
4. Après avoir saisi vos commentaires, sélectionnez **Terminé**.
5. Sélectionnez **Enregistrer le modèle** pour enregistrer vos commentaires.

Une fois votre modèle enregistré, les utilisateurs peuvent voir des icônes au-dessus des commentaires non traités. Sélectionnez **Résoudre** pour résoudre ces commentaires.

![Un commentaire de modèle d'e-mail qui dit « Ça me semble bien ».]({% image_buster /assets/img/email_templates/template_comment.png %})

Pour les réponses aux questions fréquemment posées sur les modèles d'e-mail, consultez notre [FAQ sur les modèles]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).