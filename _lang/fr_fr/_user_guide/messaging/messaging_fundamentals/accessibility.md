---
nav_title: Accessibilité
article_title: Créer des messages accessibles dans Braze
page_order: 0.5
page_type: reference
description: "Cet article de référence explique pourquoi l'accessibilité est importante dans le contenu marketing, comment la langue d'accessibilité (HTML lang) de Braze fonctionne selon les canaux, et comment vous pouvez créer des messages accessibles dans Braze."
---

# Créer des messages accessibles dans Braze {#build-accessible-messages-in-braze}

> Découvrez pourquoi l'accessibilité est importante dans votre contenu marketing, et comment vous pouvez créer des messages accessibles dans Braze. Pour plus de conseils, consultez notre cours [Fondamentaux de l'envoi de messages accessibles](https://learning.braze.com/accessible-messaging-foundations) sur Braze Learning.

Un contenu marketing qui exclut les personnes en situation de handicap, même involontairement, peut empêcher des millions de personnes d'interagir avec votre marque. L'accessibilité en marketing consiste à permettre à chacun de vivre votre marketing, de comprendre votre communication et d'avoir la possibilité d'investir dans votre produit, service ou marque, ou d'en devenir fan.

Lors de la conception de vos messages, prenez le temps supplémentaire de réfléchir à la manière dont vous pouvez rendre vos créations accessibles à l'ensemble de vos clients.

{% alert important %}
Ce contenu est fourni à titre indicatif et ne garantit pas la conformité aux normes d'accessibilité telles que les WCAG. Braze propose des outils qui facilitent la création de messages plus accessibles, mais il est de votre responsabilité de vous assurer que votre contenu final respecte les exigences applicables. L'accessibilité est un sujet complexe comportant de nombreux aspects. De nombreuses entreprises font appel à des spécialistes ou consultants en accessibilité pour s'assurer que leurs pratiques en matière de contenu, de conception et de développement répondent aux besoins de tous les utilisateurs.
{% endalert %}

## L'accessibilité chez Braze {#accessibility-at-braze}

Soutenir une communication accessible, c'est rester ouvert, curieux et prêt à apprendre. Chez Braze, nous avons à cœur d'aider les gens à se connecter, et nous savons que faire de la place pour tout le monde fait partie de cet engagement. L'accessibilité n'est jamais quelque chose que nous considérons comme « terminé », et nous accueillons avec plaisir chaque occasion de continuer à apprendre.

{% multi_lang_include accessibility/feedback.md %}

## Types de handicap à prendre en compte {#areas-of-disability-to-consider}

*Cette section est en partie adaptée de [W3C : Capacités et obstacles divers](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

{% tabs local %}
{% tab Visuel %}

Les handicaps visuels peuvent aller d'une perte de vision légère ou modérée dans un ou les deux yeux, à une perte de vision importante ou totale dans les deux yeux. Certaines personnes ont une sensibilité réduite ou inexistante à certaines couleurs, ou une sensibilité accrue aux couleurs vives.

Pour interagir avec votre contenu, ces utilisateurs ont besoin de pouvoir :

- Agrandir ou réduire la taille du texte et des images
- Personnaliser les paramètres de polices, de couleurs et d'espacement
- Écouter la synthèse vocale du contenu (c'est-à-dire utiliser un lecteur d'écran)
- Écouter les audiodescriptions des vidéos
- Lire le texte à l'aide d'un afficheur Braille

{% alert note %}
- À l'échelle mondiale, au moins 2,2 milliards de personnes souffrent d'une déficience visuelle de près ou de loin (voir [OMS](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment))
- Environ 1 homme sur 12 et 1 femme sur 200 présentent un certain degré de déficience de la vision des couleurs, soit environ 300 millions de personnes dans le monde (voir [NHS](https://www.nhs.uk/conditions/colour-vision-deficiency/))
{% endalert %}

{% endtab %}
{% tab Auditif %}

Les handicaps auditifs peuvent inclure une déficience auditive légère à modérée dans une ou les deux oreilles. Même une perte auditive partielle peut être problématique en ce qui concerne le contenu audio.

Pour comprendre votre contenu, ces utilisateurs s'appuient sur :

- Des transcriptions et des sous-titres du contenu audio
- Des lecteurs multimédias qui affichent les sous-titres et offrent des options pour ajuster la taille et les couleurs du texte des sous-titres
- Des options pour arrêter, mettre en pause et ajuster le volume du contenu audio (indépendamment du volume du système)
- Un audio de premier plan de haute qualité, clairement distinguable de tout bruit de fond

{% alert note %}
- Une personne sur huit aux États-Unis (13 %, soit 30 millions) âgée de 12 ans ou plus présente une perte auditive dans les deux oreilles, selon les examens auditifs standard
- Environ 15 % des adultes américains (37,5 millions) âgés de 18 ans et plus déclarent avoir des difficultés auditives (voir [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing))
{% endalert %}

{% endtab %}
{% tab Physique %}

Les handicaps physiques peuvent inclure une faiblesse et des limitations du contrôle musculaire ou de la sensation, des troubles articulaires, des douleurs qui entravent le mouvement et des membres manquants.

Ces utilisateurs s'appuient sur la prise en charge du clavier pour activer les fonctionnalités (même s'ils n'utilisent pas un clavier standard). Pour interagir avec votre contenu, ces utilisateurs ont besoin de :

- Zones cliquables de grande taille
- Suffisamment de temps pour accomplir les tâches
- Des indicateurs visibles du focus actuel
- Des mécanismes pour passer des blocs de contenu, comme les en-têtes de page ou les barres de navigation

{% alert note %}
Près de 2 millions de personnes aux États-Unis vivent avec une amputation (voir [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

{% endtab %}
{% tab Cognitif %}

Les handicaps cognitifs, d'apprentissage et neurologiques englobent la neurodiversité et les troubles neurologiques, ainsi que les troubles comportementaux et de santé mentale qui ne sont pas nécessairement neurologiques. Ils peuvent affecter n'importe quelle partie du système nerveux et avoir un impact sur la capacité des personnes à entendre, se déplacer, voir, parler et comprendre les informations.

En fonction des besoins individuels, ces utilisateurs s'appuient sur :

- Un contenu clairement structuré
- Un étiquetage cohérent des formulaires, des boutons et des autres contenus
- Des cibles de liens et des interactions globales prévisibles
- Différents moyens de navigation, tels que des menus et des barres de recherche
- Des paramètres pour désactiver le clignotement, le scintillement ou tout autre contenu distrayant
- Un texte plus simple accompagné d'images


{% alert note %}
- Une personne sur cinq aux États-Unis a des difficultés d'apprentissage et d'attention (voir [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.))
- Environ 10 à 20 % de la population mondiale est considérée comme neurodivergente (voir [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- Environ 1 enfant sur 100 est autiste dans le monde (voir [OMS](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Bonnes pratiques {#best-practices}

Créer du contenu accessible n'a pas besoin d'être accablant. De petits choix réfléchis peuvent faire une grande différence. Cette section présente des conseils pratiques qui aident davantage de personnes à lire, naviguer et interagir avec vos messages. Que vous ajustiez votre texte, stylisiez vos boutons ou ajoutiez du texte alt à vos images, chaque amélioration contribue à une expérience plus inclusive. Allons-y.

### Contenu {#content}

#### Structure et flux {#structure-and-flow}

Commençons par les fondations. Lorsque votre contenu a une structure claire, il est plus facile à suivre pour tout le monde, en particulier pour les personnes qui utilisent des lecteurs d'écran ou la navigation au clavier.

- **Divisez votre contenu en sections :** L'utilisation de titres, de puces et de listes aide les gens à comprendre et à parcourir rapidement votre contenu, même lorsqu'ils sont pressés.
- **Ne sautez pas de niveaux de titre :** Les titres donnent une structure à votre contenu, aidant les lecteurs à comprendre rapidement comment les sections sont liées entre elles. Lorsque vous sautez des niveaux de titre (par exemple, en passant directement d'un H2 à un H4), vous brisez cette structure logique. Cela rend la navigation et la compréhension de votre message plus difficiles pour les utilisateurs, en particulier ceux qui utilisent des lecteurs d'écran. Suivez toujours une hiérarchie logique et séquentielle de titres (H1 vers H2 vers H3, et ainsi de suite) pour vous assurer que votre contenu reste organisé, accessible et facile à suivre pour tout le monde.

#### Lisibilité {#readability}

Une fois votre structure en place, l'étape suivante consiste à vous assurer que vos mots sont réellement faciles à lire. Cela signifie garder les choses simples, faciles à parcourir et confortables à lire sur tous les appareils et pour tous les besoins des utilisateurs.

- **Écrivez des phrases courtes et claires :** Les phrases courtes sont faciles à comprendre pour tout le monde, en particulier les personnes utilisant des lecteurs d'écran ou ayant des difficultés à traiter des informations complexes. Écrivez à un niveau de lecture correspondant à la cinquième (environ le septième grade américain). Vous pouvez utiliser des ressources telles que [Hemingway App](https://hemingwayapp.com/) pour vérifier le niveau de lecture de votre texte.
- **Choisissez des tailles de police et des espacements lisibles :** Un texte trop petit peut être difficile à lire, surtout sur mobile. Utilisez au moins 14 px pour le corps du texte. Rendez les titres plus grands pour que les utilisateurs puissent clairement voir la différence. Un espacement supplémentaire entre les lignes (environ 1,5 de hauteur de ligne) et les paragraphes améliore la lisibilité, en particulier pour les personnes ayant des besoins visuels ou cognitifs.
- **Évitez le texte justifié :** Le texte justifié crée un espacement inégal entre les mots, rendant la lecture difficile pour les personnes dyslexiques ou ayant des handicaps cognitifs. Envisagez d'aligner à gauche le contenu qui s'étend sur plus de deux lignes pour les langues de gauche à droite, ou à droite pour les [langues de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).
- **Utilisez le gras, l'italique et les majuscules avec parcimonie :** Mettre trop de texte en évidence rend la lecture difficile, en particulier pour les personnes dyslexiques ou malvoyantes. Restez simple.

#### Clarté et utilisabilité {#clarity-and-usability}

Enfin, parlons des détails les plus fins : les éléments qui aident les utilisateurs non seulement à voir votre contenu, mais aussi à le comprendre et à interagir avec lui.

- **Étiquetez clairement les liens et les boutons :** Assurez-vous que vos textes de [liens](#links) et de [boutons](#buttons) expliquent clairement ce qui va se passer ensuite. Cela aide les personnes utilisant des lecteurs d'écran ou naviguant au clavier à savoir à quoi s'attendre.
- **Allez-y doucement avec les symboles et les emojis :** Les caractères spéciaux et les emojis peuvent rendre votre contenu ludique, mais ils peuvent être déroutants lorsqu'ils sont lus par des lecteurs d'écran. Utilisez-les avec parcimonie et assurez-vous qu'ils ne remplacent pas un texte clair et descriptif.
- **Testez la troncature :** Testez toujours votre texte en [envoyant un message de test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages) sur un appareil pour vous assurer que votre texte n'est pas tronqué. Si votre message est coupé, cela nuit à la fois à vous et à votre audience, car cela empêche votre contenu de les atteindre.

### Langue d'accessibilité {#accessibility-language}

La **langue d'accessibilité** indique aux lecteurs d'écran et autres outils d'assistance dans quelle langue se trouve votre contenu. Pour les canaux qui envoient une page HTML complète ou un e-mail, Braze peut ajouter une balise de langue (`lang`) lorsque vous la définissez dans l'éditeur ou via Liquid. Cela prend en charge le [critère de succès WCAG 2.1 3.1.1 Langue de la page (niveau A)](https://www.w3.org/WAI/WCAG21/Understanding/language-of-page.html).

Si vous laissez la langue d'accessibilité vide et qu'aucune valeur par défaut sûre n'est disponible, Braze omet la balise de langue. Si aucune langue n'est définie, les outils d'assistance se rabattent souvent sur la langue du téléphone ou de l'ordinateur de la personne. Si celle-ci diffère de la langue du message, la prononciation peut être incorrecte.

Les Campaigns et les Canvas utilisent les mêmes éditeurs pour ces options, sauf si une fonctionnalité n'est pas disponible pour votre espace de travail.

#### Configurer la langue d'accessibilité {#configure-accessibility-language}

Lorsque votre éditeur l'inclut, accédez à la section **Accessibilité** dans les paramètres du message. Choisissez une langue dans le menu déroulant ou utilisez Liquid (par exemple {% raw %}`{{accessibility_language}}`{% endraw %} lorsque les [messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) sont activés et que les **paramètres de localisation** sont définis).

#### Messages multilingues {#multi-language-messages}

Dans les **paramètres de localisation**, définissez une langue d'accessibilité pour chaque locale afin que Liquid puisse remplir {% raw %}`{{accessibility_language}}`{% endraw %} pour les envois localisés. Le fait que cette valeur soit déjà choisie pour les nouveaux messages dépend du canal. Pour les flux de travail CSV et de traduction, commencez par [Paramètres de langue et accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility).

#### Prise en charge des canaux et des éditeurs {#channel-and-editor-support}

Utilisez ce tableau pour comparer les canaux. Les valeurs par défaut peuvent différer, alors vérifiez ce que votre audience reçoit réellement.

| Canal | Ce qu'il faut savoir |
| --- | --- |
| E-mail (glisser-déposer, modèle complet) | Définissez la langue dans l'éditeur. Avec les messages multilingues, un modèle d'e-mail complet peut faire correspondre la langue de chaque locale pour vous. Si vous utilisez uniquement des Content Blocks (ligne unique), ces raccourcis ne fonctionnent pas de la même manière : choisissez la langue vous-même là où l'éditeur le permet. |
| E-mail (code HTML) | Braze n'ajoute pas de balise de langue pour vous. Ajoutez-la dans votre HTML si vous en avez besoin. |
| Messages in-app (glisser-déposer) | Lorsque vous choisissez une langue sous **Accessibilité**, Braze ajoute cette langue au HTML externe du message afin que les lecteurs d'écran traitent l'ensemble du message dans cette langue. Avec les messages multilingues activés, les nouveaux messages peuvent utiliser par défaut les langues de vos locales. L'**aperçu** peut n'afficher aucune langue tant que vous n'en avez pas choisi une sous **Paramètres**. |
| Bannières | Même comportement que les messages in-app. |
| Pages de destination | Vous pouvez définir la langue sur la page en direct or en ligne/en production/instantané. Choisissez une langue, ou utilisez Liquid si votre compte autorise Liquid sur les pages de destination. Les valeurs par défaut diffèrent également de celles des messages in-app et des bannières : vérifiez la page publiée. |
| Content Cards | Les Content Cards utilisent un champ **Langue** pour les applications au lieu d'une langue d'accessibilité explicite. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prise en charge des canaux et des éditeurs" }

Lorsque vous écrivez du HTML vous-même, vous pouvez toujours ajouter une balise de langue sur une partie du message (par exemple, une phrase dans une autre langue). Pour plus de modèles, consultez [HTML personnalisé](#custom-html).

#### Référence aux normes {#standards-reference}

Lorsque Braze ajoute une balise de langue au niveau racine du HTML, il suit la règle HTML [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang). Les outils de test recherchent souvent [`html-has-lang`](https://dequeuniversity.com/rules/axe/4.2/html-has-lang). Les Content Cards utilisent votre champ **langue** au lieu de ce modèle HTML.

### Boutons {#buttons}

Utilisez les **boutons** pour indiquer une action, comme l'envoi d'un formulaire ou la lecture d'un carrousel. Si vous naviguez vers une nouvelle URL, envisagez d'utiliser un [lien](#links) à la place.

#### Rédigez un texte clair et orienté vers l'action {#write-clear-action-oriented-text}

Comme pour le texte des liens, les libellés des boutons doivent décrire clairement l'action. Un texte de bouton efficace est spécifique et orienté vers l'action. Par exemple, « Valider la commande » indique clairement aux utilisateurs ce qui se passera lorsqu'ils cliqueront, tandis que simplement « Valider » peut être ambigu. Chaque libellé doit décrire précisément l'action prévue, afin que les lecteurs d'écran et tous les utilisateurs puissent facilement comprendre et anticiper le résultat lorsqu'ils interagissent avec vos boutons.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bon texte de bouton <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Mauvais texte de bouton <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>« Valider la commande »</td>
      <td>« Valider »</td>
    </tr>
    <tr>
      <td>« Créer un compte »</td>
      <td>« S'inscrire »</td>
    </tr>
    <tr>
      <td>« Télécharger notre brochure »</td>
      <td>« Télécharger »</td>
    </tr>
    <tr>
      <td>« Voir les détails du produit »</td>
      <td>« En savoir plus »</td>
    </tr>
    <tr>
      <td>« S'abonner aux mises à jour »</td>
      <td>« S'abonner »</td>
    </tr>
  </tbody>
</table>

Gardez le texte des boutons concis pour éviter la troncature. Si le texte d'un bouton est trop long, il peut être coupé avec des points de suspension au lieu de passer à la ligne.

#### Utilisez un contraste de couleur suffisant {#use-sufficient-color-contrast}

Le texte des boutons doit être facile à lire par rapport à la couleur d'arrière-plan du bouton. Vérifiez que le texte de vos boutons respecte les [minimums de contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) WCAG 2.2 AA :

- Ratio de contraste de 4,5:1 pour le texte de taille normale (la plupart des boutons)
- Ratio de contraste de 3:1 pour le texte de grande taille (généralement 18 pt ou plus)

Un contraste élevé aide les boutons à rester lisibles et cliquables pour tout le monde, y compris les utilisateurs malvoyants ou ceux qui consultent votre message dans des environnements difficiles. Pour plus de conseils, consultez la section [Contraste des couleurs](#color-contrast).

#### Rendez les boutons faciles à toucher {#make-buttons-easy-to-tap}

Assurez-vous que vos boutons (et liens) sont suffisamment grands et espacés les uns des autres pour les utilisateurs sur appareils mobiles. Des [cibles tactiles](#touch-targets) petites ou trop rapprochées peuvent être frustrantes ou impossibles à utiliser pour les personnes ayant des handicaps moteurs.

### Liens {#links}

Utilisez les liens pour la navigation, comme diriger les utilisateurs vers une page externe.

#### Rédigez un texte de lien descriptif {#write-descriptive-link-text}

Rédigez un texte de lien qui décrit clairement où le lien mènera l'utilisateur. Les utilisateurs de lecteurs d'écran passent souvent d'un lien à l'autre pour parcourir le contenu, alors assurez-vous que votre texte de lien peut se suffire à lui-même. Évitez les expressions comme « cliquez ici », « plus » et « cliquez pour plus de détails », car elles sont ambiguës lorsqu'elles sont lues hors contexte.

Par exemple, réfléchissez à la façon dont vous pourriez rédiger un lien vers un bulletin météo.

| Mauvais | Mieux | Idéal |
| --- | --- | --- |
| Cliquez ici | Cliquez ici pour accéder à la météo du jour | La météo du jour |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Rédigez un texte de lien descriptif" }

Comme pour tout contenu, restez direct avec le moins de mots superflus possible.

#### Évitez de styliser les liens comme des boutons {#avoid-styling-links-like-buttons}

Les éditeurs glisser-déposer de Braze produisent du HTML sémantique par défaut, donc les liens n'y sont pas stylisés comme des boutons. Cependant, si vous travaillez avec du [HTML personnalisé](#custom-html) ou effectuez des modifications au niveau du code, gardez ceci à l'esprit :

- Les **liens (`<a>`)** répondent à la touche <kbd>Entrée</kbd>.
- Les **boutons (`<button>`)** répondent aux touches <kbd>Entrée</kbd> et <kbd>Espace</kbd>.

Styliser un lien pour qu'il ressemble à un bouton peut dérouter les personnes qui naviguent au clavier : elles pourraient essayer d'appuyer sur <kbd>Espace</kbd> en s'attendant à ce que cela fonctionne.

Utilisez le bon élément pour l'action :

- Utilisez `<button>` pour les actions, comme soumettre un formulaire ou ouvrir une fenêtre modale.
- Utilisez `<a>` pour la navigation, comme créer un lien vers une autre page ou un fichier.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Cibles tactiles {#touch-targets}

Les cibles tactiles sont toutes les parties de votre message sur lesquelles les utilisateurs appuient pour effectuer une action, comme les boutons, les liens ou les icônes. Ces éléments doivent être suffisamment grands et espacés les uns des autres pour que les gens puissent les toucher facilement, en particulier sur les appareils mobiles.

Lorsque les cibles tactiles sont trop petites ou trop rapprochées, il peut être frustrant ou impossible pour les utilisateurs ayant des difficultés de mobilité ou de dextérité d'interagir avec votre message. Améliorer cela peut aider à réduire les erreurs et créer une expérience plus fluide pour tout le monde.

Voici ce qu'il faut garder à l'esprit :
- **Utilisez une taille de cible tactile adéquate.** Visez une taille minimale de cible tactile de 44 x 44 pixels. Cela est conforme aux directives WCAG 2.2 pour les [cibles tactiles](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) et aux normes courantes d'utilisabilité mobile.
- **Donnez à chaque cible de l'espace.** Si les cibles tactiles sont trop rapprochées, comme des liens empilés ou des boutons regroupés de manière serrée, il peut être facile de manquer ou de toucher le mauvais élément. Ajoutez de l'espacement ou du rembourrage entre les éléments pour éviter cela.
- **Ne vous fiez pas uniquement aux visuels.** Même les petites icônes peuvent être rendues plus utilisables avec un rembourrage supplémentaire, leur permettant de respecter les exigences de taille minimale sans modifier la mise en page.
- **Prévisualisez sur mobile.** Testez votre message sur différentes tailles d'écran et assurez-vous que les éléments interactifs sont faciles à utiliser.

Améliorer les cibles tactiles est l'un des moyens les plus efficaces de rendre votre message plus accessible sur mobile, et c'est une bonne expérience utilisateur pour tout le monde.

### Images {#images}

#### Fournissez du texte alt {#provide-alt-text}

Le texte alternatif (texte alt) est une courte description du contenu ou de la fonction d'une image que les lecteurs d'écran et autres technologies d'assistance fournissent aux utilisateurs. Pour chaque image significative, rédigez un texte alt descriptif afin que les utilisateurs qui ne peuvent pas voir les visuels comprennent quand même votre message ou votre appel à l'action.

#### Évitez les images contenant du texte {#avoid-images-of-text}

Dans la mesure du possible, évitez de placer du texte à l'intérieur des images : les lecteurs d'écran ne peuvent pas lire le texte intégré dans les images, et les utilisateurs ne peuvent pas facilement ajuster la taille ou la couleur de la police pour une meilleure visibilité. Considérez ces conseils :

- **Supprimez le texte lorsque c'est possible :** Déplacez tout texte descriptif ou promotionnel de l'image vers un champ de texte dans votre message. De cette façon, les utilisateurs peuvent le redimensionner ou le recolorer selon leurs besoins en utilisant les préférences de leur appareil ou navigateur.
- **Testez la lisibilité et le contraste :** Si vous devez conserver du texte dans l'image, suivez les bonnes pratiques de [contraste des couleurs](#color-contrast) et utilisez une [police de grande taille](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). Cela signifie que le texte doit être d'au moins 18 points (environ 24 pixels) pour le texte non gras ou 14 points (environ 18 pixels) s'il est en gras. L'utilisation de ces tailles aide le texte à rester lisible sans forcer les utilisateurs à zoomer, et améliore le contraste et la lisibilité globale du contenu. Testez pour confirmer qu'il est toujours lisible sur les petits écrans.
- **Fournissez du texte alt :** Pour le texte essentiel qui doit rester dans l'image, incluez un texte alt décrivant les mots.

Lorsque les images contiennent du texte qui ne peut pas être modifié, les utilisateurs malvoyants perdent la flexibilité de faire des ajustements de lecture. En séparant le texte des images, vous aidez davantage d'utilisateurs à lire et interagir confortablement avec votre message.

#### Conseils pour rédiger du texte alt {#tips-for-writing-alt-text}

- [Décrivez ce qui se trouve réellement dans l'image](#tip-1)
- [Restez bref, mais spécifique](#tip-2)
- [Évitez « image de » ou « photo de »](#tip-3)
- [Reflétez le texte qui apparaît dans l'image](#tip-4)
- [Restez dans le contexte pertinent, sans jargon marketing superflu](#tip-5)
- [Considérez l'objectif de l'image](#tip-6)

##### Décrivez ce qui se trouve réellement dans l'image {#tip-1}

Les utilisateurs de lecteurs d'écran s'appuient sur le texte alt pour comprendre le contenu ou la fonction d'une image. Évitez le « langage marketing » générique qui ne correspond pas à ce qui est visuellement montré.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemples <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Mauvais exemples <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>« Femme souriante portant une veste en jean bleu, tenant un sac de courses. »</td>
      <td>« C'est le moment de vous faire plaisir ! » (Aucune mention de ce qui se trouve réellement dans l'image)</td>
    </tr>
    <tr>
      <td>« Homme portant un T-shirt noir, appuyé sur un vélo dans une rue de la ville. »</td>
      <td>« Vivez votre meilleure vie maintenant ! » (Ignore le vélo et le décor urbain)</td>
    </tr>
    <tr>
      <td>« Immeuble d'appartements bleu avec un panneau "À louer" devant. »</td>
      <td>« La clé d'un avenir meilleur ! » (Ne reflète pas l'appartement ou le panneau)</td>
    </tr>
  </tbody>
</table>

##### Restez bref, mais spécifique {#tip-2}

Un texte alt concis facilite le traitement pour les utilisateurs. Incluez suffisamment de détails pour transmettre l'objectif, mais évitez le superflu. En règle générale, limitez le texte alt à 125 caractères ou moins. Si quelque chose de plus qu'une brève phrase ou une courte phrase est nécessaire, envisagez d'utiliser l'une des [méthodes de description longue](https://www.w3.org/WAI/tutorials/images/complex/) du W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemples <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Mauvais exemples <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>« Chaussures de course rouges sur fond blanc »</td>
      <td>« Des chaussures de course extrêmement confortables et parfaites pour votre mode de vie actif dans une teinte rouge vibrante. » (Trop long et rempli de contenu promotionnel superflu)</td>
    </tr>
    <tr>
      <td>« Quatre ordinateurs portables sur un présentoir »</td>
      <td>« Découvrez l'outil de productivité ultime qui redéfinit votre façon de travailler chaque jour, de toutes les manières imaginables. » (Ne décrit pas ce qui est réellement montré)</td>
    </tr>
    <tr>
      <td>« Groupe d'amis mangeant des glaces par une journée ensoleillée »</td>
      <td>« Capturez le bonheur pur avec la friandise la plus douce : la vie est meilleure avec notre marque de glaces ! » (Trop abstrait et centré sur la marque)</td>
    </tr>
  </tbody>
</table>

##### Évitez « image de » ou « photo de » {#tip-3}

Les lecteurs d'écran annoncent déjà qu'il s'agit d'une image. Passez directement à la description du sujet.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemples <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Mauvais exemples <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>« Table dressée pour un brunch avec des pancakes, des fruits et du café. »</td>
      <td>« Image d'une table dressée pour un brunch »</td>
    </tr>
    <tr>
      <td>« Panneau d'affichage en bord de route avec le texte en gras "Grande ouverture" »</td>
      <td>« Photo d'un panneau d'affichage en bord de route »</td>
    </tr>
    <tr>
      <td>« Paysage de montagne enneigé au coucher du soleil »</td>
      <td>« Photo de neige et de montagnes »</td>
    </tr>
  </tbody>
</table>

##### Reflétez le texte qui apparaît dans l'image {#tip-4}

Si une image contient du texte essentiel, intégrez cette information dans le texte alt afin que les utilisateurs ne la manquent pas.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemples <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Mauvais exemples <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>« Bannière indiquant "Soldes d'été — 50 % de réduction sur tous les maillots de bain." »</td>
      <td>« Bannière faisant la promotion d'une vente. » (Ne mentionne pas la réduction réelle)</td>
    </tr>
    <tr>
      <td>« Logo avec le texte "Café Toscana" en police cursive »</td>
      <td>« Image de logo pour un café. » (N'inclut pas le texte "Café Toscana")</td>
    </tr>
    <tr>
      <td>« Publicité annonçant "Billets de concert disponibles maintenant — Début le 5 juin" »</td>
      <td>« Publicité de concert. » (Aucun détail sur l'événement)</td>
    </tr>
  </tbody>
</table>

##### Restez dans le contexte pertinent, sans jargon marketing superflu {#tip-5}

Ne remplissez pas le texte alt avec des termes SEO ou des appels à l'action qui ne sont pas directement liés à l'image. Apportez de la valeur à ceux qui ne peuvent pas voir l'image.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemples <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Mauvais exemples <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>« Ordinateur portable affichant le graphique d'analyse du tableau de bord de Braze »</td>
      <td>« Boostez vos conversions et faites exploser votre ROI or retour sur investissement avec la meilleure plateforme au monde ! » (Ajoute un langage marketing inutile)</td>
    </tr>
    <tr>
      <td>« Ensemble de terrasse avec quatre chaises et une table en verre »</td>
      <td>« Organisez une fête d'été incroyable pour tous vos amis et votre famille maintenant ! » (Décrit un scénario, pas l'image)</td>
    </tr>
    <tr>
      <td>« Téléphone mobile affichant une application de prévisions météo avec 24 °C à l'écran »</td>
      <td>« Découvrez des innovations en temps réel dans le suivi météo qui changent la donne » (Ne reflète pas ce qui est visuellement montré)</td>
    </tr>
  </tbody>
</table>

##### Considérez l'objectif de l'image {#tip-6}

Si une image fonctionne comme un lien ou un appel à l'action, décrivez l'action prévue (« Acheter », « Lien vers », « S'inscrire »), pas seulement le libellé ou le produit affiché.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemples <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Mauvais exemples <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>« Acheter la collection automne »</td>
      <td>« Collection automne » (Action prévue manquante)</td>
    </tr>
    <tr>
      <td>« Lien vers l'eBook gratuit »</td>
      <td>« eBook gratuit » (Ne précise pas qu'il s'agit d'un lien)</td>
    </tr>
    <tr>
      <td>« S'inscrire à la liste de diffusion »</td>
      <td>« Liste de diffusion » (Ne décrit pas ce que l'utilisateur peut faire)</td>
    </tr>
  </tbody>
</table>

Si l'image n'a pas d'objectif, faites-le savoir également. Les images décoratives, comme les logos, doivent avoir une balise alt vide (`alt=""`) afin que les lecteurs d'écran sachent qu'ils doivent passer outre. Sans cela, c'est généralement le nom du fichier image qui est lu à la place.

#### Comment les clients de messagerie affichent le texte alt {#how-email-clients-display-alt-text}

L'affichage et le rendu du texte alt dans les e-mails sont contrôlés par le client de messagerie du destinataire (comme Gmail, Outlook ou Apple Mail), et non par Braze. Si vous remarquez des différences dans la façon dont le texte alt apparaît selon les clients de messagerie ou les plateformes — par exemple, le texte alt s'affichant différemment dans Gmail sur ordinateur par rapport à l'application mobile Gmail — cela est dû à la façon dont chaque client choisit de rendre le même HTML.

Bien que vous puissiez inclure un texte alt de n'importe quelle longueur dans votre HTML d'e-mail, certains clients de messagerie peuvent tronquer ou masquer le texte alt trop long pour tenir dans les dimensions de l'image. Si vous avez des questions sur le comportement du texte alt dans un client de messagerie spécifique, contactez le [support]({{site.baseurl}}/support_contact).

### Vidéos {#videos}

Les vidéos sont engageantes, mais si elles ne sont pas accessibles, vous risquez d'exclure une partie de votre audience. Utilisez les conseils suivants pour rendre votre contenu vidéo plus inclusif :

- [Fournissez des sous-titres](#closed-captions)
- [Fournissez des contrôles de lecture](#playback-controls)
- [Évitez la lecture automatique](#no-auto-play)
- [Évitez le contenu clignotant ou stroboscopique](#no-seizures)

#### Fournissez des sous-titres {#closed-captions}

Incluez des sous-titres avec vos vidéos afin que les utilisateurs puissent suivre les dialogues, les effets sonores et tout autre contenu audio. Les sous-titres aident :

- Les personnes sourdes ou malentendantes
- Les spectateurs qui regardent sans le son
- Les locuteurs non natifs qui préfèrent lire en même temps

Les sous-titres peuvent être activés ou désactivés, permettant aux utilisateurs de choisir ce qui leur convient le mieux.

{% alert note %}
Braze ne génère pas automatiquement de sous-titres pour vos vidéos. Il est de votre responsabilité d'ajouter des sous-titres précis à vos fichiers vidéo avant de les inclure dans votre message.
{% endalert %}


#### Fournissez des contrôles de lecture {#playback-controls}

Assurez-vous que votre vidéo intégrée inclut des contrôles de lecture accessibles — tels que lecture, pause, sourdine et avance — afin que les utilisateurs puissent interagir avec elle de la manière qui leur convient le mieux.

#### Évitez la lecture automatique {#no-auto-play}

Dans la mesure du possible, évitez de configurer les vidéos pour qu'elles se lancent automatiquement. La lecture automatique peut être déstabilisante ou désorientante pour :

- Les utilisateurs qui s'appuient sur des lecteurs d'écran ou la navigation au clavier
- Les personnes sensibles au mouvement
- Toute personne dans un environnement calme (comme un lieu de travail ou en soirée)

Laissez les utilisateurs choisir quand lancer une vidéo en incluant des contrôles clairs.

#### Évitez le contenu clignotant ou stroboscopique {#no-seizures}

N'incluez pas de vidéos avec des effets clignotants ou stroboscopiques, en particulier à haute fréquence. Ceux-ci peuvent déclencher des crises chez les utilisateurs atteints d'épilepsie photosensible et causer de l'inconfort chez d'autres personnes.

### Contraste des couleurs {#color-contrast}

Un contraste de couleur suffisant permet de s'assurer que vos messages sont faciles à lire pour tout le monde, y compris les personnes malvoyantes ou celles qui consultent votre contenu dans des conditions lumineuses ou difficiles. Visez des ratios de contraste conformes aux [exigences de niveau AA WCAG 2.2](https://www.w3.org/TR/WCAG/#contrast-minimum) :

- Ratio de contraste de 4,5:1 pour le texte normal (corps du texte, boutons et liens)
- Ratio de contraste de 3:1 pour le texte de grande taille (titres et libellés plus grands)

Vous pouvez tester vos choix de couleurs à l'aide de l'[outil de vérification du contraste WebAim](https://webaim.org/resources/contrastchecker/).

{% alert note %}
Les éditeurs de Braze vous permettent de sélectionner des combinaisons de couleurs personnalisées. Gardez à l'esprit que certains choix de couleurs peuvent nuire à l'accessibilité. Choisissez vos couleurs avec soin pour vous assurer que votre contenu est lisible et conforme aux normes d'accessibilité.
{% endalert %}


### HTML personnalisé {#custom-html}

Si vous utilisez du HTML personnalisé dans vos messages :

- Utilisez du [HTML sémantique](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Cela signifie utiliser les éléments HTML corrects pour leur objectif prévu au lieu de styliser un élément pour qu'il ressemble à un autre. La plupart des éléments HTML ont leur propre prise en charge de l'accessibilité intégrée.
- Pour la langue au niveau du document lorsque Braze peut ajouter des métadonnées HTML à l'exportation, consultez [Langue d'accessibilité](#accessibility-language) ; le comportement varie selon le canal. Lorsque vous balisez le contenu vous-même, définissez l'[attribut `lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) dans votre HTML pour identifier la langue de votre contenu. Les lecteurs d'écran utilisent différentes bibliothèques sonores pour chaque langue en fonction de la prononciation et des caractéristiques de cette langue. Si cela n'est pas spécifié, un lecteur d'écran suppose que le contenu est rédigé dans la langue par défaut que l'utilisateur a choisie lors de la configuration du lecteur d'écran. Si le message n'est pas réellement dans la langue par défaut, le lecteur d'écran risque de ne pas prononcer le message correctement.

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Lorsque vous utilisez l'éditeur d'e-mail par glisser-déposer, définissez la langue depuis l'onglet **Paramètres** lorsque ce contrôle est disponible. Les e-mails avec modèle complet et ceux utilisant uniquement des Content Blocks peuvent avoir des valeurs par défaut différentes pour la langue d'accessibilité — consultez [Langue d'accessibilité](#accessibility-language). Les autres canaux sont également couverts dans cette section.
{% endalert %}

- Utilisez les [attributs ARIA](#aria-attributes) pour fournir un contexte supplémentaire. Ces attributs fournissent des informations complémentaires aux technologies d'assistance, aidant à clarifier le rôle, l'état ou les propriétés des éléments d'interface qui pourraient autrement être peu clairs.

### Attributs ARIA {#aria-attributes}

Lorsque vous utilisez du code personnalisé dans les éditeurs Braze, vous pouvez utiliser les applications Internet riches et accessibles ([ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)) pour fournir une prise en charge supplémentaire de l'accessibilité aux utilisateurs qui s'appuient sur les technologies d'assistance. Les rôles et attributs ARIA aident les lecteurs d'écran à interpréter votre contenu plus clairement, en particulier lorsque vous utilisez des éléments qui ne transmettent pas de signification par eux-mêmes (comme `<div>` ou `<span>`).

{% alert important %}
Bien qu'ARIA soit conçu pour rendre le contenu web plus accessible, s'il est utilisé incorrectement, il peut faire plus de mal que de bien. ARIA ne remplace pas le HTML sémantique, il le complète — n'utilisez donc ARIA que lorsque les éléments HTML natifs ne répondent pas à vos besoins.
{% endalert %}

Voici quelques exemples particulièrement utiles dans les contextes de messagerie :

- [aria-label](#aria-label)
- [aria-labelledby](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="presentation"](#rolepresentation)
- [aria-en direct or en ligne/en production/instantané="polite"](#aria-livepolite)

#### aria-label {#aria-label}

`aria-label` ajoute un nom accessible aux éléments qui n'ont pas de texte visible. Si vous utilisez une icône sans texte (comme une corbeille ou un « X » pour fermer), une personne utilisant un lecteur d'écran ne saura pas ce qu'elle fait — à moins que vous ne l'étiquettiez. `aria-label` donne une voix à cette icône.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-labelledby {#aria-labelledby}

`aria-labelledby` connecte un élément à quelque chose qui a déjà un libellé visible. Donc, si vous avez une bannière ou une région qui devrait être lue à voix haute avec un titre, vous pouvez utiliser `aria-labelledby` pour indiquer à la technologie d'assistance : « Utilise ce titre là-bas pour nommer cette partie. »

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true" {#aria-hiddentrue}

`aria-hidden="true"` masque des éléments aux lecteurs d'écran. C'est utile pour le texte ou les visuels qui ne transmettent pas d'information importante — comme une étincelle, une coche ou un emoji utilisé uniquement à des fins de style.

Cela rend l'expérience plus propre pour les utilisateurs de lecteurs d'écran, qui pourraient autrement entendre du contenu redondant ou déroutant. C'est également utile pour masquer des éléments comme le contenu d'un accordéon hors écran qui n'a pas encore été déplié.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

En général, il est préférable d'utiliser `alt=""` pour les [images décoratives](#images) et les icônes plutôt que `aria-hidden="true"`. Bien que le HTML sémantique soit largement pris en charge par tous les lecteurs d'écran et logiciels d'assistance, la prise en charge d'ARIA varie. Même si vous utilisez `aria-hidden`, vous devriez quand même inclure un attribut alt vide.

#### role="presentation" {#rolepresentation}

`role="presentation"` indique aux technologies d'assistance d'ignorer les éléments utilisés uniquement pour la mise en page, comme les tableaux de design. Par exemple, les e-mails utilisent souvent des tableaux uniquement pour aligner les éléments. Sans ce rôle, les lecteurs d'écran pourraient supposer que votre mise en page est un tableau de données et commencer à lire les numéros de lignes et de colonnes.

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

Les e-mails créés dans l'éditeur d'e-mail par glisser-déposer ont les éléments de présentation automatiquement marqués avec l'attribut ARIA `role="presentation"`.

#### aria-en direct or en ligne/en production/instantané="polite" {#aria-livepolite}

`aria-live="polite"` annonce les mises à jour lorsque le contenu change sans nécessiter d'interaction de l'utilisateur. Utilisez-le lorsque vous affichez des mises à jour dynamiques dans un message, comme des succès, des erreurs ou d'autres notifications.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Tests d'accessibilité automatisés {#automated-accessibility-testing}

Pour vous aider à identifier et corriger les problèmes d'accessibilité le plus tôt possible, Braze propose des tests d'accessibilité automatisés dans les domaines suivants :

- [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#accessibility-testing) pour les e-mails
- [Scanner d'accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message#accessibility-scanner) pour les messages créés avec notre éditeur HTML (par exemple, les messages in-app HTML, les Content Blocks HTML, les [pieds de page d'e-mail personnalisés]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer), les [pages d'abonnement par e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-custom-opt-in-page) et les [pages de désabonnement par e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-custom-unsubscribe-page)).

Ces tests vérifient votre message par rapport aux directives d'accessibilité du contenu Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), un ensemble de normes techniques internationalement reconnues pour le contenu accessible. Tout problème pouvant être détecté automatiquement est signalé et classé par niveau de gravité pour vous aider à prioriser.

{% alert note %}
Inbox Vision fonctionne aussi bien pour les e-mails HTML que pour les e-mails par glisser-déposer. Le scanner ne s'exécute que sur le contenu créé avec l'éditeur HTML.
{% endalert %}

### Ce que les tests automatisés peuvent et ne peuvent pas détecter {#what-automated-testing-can-and-cant-catch}

Les tests d'accessibilité automatisés constituent un excellent point de départ, mais ils ne peuvent pas tout détecter. Certains problèmes nécessitent une évaluation humaine, en particulier lorsque le contexte ou le design visuel joue un rôle dans la façon dont les utilisateurs perçoivent votre e-mail.

Vous pouvez voir certains problèmes marqués comme **À examiner**. Il s'agit de cas où l'outil de vérification ne peut pas déterminer avec certitude si quelque chose pose un problème d'accessibilité. Dans ce cas, nous vous recommandons de les examiner manuellement.

Voici quelques exemples de ce que les outils automatisés ne peuvent pas détecter de manière fiable :

- Si l'ordre de focus des éléments interactifs suit une séquence logique
- Si le contenu est entièrement utilisable au clavier, sans nécessiter de souris
- Si le texte alt décrit de manière pertinente une image
- Si les titres sont utilisés correctement pour organiser le contenu
- Si les liens et les boutons sont clairement étiquetés et faciles à comprendre
- Si les cibles tactiles sont suffisamment grandes et correctement espacées
- Si le texte sur les images d'arrière-plan respecte les exigences de contraste de couleurs
- Si les instructions ou les étiquettes sont claires et utiles pour tous les utilisateurs

Ces limitations ne sont pas propres à Braze&#8212;elles sont communes à tous les outils d'accessibilité automatisés. Les vérifications automatisées ne peuvent pas simuler chaque technologie d'assistance, lecteur d'écran ou besoin utilisateur. C'est pourquoi l'accessibilité n'est pas une vérification ponctuelle&#8212;c'est une pratique continue.

Même si votre message passe toutes les vérifications automatisées, il reste important de :

- Examiner attentivement les problèmes signalés, en particulier ceux marqués comme **À examiner**.
- Tester manuellement dans la mesure du possible, notamment pour la mise en page et les interactions.
- Utiliser des outils tels que les lecteurs d'écran, la navigation au clavier uniquement et le zoom du navigateur pour simuler différents besoins d'accessibilité.

En combinant les tests automatisés avec une revue manuelle réfléchie, vous détecterez davantage de problèmes potentiels et créerez des Campaigns plus inclusives et utilisables pour chaque destinataire.