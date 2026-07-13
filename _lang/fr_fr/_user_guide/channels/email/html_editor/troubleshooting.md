---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes
page_order: 9
description: "Cet article d'aide vous explique comment résoudre les problèmes liés aux e-mails HTML."
channel: email
---

# Résolution des problèmes {#troubleshooting}

> Cet article aborde les problèmes courants liés aux e-mails HTML et comment les résoudre, notamment les conflits d'extensions, les différences de rendu et l'insertion CSS.

## Le HTML s'affiche incorrectement dans les e-mails de test {#html-renders-incorrectly-in-test-emails}

Si votre [e-mail de test]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) ne s'affiche pas correctement, nous vous recommandons de vérifier d'abord votre configuration HTML. Ensuite, vous pouvez vérifier les points suivants :
* [Conflits d'extensions](#check-conflicts)
* [Rendu des e-mails](#check-rendering)
* [Insertion CSS](#switch-css-inlining)
* [Espace blanc sous les images](#white-space-under-images)

### Conflits d'extensions {#extension-conflicts}

Certaines extensions de navigateur peuvent causer des problèmes avec notre éditeur d'e-mails. C'est par exemple le cas de [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) utilisé avec Google Chrome. Si vous utilisez l'une de ces extensions, vous devriez soit :
- Modifier les e-mails Braze dans un navigateur qui ne dispose pas de Grammarly comme extension
- Contacter votre gestionnaire de compte Braze et demander à passer vos éditeurs d'e-mails en HTML uniquement ou en texte brut.

La vue en texte brut supprime votre éditeur `WYSIWYG` (what you see is what you get). Assurez-vous donc que tous les membres de l'équipe sont à l'aise avec le HTML avant de faire cette demande.

### Rendu des e-mails {#email-rendering}

Les e-mails s'affichent différemment selon les navigateurs et les clients de messagerie. Prenez donc note des navigateurs et clients de messagerie avec lesquels vous rencontrez des problèmes.

- Prévisualisez vos e-mails en utilisant [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#inbox-vision) pour voir à quoi ressemblent vos e-mails dans différents navigateurs et clients de messagerie.
- Une fois que vous avez identifié les navigateurs ou clients de messagerie à l'origine des problèmes, informez votre équipe de développement qu'elle devra modifier le HTML et apporter des ajustements pour prendre en charge ces navigateurs ou clients de messagerie.

### Insertion CSS {#css-inlining}

Il arrive que les prévisualisations dans Inbox Vision ne correspondent toujours pas à ce qui est envoyé avec Braze. Cela peut être dû à la différence d'insertion CSS effectuée par Braze et par d'autres outils. Si vous pensez que c'est le cas, désactivez l'insertion CSS.

### Espace blanc sous les images {#white-space-under-images}

Si vous remarquez un espace blanc ou des lignes apparaissant sous les images dans vos e-mails de test, cela est généralement dû à la façon dont les clients de messagerie affichent les éléments de type inline. Les images sont de type inline par défaut et sont alignées sur la ligne de base, ce qui permet aux navigateurs d'accommoder les jambages (la partie des lettres comme « g » ou « y » qui descend sous la ligne de base). Cela crée un petit écart qui apparaît sous forme d'espace blanc.

Pour corriger ce problème, ajoutez `display: block;` au CSS de vos images :

```html
<style>
  img {
    display: block;
  }
</style>
```

Vous pouvez également appliquer le style directement à des images spécifiques :

```html
<img src="https://example.com/image.jpg" style="display: block;" alt="Image description" />
```

Vous avez encore besoin d'aide ? Ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support).