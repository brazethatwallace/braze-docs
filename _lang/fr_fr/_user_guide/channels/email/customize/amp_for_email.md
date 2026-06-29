---
nav_title: "AMP pour l'e-mail"
article_title: "AMP pour l'e-mail"
alias: /amphtml/
page_order: 11
description: "Cet article de référence fournit un aperçu d'AMP pour l'e-mail et des cas d'utilisation courants."
channel:
  - email

---

# AMP pour l'e-mail {#amp-for-email}

> Avec [AMP pour l'e-mail](https://amp.dev/about/email), vous pouvez ajouter des éléments interactifs à vos e-mails et enrichir vos communications avec vos clients, en offrant une expérience complète directement dans la boîte de réception de vos utilisateurs. AMP rend cela possible grâce à l'utilisation de divers composants qui permettent de créer des offres e-mail attrayantes telles que des sondages, des questionnaires de satisfaction, des campagnes de vote, des avis, des centres d'abonnement, et bien plus encore. Ces outils offrent des opportunités d'augmenter l'engagement et la rétention.

## Conditions requises {#requirements}

Braze n'est pas responsable de l'inscription des utilisateurs auprès de Google ni du respect des exigences de sécurité nécessaires. AMP pour l'e-mail est disponible uniquement pour SparkPost et SendGrid.

| Condition   | Description |
| --------------| ----------- |
| AMP pour l'e-mail activé | AMP est disponible pour tous les utilisateurs. |
| Activation du compte Gmail | Voir [Activation du compte Gmail](#enabling-gmail-account). |
| Authentification de l'expéditeur Google | Gmail [authentifie l'expéditeur](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) des e-mails AMP avec DKIM, SPF et DMARC. Ceux-ci doivent être configurés pour votre compte. <br><br>- [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Domain-based Message Authentication, Reporting, and Conformance](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| Éléments d'e-mail AMP | Un e-mail AMP convaincant inclut l'utilisation stratégique de divers composants. Consultez l'onglet Essentiels dans la section [Composants](#components) ci-dessous. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions requises" }

### Clients de messagerie pris en charge {#supported-email-clients}

Avant de pouvoir envoyer des e-mails AMP à vos utilisateurs, vous devez vous inscrire auprès de nos clients de messagerie. Le processus d'inscription consiste à envoyer un e-mail de test en AMP HTML pour obtenir une approbation. Les délais d'approbation varient d'un client à l'autre. Suivez les liens d'inscription pour plus d'informations.

| Client | Lien d'inscription |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clients de messagerie pris en charge" }

Pour une liste complète des clients de messagerie pris en charge, consultez la [documentation AMP](https://amp.dev/support/faq/email-support).

### Activation du compte Gmail {#enabling-gmail-account}

Accédez aux paramètres de votre compte Gmail, puis sélectionnez **Enable dynamic email** dans l'onglet **General**.

![Un exemple de paramètres Gmail avec la case « Enable dynamic email » cochée.]({% image_buster /assets/img/dynamic-content.png %})

## Utilisation de l'API {#api-usage}

Vous pouvez également utiliser AMP pour l'e-mail avec notre API. Si vous utilisez l'un des [endpoints d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging) de Braze pour envoyer un e-mail, ajoutez `amp_body` comme spécification d'objet comme indiqué ci-dessous.

### Spécification de l'objet e-mail {#email-object-specification}

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <user@example.com>"),
  "reply_to": (optional, valid email address in the format "user@example.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Créer votre e-mail AMP {#create-your-amp-email}

Commencez par créer votre e-mail AMP en utilisant les [composants](#components). Ensuite, utilisez l'[API Braze](#api-usage) pour envoyer votre message, en veillant à inclure `amp_body` pour votre AMP HTML.

En plus du AMP HTML, nous exigeons une version HTML standard `body` et recommandons une version `plaintext_body` de votre e-mail AMP. Tous les e-mails AMP sont envoyés en multipart, ce qui signifie que Braze envoie un e-mail prenant en charge le HTML, le texte brut et le AMP HTML. Cela s'avère utile dans le cas où votre e-mail est envoyé via un fournisseur qui ne prend pas encore en charge AMP pour l'e-mail, car l'e-mail utilisera automatiquement la version appropriée en fonction de l'utilisateur et de son appareil.

{% alert note %}
Lorsque vous créez un e-mail AMP, vérifiez que vous êtes dans l'éditeur AMP, car le code AMP ne doit pas être ajouté dans l'éditeur HTML.
{% endalert %}

Consultez ces ressources supplémentaires :

- [Tutoriel AMP](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Exemple de code](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) pour voir à quoi devrait ressembler le produit final.
- [Bibliothèque de composants e-mail AMP](https://amp.dev/documentation/components/?format=email/)

### Composants {#components}

Lors de la création des éléments AMP, nous vous recommandons de consulter votre équipe d'ingénierie et d'inclure des ressources de conception pour un niveau de finition supplémentaire.

{% tabs %}
  {% tab Essentiels %}

Chacun de ces éléments est requis dans le corps de votre e-mail AMP.

| Composant | Description | Exemple |
|---------|--------------|---------|
| Identification <br><br> `⚡4email` ou `amp4email`| Identifie votre e-mail comme un e-mail AMP HTML. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Chargement du runtime AMP <br><br> `<script>` | Permet à AMP de s'exécuter dans votre e-mail en utilisant JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| Modèle CSS | Masque le contenu jusqu'au chargement d'AMP. <br> Les fournisseurs de messagerie qui prennent en charge les e-mails AMP appliquent des contrôles de sécurité qui n'autorisent que les scripts AMP vérifiés à s'exécuter dans leurs clients. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Composants" }

  {% endtab %}
  {% tab Dynamique %}

Utilisez ces composants pour créer des mises en page et des comportements dynamiques dans vos e-mails.

| Composant | Description | Script requis |
|---------|--------------|---------|
| [Accordéon](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Permet aux utilisateurs de visualiser le plan du contenu et d'accéder directement à n'importe quelle section. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formulaires](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Créez des formulaires pour soumettre des champs de saisie dans un document AMP. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Composants" }

{% alert note %}
Tout composant nécessitant l'authentification de l'utilisateur doit utiliser des [jetons d'accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou des [jetons d'assertion proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Créatif %}

  Donnez du style à vos e-mails avec les composants AMP qui peuvent vous aider à adapter votre e-mail à votre audience.

| Composant | Description | Script requis |
|---------|--------------|---------|
| [Image animée](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Affiche une image animée (généralement un GIF) gérée via le runtime. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carrousel](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Affiche plusieurs contenus similaires le long d'un axe horizontal. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Image](https://amp.dev/documentation/components/amp-img?format=email) | Un remplacement géré par le runtime pour la balise HTML `img`. <br>  Vous pouvez également créer une [lightbox pour votre image](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Composants" }

{% alert note %}
Tout composant nécessitant l'authentification de l'utilisateur doit utiliser des [jetons d'accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou des [jetons d'assertion proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Autre %}

| Composant | Description |
|---------|--------------|
| [Liaison de données et expressions](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Ajoute une interactivité personnalisée avec état à vos pages AMP via la liaison de données et des expressions de type JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Composants" }

{% alert note %}
Tout composant nécessitant l'authentification de l'utilisateur doit utiliser des [jetons d'accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou des [jetons d'assertion proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

{% endtab %}
{% endtabs %}

Pour une liste complète des composants AMP, consultez la [documentation AMP](https://amp.dev/documentation/components/?format=email).

### Cas d'utilisation {#use-cases}

{% tabs local %}
{% tab Sondages interactifs %}

Grâce au composant `<amp-form>`, vous pouvez créer des sondages interactifs que vos utilisateurs peuvent remplir sans quitter leur boîte de réception. Il suffit d'utiliser `<amp-form>` pour soumettre les réponses au sondage, puis de faire en sorte que votre backend fournisse ces données agrégées.

Voici quelques exemples :
* E-mail de sondage de conférence
* Mise à jour dynamique des éléments dans le flux
* E-mail de mise en favoris d'articles

Avec ce composant, les utilisateurs peuvent soumettre ou effacer les valeurs des champs. De plus, selon la façon dont vous configurez votre e-mail, vous pouvez fournir des indications supplémentaires aux utilisateurs, comme indiquer si la soumission du sondage a réussi, ou afficher les réponses montrant les résultats du sondage (comme une campagne de vote).

{% endtab %}
{% tab Contenu repliable %}

Développez vos sections de contenu en utilisant le composant `<amp-accordion>`. Ce composant vous permet d'afficher des sections de contenu repliables et dépliables, offrant aux lecteurs la possibilité de parcourir le plan du contenu et d'accéder directement à n'importe quelle section.

Si vous avez tendance à envoyer de longs articles éducatifs ou des recommandations personnalisées, cela offre aux lecteurs la possibilité de parcourir le plan du contenu et d'accéder à n'importe quelle section ou recommandation produit spécifique pour obtenir plus de détails. Cela peut être particulièrement utile pour les utilisateurs mobiles, où même quelques phrases dans une section nécessitent de faire défiler l'écran.
{% endtab %}
{% tab E-mails riches en images %}

Si vous avez tendance à envoyer des e-mails contenant de nombreuses photos professionnelles, comme les marques de vente au détail, vous pouvez utiliser le composant `<amp-image-lightbox>` qui permet aux utilisateurs d'interagir avec une image qui les attire. Lorsque l'utilisateur clique sur l'image, ce composant affiche l'image au centre du message, créant un effet lightbox.

De plus, le composant `<amp-image-lightbox>` permet à l'utilisateur de voir une description détaillée de l'image. Vous pouvez utiliser le même composant pour plusieurs images. Par exemple, si votre e-mail contient plusieurs images, lorsque l'utilisateur clique sur l'une d'entre elles, l'image s'affiche dans la lightbox.

{% endtab %}
{% tab E-mails axés sur le texte %}

Pour les e-mails qui reposent principalement sur du texte, le composant `<amp-fit-text>` vous permet de gérer la taille et l'ajustement du texte dans une zone spécifiée.

Exemples :

- Mise à l'échelle du texte pour s'adapter à une zone
- Mise à l'échelle du texte pour s'adapter à la zone en utilisant une taille de police maximale, où vous pouvez définir la taille de police maximale
- Troncature du texte lorsque le contenu dépasse la zone

{% endtab %}
{% endtabs %}

### Utilisation d'amp-mustache {#use-amp-mustache}

Comme Liquid, AMP prend en charge un langage de script pour des cas d'utilisation plus avancés. Ce composant s'appelle [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email). Lorsque vous incluez du balisage Mustache, vous devez l'envelopper dans la balise [`raw`](https://shopify.github.io/liquid/tags/raw/) de Liquid. Notez que Liquid et Mustache partagent un style de syntaxe similaire.

En enveloppant votre contenu dans la balise `raw`, le moteur de traitement de Braze ignorera tout contenu entre les balises `raw` et enverra la variable Mustache dont votre équipe a besoin.

## Indicateurs et analyse {#metrics-and-analytics}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Indicateurs et analyse">
  <caption>Indicateurs et analyse</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Détails</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Nombre total d'ouvertures</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Opens' %} Pour les e-mails AMP, il s'agit du nombre total d'ouvertures pour les versions HTML et texte brut.</td>
        </tr>
        <tr>
            <td class="no-split">Nombre total de clics</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %} Pour les e-mails AMP, il s'agit du nombre total de clics dans les versions HTML et texte brut.</td>
        </tr>
        <tr>
            <td class="no-split">Ouvertures AMP</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">Clics AMP</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## Tests et résolution des problèmes {#test-and-troubleshoot}


Avant d'envoyer votre e-mail AMP, nous vous recommandons :

- De le tester conformément à ces [directives Gmail](https://developers.google.com/gmail/ampemail/testing-dynamic-email).
- D'utiliser le [Gmail AMP for Email Playground](https://amp.gmail.dev/playground/) pour valider le balisage AMP.
  - Si votre e-mail AMP utilise des balises Liquid, remplacez-les par des valeurs statiques avant de les coller dans le Gmail AMP for Email Playground. Les balises Liquid non rendues provoquent des erreurs de validation.

Pour que votre e-mail AMP soit livré à n'importe quel compte Gmail, l'e-mail doit remplir les conditions suivantes :

- Les exigences de sécurité d'AMP pour l'e-mail doivent être respectées.
- La partie MIME AMP doit contenir un document AMP valide.
- L'e-mail doit inclure la partie MIME AMP avant la partie MIME HTML.
- La partie MIME AMP doit être inférieure à 100&nbsp;Ko.

Notez que le nombre total de clics et les clics uniques ne prennent pas en compte les clics provenant d'un message AMP (HTML et texte brut uniquement). Les clics spécifiques à AMP sont attribués à l'indicateur *amp_click*.

Si aucune de ces conditions n'est à l'origine de l'erreur, contactez l'[Assistance]({{site.baseurl}}/support_contact).

### Configurer la boîte de réception Gmail pour afficher les e-mails AMP {#configure-gmail-inbox-to-render-amp-emails}

Vous pouvez configurer votre boîte de réception Gmail pour afficher les e-mails AMP à des fins de test en procédant comme suit :

1. Dans Gmail, sélectionnez **Settings** dans le coin supérieur droit de votre boîte de réception.
2. Sélectionnez **See all settings**.
3. Dans l'onglet **General**, accédez à la section **Dynamic email** et vérifiez que la case **Enable dynamic email** est cochée.
4. Ensuite, sélectionnez **Developer Settings**, puis cochez la case **Always allow dynamic emails from this sender:**.
5. Saisissez le même domaine que celui de l'adresse d'expéditeur de votre e-mail de test.
6. Enregistrez vos modifications.

Vous pouvez maintenant envoyer l'e-mail de test à votre compte Gmail, et les e-mails AMP devraient s'afficher dans Gmail.

### Questions fréquemment posées {#frequently-asked-questions}

#### Dois-je segmenter avec les e-mails AMP ? {#should-i-segment-with-amp-emails}

Nous recommandons de ne pas segmenter afin d'envoyer à tous les différents types d'utilisateurs. En effet, nous envoyons les messages AMP en multipart, avec différentes versions incluses dans l'e-mail d'origine. Si un utilisateur ne peut pas voir la version AMP, l'e-mail reviendra par défaut à la version HTML.