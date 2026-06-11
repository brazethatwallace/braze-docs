---
nav_title: FAQ
article_title: FAQ sur Audience Sync
alias: /partners/audience_sync_faq/
description: "Cet article fournit des réponses aux questions fréquemment posées sur Audience Sync."
page_order: 80
tool:
  - Canvas

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article fournit des réponses à certaines questions fréquemment posées sur Audience Sync.

### Combien de temps faut-il pour que mes audiences soient générées dans le tableau de bord de mon partenaire Audience Sync ? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

Le temps nécessaire pour générer une audience dépend du partenaire concerné. Tous les réseaux traitent les requêtes de Braze et tentent de faire correspondre les utilisateurs. Ce processus peut généralement prendre de 6 à 48 heures.

Vous pouvez consulter la plage de temps spécifique dans la section Résolution des problèmes de la documentation de chaque partenaire Audience Sync.

### Quel type de données first-party puis-je utiliser dans ma synchronisation d'audience ? {#what-type-of-first-party-data-can-i-use-in-my-audience-sync}

Les champs spécifiques utilisés pour chaque partenaire peuvent varier en fonction des exigences du partenaire.

Par exemple, lorsque vous configurez une synchronisation d'audience vers Facebook, vous pouvez utiliser une grande variété de champs first-party comme l'e-mail, le téléphone, le prénom et le nom de famille, alors qu'avec Snapchat, vous ne pouvez sélectionner que l'e-mail, le téléphone ou l'identifiant publicitaire mobile.

Il est important de noter que les champs utilisateur que vous pouvez sélectionner pour la synchronisation correspondent aux attributs standard de Braze et aux identifiants publicitaires mobiles. Vous devez vous assurer de transmettre correctement ces données via nos SDK ou API.

### Que se passe-t-il lorsque mes données sont traitées pour être envoyées à chaque partenaire Audience Sync ? {#what-happens-when-my-data-is-being-processed-to-send-to-each-audience-sync-partner}

Les données que vous sélectionnez pour envoyer à votre destination Audience Sync seront normalisées. Chaque partenaire peut avoir des spécifications différentes pour la normalisation des données en fonction des exigences de son API. Consultez donc chaque endpoint spécifique à un partenaire pour plus de détails.

De plus, Braze hache toutes les données avant de synchroniser les utilisateurs avec nos partenaires Audience Sync, garantissant que toutes les informations personnelles identifiables sont hachées en utilisant SHA256.

### Pourquoi puis-je sélectionner plusieurs identifiants en une seule étape pour certains partenaires, mais un seul identifiant pour d'autres ? {#why-can-i-select-multiple-identifiers-in-one-step-for-some-partners-but-can-only-select-one-identifier-for-others}

Cela dépend des méthodes d'intégration des partenaires et n'est pas contrôlé par Braze. Certains partenaires (comme Meta) autorisent la synchronisation de plusieurs identifiants, tandis que d'autres (comme Google) n'autorisent la synchronisation que d'un seul identifiant par utilisateur à un moment donné.

### Comment reconnecter mon intégration ? {#how-do-i-reconnect-my-integration}

Si l'utilisateur qui a initialement connecté l'intégration ne fait plus partie de votre entreprise, vous devrez mettre à jour l'intégration avec le nouvel utilisateur en sélectionnant **Change Account**. Sélectionnez ensuite **Confirm** et connectez-vous avec le nouvel utilisateur. Nous vous recommandons de changer d'utilisateur lorsqu'aucune synchronisation active n'est en cours, par exemple avant une entrée planifiée d'utilisateurs dans un Canvas, car la synchronisation pendant la transition d'un utilisateur à un autre peut perturber les Canvas actifs.

L'utilisateur qui se reconnecte doit disposer d'un accès en lecture et en écriture à toutes les audiences afin que les utilisateurs puissent être synchronisés avec les partenaires. Vérifiez que l'utilisateur qui reconnecte l'intégration a accès aux mêmes comptes publicitaires et aux mêmes audiences. Vous n'aurez pas besoin de modifier les étapes du Canvas existantes.

### Quelles sont les erreurs courantes qui peuvent survenir lors de la création et de la gestion de mes synchronisations d'audience ? {#what-are-common-errors-that-can-occur-when-creating-and-managing-my-audience-syncs}

| Erreur | Raison | Solution |
| --- | --- | --- |
| Jeton non valide | Cela peut se produire si vous avez changé votre mot de passe pour vous connecter à un réseau publicitaire spécifique, ou si vos identifiants ont expiré. | Rendez-vous sur la page partenaire correspondante pour déconnecter et reconnecter votre compte. |
| Taille de l'audience trop petite | Cela peut se produire si vous avez créé une étape Audience Sync qui supprime des utilisateurs de vos audiences. Si la taille de votre audience est proche de zéro, le réseau peut signaler que la taille de l'audience est trop petite pour être diffusée. | Vérifiez que votre stratégie Audience Sync ajoute et supprime régulièrement des utilisateurs de manière à ne pas épuiser complètement la taille de l'audience. |
| L'audience n'existe pas | L'étape Audience Sync utilise une audience qui n'existe pas. Cette erreur peut également être déclenchée si vous n'avez pas l'autorisation nécessaire pour accéder à l'audience. | Ajoutez une audience active dans votre configuration Audience Sync ou créez une nouvelle audience. |
| Tentative d'accès au compte publicitaire | Cette erreur se produit si vous n'avez pas les autorisations nécessaires pour le compte publicitaire, une audience que vous avez sélectionnée, ou les deux. | Contactez les administrateurs de votre compte publicitaire pour obtenir l'accès et les autorisations nécessaires. |
| Paramètres non valides | Cela peut se produire si vous n'avez pas configuré une destination Audience Sync spécifique dans Canvas, notamment le compte publicitaire, l'audience ou les champs utilisateur à faire correspondre. | Complétez la configuration de chaque partenaire avant le lancement. |
| Conditions d'utilisation | Pour certaines destinations Audience Sync, comme Facebook, le réseau publicitaire exige d'accepter des conditions d'utilisation spécifiques pour utiliser la fonctionnalité Audience Sync. Cette erreur se déclenche si vous n'avez pas accepté les conditions appropriées. | Vérifiez que vous avez accepté les conditions requises par chaque partenaire. Pour Facebook en particulier, consultez l'article [Résolution des problèmes Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#troubleshooting). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Quelles sont les erreurs courantes qui peuvent survenir lors de la création et de la gestion de mes synchronisations d'audience ?" }