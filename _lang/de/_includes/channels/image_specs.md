{% if include.variable_name == "image behavior" %}


| Layout | Verhalten |
| --- | --- |
| Bild und Text | Hohe oder schmale Bilder werden verkleinert und horizontal zentriert. Breite Bilder werden am linken und rechten Rand abgeschnitten. |
| Nur Bild | Die Nachricht passt sich an die meisten Seitenverhältnisse an. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabelle" }

{% endif %}

{% if include.variable_name == "payload size" %}

Wir empfehlen die folgenden Nutzlastgrößen:

| Nachrichtensystem | Empfohlene Nutzlast |
| --- | --- |
| iOS (vor iOS 8) | 0.256 KB |
| iOS (nach iOS 8) | 2 KB |
| Android (FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabelle" }

{% endif %}

{% if include.variable_name == "in-app messages" %}

Modale In-App-Nachrichten sind so konzipiert, dass sie sich bestmöglich und mit dem höchsten Füllgrad an das Gerät anpassen, während sie gleichzeitig die Größe und das Verhältnis des von Ihnen gewählten Bildes oder Textes für Ihre Nachricht beibehalten.

Es gibt zwar keine Beschränkungen für die Anzahl der Textzeichen, die Sie in einer In-App-Nachricht verwenden können (einschließlich Buttons, Überschrift, Haupttext und weiterer Elemente), aber wir empfehlen, die Textmenge moderat zu halten. Zu viel Text führt dazu, dass Nutzer:innen die Nachricht erweitern und scrollen müssen.

Alle In-App-Nachrichten haben eine empfohlene Bildgröße von 500 KB, eine maximale Bildgröße von 5 MB und unterstützen die Dateitypen PNG, JPEG und GIF. WebP-Bilder werden nicht von allen Geräten oder Browsern unterstützt. Wir empfehlen, WebP-Bilder in das PNG- oder JPEG-Format zu konvertieren, bevor Sie sie zu In-App-Nachrichten hinzufügen.

{% alert note %}
SVG-Bilder werden für In-App-Nachrichten nicht unterstützt, da sie nicht auf allen Plattformen zuverlässig gerendert werden. Verwenden Sie stattdessen PNG, JPEG oder GIF.
{% endalert %}

{% tabs %}
{% tab Hochformat %}

| Typ | Seitenverhältnis | Bildqualität | Anmerkungen |
| --- | --- | --- | --- |
| Hochformat Vollbild mit Text | 6:5 | Hohe Auflösung 1200 x 1000 px <br>Mindestauflösung 600 x 500 px | Der Beschnitt kann an allen Seiten erfolgen, aber das Bild füllt immer die oberen 50 % des Ansichtsfensters aus. |
| Hochformat Vollbild (nur Bild, mit oder ohne Buttons) | 3:5 | Hohe Auflösung 1200 x 2000 px <br> Mindestauflösung 600 x 1000 px | Bei größeren Geräten kann es am linken und rechten Rand zu Beschneidungen kommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabelle" }

{% endtab %}
{% tab Querformat %}

| Typ | Seitenverhältnis | Bildqualität | Anmerkungen |
| --- | --- | --- | --- |
| Querformat Vollbild mit Text | 10:3 | Hohe Auflösung 2000 x 600 px <br>Mindestauflösung 1000 x 300 px | Der Beschnitt kann an allen Seiten erfolgen, aber das Bild füllt immer die oberen 50 % des Ansichtsfensters aus. |
| Querformat Vollbild (nur Bild, mit oder ohne Buttons) | 5:3 | Hohe Auflösung 2000 x 600 px <br> Mindestauflösung 1000 x 600 px | Bei größeren Geräten kann es am linken und rechten Rand zu Beschneidungen kommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabelle" }

{% endtab %}
{% tab Slideup %}

| Typ | Seitenverhältnis | Bildqualität | Anmerkungen |
| --- | --- | --- | --- |
| Slideup | 1:1 | Hohe Auflösung 150 x 150 px <br> Mindestauflösung 50 x 50 px | Bilder mit unterschiedlichen Seitenverhältnissen passen in einen quadratischen Bildcontainer, ohne dass sie beschnitten werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabelle" }

{% endtab %}
{% tab Modal %}

| Typ | Seitenverhältnis | Bildqualität | Anmerkungen |
| --- | --- | --- | --- |
| Modal (nur Bild) | 1:1 | Empfohlene maximale Auflösung: 1200 x 2000 px <br> Mindestauflösung: 600 x 600 px | Die Nachricht passt sich an die meisten Seitenverhältnisse an. Die empfohlene maximale Auflösung hat ein Seitenverhältnis von 3:5, was möglicherweise nicht zu optimalen Ergebnissen führt. Größere Bilder sind zwar verwendbar, können jedoch zu längeren Ladezeiten führen. <br> Das ideale Seitenverhältnis für Bilder ist 1:1. Wird dieses Verhältnis nicht eingehalten, kann dies beim Hochladen eine Warnung auslösen. Diese Warnung ist ein Vorschlag für optimale Ergebnisse und verhindert nicht das Hochladen größerer Bilder. |
| Modal mit Text | 29:10 | Hohe Auflösung 1450 x 500 px <br> Mindestauflösung 600 x 205 px | Hohe Bilder werden verkleinert und horizontal zentriert. Breite Bilder werden am linken und rechten Rand abgeschnitten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabelle" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Das Rendering von In-App-Nachrichten im Web SDK or Software-Development-Kit kann durch benutzerdefinierte Textgrößeneinstellungen des Browsers beeinflusst werden. Nutzer:innen mit benutzerdefinierter Textgrößenskalierung können geringfügige Darstellungsprobleme feststellen, wie z. B. einen 1-px-Spalt am Rand eines modalen Bildes. Beim Testen und in der Vorschau von In-App-Nachrichten empfehlen wir, die Standard-Textgrößeneinstellungen des Browsers zu verwenden, um eine möglichst genaue Darstellung zu erhalten.
{% endalert %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Nachrichtentyp | Maximale Nachrichtenlänge | Maximale Titellänge |
| --- | --- | --- |
| iOS-Sperrbildschirm | 175 Zeichen | 43 Zeichen |
| iOS-Benachrichtigung | 175 Zeichen | 43 Zeichen |
| iOS-Banneralarm | 85 Zeichen | 43 Zeichen |
| Android-Sperrbildschirm | 49 Zeichen | 43 Zeichen |
| Android-Benachrichtigungsschublade | 597 Zeichen | 43 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tabelle" }

Die empfohlene Bildgröße für alle Push-Bilder beträgt 500 KB.

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="Tabelle">
  <thead>
    <tr>
      <th>Bildtyp</th>
      <th>Seitenverhältnis</th>
      <th>Maximale Pixel</th>
      <th>Maximale Bildgröße</th>
      <th>Dateitypen</th>
      <th>Anmerkungen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1 (empfohlen)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>Seit Januar 2020 können iOS-Rich-Push-Benachrichtigungen Bilder mit einer Größe von 1038 x 1038 px verarbeiten, solange sie unter 10 MB liegen. Wir empfehlen jedoch, eine möglichst kleine Dateigröße zu verwenden. In der Praxis kann das Versenden großer Dateien sowohl unnötigen Netzwerkstress verursachen als auch dazu führen, dass es häufiger zu Download-Timeouts kommt.<br><br>Weitere Informationen finden Sie unter <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">iOS Rich-Benachrichtigungen</a>.</td>
    </tr>
    <tr>
      <td>Android-Push-Symbol</td>
      <td>1:1</td>
      <td>N/A</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Android erweitertes Benachrichtigungsbild</td>
      <td>2:1</td>
      <td><b>Klein:</b><br>512 x 256<br><br><b>Mittel:</b><br>1024 x 512<br><br><b>Groß:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td>Wird in <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">Android Rich-Benachrichtigungen</a> verwendet.</td>
    </tr>
    <tr>
      <td>Android-Inline-Bild</td>
      <td>3:2</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>PNG, JPEG</td>
      <td>Weitere Einzelheiten finden Sie unter <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Android-Inline-Image-Push</a>.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 aria-label="Tabelle" }

{% endif %}

{% if include.variable_name == "email" %}

| E-Mail-Typ | Empfohlene Maximalwerte |
| --- | --- |
| Nur Text | 25 KB |
| Text mit Bildern | 60 KB |
| E-Mail-Breite | 600 px |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabelle" }

| Bildspezifikationen | Empfohlene Maximalwerte |
| --- | --- |
| Größe | 5 MB |
| Breite | Header: 600 px<br>Textkörper: 480 px |
| Dateitypen | PNG, JPEG, GIF<br><br> Die Unterstützung für WebP-Bilder variiert je nach E-Mail-Client. Um eine zuverlässige Darstellung zu gewährleisten, konvertieren Sie WebP-Bilder in das PNG- oder JPEG-Format, bevor Sie sie zu E-Mail-Nachrichten hinzufügen.<br><br>SVG-Bilder werden für E-Mail-Nachrichten aufgrund von Kompatibilitätsproblemen mit Gmail und anderen großen E-Mail-Clients nicht empfohlen. Verwenden Sie stattdessen PNG, JPEG oder GIF. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabelle" }

| Textspezifikationen | Empfohlene Maximalwerte |
| --- | --- |
| Länge der Betreffzeile | 35 Zeichen<br>6 bis 10 Wörter |
| `"From: Name"` Länge | 25 Zeichen |
| Preheader-Länge | 85 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabelle" }

{% endif %}

{% if include.variable_name == "content cards" %}

| Kartentyp | Seitenverhältnis     | Bildqualität       |
| --------- | ---------------- | ------------------- |
| Klassisch   | Seitenverhältnis 1:1 | 60 x 60&nbsp;px        |
| Mit Beschriftung | Seitenverhältnis 4:3 | 600&nbsp;px Mindestbreite |
| Banner    | Beliebiges Seitenverhältnis | 600&nbsp;px Mindestbreite |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tabelle" }

Weitere Informationen finden Sie unter [Kreative Details für Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/creative_details).

{% endif %}

{% if include.variable_name == "Kurzmitteilungsdienst or SMS and mms" %}

MMS-Nachrichten unterstützen ein einzelnes Bild pro Nachricht. Nur MMS-fähige Abo-Gruppen können Bilder versenden.

| Eigenschaft | Empfehlung |
| --- | --- |
| Größe | 600&nbsp;KB oder kleiner für eine zuverlässige Zustellung durch den Mobilfunkanbieter. Der Composer blockiert Uploads, die größer als 1&nbsp;MB sind. |
| Dateitypen | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kurzmitteilungsdienst or SMS und MMS" }

Informationen zu den Dateigrößenbeschränkungen und dem Durchsatz der Mobilfunkanbieter finden Sie unter [MMS-Nachrichtenlimits und Durchsatz]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup#mms-message-limits-and-throughput).

{% endif %}

{% if include.variable_name == "WhatsApp images" %}

Diese Spezifikationen gelten für Template-Header, Antwort-Mediennachrichten und Bildnachrichten.

| Eigenschaft | Spezifikationen | Anmerkungen |
|---|---|---|
| Unterstützte Formate | JPEG, PNG | Meta unterstützt offiziell nur JPEG und PNG für Bildnachrichten. WebP wird nur für Sticker unterstützt (nicht für Standard-Bildnachrichten). |
| Maximale Dateigröße | 5 MB | |
| Farbmodus | 8-Bit, RGB oder RGBA | |
| Beschriftung (nur Bildnachrichten) | Optional; maximal 1.024 Zeichen | |
| Empfohlene Abmessungen | 1.125 × 600 px | Wir empfehlen JPEG- oder PNG-Bilder mit einer Größe von 1.125 × 600 px (1,91:1) für eine konsistente Darstellung auf allen Geräten und die Einhaltung der Meta-Anforderungen. |
| Empfohlenes Seitenverhältnis | 1,91:1 (breit) | Quadratische (1:1) und breite (16:9) Formate werden akzeptiert, aber Bilder können je nach Gerät der Nutzer:innen beschnitten oder vergrößert werden.<br><br> Bei Karussell-Karten werden Header-Bilder von WhatsApp automatisch auf ein breites Verhältnis zugeschnitten, es sei denn, es gibt keinen Textkörper – in diesem Fall wird das Bild quadratisch dargestellt.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tabelle" }

{% endif %}

{% if include.variable_name == "WhatsApp videos" %}

Die folgenden Spezifikationen gelten für Template-Header, Antwort-Mediennachrichten, Videonachrichten und Karussell-Karten-Header.

| Eigenschaft | Spezifikationen |
|---|---|
| Unterstützte Formate | MP4, 3GPP |
| Dateigröße | Maximal 16 MB |
| Video-Codec | Nur H.264 |
| Audio-Codec | Nur AAC |
| Audio-Streams | Einzelner Audio-Stream oder kein Audio-Stream |
| Beschriftung (nur Videonachrichten) | Optional; maximal 1.024 Zeichen |
| Empfohlenes Seitenverhältnis | 1,91:1 (breit) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabelle" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

{% endif %}