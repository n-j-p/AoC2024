import day21
import itertools as it
nkp = day21.NumericKeypad()
def test_A_positions():
    print(nkp.gen_positions('A'))
    assert nkp.gen_positions('A') == [(3,2),(3,2)]
def test_A_seq():
    for  i, x in enumerate(nkp.gen_seq('A')):
        print('   ',i+1, x)
    # For some reason when there is just one step tuples/lists get
    # mixed up...
    assert list(list(nkp.gen_seq('A'))[0]) == [[(3,2),(3,2)]]
def test_3_positions():
    print(nkp.gen_positions('3'))
    assert nkp.gen_positions('3') == [(3,2),(2,2)]
def test_3_seq():
    assert list(list(nkp.gen_seq('3'))[0]) == [[(3,2),(2,2)]]
def test_642_positions():
    print(list(nkp.gen_positions('642')))
    assert list(nkp.gen_positions('642')) == [(3,2),(1,2),(1,0),(2,1)]
def test_A64_seq():
    for  i, x in enumerate(nkp.gen_seq('A64')):
        print('   ',i+1, x)
    assert list(nkp.gen_seq('A64')) == [([(3,2),(3,2)],
                                         [(3,2),(2,2),(1,2)],
                                         [(1,2),(1,1),(1,0)])]
    
def test_64_seq():
    for  i, x in enumerate(nkp.gen_seq('64')):
        print('   ',i+1, x)
    assert list(nkp.gen_seq('64')) == [(
                                         [(3,2),(2,2),(1,2)],
                                         [(1,2),(1,1),(1,0)])]
def test_642_seq():
    print(list(nkp.gen_seq('642')))
    for  i, x in enumerate(nkp.gen_seq('642')):
        print('   ',i+1, x)
    
    assert list(nkp.gen_seq('642')) == [([(3,2),(2,2),(1,2)],
                                         [(1,2),(1,1),(1,0)],
                                         [(1,0),(1,1),(2,1)]),
                                         ([(3,2),(2,2),(1,2)],
                                         [(1,2),(1,1),(1,0)],
                                         [(1,0),(2,0),(2,1)]),
                                        ]
                                      
def test_A9550_positions():
    assert list(nkp.gen_positions('A9550')) == [(3,2),(3,2),(0,2),(1,1),(1,1),(3,1)]
    
def test_fill_in_A9():
    g = nkp._fill_in((3,2),(0,2))
    assert list(g) == [[(3,2),(2,2),(1,2),(0,2)]]
    
def test_fill_in_95():
    g = nkp._fill_in((0,2),(1,1))
    assert sorted(list(g)) == [[(0,2),(0,1),(1,1)],
                               [(0,2),(1,2),(1,1)]]
                
def test_9550_seq():
    g = nkp.gen_seq('9550')
    assert next(g) == ([(3, 2), (2, 2), (1, 2), (0, 2)], 
                       [(0, 2), (0, 1), (1, 1)], 
                       [(1, 1), (1, 1)], 
                       [(1, 1), (2, 1), (3, 1)])
    assert next(g) == ([(3, 2), (2, 2), (1, 2), (0, 2)], 
                       [(0, 2), (1, 2), (1, 1)], 
                       [(1, 1), (1, 1)], 
                       [(1, 1), (2, 1), (3, 1)])
def test_A9550_seq():
    g = nkp.gen_seq('A9550')
    assert next(g) == ([(3,2), (3,2)],
                       [(3, 2), (2, 2), (1, 2), (0, 2)], 
                       [(0, 2), (0, 1), (1, 1)], 
                       [(1, 1), (1, 1)], 
                       [(1, 1), (2, 1), (3, 1)])
    assert next(g) == ([(3,2), (3,2)],
                       [(3, 2), (2, 2), (1, 2), (0, 2)], 
                       [(0, 2), (1, 2), (1, 1)], 
                       [(1, 1), (1, 1)], 
                       [(1, 1), (2, 1), (3, 1)])
def test_fill_in_AA():
    g = nkp._fill_in((3,2),(3,2))
    assert list(g) == [[(3,2),(3,2)]]
def test_008_str():
    # Test double press
    g = nkp.gen_seq('008')
    assert [nkp._conv_to_str(ng) for ng in g] ==['<AA^^^A']

def test_A64_str():
    seq = next(nkp.gen_seq('A64'))
    assert nkp._conv_to_str(seq) == 'A^^A<<A'

def test_A_str():
    seq = next(nkp.gen_seq('A'))
    assert nkp._conv_to_str(seq) == 'A'

def test_3_str():
    seq = next(nkp.gen_seq('3'))
    assert nkp._conv_to_str(seq) == '^A'

def test_A39AA_str():
    seq = next(nkp.gen_seq('A39AA'))
    assert nkp._conv_to_str(seq) == 'A^A^^AvvvAA'

def test_642_str():
    g = nkp.gen_seq('642')
    assert nkp._conv_to_str(next(g)) == '^^A<<A>vA'
    assert nkp._conv_to_str(next(g)) == '^^A<<Av>A'
def test_63A_str():
    assert nkp._conv_to_str(next(nkp.gen_seq('63A'))) == '^^AvAvA'

def test_029A_str():
    g = nkp.gen_seq('029A')
    assert sorted([nkp._conv_to_str(ng) for ng in g]) == \
           sorted(['<A^A>^^AvvvA','<A^A^>^AvvvA','<A^A^^>AvvvA'])

def test_01_str():
    # Testing whether we avoid gap
    g = nkp.gen_seq('01')
    assert len([nkp._conv_to_str(ng) for ng in g]) == 1


     
def test_directional_keypad():
    nkp = day21.NumericKeypad()
    seqs0 = nkp.gen_all_seqs('029A')
    dkp = day21.DirectionalKeypad()
    seqs1 = it.chain.from_iterable([dkp.gen_all_seqs(s0) for s0 in seqs0])
    assert 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A' in seqs1

def test_directional_keypad2():
    nkp = day21.NumericKeypad()
    seqs0 = nkp.gen_all_seqs('029A')
    dkp1 = day21.DirectionalKeypad()
    seqs1 = it.chain.from_iterable([dkp1.gen_all_seqs(s0) for s0 in seqs0])
    dkp2 = day21.DirectionalKeypad()
    seqs2 = it.chain.from_iterable([dkp2.gen_all_seqs(s1) for s1 in seqs1])
    assert '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A' in seqs2

def test_sample_input():
    sample_seqs = ['029A',
                   '980A',
                   '179A',
                   '456A',
                   '379A']
    
    assert day21.part1_semiBF(sample_seqs) == 126384


