def solution(cacheSize, cities):
    answer = 0
    cache = []

    # 캐시 크기가 0이면 모든 도시가 cache miss
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()  # 대소문자 구분 X

        if city in cache:
            # cache hit
            answer += 1

            # 최근에 사용했으므로 맨 뒤로 이동
            cache.remove(city)
            cache.append(city)

        else:
            # cache miss
            answer += 5

            # 캐시가 가득 찼다면
            if len(cache) == cacheSize:
                # 가장 오래 사용하지 않은 도시 제거
                cache.pop(0)

            cache.append(city)

    return answer