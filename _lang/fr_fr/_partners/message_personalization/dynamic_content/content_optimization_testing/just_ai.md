---
nav_title: JustAI
article_title: JustAI
description: "Cet article de référence décrit le partenariat entre Braze et JustAI, une plateforme SaaS basée sur l'intelligence artificielle qui crée des versions personnalisées de Campaigns existantes et optimise les lignes d'objet, le contenu créatif et les mises en page d'e-mails HTML au fil du temps."
alias: ["/partners/just_ai/", "/partners/just_words/"]
page_type: partner
---

# Guide d'intégration JustAI {#justai-integration-guide}

> [JustAI](https://www.getjust.ai/) hyper-personnalise les messages à grande échelle sur les canaux de marketing du cycle de vie, vous permettant de tester dynamiquement des centaines de variations et d'actualiser automatiquement le contenu sous-performant.

Lorsque vous utilisez JustAI avec le [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) de Braze pour personnaliser vos Campaigns et Canvas Braze existants, JustAI utilise Braze Currents pour optimiser le contenu de manière dynamique, sans intervention de votre part.

## Quels sont les avantages ? {#what-are-the-benefits}

Une fois votre intégration terminée, vous pouvez tirer parti de la plateforme JustAI pour :

- Consulter les résultats d'expériences en temps réel
- Modifier dynamiquement le texte
- Visualiser des informations sur les performances

{% alert note %}
Des questions ? Contactez JustAI via leur [page de réservation](https://www.getjust.ai/book-demo) ou via le canal Slack partagé.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte JustAI | Un compte [JustAI](https://www.getjust.ai/) est requis pour bénéficier de ce partenariat. Si vous n'avez pas de compte JustAI, [planifiez un appel d'onboarding de 30 minutes](https://www.getjust.ai/book-demo). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de JustAI avec Braze {#integrating-justai-with-braze}

### Étape 1 : Créer un modèle JustAI {#step-1-create-a-justai-template}

1. Accédez à votre console JustAI et [créez un nouveau modèle](https://console.getjust.ai/new).
2. Choisissez un identifiant facile à retenir qui utilise uniquement des lettres, des chiffres et des underscores.
3. Renseignez les détails de base de la campagne.
4. Utilisez l'intelligence artificielle pour générer des variations personnalisées.

![La plateforme de création de modèles JustAI.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### Étape 2 : Créer une clé API JustAI {#step-2-create-a-justai-api-key}

1. Accédez à **Org Settings** > **API Keys** > **Generate API Key**.
2. Copiez et enregistrez la clé API dans un emplacement sécurisé.

![Le formulaire de clé API JustAI.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### Étape 3 : Utiliser JustAI dans votre contenu Braze {#step-3-use-justai-in-your-braze-content}

JustAI fonctionne avec les Canvas et les Campaigns grâce au Contenu connecté. Si vous créez un Canvas, chaque étape d'e-mail doit correspondre à un modèle JustAI unique.

#### Étape 3.1 : Configurer votre test A/B {#step-31-set-up-your-ab-test}

{% tabs %}
{% tab Canvas %}

1. Dans un Canvas, sélectionnez **Ajouter une variante** > **Ajouter une variante** jusqu'à obtenir le nombre de variantes souhaité, puis ajoutez des étapes à chaque variante (comme une étape de message e-mail).
2. Répartissez le trafic d'audience comme souhaité. Par exemple, si vous avez deux variantes, vous pouvez attribuer 50 % à chacune. Ou bien, vous pouvez avoir deux variantes à 40 % chacune et un groupe de contrôle à 20 %. Pour en savoir plus sur les tests A/B pour les Canvas, consultez [Créer un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
3. Dans les compositeurs des étapes de message que vous souhaitez utiliser avec le Contenu connecté, collez l'extrait de code de Contenu connecté depuis la console JustAI, comme l'extrait suivant.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Configuration d'un test A/B Canvas dans Braze.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campaign %}

1. À l'étape **Compose Messages** de votre Campaign, créez deux variantes.
2. À l'étape **Target Audience**, accédez à la section **A/B Testing** et modifiez les pourcentages d'utilisateurs qui recevront chacune de vos variantes (et votre groupe de contrôle facultatif). Vous pouvez personnaliser davantage votre test en sélectionnant une option d'optimisation. Pour en savoir plus sur les tests A/B pour les Campaigns, consultez [Créer des tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/).
3. Dans le compositeur de messages, collez l'extrait de code de Contenu connecté depuis la console JustAI. L'extrait Liquid suivant en montre un exemple.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Étape 3.2 : Ajouter la personnalisation avec des attributs personnalisés (facultatif) {#step-32-add-personalization-with-custom-attributes-optional}

Pour personnaliser vos messages avec des attributs personnalisés (tels que `industry`), utilisez le format Liquid suivant :

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

Notez que l'attribut personnalisé `industry` est indiqué par {% raw %}`&attrs.industry={{ custom_attribute.industry }}`{% endraw %}.

![Logique Liquid Braze dans un compositeur de messages HTML.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### Étape 4 : Prévisualiser l'e-mail {#step-4-preview-the-email}

Assurez-vous de prévisualiser l'e-mail dans Braze pour confirmer que le contenu personnalisé s'affiche correctement.

![Prévisualisation d'un message Braze pour un e-mail JustAI.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### Étape 5 : Configurer Braze Currents {#step-5-set-up-braze-currents}

Braze Currents permet le suivi des performances et l'optimisation au fil du temps.

1. Dans Braze, accédez à **Intégrations partenaires** > **Exportation de données**.
2. Sélectionnez **Create New Test Current**, puis sélectionnez **Test Amazon S3 Data Export**.

![Menu déroulant « Create New Test Current » avec l'option « Test Amazon S3 Data Export ».]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3. Saisissez l'identifiant d'accès S3, la clé d'accès secrète AWS, le nom du compartiment et le dossier fournis par JustAI lors de l'onboarding.

![Section « Credentials » pour la clé d'accès secrète AWS.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4. Sélectionnez les événements à suivre, tels que les envois, les ouvertures, les clics, les désabonnements, les conversions et autres.

![Section « Message Engagement Events » avec les événements à sélectionner.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5. Lancez le Braze Current.

Vous êtes prêt ! Vous pouvez maintenant utiliser JustAI avec le Contenu connecté de Braze.