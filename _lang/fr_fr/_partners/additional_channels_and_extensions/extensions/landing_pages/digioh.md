---
nav_title: Digioh
article_title: Digioh
description: "Cet article de référence présente le partenariat entre Braze et Digioh, une plateforme d'enquête permettant de créer des pop-ups, des formulaires, des enquêtes et des centres de préférences de communication qui stimulent l'engagement à travers vos Campaigns Braze."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) prend en charge la croissance des listes, la capture des données first-party et l'utilisation de ces données dans les Campaigns Braze.

_Cette intégration est maintenue par Digioh._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Digioh vous permet d'utiliser un générateur par glisser-déposer pour créer des formulaires, des pop-ups, des centres de préférences, des pages d'accueil et des enquêtes adaptés à votre marque, qui vous mettent en relation avec vos clients. Digioh vous aide à configurer l'intégration et peut créer, concevoir et lancer votre première Campaign.

![« Créez des centres de préférences flexibles pour les e-mails et les communications avec Digioh »]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Digioh | Un [compte Digioh](https://www.digioh.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST Braze avec les autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint de l'API Braze `/users/track/` | L'URL de votre endpoint REST avec les détails `/users/track/` ajoutés. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints).<br><br>Par exemple, si votre endpoint REST API est `https://rest.iad-01.braze.com`, votre endpoint `/users/track/` sera `https://rest.iad-01.braze.com/users/track/`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour intégrer Digioh, vous devez d'abord configurer le connecteur Braze. Une fois cette opération terminée, vous devrez appliquer l'intégration à une fenêtre modale (widget). Consultez [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) pour en savoir plus sur les principes de base de l'intégration.

### Étape 1 : Créer une intégration Digioh {#step-1-create-digioh-integration}

Dans Digioh, cliquez sur l'onglet **Integrations**, puis sur le bouton **New Integration**. Sélectionnez **Braze** dans la liste déroulante **Integration** et nommez l'intégration.

![« Sélectionnez la bonne intégration dans la liste déroulante »]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

Ensuite, saisissez la clé API REST Braze et votre endpoint de l'API Braze `/users/track/`.

Enfin, utilisez la section de mappage des champs pour associer des champs personnalisés supplémentaires au-delà de l'e-mail et du nom. L'extrait de code suivant montre un exemple de payload. Lorsque vous avez terminé, sélectionnez **Create Integration**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### Étape 2 : Créer une lightbox Digioh {#step-2-create-a-digioh-lightbox}

Utilisez l'[éditeur de conception](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) de Digioh pour créer une fenêtre modale (widget). <br>
Vous souhaitez consulter une galerie de méthodes pour tirer parti de l'éditeur de conception ? Visitez la [galerie thématique](https://www.digioh.com/theme-gallery) de Digioh.

### Étape 3 : Appliquer l'intégration {#step-3-apply-integration}

Pour appliquer cette intégration à une [lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) Digioh, accédez à la page **Boxes** et sélectionnez le lien **Add** ou **Edit** dans la colonne **Integrations**. Vous pouvez également l'ajouter depuis la section **Integration** de l'éditeur.

![« Ajouter l'intégration à une lightbox »]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

Ici, sélectionnez **Add Integration**, choisissez l'intégration souhaitée et cliquez sur **Save**. Digioh transmettra désormais vos leads capturés à Braze en temps réel.