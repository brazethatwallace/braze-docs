---
nav_title: Modèles de liens
article_title: Modèles de liens
page_order: 4
description: "Cet article explique comment créer différents types de modèles de liens dans vos e-mails."
tool:
  - Templates
channel:
  - email

---

# Modèles de liens {#link-templates}

> Grâce aux modèles de liens, vous pouvez créer des liens dynamiques et réutilisables pour vos campagnes par e-mail en ajoutant des paramètres ou en préfixant des URL. Cela permet de garantir la cohérence des URL dans vos campagnes et messages.

{% alert note %}
Les modèles de liens sont une fonctionnalité facultative. Si **Modèles de liens d'e-mail** n'apparaît pas dans la section **Modèles**, contactez votre gestionnaire de compte pour activer cette fonctionnalité.
{% endalert %}

## Fonctionnement {#how-it-works}

Les modèles de liens sont le plus souvent utilisés dans les cas d'usage suivants :

- Ajouter des paramètres de requête Google Analytics à tous les liens d'un e-mail donné
- Préfixer une URL à tous les liens d'un e-mail donné

Imaginons que vous meniez une campagne promotionnelle par e-mail pour le lancement d'un nouveau produit. Vous pouvez utiliser un modèle de lien qui dirige les utilisateurs vers la page du produit et personnaliser le lien pour inclure le nom de votre utilisateur ou un code promotionnel spécifique. Cela vous permet de suivre combien d'utilisateurs ont cliqué sur le lien et ont effectué un achat. De cette façon, vous pouvez garantir la cohérence de vos liens et mieux suivre vos analyses.

## Créer un modèle de lien {#creating-a-link-template}

Vous pouvez créer un nombre illimité de modèles de liens pour répondre à vos différents besoins. Pour créer un modèle de lien, procédez comme suit :

1. Accédez à **Contenu** > **Lien d'e-mail**.
2. Sélectionnez **Créer un modèle de lien d'e-mail**.
3. Donnez un nom à votre modèle de lien.
4. (Facultatif) Ajoutez une description, une équipe ou une étiquette pour ajouter des détails sur le modèle de lien.
5. (Facultatif) Activez le basculement pour ajouter automatiquement le modèle de lien aux liens dans les campagnes par e-mail et les Canvas. Cela s'applique lors de l'ajout d'un nouveau lien à tout e-mail nouveau ou existant.

Il existe deux types de modèles de liens que vous pouvez créer :

- [Modèle de lien qui s'insère avant une URL](#prepend-link-template)
- [Modèle de lien qui s'insère après une URL](#append-link-template)

Lorsque vous utilisez des modèles de liens et [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), Liquid ne doit être ajouté que dans la balise body pour garantir un rendu cohérent.

### Préfixe : créer un modèle de lien qui s'insère avant une URL {#prepend-link-template}

Pour ajouter une chaîne de caractères ou une URL avant les liens de votre e-mail, procédez comme suit :

1. Créez un nouveau modèle de lien.
2. Définissez la **Position du modèle** sur **Avant l'URL**.
3. Saisissez une chaîne de caractères qui sera toujours préfixée à votre URL.

L'**aperçu du modèle** vous fournit un exemple de la façon dont le modèle de lien sera inséré avant une URL.

![Champs Position du modèle, URL préfixée et Aperçu du modèle pour le processus d'insertion du modèle de lien avant une URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Suffixe : créer un modèle de lien qui s'insère après une URL {#append-link-template}

Si vous souhaitez ajouter des paramètres de requête après une URL dans votre e-mail :

1. Créez un nouveau modèle de lien.
2. Définissez la **Position du modèle** sur **Après l'URL**.
3. Saisissez les paramètres de requête (`value=example`) à la fin de chaque URL. Vous pouvez ajouter plusieurs paramètres à la fin d'une URL.

![Champs Position du modèle, Paramètres de requête et Aperçu du modèle pour le processus d'insertion du modèle de lien après une URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Utiliser des modèles de liens dans les campagnes par e-mail {#using-link-templates-in-email-campaigns}

Une fois vos modèles de liens configurés, vous pouvez les appliquer dans vos e-mails.

Pour appliquer un modèle de lien dans l'éditeur HTML ou l'éditeur par glisser-déposer, suivez ces étapes :

{% alert important %}
Pour accéder à l'onglet **Gestion des liens** dans l'éditeur HTML mis à jour ou l'éditeur par glisser-déposer, l'aliasing de lien doit être activé. Pour activer l'aliasing de lien, contactez votre gestionnaire de compte. Pour en savoir plus, consultez [Aliasing de lien]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing).
{% endalert %}

- **Éditeur HTML mis à jour :** Dans l'onglet **Contenu**, sélectionnez **Gestion des liens**, puis **Ajouter un modèle de lien**, choisissez votre modèle de lien, puis sélectionnez **Ajouter**.
- **Éditeur par glisser-déposer :** Dans l'onglet **Contenu**, sélectionnez **Gestion des liens**, puis **Ajouter un modèle de lien**, choisissez votre modèle de lien, puis sélectionnez **Ajouter**.

![Onglet Gestion des liens dans l'éditeur par glisser-déposer avec un exemple de liste de modèles de liens.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Les modèles de liens ne s'appliquent pas au texte brut. Cela signifie que Currents peut afficher des clics qui n'incluent pas les paramètres des modèles de liens, car ces clics peuvent provenir de la version texte brut de l'e-mail.
{% endalert %}

Lorsque vous ajoutez des modèles de liens dans l'onglet **Gestion des liens**, chaque modèle apparaît sous forme de colonne supplémentaire dans le tableau. Si des liens existants dans un e-mail ont déjà un modèle de lien ajouté, les liens nouvellement ajoutés auront également le modèle de lien ajouté par défaut.

{% alert tip %}
Lorsque vous incluez des liens dans votre message, veillez à commencer les URL par `http://` ou `https://`.
{% endalert %}

## Gérer les modèles de liens {#managing-link-templates}

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) des modèles de liens. Pour en savoir plus sur la création et la gestion des modèles et du contenu créatif, consultez [Modèles et médias]({{site.baseurl}}/user_guide/messaging/templates).

{% alert important %}
L'archivage des modèles n'est actuellement pas disponible pour les modèles de liens.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

### Paramètres UTM manquants {#missing-utm-parameters}

Les modèles de liens ne s'appliquent pas aux liens contenus dans les commentaires HTML standard (`<!-- ... -->`). Pour les commentaires conditionnels Outlook (par exemple, `<!--[if mso]>`), les modèles de liens sont appliqués lorsque l'aliasing de lien est activé pour votre espace de travail. Les espaces de travail sans aliasing de lien activé ignorent toujours les commentaires conditionnels.

### Paramètres UTM présents dans le navigateur mais absents des liens {#utm-parameters-present-in-browser-but-missing-from-links}

Cela peut se produire lorsque le chemin de l'URL dans votre e-mail ne correspond pas au chemin complet prévu (par exemple, un chemin raccourci ou différent de l'URL complète du site web).

- **Ce qu'il faut vérifier :** Le `href` dans l'e-mail inclut le chemin complet vers la page (pas seulement un chemin partiel qui repose sur des redirections).
- **Ce à quoi s'attendre :** Si le chemin dans l'e-mail est incomplet ou différent, les paramètres UTM de votre modèle de lien peuvent ne pas être appliqués à ce lien lorsqu'il est cliqué, même si le site web redirige quand même le visiteur vers la bonne page.

Par exemple, si le lien complet est `https://www.somewebsite.com/women/designer/johnjane` mais que l'e-mail utilise `https://www.somewebsite.com/designer/johnjane`, il est attendu que les paramètres UTM ne soient pas ajoutés au lien de l'e-mail.

### Paramètres UTM manquants dans les liens rendus par Liquid {#utm-parameters-missing-from-liquid-rendered-links}

Lors de l'application des modèles de liens, Braze analyse chaque URL pour déterminer où ajouter les paramètres. Si une étiquette Liquid génère une URL qui ne peut pas être analysée comme un URI valide, le modèle de lien est ignoré silencieusement. Vérifiez que votre sortie Liquid produit une URL bien formée. Testez en prévisualisant le message pour un utilisateur spécifique et en vérifiant que l'URL rendue est valide. Si l'URL inclut des variables Liquid dans le chemin ou la chaîne de requête, confirmez que la sortie ne contient pas de caractères invalides ou d'encodage défectueux.

### Valeurs UTM manquantes dans les envois de test {#utm-values-missing-in-test-sends}

Lors de l'envoi de test des modèles de liens, {% raw %}`{{${user_id}}}`{% endraw %} n'est pas rendu. À la place, dupliquez la campagne et configurez-la pour cibler les e-mails ou les `external_id` de vos utilisateurs internes, puis lancez la campagne pour vérifier que tous les paramètres UTM du modèle de lien sont renseignés.

## Questions fréquemment posées {#frequently-asked-questions}

Pour obtenir des réponses aux questions fréquemment posées sur les modèles de liens, consultez notre page [FAQ sur les modèles]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).