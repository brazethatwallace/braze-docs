---
nav_title: "Bonnes pratiques pour les e-mails"
article_title: "Bonnes pratiques pour les e-mails"
page_order: 1
page_type: reference
description: "Cet article présente des conseils et astuces généraux à garder à l'esprit lors de la création de campagnes e-mail pour différents cas d'utilisation et sujets."
channel: email

---

# Bonnes pratiques pour les e-mails {#email-guidelines}

> Lorsque vous créez votre campagne e-mail, il est important de garder à l'esprit la manière dont vos messages sont reçus par vos différents utilisateurs et fournisseurs de services d'e-mailing (ESP).

## Général {#general}

Voici quelques conseils rapides à garder à l'esprit lors de la création de votre contenu :

- Lorsque vous mettez en forme votre e-mail, utilisez des feuilles de style en ligne (inline CSS).
- Pour utiliser un seul modèle d'e-mail pour les versions mobile et ordinateur de bureau, maintenez la largeur en dessous de 500 pixels.
- Les images doivent peser moins de 5&nbsp;Mo. Nous recommandons d'utiliser les formats PNG, JPEG ou GIF pour une compatibilité maximale. Évitez les formats SVG et WebP, car de nombreux clients de messagerie majeurs ne les prennent pas encore en charge.
- Ne définissez pas de hauteurs et de largeurs pour les images, car cela peut provoquer des espaces blancs indésirables dans un e-mail dégradé.
- Les balises `div` ne doivent pas être utilisées, car la plupart des clients de messagerie ne prennent pas en charge leur utilisation. Utilisez plutôt des tableaux imbriqués.
- Évitez d'utiliser JavaScript, car il ne fonctionne avec aucun ESP.
- Braze améliore les temps de chargement en utilisant un réseau de diffusion de contenu mondial pour héberger toutes les images des e-mails.
- Sur mobile, les colonnes d'images sont étroites (~100 px chacune), de sorte que les lignes multi-images s'affichent toujours correctement (par exemple, quatre images ≈ quatre colonnes utilisables).

## Texte alternatif {#alternative-text}

Étant donné que les filtres anti-spam vérifient la présence d'une version HTML et d'une version texte brut d'un message, l'utilisation d'alternatives en texte brut est un excellent moyen de réduire votre score de spam. De plus, le texte alternatif `(alt="")` peut servir à compléter et, dans certains cas, à remplacer les images incluses dans le corps de votre e-mail qui auraient pu être filtrées par le fournisseur de messagerie de l'utilisateur. Les lecteurs d'écran annoncent le texte alternatif pour décrire les images, c'est donc l'occasion d'utiliser un langage simple pour fournir des informations clés sur une image.

## Validation des e-mails {#email-validation}

{% alert important %}
La validation est utilisée pour les adresses e-mail du tableau de bord, les adresses e-mail des utilisateurs finaux (vos clients), ainsi que les adresses d'expéditeur et de réponse d'un message e-mail.
{% endalert %}

La validation des e-mails a lieu lorsque l'adresse e-mail d'un utilisateur est mise à jour ou importée dans Braze via l'API, un téléchargement CSV, le SDK, ou modifiée dans le tableau de bord. Notez que vos adresses e-mail ne peuvent pas contenir d'espaces ; si elles sont envoyées via l'API, les espaces peuvent entraîner une erreur `400`.

Les adresses e-mail ciblées via les serveurs de Braze doivent être validées conformément aux normes [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822). Braze n'accepte pas certains caractères et les considère comme invalides. Si un e-mail fait l'objet d'un rebond, Braze marque l'adresse comme invalide et le statut d'abonnement n'est pas modifié.

Pour plus d'informations sur les caractères non autorisés et les règles de validation des e-mails, consultez [Validation des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/#how-it-works).

## Adresses d'expéditeur et de réponse {#from-and-reply-to-addresses}

Lorsque vous définissez vos adresses d'expéditeur, assurez-vous que le domaine de votre e-mail d'expéditeur correspond à votre domaine d'envoi (par exemple `marketing.yourdomain.com`). Ne pas respecter cette règle peut entraîner un désalignement SPF et DKIM. Toutes les adresses de réponse peuvent être définies sur votre domaine racine.

{% alert note %}
L'encodage Unicode n'est pas pris en charge dans les adresses d'expéditeur.
{% endalert %}

## Pièces jointes dans les e-mails {#attachments}

Lorsque vous ajoutez des pièces jointes à vos messages e-mail, suivez ces bonnes pratiques de livrabilité :

- Les filtres anti-spam analysent les pièces jointes et peuvent signaler votre message.
- Les fournisseurs de messagerie mettent parfois plus de temps à accepter les messages contenant des pièces jointes.
- En dehors des messages individuels, les pièces jointes peuvent donner à votre message une apparence risquée dans la boîte de réception.
- Limitez chaque pièce jointe à moins de 2&nbsp;Mo.
- N'envoyez pas d'informations sensibles en pièce jointe. Dirigez plutôt les utilisateurs vers votre portail sécurisé pour les consulter.

## Mise en page (glisser-déposer et HTML personnalisé) {#layout-drag-and-drop-and-custom-html}

La mise en page peut se casser lorsque le HTML/CSS généré par Braze entre en conflit avec du HTML personnalisé. Si cela se produit, procédez comme suit :

- Supprimez d'abord le HTML/CSS personnalisé.
- Vérifiez que les polices personnalisées se chargent correctement dans la prévisualisation.
- Vérifiez le remplissage (padding) des lignes et des colonnes.
- Privilégiez les mises en page basées sur des tableaux et restez dans les limites de largeur de l'éditeur.

Les Content Blocks qui intègrent du HTML provenant de l'extérieur de l'éditeur peuvent également casser la mise en page.

## Paramètres UTM dans les URL des e-mails {#utm-parameters-in-email-urls}

Les paramètres UTM balisent les URL à des fins d'analyse. Vous pouvez les construire avec Liquid et des attributs personnalisés.

- N'utilisez qu'un seul point d'interrogation `?` dans l'URL finale (des `?` supplémentaires peuvent casser les requêtes).
- Évitez les espaces et les caractères spéciaux dans les valeurs (utilisez `_` ou `-`).
- Confirmez que votre outil d'analyse ingère les UTM. Supprimez les espaces de fin dans les blocs Liquid `capture`. Les UTM sont sensibles à la casse.

### Vérifier les détails HTML {#check-html-details}

Gardez à l'esprit que certaines balises et certains attributs HTML ne sont pas autorisés, car ils pourraient permettre l'exécution de code malveillant dans le navigateur.

Consultez les listes suivantes pour connaître les balises et attributs HTML qui ne sont pas autorisés dans vos e-mails :
{% details Développer pour voir les balises HTML non autorisées %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `<iframe>`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details Développer pour voir les attributs HTML non autorisés %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}