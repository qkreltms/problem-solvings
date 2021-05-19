import re

def solution(new_id):
    st = new_id
    st = st.lower()
    # sub => 해당되는 정규식 어떤 값으로 변환해 반환
    st = re.sub('[^a-z0-9\-_.]', '', st)
    # .이 여러개 있으면
    st = re.sub('\.+', '.', st)
    # .으로 시작하거나 끝나면
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st