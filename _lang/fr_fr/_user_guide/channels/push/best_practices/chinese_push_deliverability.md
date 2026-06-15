---
nav_title: Livrabilité pour les appareils Android chinois
article_title: Livrabilité des notifications push pour les appareils Android chinois
page_order: 10

page_type: reference
description: "Cet article présente les nuances de livrabilité des notifications push à connaître lorsque vous ciblez des utilisateurs sur des appareils Android fabriqués par des OEM chinois."
channel: push

---

# Livrabilité des notifications push pour les appareils Android chinois {#push-deliverability-for-chinese-android-devices}

> Certains appareils Android fabriqués par des fabricants d'équipements d'origine (OEM) chinois, tels que Xiaomi, OPPO et Vivo, optimisent l'autonomie de la batterie grâce à une gestion agressive du cycle de vie des applications. Cette optimisation peut avoir pour conséquence involontaire d'interrompre le traitement en arrière-plan des applications, ce qui peut réduire la livrabilité de vos notifications push.<br><br>Pour vous assurer que les performances d'envoi de messages de votre application fonctionnent comme prévu sur ces appareils, vos équipes marketing et d'ingénierie doivent collaborer et suivre les étapes décrites dans cet article.

## Étapes pour les développeurs {#steps-for-developers}
Ces OEM réalisent leurs optimisations en arrêtant de manière agressive les applications en arrière-plan et en les empêchant de se lancer automatiquement pour exécuter des tâches en arrière-plan. En tant que développeur, vous devrez configurer votre application pour demander à l'utilisateur d'assouplir ces restrictions chaque fois que possible.

Pour ce faire, faites démarrer automatiquement votre application sur l'appareil de votre utilisateur final, ce qui lui donne la permission de s'exécuter en arrière-plan et d'écouter les messages provenant de Braze. Malheureusement, comme il s'agit d'un problème spécifique aux OEM et non d'un problème Android, il n'existe pas d'API documentées pour afficher l'invite d'autorisation de démarrage automatique pour chaque OEM.

Pour résoudre ce problème, intégrez une bibliothèque comme [AutoStarter](https://github.com/judemanutd/AutoStarter) dans votre application. AutoStarter prend en charge plusieurs fabricants, ce qui vous offre un moyen simple d'appeler le gestionnaire d'autorisations de démarrage sur un large éventail d'appareils. Après avoir intégré AutoStarter, appelez `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` pour afficher le gestionnaire d'autorisations de démarrage sur l'appareil de votre utilisateur final. Associez cette action à une invite encourageant l'utilisateur final à activer le « démarrage automatique » pour votre application. Votre équipe marketing rédigera ce message — consultez la section suivante !

## Étapes pour les marketeurs {#steps-for-marketers}
Une fois que vos utilisateurs ont accepté de recevoir des notifications push, ils peuvent effectuer des étapes supplémentaires de leur côté pour améliorer la distribution des messages sur ces appareils. Nous vous recommandons de faire suivre votre [message d'amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) d'un message in-app ciblant les utilisateurs sur les appareils OEM chinois avec ces étapes supplémentaires :

- Activer le « démarrage automatique » pour l'application
- Désactiver l'optimisation de la batterie pour l'application

Pour amplifier davantage votre message, ajoutez d'autres canaux pour relayer les informations des notifications push non ouvertes via des canaux hors application tels que SMS, WhatsApp et LINE, ainsi que des canaux in-app comme les messages in-app et les Content Cards. Vos utilisateurs pourront voir tout ce qu'ils auraient pu manquer la prochaine fois qu'ils ouvriront l'application.