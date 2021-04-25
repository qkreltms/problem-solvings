//링크
/*
문제: https://leetcode.com/problems/longest-palindromic-substring/
가장 긴 팰린드롬(뒤집어도 같음 예: 토마토)을 주어진 문자열의 부분문자열에서 찾아라
참고:
*/

//풀이 법
/*
bruteforce 방식
문자열을 순회하며 모든 부분문자열을 가져온다.
만약 h에 없는 문자열이라면 h에 넣고
팰린드롬인지 판별한다.
만약 h에 있다면 스킵하고 다음 부분문자열을 찾는다.
*/

//키포인트
/*
성능 최적화
문자열길이가 최대 1000개 
bruteforce 방법은 n^3, 최대 n^2으로 줄여야함
*/

const isP = (S) => {
  const r = S.split('').reverse().join('')
  if (r === S) {
    return true
  }
  return false
}
function splice(S, i, j) {
  return S.split('').splice(i, j + 1 - i).join('')
}
var longestPalindrome = function (S) {
  const h = {}
  const l = S.length
  const results = []
  for (let i = 0; i < l; i++) {
    for (let j = i; j < l; j++) {
      const s = splice(S, i, j)
      if (h[s]) {
        continue;
      }
      h[s] = s
      if (isP(s)) {
        results.push(s)
      }
    }
  }

  results.sort((a, b) => b.length - a.length)
  ans = results[0]
  return ans
};


// longestPalindrome('abba')
// longestPalindrome("abcdbbfcba")
longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")