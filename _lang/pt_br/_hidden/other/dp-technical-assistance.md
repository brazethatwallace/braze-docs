---
nav_title: Assistência técnica em proteção de dados
article_title: Assistência técnica de proteção de dados nos Serviços Braze
page_order: 1
description: "Esta página fornece instruções técnicas para que você gerencie, por meio dos Serviços Braze, solicitações de indivíduos em relação a seus direitos de dados pessoais."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Assistência técnica de proteção de dados nos Serviços Braze {#data-protection-technical-assistance-in-the-braze-services}

Há uma série de leis de proteção de dados que regulam o que as organizações podem fazer com dados pessoais ("Leis de Proteção de Dados"), incluindo o Regulamento Geral de Proteção de Dados da UE e do Reino Unido ("GDPR"), a Lei de Privacidade do Consumidor da Califórnia ("CCPA") e a Lei de Portabilidade e Responsabilidade de Seguros de Saúde ("HIPAA"). Existem outras leis e regulamentações nacionais, estaduais e específicas do setor que podem se aplicar ao seu negócio.

Essas Leis de Proteção de Dados concedem aos indivíduos "direitos de privacidade" sobre seus dados pessoais. As organizações são obrigadas a receber e responder a solicitações de indivíduos que exercem seus direitos de privacidade. Os Serviços Braze podem ajudar você a cumprir essas Leis de Proteção de Dados, fornecendo recursos para facilitar determinadas ações exigidas por essas leis. Este documento fornece instruções técnicas para usar esses recursos para gerenciar solicitações de direitos de privacidade. Cabe a você determinar quais Leis de Proteção de Dados se aplicam ao seu negócio e agir em conformidade com elas.

## Aviso legal {#legal-disclaimer}

Nada do que está descrito a seguir pretende ser, nem deve ser interpretado como, aconselhamento jurídico da Braze. Recomendamos que você busque orientação do seu próprio advogado em relação à sua situação específica e a como as Leis de Proteção de Dados se aplicam a você e ao seu uso dos Serviços da Braze.

## Terminologia {#terminology}

Para os fins deste documento, qualquer referência a dados pessoais também pode ser entendida como uma referência a informações pessoais ou informações de identificação pessoal ("Dados Pessoais"). Por questões de simplicidade, geralmente nos baseamos na linguagem do GDPR ao abordar os direitos dos usuários finais. A linguagem do GDPR é frequentemente intercambiável ou está estreitamente alinhada com um termo ou conceito definido em outras Leis de Proteção de Dados.

## Conceitos básicos {#the-basics}

A maioria das leis de privacidade define três partes principais envolvidas no processamento de Dados Pessoais: titulares dos dados, controladores de dados e processadores de dados. Cada grupo tem direitos e responsabilidades diferentes em relação ao uso de Dados Pessoais:

- Um titular dos dados é um indivíduo cujos Dados Pessoais estão sendo processados pelo processador de dados ou controlador de dados
- Um controlador de dados é uma entidade que determina as finalidades e os meios do processamento de Dados Pessoais
- Um processador de dados é uma entidade que processa Dados Pessoais em nome e conforme as instruções do controlador de dados

Em relação aos Serviços da Braze:

- Os titulares dos dados são, por exemplo, os usuários finais do seu aplicativo para clientes (por exemplo, seus clientes) ou seus colaboradores que são usuários da empresa na sua instância dos Serviços da Braze.
- Você, o cliente da Braze, é o controlador de dados que decide como e por que os Dados Pessoais dos titulares dos dados serão coletados e processados dentro dos Serviços da Braze.
- A Braze é um processador de dados que processa Dados Pessoais nos Serviços da Braze em seu nome e de acordo com as instruções que recebemos de você.

Os termos acima são do GDPR, mas, por exemplo, termos comparáveis na CCPA são:
- "consumidores" para titulares dos dados.
- "empresas" para controladores de dados.
- "prestadores de serviço" para processadores de dados.

Abaixo, você encontrará informações relevantes sobre as solicitações de direitos de privacidade mais comuns feitas por titulares dos dados, incluindo como respondê-las por meio dos recursos técnicos dos Serviços da Braze.

## O direito de ser informado {#the-right-to-be-informed}

O direito de ser informado abrange sua obrigação de fornecer "informações de processamento justo", geralmente por meio de um aviso de privacidade. Ele enfatiza a necessidade de transparência sobre como você usa dados pessoais.

### Recomendação da Braze {#braze-recommendation}

A maioria das leis de proteção de dados enfatiza a necessidade de transparência em relação ao uso de dados pessoais. Essa é a responsabilidade dos controladores de dados, que normalmente mantêm um aviso de privacidade facilmente acessível aos usuários de seus produtos e serviços e que abrange o processamento realizado pela Braze.

## O direito de acesso {#the-right-of-access}

De acordo com as leis de proteção de dados, os titulares de dados podem ter o direito de obter:

- Confirmação de que seus dados pessoais estão sendo processados,
- Acesso aos seus dados pessoais, e
- Outras informações complementares conforme determinado pela lei de proteção de dados aplicável.

### Recomendação da Braze

Para fornecer dados pessoais da Braze em um formato legível por máquina em resposta a uma solicitação de acesso de um titular de dados, você pode exportar o perfil do usuário final fazendo uma chamada de API para as [REST APIs]({{site.baseurl}}/api/endpoints/export) da Braze usando o identificador do usuário (definido por você como o `external_id` fornecido à Braze) e/ou o identificador do dispositivo.

#### BrazeAI Decisioning Studio™

Para atender a uma solicitação de direito de acesso em relação a dados pessoais no BrazeAI Decisioning Studio™, entre em contato com seu gerente de conta informando os customer_id(s) e/ou e-mail(s) relevantes.

## O Direito de Retificação {#the-right-to-rectification}

Os indivíduos têm o direito de solicitar a correção de Dados Pessoais que estejam incorretos ou incompletos. Se você divulgou os Dados Pessoais em questão a terceiros, considere a necessidade de informá-los sobre a retificação, sempre que possível.

### Recomendação da Braze

Caso um Titular de Dados solicite que você corrija imprecisões nos Dados Pessoais sendo processados por você ou pela Braze em seu nome, você pode usar os SDKs da Braze ou as [REST APIs]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze para corrigir esses Dados Pessoais.

## O direito ao apagamento {#the-right-to-erasure}

O direito ao apagamento também é conhecido como "o direito ao esquecimento" ou "direito à exclusão".

### Recomendação da Braze

#### Exclusão padrão {#standard-deletion}

Depois de interromper a coleta de dados, você pode usar o [endpoint de exclusão de usuários da REST API da Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) para excluir um usuário final, o que removerá todos os registros desse usuário final dos serviços da Braze:

- Para usuários finais que possuem um external_id nos serviços da Braze, você pode usar esse ID para excluir os dados desse usuário final.
- Para usuários anônimos que não possuem um external_id nos serviços da Braze, você pode recuperar o identificador de dispositivo desse usuário final usando o SDK da Braze e pode usar o identificador de dispositivo para encontrar o perfil de usuário final associado àquele dispositivo. Em seguida, você pode usar a API de exclusão de usuários para excluir o perfil associado a esse usuário final.

A exclusão de um usuário final dos serviços da Braze excluirá permanentemente o perfil de usuário centralizado da Braze para esse usuário final, conforme definido pelo `external_id` fornecido. Isso inclui informações estruturadas do perfil que a Braze coletou por padrão ou que você configurou os serviços da Braze para coletar, como informações de dispositivo, país, idioma e endereço de e-mail.

Observe que o endereço de e-mail ou número de telefone associado ao perfil do usuário final ainda pode estar armazenado na Braze, pois podem estar associados ao perfil de outro usuário final. Endereços de e-mail e números de telefone não são únicos nos serviços da Braze. Isso significa que sua equipe pode ter configurado a Braze para armazenar o mesmo endereço de e-mail ou número de telefone em vários perfis de usuário. Se sua equipe configurou a Braze dessa forma, saiba que pode ser necessário excluir todos os perfis de usuário que representam um determinado titular dos dados para cumprir uma solicitação de exclusão de um titular dos dados, e sua equipe precisará fazer várias chamadas de API para excluir todos os perfis de usuário que se referem a um determinado titular dos dados.

#### BrazeAI Decisioning Studio™

Para atender a uma solicitação de direito ao apagamento em relação a dados pessoais no BrazeAI Decisioning Studio™, entre em contato com seu gerente de conta com os customer_id(s) e/ou e-mail(s) relevantes. Seu gerente de conta pode providenciar a exclusão de todos os dados pessoais associados encontrados no data warehouse.

#### Considerações adicionais sobre exclusão {#additional-deletion-considerations}

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
  <caption>Considerações adicionais sobre exclusão</caption>
<tbody>
  <tr>
    <td>
        <p>Os clientes podem criar campos personalizados para propriedades de eventos e extras de mensagem. Esses campos não são destinados a dados pessoais e, como resultado, não estão incluídos no processo de exclusão padrão descrito acima. No entanto, se você usar a Braze para inserir ou coletar dados pessoais por meio de propriedades de eventos e extras de mensagem, você pode configurar o processo de exclusão acionado pelo endpoint de exclusão de usuários da REST API para incluir também esses campos, de modo que os dados contidos neles sejam excluídos.</p>
        <p>As configurações padrão são aplicadas no nível da empresa, mas você pode optar por excluir os seguintes campos quando o processo de exclusão for executado, no nível do grupo de apps/espaço de trabalho:</p>
    <ul>
        <li>PROPERTIES para USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES para USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS para:
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Futuros eventos de envio de mensagem</li>
            </ul>
        </li>
    </ul>
    <p>As configurações para isso podem ser acessadas em <b>Configurações da empresa</b> > <b>Configurações de administrador</b> > <b>Configurações de segurança</b>. As preferências de exclusão de dados são definidas por tipo de evento ou categoria. Somente um usuário com permissões de Administrador pode fazer alterações nessas configurações. Alternativamente, um Administrador pode delegar essas permissões a outro usuário.</p>
    <p>Se um tipo de evento ou extra de mensagem estiver configurado para ser incluído no processo de exclusão, os dados nesse campo serão excluídos daqui em diante para os usuários para os quais você estiver executando o endpoint de exclusão de usuários da REST API. Além disso, quando você selecionar essa preferência de exclusão, no próximo trabalho de exclusão agendado, os dados desses campos serão excluídos de quaisquer conjuntos de dados anonimizados existentes que contenham esses campos. Não será possível restaurar os campos de dados excluídos.</p>
    </td>
  </tr>
</tbody>
</table>

#### Análise de dados {#analytics}

Para manter a integridade das análises de uso de Campaigns e do app, os dados agregados anônimos não serão modificados quando um usuário final for excluído. Por exemplo, a Braze não diminuirá o número total de sessões de um app quando um usuário final for excluído. A(s) sessão(ões) em que esse usuário final visitou o app ainda serão incluídas no número total de visitas a esse app, mas esses dados não estarão conectados de forma alguma ao perfil do usuário final esquecido, garantindo que esses dados anonimizados e agregados não possam ser vinculados a um usuário final individual.

As análises dentro dos serviços da Braze estão vinculadas ao identificador de usuário final da Braze. Após a exclusão do perfil do usuário final, o identificador de usuário da Braze se torna efetivamente um identificador completamente anonimizado, pois a Braze não consegue vinculá-lo de volta a nenhum usuário final individual.

#### Após a exclusão ter ocorrido {#once-deletion-has-happened}

Geralmente, espera-se que você faça esforços razoáveis para notificar os titulares dos dados quando tiver cumprido a solicitação deles de apagar seus dados pessoais. Um usuário final excluído pode se registrar novamente ou voltar a interagir com seu app ou serviço em uma data posterior, e a Braze não será capaz de identificá-lo como o usuário excluído ou esquecido. Os serviços da Braze não são capazes de criar listas de identificadores de usuários excluídos ou endereços de e-mail em seu nome.

## O direito à restrição de processamento {#the-right-to-restriction-of-processing}

Os titulares dos dados podem ter o direito de "bloquear" ou suprimir o processamento de seus Dados Pessoais em determinadas circunstâncias. Restringir o processamento significa não realizar nenhum processamento ao qual o titular dos dados tenha se oposto.

### Recomendação da Braze

Os serviços da Braze não oferecem suporte à restrição de processamento de categorias individuais de Dados Pessoais. Se um titular de dados solicitou que você restrinja o processamento de determinados subconjuntos dos Dados Pessoais desse titular, você deve usar as [APIs da Braze]({{site.baseurl}}/api/home) para exportar o(s) perfil(is) completo(s) desse usuário final e, em seguida, [excluí-lo(s)]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) da Braze. As APIs da Braze podem ser usadas para reimportar esses dados caso o usuário final permita posteriormente que você processe esses subconjuntos específicos de seus Dados Pessoais. Além disso, você deve recomendar que seu usuário final desinstale ou faça logout de todos os seus aplicativos que usam o SDK da Braze para interromper a coleta de quaisquer dados adicionais sobre o titular dos dados.

Para clientes que utilizam apenas o BrazeAI Decisioning Studio™, você não deve mais enviar dados ao Decisioning Studio.

## O direito à portabilidade de dados {#the-right-to-data-portability}

O direito à portabilidade de dados permite que os titulares de dados obtenham e reutilizem seus dados pessoais para seus próprios fins em diferentes serviços. Os dados pessoais devem ser fornecidos em um formato estruturado, legível por máquina e de uso comum.

### Recomendação da Braze

Assim como no direito de acesso, você pode usar a [REST API]({{site.baseurl}}/api/endpoints/export) da Braze para exportar os dados pessoais de um usuário final e fornecê-los ao titular dos dados conforme a solicitação. Além disso, fale com seu gerente de conta com os `customer_id`(s) e/ou e-mail(s) relevantes para solicitar uma cópia de quaisquer dados pessoais armazenados no BrazeAI Decisioning Studio.

## O direito de objeção {#the-right-to-object}

Os indivíduos podem ter o direito de se opor a:

- processamento baseado em interesses legítimos ou na execução de uma tarefa de interesse público/exercício de autoridade oficial (incluindo criação de perfil);
- marketing direto (incluindo criação de perfil); e
- processamento para fins de pesquisa científica/histórica e estatísticas.

### Recomendação da Braze

A Braze oferece a capacidade de marcar um perfil de usuário como tendo cancelado a inscrição de SMS, e-mails ou notificações por push, tanto por meio das nossas [REST APIs]({{site.baseurl}}/api/home) quanto pelos SDKs para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes) e [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes). Se você receber objeções de titulares de dados sobre o recebimento dessas mensagens, pode usar as APIs da Braze para cancelar a inscrição desses usuários finais.

Se isso não for suficiente, para evitar o processamento de dados pessoais do usuário final pela Braze, o perfil do usuário final deve ser excluído da mesma forma especificada em "Direito à exclusão".

## Direitos relacionados à tomada de decisões automatizada e à criação de perfis {#rights-related-to-automated-decision-making-and-profiling}

Algumas leis de proteção de dados proíbem, ou permitem que titulares de dados optem por não participar de, tomadas de decisões automatizadas ou criação de perfis em determinadas circunstâncias, em particular para decisões que "produzem um efeito legal ou um efeito igualmente significativo sobre o indivíduo."

### Recomendação da Braze

A Braze não realiza nenhuma ação automatizada de criação de perfis ou tomada de decisões com ramificações legais ou equivalentes para os titulares de dados. Se você acredita que o seu próprio uso dos Serviços da Braze terá impactos legais ou equivalentes e recebeu uma objeção a isso, pode optar por excluir o perfil de usuário da mesma forma descrita em "Direito à exclusão."

## Publicidade direcionada {#targeting-advertising}

De acordo com algumas leis estaduais de privacidade dos EUA, os titulares de dados podem se opor ao uso de seus dados pessoais para fins de publicidade direcionada.

### Recomendação da Braze

Ao criar públicos com o objetivo de direcionar anúncios aos seus titulares de dados, você deve garantir que excluiu todos os titulares de dados que se opuseram à publicidade direcionada, como, por exemplo, consumidores da Califórnia que exerceram seu direito de "Não Vender ou Compartilhar" nos termos da CCPA.

Para saber mais sobre como criar públicos para sincronizar com plataformas de terceiros, consulte [Audience sync]({{site.baseurl}}/partners/canvas_audience_sync).

## O direito à não discriminação {#the-right-to-non-discrimination}

Os titulares de dados têm o direito de exercer seus direitos de privacidade sem sofrer discriminação.

### Recomendação da Braze

Ao utilizarem os Serviços da Braze, os clientes devem garantir que não discriminem os titulares de dados que exerceram seus direitos de privacidade. Por exemplo, recomendamos que os titulares de dados que exerceram seus direitos de privacidade não sejam segmentados em públicos nem direcionados de forma que possa resultar em discriminação contra eles.