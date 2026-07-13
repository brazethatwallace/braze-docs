---
nav_title: Nachrichten- und Bildformate
article_title: WhatsApp-Nachrichten- und Bildformate
description: "Dieser Referenzartikel behandelt die Nachrichtenstruktur, Komponentenbeschränkungen und Medien-Asset-Anforderungen für die Erstellung von WhatsApp-Nachrichten und -Templates."
alias: /whatsapp_media_formats/
page_order: 9
channel:
  - WhatsApp
---

# WhatsApp-Nachrichten- und Bildformate {#whatsapp-message-and-image-formats}

> Hier finden Sie die Anforderungen an Nachrichtenstruktur, Komponenten und Medien-Assets für die Erstellung von WhatsApp-Nachrichten und -Templates.

Es gibt zwei Arten von WhatsApp-Nachrichten in Braze: [Template-Nachrichten](#template-messages) und [Antwortnachrichten](#response-messages).

| Nachrichtentyp | Verwendung | Meta-Genehmigung |
|---|---|---|
| Template-Nachrichten | Vom Unternehmen initiierte Kontaktaufnahme; kann jederzeit gesendet werden | Erforderlich; Templates müssen bei Meta eingereicht und vor dem Versand genehmigt werden. |
| Antwortnachrichten | Antworten auf von Nutzer:innen initiierte Nachrichten; nur innerhalb des 24-Stunden-Konversationsfensters | Nicht erforderlich |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="WhatsApp-Nachrichten- und Bildformate" }

Template-Nachrichten müssen zur Genehmigung bei Meta eingereicht werden, was bis zu 24 Stunden dauern kann. Nach der Genehmigung können sie jederzeit gesendet werden. Antwortnachrichten (in der Meta-Dokumentation als „Session Messages“ bezeichnet) können nur gesendet werden, solange ein aktives Konversationsfenster geöffnet ist – innerhalb von 24 Stunden nach der letzten eingehenden Nachricht der Nutzer:innen.

## Template-Nachrichten {#template-messages}

WhatsApp-Template-Nachrichten sind vorab genehmigte Nachrichtenformate, die für vom Unternehmen initiierte Kontaktaufnahmen verwendet werden. In Braze werden sie aus Komponenten erstellt, die Sie vor der Einreichung bei Meta definieren. Alle Template-Nachrichten sind kategoriebasiert: Marketing, Utility oder Authentifizierung.

### Marketing-Templates {#marketing-templates}

Marketing-Templates sind der am häufigsten in Braze verwendete Typ. Sie bestehen aus bis zu vier Komponenten:

| Komponente | Erforderlich | Hinweise |
|---|---|---|
| Header | Nein | Unterstützt Text, Bild, Video, Dokument oder Standort. Siehe [Medienspezifikationen](#media-specifications) für Dateityp-, Größen- und Dimensionsanforderungen. |
| Body | Ja | Der Hauptnachrichteninhalt |
| Footer | Nein | Ergänzender Text, der unterhalb des Body angezeigt wird |
| Buttons | Nein | Bis zu 10 Buttons (alle Button-Typen werden unterstützt) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Marketing-Templates" }

#### Zeichenlänge {#character-length}

| Komponente | Maximale Zeichenlänge |
|---|---|
| Body | 1.024 Zeichen |
| Footer | 60 Zeichen |
| Button-Beschriftung (URL, Telefon, Schnellantwort) | 25 Zeichen |
| Telefonnummer (im Telefon-Button) | 20 Zeichen |
| Template-Name | 512 Zeichen (nur Kleinbuchstaben, alphanumerisch und Unterstriche) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zeichenlänge" }

#### Button-Typen {#button-types}

| Button-Typ | Verhalten | Hinweise |
|---|---|---|
| Schnellantwort | Sendet den Button-Beschriftungstext als Antwort in der Konversation | |
| URL | Öffnet eine URL im Standardbrowser der Nutzer:innen; unterstützt 1 Variable, die am Ende der URL angehängt wird (max. 2.000 Zeichen) | |
| Telefonnummer | Initiiert einen Anruf an die angegebene Telefonnummer | |
| Gutscheincode kopieren | Kopiert einen Gutscheincode in die Zwischenablage der Nutzer:innen | Erfordert immer eine Meta-Genehmigung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Button-Typen" }

#### Parameterformatierung {#parameter-formatting}

Template-Variablen können entweder benannte Parameter (wie {% raw %}`{{first_name}}`{% endraw %}) oder positionelle Parameter (wie {% raw %}`{{1}}`{% endraw %}) verwenden. In Braze können Variablen durch Liquid oder Klartext ersetzt werden. Geben Sie immer Standardwerte für Liquid-Variablen an; Nachrichten mit fehlenden Variablenwerten werden nicht gesendet.

### Media-Card-Karussell-Templates {#media-card-carousel-templates}

Karussell-Templates zeigen einen Nachrichtentext gefolgt von 2–10 horizontal scrollbaren Produktkarten an, die jeweils ein eigenes Medien-Asset und Buttons haben. Sie sind nur für Marketing-Template-Nachrichten verfügbar.

#### Nachricht auf oberster Ebene {#top-level-message}

| Komponente | Erforderlich | Maximale Eigenschaften | Hinweise |
|---|---|---|---|
| Body-Text | Ja | 1.024 Zeichen | Unterstützt Variablen |
| Karten | Ja | 2–10 Karten | Die Kartenanzahl wird bei der Template-Erstellung festgelegt. Ein genehmigtes Karussell-Template kann nur mit der exakten Anzahl von Karten gesendet werden, die bei der Erstellung definiert wurde. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Nachricht auf oberster Ebene" }

#### Spezifikationen pro Karte {#per-card-specifications}

| Komponente | Erforderlich | Hinweise |
|---|---|---|
| Header (Bild oder Video) | Ja | Alle Karten müssen dasselbe Format verwenden (alle Bilder oder alle Videos). Dies schließt dieselbe Komponentenstruktur ein; Sie können keine Karten mit und ohne Body-Text oder Buttons mischen.<br><br> Header-Assets der Karten werden automatisch auf ein Breitformat zugeschnitten, basierend auf dem Gerät der Nutzer:innen. |
| Body-Text | Nein | Wenn eine Karte Body-Text enthält, müssen alle Karten Body-Text enthalten |
| Buttons | Nein | Maximal 2 Buttons pro Karte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Spezifikationen pro Karte" }

#### Zeichenlängen pro Karte {#per-card-character-lengths}

| Komponente | Maximale Zeichenlänge | Hinweise |
|---|---|---|
| Karten-Body-Text | 160 Zeichen | |
| Button-Beschriftung | 25 Zeichen | |
| Telefonnummer (im Telefon-Button) | 20 Zeichen | |
| URL (im URL-Button) | 2.000 Zeichen; unterstützt 1 Variable, die am Ende angehängt wird | URL-Buttons öffnen sich im Standardbrowser der Nutzer:innen, außerhalb von WhatsApp. Ab diesem Punkt werden keine Bestell- oder Conversion-Webhooks ausgelöst. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zeichenlängen pro Karte" }

## Antwortnachrichten {#response-messages}

Antwortnachrichten (von Meta auch „Session Messages“ genannt) können nur innerhalb des 24-Stunden-Konversationsfensters gesendet werden. Dieses wird geöffnet und zurückgesetzt, wenn Nutzer:innen Ihrem Unternehmen eine Nachricht senden.

Antwortnachrichten, die direkt im Braze-Campaign- oder Canvas-Editor verfasst werden, erfordern keine Meta-Genehmigung.

Braze unterstützt sieben Antwortnachrichten-Layouts:

| Nachrichten-Layout | Beschreibung |
|---|---|
| Text | Reiner Body-Text |
| Medien | Nachricht mit einem Bild-, Video-, Audio- oder Dokumentanhang |
| Schnellantwort | Nachricht mit bis zu 3 antippbaren Antwort-Buttons |
| Call-to-Action (CTA)-Button | Nachricht mit einem URL-Button oder Telefonnummer-Button |
| Listennachricht | Nachricht mit einer strukturierten, scrollbaren Liste auswählbarer Optionen |
| Flow-Nachricht | Nachricht, die Nutzer:innen auffordert, ein Formular oder eine interaktive Aufgabe in WhatsApp auszufüllen, wobei die Ausgabe an Braze zurückgegeben wird |
| Meta-Produktnachricht | Nachricht, die ein einzelnes Produkt, mehrere Produkte oder einen gesamten Katalog aus einem verbundenen Meta-Katalog hervorhebt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Antwortnachrichten" }

### Listennachricht-Komponenten {#list-message-components}

| Komponente | Maximale Eigenschaften |
|---|---|
| Body-Text | 4.096 Zeichen |
| Button-Beschriftung (zum Öffnen der Liste) | 20 Zeichen |
| Anzahl der Abschnitte | Bis zu 10 |
| Anzahl der Zeilen pro Abschnitt | Bis zu 10 |
| Abschnittstitel | 24 Zeichen |
| Zeilentitel | 24 Zeichen |
| Zeilenbeschreibung | 72 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Listennachricht-Komponenten" }

### Schnellantwort-Komponenten {#quick-reply-components}

| Komponente | Maximale Eigenschaften |
| --- | --- |
| Button | Bis zu 3 |
| Button-Beschriftung | 20 Zeichen pro Button |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schnellantwort-Komponenten" }

## Medienspezifikationen {#media-specifications}

Die folgenden Spezifikationen gelten für alle Medien in WhatsApp-Template-Headern, Antwortnachrichten oder eigenständigen Mediennachrichten.

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

### Bilder {#images}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp images' %}

### Video {#video}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp videos' %}

#### Android-Kompatibilität {#android-compatibility}

Das H.264-Profil „High“ mit B-Frames wird auf Android-WhatsApp-Clients nicht unterstützt. Verwenden Sie das H.264-Profil „Main“ ohne B-Frames oder das Profil „Baseline“ für die breiteste Kompatibilität. Wenn Sie mit ffmpeg neu kodieren, verwenden Sie das Flag `-movflags faststart`, um `moov`-Boxen vor `mdat`-Boxen zu platzieren.

### Audio {#audio}

Die folgenden Spezifikationen gelten für Antwort-Mediennachrichten und Audio-Nachrichten und basieren auf dem Audio-Typ: Sprachnachricht oder einfache Audio-Nachricht.

#### Sprachnachricht {#voice-message}

Eine Sprachnachricht funktioniert wie eine aufgenommene Sprachnotiz mit Wiedergabesteuerung und Transkriptionsunterstützung.

| Eigenschaft | Spezifikationen |
|---|---|
| Erforderliches Format | Nur OGG |
| Erforderlicher Codec | Nur OPUS (Mono-Eingang) |
| Dateigröße | Maximal 16 MB |
| Wiedergabe-Symbol | Dieses Symbol wird nur angezeigt, wenn die Datei 512 KB oder kleiner ist; größere Dateien zeigen ein Download-Symbol an |
| Transkription | Wird automatisch angezeigt, wenn Nutzer:innen WhatsApp-Sprachtranskripte aktiviert haben |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sprachnachricht" }

#### Einfache Audio-Nachricht {#basic-audio-message}

Die folgenden Spezifikationen gelten für das Teilen von Standard-Audio-Dateien (Musikclips, Audio-Werbung und Sounddateien).

| Format | Erweiterung | Maximale Dateigröße | Hinweise |
|---|---|---|---|
| AAC | .aac | 16 MB | |
| AMR | .amr | 16 MB | |
| MP3 | .mp3 | 16 MB | |
| MP4 Audio | .m4a | 16 MB | |
| OGG (OPUS-Codec) | .ogg | 16 MB | OGG-Dateien müssen den OPUS-Codec verwenden. Einfaches `audio/ogg` ohne OPUS wird nicht unterstützt.<br><br> OGG/OPUS-Dateien, die als einfache Audio-Nachrichten gesendet werden, zeigen ein Mikrofon-Symbol (wie bei Sprachnachrichten) anstelle eines Musik-Symbols an. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Einfache Audio-Nachricht" }

#### Hinweise {#considerations}

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- Keine Untertitelunterstützung für Audio-Nachrichten.
- Ein häufiger Fehler sind nicht übereinstimmende MIME-Typen. Überprüfen Sie, ob der MIME-Typ Ihrer Datei mit der Erweiterung übereinstimmt, bevor Sie sie senden.

### Dokumente {#documents}

Die folgenden Spezifikationen gelten für Template-Header (Dokumentformat), Antwort-Mediennachrichten und Dokumentnachrichten.

| Dokumenttyp | Dateitypen | Maximale Dateigröße |
|---|---|---|
| PDF | PDF | 100 MB |
| Microsoft Word | DOC, DOCX | 100 MB |
| Microsoft Excel | XLS, XLSX | 100 MB |
| Microsoft PowerPoint | PPT, PPTX | 100 MB |
| Klartext | TXT | 100 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dokumente" }

#### Hinweise

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- Untertitel sind optional und können maximal 1.024 Zeichen lang sein.
- Der Dateiname ist optional. WhatsApp verwendet die Dateierweiterung, um zu bestimmen, welches Dokumentsymbol in der Konversation angezeigt wird.
- Nur die aufgeführten Formate werden offiziell unterstützt. Andere Dateitypen können gesendet werden, es wird jedoch nicht garantiert, dass sie in WhatsApp korrekt dargestellt werden.

## Kurzreferenz: WhatsApp-Medienspezifikationen {#quick-reference-whatsapp-media-specifications}

| Medientyp | Dateitypen | Maximale Dateigröße | Untertitelverfügbarkeit |
|---|---|---|---|
| Bild | JPEG, PNG | 5 MB | Ja (maximal 1.024 Zeichen) |
| Video | MP4, 3GPP | 16 MB | Ja (maximal 1.024 Zeichen) |
| Audio (Sprache) | OGG (OPUS) | 16 MB | Nein |
| Audio (einfach) | AAC, AMR, MP3, M4A, OGG | 16 MB | Nein |
| Dokument | PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT | 100 MB | Ja (maximal 1.024 Zeichen) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Kurzreferenz: WhatsApp-Medienspezifikationen" }