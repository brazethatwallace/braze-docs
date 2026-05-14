---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 7
description: "Cette page explique comment configurer Inbox Vision, une fonctionnalité qui permet aux marketeurs de visualiser leurs e-mails du point de vue de différents clients de messagerie et appareils mobiles."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision {#inbox-vision}

> Inbox Vision vous permet de visualiser vos e-mails depuis différents clients de messagerie et appareils mobiles. Par exemple, vous pouvez tester les différences entre le mode sombre et le mode clair afin de vérifier que vos e-mails s'affichent correctement.

{% alert important %}
Inbox Vision peut ne pas fonctionner si le contenu de votre e-mail repose sur des informations provenant de modèles, telles que les données du profil utilisateur. Braze crée un modèle d'utilisateur vide lors de l'envoi d'e-mails pour cette fonctionnalité.<br><br>Ajoutez des valeurs par défaut à tout élément Liquid dans votre e-mail. Sans valeurs par défaut, vous pourriez obtenir un faux positif ou le test pourrait échouer.
{% endalert %}

## Considérations {#considerations}

En règle générale, votre e-mail ne fonctionnera pas avec Inbox Vision si son contenu repose sur des informations provenant de modèles, telles que les informations du profil utilisateur. En effet, Braze crée un modèle d'utilisateur vide lorsque nous envoyons des e-mails à l'aide de cette fonctionnalité.

Vous pouvez résoudre ce problème en ajoutant des valeurs par défaut ou n'importe quelle autre valeur aux éléments Liquid de votre e-mail avant d'exécuter Inbox Vision. Une fois les tests terminés dans Inbox Vision, le message e-mail d'origine réapparaît. Si aucune valeur n'est fournie, le test peut échouer à générer les prévisualisations correctement.

Votre entreprise dispose d'une limite sur le nombre d'e-mails que vous pouvez prévisualiser avec Inbox Vision. Vous pouvez suivre cette limite dans l'onglet **Email Previews** d'Inbox Vision.

Incluez une ligne d'objet et un domaine d'envoi valide pour afficher les prévisualisations. Soyez attentif aux différences de rendu entre ordinateur de bureau et appareil mobile. Utilisez les prévisualisations pour confirmer que l'e-mail s'affiche comme prévu.

{% alert note %}
Si la prévisualisation d'une Campaign affiche une erreur de permission, videz votre cache et vos cookies, ou essayez une fenêtre de navigation privée. Les extensions de navigateur bloquent parfois la prévisualisation.
{% endalert %}

Pour tester votre e-mail dans Inbox Vision :

1. Accédez à votre éditeur par glisser-déposer ou à votre éditeur d'e-mail HTML.
2. Dans votre éditeur, sélectionnez **Preview & Test**.
3. Sélectionnez **Inbox Vision**.
4. Sélectionnez **Run Inbox Vision**. Cette opération peut prendre jusqu'à dix minutes.
5. Ensuite, sélectionnez une vignette pour afficher la prévisualisation en détail. Ces prévisualisations sont regroupées dans les sections suivantes : **Web Clients**, **Application Clients** et **Mobile Clients**.

![L'option pour sélectionner les clients de messagerie à prévisualiser.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5. Sélectionnez **Run Inbox Vision**. Cette opération peut prendre entre deux et dix minutes.

{% alert note %}
Inbox Vision ne prend pas en charge les e-mails qui incluent une [logique d'abandon]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/) car ces e-mails sont rendus sous forme de contenu statique.
{% endalert %}

### Prévisualiser en tant qu'utilisateur {#previewing-as-a-user}

Lorsque vous prévisualisez en tant qu'utilisateur aléatoire, Inbox Vision ne sauvegarde pas les paramètres ou attributs spécifiques à l'utilisateur (tels que le nom ou les préférences). Lorsque vous sélectionnez un utilisateur personnalisé, la prévisualisation Inbox Vision peut différer des autres prévisualisations car elle utilise les données spécifiques de cet utilisateur.

## Analyse du code {#code-analysis}

L'analyse du code met en évidence les problèmes HTML potentiels, affiche le nombre d'occurrences et indique les éléments HTML non pris en charge.

### Consulter les informations d'analyse du code {#viewing-code-analysis-information}

Retrouvez ces informations dans l'onglet **Inbox Vision** en sélectionnant <i class="fas fa-list" aria-label="Vue en liste"></i> **List view**. La vue en liste est disponible uniquement pour les modèles d'e-mail HTML. Pour les modèles par glisser-déposer, utilisez plutôt les prévisualisations pour résoudre les problèmes.

![Exemple d'analyse du code dans la prévisualisation Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
L'analyse du code peut apparaître plus rapidement que la prévisualisation pour un client donné, car Braze attend que l'e-mail arrive avant de prendre la capture d'écran.
{% endalert %}

## Tests de courrier indésirable {#spam-testing}

Les tests de courrier indésirable estiment si un e-mail risque d'être filtré comme spam. Les tests sont exécutés à travers des filtres tels qu'IronPort, SpamAssassin et Barracuda, ainsi que des filtres ISP tels que Gmail et Outlook, en utilisant des boîtes de réception initiatrices statiques qui n'ouvrent ni ne cliquent par défaut.

{% alert important %}
Le placement en boîte de réception dépend principalement de l'engagement des destinataires en temps réel. Les résultats des tests de courrier indésirable peuvent ne pas correspondre à ce que vous observez avec de vraies campagnes.
{% endalert %}

Pour une lecture plus claire de la livrabilité, testez le contenu avec de petites cohortes en conditions réelles : des taux d'ouverture et de clics élevés constituent le signal le plus fiable. Utilisez les tests de courrier indésirable comme un indicateur parmi d'autres, en complément du suivi de l'engagement.

### Consulter les résultats des tests de courrier indésirable {#viewing-spam-test-results}

Pour vérifier les résultats de vos tests de courrier indésirable :

1. Sélectionnez l'onglet **Spam Testing** dans la section **Inbox Vision**. Le tableau **Spam Test Result** affiche le nom du filtre anti-spam, l'état et le type.
2. Examinez ces résultats et apportez les ajustements nécessaires à votre campagne e-mail.
3. Sélectionnez **Re-run Test** pour relancer vos tests de courrier indésirable.

## Tests d'accessibilité {#accessibility-testing}

Les tests d'accessibilité mettent en évidence les problèmes d'accessibilité potentiels dans votre e-mail et indiquent quels éléments ne respectent pas les normes. Braze analyse le contenu selon certaines directives pour l'accessibilité des contenus web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), un ensemble de normes internationalement reconnues développées par le W3C pour rendre le contenu web plus accessible.

### Fonctionnement {#how-it-works}

Lorsque vous exécutez Inbox Vision, Braze vérifie automatiquement les problèmes d'accessibilité courants dans le [jeu de règles WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (tels que le texte alternatif manquant, un contraste de couleurs insuffisant, une structure de titres incorrecte) et catégorise la gravité pour vous aider à prioriser les corrections.

{% alert important %}
Les tests d'accessibilité peuvent être utilisés pour soutenir les efforts de conformité du client vis-à-vis de réglementations ou de lois telles que l'[Acte européen sur l'accessibilité](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers) ; toutefois, le client reconnaît que Braze ne fait aucune déclaration ni garantie quant à la conformité du client résultant de l'utilisation des tests d'accessibilité, et décline toute responsabilité à cet égard.
{% endalert %}

### Consulter les résultats des tests d'accessibilité {#viewing-accessibility-testing-results}

Les tests d'accessibilité génèrent des résultats pour chaque règle sous forme de réussi, échoué ou à vérifier dans l'onglet **Accessibility Testing**. Braze catégorise chaque règle selon POUR (Perceptible, Opérable, Compréhensible, Robuste), les quatre principes fondamentaux des WCAG.

#### Catégories POUR {#pour-categories}

Inbox Vision catégorise les problèmes selon les quatre [principes fondamentaux POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) : Perceptible, Opérable, Compréhensible et Robuste.

| Principe | Définition |
| --- | --- |
| Perceptible | Les informations et les composants de l'interface utilisateur doivent être présentés aux utilisateurs de manière à ce qu'ils puissent les percevoir.<br><br>Les utilisateurs doivent pouvoir percevoir les informations présentées (elles ne peuvent pas être invisibles pour tous leurs sens). |
| Opérable | Les composants de l'interface utilisateur et la navigation doivent être opérables.<br><br>Les utilisateurs doivent pouvoir utiliser l'interface (l'interface ne peut pas exiger une interaction qu'un utilisateur ne peut pas effectuer). |
| Compréhensible | Les informations et le fonctionnement de l'interface utilisateur doivent être compréhensibles.<br><br>Les utilisateurs doivent pouvoir comprendre les informations ainsi que le fonctionnement de l'interface utilisateur (le contenu ou le fonctionnement ne peut pas dépasser leur compréhension). |
| Robuste | Le contenu doit être suffisamment robuste pour être interprété de manière fiable par une grande variété d'agents utilisateurs, y compris les technologies d'assistance.<br><br>Les utilisateurs doivent pouvoir accéder au contenu à mesure que les technologies évoluent (à mesure que les technologies et les agents utilisateurs évoluent, le contenu doit rester accessible). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catégories POUR" }

#### Niveaux de gravité {#severity-levels}

Inbox Vision classe les problèmes d'accessibilité par gravité pour vous aider à prioriser les corrections.

| État | Définition |
| --- | --- |
| Critique | Problèmes pouvant bloquer l'accès au contenu ou aux fonctionnalités pour les utilisateurs en situation de handicap. Ce sont les plus graves et doivent être corrigés en priorité. |
| Grave | Problèmes pouvant créer des obstacles significatifs sans pour autant bloquer complètement l'accès. Ils doivent être traités rapidement. |
| Modéré | Problèmes pouvant causer certaines difficultés pour les utilisateurs en situation de handicap, mais moins susceptibles de bloquer complètement l'accès. |
| Mineur | Problèmes ayant un impact relativement faible sur l'accessibilité et pouvant ne causer qu'un inconvénient mineur. |
| À vérifier | Impossible de détecter s'il y a un problème ou non. Cela peut se produire lorsque le ratio de contraste ne peut pas être déterminé car le texte est placé sur une image d'arrière-plan. Une vérification manuelle est nécessaire car la détection automatique n'est pas possible. |
| Réussi | Conforme aux normes WCAG A, AA ou aux bonnes pratiques d'accessibilité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveaux de gravité" }

{% alert important %}
L'éditeur par glisser-déposer ne prend pas en charge la définition d'un élément `<title>` de document, ce qui fait que le scanner d'accessibilité échoue systématiquement à cette vérification.<br><br>Cette limitation est suivie pour de futures améliorations. Si cela affecte vos flux de travail ou vos utilisateurs, [partagez vos commentaires]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard/#sharing-feedback) afin que nous puissions prioriser les corrections les plus impactantes.
{% endalert %}

### Comprendre les tests d'accessibilité automatisés {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

## Bonnes pratiques {#best-practices}

### Examiner votre liste d'utilisateurs abonnés aux e-mails {#review-your-email-subscriber-list}

Consultez le [tableau de bord d'informations sur les e-mails]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance/#email-insights-dashboard) pour déterminer le type d'appareil et les fournisseurs les plus populaires auprès de vos utilisateurs abonnés. Si vous avez besoin de plus de granularité (navigateur, modèle d'appareil, etc.), vous pouvez exploiter vos données [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) ou le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) pour obtenir ce niveau de détail sur l'engagement e-mail récent de vos utilisateurs.

Par défaut, Braze propose les 20 prévisualisations les plus courantes basées sur les données générales du secteur et d'experts, ce qui couvre la majorité des environnements où vos utilisateurs abonnés consultent vos e-mails. Si votre analyse de données indique d'autres prévisualisations plus populaires, vous pouvez définir un ensemble de prévisualisations par défaut à chaque exécution d'Inbox Vision.

### Sélectionner des prévisualisations pertinentes et impactées {#select-meaningful-previews-and-impacted-previews}

Si votre activité est principalement basée aux États-Unis, certaines prévisualisations internationales comme GMX.de ne sont utilisées que par un nombre marginal d'utilisateurs. Nous vous recommandons de prioriser et d'optimiser pour les boîtes de réception ayant un impact significatif sur vos utilisateurs abonnés, et de réserver vos prévisualisations pour les boîtes de réception à fort impact.

Lorsque vous effectuez des corrections affectant des prévisualisations spécifiques, veillez à sélectionner uniquement les prévisualisations impactées pour éviter de consommer des prévisualisations inutilisées.

### Exécuter Inbox Vision sur la version finale de l'e-mail {#run-inbox-vision-on-the-final-email-version}

Nous vous recommandons d'exécuter Inbox Vision lorsque l'e-mail est prêt pour la production ou proche de l'être. Cela vous permet de réduire le nombre de prévisualisations générées, car l'e-mail passe par plusieurs itérations avant d'être finalisé et prêt à être envoyé aux utilisateurs.

Exécuter Inbox Vision à chaque modification peut rapidement consommer vos prévisualisations. Nous vous recommandons d'apporter d'abord toutes les modifications nécessaires à l'e-mail, puis d'exécuter Inbox Vision pour prévisualiser l'impact de l'ensemble de vos changements sur le rendu de votre e-mail dans les différents environnements.

Braze exécute les tests via de véritables clients de messagerie et s'efforce de garantir l'exactitude des rendus. Si vous constatez un problème récurrent avec un client, ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).

### Précision des tests par rapport aux boîtes de réception réelles {#test-accuracy-versus-live-inboxes}

Un message envoyé peut avoir un aspect différent de la prévisualisation dans l'éditeur, car les fournisseurs interprètent le même HTML différemment. Téléchargez une copie du HTML envoyé pour comparer, et utilisez l'insertion CSS lorsque les clients suppriment les blocs `<style>`.