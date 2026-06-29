---
nav_title: FAQ
article_title: FAQ sur l'éditeur par glisser-déposer
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "Cet article répond à diverses questions fréquemment posées sur l'éditeur par glisser-déposer."
tool:
  - Campaigns
  - Canvas

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cette page répond à certaines questions fréquemment posées sur l'éditeur par glisser-déposer pour les e-mails.

## Puis-je prévisualiser l'apparence de mon e-mail en mode sombre ? {#can-i-preview-how-my-email-appears-in-dark-mode}

Oui. Accédez à la section **Preview and Test** de l'éditeur par glisser-déposer et activez le **Dark mode**. Nous vous recommandons également de prévisualiser et de tester vos e-mails sur différentes plateformes utilisateur et d'utiliser des images transparentes pour les images d'arrière-plan des lignes lorsque cela est possible.

### Comment concevoir des e-mails pour le mode sombre et le mode clair ? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

Les e-mails n'ont pas besoin d'être envoyés dans des mises en page distinctes pour le mode clair et le mode sombre, car les clients de messagerie et les appareils peuvent appliquer leur propre thème sombre. Cependant, cela peut inverser les couleurs ou masquer les arrière-plans si des couleurs explicites ne sont pas définies sur le conteneur externe et les sections principales. Pour éviter cela, nous vous recommandons de définir des couleurs d'arrière-plan unies afin que votre message soit lisible aussi bien en mode sombre qu'en mode clair.

### Comment modifier le padding de l'e-mail sur mobile sans mettre à jour le padding dans la vue web ? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

Il n'est pas possible de modifier le padding séparément pour les vues mobile et web : toute modification est donc reflétée dans les deux vues. Vous pouvez toutefois ajouter une logique CSS dans l'éditeur HTML qui définit le padding en fonction des différentes tailles d'écran. Cette fonctionnalité n'étant pas prise en charge dans l'éditeur par glisser-déposer, vous pouvez exporter le fichier HTML et utiliser l'éditeur HTML à la place.

### Comment optimiser une ligne de boutons pour qu'elle reste horizontale sur ordinateur de bureau et mobile ? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

Lorsque vous créez un e-mail avec l'éditeur par glisser-déposer et que vous disposez une ligne horizontale de boutons d'appel à l'action, vous constaterez peut-être que les boutons passent en orientation verticale sur mobile.

Pour conserver le même format sur les différentes tailles d'appareil, nous vous recommandons de créer une ligne distincte avec des boutons d'appel à l'action dont le padding est optimisé pour le mobile, et de configurer cette ligne pour qu'elle soit masquée sur un ordinateur de bureau. Avoir deux lignes distinctes vous permet de définir le padding souhaité pour un rendu optimal du texte sur ordinateur de bureau et sur appareil mobile.

### Puis-je ajuster la hauteur des lignes dans l'éditeur par glisser-déposer ? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

La hauteur des lignes s'ajuste automatiquement au contenu. Comme alternative, nous vous recommandons de :
1. Ajouter un bloc séparateur.
2. Cliquer sur le bouton bascule pour activer sa transparence.
3. Ajuster la hauteur.

### Est-il possible de créer des calques dans l'éditeur ? Puis-je ajouter une image d'arrière-plan, superposer une image et ajouter une couche de texte par-dessus ? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

L'éditeur par glisser-déposer prend actuellement en charge deux calques. Vous pouvez définir une image d'arrière-plan de ligne et personnaliser les couleurs d'arrière-plan.

### Puis-je enregistrer mon e-mail par glisser-déposer en tant que modèle après l'avoir créé dans ma campagne ou mon Canvas ? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Non. Vous ne pouvez pas enregistrer un e-mail par glisser-déposer depuis une campagne ou un Canvas en tant que **modèle d'e-mail** par glisser-déposer dans **Templates** > **Email Templates**. Recréez la mise en page dans **Templates** > **Email Templates**, ou partez d'un modèle enregistré la prochaine fois. Pour les instructions, consultez [Créer un modèle d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template).

Si vous avez besoin d'un modèle HTML réutilisable, sélectionnez **Download file** lors de la modification du corps par glisser-déposer, ouvrez le fichier HTML depuis le ZIP, puis collez le balisage dans un [modèle d'e-mail HTML]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) à l'aide de l'éditeur de code HTML. Vérifiez à nouveau le Liquid, les liens et les ressources hébergées par la suite.

Pour plus d'informations sur l'emplacement des modèles, consultez [Modèles et médias]({{site.baseurl}}/user_guide/messaging/templates).

### Pourquoi ne puis-je pas modifier la couleur de remplissage d'un bouton dans l'éditeur par glisser-déposer ? {#why-cant-i-change-a-buttons-fill-color-in-the-drag-and-drop-editor}

Les styles au niveau de la page peuvent remplacer les styles au niveau du message. Si la modification du **Fill** d'un bouton ou d'un bloc n'a aucun effet, essayez ce qui suit :
1. Ouvrez les [paramètres de style global des e-mails]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) et sélectionnez **Reset to default** sur le style de page en conflit afin que la couleur définie au niveau du message puisse s'appliquer.
2. Définissez à nouveau la couleur sur le bloc.

### Puis-je ajouter des pièces jointes aux e-mails dans l'éditeur par glisser-déposer ? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

Oui. Vous pouvez ajouter des pièces jointes à votre e-mail en accédant à **Sending Settings** > **Advanced**.

### Comment télécharger le HTML brut d'un e-mail par glisser-déposer ? {#how-do-i-download-the-raw-html-for-a-drag-and-drop-email}

1. Ouvrez votre campagne ou Canvas et modifiez le message e-mail.
2. Sélectionnez **Edit email body** pour ouvrir l'éditeur par glisser-déposer.
3. Sélectionnez **Download file** (en bas de l'éditeur). Extrayez l'archive pour accéder au HTML généré.

Vous pouvez coller ce HTML dans un [bloc HTML]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#content) ou dans l'éditeur HTML lorsque vous avez besoin de modifications de bas niveau, par exemple pour [désactiver le suivi des clics sur des liens spécifiques]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis).

### Pourquoi ma mise en page par glisser-déposer est-elle cassée ? {#why-is-my-drag-and-drop-layout-breaking}

Les problèmes de mise en page sont souvent causés par du **HTML ou CSS personnalisé** qui entre en conflit avec le balisage généré par l'éditeur. Essayez les étapes suivantes :

1. Supprimez ou isolez les blocs HTML personnalisés pour voir si le problème disparaît.
2. Vérifiez les paramètres de l'**éditeur d'e-mail par glisser-déposer** pour les polices personnalisées qui pourraient ne pas se charger dans tous les clients.
3. Dans **Row Properties**, vérifiez le padding et la largeur des colonnes.
4. Lorsque vous ajoutez du HTML personnalisé, privilégiez les mises en page basées sur des tableaux, les images fluides et des largeurs de tableau totales adaptées à la largeur de votre e-mail. Les images en pixels fixes ou les structures non tabulaires cassent souvent dans Outlook et d'autres clients.

### Pourquoi mon bloc de contenu ne s'affiche-t-il pas dans la prévisualisation de l'e-mail ? {#why-doesnt-my-content-block-render-in-email-preview}

Si un bloc de contenu ne s'affiche pas dans la prévisualisation de l'e-mail, vérifiez qu'il n'y a pas de balises d'ancrage non fermées. Pour les URL de Contenu connecté, utilisez le filtre `replace` pour convertir les esperluettes doublement encodées (`&amp;amp;`) en une seule esperluette encodée (`&amp;`). Limitez l'imbrication des blocs de contenu à deux niveaux.

### Pourquoi l'éditeur par glisser-déposer ignore-t-il les paramètres d'alignement ? {#why-is-the-drag-and-drop-editor-ignoring-alignment-settings}

Si l'éditeur par glisser-déposer ignore les paramètres d'alignement, supprimez le CSS ou les blocs HTML personnalisés, supprimez les polices personnalisées, vérifiez les conflits CSS et évitez de dupliquer les blocs de lignes. Contactez l'assistance Braze si le problème persiste.