Braze fügt ausgehenden Connected-Content-Anfragen die folgenden Header hinzu. Die meisten werden nur gesetzt, wenn Sie sie nicht bereits im Tag angegeben haben. Header, die Sie über `:headers`, Zugangsdaten oder Tag-Optionen bereitstellen, werden wie angegeben gesendet.

| Header | Wann Braze ihn setzt |
| --- | --- |
| `User-Agent` | Wenn Sie ihn nicht bereits gesetzt haben, sendet Braze `Braze Sender <version>`. Der Versions-String kann sich ändern. Wenn Sie Traffic nach `User-Agent` filtern, lassen Sie alle Werte zu, die mit `Braze Sender` beginnen. Um einen konsistenten Wert zu senden, setzen Sie `User-Agent` in `:headers`. |
| `X-Braze-Sender-Version` | Wird immer auf die Connected-Content-Sender-Version gesetzt. |
| `Accept-Encoding` | Wenn Sie ihn nicht bereits gesetzt haben, sendet Braze `gzip`. |
| `Authorization` | Wenn die URL einen Nutzernamen und ein Passwort enthält (`user:pass@host`), fügt Braze einen Basic-`Authorization`-Header hinzu, der aus diesen Zugangsdaten abgeleitet wird. Ein expliziter `Authorization`-Header überschreibt ihn. Bevorzugen Sie [`:basic_auth`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-basic-authentication) oder `:headers`, anstatt Zugangsdaten in die URL einzufügen. |
| `Host` | Hostname aus der Anfrage-URL (zum Beispiel `www.example.com` für `https://www.example.com/abc/123`), sofern Sie keinen `Host`-Header gesetzt haben. |
| `Content-Length` | Größe des Anfrage-Bodys in Bytes, wenn ein Body vorhanden ist. |
| `BrazeToBraze` | Wird nur für Anfragen an Braze-REST-Endpunkte auf `true` gesetzt. Wird für andere Ziele weggelassen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ausgehende Anfrage-Header, die Braze zu Connected Content hinzufügt" }