'''
https://www.youtube.com/watch?v=V5-7GzOfADQ&ab_channel=AbdulBari
https://www.youtube.com/watch?v=WAzjfl7Pt_4&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
https://baeharam.github.io/posts/algorithm/kmp/
https://www.youtube.com/watch?v=UcjK_k5PLHI&ab_channel=%EC%BD%94%EB%93%9C%EC%97%86%EB%8A%94%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D
H와S문자열이있을 때 H안에 S가있는지 탐색한다.

H= ABAABAC가 있을 때S= ABAC를 찾는다면
브루트 포스 문자열 탐색 알고리즘:
ABAABAC
ABAC
 ABAC
  ABAC
   ...반복
n^2 시간 소요
KMP
S에 접두사, 접미사의 최대 일치길이 테이블을 구한다.
ABAC
0010

일치한게 일부분 있으면 테이블을 보고 적당히 스킵한다.
i=0, j=0,1
ABAABAC
ABAC => AB까지는 일치하지만 불일치 j=1 다음 i는부터는 B부터 비교한다.(i, j는 계속 증가)

i=1, j=1
ABAABAC
ABAC
...

'''
