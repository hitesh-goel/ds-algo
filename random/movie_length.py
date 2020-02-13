# are there any 2 movies in an array whose lenghts are equal to duration of flight


def movies_available(ft, movies):
    m_set = set()
    for fm in movies:
        sm = ft - fm
        if sm in m_set:
            return True
        m_set.add(fm)
    return False


def main():
    movies = [90, 80, 100, 20, 110, 130]
    ft = 180
    assert(movies_available(ft, movies) == True)


main()
