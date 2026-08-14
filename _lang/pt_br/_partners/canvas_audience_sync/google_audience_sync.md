---
nav_title: Google
article_title: Canvas Audience Sync para o Google
alias: /google_audience_sync/
description: "Este artigo de referência abordará como usar o Audience Sync da Braze para o Google, para veicular anúncios com base em gatilhos comportamentais, segmentação e mais."
tool:
  - Canvas
page_order: 3

---

# Audience Sync para o Google {#audience-sync-to-google}

{% alert important %}
O Google está atualizando sua [Política de consentimento do usuário da UE](https://www.google.com/about/company/user-consent-policy/) em resposta às alterações na [Lei de Mercados Digitais (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que está em vigor desde 6 de março de 2024. Essa nova alteração exige que os anunciantes divulguem determinadas informações aos seus usuários finais do EEE, Reino Unido e Suíça, bem como obtenham o consentimento necessário deles. Consulte a documentação a seguir para saber mais.
{% endalert %}

A integração do Audience Sync da Braze com o Google permite que as marcas ampliem o alcance de suas jornadas de clientes em vários canais para o Google Search, Google Shopping, Gmail, YouTube e Google Display. Usando seus dados primários de clientes, você pode entregar anúncios com segurança com base em gatilhos comportamentais dinâmicos, segmentação e mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (por exemplo, push, e-mail ou SMS) como parte de um Canvas da Braze pode ser usado para disparar um anúncio para esse usuário com o [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) do Google.

{% alert note %}
A integração do Audience Sync da Braze com o Google é compatível com o Google Ads, não com o Google Ads Manager.
{% endalert %}

O Google Ads não gera mais públicos semelhantes, também conhecidos como "lookalike audiences", para direcionamento e relatórios. Consulte a [documentação do Google Ads](https://support.google.com/google-ads/answer/12463119?) para saber mais.

**Casos de uso comuns para sincronização de públicos personalizados incluem:**
{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

{% alert note %}
Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Google. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Saiba mais sobre nossa [política de privacidade de dados da Braze](https://www.braze.com/privacy).
{% endalert %}

## Pré-requisitos {#prerequisites}

Certifique-se de que os itens a seguir foram criados e concluídos antes de configurar sua etapa de público do Google no Canvas.

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Conta do Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Uma conta ativa do Google Ads para sua marca.<br><br>Se você deseja compartilhar um público entre várias contas gerenciadas, pode fazer upload dos seus públicos na sua [conta de gerente](https://support.google.com/google-ads/answer/6139186). |
| Termos do Google Ads e Políticas do Google Ads | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Você deve aceitar e garantir que está em conformidade com os [Termos de anúncios do Google](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) e as [Políticas de anúncios do Google](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), que incluem a [Política de consentimento do usuário da UE](https://www.google.com/about/company/user-consent-policy/), conforme aplicável a você, no uso do Braze Audience Sync.<br><br>Consulte sua equipe jurídica sobre a nova Política de consentimento do usuário da UE do Google para garantir que você está coletando o consentimento adequado para usar os serviços do Google Ads para seus usuários finais do EEE, Reino Unido e Suíça. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) | O Customer Match não está disponível para todos os anunciantes.<br><br>**Para usar o Customer Match, sua conta deve ter:**<br>• Um bom histórico de conformidade com as políticas<br>• Um bom histórico de pagamentos<br>• Pelo menos 90 dias de histórico no Google Ads<br>• Mais de USD 50.000 em gastos totais acumulados. Para anunciantes cujas contas são gerenciadas em moedas diferentes de USD, o valor gasto será convertido para USD usando a taxa de conversão mensal média para essa moeda.<br><br>Se sua conta não atender a esses critérios, ela não é elegível no momento para usar o Customer Match.<br><br>Entre em contato com seu representante do Google Ads para obter mais orientações sobre a disponibilidade do Customer Match para sua conta. |
| Sinais de consentimento do Google | [Google](https://support.google.com/google-ads/answer/14310715) | Se você deseja exibir anúncios para usuários finais do EEE usando o serviço Customer Match do Google, será necessário enviar à Braze os seguintes atributos personalizados (booleanos) como parte da Política de consentimento do usuário da UE do Google. Mais detalhes podem ser encontrados em [Coletando consentimento para usuários finais do EEE, Reino Unido e Suíça](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

### Versões mínimas do SDK {#required-sdk-versions}

Ao usar os SDKs da Braze para coletar sinais de consentimento, certifique-se de atender às seguintes versões mínimas:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Coletando consentimento para usuários finais do EEE, Reino Unido e Suíça {#collecting-consent-for-eea-uk-and-switzerland-end-users}

A Política de consentimento do usuário da UE do Google exige que os anunciantes divulguem o seguinte aos seus usuários finais do EEE, Reino Unido e Suíça, bem como obtenham seu consentimento para:

* O uso de cookies ou outro armazenamento local quando legalmente exigido; e
* A coleta, o compartilhamento e o uso de seus dados pessoais para a personalização de anúncios.

Isso não afeta usuários finais dos EUA ou quaisquer outros usuários finais localizados fora do EEE, do Reino Unido ou da Suíça. Consulte sua equipe jurídica sobre a nova Política de consentimento do usuário da UE do Google para garantir que você está coletando o consentimento adequado para usar os serviços do Google Ads para seus usuários finais do EEE, Reino Unido e Suíça.

De acordo com os requisitos do Digital Markets Act (DMA) em vigor desde 6 de março de 2024, os anunciantes devem enviar o consentimento dos usuários finais do EEE, Reino Unido e Suíça ao compartilhar dados com o Google. Como parte dessa mudança, você pode coletar ambos os sinais de consentimento na Braze como os seguintes atributos personalizados booleanos:

* `$google_ad_user_data`
* `$google_ad_personalization`

A Braze sincronizará os dados desses atributos personalizados com os [campos de consentimento apropriados no Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Gerenciando consentimento revogado {#managing-revoked-consent}

Para manter suas listas de público atualizadas caso um usuário final do EEE tenha sido adicionado à lista de público e, posteriormente, tenha revogado qualquer um dos dois consentimentos (`$google_ad_user_data` ou `$google_ad_personalization`), você deve configurar um Canvas para remover usuários das listas de público existentes usando uma etapa de Audience Sync.

{% alert note %}
Se um usuário do EEE forneceu consentimento anteriormente para ambos os sinais, esses dados continuarão sendo usados para o Customer Match do Google até que a lista expire, ou até que o status de consentimento seja explicitamente atualizado via Google Audience Sync, ou ambos.
{% endalert %}

#### Dicas {#tips}

* Envie o valor como tipo booleano, não como tipo string.
* Adicione o prefixo de cifrão ($) ao nome do atributo. A Braze usa um cifrão no início do nome de um atributo para indicar que se trata de uma chave especial e reservada.
* Insira o nome do atributo em letras minúsculas.
* Embora você não possa definir explicitamente um usuário como não especificado, se enviar um valor `null` ou `nil` ou qualquer valor que não seja `true` ou `false`, a Braze enviará esse usuário ao Google como `UNSPECIFIED`.
* Novos usuários adicionados ou atualizados sem especificar nenhum dos atributos de consentimento serão sincronizados com o Google com esses atributos de consentimento marcados como não especificados.

Se você tentar sincronizar um usuário do EEE sem os campos de consentimento necessários e o status concedido, o Google rejeitará esse usuário e não exibirá anúncios para ele. Além disso, se um anúncio for exibido a um usuário do EEE sem seu consentimento explícito, você poderá ser responsabilizado e estar em risco financeiro. Para evitar isso, sugerimos enviar Campaigns com filtros de Segment que incluam apenas usuários do EEE, Reino Unido e Suíça com atributos de consentimento do Google definidos como `true`. Para mais detalhes sobre a Política de consentimento do usuário da UE para parceiros de upload do Customer Match, consulte as [Perguntas frequentes](https://support.google.com/google-ads/answer/14310715) do Google.

### Configurando seu Canvas {#setting-up-your-canvas}

Após a sincronização com a Braze, os seguintes atributos de consentimento estarão disponíveis nos perfis de usuário e para segmentação:

- `$google_ad_user_data`
- `$google_ad_personalization`

Em qualquer Canvas em que você esteja direcionando usuários finais do EEE, Reino Unido e Suíça usando um Google Audience Sync para adicionar usuários a um público, você deve excluir esses usuários sempre que ambos os atributos de consentimento tiverem qualquer valor diferente de `true`. Você pode fazer isso segmentando esses usuários quando os valores de consentimento estiverem definidos como `true`. Isso também garante que a análise de dados dos usuários sincronizados seja mais precisa, pois sabemos que o Google rejeitará esses usuários dos públicos. Observe que, se você estiver usando o Google Audience Sync para remover usuários de um público, os atributos de consentimento não são obrigatórios.

## Integração {#integration}

### Etapa 1: Conectar a conta do Google {#step-1-connect-google-account}

{% alert important %}
Você precisa ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar o Google Ads à sua conta da Braze.
{% endalert %}

Para começar, acesse **Integrações com parceiros** > **Parceiros de tecnologia** > **Google Ads** e selecione **Conectar Google Ads**. Você verá um modal para selecionar o e-mail associado à sua conta do Google Ads e, em seguida, conceder à Braze acesso à sua conta do Google Ads.

Após conectar sua conta do Google Ads com sucesso, você será redirecionado para a página de parceiro do Google Ads. Em seguida, será solicitado que você selecione quais contas de anúncios deseja acessar no espaço de trabalho da Braze.

![Um GIF que mostra o fluxo de trabalho de uma conexão bem-sucedida da conta do Google Ads à Braze.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Exportar IDFA do iOS ou IDs de publicidade do Google {#export-ios-idfa-or-google-advertising-ids}

Se você planeja exportar IDFA do iOS ou IDs de publicidade do Google na sincronização de público, o Google exige o ID do app iOS e o ID do app Android nas solicitações. Em Google Audience Sync, selecione **Adicionar IDs de publicidade móvel**, insira o ID do app iOS e o ID do app Android (nome do pacote do app) e salve cada um.

<br><br>
![A página de tecnologia atualizada do Google Ads mostrando as contas de anúncios conectadas, permitindo ressincronizar contas e adicionar IDs de publicidade móvel.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

Se você tiver vários apps em um único espaço de trabalho, pode inserir qualquer um dos IDs de app na configuração, pois os IDs de publicidade móvel dos seus usuários serão os mesmos em vários apps. Isso ocorre porque tanto o GAID do Android quanto o IDFA do iOS são identificadores de publicidade universais no dispositivo e não são específicos de um app. Para sincronizar IDs de publicidade móvel de usuários de um app específico, você pode usar filtros de Segment ("Último app específico usado" ou "Versão mais recente do app") para direcionar esses usuários.

### Etapa 2: Adicionar uma etapa de público do Google no Canvas {#step-2-add-a-google-audience-step-in-canvas}

Adicione um componente no seu Canvas e selecione **Audience Sync**.

![O menu para selecionar um componente do Canvas no editor.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![A etapa Audience Sync adicionada à jornada do usuário.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 3: Configuração da sincronização {#step-3-sync-setup}

1. Selecione **Custom Audience** para abrir o editor de componentes.
2. Selecione **Google** como parceiro de Audience Sync.

![As configurações da etapa Audience Sync com a opção de selecionar um parceiro para iniciar a sincronização.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. Selecione a conta de anúncios do Google desejada.
4. No menu suspenso **Escolher um público novo ou existente**, insira o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}

1. Insira um nome para o novo público personalizado.
2. Selecione **Adicionar usuários ao público**.
3. Selecione os dados de campo de usuário primários para enviar ao seu público. Você pode escolher entre:

- **Informações de contato do cliente**: Contém os e-mails ou números de telefone dos seus usuários, ou ambos, se existirem na Braze. O Google exige que isso seja um campo único para sincronização, em vez de identificadores separados. Você ainda pode usar esse campo único se tiver apenas um dos identificadores.
- **ID de anunciante móvel**: Selecione IDFA do iOS ou GAID do Android. Devido aos requisitos do Google Customer Match, você não pode ter ambos os IDs de anunciante móvel nas mesmas listas de clientes.

{% alert note %}
**Sobre o banner "IDs de publicidade móvel ausentes? Vamos corrigir isso.":** Quando você sincroniza com um público usando IDFA do iOS ou GAID do Android como campo de correspondência, essa mensagem pode aparecer no editor de etapas. Ela é **informativa, não um erro**. Ela lembra você de confirmar que o campo de ID de publicidade móvel que está sendo usado para correspondência existe nos dados do seu público (por exemplo, que os usuários na jornada do Canvas têm o identificador correspondente coletado). Você pode descartá-la após verificar seus dados.
{% endalert %}

{: start="4"}
4. Em seguida, salve seu público selecionando o botão **Criar público** na parte inferior do editor de etapas.

![Visualização expandida do componente Custom Audience do Canvas. Aqui, a conta de anúncios desejada está selecionada, um novo público é criado e a caixa de seleção "informações de contato do cliente" está marcada.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Os usuários serão notificados na parte superior do editor de etapas se o público for criado com sucesso ou se ocorrerem erros durante esse processo. Os usuários podem referenciar esse público para remoção de usuários posteriormente na jornada do Canvas, pois o público foi criado em modo de rascunho.

![Um alerta que aparece após a criação de um novo público no componente do Canvas.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Quando você lança um Canvas com um novo público, a Braze cria um novo público personalizado ao lançar o Canvas e, em seguida, sincroniza os usuários em tempo quase real à medida que eles entram na etapa de público do Google.

{% alert important %}
Devido aos requisitos do Google Customer Match, você não pode ter informações de contato do cliente e IDs de anunciante móvel nas mesmas listas de clientes. O Google Customer Match usará essas informações para determinar quem pode ser direcionado no Google Search, Google Display, YouTube e Gmail. Para mais detalhes sobre os requisitos do Google Customer Match, consulte a [documentação](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sincronizar com um público existente %}

A Braze também oferece a capacidade de adicionar ou remover usuários de listas de clientes existentes do Google para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente:

1. Selecione um público personalizado existente para sincronizar.
2. Escolha se deseja **Adicionar ao público** ou **Remover do público**.
3. A Braze adicionará ou removerá usuários em tempo quase real à medida que eles entrarem na etapa de público do Google.
4. Após configurar sua etapa de público do Google, selecione **Concluído**. Sua etapa de público do Google incluirá detalhes sobre o novo público.

![Visualização expandida do componente Custom Audience do Canvas. Aqui, a conta de anúncios desejada e o público existente estão selecionados, assim como o botão de opção "Adicionar usuário ao público".]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar o Canvas {#step-4-launch-canvas}

Conclua o restante da jornada do usuário no Canvas e lance! Se você optou por criar um novo público, a Braze criará o público no Google e adicionará os usuários à medida que eles alcançarem essa etapa no seu Canvas. Se você selecionou adicionar ou remover usuários de um público existente, a Braze adicionará ou removerá os usuários quando eles alcançarem essa etapa na jornada do usuário.

Os usuários avançarão para o próximo componente do Canvas, se houver um, ou sairão do Canvas se for a última etapa da jornada do usuário.

## Sincronização de usuários e considerações sobre limite de frequência {#user-syncing-and-rate-limit-considerations}

À medida que os usuários chegam ao componente de Audience Sync, a Braze sincronizará esses usuários em tempo quase real, respeitando os limites de frequência da API do Google Ads. Na prática, isso significa que a Braze tentará agrupar e processar o maior número possível de usuários a cada 5 segundos antes de enviá-los ao Google.

Quando um cliente estiver próximo de atingir o limite de frequência da API do Google Ads, o Google fornecerá feedback à Braze com recomendações de nova tentativa. Se um cliente da Braze atingir o limite de frequência, o Canvas da Braze tentará novamente a sincronização por até &#126;13 horas. Se a sincronização não for possível, esses usuários serão listados na métrica Users Errored.

## Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudar você a entender melhor a análise de dados da sua etapa de Audience Sync.

| Métrica | Descrição |
| ------ | ----------- |
| *Entered* | Número de usuários que entraram nesta etapa para serem sincronizados com o Google. |
| *Proceeded to Next Step* | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançam automaticamente. Se esta for a última etapa na ramificação do Canvas, essa métrica será 0. |
| *Users Synced* | Número de usuários que foram sincronizados com sucesso com o Google. |
| *User Not Synced* | Número de usuários que não foram sincronizados devido a campos ausentes para correspondência ou porque o atributo de consentimento foi definido como `false`. |
| *Users Errored* | Número de usuários que não foram sincronizados com o Google devido a um erro, após &#126;13 horas de tentativas. Para erros específicos, como interrupções no serviço da API do Google Ads, o Canvas tentará novamente a sincronização por até &#126;13 horas. Se a sincronização ainda não for possível nesse ponto, o campo *User Not Synced* será preenchido. |
| *Users Pending* | Número de usuários sendo processados atualmente pela Braze para sincronização com o Google. |
| *Exited Canvas* | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa em um Canvas é uma etapa do Google. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

## Perguntas frequentes {#frequently-asked-questions}

### Por que não consigo selecionar vários campos para correspondência na configuração da minha etapa de público do Google? {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

O Google Customer Match tem requisitos rigorosos sobre como esses públicos são formatados e quais informações do cliente são incluídas. Especificamente, os IDs de anunciantes móveis precisam ser enviados separadamente das informações de contato do cliente (como e-mail e número de telefone). Para mais detalhes, consulte a [documentação do Google Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### Quanto tempo leva para meus públicos serem sincronizados no Google? {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

Pode levar de 6 a 12 horas para um público ser sincronizado no Google.

### Sincronizei um público, mas por que o tamanho do público no Google está zerado? {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

Por questões de privacidade, o tamanho da lista de usuários será exibido como zero até que a lista tenha pelo menos 1.000 membros. Depois disso, o tamanho será arredondado para os dois dígitos mais significativos.

### Por que o tamanho do meu público correspondente no Google é menor do que o número de usuários sincronizados da Braze? {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Embora a Braze possa sincronizar um determinado número de usuários para o Google, o tamanho real do público correspondente que você vê no Google Ads pode ser significativamente menor. Isso acontece porque o Google precisa fazer a correspondência dos dados de usuário que você fornece (como endereços de e-mail ou números de telefone) com contas reais do Google na plataforma deles.

Mesmo que seus perfis de usuário na Braze contenham campos de correspondência válidos, os usuários só aparecem no seu público personalizado do Google se tiverem uma conta do Google com informações correspondentes.

Para melhorar sua taxa de correspondência:
- Confirme que você está [formatando seus dados corretamente](https://support.google.com/google-ads/answer/7659867).
- Forneça vários identificadores quando possível (por exemplo, tanto e-mail quanto número de telefone).
- Observe que pode levar de 48 a 72 horas para o Google processar e fazer a correspondência dos usuários, embora em alguns casos possa levar vários dias.

O tamanho final do público correspondente depende inteiramente do processo de correspondência do Google. A Braze não tem visibilidade sobre a correspondência do Google depois que os dados são enviados para a plataforma deles.

### Sincronizei um público no Google, mas meus anúncios não estão sendo veiculados. {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

Verifique se seus públicos contêm pelo menos 5.000 usuários para que os anúncios possam começar a ser veiculados.

### Como resolvo o erro "Mobile App IDs Deleted"? {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Se você está sincronizando públicos com o Google, esse erro será disparado se você selecionou a sincronização de identificadores móveis como parte das suas sincronizações, mas excluiu os IDs de app móvel da página de parceiro do Google. Para resolver esse problema, certifique-se de que adicionou os IDs de app móvel apropriados para iOS e Android na página de parceiro do Google.

### Por que recebi um e-mail de credenciais inválidas do Google Ads quando o dashboard ainda mostra como conectado? {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

A Braze envia esse e-mail automaticamente quando a API do Google retorna um erro de autorização. Isso pode acontecer mesmo quando o **Google Ads** ainda aparece como conectado no dashboard e os públicos parecem estar sincronizando — por exemplo, quando a conta do Google conectada não tem permissão para uma ação específica solicitada pelo Google, ou quando os termos de serviço do Google Ads ainda precisam ser aceitos para a conta.

Alguns erros de autorização se resolvem sozinhos. Verifique as análises de **Audience Sync** do seu Canvas (por exemplo, *Users Synced* e *Users Errored*) para confirmar se os usuários ainda estão sincronizando. Se os problemas continuarem, acesse **Partner Integrations** > **Technology Partners** > **Google Ads**, encontre **Google Audience Sync** e use **Change Account** para reconectar com uma conta do Google Ads que tenha o acesso necessário e a configuração concluída.