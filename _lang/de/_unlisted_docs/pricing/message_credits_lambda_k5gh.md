---
nav_title: Message Credits – Lambda
permalink: "/message_credits_lambda_k5gh/"
hidden: true
noindex: true
hide_toc: true
---

# Message Credits – Lambda (vertraulich) {#message-credits-lambda-confidential}

> Message Credits ist die produktübergreifende Paketstruktur von Braze für unsere nativen Angebote Agent Console, SMS, MMS, RCS, WhatsApp und LINE. Message Credits bieten ein flexibles und transparentes Erlebnis bei der Nutzung der Braze-Messaging-Kanäle und bestimmter KI-Features. Credits gewähren Ihnen Zugang zu allen Kanälen, die in der Tabelle auf dieser Seite aufgeführt sind.

{% alert note %}
Verschiedene Produkte verwenden unterschiedliche Maßeinheiten im Reporting.<br><br>
<b>Agent Console:</b> Invocations<br>
<b>SMS:</b> Segments<br>
<b>MMS:</b> Sends<br>
<b>WhatsApp:</b> Zugestellte Nachrichten<br>
<b>RCS:</b> Zugestellte Segments, zugestellte Sends<br>
<b>LINE:</b> Sends<br>
<b>KakaoTalk:</b> Sends<br>

Darüber hinaus werden Carrier-Gebühren für SMS, MMS und RCS separat (nachträglich) abgerechnet und sind nicht Bestandteil dieser Message-Credits-SKU.
{% endalert %}

## Definitionen {#definitions}

Die Spaltendefinitionen lauten wie folgt:

|---------|-------------------------------------------------|
| **Ziel** | Spezifische Endregion, Land oder Art der Aktion, die über die Braze-Plattform gesendet wird |
| **Credits pro 1 Versand** | Genaue Anzahl der Message Credits für einen Versand<br> (Credits pro Versand = Credit-Verhältnis × Zielmultiplikator) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## Credit-Verhältnistabelle für Message Credits – Lambda {#credit-ratio-table-for-message-credits-lambda}

{% details Zum Aufklappen klicken %}
<table class="credits-table" aria-label="Credit-Verhältnistabelle für Message Credits – Lambda">
    <colgroup>
        <col span="3">
        <col class="col-highlight">
    </colgroup>
    <thead>
    <tr>
        <th><b>Kanal</b></th>
        <th><b>Ziel</b></th>
        <th class="credits-column"><b>Credits pro 1 Versand</b></th>
    </tr>
    <tr>
        <td>Agent Console</td>
        <td>Braze Auto</td>
        <td>1.60</td>
    </tr>
    </thead>
    <tbody>
<tr>
        <td>Agent Console</td>
        <td>BYO LLM API Key</td>
        <td>0.16</td>
    </tr>
    <tr>
        <td>SMS – US / CA</td>
        <td>Kanada</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS – US / CA</td>
        <td>Kanada Toll Free</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS – US / CA</td>
        <td>Vereinigte Staaten</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS – US / CA</td>
        <td>Vereinigte Staaten Toll Free</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>MMS – US / CA</td>
        <td>Kanada Langcode</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>MMS – US / CA</td>
        <td>Kanada Shortcode</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>MMS – US / CA</td>
        <td>Kanada Toll Free</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>MMS – US / CA</td>
        <td>Vereinigte Staaten</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>MMS – US / CA</td>
        <td>Vereinigte Staaten Toll Free</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Abchasien</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Afghanistan</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Albanien</td>
        <td>10.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Algerien</td>
        <td>32.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Amerikanisch-Samoa</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Andorra</td>
        <td>11.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Angola</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Anguilla</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Antigua und Barbuda</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Argentinien</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Armenien</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Aruba</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Australien SMS</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Österreich</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Aserbaidschan</td>
        <td>33.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Bahamas</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Bahrain</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Bangladesch</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Barbados</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Belarus</td>
        <td>32.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Belgien</td>
        <td>14.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Belize</td>
        <td>16.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Benin</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Bermuda</td>
        <td>10.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Bhutan</td>
        <td>25.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Bolivien</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Bosnien und Herzegowina</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Botswana</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Brasilien</td>
        <td>2.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Brunei</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Bulgarien</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Burkina Faso</td>
        <td>14.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Burundi</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kambodscha</td>
        <td>24.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kamerun</td>
        <td>11.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kap Verde</td>
        <td>14.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Karibische Niederlande</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kaimaninseln</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Zentralafrikanische Republik</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Tschad</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Chile</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>China</td>
        <td>1.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kolumbien</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Komoren</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kongo</td>
        <td>6.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Cookinseln</td>
        <td>6.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Costa Rica</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kroatien</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kuba</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Curaçao</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Zypern</td>
        <td>2.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Tschechische Republik</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Dänemark</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Dschibuti</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Dominica</td>
        <td>9.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Dominikanische Republik</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>DR Kongo</td>
        <td>14.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Ecuador</td>
        <td>22.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Ägypten</td>
        <td>21.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>El Salvador</td>
        <td>8.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Äquatorialguinea</td>
        <td>5.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Eritrea</td>
        <td>14.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Estland</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Eswatini</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Äthiopien</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Falklandinseln</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Färöer</td>
        <td>2.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Fidschi</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Finnland</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Frankreich</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Französisch-Guayana</td>
        <td>20.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Französisch-Polynesien</td>
        <td>15.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Gabun</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Gambia</td>
        <td>12.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Georgien</td>
        <td>21.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Deutschland</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Ghana</td>
        <td>17.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Gibraltar</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Griechenland</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Grönland</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Grenada</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Guadeloupe</td>
        <td>20.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Guam</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Guatemala</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Guernsey</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Guinea</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Guinea-Bissau</td>
        <td>14.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Guyana</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Haiti</td>
        <td>11.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Honduras</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Hongkong</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Ungarn</td>
        <td>11.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Island</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Indien</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Indonesien</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Iran</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Irak</td>
        <td>23.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Irland</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Isle of Man</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Israel</td>
        <td>15.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Italien</td>
        <td>8.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Elfenbeinküste</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Jamaika</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Japan</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Jersey</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Jordanien</td>
        <td>25.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kasachstan</td>
        <td>25.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kenia</td>
        <td>22.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kiribati</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Republik Korea</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kosovo</td>
        <td>9.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kuwait</td>
        <td>24.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Kirgisistan</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Laos (VDR)</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Lettland</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Libanon</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Lesotho</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Liberia</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Libyen</td>
        <td>26.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Liechtenstein</td>
        <td>3.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Litauen</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Luxemburg</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Macao</td>
        <td>3.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Madagaskar</td>
        <td>22.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Malawi</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Malaysia</td>
        <td>7.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Malediven</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Mali</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Malta</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Martinique</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Mauretanien</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Mauritius</td>
        <td>18.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Mayotte</td>
        <td>23.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Mexiko</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Mikronesien</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Moldau</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Monaco</td>
        <td>16.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Mongolei</td>
        <td>19.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Montenegro</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Montserrat</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Marokko</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Mosambik</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Myanmar</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Namibia</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Nauru</td>
        <td>11.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Nepal</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Niederlande</td>
        <td>18.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Neukaledonien</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Neuseeland</td>
        <td>14.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Nicaragua</td>
        <td>12.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Niger</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Nigeria</td>
        <td>21.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Nordmazedonien</td>
        <td>3.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Nordzypern</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Norwegen</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Oman</td>
        <td>16.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Pakistan</td>
        <td>22.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Palau</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Panama</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Papua-Neuguinea</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Paraguay</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Peru</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Philippinen</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Polen</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Portugal</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Puerto Rico</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Katar</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Réunion/Mayotte</td>
        <td>11.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Rumänien</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Russland</td>
        <td>18.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Ruanda</td>
        <td>12.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>St. Kitts und Nevis</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>St. Lucia</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Saint-Pierre und Miquelon</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>St. Vincent und die Grenadinen</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Samoa</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>São Tomé und Príncipe</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Saudi-Arabien</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Senegal</td>
        <td>20.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Serbien</td>
        <td>8.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Seychellen</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Sierra Leone</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Singapur</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Sint Maarten</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Slowakei</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Slowenien</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Salomonen</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Somalia</td>
        <td>17.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Südafrika</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Südossetien</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Südsudan</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Spanien</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Sri Lanka</td>
        <td>25.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Sudan</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Suriname</td>
        <td>7.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Schweden</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Schweiz</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Taiwan</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Tadschikistan</td>
        <td>34.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Tansania</td>
        <td>16.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Thailand</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Timor-Leste</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Togo</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Tonga</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Trinidad und Tobago</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Tunesien</td>
        <td>22.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Türkei</td>
        <td>0.50</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Turkmenistan</td>
        <td>19.70</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Turks- und Caicosinseln</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Uganda</td>
        <td>19.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Ukraine</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Vereinigte Arabische Emirate</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Vereinigtes Königreich</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Uruguay</td>
        <td>7.10</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Usbekistan</td>
        <td>35.20</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Vanuatu</td>
        <td>14.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Venezuela</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Vietnam</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Britische Jungferninseln</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Wallis und Futuna</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Jemen</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Sambia</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>SMS / MMS – Global</td>
        <td>Simbabwe</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Argentina Authentication</td>
        <td>7.67</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Argentina Marketing</td>
        <td>16.39</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Argentina Marketing - Optimized Delivery</td>
        <td>16.39</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Argentina Utility</td>
        <td>7.67</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Brazil Authentication</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Brazil Marketing</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Brazil Marketing - Optimized Delivery</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Brazil Utility</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Chile Authentication</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Chile Marketing</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Chile Marketing - Optimized Delivery</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Chile Utility</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Colombia Authentication</td>
        <td>0.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Colombia Marketing</td>
        <td>3.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Colombia Marketing - Optimized Delivery</td>
        <td>3.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Colombia Utility</td>
        <td>0.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Authentication</td>
        <td>1.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Authentication International</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Marketing</td>
        <td>28.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Marketing - Optimized Delivery</td>
        <td>28.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Utility</td>
        <td>1.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>France Authentication</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>France Marketing</td>
        <td>37.99</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>France Marketing - Optimized Delivery</td>
        <td>37.99</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>France Utility</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Germany Authentication</td>
        <td>14.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Germany Marketing</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Germany Marketing - Optimized Delivery</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Germany Utility</td>
        <td>14.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Authentication</td>
        <td>0.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Authentication International</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Marketing</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Marketing - Optimized Delivery</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Utility</td>
        <td>0.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Authentication</td>
        <td>6.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Authentication International</td>
        <td>36.08</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Marketing</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Marketing - Optimized Delivery</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Utility</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Israel Authentication</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Israel Marketing</td>
        <td>9.36</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Israel Marketing - Optimized Delivery</td>
        <td>9.36</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Israel Utility</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Italy Authentication</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Italy Marketing</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Italy Marketing - Optimized Delivery</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Italy Utility</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Authentication</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Authentication International</td>
        <td>11.09</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Marketing</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Marketing - Optimized Delivery</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Utility</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Mexico Authentication</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Mexico Marketing</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Mexico Marketing - Optimized Delivery</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Mexico Utility</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Netherlands Authentication</td>
        <td>13.26</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Netherlands Marketing</td>
        <td>42.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Netherlands Marketing - Optimized Delivery</td>
        <td>42.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Netherlands Utility</td>
        <td>13.26</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Authentication</td>
        <td>1.78</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Authentication International</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Marketing</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Marketing - Optimized Delivery</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Utility</td>
        <td>1.78</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>North America Authentication</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>North America Marketing</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>North America Marketing - Optimized Delivery</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>North America Utility</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Other Authentication</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Other Marketing</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Other Marketing - Optimized Delivery</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Other Utility</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Authentication</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Authentication International</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Marketing</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Marketing - Optimized Delivery</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Utility</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Peru Authentication</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Peru Marketing</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Peru Marketing - Optimized Delivery</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Peru Utility</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Africa Authentication</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Africa Marketing</td>
        <td>5.97</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Africa Marketing - Optimized Delivery</td>
        <td>5.97</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Africa Utility</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Asia Pacific Authentication</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Asia Pacific Marketing</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Asia Pacific Marketing - Optimized Delivery</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Asia Pacific Utility</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Central & Eastern Europe Authentication</td>
        <td>5.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Central & Eastern Europe Marketing</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Central & Eastern Europe Marketing - Optimized Delivery</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Central & Eastern Europe Utility</td>
        <td>5.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Latin America Authentication</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Latin America Marketing</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Latin America Marketing - Optimized Delivery</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Latin America Utility</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Middle East Authentication</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Middle East Marketing</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Middle East Marketing - Optimized Delivery</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Middle East Utility</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Western Europe Authentication</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Western Europe Marketing</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Western Europe Marketing - Optimized Delivery</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Western Europe Utility</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Russia Authentication</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Russia Marketing</td>
        <td>21.28</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Russia Marketing - Optimized Delivery</td>
        <td>21.28</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Russia Utility</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Authentication</td>
        <td>3.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Authentication International</td>
        <td>15.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Marketing</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Marketing - Optimized Delivery</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Utility</td>
        <td>3.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Authentication</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Authentication International</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Marketing</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Marketing - Optimized Delivery</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Utility</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Spain Authentication</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Spain Marketing</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Spain Marketing - Optimized Delivery</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Spain Utility</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Turkey Authentication</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Turkey Marketing</td>
        <td>2.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Turkey Marketing - Optimized Delivery</td>
        <td>2.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Turkey Utility</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Authentication</td>
        <td>4.17</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Authentication International</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Marketing</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Marketing - Optimized Delivery</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Utility</td>
        <td>4.17</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Kingdom Authentication</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Kingdom Marketing</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Kingdom Marketing - Optimized Delivery</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Kingdom Utility</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>Line</td>
        <td>Alle Regionen</td>
        <td>0.15</td>
    </tr>
    <tr>
        <td>KakaoTalk</td>
        <td>Alle Regionen</td>
        <td>0.20</td>
    </tr>
    <tr>
        <td>Webhooks</td>
        <td>Standard</td>
        <td>0.08</td>
    </tr>
    <tr>
        <td>BYO SMS Connector</td>
        <td>Infobip – Alle Regionen</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>BYO SMS Connector</td>
        <td>Twilio – Alle Regionen</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Brazil - Basic</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Brazil - Single</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Colombia - Basic</td>
        <td>1.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Colombia - Single</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>France - Basic</td>
        <td>12.60</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>France - Single</td>
        <td>12.60</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Germany - Basic</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Germany - Single</td>
        <td>12.80</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Italy - Basic</td>
        <td>4.70</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Italy - Single</td>
        <td>6.70</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Mexico - Basic</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Mexico - Single</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Singapore - Basic</td>
        <td>4.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Singapore - Single</td>
        <td>8.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Spain - Basic</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Spain - Single</td>
        <td>13.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Sweden - Basic</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Sweden - Single</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United Kingdom - Basic</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United Kingdom - Single</td>
        <td>14.10</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United States - Basic - Deprecated</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United States - Rich</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United States - Rich Media</td>
        <td>1.30</td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% enddetails %}

------

## Details zur Agent Console {#agent-console-details}
Braze berechnet Message Credits für Agent-Console-Invocations, die über die Braze-Plattform gesendet werden. Eine Invocation wird protokolliert, wenn ein Agent einen Aufruf an ein LLM initiiert. Standardmäßig umfasst Ihr Vertrag zehntausend Invocations pro Laufzeitperiode Ihres Abonnements.

## Details zum SMS-/MMS-Kanal {#smsmms-channel-details}

### SMS-Nachrichtensegmente {#sms-segments}

SMS-Nachrichtensegmente sind die Einheit, mit der die SMS-Branche Nachrichten zählt. Ein Nachrichtensegment ist eine Gruppierung von bis zu einer definierten Zeichenanzahl (160 für GSM-7-Kodierung; 67 für UCS-2-Kodierung), die in einem einzelnen SMS-Versand gesendet wird. Wenn Sie eine SMS mit 161 Zeichen in GSM-7-Kodierung versenden, werden zwei (2) Nachrichtensegmente gesendet. Das Senden mehrerer Nachrichtensegmente führt zu zusätzlichen Kosten.

### MMS-Nachrichtensegmente {#mms-segments}

Für MMS liegt das Nachrichtenlimit bei 5 MB (einschließlich des Multimedia-Assets und der Nachrichtenkörpergröße). Um auf der sicheren Seite zu sein, empfiehlt Braze, 600 KB für Ihr Multimedia-Asset nicht zu überschreiten und gleichzeitig einen Nachrichtentext einzuschließen.

### RCS-Typen {#rcs-types}

RCS ist die nächste Generation von SMS und MMS. Es bietet die Vorteile eines direkten, stark engagierenden Kanals wie SMS – mit umfangreicheren Funktionen, die moderne Verbraucher:innen erwarten, wie Rich Content (Bilder, Videos, Dokumente), verifizierter und gebrandeter Versand, interaktive Features wie vorgeschlagene Antworten und Aktionen und mehr.

- Die RCS-Abrechnung basiert auf zwei verschiedenen Nachrichtentypen (mit Unterscheidungen für die USA):
    - **Basic RCS:** Nur Text, bis zu 160 Zeichen
    - **Single RCS:** Nachrichten mit Rich Content oder reine Textnachrichten mit mehr als 160 Zeichen
    - **Rich RCS (nur USA):** Nur Text, kann begrenzte Vorschläge/Buttons enthalten (quickReply, dialPhone, openURL ohne Webview), segmentiert pro 160 UTF-8-Bytes
    - **Rich Media RCS (nur USA):** Beliebige Medien ODER Text mit umfangreicheren Vorschlägen/Buttons (Webview, Standort, Kalender usw.), wird als eine Nachricht gezählt

## Details zum WhatsApp-Kanal {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## Details zu weiteren Kanälen {#additional-channel-details}

### Webhooks

Webhooks wurden am 9. Dezember 2024 in die Message Credits aufgenommen. Braze berechnet Message Credits für alle Webhooks, die über die Braze-Plattform gesendet werden. Standardmäßig umfasst Ihr Vertrag hunderttausend Webhooks pro Laufzeitperiode Ihres Abonnements. Zusätzliche Webhooks werden gemäß Ihrem Bestellformular berechnet.

### Bring-your-own (BYO) SMS-Konnektoren {#bring-your-own-byo-sms-connectors}

Braze ermöglicht es Kund:innen, Drittanbieter zu integrieren, um SMS-Nachrichten über das „BYO SMS Connector“-Modell zu versenden. Braze berechnet Message Credits für jede Nachricht, die über BYO-SMS-Konnektoren von der Braze-Plattform gesendet wird.

### LINE

Braze berechnet Message Credits für alle LINE-Nachrichten, die über die Braze-Plattform gesendet werden.

## Aufschlüsselung der Abrechnungsregionen {#billing-region-breakdown}

### Nordamerika {#north-america}

Vereinigte Staaten, Kanada

### Übriges Afrika {#rest-of-africa}

Algerien, Angola, Benin, Botswana, Burkina Faso, Burundi, Kamerun, Tschad, Kongo, Eritrea, Äthiopien, Gabun, Gambia, Ghana, Guinea-Bissau, Elfenbeinküste, Kenia, Lesotho, Liberia, Libyen, Madagaskar, Malawi, Mali, Mauretanien, Marokko, Mosambik, Namibia, Niger, Ruanda, Senegal, Sierra Leone, Somalia, Südsudan, Sudan, Swasiland, Tansania, Togo, Tunesien, Uganda, Sambia

### Übriger Asien-Pazifik-Raum {#rest-of-asia-pacific}

Afghanistan, Australien, Bangladesch, Kambodscha, China, Japan, Laos, Mongolei, Nepal, Neuseeland, Papua-Neuguinea, Philippinen, Sri Lanka, Taiwan, Tadschikistan, Thailand, Turkmenistan, Usbekistan, Vietnam

### Übriges Mittel- und Osteuropa {#rest-of-central-eastern-europe}

Albanien, Armenien, Aserbaidschan, Belarus, Bulgarien, Kroatien, Tschechische Republik, Georgien, Griechenland, Lettland, Litauen, Mazedonien, Moldau, Serbien, Slowakei, Slowenien, Ukraine

### Übriges Lateinamerika {#rest-of-latin-america}

Bolivien, Costa Rica, Dominikanische Republik, Ecuador, El Salvador, Guatemala, Haiti, Honduras, Jamaika, Nicaragua, Panama, Paraguay, Puerto Rico, Uruguay, Venezuela

### Übriger Naher Osten {#rest-of-middle-east}

Bahrain, Irak, Jordanien, Kuwait, Libanon, Oman, Jemen

### Übriges Westeuropa {#rest-of-western-europe}

Österreich, Belgien, Dänemark, Finnland, Irland, Norwegen, Portugal, Schweden, Schweiz