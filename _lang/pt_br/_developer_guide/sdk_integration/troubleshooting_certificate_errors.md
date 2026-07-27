---
page_order: 1.35
nav_title: Erros de confiança de certificado
article_title: Solução de problemas de erros de confiança de certificado do SDK
description: "Solucione erros de confiança de certificado HTTPS que podem bloquear a inicialização do SDK da Braze em Android, Swift e outros SDKs."
---

# Solução de problemas de erros de confiança de certificado do SDK {#troubleshooting-sdk-certificate-trust-errors}

Se a inicialização do SDK falhar com erros de confiança de certificado SSL ou TLS, isso geralmente significa que o dispositivo, simulador, navegador ou servidor não consegue validar a cadeia de certificados do endpoint da Braze.

Por exemplo, em Android ou outros ambientes baseados em JVM, você pode ver:

```
javax.net.ssl.SSLHandshakeException: java.security.cert.CertPathValidatorException: Trust anchor for certification path not found
```

Isso geralmente é um problema de configuração de rede ou de confiança de certificado no seu ambiente, e não um bug na integração SDK.

## Causas comuns {#common-causes}

- Um proxy corporativo, firewall ou ferramenta de inspeção de tráfego está interceptando o tráfego HTTPS com um certificado no qual o seu runtime não confia.
- Um certificado raiz ou intermediário necessário está ausente do armazenamento de confiança no dispositivo, simulador, navegador ou servidor.
- Configurações de segurança locais bloqueiam HTTPS de saída para os endpoints da Braze.
- Configurações de certificado ou segurança de transporte no nível do app bloqueiam a conexão.

## Etapas de solução de problemas {#troubleshooting-steps}

1. Confirme seu endpoint de SDK e o acesso à rede.
   - Verifique se você está usando o [endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) correto para o seu espaço de trabalho.
   - Verifique se o seu ambiente consegue alcançar esse endpoint via HTTPS.
2. Compare o comportamento em diferentes redes.
   - Teste em uma rede diferente (por exemplo, dados móveis em vez de Wi-Fi corporativo).
   - Se o problema ocorrer apenas em uma rede, a causa raiz provavelmente é a configuração de proxy ou firewall.
3. Valide sua configuração de confiança.
   - Confirme que os certificados raiz e intermediários necessários estão instalados e são confiáveis no runtime onde o SDK está sendo executado.
   - Se o seu ambiente usa autoridades de certificação personalizadas, confirme que esses certificados estão distribuídos corretamente.
4. Revise as configurações de segurança da plataforma.
   - Se o seu app ou ambiente possui regras explícitas de transporte ou certificado, confirme que essas configurações permitem requisições HTTPS para os endpoints da Braze.
5. Trabalhe com sua equipe de rede ou segurança.
   - Compartilhe o erro completo e o timestamp para que possam verificar as cadeias de certificados, as configurações de inspeção TLS e as regras de allowlist.

{% alert note %}
Como o tráfego do SDK da Braze usa HTTPS, falhas de confiança de certificado podem afetar qualquer SDK da Braze (incluindo Android, Swift, Web, React Native, Flutter, Unity e Cordova) em ambientes com políticas de rede restritivas.
{% endalert %}