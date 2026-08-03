---
nav_title: "Playable"
article_title: "Playable"
description: "Cet article de référence présente le partenariat entre Braze et Playable, une plateforme vidéo qui vous permet d'ajouter du contenu vidéo à vos campagnes e-mail Braze."
alias: /partners/playable/
page_type: partner
search_tag: Partner

---

# Playable

> [Playable](https://playable.video) vous permet d'ajouter du contenu vidéo en lecture automatique à vos campagnes e-mail Braze.

_Cette intégration est maintenue par Playable._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Playable vous permet de diffuser votre meilleur contenu (vidéo de haute qualité) auprès de votre meilleure audience (e-mail), augmentant ainsi vos indicateurs de clics et de post-clic grâce à du contenu captivant et de haute qualité qui se lance automatiquement dans la boîte de réception.

{% alert important %}
Les vidéos intégrées ne sont pas prises en charge nativement par de nombreux clients de messagerie et peuvent considérablement augmenter la taille de l'e-mail, ce qui risque d'entraîner le marquage des messages comme spam. Playable résout ce problème en diffusant du contenu vidéo optimisé qui fonctionne sur l'ensemble des clients de messagerie. Pour plus de détails sur la vidéo dans les e-mails, consultez [Puis-je intégrer des vidéos dans les e-mails ?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-embed-videos-in-emails)
{% endalert %}

## Prérequis {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Playable | Un compte Playable est nécessaire pour profiter de ce partenariat. Si vous ne possédez pas encore de compte Playable, [créez un compte Playable](https://signup.playable.video). |
| Contenu vidéo | Importez des fichiers vidéo sur Playable ou fournissez des URL de vidéos provenant de sites tels que Facebook, Instagram, YouTube, X (anciennement Twitter), TikTok, et bien d'autres. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Déploiement {#implementation}

### Étape 1 : Ajoutez votre vidéo à Playable {#step-1-add-your-video-to-playable}

Dans la plateforme Playable, téléchargez des fichiers vidéo ou ajoutez des vidéos en fournissant l'URL de votre vidéo sur Facebook, Instagram, YouTube, X (anciennement Twitter), TikTok, et bien d'autres.

### Étape 2 : Copiez le code d'intégration depuis Playable {#step-2-copy-the-embed-code-from-playable}

Une fois la vidéo téléchargée, Playable génère un code qui, une fois inséré dans votre Campaign Braze, intègre la vidéo dans votre e-mail pour qu'elle se lance automatiquement à l'ouverture. Lorsque votre e-mail est ouvert, les serveurs Playable diffusent la meilleure version possible de votre vidéo en fonction du client de messagerie, de l'appareil, de la taille de l'écran et des conditions réseau.

{% alert tip %}
Les vidéos se lancent automatiquement dans plus de 98 % des boîtes de réception, y compris iPhone Mail, Gmail, Apple Mail, Outlook pour iOS, Outlook pour Android, Outlook pour Mac et les versions récentes d'Outlook 365 pour Windows. Les utilisateurs d'anciennes versions d'Outlook pour Windows verront une image statique à la place.
{% endalert %}

### Étape 3 : Collez le code d'intégration dans Braze {#step-3-paste-the-embed-code-into-braze}

Enfin, collez le code dans votre Campaign e-mail Braze, puis continuez à concevoir, tester et publier votre campagne e-mail.