def test_passing_1():
    assert ('home', 'work') == ('home', 'work')


def test_passing_2():
    assert 'QC' == 'QC'


def test_passing_3():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)


