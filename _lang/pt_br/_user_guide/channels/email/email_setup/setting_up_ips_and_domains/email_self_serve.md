---
nav_title: Autoatendimento de e-mail
article_title: Autoatendimento de e-mail
page_order: 0
page_type: tutorial
channel: email
description: "Este artigo de instruções aborda como configurar domínios de envio e rastreamento com o autoatendimento de e-mail na Braze."
toc_headers: h2
---

# Autoatendimento de e-mail {#email-self-serve}

> Esta página aborda como configurar domínios de envio e rastreamento na Braze para que seu domínio de remetente e links de rastreamento compartilhem o mesmo subdomínio.

## Pré-requisitos {#prerequisites}

Para usar a configuração de e-mail por autoatendimento, você deve atender aos seguintes pré-requisitos:

- Ser um novo cliente em integração
- Ter a permissão de nível de empresa "Edit Domain Settings"
- Ter um pool de IP, endereços IP e um domínio verificado

## Considerações {#considerations}

- Planeje um subdomínio de envio com no mínimo três níveis. Como a Braze cria um subdomínio sob o seu domínio delegado (como "marketing.exemplo.com"), seu domínio de envio precisa ter pelo menos três níveis de profundidade (como "e.marketing.exemplo.com").
- O domínio de envio deve ser subordinado a um domínio que você possui. Por exemplo, se você possui "exemplo.com", um subdomínio poderia ser "mail.exemplo.com", o que permite usar o endereço de envio "@mail.exemplo.com".
- Limites de domínio se aplicam. O número total de domínios de rastreamento é limitado a 2 multiplicado pelo número de domínios verificados em seu contrato. Se precisar de mais, entre em contato com seu gerente de conta.

## Configuração {#setup}

### Etapa 1: Adicionar um domínio de envio {#step-1-add-a-sending-domain}

Seu subdomínio de envio é o endereço a partir do qual seus e-mails são enviados. Ele determina o endereço de remetente que seus destinatários veem.

1. Na seção **Domains**, selecione **Add domain**.
2. Adicione seu domínio de envio nos campos **Mail from** e **Sending domain** para o pool de IP.
    - O endereço **Mail from** (envelope sender ou return path) é o que lida com bounces nos bastidores. Seus destinatários não veem isso em um e-mail. Por exemplo, você pode usar "bounce" como subdomínio, de modo que o mail from personalizado seja "bounce.mail.example.com". Usar esse subdomínio é uma prática recomendada para alinhamento DMARC SPF.
    - O **Sending domain** é o domínio no endereço de remetente que os destinatários veem na caixa de entrada. Por exemplo, se o endereço de remetente for "hello@e.mail.example.com", então "e.mail.example.com" é o domínio de envio.
{: start="3"}
3. Selecione seu domínio verificado no menu suspenso.

Os domínios de envio não podem ser alterados depois de enviados. A Braze cria registros DNS para verificação e autenticação e os adiciona às suas configurações de DNS. Se você precisar excluir um domínio de envio, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) para obter ajuda.

### Etapa 2: Adicionar um domínio de rastreamento {#step-2-add-a-tracking-domain}

Um domínio de rastreamento é usado para encapsular links nos seus e-mails para fins de rastreamento de cliques e branding. Os destinatários veem esse domínio quando passam o cursor sobre os links ou clicam neles nos seus e-mails. Ele deve ser um subdomínio do seu domínio de envio ou domínio verificado para a delegação de DNS adequada.

1. Selecione se você está usando um **Verified domain** ou **Sending domain** como subdomínio para o seu domínio de rastreamento:
    - Se você deseja que a URL de rastreamento corresponda ao domínio de envio para consistência de marca, selecione **Sending domain**.
    - Se você deseja uma URL de rastreamento mais curta, selecione o **Verified domain**.

{: start="2"}
2. Insira seu subdomínio de rastreamento. Ele é adicionado antes do subdomínio selecionado anteriormente.

O exemplo a seguir mostra como o domínio de rastreamento é exibido no e-mail com base na sua seleção:

|  | Seleção | Domínio de rastreamento |
| --- | --- | ---|
| Domínio verificado | mail.example.com | links.mail.example.com |
| Domínio de envio | marketing.mail.example.com | links.marketing.mail.example.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Domínio de rastreamento por seleção" }

{: start="3"}
3. Selecione o subdomínio verificado ou de envio associado no menu suspenso.
4. Selecione **Submit**. Você pode ver os domínios de envio e rastreamento com o status **Pending**.

Pode levar de 5 a 10 minutos para os registros DNS propagarem para domínios de envio. Quando seu domínio estiver pronto para uso, você receberá um e-mail de notificação. Os registros DNS para domínios de rastreamento podem levar até 24 horas para propagar, embora geralmente leve menos tempo. Você pode ver o subdomínio de envio ficar pronto antes do domínio de rastreamento.

### Etapa 3: Selecionar espaços de trabalho {#step-3-select-workspaces}

Selecione os espaços de trabalho que devem ter acesso ao domínio e, em seguida, selecione **Confirm**. Você também pode optar por adicionar automaticamente o domínio de envio a novos espaços de trabalho quando eles forem criados.

### Etapa 4: Configurar universal links (opcional) {#step-4-set-up-universal-links-optional}

Universal links permitem que os links nas suas mensagens abram diretamente no seu app em vez de em um navegador móvel. A Braze pode hospedar os arquivos de associação nos seus domínios de rastreamento em seu nome.

{% alert note %}
Universal links são aplicados por domínio de rastreamento. O mesmo conteúdo de arquivo pode ser compartilhado entre domínios, mas cada domínio hospeda sua própria cópia.
{% endalert %}

1. Acessar **Settings** > **Company Settings** > **Verified Domains** > **Universal Links**.
2. Selecione **Set up universal links**.
3. Insira um nome para o conjunto de universal links.
4. Ative a configuração do iOS e adicione seu arquivo AASA. JSON é o único tipo de arquivo aceito. A Braze lê o arquivo e exibe o número de IDs de app e componentes encontrados, além de uma prévia do arquivo gerado.
5. Ative a configuração do Android e adicione seu arquivo Digital Asset Links da mesma forma. A Braze exibe os nomes dos pacotes, a impressão digital do certificado SHA-256 e o número de declarações, além de uma prévia.
6. Verifique cada prévia para confirmar que o conteúdo está correto e, em seguida, selecione **Next: Select tracking domains**. Apenas domínios de rastreamento verificados aparecem. Um conjunto pode ser aplicado a vários domínios de rastreamento.
7. Seu conjunto aparece na página Universal Links junto com seus domínios de rastreamento, canais, status do iOS, status do Android e data de criação. A Braze verifica se o arquivo AASA está hospedado corretamente para cada domínio e reporta o resultado na coluna de status.

### Etapa 5: Testar o envio de e-mail {#step-5-test-your-email-sending}

Depois que os domínios de envio e rastreamento mostrarem o status **Ready for use**, teste sua configuração:

1. No seu espaço de trabalho, acessar **Settings** > **Email Settings**.
2. Verifique se o novo domínio de envio está listado na seção **Display Name Address**.
3. Adicione um endereço de remetente usando o novo domínio (por exemplo, "hello@e.mail.example.com").
4. Selecione **Save**.
5. Crie uma Campaign de e-mail de teste e envie para você mesmo. Em seguida, confirme que:
    - Seu e-mail foi entregue com sucesso.
    - O endereço de remetente está correto.
    - Os links de rastreamento de cliques usam o domínio de rastreamento.
    - Os universal links estão abrindo o app ou website conforme esperado, com base no dispositivo do destinatário.
    - Os cabeçalhos do e-mail são exibidos corretamente.

## Próximas etapas {#next-steps}

Após a conclusão da verificação do remetente, a Braze recomenda o [aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) para que suas mensagens cheguem às caixas de entrada de destino com uma taxa consistentemente alta.

Após concluir essa configuração, consulte a equipe de integração da Braze para confirmar se seus domínios e o aquecimento de IP estão funcionando corretamente.

## Solução de problemas {#troubleshooting}

### A propagação do DNS está demorando mais do que o esperado {#dns-propagation-is-taking-longer-than-expected}

Registros de domínio de envio normalmente se propagam em 5 a 10 minutos. Registros de domínio de rastreamento podem levar até 24 horas, dependendo das configurações de TTL do seu provedor DNS. Se a propagação demorar mais, confirme se os registros NS foram adicionados corretamente primeiro e, em seguida, entre em contato com o suporte da Braze.

### Não consigo remover um domínio verificado {#im-not-able-to-remove-a-verified-domain}

Domínios verificados não podem ser removidos diretamente no dashboard, pois isso pode prejudicar seus envios se não for devidamente revisado. Entre em contato com o suporte da Braze para ajudar a remover o domínio da sua conta.

### Meus links universais não estão abrindo o app {#my-universal-links-arent-opening-the-app}

Verifique os status do iOS e do Android na página de Universal Links primeiro. Se um domínio não estiver hospedando um arquivo válido, abra o conjunto, corrija a configuração e salve novamente. Se os status parecerem corretos, certifique-se de que está testando a partir de um link em um e-mail em um dispositivo real, em vez de colar o URL na barra de endereço do navegador.

## Perguntas frequentes {#frequently-asked-questions}

### A Braze pode gerenciar meu certificado SSL sem delegação de NS? {#can-braze-manage-my-ssl-certificate-without-ns-delegation}

O recurso Verified Domains exige registros NS (Name Server) para a delegação de propriedade do DNS à Braze. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="Braze-hosted SSL certificates without NS delegation" %}

### Posso delegar um domínio raiz? {#can-i-delegate-a-root-domain-instead}

O Verified Domains foi projetado e recomendado principalmente para uso com subdomínios. Não recomendamos delegar o domínio principal da sua marca por questões de segurança, pois você perde a visibilidade e o controle sobre ele. Se quiser delegar um domínio principal, use um que não seja utilizado em nenhum outro lugar além da Braze.

### Por que meu domínio verificado não pode ser também o domínio de envio? {#why-cant-my-verified-domain-also-be-the-sending-domain}

A Braze só pode criar um subdomínio de envio dentro do seu domínio verificado, que normalmente é um subdomínio do domínio principal (`mail.example.com`). Portanto, a profundidade mínima do domínio de envio nesse caso é de três níveis (`e.mail.example.com`), em vez dos dois níveis típicos.

### O que acontece se eu modificar algum dos meus registros NS após a configuração? {#what-happens-if-i-modify-any-of-my-ns-records-after-setup}

Os domínios verificados dependem totalmente da integridade dos registros NS. Se você fizer alterações em qualquer um dos seus registros NS, isso pode interromper o envio e o rastreamento de e-mails.

### Posso adicionar apenas uma das quatro linhas de registro NS, já que meu comando dig mostra todos os quatro registros? {#can-i-add-only-one-of-four-ns-record-lines-since-my-dig-command-shows-all-four-records}

Confirme que todos os quatro registros NS estão explicitamente presentes usando o comando `dig` e que o domínio é validado no dashboard antes de considerar a configuração como concluída.