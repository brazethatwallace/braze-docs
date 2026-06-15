---
nav_title: Archivage de l'utilisateur
article_title: Archivage de l'utilisateur
permalink: /user_archival/
page_order: 0
page_type: reference
description: "Cet article de référence décrit les définitions de l'archivage des utilisateurs, le blocage des courriers indésirables et comment personnaliser votre politique d'archivage des utilisateurs."

---
# Archivage de l'utilisateur {#user-archival}

> Chaque semaine, le dimanche à 5 h 30 EST, Braze exécute un processus visant à supprimer les utilisateurs inactifs et les utilisateurs dormants des services Braze. Notez que Braze n'archive pas les utilisateurs à moins que le nombre d'utilisateurs de l'espace de travail n'atteigne le seuil de 250 000.

Ce processus a pour but d'aider Braze à fournir des statistiques précises concernant les audiences atteignables par les campagnes. Il sert également à respecter deux concepts clés du [RGPD][1] :

1. Le principe de limitation du stockage : les données personnelles traitées et stockées ne doivent pas être conservées plus longtemps que nécessaire.
2. Il faut avoir un objectif commercial légitime pour traiter les données personnelles.

En d'autres termes, les données personnelles traitées et stockées ne doivent pas être conservées plus longtemps que nécessaire, et les données personnelles ne doivent être traitées qu'à des fins professionnelles légitimes. Les utilisateurs archivés auront également leur statut de désabonnement supprimé conformément au RGPD.

{% alert important %}
Les utilisateurs archivés seront définitivement supprimés. <br><br>Vous pouvez [personnaliser votre politique d'archivage de l'utilisateur](#customizing-your-user-archival-policy) à l'aide de Canvas. Les clients ont un contrôle total sur le fait qu'un utilisateur soit inactif ou dormant. Canvas offre la possibilité de le faire automatiquement, ce qui vous permet de désactiver efficacement cette fonctionnalité pour une partie ou la totalité de vos utilisateurs inactifs ou dormants.
{% endalert %}

## Définitions de l'archivage de l'utilisateur {#user-archival-definitions}

### Utilisateurs actifs {#active-users}

Braze définit un « utilisateur actif » pour une période donnée comme tout utilisateur qui a enregistré une session dans une application mobile ou un site web, qui a été mis à jour, qui a reçu un message ou qui a interagi avec un message.

Si vous définissez des ID utilisateur pour identifier les utilisateurs lorsqu'un nouvel utilisateur se connecte, il sera compté comme un utilisateur actif distinct. Les utilisateurs mis à jour via l'API seront également comptés comme utilisateurs actifs dans la période où ils ont été mis à jour.

{% alert important %}
Les utilisateurs inactifs et les utilisateurs dormants seront archivés, sauf si l'utilisateur est exclu de l'archivage pour les raisons énumérées ci-dessous.
{% endalert %}

### Utilisateurs inactifs {#inactive-users}

Les « utilisateurs inactifs » sont des utilisateurs qui ne sont pas joignables et qui ont probablement fait l'objet d'une attrition. Les utilisateurs inactifs sont ceux qui répondent à tous ces critères :

- Ne peuvent pas recevoir d'e-mail. Par exemple, ils n'ont pas d'adresse e-mail ou ils sont désabonnés de toutes les listes d'e-mails.
- Ne peuvent pas recevoir de SMS. Par exemple, ils n'ont pas de numéro de téléphone valide ou ils sont désabonnés de tous les groupes d'abonnement SMS.
- Ne peuvent pas recevoir de notifications push. Par exemple, ils ont désinstallé l'application ou désactivé les autorisations de notification push.
- Ne peuvent pas recevoir de message WhatsApp. Par exemple, ils n'ont pas de numéro de téléphone valide ou sont désabonnés de tous les groupes d'abonnement WhatsApp.
- Ne peuvent pas recevoir de message LINE. Par exemple, ils n'ont pas d'ID LINE ou sont désabonnés de tous les groupes d'abonnement LINE.
- N'ont pas utilisé d'application mobile ni visité de site web dans un espace de travail depuis plus de six mois.
- N'ont reçu aucun message d'un espace de travail depuis plus de six mois.
- N'ont pas été mis à jour depuis plus de six mois.

Dans ce cas, ces utilisateurs ne peuvent pas recevoir de communications et ne s'engagent pas avec votre marque. Dans les faits, ces utilisateurs ont fait l'objet d'une attrition.

### Utilisateurs dormants {#dormant-users}

Les « utilisateurs dormants » sont des utilisateurs qui n'ont eu aucune activité au cours des douze derniers mois et :

- N'ont pas utilisé d'application mobile ni visité de site web dans un espace de travail depuis plus de 12 mois.
- N'ont reçu aucun message d'un espace de travail depuis plus de 12 mois.
- N'ont pas été mis à jour depuis plus de 12 mois.

## Utilisateurs du Groupe de contrôle global {#global-control-group-users}

Les utilisateurs du Groupe de contrôle global ne seront jamais archivés, même s'ils répondent à la définition d'utilisateurs inactifs ou dormants.

### Groupe d'échantillons de traitement {#treatment-sample-group}

Les utilisateurs du groupe d'échantillons de traitement dans un Rapport sur le groupe de contrôle global sont exclus de l'archivage.

## Utilisateurs test {#test-users}

Les utilisateurs test ne seront jamais archivés, même s'ils répondent à la définition d'utilisateurs inactifs ou dormants.

## Blocage du spam {#spam-blocking}

Braze bloque les utilisateurs individuels ayant plus de 5 millions de sessions (« utilisateurs factices ») et n'ingère plus leurs événements SDK, car ils sont généralement le résultat d'une intégration incorrecte. Si vous constatez que cela s'est produit pour un utilisateur légitime, ouvrez un ticket auprès de l'[assistance]({{site.baseurl}}/braze_support/) Braze.

Pour trouver les utilisateurs factices de votre tableau de bord, procédez comme suit :

1. Créez un [segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).
2. Sélectionnez le filtre `Session Count` et définissez-le sur `more than 5,000,000`.
3. Exportez le segment via CSV.

Si nécessaire, vous pouvez supprimer les utilisateurs via l'[endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

## Personnaliser votre politique d'archivage de l'utilisateur {#customizing-your-user-archival-policy}

Braze propose des fonctionnalités d'orchestration des données qui vous permettent de personnaliser votre politique d'archivage de l'utilisateur. Créez une politique d'archivage des utilisateurs qui vous offre le meilleur des deux mondes avec le composant Canvas [Mise à jour utilisateur]({{site.baseurl}}/user_update/).

Ceci vous permet de :

- Vous conformer au RGPD et aux bonnes pratiques en matière de confidentialité en supprimant les profils utilisateur qui ne sont plus utiles.
- Conserver tous les profils utilisateur dont vous avez un besoin commercial légitime.

### Étapes {#steps}

1. Ciblez les utilisateurs qui répondent aux critères d'archivage de votre marque et que vous souhaitez conserver. Par exemple, vous pouvez conserver les utilisateurs qui :
    - Ont reçu un message pour la dernière fois il y a plus de 23 semaines ou n'ont jamais reçu de message<br>ET<br>
    - Ont utilisé votre application pour la dernière fois il y a plus de 23 semaines ou n'ont eu aucune session dans votre application<br><br>
      ![Ciblez les utilisateurs qui ont reçu un message pour la dernière fois il y a plus de 23 semaines, qui n'ont jamais reçu de message d'une campagne ou d'une étape du Canvas, qui ont utilisé ces applications pour la dernière fois il y a plus de 23 semaines et qui ont utilisé ces applications exactement zéro fois.][2]<br><br>
2. Définissez la rééligibilité sur un peu moins de 6 mois.<br><br>
      ![Contrôles d'entrée avec la rééligibilité activée et la fenêtre de rééligibilité fixée à 23 semaines.][3]<br><br>
3. Configurez l'étape Mise à jour utilisateur pour ajouter un événement à chaque profil.<br><br>
      ![Étape Mise à jour utilisateur qui ajoute l'événement « do_not_archive » au profil de l'utilisateur.][4]
{% details Exemple d'objet Mise à jour utilisateur %}

{% raw %}
```json
{
    "events": [
        {
            "name": "do_not_archive",
            "time": "{{ 'now' | time_zone: 'UTC' | date: '%Y-%m-%dT%H:%M:%SZ' }}"
        }
    ]
}
```
{% endraw %}

{% enddetails %}

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}