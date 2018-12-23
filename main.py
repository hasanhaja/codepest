from solutions import solution1
from solutions import solution2
from solutions import solution3

def test(boolean_condition):
    # System.out.println("Input " + (count++) + ": " + (result ? "OK" : "FAIL!"));
    if boolean_condition:
        print("OK")
    else:
        print("FAILED!")

def challenge1():
    print("x------------Challenge 1------------x")
    test(solution1(1, 2, 3) == 4)
    test(solution1(1, 5, 8) == 11)
    test(solution1(2, 6, 9) == 12)
    print("x----------END OF CHALLENGE----------x")

def challenge2():
    print("x------------Challenge 2------------x")
    test(solution2(["a", "b", "c"]) == 3)
    test(solution2(["a", "a", "b", "b", "c"]) == 3)
    test(solution2(["a", "b", "c", "d", "d"]) == 4)
    print("x----------END OF CHALLENGE----------x")

def challenge3():
    print("x------------Challenge 3------------x")
    test(solution3(["a", "b", "c"], ["a", "b", "c"]) == 0)
    test(solution3(["a", "b", "c"], ["b", "c", "d"]) == 2)
    test(solution3(["a", "c", "f"], ["a", "b", "d"]) == 4)
    print("x----------END OF CHALLENGE----------x")

def main():

    challenge1()
    challenge2()

if __name__ == '__main__':
    main()