---
nav_title: SCIM
article_title: SCIM 엔드포인트
search_tag: Endpoint
page_order: 5
layout: dev_guide
alias: /scim/

description: "이 랜딩 페이지에는 Braze SCIM 엔드포인트가 나열되어 있습니다."
page_type: landing

guide_top_header: "SCIM 엔드포인트"
guide_top_text: "[크로스 도메인 ID 관리 시스템(SCIM)](http://www.simplecloud.info/) 사양은 사용자 및 그룹을 표현하는 정의된 스키마를 제공하여 클라우드 기반 애플리케이션 및 서비스에서 사용자 ID를 보다 쉽게 관리할 수 있도록 설계되었습니다. Braze SCIM 엔드포인트를 사용하여 자동화된 사용자 프로비저닝을 관리하세요."

guide_featured_title: ""
guide_featured_list:
  - name: "POST: 새 대시보드 사용자 계정 생성"
    link: /docs/post_create_user_account
    image: /assets/img/braze_icons/plus-circle.svg
  - name: "GET: 리소스 ID로 기존 대시보드 사용자 계정 조회"
    link: /docs/get_see_user_account_information
    image: /assets/img/braze_icons/eye.svg
  - name: "GET: 이메일로 기존 대시보드 사용자 계정 검색"
    link: /docs/api/endpoints/scim/get_search_existing_dashboard_user
    image: /assets/img/braze_icons/eye.svg
  - name: "PUT: 대시보드 사용자 계정 업데이트"
    link: /docs/post_update_existing_user_account
    image: /assets/img/braze_icons/pencil-01.svg
  - name: "DELETE: 대시보드 사용자 계정 제거"
    link: /docs/delete_existing_dashboard_user
    image: /assets/img/braze_icons/trash-01.svg
---


## 대시보드 액세스 권한이 있는 사용자 목록을 내보내는 방법 {#how-to-export-a-list-of-users-with-dashboard-access}

이 워크플로를 사용하여 Braze 대시보드에 액세스할 수 있는 사용자를 감사할 수 있습니다.

1. **설정** > **관리자 설정** > **보안 설정** > **보안 이벤트 다운로드**에서 보안 이벤트 보고서를 다운로드합니다.
2. 보고서에서 사용자 이메일을 추출합니다.
3. 각 이메일에 대해 [GET: 이메일로 기존 대시보드 사용자 계정 검색]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user)을 사용하여 사용자 세부 정보를 조회합니다.
4. 필요한 경우 반환된 리소스 `id`를 [GET: 리소스 ID로 기존 대시보드 사용자 계정 조회]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information)와 함께 사용하여 추가 사용자 세부 정보를 확인합니다.

전체 SCIM 엔드포인트 목록은 [SCIM 엔드포인트]({{site.baseurl}}/api/endpoints/scim)를 참조하세요. 보고서 소스에 대한 자세한 내용은 [보안 이벤트 보고서 다운로드]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report)를 참조하세요.