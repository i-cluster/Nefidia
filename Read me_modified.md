# Read me

-----

> [toc]



## Netfidia Movies



### 1. 프로젝트 정보

| 팀 구성       | 업무 내용                                                    |
| ------------- | ------------------------------------------------------------ |
| (팀장) 이준희 | Django Model 구성, 데이터 베이스 구축 및 관리(API 이용), Vue axios(로그인,회원가입,front-back연결) |
| (팀원) 구영지 | Django Model 구성, UI 기획 적용한 Vue 페이지 구성, Vue component 관리 및 Vue axios, CSS 및 부트스트랩, |

프로젝트 기간 : 2020.11.19 ~ 2020.11.26



### 2. 프로젝트 목표

- 개인화된 영화 추천 알고리즘
- 비슷한 영화 취향을 가진 사용자들이 이 커뮤니티 사이트에서 모여 서로의 영화 후기를 공유하고 댓글과 팔로잉으로 소통할 수 있습니다.



### 3. 프로젝트가 제공하는 서비스 기능

주요기능

- 영화 정보 기반 개인 맞춤 추천 서비스
- 커뮤니티 서비스 (리뷰 작성 및 수정, 댓글 작성 기능)
- HTML, CSS, JavaScript, Vue.js, Django, REST API, DataBase 등을 활용한 실제 서비스 설계





### Frotend (Vue.js)

-----



#### 1.최종 화면 구성

* 처음 사이트 접속 시, Login 페이지

로그인 페이지 이미지 삽입

* Login 페이지 하단에 있는 Signup 버튼을 클릭하면 Signup 페이지로 이동

사입업 페이지 이미지 삽입

* Login 후에는 Home 페이지가 메인 페이지로 나타남

메인 홈페이지 이미지 삽입



#### 2. Signup/Login 페이지 구성

* 처음 Netfidia 사이트 접속 시에, 가장 먼저 Login 페이지가 뜨고 하단부에 Signup 페이지로 이동하는 링크를 만들었다. App에서 router로 연결된 Login과 Signup 페이지는 각각 LoginForm 과 SignupForm component로 연결된다.
* Signup 페이지에서는 선호하는 영화 장르와 더 구체적으로는 선호하는 영화의 세부적인 테마를 선택하도록 하여 개인화된 추천 알고리즘의 데이터로 활용할 수 있게 하였다. 



#### 2. Home 페이지 구성

##### Nav Bar

* Netfidia 로고 클릭으로도 홈페이지 이동 가능
* search 기능 구현 - 영화 제목에 기반해 검색할 수 있다. (보류)



##### Main Movie List

* 영화 추천 알고리즘에 따라 선정된 영화 리스트들 중에서 1순위로 추천하는 영화 이미지를 상단에서 보여준다.
* 이후 하단을 수평 그리드로 나누어 사이트 알고리즘 기반 개인화 영화 추천 리스트, 사이트 유저들에게 인기가 많은 영화 리스트, 박스 오피스 리스트를 캐러셀 형태로 라이브하게 보여준다.
* 사용자 입장에서 한 눈에 영화 리스트들이 들어오도록 화면을 수평적으로 4개의 단으로 구성했다.



#### 3. Movie 페이지 구성

##### Movie Detail

* 메인 Home 페이지에서 클릭한 영화의 정보들을 불러와서 화면의 좌측에 보여준다.
* 불러오는 영화의 정보는 영화의 포스터, 제목, 감독, 출연자, 줄거리, 테마를 나타내는 해시태그, 평점이며 마지막으로 크레딧 영상을 캐러셀형태로 덧붙였다. 



##### Review

* 메인 Home 페이지에서 클릭한 영화의 리뷰를 작성하고 다른 유저들의 리뷰를 볼 수 있는 게시판을 화면 우측에 보여준다.
* ReviewForm component를 불러온다.
* 해당 영화의 리뷰를 작성할 수 



##### Comment 





##### Like





##### Follow



#### 4. Profile 페이지 구성

##### Admin Page

* Django에서 제공하는 기본 기능 활용









#### 5. Frontend 작업 중에 겪은 문제상황 및 해결

* 



#### 6. 종합 : 향후 프로젝트를 위한 제안







### Backend (Django)

---------

#### 1. 초기 파일 및 환경설정 세팅

>  협업을 위한 버전 및 툴을 requirements.txt에 정리

Django == 3.1.3

asgiref==3.3.1

django-extensions==3.0.6    

django-cors-headers==3.5.0    

djangorestframework==3.12.2    

djangorestframework-jwt==1.11.0    

PyJWT==1.7.1    

pytz==2020.4    

sqlparse==0.4.1

Vue.js == 4.5.8

python == 3.9.0

node == 14.15.0

npm == 6.14.8



#### 2. 데이터베이스 모델링 (ERD)



#### 3. 영화 추천 알고리즘 구현





#### 3. URL 만들기

* 

```python

```





#### 4. Model 만들기

* 

```python

```





#### 5. Serializer 만들기

* 

```python

```





#### 6. Views.py 

* 

```python

```





#### 7. Settings.py

* 

```python

```





#### 8. Backend 작업 중에 겪은 문제상황 및 해결

* 



#### 9. 종합 : 향후 프로젝트를 위한 제안







