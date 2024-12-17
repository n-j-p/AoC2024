import day17

def test_adv():
    test_comp = day17.Computer(A=41, B=3, C=None)
    test_comp.adv(2)
    assert test_comp.A == 41 // pow(2,2)

    test_comp = day17.Computer(A=18, B=3, C=None)
    test_comp.adv(5) 
    assert test_comp.A == 18 // pow(2,3)

def test_bxl():
    test_comp = day17.Computer(A=None, B=5, C=None)
    test_comp.bxl(3)
    assert test_comp.B == 6

def test_bst():
    test_comp = day17.Computer(A=5,B=123,C=55)
    test_comp.bst(6)
    assert test_comp.B == 55 % 8

def test_jnz():
    test_comp = day17.Computer(0,None,None)
    test_comp.inspo = 55
    test_comp.jnz(0)
    assert test_comp.inspo == 55
    test_comp = day17.Computer(6,None,None)
    test_comp.jnz(4)
    assert test_comp.inspo == 4 - 2

def test_bxc():
    test_comp = day17.Computer(0,12,65)
    test_comp.bxc(None)
    assert test_comp.B == 77 # == 12 ^ 65

def test_out():
    test_comp = day17.Computer(16,17,19)
    test_comp.out(3)
    test_comp.out(4)
    test_comp.out(6)
    assert test_comp.output == [3, 0, 3]

def test_first_program():
    test_comp = day17.Computer(None,None,9)
    test_comp.bst(6)
    assert test_comp.B == 1

def test_program1():
    test_comp = day17.Computer(None, None, 9)
    test_comp.program([2,6])
    test_comp.run_one_step()
    assert test_comp.B == 1

def test_program2():
    test_comp = day17.Computer(10, None, None)
    test_comp.program([5,0,5,1,5,4])
    test_comp.run_one_step()
    test_comp.run_one_step()
    test_comp.run_one_step()
    assert test_comp.output == [0,1,2]

    test_comp = day17.Computer(10, None, None)
    test_comp.program([5,0,5,1,5,4])
    test_comp.run()
    assert test_comp.output == [0,1,2]

def test_program3():
    test_comp = day17.Computer(2024, None, None)
    test_comp.program([0,1,5,4,3,0])
    test_comp.run()
    assert test_comp.output == [4,2,5,6,7,7,7,7,3,1,0]
    assert test_comp.A == 0

def test_program4():
    test_comp = day17.Computer(None, 29, None)
    test_comp.program([1,7])
    test_comp.run()
    assert test_comp.B == 26

def test_program5():
    '''If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.'''
    test_comp = day17.Computer(None, 2024, 43690)
    test_comp.program([4,0])
    test_comp.run()
    assert test_comp.B == 44354

sample_input = ['Register A: 729',
                'Register B: 0',
                'Register C: 0',
                '',
                'Program: 0,1,5,4,3,0']
def test_sample_input():
    sample_comp = day17.parse_input(sample_input)
    sample_comp.run()
    print(sample_comp.output)
    assert sample_comp.output == [4,6,3,5,6,3,5,2,1,0]

