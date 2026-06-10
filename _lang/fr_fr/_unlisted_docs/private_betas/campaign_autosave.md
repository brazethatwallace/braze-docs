---
nav_title: Sauvegarde automatique pour les Campaigns
article_title: Sauvegarde automatique pour les Campaigns
permalink: "/campaign_autosave/"
hidden: true
description: "Cet article de référence détaille le fonctionnement de la sauvegarde automatique pour les Campaigns."
page_type: reference
---

# Sauvegarde automatique des Campaigns {#autosaving-campaigns}

> Lorsque vous créez vos Campaigns dans Braze, vos modifications sont désormais automatiquement enregistrées. Vous pouvez ainsi peaufiner les détails de votre Campaign en toute confiance, sachant que votre progression est préservée.

{% alert important %}
La sauvegarde automatique est actuellement en version bêta et n'est disponible que pour les Campaigns. Contactez votre gestionnaire de la satisfaction client si vous souhaitez participer à cette bêta.
{% endalert %}

{% alert warning %}
Lorsque vous modifiez un message dans un éditeur plein écran, comme pour les e-mails ou les messages in-app, les modifications apportées au message ne sont pas sauvegardées automatiquement. Lorsque vous sélectionnez **Done** pour quitter l'éditeur et revenir à la Campaign, les modifications du message seront enregistrées lors de la prochaine sauvegarde automatique. Vous pouvez également enregistrer manuellement votre message par précaution.
{% endalert %}

## Fonctionnement {#how-it-works}

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Vos Campaigns sont automatiquement et périodiquement enregistrées lorsque vous les modifiez et naviguez entre les onglets dans l'éditeur de Campaign.

Les modifications sont enregistrées en tant que brouillon, aussi bien pour les Campaigns en brouillon que pour les Campaigns actives. Pour les Campaigns arrêtées, vos modifications seront enregistrées, mais la Campaign restera arrêtée.

Si vous et un autre utilisateur apportez des modifications à une Campaign, le premier ensemble de modifications sera enregistré. Si vous êtes la deuxième personne à enregistrer des modifications, vous devrez actualiser la page pour voir les dernières mises à jour de la Campaign.

[1]: {% image_buster /assets/unlisted_docs/img/campaign_autosave.png %}