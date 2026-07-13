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
- Direcionamento de usuários de alto valor por meio de vários canais para impulsionar compras ou engajamento.
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing.
- Criação de públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.

{% alert note %}
Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Google. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Saiba mais sobre nossa [política de privacidade de dados da Braze](https://www.braze.com/privacy).
{% endalert %}

## Pré-requisitos {#prerequisites}

Certifique-se de que os itens a seguir tenham sido criados e concluídos antes de configurar a etapa do Google Audience no Canvas.

| Requisito | Origem | Descrição |
| ----------- | ------ | ----------- |
| Conta do Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Uma conta ativa do Google Ads para sua marca.<br><br>Se você deseja compartilhar um público entre várias contas gerenciadas, pode fazer upload dos seus públicos na sua [conta de gerente](https://support.google.com/google-ads/answer/6139186). |
| Termos do Google Ads e Políticas do Google Ads | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Você deve aceitar e garantir que está em conformidade com os [Termos de Anúncios do Google](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) e as [Políticas de Anúncios do Google](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), que incluem a [Política de Consentimento do Usuário da UE](https://www.google.com/about/company/user-consent-policy/), conforme aplicável a você, no uso do Braze Audience Sync.<br><br>Consulte sua equipe jurídica sobre a nova Política de Consentimento do Usuário da UE do Google para garantir que esteja coletando o consentimento adequado para usar os serviços do Google Ads para seus usuários finais do EEE, Reino Unido e Suíça. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) | O Customer Match não está disponível para todos os anunciantes.<br><br>**Para usar o Customer Match, sua conta deve ter:**<br>• Um bom histórico de conformidade com as políticas<br>• Um bom histórico de pagamento<br>• Pelo menos 90 dias de histórico no Google Ads<br>• Mais de US$ 50.000 de gasto total ao longo da vida. Para anunciantes cujas contas são gerenciadas em moedas diferentes de USD, o valor gasto será convertido para USD usando a taxa de conversão média mensal para essa moeda.<br><br>Caso sua conta não atenda a esses critérios, ela não será considerada elegível para usar o Customer Match.<br><br>Fale com seu representante do Google Ads para obter mais orientações sobre a disponibilidade do Customer Match para sua conta. |
| Sinais de consentimento do Google | [Google](https://support.google.com/google-ads/answer/14310715) | Se você deseja veicular anúncios para usuários finais do EEE usando o serviço Customer Match do Google, precisará enviar à Braze os seguintes atributos personalizados (booleanos) como parte da Política de Consentimento do Usuário da UE do Google. Mais detalhes podem ser encontrados em [Coleta de consentimento para usuários finais do EEE, Reino Unido e Suíça](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

### Versões necessárias do SDK {#required-sdk-versions}

Ao usar os SDKs da Braze para coletar sinais de consentimento, certifique-se de atender às seguintes versões mínimas:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Coleta de consentimento para usuários finais do EEE, Reino Unido e Suíça {#collecting-consent-for-eea-uk-and-switzerland-end-users}

A Política de Consentimento do Usuário da UE do Google exige que os anunciantes divulguem o seguinte aos seus usuários finais do EEE, Reino Unido e Suíça, bem como obtenham seu consentimento para:

* O uso de cookies ou outro armazenamento local onde legalmente exigido; e
* A coleta, o compartilhamento e o uso de seus dados pessoais para a personalização de anúncios.

Isso não afeta os usuários finais dos EUA ou quaisquer outros usuários finais localizados fora do EEE, do Reino Unido ou da Suíça. Consulte sua equipe jurídica sobre a nova Política de Consentimento do Usuário da UE do Google para garantir que esteja coletando o consentimento adequado para usar os serviços do Google Ads para seus usuários finais do EEE, Reino Unido e Suíça.

De acordo com os requisitos da Lei de Mercados Digitais (DMA) em vigor desde 6 de março de 2024, os anunciantes devem transmitir o consentimento dos usuários finais do EEE, Reino Unido e Suíça ao compartilhar dados com o Google. Como parte dessa mudança, você pode coletar ambos os sinais de consentimento na Braze como os seguintes atributos personalizados booleanos:

* `$google_ad_user_data`
* `$google_ad_personalization`

A Braze sincronizará os dados desses atributos personalizados com os [campos de consentimento apropriados no Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Como gerenciar consentimento revogado {#managing-revoked-consent}

Para manter suas listas de público atualizadas no caso de um usuário final do EEE ter sido adicionado à lista de público e, em seguida, ter retirado qualquer um dos dois consentimentos (`$google_ad_user_data` ou `$google_ad_personalization`), você deve configurar um Canvas para remover usuários das listas de público existentes usando uma etapa do Audience Sync.

{% alert note %}
Se um usuário do EEE já tiver fornecido consentimento para ambos os sinais, esses dados continuarão a ser usados para o Customer Match do Google até que essa lista expire, ou que o status de consentimento seja explicitamente atualizado via Google Audience Sync, ou ambos.
{% endalert %}

#### Dicas {#tips}

* Envie o valor como tipo booleano, não como string.
* Prefixe o cifrão ($) para o nome do atributo. A Braze usa um cifrão no início de um nome de atributo para indicar que esta é uma chave especial e reservada.
* Digite o nome do atributo em letras minúsculas.
* Embora você não possa definir explicitamente um usuário como não especificado, se você enviar um valor `null` ou `nil` ou qualquer valor que não seja `true` ou `false`, a Braze passará esse usuário para o Google como `UNSPECIFIED`.
* Novos usuários adicionados ou atualizados sem especificar qualquer atributo de consentimento serão sincronizados com o Google com esses atributos de consentimento marcados como não especificados.

Se você tentar sincronizar um usuário do EEE sem os campos de consentimento necessários e o status concedido, o Google rejeitará a tentativa e não exibirá anúncios para esse usuário. Além disso, se um anúncio for exibido a um usuário do EEE sem o seu consentimento explícito, você pode ser responsabilizado e correr risco financeiro. Para evitar isso, sugerimos o envio de campanhas com filtros de segmento que incluam apenas usuários do EEE, Reino Unido e Suíça com atributos de consentimento do Google definidos como `true`. Para mais detalhes sobre a Política de Consentimento do Usuário da UE para parceiros de upload do Customer Match, consulte as [perguntas frequentes](https://support.google.com/google-ads/answer/14310715) do Google.

### Configurando seu Canvas {#setting-up-your-canvas}

Após a sincronização com a Braze, os seguintes atributos de consentimento estarão disponíveis nos seus perfis de usuário e para segmentação:

- `$google_ad_user_data`
- `$google_ad_personalization`

Em qualquer Canvas em que esteja direcionando usuários finais do EEE, do Reino Unido e da Suíça usando o Google Audience Sync para adicionar usuários a um público, é necessário excluir esses usuários sempre que ambos os atributos de consentimento tiverem qualquer valor que não seja `true`. Você pode fazer isso segmentando esses usuários quando os valores de consentimento estiverem definidos como `true`. Isso também garante que a análise de dados mais precisa dos usuários seja sincronizada, pois sabemos que o Google rejeitará esses usuários do público. Note que, se estiver usando o Google Audience Sync para remover usuários de um público, os atributos de consentimento não são necessários.

## Integração {#integration}

### Etapa 1: conecte a conta do Google {#step-1-connect-google-account}

{% alert important %}
Você deve ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar o Google Ads à sua conta Braze.
{% endalert %}

Para começar, acesse **Integrações de Parceiros** > **Parceiros de Tecnologia** > **Google Ads** e selecione **Connect Google Ads**. Será exibido um modal para selecionar o e-mail associado à sua conta do Google Ads e, em seguida, conceder à Braze acesso à sua conta do Google Ads.

Depois de conectar sua conta do Google Ads com sucesso, você será levado de volta à página de parceiro do Google Ads. Em seguida, será solicitado que você selecione as contas de anúncios que deseja acessar no espaço de trabalho da Braze.

![Um GIF que mostra o fluxo de trabalho de uma conexão bem-sucedida da conta do Google Ads com a Braze.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Exportar iOS IDFA ou Google Advertising IDs {#export-ios-idfa-or-google-advertising-ids}

Se você planeja exportar iOS IDFA ou Google Advertising IDs na sua sincronização de público, o Google exige o ID do aplicativo iOS e o ID do aplicativo Android nas solicitações. Em Google Audience Sync, selecione **Add Mobile Advertising IDs**, insira o ID do aplicativo iOS e o ID do aplicativo Android (nome do pacote do app) e salve cada um.

<br><br>
![A página atualizada da tecnologia Google Ads mostrando as contas de anúncios conectadas, permitindo que você sincronize novamente as contas e adicione IDs de publicidade móvel.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

Se você tiver vários apps em um único espaço de trabalho, poderá inserir qualquer ID de app na configuração, pois os IDs de anúncios para celular dos seus usuários serão os mesmos em vários apps. Isso ocorre porque tanto o GAID do Android quanto o IDFA do iOS são identificadores de anúncios universais no dispositivo e não são específicos do app. Para sincronizar IDs de anúncios móveis para usuários de um app específico, é possível usar filtros de segmento ("Last Used Specific App" ou "Most Recent App Version") para direcionar esses usuários.

### Etapa 2: adicionar uma etapa do Google Audience no Canvas {#step-2-add-a-google-audience-step-in-canvas}

Adicione um componente no seu Canvas e selecione **Audience Sync**.

![O menu para selecionar um componente Canvas no editor.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![A etapa Audience Sync adicionada à jornada do usuário.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 3: configuração de sincronização {#step-3-sync-setup}

1. Selecione **Custom Audience** para abrir o editor de componentes.
2. Selecione **Google** como o parceiro do Audience Sync.

![As configurações da etapa Audience Sync com a opção de selecionar um parceiro para iniciar a sincronização.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. Selecione a conta de anúncio do Google desejada.
4. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}

1. Digite um nome para o novo público personalizado.
2. Selecione **Add Users to Audience**.
3. Selecione os dados primários do campo do usuário para enviar ao seu público. Você pode escolher:

- **Customer Contact Info**: contém os e-mails ou números de telefone dos seus usuários, ou ambos, se existirem na Braze. O Google exige que esse seja um único campo a ser sincronizado, em vez de identificadores separados. Você ainda pode usar esse campo único se tiver apenas um dos identificadores.
- **Mobile Advertiser ID**: selecione iOS IDFA ou Android GAID. Devido aos requisitos do Customer Match do Google, você não pode ter os dois IDs de anunciante móvel nas mesmas listas de clientes.

{% alert note %}
**Sobre o banner "Missing Mobile Ad IDs? Let's fix that.":** quando você sincroniza com um público usando o IDFA do iOS ou o GAID do Android como campo de correspondência, essa mensagem pode aparecer no editor de etapas. É **informativo, não um erro**. Ele lembra você de confirmar que o campo de ID de anúncio móvel que está sendo correspondido existe nos dados do público (por exemplo, que os usuários na jornada do Canvas têm o identificador correspondente coletado). Você pode descartá-lo depois de verificar seus dados.
{% endalert %}

{: start="4"}
4. Em seguida, salve seu público selecionando o botão **Create Audience** na parte inferior do editor de etapas.

![Vista expandida do componente de Canvas de público personalizado. Aqui, a conta de anúncios desejada é selecionada, um novo público é criado e a caixa de seleção "customer contact info" é marcada.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Os usuários serão notificados no topo do editor de etapas se o público for criado com sucesso ou se ocorrerem erros durante esse processo. Os usuários podem referenciar esse público para remoção de usuários mais tarde na jornada do Canvas, pois o público foi criado no modo de rascunho.

![Um alerta que aparece depois que um novo público é criado no componente Canvas.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Ao lançar um Canvas com um novo público, a Braze criará um novo público personalizado ao lançar o Canvas e, posteriormente, sincronizará os usuários quase em tempo real quando eles entrarem na etapa do Google Audience.

{% alert important %}
De acordo com os requisitos do Customer Match do Google, você não pode ter informações de contato de clientes e IDs de anunciantes móveis nas mesmas listas de clientes. O Customer Match do Google usará essas informações para determinar quem pode ser direcionado no Google Search, Google Display, YouTube e Gmail. Para mais detalhes sobre os requisitos do Customer Match do Google, revise a [documentação](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sincronizar com um público existente %}

A Braze também oferece a capacidade de adicionar ou remover usuários de listas de clientes do Google existentes para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente:

1. Selecione um público personalizado existente para sincronizar.
2. Escolha se você deseja **Add to the audience** ou **Remove from the audience**.
3. A Braze adicionará ou removerá usuários quase em tempo real à medida que eles entrarem na etapa do Google Audience.
4. Após configurar a etapa do Google Audience, selecione **Done**. Sua etapa do Google Audience incluirá detalhes sobre o novo público.

![Vista expandida do componente de Canvas de público personalizado. Aqui, a conta de anúncios desejada e o público existente são selecionados, bem como o botão de rádio "Add user to Audience".]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: lançar o Canvas {#step-4-launch-canvas}

Complete o restante da sua jornada de usuário dentro do Canvas e depois lance! Se você optou por criar um novo público, a Braze criará o público no Google e, em seguida, adicionará usuários à medida que eles alcançarem essa etapa no seu Canvas. Se você selecionou adicionar ou remover usuários de um público existente, a Braze adicionará ou removerá usuários quando eles alcançarem essa etapa em sua jornada de usuário.

Os usuários então avançarão para o próximo componente do Canvas, se houver um, ou sairão do Canvas se for a última etapa da jornada do usuário.

## Considerações sobre sincronização de usuários e limite de frequência {#user-syncing-and-rate-limit-considerations}

À medida que os usuários alcançam o componente Audience Sync, a Braze os sincronizará quase em tempo real, respeitando os limites de frequência da API do Google Ads. Na prática, isso significa que a Braze tentará agrupar e processar o maior número possível de usuários a cada 5 segundos antes de enviá-los para o Google.

Quando um cliente estiver perto de atingir o limite de frequência da API do Google Ads, o Google fornecerá feedback à Braze sobre as recomendações de novas tentativas. Se um cliente da Braze atingir seu limite de frequência, o Canvas tentará sincronizar novamente por até &#126;13 horas. Se a sincronização não for possível, esses usuários são listados na métrica de Usuários com Erro.

## Detalhes da análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados da sua etapa de Audience Sync.

| Métrica | Descrição |
| ------ | ----------- |
| *Entraram* | Número de usuários que entraram nesta etapa para serem sincronizados com o Google. |
| *Avançaram para a etapa seguinte* | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente. Se esta for a última etapa no ramo do Canvas, esta métrica será 0. |
| *Usuários sincronizados* | Número de usuários que foram sincronizados com sucesso com o Google. |
| *Usuários não sincronizados* | Número de usuários que não foram sincronizados devido à falta de campos para correspondência ou porque o atributo de consentimento foi definido como `false`. |
| *Usuários com erro* | Número de usuários que não foram sincronizados com o Google devido a um erro, após &#126;13 horas de tentativas. Para erros específicos, como interrupções no serviço da API do Google Ads, o Canvas tentará sincronizar novamente por até &#126;13 horas. Se a sincronização ainda não for possível nesse ponto, o *Usuários não sincronizados* será preenchido. |
| *Usuários pendentes* | Número de usuários atualmente sendo processados pela Braze para sincronizar com o Google. |
| *Saíram do Canvas* | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa em um Canvas é uma etapa do Google. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhes da análise de dados" }

## Perguntas frequentes {#frequently-asked-questions}

### Por que não posso selecionar vários campos para correspondência na minha configuração da etapa do Google Audience? {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

O Customer Match do Google tem requisitos rigorosos sobre como esses públicos são formatados e quais informações do cliente são incluídas. Especificamente, os IDs de anunciantes móveis precisam ser carregados separadamente das informações de contato do cliente (como e-mail e número de telefone). Para mais detalhes, consulte a [documentação do Customer Match do Google](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### Quanto tempo levará para que meus públicos sejam sincronizados no Google? {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

Pode levar de 6 a 12 horas para um público ser sincronizado no Google.

### Sincronizei um público, então por que o tamanho do público no Google é zero? {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

Para fins de privacidade, o tamanho da lista de usuários mostrará zero até que a lista tenha pelo menos 1.000 membros. Depois disso, o tamanho será arredondado para os dois dígitos mais significativos.

### Por que o tamanho do público correspondido no Google é menor do que o número de usuários sincronizados pela Braze? {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Embora a Braze possa sincronizar um determinado número de usuários para o Google, o tamanho real do público correspondido que você vê no Google Ads pode ser significativamente menor. Isso ocorre porque o Google precisa corresponder os dados de usuário que você fornece (como endereços de e-mail ou números de telefone) com contas reais do Google em sua plataforma.

Mesmo que seus perfis de usuário na Braze contenham campos de correspondência válidos, os usuários só aparecerão no seu público personalizado do Google se tiverem uma conta do Google com informações correspondentes.

Para melhorar sua taxa de correspondência:
- Confirme que você está [formatando seus dados corretamente](https://support.google.com/google-ads/answer/7659867).
- Forneça vários identificadores quando possível (por exemplo, tanto e-mail quanto número de telefone).
- Observe que pode levar de 48 a 72 horas para o Google processar e corresponder os usuários, embora em alguns casos possa levar vários dias.

O tamanho final do público correspondido depende inteiramente do processo de correspondência do Google. A Braze não tem visibilidade sobre a correspondência do Google depois que os dados são enviados para a plataforma deles.

### Sincronizei um público no Google, mas meus anúncios não estão sendo exibidos. {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

Verifique se seus públicos contêm pelo menos 5.000 usuários para que os anúncios possam começar a ser veiculados.

### Como faço para resolver o erro "Mobile App IDs Deleted"? {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Se estiver sincronizando públicos com o Google, esse erro será disparado se você tiver selecionado a sincronização de identificadores móveis como parte das suas sincronizações, mas tiver excluído os IDs de apps móveis da página de parceiros do Google. Para resolver esse problema, certifique-se de ter adicionado os IDs de app móvel apropriados para iOS e Android à página de parceiros do Google.

### Por que recebi um e-mail de credenciais inválidas do Google Ads quando o dashboard ainda mostra como conectado? {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

A Braze envia esse e-mail automaticamente quando a API do Google retorna um erro de autorização. Isso pode acontecer mesmo quando o **Google Ads** ainda aparece como conectado no dashboard e os públicos parecem estar sincronizando — por exemplo, quando a conta do Google conectada não tem permissão para uma ação específica solicitada pelo Google, ou quando os termos de serviço do Google Ads ainda precisam ser aceitos para a conta.

Alguns erros de autorização se resolvem sozinhos. Verifique a análise de dados do **Audience Sync** no seu Canvas (por exemplo, *Usuários sincronizados* e *Usuários com erro*) para confirmar se os usuários ainda estão sendo sincronizados. Se os problemas continuarem, acesse **Integrações de Parceiros** > **Parceiros de Tecnologia** > **Google Ads**, encontre **Google Audience Sync** e use **Change Account** para reconectar com uma conta do Google Ads que tenha o acesso necessário e a configuração concluída.