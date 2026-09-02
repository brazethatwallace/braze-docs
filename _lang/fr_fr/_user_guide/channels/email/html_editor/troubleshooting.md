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

Identifiez votre symptôme dans le tableau ci-dessous pour accéder à la section correspondante.

| Symptôme | Aller à |
| --- | --- |
| Le HTML de l'e-mail de test s'affiche mal | [Le HTML s'affiche incorrectement dans les e-mails de test](#html-renders-incorrectly-in-test-emails) |
| L'éditeur se comporte de manière anormale dans Chrome | [Conflits d'extensions](#extension-conflicts) |
| L'e-mail s'affiche différemment selon les clients de messagerie | [Rendu des e-mails](#email-rendering) |
| L'e-mail affiche du code Liquid ou des liens cassés | [HTML déséquilibré dans les modèles Liquid](#unbalanced-html-in-liquid-templates) |
| L'aperçu Inbox Vision ne correspond pas à l'e-mail envoyé | [Insertion CSS](#css-inlining) |
| Espaces blancs ou lignes après les images dans les e-mails de test | [Espace blanc sous les images](#white-space-under-images) |
| Les analyses de clics n'incluent pas les paramètres de requête | [Limitations de l'analyse des clics sur les liens](#link-click-analytics-limitations) |
| Les exposants provoquent un espacement de ligne incohérent | [Problèmes de hauteur de ligne avec les exposants](#superscript-line-height-issues) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptômes liés aux e-mails HTML" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce parcours lorsque le rendu d'un e-mail HTML ou le comportement de l'éditeur ne correspond pas à ce que vous attendez. Commencez à l'étape 1.

1. Validez votre balisage HTML dans l'éditeur ou un validateur externe.
2. Envoyez un [e-mail de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) et notez quels clients de messagerie ou navigateurs présentent le problème.
3. Prévisualisez avec [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) pour comparer le rendu entre les différents clients.
4. Éliminez les [conflits d'extensions de navigateur](#extension-conflicts) si l'éditeur lui-même se comporte de manière inattendue.
5. Si le problème persiste, ouvrez un [ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support) avec des captures d'écran d'Inbox Vision et des clients concernés.

## Le HTML s'affiche incorrectement dans les e-mails de test {#html-renders-incorrectly-in-test-emails}

### Symptôme {#symptom}

Un [e-mail de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) ne correspond pas à ce que vous attendez de l'éditeur.

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
- Si le problème est lié à [l'affichage du texte alternatif]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text), gardez à l'esprit que ce comportement est contrôlé par le client de messagerie du destinataire, et non par Braze.

### HTML déséquilibré dans les modèles Liquid {#unbalanced-html-in-liquid-templates}

#### Symptôme

Certains utilisateurs reçoivent une version modifiée de l'e-mail dans laquelle le code Liquid s'affiche dans le message, les liens sont cassés ou l'espacement semble incorrect.

Braze utilise un analyseur HTML interne pour préparer les e-mails avant leur envoi. Cet analyseur prend en charge des fonctionnalités telles que la génération de l'accroche, le placement du pixel de suivi, le templating de liens et l'aliasage de lien. Lorsque les balises HTML ne sont pas équilibrées au sein de leurs blocs logiques Liquid ou Content Blocks correspondants, l'analyseur peut modifier le HTML sous-jacent de manière inattendue. Cela peut entraîner :

- Des retours à la ligne issus du rendu Liquid dans certains clients de messagerie
- Un espacement inhabituel dû à des balises `<p>` ajoutées au corps de l'e-mail
- Le contenu de la balise `<head>` déplacé vers l'accroche
- Un rendu incohérent selon les systèmes d'exploitation mobiles
- La suppression du code spécifique à AMP dans les corps d'e-mails AMP, provoquant des échecs de validation
- Des liens cassés lorsque de nombreux paramètres de requête ou media queries sont utilisés

#### Équilibrer le HTML au sein des blocs Liquid {#balance-html-within-liquid-blocks}

Assurez-vous que toutes les balises HTML s'ouvrent et se ferment au sein de leur bloc logique Liquid ou Content Block correspondant. Cela empêche l'analyseur interne d'interpréter le HTML comme invalide et de le modifier.

#### Exemple déséquilibré {#unbalanced-example}

{% raw %}
```liquid
<img src={% if ${language} == 'en' %}"https://example.com/images/banner-en.png" style="width: 100%"{% elsif ${language} == 'de' %}"https://example.com/images/banner-de.png"{% else %}"https://example.com/images/banner-default.png" {% endif %} />
```
{% endraw %}

Dans cet exemple, la balise ouvrante `<img` commence en dehors de tout bloc Liquid, et différentes parties des attributs de la balise sont réparties entre les instructions conditionnelles Liquid. Cette structure perturbe l'analyseur, qui ne peut pas déterminer où la balise commence ou se termine.

#### Exemple équilibré {#balanced-example}

{% raw %}
```liquid
{% if ${language} == 'en' %}
  <img src="https://example.com/images/banner-en.png" style="width: 100%;" />
{% elsif ${language} == 'de' %}
  <img src="https://example.com/images/banner-de.png" style="width: 100%;" />
{% else %}
  <img src="https://example.com/images/banner-default.png" style="width: 100%;" />
{% endif %}
```
{% endraw %}

Dans la version équilibrée, chaque branche Liquid contient une balise `<img>` complète et autonome. Cette approche garantit que l'analyseur traite correctement chaque branche.

#### Corrections supplémentaires {#additional-fixes}

Si vous rencontrez des problèmes de rendu avec les media queries ou de nombreux paramètres de requête, essayez de désactiver l'insertion CSS dans les paramètres de votre e-mail. Cela peut résoudre les conflits entre l'analyseur HTML et les règles CSS complexes.

### Insertion CSS {#css-inlining}

Il arrive que les prévisualisations dans Inbox Vision ne correspondent toujours pas à ce qui est envoyé avec Braze. Cela peut être dû à la différence d'insertion CSS effectuée par Braze et par d'autres outils. Si vous pensez que c'est le cas, désactivez l'insertion CSS.

### Espace blanc sous les images {#white-space-under-images}

#### Symptôme

Des espaces blancs ou des lignes apparaissent après les images dans les e-mails de test.

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

## Limitations de l'analyse des clics sur les liens {#link-click-analytics-limitations}

### Symptôme

L'analyse des clics pour les e-mails comportant de nombreux paramètres de requête uniques ne correspond pas à vos attentes. Vous pouvez constater des comptages de clics agrégés pour des URL déparamétrées au-delà des 100 premiers liens uniques.

### Fonctionnement du suivi des clics sur les liens {#how-link-click-tracking-works}

Braze suit les clics à la fois sur les URL paramétrées (avec des paramètres de requête) et sur les URL de base déparamétrées. Pour les 100 premiers liens paramétrés uniques cliqués dans une Campaign e-mail ou un Canvas, Braze collecte et rapporte les données pour les deux :

- L'URL paramétrée complète (par exemple, `https://example.com?user_id=12345`)
- L'URL de base déparamétrée (par exemple, `https://example.com`)

Au-delà des 100 premiers liens paramétrés uniques cliqués, Braze incrémente uniquement les comptages de clics pour l'URL de base déparamétrée. Cela signifie que :

- L'analyse des clics s'agrège sur le domaine de base et le chemin plutôt que sur les combinaisons individuelles de paramètres de requête
- Vous pouvez toujours suivre l'engagement significatif en fonction des chemins de liens
- Le suivi des clics au niveau de l'utilisateur individuel continue de fonctionner normalement

Ce comportement empêche l'analyse de devenir surchargée par des milliers de combinaisons uniques de paramètres de requête, tout en capturant les tendances globales d'engagement sur les liens.

### Ce que cela signifie pour vos campagnes {#what-this-means-for-your-campaigns}

Si vous vous appuyez sur des paramètres de requête uniques pour suivre le comportement spécifique des utilisateurs dans des plateformes externes (par exemple, `https://example.com?user_id=USER_ID`), sachez que l'analyse des clics de Braze ne conservera ces paramètres que pour les 100 premiers liens uniques cliqués. Au-delà de ce seuil, les clics sont toujours enregistrés dans votre analyse, mais sont attribués à l'URL déparamétrée.

Les données de clics au niveau de l'utilisateur restent disponibles via [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), quel que soit le nombre de liens paramétrés uniques cliqués.

### Problèmes de hauteur de ligne avec les exposants {#superscript-line-height-issues}

#### Symptôme

Le texte contenant des exposants s'affiche avec un espacement de ligne incohérent, où les lignes apparaissent plus rapprochées ou plus éloignées que prévu. Il s'agit d'un problème de rendu courant dans les clients de messagerie et n'est pas spécifique à Braze.

L'utilisation d'exposants dans les e-mails peut provoquer un comportement inattendu de la hauteur de ligne, car les différents clients de messagerie gèrent le texte en exposant de manières variées.

#### Résolution {#resolution}

Utilisez l'éditeur HTML pour contrôler le style des exposants et des éléments environnants.

Pour définir explicitement la hauteur de ligne, ajoutez du CSS en ligne pour définir le `line-height` du texte :

```html
<p style="line-height: 1.5;">Example text with superscript<sup style="line-height: inherit;">1</sup></p>
```

Pour ajuster l'alignement vertical, utilisez la propriété `vertical-align` pour aligner l'exposant sans perturber la hauteur de ligne :

```html
<sup style="vertical-align: top; font-size: smaller;">1</sup>
```

Si les exposants continuent de poser des problèmes, utilisez un `<span>` comme alternative à `<sup>` pour un meilleur contrôle :

```html
<span style="font-size: smaller; vertical-align: top;">1</span>
```
