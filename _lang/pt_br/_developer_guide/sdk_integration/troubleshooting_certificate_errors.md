---
page_order: 1.35
nav_title: Erros de confiança de certificado
article_title: Solução de problemas de erros de confiança de certificado do SDK or kit de desenvolvimento de software
description: "Solucione erros de confiança de certificado HTTPS que podem bloquear a inicialização do SDK or kit de desenvolvimento de software da Braze em Android, Swift e outros SDKs."
---

# Solução de problemas de erros de confiança de certificado do SDK or kit de desenvolvimento de software {#troubleshooting-sdk-certificate-trust-errors}

Se a inicialização do SDK or kit de desenvolvimento de software falhar com erros de confiança de certificado SSL ou TLS, isso geralmente significa que o dispositivo, simulador, navegador ou servidor não consegue validar a cadeia de certificados do endpoint da Braze.

Por exemplo, em Android ou outros ambientes baseados em JVM, você pode ver:

```
javax.net.ssl.SSLHandshakeException: java.security.cert.CertPathValidatorException: Trust anchor for certification path not found
```

Isso geralmente é um problema de configuração de rede ou de confiança de certificado no seu ambiente, e não um bug na integração SDK or kit de desenvolvimento de software.

## Causas comuns {#common-causes}

- Um proxy corporativo, firewall ou ferramenta de inspeção de tráfego está interceptando o tráfego HTTPS com um certificado que seu ambiente de execução não confia.
- Um certificado raiz ou intermediário necessário está ausente do armazenamento de confiança no dispositivo, simulador, navegador ou servidor.
- Configurações de segurança locais bloqueiam HTTPS de saída para os endpoints da Braze.
- Configurações de certificado ou segurança de transporte no nível do app bloqueiam a conexão.

## Etapas de solução de problemas {#troubleshooting-steps}

1. Confirme o endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software e o acesso à rede.
   - Verifique se você está usando o [endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) correto para o seu espaço de trabalho.
   - Verifique se o seu ambiente consegue alcançar esse endpoint via HTTPS.
2. Compare o comportamento em diferentes redes.
   - Teste em uma rede diferente (por exemplo, dados móveis em vez de Wi-Fi corporativo).
   - Se o problema ocorrer apenas em uma rede, a causa raiz provavelmente é a configuração de proxy ou firewall.
3. Valide a configuração de confiança.
   - Confirme se os certificados raiz e intermediários necessários estão instalados e são confiáveis no ambiente de execução onde o SDK or kit de desenvolvimento de software está rodando.
   - Se o seu ambiente usa autoridades certificadoras personalizadas, confirme se esses certificados estão distribuídos corretamente.
4. Revise as configurações de segurança da plataforma.
   - Se o seu app ou ambiente possui regras explícitas de transporte ou certificado, confirme se essas configurações permitem requisições HTTPS para os endpoints da Braze.
5. Trabalhe com sua equipe de rede ou segurança.
   - Compartilhe o erro completo e o timestamp para que possam verificar as cadeias de certificados, as configurações de inspeção TLS e as regras de lista de permissões.

{% alert note %}
Como o tráfego do SDK or kit de desenvolvimento de software da Braze usa HTTPS, falhas de confiança de certificado podem afetar qualquer SDK or kit de desenvolvimento de software da Braze (incluindo Android, SWIFT, web, React Native, Flutter, Unity e Cordova) em ambientes com políticas de rede restritivas.
{% endalert %}