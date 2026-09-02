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

> Inbox Vision vous permet de visualiser vos e-mails du point de vue de différents clients de messagerie et appareils mobiles. Par exemple, vous pouvez tester les différences entre le mode sombre et le mode clair afin de vérifier que vos e-mails s'affichent correctement.

{% alert important %}
Inbox Vision peut ne pas fonctionner si le contenu de votre e-mail repose sur des informations de modèles, telles que les données du profil utilisateur. Braze utilise un utilisateur vide comme modèle lors de l'envoi d'e-mails pour cette fonctionnalité.<br><br>Ajoutez des valeurs par défaut à tout élément Liquid dans votre e-mail. Sans valeurs par défaut, vous pourriez obtenir un faux positif ou le test pourrait échouer.
{% endalert %}

## Considérations {#considerations}

En général, votre e-mail ne fonctionnera pas avec Inbox Vision si le contenu de votre e-mail repose sur des informations de modèle, telles que les informations du profil utilisateur. En effet, Braze utilise un utilisateur vide comme modèle lorsque nous envoyons des e-mails via cette fonctionnalité.

Vous pouvez résoudre ce problème en ajoutant des valeurs par défaut ou toute autre valeur au Liquid dans votre e-mail avant d'exécuter Inbox Vision. Lorsque vous avez terminé vos tests dans Inbox Vision, le message e-mail original réapparaît. Si aucune valeur n'est fournie, le test peut échouer à afficher correctement les aperçus.

Votre entreprise dispose d'une limite sur le nombre d'e-mails que vous pouvez prévisualiser avec Inbox Vision. Vous pouvez suivre cela dans l'onglet **Email Previews** d'Inbox Vision.

Incluez une ligne d'objet et un domaine d'envoi valide pour afficher les aperçus. Soyez attentif aux différences de rendu entre bureau et mobile. Utilisez les aperçus pour confirmer que l'e-mail s'affiche comme prévu.

{% alert note %}
Si la prévisualisation d'une Campaign affiche une erreur de permission, videz votre cache et vos cookies, ou essayez une fenêtre de navigation privée. Les extensions de navigateur bloquent parfois l'aperçu.
{% endalert %}

Pour tester votre e-mail dans Inbox Vision :

1. Accédez à votre éditeur par glisser-déposer ou à votre éditeur d'e-mail HTML.
2. Dans votre éditeur, sélectionnez **Preview & Test**.
3. Sélectionnez **Inbox Vision**.
4. Sélectionnez **Run Inbox Vision**. Cela prend jusqu'à dix minutes.
5. Ensuite, sélectionnez une vignette pour afficher l'aperçu plus en détail. Ces aperçus sont regroupés dans les sections suivantes : **Web Clients**, **Application Clients** et **Mobile Clients**.

![Option pour sélectionner les clients de messagerie à prévisualiser.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5. Sélectionnez **Run Inbox Vision**. Cela peut prendre entre deux et dix minutes.

{% alert note %}
Inbox Vision ne prend pas en charge les e-mails qui incluent une [logique d'abandon]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) car ces e-mails sont rendus sous forme de contenu statique.
{% endalert %}

### Prévisualiser en tant qu'utilisateur {#previewing-as-a-user}

Lorsque vous prévisualisez en tant qu'utilisateur aléatoire, Inbox Vision n'enregistre pas les paramètres ou attributs spécifiques à l'utilisateur (tels que le nom ou les préférences). Lorsque vous sélectionnez un utilisateur personnalisé, l'aperçu Inbox Vision peut différer des autres aperçus car il utilise des données utilisateur spécifiques.

## Analyse du code {#code-analysis}

L'analyse du code met en évidence les problèmes HTML potentiels, indique le nombre d'occurrences et signale les éléments HTML non pris en charge.

### Afficher les informations d'analyse du code {#viewing-code-analysis-information}

Retrouvez ces informations dans l'onglet **Inbox Vision** en sélectionnant <i class="fas fa-list"></i> **List view**. La vue en liste est disponible uniquement pour les modèles d'e-mail HTML. Pour les modèles par glisser-déposer, utilisez plutôt les aperçus pour résoudre les problèmes.

![Exemple d'analyse du code dans l'aperçu Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
L'analyse du code peut s'afficher plus rapidement que l'aperçu pour un client donné, car Braze attend que l'e-mail soit arrivé avant de prendre la capture d'écran.
{% endalert %}

## Tests de courrier indésirable {#spam-testing}

Les tests de courrier indésirable estiment si un e-mail risque d'être filtré comme spam. Les tests s'exécutent sur différents filtres tels qu'IronPort, SpamAssassin et Barracuda, ainsi que sur des filtres de fournisseurs de services Internet tels que Gmail et Outlook, en utilisant des boîtes de réception statiques d'initiateurs qui n'ouvrent ni ne cliquent par défaut.

{% alert important %}
Le placement en boîte de réception dépend principalement de l'engagement des destinataires en direct or en ligne/en production/instantané. Les résultats des tests de courrier indésirable peuvent ne pas correspondre à ce que vous observez avec de véritables Campaigns.
{% endalert %}

Pour une vision plus claire de la livrabilité, testez votre contenu avec de petites cohortes en direct or en ligne/en production/instantané : des taux élevés d'ouvertures et de clics constituent le signal le plus fiable. Utilisez les tests de courrier indésirable comme un indicateur parmi d'autres, en complément du suivi de l'engagement.

### Consultation des résultats des tests de courrier indésirable {#viewing-spam-test-results}

Pour consulter les résultats de vos tests de courrier indésirable :

1. Sélectionnez l'onglet **Spam Testing** dans la section **Inbox Vision**. Le tableau **Spam Test Result** affiche le nom du filtre anti-spam, le statut et le type.
2. Examinez ces résultats et apportez les ajustements nécessaires à votre campagne e-mail.
3. Sélectionnez **Re-run Test** pour recharger les résultats de vos tests de courrier indésirable.

## Tests d'accessibilité {#accessibility-testing}

Les tests d'accessibilité mettent en évidence les problèmes d'accessibilité potentiels dans votre e-mail et indiquent quels éléments ne respectent pas les normes. Braze analyse le contenu en fonction de certaines règles des Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), un ensemble de normes internationalement reconnues développées par le W3C pour rendre le contenu web plus accessible.

### Comment ça fonctionne {#how-it-works}

Lorsque vous lancez Inbox Vision, Braze vérifie automatiquement les problèmes d'accessibilité courants dans le [jeu de règles WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (comme le texte alternatif manquant, un contraste de couleurs insuffisant, une structure de titres inadéquate) et catégorise la gravité pour vous aider à prioriser les corrections. Notez que même lorsque le texte alternatif est présent, [la manière dont il s'affiche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) est contrôlée par le client de messagerie du destinataire, et non par Braze.

{% alert important %}
Les tests d'accessibilité peuvent être utilisés pour soutenir les efforts de conformité du client aux réglementations ou lois telles que le [European Accessibility Act](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers) ; cependant, le client reconnaît que Braze ne fait aucune déclaration ni garantie quant à savoir si l'utilisation des tests d'accessibilité satisfait ou non les obligations de conformité du client, et décline toute responsabilité à cet égard.
{% endalert %}

### Consulter les résultats des tests d'accessibilité {#viewing-accessibility-testing-results}

Les tests d'accessibilité génèrent des résultats pour chaque règle sous forme de réussite, d'échec ou de révision nécessaire dans l'onglet **Accessibility Testing**. Braze catégorise chaque règle en utilisant POUR (Perceptible, Opérable, Compréhensible, Robuste), les quatre principes fondamentaux des WCAG.

#### Catégories POUR {#pour-categories}

Inbox Vision catégorise les problèmes selon les quatre [principes fondamentaux POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) : Perceptible, Opérable, Compréhensible et Robuste.

| Principe | Définition |
| --- | --- |
| Perceptible | Les informations et les composants de l'interface utilisateur doivent être présentés aux utilisateurs de manière à ce qu'ils puissent les percevoir.<br><br>Les utilisateurs doivent pouvoir percevoir les informations présentées (elles ne peuvent pas être invisibles pour tous leurs sens). |
| Opérable | Les composants de l'interface utilisateur et la navigation doivent être opérables.<br><br>Les utilisateurs doivent pouvoir utiliser l'interface (l'interface ne peut pas exiger une interaction qu'un utilisateur ne peut pas effectuer). |
| Compréhensible | Les informations et le fonctionnement de l'interface utilisateur doivent être compréhensibles.<br><br>Les utilisateurs doivent pouvoir comprendre les informations ainsi que le fonctionnement de l'interface utilisateur (le contenu ou le fonctionnement ne peut pas dépasser leur compréhension). |
| Robuste | Le contenu doit être suffisamment robuste pour pouvoir être interprété de manière fiable par une grande variété d'agents utilisateurs, y compris les technologies d'assistance.<br><br>Les utilisateurs doivent pouvoir accéder au contenu à mesure que les technologies évoluent (à mesure que les technologies et les agents utilisateurs progressent, le contenu doit rester accessible). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catégories POUR" }

#### Niveaux de gravité {#severity-levels}

Inbox Vision classe les problèmes d'accessibilité par gravité pour vous aider à prioriser les corrections.

| Statut | Définition |
| --- | --- |
| Critique | Problèmes pouvant bloquer l'accès au contenu ou aux fonctionnalités pour les utilisateurs en situation de handicap. Ce sont les plus graves et doivent être corrigés en priorité. |
| Grave | Problèmes pouvant créer des obstacles importants sans pour autant bloquer complètement l'accès. Ils doivent être traités rapidement. |
| Modéré | Problèmes pouvant causer certaines difficultés pour les utilisateurs en situation de handicap, mais qui sont moins susceptibles de bloquer totalement l'accès. |
| Mineur | Problèmes ayant un impact relativement faible sur l'accessibilité et pouvant ne causer qu'un inconvénient mineur. |
| Révision nécessaire | Impossible de détecter s'il y a un problème ou non. Cela peut se produire lorsqu'il est impossible de déterminer le ratio de contraste parce que le texte est placé sur une image d'arrière-plan. Vous devez vérifier manuellement car cela ne peut pas être déterminé automatiquement. |
| Réussi | Conforme aux règles WCAG A, AA ou aux bonnes pratiques d'accessibilité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveaux de gravité" }

{% alert important %}
L'éditeur par glisser-déposer ne prend pas en charge la définition d'un élément `<title>` du document, de sorte que le scanner d'accessibilité échoue systématiquement à cette vérification.<br><br>Cette limitation est suivie pour de futures améliorations. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="the drag-and-drop editor document title limitation in Inbox Vision" %}
{% endalert %}

### Comprendre les tests d'accessibilité automatisés {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

## Bonnes pratiques {#best-practices}

### Vérifiez votre liste d'abonnés e-mail {#review-your-email-subscriber-list}

Consultez le [tableau de bord des informations e-mail]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-insights-dashboard) pour déterminer les types d'appareils et les fournisseurs les plus populaires auprès de vos abonnés.

Si vous avez besoin de plus de granularité, comme le navigateur, le modèle d'appareil, et plus encore, vous pouvez tirer parti de vos données [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou du [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder) pour obtenir ce niveau de détail sur l'engagement e-mail récent de vos utilisateurs.

### Sélectionnez des aperçus pertinents et ciblés {#select-meaningful-previews-and-impacted-previews}

Si votre entreprise est principalement basée aux États-Unis, certains aperçus, comme les aperçus internationaux tels que GMX.de, peuvent n'être utilisés que par un nombre négligeable d'utilisateurs. Nous vous recommandons de prioriser et d'optimiser pour les boîtes de réception avec un impact significatif sur vos abonnés, et de réserver vos aperçus pour les boîtes de réception à fort impact.

Lorsque vous effectuez des corrections affectant des aperçus spécifiques, veillez à sélectionner uniquement les aperçus concernés pour éviter de consommer des aperçus inutilisés.

### Exécutez Inbox Vision sur la version finale de l'e-mail {#run-inbox-vision-on-the-final-email-version}

Nous vous suggérons d'exécuter Inbox Vision lorsque le message e-mail est prêt pour la production ou proche de l'être. Cela vous permet de réduire le nombre d'aperçus générés, car l'e-mail passe par plusieurs itérations avant d'être finalisé et prêt à être envoyé aux utilisateurs.

Exécuter Inbox Vision à chaque modification ou changement individuel peut rapidement consommer vos aperçus. Nous vous suggérons d'apporter d'abord toutes les modifications nécessaires à l'e-mail, puis d'exécuter Inbox Vision pour prévisualiser l'impact de l'ensemble de vos changements sur le rendu de votre e-mail dans les différents environnements.

Braze exécute les tests via de véritables clients de messagerie et s'efforce de garantir l'exactitude des rendus. Braze utilise par défaut les 20 principaux aperçus basés sur les données du secteur et les recommandations d'experts, ce qui couvre la majorité des environnements dans lesquels vos utilisateurs consultent vos e-mails. Si votre analyse de données indique d'autres aperçus plus populaires, vous pouvez définir un ensemble d'aperçus par défaut à chaque exécution d'Inbox Vision.

Si vous constatez régulièrement un problème avec un client, ouvrez un [ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Exactitude des tests par rapport aux boîtes de réception réelles {#test-accuracy-versus-live-inboxes}

Un message envoyé peut avoir un aspect différent de l'aperçu dans l'éditeur, car les fournisseurs interprètent le même HTML de manière différente. Téléchargez une copie du HTML envoyé pour comparer, et utilisez l'insertion CSS lorsque les clients suppriment les blocs `<style>`.

#### Corps d'e-mail vides {#blank-email-bodies}

Si les destinataires signalent des corps d'e-mail vides tout en pouvant voir le nom de l'expéditeur ou la ligne d'objet :

1. Confirmez quels clients de messagerie sont concernés.
2. Utilisez Inbox Vision pour tester la variante dans ces clients et identifier les problèmes de compatibilité HTML ou CSS.
3. Si un client supprime les blocs `<style>`, ajoutez des attributs `style` aux éléments HTML concernés. Pour en savoir plus sur le comportement de l'insertion et ses limitations, consultez [Insertion CSS]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline). Dans Gmail, un excès de CSS peut entraîner la suppression de l'intégralité du bloc `<style>`, ce qui est une cause fréquente de corps d'e-mail vides.
4. Dans l'éditeur HTML, vous pouvez également activer **Activer l'insertion CSS** sous **Informations d'envoi** > **Avancé** pour insérer les règles de feuille de style pour l'ensemble du message. Cette option n'est pas disponible pour les e-mails par glisser-déposer, qui sont déjà traités par l'éditeur.
5. Retestez dans Inbox Vision avant d'envoyer de futures Campaigns.