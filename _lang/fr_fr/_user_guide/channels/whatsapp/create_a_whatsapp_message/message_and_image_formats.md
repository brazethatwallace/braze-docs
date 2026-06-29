---
nav_title: Formats de messages et d'images
article_title: Formats de messages et d'images WhatsApp
description: "Cet article de référence couvre la structure des messages, les limites des composants et les exigences relatives aux ressources média pour la création de messages et de modèles WhatsApp."
alias: /whatsapp_media_formats/
page_order: 9
channel:
  - WhatsApp
---

# Formats de messages et d'images WhatsApp {#whatsapp-message-and-image-formats}

> Voici les exigences relatives à la structure des messages, aux composants et aux ressources média pour la création de messages et de modèles WhatsApp.

Il existe deux types de messages WhatsApp dans Braze : les [messages modèles](#template-messages) et les [messages de réponse](#response-messages).

| Type de message | Quand l'utiliser | Approbation Meta |
|---|---|---|
| Messages modèles | Communication initiée par l'entreprise ; envoyée à tout moment | Requise ; les modèles doivent être soumis à Meta et approuvés avant l'envoi. |
| Messages de réponse | Réponses aux messages initiés par l'utilisateur ; uniquement dans la fenêtre de conversation de 24 heures | Non requise |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="WhatsApp message and image formats" }

Les messages modèles doivent être soumis à Meta pour approbation, ce qui peut prendre jusqu'à 24 heures. Une fois approuvés, ils peuvent être envoyés à tout moment. Les messages de réponse (appelés « messages de session » dans la documentation de Meta) ne peuvent être envoyés que lorsqu'une fenêtre de conversation active est ouverte, c'est-à-dire dans les 24 heures suivant le dernier message entrant de l'utilisateur.

## Messages modèles {#template-messages}

Les messages modèles WhatsApp sont des formats de messages pré-approuvés utilisés pour les communications initiées par l'entreprise. Dans Braze, ils sont construits à partir de composants que vous définissez avant de les soumettre à Meta. Tous les messages modèles sont classés par catégorie : marketing, utilitaire ou authentification.

### Modèles marketing {#marketing-templates}

Les modèles marketing sont le type le plus couramment utilisé dans Braze. Ils se composent de quatre composants maximum :

| Composant | Requis | Notes |
|---|---|---|
| En-tête | Non | Prend en charge le texte, les images, les vidéos, les documents ou la localisation. Consultez les [spécifications média](#media-specifications) pour les exigences relatives aux types de fichiers, tailles et dimensions. |
| Corps | Oui | Le contenu principal du message |
| Pied de page | Non | Texte complémentaire affiché sous le corps |
| Boutons | Non | Jusqu'à 10 boutons (tous les types de boutons sont pris en charge) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Marketing templates" }

#### Longueur des caractères {#character-length}

| Composant | Longueur maximale en caractères |
|---|---|
| Corps | 1 024 caractères |
| Pied de page | 60 caractères |
| Libellé du bouton (URL, téléphone, réponse rapide) | 25 caractères |
| Numéro de téléphone (dans le bouton téléphone) | 20 caractères |
| Nom du modèle | 512 caractères (minuscules, alphanumériques et underscores uniquement) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Character length" }

#### Types de boutons {#button-types}

| Type de bouton | Comportement | Notes |
|---|---|---|
| Réponse rapide | Envoie le texte du libellé du bouton comme réponse dans la conversation | |
| URL | Ouvre une URL dans le navigateur par défaut de l'utilisateur ; prend en charge 1 variable ajoutée à la fin de l'URL (2 000 caractères maximum) | |
| Numéro de téléphone | Lance un appel vers le numéro de téléphone spécifié | |
| Copier le code promo | Copie un code promo dans le presse-papiers de l'utilisateur | Nécessite toujours l'approbation de Meta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Button types" }

#### Formatage des paramètres {#parameter-formatting}

Les variables de modèle peuvent utiliser des paramètres nommés (tels que {% raw %}`{{first_name}}`{% endraw %}) ou des paramètres positionnels (tels que {% raw %}`{{1}}`{% endraw %}). Dans Braze, les variables peuvent être remplacées par du Liquid ou du texte brut. Incluez toujours des valeurs par défaut pour les variables Liquid ; les messages dont les valeurs de variables sont manquantes ne seront pas envoyés.

### Modèles de carrousel de cartes média {#media-card-carousel-templates}

Les modèles de carrousel affichent un corps de message suivi de 2 à 10 cartes produit défilables horizontalement, chacune avec sa propre ressource média et ses boutons. Ils ne sont disponibles que pour les messages modèles marketing.

#### Message de niveau supérieur {#top-level-message}

| Composant | Requis | Propriétés maximales | Notes |
|---|---|---|---|
| Corps du texte | Oui | 1 024 caractères | Prend en charge les variables |
| Cartes | Oui | 2 à 10 cartes | Le nombre de cartes est fixé lors de la création du modèle. Un modèle de carrousel approuvé ne peut être envoyé qu'avec le nombre exact de cartes défini lors de la création. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Top-level message" }

#### Spécifications par carte {#per-card-specifications}

| Composant | Requis | Notes |
|---|---|---|
| En-tête (image ou vidéo) | Oui | Toutes les cartes doivent utiliser le même format (toutes en image ou toutes en vidéo). Cela inclut la même structure de composant ; vous ne pouvez pas mélanger des cartes avec et sans corps de texte ou boutons.<br><br> Les ressources d'en-tête de carte sont automatiquement recadrées en format large en fonction de l'appareil de l'utilisateur. |
| Corps du texte | Non | Si une carte inclut un corps de texte, toutes les cartes doivent inclure un corps de texte |
| Boutons | Non | 2 boutons maximum par carte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Per-card specifications" }

#### Longueur des caractères par carte {#per-card-character-lengths}

| Composant | Longueur maximale en caractères | Notes |
|---|---|---|
| Corps du texte de la carte | 160 caractères | |
| Libellé du bouton | 25 caractères | |
| Numéro de téléphone (dans le bouton téléphone) | 20 caractères | |
| URL (dans le bouton URL) | 2 000 caractères ; prend en charge 1 variable ajoutée à la fin | Les boutons URL s'ouvrent dans le navigateur par défaut de l'utilisateur, en dehors de WhatsApp. Aucun webhook de commande ou de conversion n'est déclenché à partir de ce point. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Per-card character lengths" }

## Messages de réponse {#response-messages}

Les messages de réponse (également appelés « messages de session » par Meta) ne peuvent être envoyés que dans la fenêtre de conversation de 24 heures. Celle-ci est ouverte et réinitialisée lorsqu'un utilisateur envoie un message à votre entreprise.

Les messages de réponse composés directement dans l'éditeur de Campaign ou de Canvas de Braze ne nécessitent pas l'approbation de Meta.

Braze prend en charge sept mises en page de messages de réponse :

| Mise en page du message | Description |
|---|---|
| Texte | Corps de message en texte brut |
| Média | Message avec une image, une vidéo, un fichier audio ou un document en pièce jointe |
| Réponse rapide | Message avec jusqu'à 3 boutons de réponse cliquables |
| Bouton d'appel à l'action (CTA) | Message avec un bouton URL ou un bouton de numéro de téléphone |
| Message de liste | Message avec une liste structurée et défilable d'options sélectionnables |
| Message de flux | Message qui invite les utilisateurs à remplir un formulaire ou une tâche interactive dans WhatsApp, dont le résultat est renvoyé à Braze |
| Message produit Meta | Message qui met en avant un seul produit, plusieurs produits ou un catalogue entier à partir d'un catalogue Meta connecté |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Response messages" }

### Composants du message de liste {#list-message-components}

| Composant | Propriétés maximales |
|---|---|
| Corps du texte | 4 096 caractères |
| Libellé du bouton (pour ouvrir la liste) | 20 caractères |
| Nombre de sections | Jusqu'à 10 |
| Nombre de lignes par section | Jusqu'à 10 |
| Titre de la section | 24 caractères |
| Titre de la ligne | 24 caractères |
| Description de la ligne | 72 caractères |
{: .reset-td-br-1 .reset-td-br-2 aria-label="List message components" }

### Composants de réponse rapide {#quick-reply-components}

| Composant | Propriétés maximales |
| --- | --- |
| Bouton | Jusqu'à 3 |
| Libellé du bouton | 20 caractères par bouton |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quick reply components" }

## Spécifications média {#media-specifications}

Les spécifications suivantes s'appliquent à tous les médias dans les en-têtes de modèles WhatsApp, les messages de réponse ou les messages média autonomes.

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

### Images {#images}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp images' %}

### Vidéo {#video}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp videos' %}

#### Compatibilité Android {#android-compatibility}

Le profil H.264 « High » encodé avec des B-frames n'est pas pris en charge sur les clients WhatsApp Android. Utilisez le profil H.264 « Main » sans B-frames ou le profil « Baseline » pour la compatibilité la plus large. Si vous ré-encodez avec ffmpeg, utilisez le flag `-movflags faststart` pour placer les boîtes `moov` avant les boîtes `mdat`.

### Audio {#audio}

Les spécifications suivantes s'appliquent aux messages média de réponse et aux messages audio, et sont basées sur leur type audio : message vocal ou message audio basique.

#### Message vocal {#voice-message}

Un message vocal fonctionne comme une note vocale enregistrée, avec des contrôles de lecture et la prise en charge de la transcription.

| Propriété | Spécifications |
|---|---|
| Format requis | OGG uniquement |
| Codec requis | OPUS uniquement (entrée mono) |
| Taille du fichier | 16 Mo maximum |
| Icône de lecture | Cette icône n'apparaît que si le fichier fait 512 Ko ou moins ; les fichiers plus volumineux affichent une icône de téléchargement |
| Transcription | S'affiche automatiquement si l'utilisateur a activé les transcriptions vocales WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voice message" }

#### Message audio basique {#basic-audio-message}

Les spécifications suivantes s'appliquent au partage de fichiers audio standard (extraits musicaux, publicités audio et fichiers sonores).

| Format | Extension | Taille maximale du fichier | Notes |
|---|---|---|---|
| AAC | .aac | 16 Mo | |
| AMR | .amr | 16 Mo | |
| MP3 | .mp3 | 16 Mo | |
| MP4 Audio | .m4a | 16 Mo | |
| OGG (codec OPUS) | .ogg | 16 Mo | Les fichiers OGG doivent utiliser le codec OPUS. Le format de base `audio/ogg` sans OPUS n'est pas pris en charge.<br><br> Les fichiers OGG/OPUS envoyés en tant que messages audio basiques afficheront une icône de microphone (identique aux messages vocaux) plutôt qu'une icône de musique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Basic audio message" }

#### Considérations {#considerations}

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- Pas de prise en charge des légendes pour les messages audio.
- Une erreur courante est l'inadéquation des types MIME. Vérifiez que le type MIME de votre fichier correspond à son extension avant l'envoi.

### Documents {#documents}

Les spécifications suivantes s'appliquent aux en-têtes de modèles (format document), aux messages média de réponse et aux messages de document.

| Type de document | Types de fichiers | Taille maximale du fichier |
|---|---|---|
| PDF | PDF | 100 Mo |
| Microsoft Word | DOC, DOCX | 100 Mo |
| Microsoft Excel | XLS, XLSX | 100 Mo |
| Microsoft PowerPoint | PPT, PPTX | 100 Mo |
| Texte brut | TXT | 100 Mo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Documents" }

#### Considérations

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- Les légendes sont facultatives et peuvent contenir 1 024 caractères maximum.
- Le nom de fichier est facultatif. WhatsApp utilise l'extension du fichier pour déterminer quelle icône de document afficher dans la conversation.
- Seuls les formats listés sont officiellement pris en charge. D'autres types de fichiers peuvent être envoyés, mais leur rendu correct dans WhatsApp n'est pas garanti.

## Référence rapide : spécifications média WhatsApp {#quick-reference-whatsapp-media-specifications}

| Type de média | Types de fichiers | Taille maximale du fichier | Disponibilité des légendes |
|---|---|---|---|
| Image | JPEG, PNG | 5 Mo | Oui (1 024 caractères maximum) |
| Vidéo | MP4, 3GPP | 16 Mo | Oui (1 024 caractères maximum) |
| Audio (vocal) | OGG (OPUS) | 16 Mo | Non |
| Audio (basique) | AAC, AMR, MP3, M4A, OGG | 16 Mo | Non |
| Document | PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT | 100 Mo | Oui (1 024 caractères maximum) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Quick reference: WhatsApp media specifications" }