class KunInfoAnswer:
    def request(self, keyword: str):
        try:
            return self.request_debug(keyword)
        except Exception as e:
            print(e)
            return "죄송합니다. 오류가 발생 했어요"

    def request_debug(self, Keyword: str):
        if "수강신청" in Keyword:
            answer = "수강신청일정은 2.23(수) ~ 2.25(금) 10:00 ~ 17:00 입니다. :D <br> 2.23(수): 1,4학년 <br> 2.24(목): 2,3학년 <br> 2.25(금): 전학년 대상 <br> <a href=\"https://sugang.kangwon.ac.kr/\" target='_blank'>수강신청 바로가기</a>"

        elif "정정" in Keyword:
            answer = "수강신청 정정기간은 3.4(금), 3.7(월) ~ 3.8(화) 10:00 ~ 17:00 입니다. ^_^ <br> <a href=\"https://sugang.kangwon.ac.kr/\" target='_blank'>수강신청 정정 바로가기</a>"

        elif "강의계획서" in Keyword:
            answer = "강의계획서는 KCloud - 학부생서비스 - 교과 - 수업 - 강의계획서에서 확인 할 수 있습니다. <br> <a href=\"https://kcloud.kangwon.ac.kr/\" target='_blank'>KCloud</a>"
            
        elif "강의평가" in Keyword:
            answer = "강의평가는 KCloud - 학부생서비스 - 교과 - 수업 - 강의평가에서 확인 할 수 있습니다. <br> <a href=\"https://kcloud.kangwon.ac.kr/\" target='_blank'>KCloud</a> <br> *강의 평가시 학점 확인 가능"

        elif "학사일정" in Keyword:
            answer = "학사일정을 확인하는 사이트를 알려드릴게요. <a href=\"https://www.kangwon.ac.kr/www/selectTnSchafsSchdulListUS.do?sc1=%ED%95%99%EC%82%AC%EC%9D%BC%EC%A0%95&key=156&\" target='_blank'>학사일정 확인하기</a>"

        elif "학교지도" in Keyword or "지도" in Keyword:
            answer = "학교지도를 띄워드릴게요. :D <br> <script>window.open('/static/img/knu.html','popup','width=800, height=600, left=700, top=150')</script>"

        elif "학식" in Keyword or "학생식당" in Keyword:
            answer = "<script>window.open('/static/img/map_restaurant.html','popup','width=800, height=600, left=700, top=150')</script>강원대 학생식당은 천지관, 백록관, 석재관, 두리관이 있습니다. <br> 추천메뉴 <br> 백록관 - 치킨까스, 해장라면 <br> 석재관 - 닭갈비알밥돌솥, 짬뽕 <br> 천지관 - 딱히 없어요 '_'  <br> 두리관 - 닭갈비뚝배기 "

        elif "동아리" in Keyword:
            answer = "강원대에는 여러 종류의 중앙동아리가 존재합니다. <br> <a href=\"https://clubknu.modoo.at/\" target='_blank'>동아리 정보 보러가기</a>"

        elif "부전공" in Keyword or "복수전공" in Keyword:
            answer = "부.복수전공 신청 기간은 2022.11.16(수) ~ 2022.11.25(금)이며 최대 2개까지 신청할 수 있습니다. <br> 복수전공은 부전공에 비하여 이수해야 하는 학점이 많으며 졸업요건을 만족해야 합니다."

        elif "와이파이" in Keyword or "wifi" in Keyword:
            answer = "학교에서 무료로 제공하는 Wifi가 존재합니다. <br> <a href=\"https://kangwonuniv.notion.site/f4b2290d3a5d4ed0b2921874cd344824/\" target='_blank'>Wifi 비밀번호 확인하러가기</a>"

        elif "장학금" in Keyword:
            answer = "학교 장학금 관련 정보는 https://www.kangwon.ac.kr/www/contents.do?key=227&에서 확인 가능합니다 :D <a href=\"https://www.kangwon.ac.kr/www/contents.do?key=227&/\" target='_blank'>바로가기</a>"

        elif "수업시간" in Keyword:
            answer = "수업시간 정보는 https://www.kangwon.ac.kr/www/contents.do?key=2069&에서 알 수 있습니다. <br> <a href=\"https://www.kangwon.ac.kr/www/contents.do?key=2069&\" target='_blank'>바로가기</a> "

        elif "봉사활동" in Keyword:
            answer = "수강신청에서 봉사활동 신청후 <a href=\"https://bongsa.kangwon.ac.kr/login/loginPage.do\" target='_blank'>https://bongsa.kangwon.ac.kr/login/loginPage.do</a>에서 신청할 수 있습니다. 추가적인 정보는 <a href=\"https://knuserv.kangwon.ac.kr/\" target='_blank'>https://knuserv.kangwon.ac.kr/</a>에서 확인 가능합니다."

        elif "술집" in Keyword:
            answer = "알려두리가 추천하는 술집 리스트 '^' <br> 후문 - 주동아리, 치치, 파파야 <br> 애막골 - KMGM, 예술관, 시리우스"

        elif "맛집" in Keyword:
            answer = "알려두리가 추천하는 맛집 리스트 '^' <br> 후문 - 숨어있는 고기집, 멘시루, 노란   <br> 애막골 - 가마솥 순대국, 니하오 양꼬치, 미가쭈꾸미 "

        elif "웹메일" in Keyword:
            answer= "웹 메일은 <a href=\"https://kcloud.kangwon.ac.kr/\" target='_blank'>K-Cloud</a>에 접속하여 웹메일 클릭 → 계정 생성하여 사용이 가능합니다. <br> *웹메일을 통해 에브리 타임등 학교 인증이 가능합니다."

        elif "학생증" in Keyword:
            answer = "신한 SOL 앱에서 만들거나 신한은행 강원대점에 방문하여 만들 수 있습니다. <br> *주민등록증, 증명사진 지참"

        elif "워드" in Keyword or "한글" in Keyword or "파워포인트" in Keyword:
            answer = "학교 소프트웨어는 <a href=\"https://www.kangwon.ac.kr/itservice/selectBbsNttList.do?bbsNo=250&key=726&searchCtgry=Y&\" target='_blank'>여기</a>에서 다운로드 가능합니다. <br> *학교 네트워크로 접속시 사용 가능"

        elif "인쇄" in Keyword or "제본" in Keyword or "복사" in Keyword:
            answer = "인쇄, 복사, 제본은 천지관 복사실 또는 60주년 기념관 복사실에서 가능합니다. <br>*복사카드 필수"

        elif "기숙사" in Keyword:
            answer = "강원대의 기숙사는 이룸관, 새롬관, 퇴계관, 다산관, 재정생활관이 있습니다. <br> <script>window.open('/static/img/map_dormitory.html','popup','width=800, height=600, left=700, top=150')</script>*통금시간 - 01:00 ~ 05:00 어길시 벌점 부과"

        else:
            answer = "아직 제공되지 않는 정보에요 ㅠㅠ"

        return answer
