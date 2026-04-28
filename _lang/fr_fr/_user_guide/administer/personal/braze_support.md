---
nav_title: Assistance Braze
article_title: Assistance Braze
page_order: 4
description: "Cette page vous aidera à localiser le portail d'assistance Braze pour soumettre des commentaires sur les produits Braze. Cette page n'est accessible qu'aux clients Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Assistance Braze {#braze-learning-course-imagebuster-assetsimgblicon3png-httpslearningbrazecomthe-braze-support-portal-stylefloatrightwidth120pxborder0-classnoimgborderbraze-support}

> Découvrez comment accéder au portail d'assistance Braze, soumettre et suivre des demandes d'assistance, et fournir les informations nécessaires à une résolution des problèmes efficace.

## Accéder au portail d'assistance {#access-the-support-portal}

Pour contacter l'équipe d'assistance Braze, accédez au tableau de bord de Braze. Dans le tableau de bord, sélectionnez **Assistance** > **Obtenir de l'aide**.

![Le menu déroulant « Assistance » avec l'option pour obtenir de l'aide.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

En fonction de vos autorisations Braze et selon que vous êtes un contact d'assistance désigné ou non, vous serez dirigé vers le portail d'assistance Braze, où vous pouvez soumettre et suivre des demandes, ou vers notre formulaire d'assistance standard. Si vous ne savez pas si vous êtes un contact d'assistance Braze, contactez l'administrateur Braze de votre entreprise, votre gestionnaire de réussite Braze ou le propriétaire du compte.

## Ajouter des contacts d'assistance désignés {#adding-designated-support-contacts}

Les contacts d'assistance désignés peuvent accéder à toutes les demandes d'assistance de votre entreprise, quel que soit l'auteur de la soumission. Vous pouvez définir des utilisateurs comme contacts d'assistance désignés directement depuis la page **Modifier l'utilisateur**.

1. Accédez à **Paramètres** > **Utilisateurs de l'entreprise**, puis recherchez l'utilisateur par son nom ou son adresse e-mail.
2. Sélectionnez le nom de l'utilisateur ou survolez la ligne du nom de l'utilisateur pour afficher un menu.
3. Dans le menu, sélectionnez **Modifier** pour être redirigé vers la page **Modifier l'utilisateur**.
4. Cochez la case **Définir cet utilisateur comme contact d'assistance désigné pour le portail d'assistance Braze**.

![La case à cocher pour définir un utilisateur comme contact d'assistance désigné.]({% image_buster /assets/img_archive/designated_support_contact.png %}){: style="max-width:70%;"}

### Obtenir l'accès {#gaining-access}

Lorsqu'un utilisateur est désigné comme contact d'assistance, le portail d'assistance Braze lui envoie un e-mail de bienvenue avec des instructions pour configurer son accès.

## Consulter les demandes de votre entreprise {#view-cases-from-your-company}

Si vous êtes un contact d'assistance désigné, utilisez les vues de filtre **Mon organisation** dans le portail d'assistance pour consulter toutes les demandes soumises par les utilisateurs de votre entreprise. Les demandes provenant de tous les canaux de soumission (BrazeAI Operator<sup>TM</sup>, formulaire web, e-mail ou portail) sont incluses dans ces vues.

## Fournir des captures d'écran de la console de développement {#provide-developer-console-screenshots}

Lorsque vous communiquez avec l'assistance, vous pourriez avoir besoin d'accéder à votre console de développement pour fournir des informations supplémentaires :
- Chrome
  1. Faites un clic droit sur la page web et sélectionnez **Inspecter**.
  2. Sélectionnez l'onglet **Console** dans la fenêtre qui s'ouvre.
  3. Prenez une capture d'écran de l'onglet Console.<br><br>
- Firefox
  1. Faites un clic droit sur la page web et sélectionnez **Inspecter l'élément**.
  2. Sélectionnez l'onglet **Console** dans la fenêtre qui s'ouvre.
  3. Prenez une capture d'écran de l'onglet Console.<br><br>
- Safari
  1. Accédez à Safari dans la barre de menus en haut de votre écran, puis sélectionnez **Préférences**.
  2. Sélectionnez **Avancé**, puis cochez la case à côté de **Afficher le menu Développement dans la barre des menus**. Vous pouvez ensuite fermer la fenêtre.
  3. Faites un clic droit sur la page web et sélectionnez **Inspecter l'élément**.
  4. Sélectionnez l'onglet **Console** dans la fenêtre qui s'ouvre.
  5. Prenez une capture d'écran de l'onglet Console.

## Bonnes pratiques pour soumettre une demande d'assistance {#best-practices-for-submitting-a-support-case}

### Fournir autant d'informations que possible {#provide-as-much-information-as-possible}

Plus vous pouvez fournir d'informations, mieux c'est. Incluez des détails tels que l'espace de travail, l'URL de la Campaign ou du Segment, ainsi que tout ID externe pertinent. Cela peut nous aider à résoudre votre problème plus efficacement.

### Fournir un échantillon d'utilisateurs {#provide-a-sample-of-users}

Partagez un échantillon d'utilisateurs plutôt que l'ensemble du segment concerné. Fournir un nombre réduit d'utilisateurs nous aide à affiner notre périmètre et à accélérer nos investigations.

### Joindre des journaux réseau (journaux HAR) {#attach-network-logs-har-logs}

Si vous contactez l'assistance, il sera utile que l'utilisateur concerné collecte des journaux réseau (journaux HAR) depuis son navigateur pendant que le problème se produit. Cela affichera les requêtes réseau entre le navigateur et le serveur pour les composants individuels d'une page web, ainsi que le tableau de bord de Braze que l'utilisateur essaie d'ouvrir.

Demandez à l'utilisateur concerné de procéder comme suit :

1. Ouvrir ses outils de développement. Sous Chrome, cela peut se faire avec le raccourci clavier `option` + `⌘` + `J` (sur macOS). Sous Windows ou Linux, cela peut se faire avec le raccourci `shift` + `CTRL` + `J`.
2. Sélectionner **Network** > **Fetch/XHR** ou **XHR**.
3. Capturer un enregistrement d'écran ou une capture d'écran montrant les colonnes **Name**, **Status**, **Size** et **Time** pour les éléments.<br><br>![L'onglet « Fetch/XHR » dans un navigateur Chrome.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

Joignez ensuite l'enregistrement ou la capture d'écran de l'utilisateur au ticket d'assistance. Ces informations peuvent aider l'investigation de l'équipe d'assistance.

### Préciser le comportement attendu par rapport au comportement réel {#clarify-expected-versus-actual-behavior}

Indiquez-nous ce que vous attendiez et ce qui s'est réellement passé. Cela peut nous aider à réduire les causes possibles du problème.

### Joindre des images pertinentes {#attach-relevant-images}

Pensez à joindre une capture d'écran pour illustrer le problème. Fournir ces images peut considérablement faciliter notre compréhension du problème et accélérer le processus de résolution.

### Évaluer l'impact {#assess-the-impact}

Sélectionnez le niveau de gravité approprié pour nous aider à affecter les bonnes ressources à la résolution du problème.

{% alert important %}
Marquer un problème comme « Critique » signifie que votre instance de production est hors service et que tout travail dans Braze est arrêté.
{% endalert %}

## Résolution des problèmes d'accès {#troubleshooting-access}

Si vous recevez une erreur lors de la connexion au portail d'assistance Braze, telle que `Check your entry`, assurez-vous d'avoir suivi le lien dans votre e-mail de bienvenue pour définir un mot de passe pour le portail. Si vous l'avez déjà fait ou si vous pouviez auparavant vous connecter au portail, créez un ticket d'assistance.