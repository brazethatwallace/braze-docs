---
nav_title: Assistance Braze
article_title: Assistance Braze
page_order: 4
description: "Cette page vous aide à localiser le portail d'assistance Braze pour soumettre des commentaires sur les produits Braze. Cette page n'est accessible qu'aux clients Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Assistance Braze {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomthe-braze-support-portal-stylefloatrightwidth120pxborder0-classnoimgborderbraze-support}

> Découvrez comment accéder au portail d'assistance Braze, soumettre et suivre des demandes d'assistance, et fournir les informations nécessaires à une résolution des problèmes efficace.

## Accéder au portail d'assistance {#access-the-support-portal}

Pour contacter l'équipe d'assistance Braze, accédez à **Support** > **Get help with Operator** pour ouvrir BrazeAI<sup>TM</sup> Operator.

Operator peut résoudre votre problème en utilisant le contexte de votre conversation et de l'écran actuel. Si Operator ne parvient pas à résoudre votre problème, demandez-lui de rédiger un ticket d'assistance basé sur votre conversation et soumettez le ticket dans le portail d'assistance Braze (si vous êtes un contact d'assistance désigné). Vous pouvez également sélectionner <i class="fa-regular fa-circle-question"></i> **Contact Support** dans Operator pour créer un ticket directement. Si **Get help with Operator** n'est pas disponible dans votre tableau de bord, sélectionnez **Support** > **Get help** pour ouvrir le portail d'assistance ou le formulaire d'assistance à la place.

Pour en savoir plus, consultez [créer des tickets d'assistance avec BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets). Si vous ne savez pas si vous êtes un contact d'assistance Braze, contactez l'administrateur Braze de votre entreprise, votre gestionnaire de succès Braze ou le propriétaire du compte.

![Le menu déroulant « Support » affichant « Get help with Operator ».]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}

## Ajout de contacts de support désignés {#adding-designated-support-contacts}

Les contacts de support désignés peuvent accéder à tous les cas de support de votre entreprise, quel que soit l'auteur de la soumission. Vous pouvez définir des utilisateurs comme contacts de support désignés directement depuis la page **Modifier l'utilisateur**.

1. Allez dans **Paramètres** > **Utilisateurs de l'entreprise**, puis recherchez l'utilisateur par son nom ou son adresse e-mail.
2. Sélectionnez le nom de l'utilisateur ou survolez la ligne correspondante pour afficher un menu.
3. Dans le menu, sélectionnez **Modifier** pour être redirigé vers la page **Modifier l'utilisateur**.
4. Cochez la case **Set this user as a Designated Support Contact for Braze Support Portal**.

### Obtenir l'accès {#gaining-access}

Lorsqu'un utilisateur est désigné comme contact de support, le portail de support Braze lui envoie un e-mail de bienvenue contenant les instructions pour configurer son accès.

## Consulter les cas de votre entreprise {#view-cases-from-your-company}

Si vous êtes un contact de support désigné, utilisez les vues de filtre **My Org's** dans le portail de support pour consulter tous les cas soumis par les utilisateurs de votre entreprise. Les cas provenant de tous les canaux de soumission (BrazeAI<sup>TM</sup> Operator, formulaire web, e-mail ou portail) sont inclus dans ces vues.

## Bonnes pratiques pour soumettre un cas au support {#best-practices-for-submitting-a-support-case}

### Fournissez autant d'informations que possible {#provide-as-much-information-as-possible}

Plus vous pouvez offrir d'informations, mieux c'est. Incluez des détails précis comme l'espace de travail, l'URL de la Campaign ou du Segment, ainsi que tout ID externe pertinent. Cela peut nous aider à résoudre votre problème plus efficacement.

### Fournissez un échantillon d'utilisateurs {#provide-a-sample-of-users}

Partagez un échantillon d'utilisateurs plutôt que l'ensemble du Segment affecté. Fournir un nombre réduit d'utilisateurs nous aide à cibler notre périmètre d'analyse et à accélérer nos investigations.

### Précisez le comportement attendu par rapport au comportement réel {#clarify-expected-versus-actual-behavior}

Indiquez-nous ce que vous attendiez et ce qui s'est réellement passé. Cela peut nous aider à identifier les causes possibles du problème.

### Joignez des images pertinentes {#attach-relevant-images}

Pensez à joindre une capture d'écran pour illustrer le problème. Fournir ces images peut considérablement faciliter notre compréhension du problème et accélérer le processus de résolution.

### Évaluez l'impact {#assess-the-impact}

Sélectionnez le niveau de gravité approprié pour nous aider à affecter les bonnes ressources à la résolution du problème.

{% alert important %}
Marquer un problème comme « Critique » signifie que votre instance de production est hors service et que tout travail dans Braze est interrompu.
{% endalert %}

## Résolution des problèmes de chargement du tableau de bord {#troubleshooting-dashboard-load-issues}

Si le tableau de bord de Braze ne se charge pas correctement, essayez les étapes suivantes avant de contacter le support :

1. Ouvrez le tableau de bord dans un autre navigateur ou dans une fenêtre de navigation privée.
2. [Videz le cache et les cookies de votre navigateur]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#clearing-your-browser-cache-and-cookies).
3. Désactivez les bloqueurs de publicités et les extensions de navigateur, puis rechargez le tableau de bord.
4. Si vous utilisez un VPN, déconnectez-vous et réessayez.

Si la console de développement de votre navigateur affiche `ERR_BLOCKED_BY_CLIENT`, une extension ou un bloqueur de publicités empêche le chargement des ressources du tableau de bord. Désactivez le bloqueur pour l'URL de votre tableau de bord de Braze et rechargez la page.

## Résolution des problèmes d'accès {#troubleshooting-access}

Si vous recevez une erreur lors de la connexion au portail d'assistance Braze, telle que `Check your entry`, assurez-vous d'avoir suivi le lien dans votre e-mail de bienvenue pour définir un mot de passe pour le portail. Si vous l'avez déjà fait ou si vous pouviez auparavant vous connecter au portail, créez un ticket d'assistance.