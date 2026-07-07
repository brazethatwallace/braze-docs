---
nav_title: Approbations
article_title: Approbations
page_order: 1
page_type: reference
description: "Cet article de référence donne un aperçu des différents états qu'une campagne et un Canvas peuvent avoir et ce qu'ils signifient."
tool:
    - Campaigns
    - Canvas
---

# Approbations pour les campagnes et les Canvas {#approvals-for-campaigns-and-canvases}

> Utilisez les approbations pour ajouter un point de contrôle final à vos campagnes et Canvas avant le lancement. Grâce à ce flux de travail, vous pouvez vérifier et approuver le contenu de toutes les sections requises de votre message.

## Comment ça fonctionne {#how-it-works}

Vous pouvez vérifier les détails de votre campagne ou de votre Canvas à la dernière étape de l'édition.

Pour les Canvas comme pour les Campaigns, vous devez enregistrer toutes les modifications avant d'approuver, même s'il s'agit de vos propres modifications. Un utilisateur disposant des autorisations appropriées doit approuver chaque section du résumé avant que le message puisse être lancé. L'état par défaut de chaque section est **Pending Approval**.

{% tabs %}
{% tab campaign %}
Pour lancer une campagne, vous devez approuver ces composants :

- **Messages :** il s'agit du message de la campagne.
- **Delivery :** il s'agit du type de distribution et détermine quand les utilisateurs reçoivent la campagne.
- **Target Audience :** cela détermine qui recevra la campagne.
- **Conversion Events :** il s'agit de l'indicateur que vous suivez à des fins d'engagement et de reporting.
{% endtab %}

{% tab canvas %}
Pour lancer un Canvas, vous devez approuver ces composants clés :

- **Conversion Events :** il s'agit de l'indicateur que vous suivez à des fins d'engagement et de reporting.
- **Entry Schedule :** cela inclut le type de planification d'entrée et le moment où les utilisateurs entrent dans le Canvas.
- **Target Audience :** cela détermine qui entrera dans ce Canvas.
- **Send Settings :** ce sont les options d'envoi pour toutes les étapes du Canvas.
- **Build Canvas :** il s'agit du parcours utilisateur du Canvas.
{% endtab %}
{% endtabs %}

## Activer le flux de travail d'approbation {#turning-on-the-approval-workflow}

Par défaut, le paramètre du flux de travail d'approbation est désactivé pour les Campaigns et les Canvas. Pour activer cette fonctionnalité, accédez à **Paramètres** > **Flux de travail d'approbation** et sélectionnez le basculement applicable :

- **Utiliser le flux de travail d'approbation pour toutes les Campaigns dans [votre espace de travail]**
- **Utiliser le flux de travail d'approbation pour tous les Canvas dans [votre espace de travail]**

{% alert important %}
L'approbation des Campaigns n'est pas prise en charge pour les [Campaigns API]({{site.baseurl}}/api/api_campaigns) et les [campagnes d'e-mail transactionnel]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email).
{% endalert %}

## Définir les autorisations utilisateur {#setting-user-permissions}

Après avoir activé le flux de travail d'approbation, vous devez définir les autorisations utilisateur afin que les utilisateurs de votre entreprise puissent approuver ou refuser les Campaigns et les Canvas. Les deux autorisations peuvent également être appliquées aux espaces de travail ou aux [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) ou ajoutées à un [ensemble d'autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#permission-sets).

{% tabs %}
{% tab campaign %}
Vous devez disposer de l'[autorisation « Approve and Deny Campaigns »]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#managing-limited-and-team-role-permissions). Cette autorisation contrôle qui peut mettre à jour l'état d'approbation d'une campagne. Avec cette autorisation, vous pouvez effectuer les actions suivantes :

- Auto-approuver la campagne
- Approuver et lancer la campagne
- Approuver mais ne pas lancer la campagne (un autre utilisateur disposant de l'autorisation « Send Campaigns, Canvases » peut lancer la campagne)
- Ne pas approuver ni lancer la campagne

Une fois les états d'approbation définis à l'étape **Summary**, toute modification ultérieure apportée à la campagne réinitialise tous les états d'approbation lors de l'enregistrement. Cela s'applique à toute modification effectuée dans un brouillon de campagne ou dans une campagne déjà lancée. Par exemple, si vous ne modifiez que l'audience cible, l'étape **Summary** rétablit les états d'approbation de toutes les sections à l'état par défaut, **Pending Approval**.

{% endtab %}

{% tab canvas %}
Vous devez disposer de l'[autorisation « Approve and Deny Canvases »]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#managing-limited-and-team-role-permissions). Cette autorisation contrôle qui peut mettre à jour l'état d'approbation d'un Canvas. Avec cette autorisation, vous pouvez effectuer les actions suivantes :

- Auto-approuver le Canvas
- Approuver et lancer le Canvas
- Approuver mais ne pas lancer le Canvas (un autre utilisateur disposant de l'autorisation « Send Campaigns, Canvases » peut lancer le Canvas)
- Ne pas approuver ni lancer le Canvas

Une fois les états d'approbation définis à l'étape **Summary**, toute modification ultérieure apportée au Canvas réinitialise tous les états d'approbation lors de l'enregistrement. Cela s'applique à toute modification effectuée dans un brouillon de Canvas ou dans un Canvas déjà lancé. Par exemple, si vous ne modifiez que l'audience cible, l'étape **Summary** rétablit les états d'approbation de toutes les sections à l'état par défaut, **Pending Approval**.

{% alert note %}
**État d'approbation et enregistrement**

- Lorsque vous cliquez sur **Approve** pour une section à l'étape **Summary**, cette approbation est enregistrée immédiatement.
- Le bouton **Save** enregistre les modifications apportées au contenu et aux paramètres du Canvas, pas l'état d'approbation.

Pour éviter de perdre des approbations :

1. Effectuez les modifications nécessaires sur le Canvas, puis cliquez sur **Save**.
2. Une fois l'enregistrement du Canvas terminé, approuvez les sections concernées à l'étape **Summary**.
3. Cliquez à nouveau sur **Save** uniquement si vous apportez des modifications supplémentaires au Canvas après l'approbation. Si vous modifiez le Canvas et enregistrez, tous les états d'approbation sont réinitialisés à **Pending Approval**.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Pour modifier une campagne en production, vous avez besoin de l'autorisation « Approve and Deny Campaigns ». Un utilisateur doit approuver ses modifications car une version brouillon des Campaigns n'est pas encore disponible. Ce n'est pas le cas pour les Canvas, car un utilisateur peut apporter des modifications et les enregistrer en tant que brouillon, et un autre utilisateur peut approuver et lancer le Canvas.
{% endalert %}