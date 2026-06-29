---
nav_title: Assistance Braze
article_title: Assistance Braze
page_order: 4
description: "Cette page vous aidera à localiser le portail d'assistance Braze pour soumettre des commentaires sur les produits Braze. Cette page n'est accessible qu'aux clients Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Assistance Braze {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomthe-braze-support-portal-stylefloatrightwidth120pxborder0-classnoimgborderbraze-support}

> Découvrez comment accéder au portail d'assistance Braze, soumettre et suivre des demandes d'assistance, et fournir les informations nécessaires à une résolution des problèmes efficace.

## Accéder au portail d'assistance {#access-the-support-portal}

Pour contacter l'équipe d'assistance Braze, accédez au tableau de bord de Braze et sélectionnez **Support**. Le menu propose deux options :

- **Get help with Operator** ouvre BrazeAI Operator<sup>TM</sup>, qui peut résoudre votre problème sur-le-champ en utilisant le contexte de votre conversation et de l'écran actuel. Si Operator ne parvient pas à résoudre votre problème, vous pouvez lui demander de rédiger un ticket d'assistance basé sur votre conversation. Pour en savoir plus, consultez [soumettre des tickets d'assistance avec BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets).
- **Get help** vous dirige directement vers le portail d'assistance Braze (si vous êtes un contact d'assistance désigné) ou vers notre formulaire d'assistance standard, où vous pouvez soumettre et suivre des demandes. Si vous ne savez pas si vous êtes un contact d'assistance Braze, contactez l'administrateur Braze de votre entreprise, votre gestionnaire de réussite Braze ou le propriétaire du compte.

![Le menu déroulant « Support » affichant les options « Get help with Operator » et « Get help ».]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}


## Ajouter des contacts d'assistance désignés {#adding-designated-support-contacts}

Les contacts d'assistance désignés peuvent accéder à toutes les demandes d'assistance de votre entreprise, quel que soit l'auteur de la soumission. Vous pouvez définir des utilisateurs comme contacts d'assistance désignés directement depuis la page **Edit user**.

1. Accédez à **Paramètres** > **Utilisateurs de l'entreprise**, puis recherchez l'utilisateur par son nom ou son adresse e-mail.
2. Sélectionnez le nom de l'utilisateur ou survolez la ligne du nom de l'utilisateur pour afficher un menu.
3. Dans le menu, sélectionnez **Edit** pour être redirigé vers la page **Edit user**.
4. Cochez la case **Set this user as a Designated Support Contact for Braze Support Portal**.

### Obtenir l'accès {#gaining-access}

Lorsqu'un utilisateur est désigné comme contact d'assistance, le portail d'assistance Braze lui envoie un e-mail de bienvenue avec des instructions pour configurer son accès.

## Consulter les demandes de votre entreprise {#view-cases-from-your-company}

Si vous êtes un contact d'assistance désigné, utilisez les vues de filtre **My Org's** dans le portail d'assistance pour consulter toutes les demandes soumises par les utilisateurs de votre entreprise. Les demandes provenant de tous les canaux de soumission (BrazeAI Operator<sup>TM</sup>, formulaire web, e-mail ou portail) sont incluses dans ces vues.

## Fournir des captures d'écran de la console de développement {#provide-developer-console-screenshots}

Lorsque vous communiquez avec l'assistance, vous pourriez avoir besoin d'accéder à votre console de développement pour fournir des informations supplémentaires :
- Chrome
  1. Faites un clic droit sur la page web et sélectionnez **Inspect**.
  2. Sélectionnez l'onglet **Console** dans la fenêtre qui s'ouvre.
  3. Prenez une capture d'écran de l'onglet Console.<br><br>
- Firefox
  1. Faites un clic droit sur la page web et sélectionnez **Inspect Element**.
  2. Sélectionnez l'onglet **Console** dans la fenêtre qui s'ouvre.
  3. Prenez une capture d'écran de l'onglet Console.<br><br>
- Safari
  1. Accédez à Safari dans la barre de menus en haut de votre écran, puis sélectionnez **Preferences**.
  2. Sélectionnez **Advanced**, puis cochez la case à côté de **Show Develop menu in menu bar**. Vous pouvez ensuite fermer la fenêtre.
  3. Faites un clic droit sur la page web et sélectionnez **Inspect Element**.
  4. Sélectionnez l'onglet **Console** dans la fenêtre qui s'ouvre.
  5. Prenez une capture d'écran de l'onglet Console.

## Bonnes pratiques pour soumettre une demande d'assistance {#best-practices-for-submitting-a-support-case}

### Fournir autant d'informations que possible {#provide-as-much-information-as-possible}

Plus vous pouvez fournir d'informations, mieux c'est. Incluez des détails tels que l'espace de travail, l'URL de la campagne ou du segment, ainsi que tout ID externe pertinent. Cela peut nous aider à résoudre votre problème plus efficacement.

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

## Résolution des problèmes de chargement du tableau de bord {#troubleshooting-dashboard-load-issues}

Si le tableau de bord de Braze ne se charge pas correctement, essayez les étapes suivantes avant de contacter l'assistance :

1. Ouvrez le tableau de bord dans un autre navigateur ou dans une fenêtre de navigation privée.
2. [Videz le cache et les cookies de votre navigateur]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#clearing-your-browser-cache-and-cookies).
3. Désactivez les bloqueurs de publicités et les extensions de navigateur, puis rechargez le tableau de bord.
4. Si vous utilisez un VPN, déconnectez-vous et réessayez.

Si la console de développement de votre navigateur affiche `ERR_BLOCKED_BY_CLIENT`, une extension ou un bloqueur de publicités bloque les ressources du tableau de bord. Désactivez le bloqueur pour l'URL de votre tableau de bord de Braze et rechargez la page.

## Résolution des problèmes d'accès {#troubleshooting-access}

Si vous recevez une erreur lors de la connexion au portail d'assistance Braze, telle que `Check your entry`, assurez-vous d'avoir suivi le lien dans votre e-mail de bienvenue pour définir un mot de passe pour le portail. Si vous l'avez déjà fait ou si vous pouviez auparavant vous connecter au portail, créez un ticket d'assistance.