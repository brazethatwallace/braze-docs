---
nav_title: FAQ
article_title: FAQ sur l'éditeur par glisser-déposer
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "Questions fréquemment posées sur l'éditeur d'e-mails par glisser-déposer."
tool:
  - Campaigns
  - Canvas


---

# Questions fréquemment posées {#frequently-asked-questions}

> Cette page répond à certaines questions fréquemment posées sur l'éditeur par glisser-déposer pour les e-mails.

## Puis-je prévisualiser l'apparence de mon e-mail en mode sombre ? {#can-i-preview-how-my-email-appears-in-dark-mode}

Oui. Accédez à la section **Aperçu et test** de l'éditeur par glisser-déposer et activez le **Mode sombre**. Nous vous recommandons également de prévisualiser et de tester vos e-mails sur différentes plateformes utilisateur et d'utiliser des images transparentes pour les images d'arrière-plan des lignes lorsque cela est possible.

## Comment concevoir des e-mails pour le mode sombre et le mode clair ? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

Les e-mails n'ont pas besoin d'être envoyés dans des mises en page distinctes pour le mode clair et le mode sombre, car les clients de messagerie et les appareils peuvent appliquer leur propre thème sombre. Cependant, cela peut inverser les couleurs ou masquer les arrière-plans si des couleurs explicites ne sont pas définies sur le conteneur externe et les sections principales. Pour éviter cela, nous recommandons de définir des couleurs d'arrière-plan solides afin que votre message reste lisible aussi bien en mode sombre qu'en mode clair.

Certains clients de messagerie remplacent les images d'arrière-plan ou inversent le texte à faible contraste en mode sombre, de sorte que le corps du texte peut sembler absent ou s'afficher différemment selon les clients (par exemple, Gmail sur iOS par rapport à Android). Définissez `background-color` sur le conteneur externe et les sections principales au lieu de vous appuyer uniquement sur des images d'arrière-plan pour les fonds clairs.

## Pourquoi ma police personnalisée n'apparaît-elle pas dans l'aperçu de l'e-mail par glisser-déposer ? {#why-doesnt-my-custom-font-appear-in-drag-and-drop-email-preview}

Les polices personnalisées se chargent dans l'aperçu de l'éditeur lorsqu'un bloc **Text** du message fait référence à la police. Si l'aperçu affiche toujours une police de substitution après avoir configuré une police personnalisée dans les paramètres de l'**éditeur d'e-mails par glisser-déposer**, ajoutez un bloc **Text** qui utilise cette police afin que l'éditeur la charge pour l'aperçu. Vérifiez que le partage de ressources entre origines (CORS) est activé sur votre fichier de police. Revérifiez **Preview and Test** ainsi que vos clients de messagerie cibles avant d'envoyer. Pour les étapes de configuration, consultez [Police personnalisée]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings#custom-font).

## Comment conserver la mise en forme du texte lorsque je copie-colle depuis une autre application ? {#how-can-i-carry-over-text-formatting-when-i-copy-and-paste-from-another-application}

Les différents éditeurs de texte et applications ont leur propre façon de gérer la mise en forme du texte, qui n'est pas toujours universellement reconnue. Lorsque vous copiez-collez du texte mis en forme depuis l'extérieur de Braze dans l'éditeur par glisser-déposer, la mise en forme enrichie peut ne pas être conservée.

Pour coller du texte sans mise en forme enrichie, utilisez l'une de ces méthodes :
- Sur Mac : Appuyez sur <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> au lieu de <kbd>cmd</kbd>+<kbd>V</kbd>
- Sur Windows : Appuyez sur <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> au lieu de <kbd>ctrl</kbd>+<kbd>V</kbd>
- Faites un clic droit dans l'éditeur et sélectionnez **Coller et adapter le style**

## Comment puis-je modifier le padding des e-mails sur mobile sans mettre à jour le padding dans la vue web ? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

Vous ne pouvez pas modifier le padding exclusivement pour les vues mobile et web, donc toute modification est reflétée dans les deux vues. Cependant, vous pouvez ajouter une logique CSS dans l'éditeur HTML qui définit le padding en fonction de différentes tailles d'écran. Cette fonctionnalité n'est pas prise en charge dans l'éditeur par glisser-déposer, vous pouvez donc exporter le fichier HTML et utiliser l'éditeur HTML à la place.

## Comment optimiser une rangée de boutons pour qu'elle reste horizontale sur ordinateur et mobile ? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

Lors de la création d'un e-mail à l'aide de l'éditeur par glisser-déposer, si vous créez une rangée horizontale de boutons d'appel à l'action, vous constaterez peut-être que les boutons passent en orientation verticale sur mobile.

Pour conserver le même format sur les différentes tailles d'appareils, nous recommandons de créer une rangée distincte avec des boutons d'appel à l'action dont le padding est optimisé pour le mobile et de configurer cette rangée pour qu'elle soit masquée sur un appareil de bureau. Avoir deux rangées distinctes vous permet de définir le padding souhaité pour un rendu optimal du texte sur ordinateur et sur mobile.

## Puis-je ajuster la hauteur des lignes dans l'éditeur par glisser-déposer ? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

La hauteur des lignes s'ajuste automatiquement au contenu. Comme alternative, nous vous recommandons de :
1. Ajouter un bloc séparateur.
2. Cliquer sur le bouton pour activer sa transparence.
3. Ajuster la hauteur.

## Est-il possible de créer des calques dans l'éditeur ? Puis-je ajouter une image d'arrière-plan, superposer une image et ajouter un calque de texte par-dessus ? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

L'éditeur par glisser-déposer prend actuellement en charge deux calques. Vous pouvez définir une image d'arrière-plan pour une ligne et personnaliser les couleurs d'arrière-plan.

## Puis-je enregistrer mon e-mail en glisser-déposer comme modèle après l'avoir créé dans ma Campaign ou mon Canvas ? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Non. Vous ne pouvez pas enregistrer un e-mail en glisser-déposer depuis une Campaign ou un Canvas en tant que **modèle d'e-mail** en glisser-déposer dans **Templates** > **Email Templates**. Recréez la mise en page sous **Templates** > **Email Templates**, ou partez d'un modèle enregistré la prochaine fois. Pour les instructions, consultez [Créer un modèle d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template).

Si vous avez besoin d'un modèle HTML réutilisable, sélectionnez **Download file** lors de la modification du corps en glisser-déposer, ouvrez le fichier HTML depuis le ZIP, puis collez le balisage dans un [modèle d'e-mail HTML]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) à l'aide de l'éditeur de code HTML. Vérifiez à nouveau le Liquid, les liens et les ressources hébergées par la suite.

Pour plus d'informations sur l'emplacement des modèles, consultez [Templates and Media]({{site.baseurl}}/user_guide/messaging/templates).

## Pourquoi ne puis-je pas modifier la couleur de remplissage d'un bouton dans l'éditeur par glisser-déposer ? {#why-cant-i-change-a-buttons-fill-color-in-the-drag-and-drop-editor}

Les styles au niveau de la page peuvent remplacer les styles au niveau du message. Si la modification du **Remplissage** d'un bouton ou d'un bloc ne produit aucun effet, essayez ce qui suit :
1. Ouvrez les [paramètres de style global des e-mails]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) et sélectionnez **Réinitialiser par défaut** sur le style de page en conflit afin que la couleur définie au niveau du message puisse s'appliquer.
2. Définissez à nouveau la couleur sur le bloc.

## Puis-je ajouter des pièces jointes aux e-mails dans l'éditeur par glisser-déposer ? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

Oui. Vous pouvez ajouter des pièces jointes à votre e-mail en accédant à **Paramètres d'envoi** > **Avancé**.

## Comment télécharger le HTML brut d'un e-mail créé par glisser-déposer ? {#how-do-i-download-the-raw-html-for-a-drag-and-drop-email}

1. Ouvrez votre Campaign ou Canvas et modifiez le message e-mail.
2. Sélectionnez **Modifier le corps de l'e-mail** pour ouvrir l'éditeur par glisser-déposer.
3. Sélectionnez **Télécharger le fichier** (en bas de l'éditeur). Extrayez l'archive pour accéder au HTML généré.

Vous pouvez coller ce HTML dans un [bloc HTML]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#content) ou dans l'éditeur HTML lorsque vous avez besoin d'effectuer des modifications de bas niveau, par exemple pour [désactiver le suivi des clics sur des liens spécifiques]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis).

## Pourquoi ma mise en page par glisser-déposer se casse-t-elle ? {#why-is-my-drag-and-drop-layout-breaking}

Les problèmes de mise en page sont souvent causés par du **HTML ou CSS personnalisé** qui entre en conflit avec le balisage généré par l'éditeur. Essayez les étapes suivantes :

1. Supprimez ou isolez les blocs HTML personnalisés pour voir si le problème disparaît.
2. Vérifiez les paramètres de l'**éditeur d'e-mails par glisser-déposer** pour les polices personnalisées qui pourraient ne pas se charger dans tous les clients.
3. Dans **Row Properties**, vérifiez le remplissage (padding) et les largeurs des colonnes.
4. Lorsque vous ajoutez du HTML personnalisé, privilégiez les mises en page basées sur des tableaux, les images fluides et des largeurs totales de tableau adaptées à la largeur de votre e-mail — les images en pixels fixes ou les structures non tabulaires se cassent souvent dans Outlook et d'autres clients.

## Pourquoi mon Content Block ne s'affiche-t-il pas dans l'aperçu de l'e-mail ? {#why-doesnt-my-content-block-render-in-email-preview}

Si un Content Block ne s'affiche pas dans l'aperçu de l'e-mail, vérifiez qu'il n'y a pas de balises d'ancrage non fermées. Pour les URL de contenu connecté, utilisez le filtre `replace` pour convertir les esperluettes doublement encodées (`&amp;amp;`) en une seule esperluette encodée (`&amp;`). Limitez l'imbrication des Content Blocks à deux niveaux.

## Pourquoi un Content Block en glisser-déposer perd-il son style mobile à l'intérieur d'un bloc de code personnalisé ? {#why-does-a-drag-and-drop-content-block-lose-mobile-styling-inside-a-custom-code-block}

Lorsque vous placez un **Content Block** en glisser-déposer à l'intérieur d'un bloc de **code personnalisé** (HTML), le style et l'alignement spécifiques au mobile du Content Block peuvent ne pas s'appliquer dans le message envoyé. Lorsque le Content Block et le modèle utilisent tous deux l'éditeur par glisser-déposer, ajoutez le Content Block en tant que ligne distincte au lieu de l'imbriquer dans du code personnalisé.

Lorsque vous empilez plusieurs Content Blocks, utilisez une ligne séparée pour chaque bloc au lieu de placer plusieurs blocs dans une seule ligne.

## Pourquoi l'éditeur par glisser-déposer ignore-t-il les paramètres d'alignement ? {#why-is-the-drag-and-drop-editor-ignoring-alignment-settings}

Si l'éditeur par glisser-déposer ignore les paramètres d'alignement, supprimez le CSS personnalisé ou les blocs HTML, supprimez les polices personnalisées, vérifiez les conflits CSS et évitez de dupliquer les blocs de lignes. Contactez le support Braze si le problème persiste.

## Pourquoi le code couleur hexadécimal que j'ai choisi ne correspond-il pas à la police dans mon e-mail ? {#why-does-my-chosen-hex-color-code-not-match-the-font-in-my-email}

Si vous utilisez un Content Block, celui-ci peut avoir son propre paramètre de couleur de police. Sélectionnez le bloc de texte à l'intérieur du Content Block et supprimez tout remplacement local de **Font color** afin que votre couleur hexadécimale définie au niveau global ou du paragraphe puisse s'appliquer.