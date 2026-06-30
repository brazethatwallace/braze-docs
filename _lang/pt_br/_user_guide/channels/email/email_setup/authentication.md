---
nav_title: Autenticação de e-mail
article_title: Autenticação de e-mail
page_order: 2
page_type: reference
description: "Este artigo de referência aborda a autenticação de e-mail, um conjunto de técnicas destinadas a equipar seus e-mails com informações verificáveis sobre sua origem."
channel: email

---

# Autenticação de e-mail {#email-authentication}

> A autenticação de e-mail é um conjunto de técnicas que equipam seus e-mails com informações verificáveis sobre sua origem.<br><br>A autenticação adequada é crucial para que os provedores de acesso à internet (ISPs) reconheçam você como remetente de e-mails desejáveis e entreguem seus e-mails imediatamente. Sem autenticação, presume-se que seu alcance seja fraudulento.

{% alert note %}
Nenhuma coordenação especial com a Braze é necessária para o **BIMI** (Brand Indicators for Message Identification). Os registros DNS e certificados necessários são gerenciados do seu lado.
{% endalert %}

## Métodos de autenticação {#methods-of-authentication}

### Sender Policy Framework (SPF) {#spf}

Esse método confirma que seu endereço IP de envio de e-mail da Braze está autorizado a enviar e-mails em seu nome. O SPF é a autenticação básica e é realizado por meio da publicação dos registros de texto nas configurações de DNS. O servidor receptor verificará os registros DNS e determinará se eles são autênticos. Esse método foi criado para validar o remetente do e-mail.

A Braze configura seu registro SPF quando configuramos seus IPs e domínios. Além de adicionar os registros DNS que fornecemos, você não precisa tomar mais nenhuma ação.

### Domain Keys Identified Mail (DKIM) {#dkim}

Esse método confirma que seu domínio de envio de e-mail da Braze está autorizado a enviar e-mails em seu nome. Esse método foi projetado para validar a autenticidade do remetente e garantir que a integridade da mensagem seja preservada. Ele também usa assinaturas digitais criptográficas individuais para que os provedores de acesso à internet possam ter certeza de que o e-mail entregue é o mesmo que você enviou.

A Braze assina o e-mail com sua chave privada secreta. Os ISPs verificam a assinatura usando sua chave pública, que está armazenada no seu registro DNS personalizado. Nenhuma assinatura é exatamente igual, e somente sua chave pública pode verificar com sucesso a assinatura da sua chave privada.

A Braze configura seu registro DKIM quando configuramos seus IPs e domínios. Além de adicionar os registros DNS que fornecemos, você não precisa tomar mais nenhuma ação.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC) {#dmarc}

O [Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) é um protocolo de autenticação de e-mail para que remetentes comprovem a legitimidade de suas mensagens, o que aumenta a confiança do provedor de caixa de e-mail receptor e incentiva a aceitação do e-mail. O DMARC permite que remetentes de e-mail especifiquem como lidar com e-mails que não foram autenticados usando Sender Policy Framework (SPF) ou Domain Keys Identified Mail (DKIM). Isso é feito verificando se as checagens de SPF e DKIM foram aprovadas.

Os remetentes instruem os provedores de caixa de e-mail sobre como lidar com e-mails que falham nas verificações de assinatura ou autenticação. Falhas podem indicar falsificação. Você pode instruir os provedores a rejeitar ou colocar em quarentena e-mails que falharam e a enviar relatórios automatizados. Isso ajuda os provedores a identificar spammers, bloquear e-mails maliciosos, minimizar falsos positivos e melhorar a transparência dos relatórios de autenticação.

#### Como funciona {#how-it-works}

Para implementar o DMARC, você precisa publicar um registro DMARC no seu Domain Naming System (DNS). Este é um registro TXT que expressa publicamente a política do seu domínio de e-mail após verificar o status de SPF e DKIM. O DMARC autentica se o SPF ou o DKIM, ou ambos, são aprovados. Isso é chamado de alinhamento DMARC.

Um registro DMARC também instrui os servidores de e-mail a enviar relatórios XML de volta para o endereço de e-mail de relatório listado no registro DMARC. Esses relatórios fornecem insights sobre como seu e-mail está se movendo pelo ecossistema e permitem que você identifique tudo que está tentando usar seu domínio de e-mail para enviar comunicações por e-mail.

Defina uma política DMARC no domínio raiz para que ela se aplique a todos os subdomínios. Isso evita configurações adicionais em subdomínios atuais e futuros. Você pode definir uma das seguintes políticas:

| Política | Impacto |
| --- | --- |
| None | Instrui o provedor de caixa de e-mail a não tomar nenhuma ação contra mensagens que falharam. |
| Quarantine | Instrui o provedor de caixa de e-mail a enviar mensagens que falharam para a pasta de spam. |
| Reject | Instrui o provedor de caixa de e-mail que mensagens que falharam irão para a pasta de spam e devem ser bloqueadas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Como funciona" }

#### Como verificar a autenticação DMARC do seu domínio {#how-to-check-your-domains-dmarc-authentication}

Existem duas opções para verificar a autenticação DMARC do seu domínio:

- **Opção 1:** Você pode inserir seu domínio principal ou subdomínio em qualquer verificador DMARC de terceiros, como o [MXToolbox](https://mxtoolbox.com/dmarc.aspx), para verificar se você tem uma política DMARC em vigor e qual é essa política.
    - **MXToolbox**: Se você configurou seu DMARC no domínio raiz, insira-o no MXToolbox. Se você configurou o DMARC no subdomínio, insira o subdomínio no MXToolbox. Esteja ciente de que o MXToolbox não faz buscas "para cima ou para baixo" ao realizar consultas. Isso significa que, se você configurou o DMARC no domínio raiz e inserir o subdomínio, o MXToolbox mostrará uma falha, pois não sabe que o DMARC foi configurado no domínio raiz.
- **Opção 2:** Abra um e-mail do seu domínio ou subdomínio na sua caixa de entrada e encontre a mensagem original para verificar se o DMARC está passando na autenticação desse e-mail.

Por exemplo, se você usa o Gmail, siga estas etapas:

1. Clique em **Mais** <i class="fa-solid fa-ellipsis"></i> em uma mensagem de e-mail.
2. Selecione **Mostrar original**.
3. Verifique se você tem o status "PASS" para **DMARC**.

![Um e-mail que tem "PASS" como valor de DMARC.]({% image_buster /assets/img_archive/dmarc_example.png %})

#### Solucionar falhas de DMARC {#troubleshoot-dmarc-failures}

Se o DMARC mostrar **FAIL** para mensagens enviadas pela Braze:

1. Abra os cabeçalhos brutos ou os resultados de autenticação de uma mensagem recente e verifique se **SPF** e **DKIM** passaram ou falharam individualmente.
2. **Alinhamento:** O DMARC é aprovado quando *o SPF* *ou* o DKIM está alinhado com o domínio **From**. Alinhamento significa que o domínio **From** corresponde ao domínio que passou no SPF (geralmente o domínio **Return-Path** / envelope) *ou* ao domínio na assinatura **d=** do DKIM.
3. Se o SPF passar, mas o DMARC falhar, o domínio Return-Path pode não estar alinhado com o seu domínio **From** — confirme se seus [domínios de envio e rastreamento com marca branca]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains) correspondem aos domínios para os quais você publica SPF e DKIM.
4. Se o DKIM falhar, verifique se os registros DNS de DKIM fornecidos pela Braze estão presentes e inalterados.

Verificadores de terceiros (por exemplo, [MXToolbox](https://mxtoolbox.com/dmarc.aspx)) ajudam a confirmar os registros publicados; sempre valide também com uma mensagem real enviada pela Braze.