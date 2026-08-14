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

## Définitions de l'archivage des utilisateurs {#user-archival-definitions}

### Utilisateurs actifs {#active-users}

Braze définit un « utilisateur actif » pour une période donnée comme tout utilisateur ayant enregistré une session dans une application mobile ou un site web, ayant été mis à jour, ayant reçu un message ou ayant interagi avec un message.

Si vous définissez des ID utilisateur pour identifier les utilisateurs lorsqu'un nouvel utilisateur se connecte, il sera comptabilisé comme un utilisateur actif distinct. Les utilisateurs mis à jour via l'API seront également comptabilisés comme utilisateurs actifs pendant la période au cours de laquelle ils sont mis à jour.

{% alert important %}
Les utilisateurs inactifs et les utilisateurs dormants seront archivés, sauf si l'utilisateur est exclu de l'archivage pour les raisons énumérées ci-dessous.
{% endalert %}

### Utilisateurs inactifs {#inactive-users}

Les « utilisateurs inactifs » sont des utilisateurs injoignables qui se sont probablement désabonnés. Les utilisateurs inactifs sont ceux qui remplissent tous les critères suivants :

- Ne peuvent pas recevoir d'e-mail. Par exemple, ils n'ont pas d'adresse e-mail ou se sont désabonnés de toutes les listes d'e-mails.
- Ne peuvent pas recevoir de SMS. Par exemple, ils n'ont pas de numéro de téléphone valide ou se sont désabonnés de tous les groupes d'abonnement SMS.
- Ne peuvent pas recevoir de notification push. Par exemple, ils ont désinstallé l'application ou désactivé les autorisations push.
- Ne peuvent pas recevoir de message WhatsApp. Par exemple, ils n'ont pas de numéro de téléphone valide ou se sont désabonnés de tous les groupes d'abonnement WhatsApp.
- Ne peuvent pas recevoir de message LINE. Par exemple, ils n'ont pas d'ID LINE ou se sont désabonnés de tous les groupes d'abonnement LINE.
- N'ont utilisé aucune application mobile ni visité de site web dans un espace de travail depuis plus de six mois.
- N'ont reçu aucun message d'un espace de travail depuis plus de six mois.
- N'ont pas été mis à jour depuis plus de six mois.

Dans ce cas, ces utilisateurs ne peuvent pas recevoir de messages et n'interagissent pas avec votre marque. Ces utilisateurs se sont effectivement désabonnés.

### Utilisateurs dormants {#dormant-users}

Les « utilisateurs dormants » sont des utilisateurs qui n'ont eu aucune activité au cours des douze derniers mois et :

- N'ont utilisé aucune application mobile ni visité de site web dans un espace de travail depuis plus de 12 mois.
- N'ont reçu aucun message d'un espace de travail depuis plus de 12 mois.
- N'ont pas été mis à jour depuis plus de 12 mois.

## Utilisateurs du groupe de contrôle global {#global-control-group-users}

Les utilisateurs du groupe de contrôle global ne seront jamais archivés, même s'ils correspondent à la définition d'utilisateurs inactifs ou dormants.

### Groupe d'échantillon de traitement {#treatment-sample-group}

Les utilisateurs du groupe d'échantillon de traitement dans un rapport de groupe de contrôle global sont exclus de l'archivage.

## Utilisateurs test {#test-users}

Les utilisateurs test ne seront jamais archivés, même s'ils correspondent à la définition d'utilisateurs inactifs ou dormants.

## Blocage du spam {#spam-blocking}

Braze bloque les profils utilisateur individuels qui deviennent anormalement volumineux (« utilisateurs factices »), car ils résultent généralement d'une intégration incorrecte. Un profil est bloqué lorsqu'il dépasse l'un des seuils suivants :

| Seuil | Description |
| --- | --- |
| Plus de 5 000 000 de sessions | Généralement causé par la réutilisation d'un seul `external_id` pour de nombreux utilisateurs. |
| Plus de 20 000 noms d'événements personnalisés distincts | Généralement causé par la génération d'un nouveau nom d'événement pour chaque événement au lieu de réutiliser un ensemble fixe de noms. |
| Plus de 20 000 noms de produits distincts dans les achats | Généralement causé par la génération d'un nouveau `product_id` pour chaque achat au lieu de réutiliser un ensemble fixe d'identifiants de produits. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Seuils de blocage des utilisateurs factices" }

Lorsqu'un profil est bloqué, Braze cesse d'ingérer toutes les données entrantes pour ce profil, que ce soit depuis les SDK ou la REST API. Les requêtes vers [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) qui font référence à un identifiant bloqué renvoient l'erreur `"provided external_id is blacklisted and disallowed"`. Ce libellé est repris tel quel depuis la réponse de l'API. Braze notifie également votre gestionnaire de compte Braze afin qu'il puisse signaler le problème d'intégration.

Si vous constatez que cela s'est produit pour un utilisateur légitime, soumettez un ticket auprès du [support]({{site.baseurl}}/braze_support) Braze.

Pour trouver les utilisateurs factices de votre tableau de bord, procédez comme suit :

1. Créez un [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Sélectionnez le filtre `Session Count` et définissez-le sur `more than 5,000,000`.
3. Exportez le Segment via CSV.

Le filtre **Session Count** ne trouve que les utilisateurs factices basés sur les sessions. Il n'existe pas de filtre de segmentation pour le nombre de noms d'événements personnalisés distincts ou de noms de produits sur un profil. Contactez donc votre gestionnaire de compte Braze pour identifier les profils bloqués pour ces raisons.

Si nécessaire, vous pouvez supprimer les utilisateurs via l'[endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete).

## Personnaliser votre politique d'archivage de l'utilisateur {#customizing-your-user-archival-policy}

Braze fournit des fonctionnalités d'orchestration des données qui vous permettent de personnaliser votre politique d'archivage de l'utilisateur. Créez une politique d'archivage de l'utilisateur qui vous offre le meilleur des deux mondes grâce au composant Canvas [User Update]({{site.baseurl}}/user_update).

Cela vous permet de :

- Respecter le RGPD et les bonnes pratiques en matière de confidentialité en supprimant les profils utilisateur qui ne sont plus pertinents.
- Fidéliser tout profil utilisateur pour lequel vous avez un besoin commercial légitime.

### Étapes {#steps}

1. Ciblez les utilisateurs qui répondent aux critères d'archivage de votre marque et que vous souhaitez conserver. Par exemple, vous pourriez conserver les utilisateurs qui :
    - Ont reçu un message pour la dernière fois il y a plus de 23 semaines ou n'ont jamais reçu de message<br>ET<br>
    - Ont utilisé votre application pour la dernière fois il y a plus de 23 semaines ou n'ont eu aucune session dans votre application<br><br>
      ![Cibler les utilisateurs qui ont reçu un message pour la dernière fois il y a plus de 23 semaines, n'ont jamais reçu de message d'une Campaign ou d'une étape Canvas, ont utilisé ces applications pour la dernière fois il y a plus de 23 semaines et ont utilisé ces applications exactement zéro fois.][2]<br><br>
2. Définissez la rééligibilité sur une durée légèrement inférieure à 6 mois.<br><br>
      ![Contrôles d'entrée avec la rééligibilité activée et la fenêtre de rééligibilité définie sur 23 semaines.][3]<br><br>
3. Configurez l'étape User Update pour ajouter un événement à chaque profil.<br><br>
      ![Étape User Update qui ajoute l'événement « do_not_archive » au profil de l'utilisateur.][4]
{% details Exemple d'objet User Update %}

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