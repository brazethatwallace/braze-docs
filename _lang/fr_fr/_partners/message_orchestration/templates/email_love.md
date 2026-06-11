---
nav_title: "Email Love"
article_title: "Email Love"
description: "Découvrez comment intégrer Braze avec Email Love, un plugin Figma qui vous permet de concevoir et d'exporter des e-mails HTML responsifs et accessibles directement depuis Figma."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Email Love

> [Email Love](https://emaillove.com/) est un plugin Figma qui vous permet de concevoir et d'exporter des e-mails HTML responsifs et accessibles directement depuis Figma. La fonctionnalité Export to Braze d'Email Love utilise l'API de Braze pour télécharger de façon fluide vos modèles d'e-mails vers Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
|------------------------|------------------------------------------------------------------|
| **Compte Email Love** | Un compte Email Love est nécessaire pour profiter de ce partenariat. |
| **Clé REST API Braze** | Une clé REST API Braze avec l'autorisation complète `Templates` activée. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Utiliser Email Love avec Braze {#using-email-love-with-braze}

### Étape 1 : Exécuter le plugin {#step-1-run-the-plugin}

Pour concevoir votre modèle d'e-mail, vous devrez d'abord charger le plugin. Pour des instructions plus détaillées, reportez-vous à la documentation d'Email Love concernant le [téléchargement de votre e-mail vers Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Étape 2 : Créer votre premier cadre {#step-2-create-your-first-frame}

Dans le plugin, sélectionnez le bouton **[+ No Template Selected]** pour créer un nouveau cadre pour la conception de votre e-mail.

### Étape 3 : Concevoir le modèle avec les composants préconstruits d'Email Love {#step-3-design-the-template-with-email-loves-pre-built-components}

Sélectionnez le cadre que vous avez créé et commencez à ajouter des composants (en-têtes, blocs de contenu, CTA et pieds de page) à partir de la bibliothèque **Assets** du plugin pour structurer votre e-mail.

![Composants préconstruits d'Email Love.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Étape 4 : Personnaliser les composants {#step-4-customize-the-components}

Modifiez les composants à l'aide des outils de Figma pour ajuster votre texte, vos images, vos couleurs et vos éléments de mise en page afin d'aligner la conception du modèle sur votre marque. Si vous ajoutez un composant de pied de page, un lien de désabonnement Braze sera automatiquement inclus lors de l'exportation.

![Personnalisation des composants dans Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Étape 5 : Exporter votre modèle d'e-mail vers Braze {#step-5-export-your-email-template-to-braze}

1. Lorsque vous avez terminé, sélectionnez le cadre que vous souhaitez exporter. Notez que vous devrez utiliser un pied de page Email Love contenant un lien de désabonnement pour que l'exportation fonctionne.
2. Sélectionnez le bouton **Export** dans le plugin, puis sélectionnez **Braze** dans le menu déroulant.
3. Copiez et collez votre clé API dans le champ **Braze API Key** du plugin Email Love pour Figma.
4. Sélectionnez le bouton **Set API Key**.
5. Sélectionnez **Change Instance ID**, puis sélectionnez votre ID d'instance Braze.

![Exportation d'un modèle vers Braze depuis le plugin Email Love.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### Étape 6 : Modifier votre e-mail dans Braze {#step-6-edit-your-email-in-braze}

Dans Braze, accédez à **Templates** > **Edit Templates** > **Edit Message**. Dans l'éditeur de modèles, vous pouvez soit modifier le code HTML de votre e-mail, soit utiliser l'**éditeur de texte enrichi** dans l'onglet **Classic**.

## Assistance et résolution des problèmes {#support-and-troubleshooting}

Pour des instructions plus détaillées, reportez-vous à la documentation d'Email Love sur l'[exportation d'un design d'e-mail](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). Pour obtenir une assistance supplémentaire, contactez l'équipe d'assistance d'Email Love.