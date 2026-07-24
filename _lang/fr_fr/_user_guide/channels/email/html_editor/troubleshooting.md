---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes liés aux e-mails HTML
page_order: 9
description: "Diagnostiquez les problèmes de rendu et d'éditeur des e-mails HTML à l'aide d'un index des symptômes et d'étapes de résolution standard."
channel: email
---

# Résolution des problèmes liés aux e-mails HTML {#troubleshoot-html-emails}

> Utilisez cette page pour résoudre les problèmes courants liés à l'éditeur d'e-mails HTML et aux envois de test. Pour Inbox Vision et la livrabilité, consultez [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) et [Configuration des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

Identifiez votre symptôme dans le tableau pour accéder à la section correspondante.

| Symptôme | Aller à |
| --- | --- |
| Le HTML de l'e-mail de test s'affiche mal | [Le HTML s'affiche incorrectement dans les e-mails de test](#html-renders-incorrectly-in-test-emails) |
| L'éditeur se comporte de manière inattendue dans Chrome | [Conflits d'extensions](#extension-conflicts) |
| L'e-mail s'affiche différemment selon les clients | [Rendu des e-mails](#email-rendering) |
| La prévisualisation Inbox Vision ne correspond pas à l'e-mail envoyé | [Insertion CSS](#css-inlining) |
| Espaces blancs ou lignes après les images dans les e-mails de test | [Espace blanc sous les images](#white-space-under-images) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptômes liés aux e-mails HTML" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail lorsque le rendu d'un e-mail HTML ou le comportement de l'éditeur ne correspond pas à vos attentes. Commencez à l'étape 1.

1. Validez votre balisage HTML dans l'éditeur ou un validateur externe.
2. Envoyez un [e-mail de test]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) et notez quels clients de messagerie ou navigateurs présentent le problème.
3. Prévisualisez avec [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) pour comparer le rendu entre les différents clients.
4. Éliminez les [conflits d'extensions de navigateur](#extension-conflicts) si l'éditeur lui-même se comporte de manière inattendue.
5. Si le problème persiste, ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support) avec des captures d'écran d'Inbox Vision et des clients concernés.

## Le HTML s'affiche incorrectement dans les e-mails de test {#html-renders-incorrectly-in-test-emails}

**Symptôme :** Un [e-mail de test]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) ne correspond pas à ce que vous attendez de l'éditeur.

Vérifiez d'abord votre configuration HTML, puis consultez les sections [Conflits d'extensions](#extension-conflicts), [Rendu des e-mails](#email-rendering), [Insertion CSS](#css-inlining) et [Espace blanc sous les images](#white-space-under-images).

### Conflits d'extensions {#extension-conflicts}

Certaines extensions de navigateur peuvent causer des problèmes avec l'éditeur d'e-mails. C'est par exemple le cas de [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) utilisé avec Google Chrome. Si vous utilisez l'une de ces extensions, vous devriez soit :

- Modifier les e-mails Braze dans un navigateur qui ne dispose pas de Grammarly comme extension
- Contacter votre gestionnaire de compte Braze et demander à passer vos éditeurs d'e-mails en HTML uniquement ou en texte brut.

La vue en texte brut supprime votre éditeur `WYSIWYG` (what you see is what you get). Assurez-vous donc que tous les membres de l'équipe sont à l'aise avec le HTML avant de faire cette demande.

### Rendu des e-mails {#email-rendering}

Les e-mails s'affichent différemment selon les navigateurs et les clients de messagerie. Prenez donc note des navigateurs et clients de messagerie avec lesquels vous rencontrez des problèmes.

- Prévisualisez vos e-mails en utilisant [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) pour voir à quoi ressemblent vos e-mails dans différents navigateurs et clients de messagerie.
- Une fois que vous avez identifié les navigateurs ou clients de messagerie à l'origine des problèmes, informez votre équipe de développement qu'elle devra modifier le HTML et apporter des ajustements pour prendre en charge ces navigateurs ou clients de messagerie.

### Insertion CSS {#css-inlining}

Il arrive que les prévisualisations dans Inbox Vision ne correspondent toujours pas à ce qui est envoyé avec Braze. Cela peut être dû à la différence d'insertion CSS effectuée par Braze et par d'autres outils. Si vous pensez que c'est le cas, désactivez l'insertion CSS.

### Espace blanc sous les images {#white-space-under-images}

**Symptôme :** Des espaces blancs ou des lignes apparaissent après les images dans les e-mails de test.

Si vous remarquez des espaces blancs ou des lignes après les images dans vos e-mails de test, cela est généralement dû à la façon dont les clients de messagerie affichent les éléments de type inline. Les images sont de type inline par défaut et sont alignées sur la ligne de base, ce qui permet aux navigateurs d'accommoder les jambages (la partie des lettres comme « g » ou « y » qui descend sous la ligne de base). Cela crée un petit écart qui apparaît sous forme d'espace blanc.

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
